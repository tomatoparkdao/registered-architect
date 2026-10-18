#!/usr/bin/env python3
"""
建筑师传热系数（U 值）计算器
============================
计算简单墙体构造及复合立面构件的传热系数；复合立面可包含窗、门、阳台门，
以及线性/点状热桥。

立面模式会自动布置洞口，使窗间墙宽度相等、门洞两侧保持对称、窗台高度对齐，
并生成按比例绘制的 ASCII 立面图。

模式 1 —— 简单墙体构造：
  python uvalue_calculator.py --layers '[
    {"name":"砖墙","thickness_mm":102,"conductivity":0.77},
    {"name":"PIR 保温层","thickness_mm":100,"conductivity":0.022},
    {"name":"混凝土砌块","thickness_mm":100,"conductivity":0.15}
  ]'

模式 2 —— 复合立面（自动布局 + 热工计算）：
  python uvalue_calculator.py --facade '{
    "width": 7.0, "height": 3.0,
    "wall_layers": [
      {"name":"抹灰层","thickness_mm":15,"conductivity":0.50},
      {"name":"EPS","thickness_mm":150,"conductivity":0.034},
      {"name":"混凝土","thickness_mm":200,"conductivity":1.40},
      {"name":"石膏抹灰层","thickness_mm":13,"conductivity":0.16}
    ],
    "openings": [
      {"type":"window","name":"W1","width":1.2,"height":1.5,"u_value":1.2},
      {"type":"door","name":"D1 入户门","width":0.9,"height":2.1,"u_value":1.8},
      {"type":"window","name":"W2","width":1.2,"height":1.5,"u_value":1.2}
    ]
  }'

  洞口将按给定顺序从左至右布置，并自动计算相等的窗间墙宽度。门落地布置（sill=0），
  窗的默认窗台高度为 0.9m。可通过 "sill" 字段覆盖窗台高度。
"""

import argparse
import json
import math
import sys


# ============================================================================
# 常量
# ============================================================================

DEFAULT_PSI_WINDOW = 0.04
DEFAULT_PSI_DOOR = 0.06
DEFAULT_PSI_BALCONY_DOOR = 0.05

MIN_PIER_STRUCTURAL = 0.20   # 结构绝对最小值（m）
MIN_PIER_THERMAL = 0.40      # 避免严重热桥的最小值（m）
MIN_PIER_RECOMMENDED = 0.60  # 良好实践建议值（m）

DEFAULT_SILL_WINDOW = 0.90   # 距楼地面高度（m）
DEFAULT_SILL_DOOR = 0.00     # 地面标高

COMPLIANCE_TARGETS = {
    "passive_house_wall": 0.15,
    "code_wall": 0.30,
}

DIAGRAM_TARGET_WIDTH = 74  # ASCII 图示宽度（字符数）


# ============================================================================
# 模式 1：简单墙体
# ============================================================================

def validate_layers(layers):
    errors = []
    if not layers:
        errors.append("至少需要一个构造层。")
        return errors
    for i, layer in enumerate(layers):
        label = f"第 {i + 1} 层"
        if "name" not in layer:
            errors.append(f"{label}：缺少 'name'。")
        if "thickness_mm" not in layer:
            errors.append(f"{label}：缺少 'thickness_mm'。")
        elif layer["thickness_mm"] <= 0:
            errors.append(f"{label}：thickness_mm 必须为正数。")
        if "conductivity" not in layer:
            errors.append(f"{label}：缺少 'conductivity'。")
        elif layer["conductivity"] <= 0:
            errors.append(f"{label}：conductivity 必须为正数。")
    return errors


def calculate_wall_uvalue(layers, rsi_internal, rsi_external):
    layer_results = []
    total_r = rsi_internal
    for layer in layers:
        thickness_m = layer["thickness_mm"] / 1000.0
        r_value = thickness_m / layer["conductivity"]
        total_r += r_value
        layer_results.append({
            "name": layer["name"],
            "thickness_mm": layer["thickness_mm"],
            "conductivity": round(layer["conductivity"], 4),
            "r_value": round(r_value, 4),
        })
    total_r += rsi_external
    u_value = 1.0 / total_r
    return {
        "layers": layer_results,
        "rsi_internal": round(rsi_internal, 4),
        "rsi_external": round(rsi_external, 4),
        "total_r_value": round(total_r, 4),
        "u_value": round(u_value, 4),
        "total_thickness_mm": sum(l["thickness_mm"] for l in layers),
    }


# ============================================================================
# 模式 2：立面布局引擎
# ============================================================================

def expand_openings(openings):
    """将 count>1 展开为独立洞口，并保留输入顺序。"""
    expanded = []
    for op in openings:
        count = op.get("count", 1)
        for i in range(count):
            item = dict(op)
            item.pop("count", None)
            if count > 1:
                base = op.get("name", op["type"])
                item["name"] = f"{base} #{i+1}"
            expanded.append(item)
    return expanded


def generate_layout(facade_width, facade_height, openings):
    """
    按从左至右顺序布置洞口，并使窗间墙宽度相等。

    规则：
    - 洞口按输入顺序布置（由用户控制构图）
    - 所有窗间墙宽度（洞口之间及边缘处的间距）相等
    - 门：除非另行指定，sill = 0.0m（地面标高）
    - 窗：除非另行指定，sill = 0.9m
    - 阳台门：除非另行指定，sill = 0.0m
    - 校验窗间墙宽度是否过窄，以及洞口是否能够容纳于立面内

    返回：
        positioned：新增 'x'、'sill'、'x_center' 字段的字典列表
        pier_width：相等的窗间墙宽度（米）
        piers：包含 'x'、'width'、'label' 的窗间墙字典列表
    """
    expanded = expand_openings(openings)

    total_opening_width = sum(o["width"] for o in expanded)
    remaining = facade_width - total_opening_width
    n_piers = len(expanded) + 1
    pier_width = remaining / n_piers if n_piers > 0 else remaining

    # 分配位置
    x = pier_width
    piers = []
    # 左侧边缘窗间墙
    piers.append({
        "label": "pier",
        "x": 0.0,
        "width": round(pier_width, 4),
    })

    for i, op in enumerate(expanded):
        # 设置窗台高度
        if "sill" not in op:
            if op["type"] in ("door", "balcony_door"):
                op["sill"] = DEFAULT_SILL_DOOR
            else:
                op["sill"] = DEFAULT_SILL_WINDOW

        op["x"] = round(x, 4)
        op["x_center"] = round(x + op["width"] / 2, 4)
        op["head"] = round(op["sill"] + op["height"], 4)

        x_after = x + op["width"]

        # 此洞口后的窗间墙
        piers.append({
            "label": "pier",
            "x": round(x_after, 4),
            "width": round(pier_width, 4),
        })

        x = x_after + pier_width

    return expanded, round(pier_width, 4), piers


def draw_facade_elevation(facade_width, facade_height, positioned, pier_width):
    """
    生成按比例绘制的 ASCII 立面图。

    图示中的字符宽度与实际尺寸成比例；墙体中的洞口以框线表示，并标注
    窗台高度、名称和尺寸。
    """
    scale = (DIAGRAM_TARGET_WIDTH - 2) / facade_width  # 每米对应的字符数（边框内）
    min_label_width = 3  # 任一元素的最小字符宽度

    # 构建元素序列：窗间墙、洞口、窗间墙、洞口……窗间墙
    elements = []
    x = 0.0
    for op in positioned:
        # 此洞口前的窗间墙
        op_x = op.get("x", op.get("x_m", 0))
        pw = op_x - x
        if pw > 0.001:
            elements.append({"type": "pier", "width_m": pw, "data": None})
        op_w = op.get("width", op.get("width_m", 0))
        elements.append({"type": "opening", "width_m": op_w, "data": op})
        x = op_x + op_w
    # 最后一段窗间墙
    pw = facade_width - x
    if pw > 0.001:
        elements.append({"type": "pier", "width_m": pw, "data": None})

    # 计算字符宽度
    raw_chars = []
    for el in elements:
        c = max(min_label_width, round(el["width_m"] * scale))
        raw_chars.append(c)

    # 调整至目标宽度
    total_c = sum(raw_chars)
    target = DIAGRAM_TARGET_WIDTH - 2  # 减去左右边框字符
    diff = target - total_c
    # 将差值分配给最宽的元素
    if diff != 0:
        sorted_indices = sorted(range(len(raw_chars)),
                                key=lambda i: raw_chars[i], reverse=True)
        for i in range(abs(diff)):
            idx = sorted_indices[i % len(sorted_indices)]
            raw_chars[idx] += 1 if diff > 0 else -1
            raw_chars[idx] = max(min_label_width, raw_chars[idx])

    char_widths = raw_chars

    lines = []
    lines.append(f"--- 立面图 ({facade_width:.1f}m × {facade_height:.1f}m) ---")
    lines.append("")

    # --- 顶部边框 ---
    top = "+"
    for cw in char_widths:
        top += "-" * cw + "+"
    lines.append("  " + top)

    # --- 上部墙体（洞口顶以上、立面顶部以下）---
    # 显示洞口类型标签
    row_type = "|"
    row_name = "|"
    row_size = "|"
    row_uval = "|"

    for i, el in enumerate(elements):
        cw = char_widths[i]
        if el["type"] == "pier":
            row_type += " " * cw + "|"
            row_name += " " * cw + "|"
            row_size += " " * cw + "|"
            row_uval += " " * cw + "|"
        else:
            op = el["data"]
            op_type = {
                "window": "窗",
                "door": "门",
                "balcony_door": "阳台门",
            }.get(op["type"], op["type"].upper().replace("_", " "))
            op_name = op.get("name", op["type"])
            w = op.get("width", op.get("width_m", 0))
            h = op.get("height", op.get("height_m", 0))
            size_str = f"{w:.1f}x{h:.1f}m"
            u_str = f"U={op['u_value']:.2f}"

            row_type += center_text(op_type, cw) + "|"
            row_name += center_text(op_name, cw) + "|"
            row_size += center_text(size_str, cw) + "|"
            row_uval += center_text(u_str, cw) + "|"

    lines.append("  " + row_type)
    lines.append("  " + row_name)
    lines.append("  " + row_size)
    lines.append("  " + row_uval)

    # --- 窗台线（窗止于此线，门延续至地面）---
    sill_row = "|"
    for i, el in enumerate(elements):
        cw = char_widths[i]
        if el["type"] == "pier":
            sill_row += " " * cw + "|"
        else:
            op = el["data"]
            sill = op.get("sill", op.get("sill_m", 0))
            if sill > 0.01:
                sill_str = f"窗台 {sill:.1f}m"
                sill_row += center_text(sill_str, cw) + "|"
            else:
                sill_row += center_text("（至地面）", cw) + "|"
    lines.append("  " + sill_row)

    # --- 窗台以下行（窗下为墙体，门洞仍为空）---
    below = "|"
    for i, el in enumerate(elements):
        cw = char_widths[i]
        if el["type"] == "pier":
            below += " " * cw + "|"
        else:
            op = el["data"]
            sill2 = op.get("sill", op.get("sill_m", 0))
            if sill2 > 0.01:
                below += center_text("[墙体]", cw) + "|"
            else:
                below += " " * cw + "|"
    lines.append("  " + below)

    # --- 底部边框 ---
    bot = "+"
    for cw in char_widths:
        bot += "-" * cw + "+"
    lines.append("  " + bot)

    # --- 尺寸线 ---
    dim_row = " "
    for i, el in enumerate(elements):
        cw = char_widths[i]
        if el["type"] == "pier":
            dim_str = f"{el['width_m']:.2f}"
        else:
            dim_str = f"{el['width_m']:.2f}"
        dim_row += center_text(dim_str, cw + 1)
    lines.append("  " + dim_row)

    # --- 标签行 ---
    label_row = " "
    for i, el in enumerate(elements):
        cw = char_widths[i]
        if el["type"] == "pier":
            label_row += center_text("窗间墙", cw + 1)
        else:
            op = el["data"]
            label_row += center_text(op.get("name", op["type"]), cw + 1)
    lines.append("  " + label_row)

    lines.append("")
    lines.append(f"  等宽窗间墙：{pier_width:.2f}m")

    # 窗间墙质量评估
    if pier_width < MIN_PIER_STRUCTURAL:
        lines.append(f"  !! 严重：窗间墙 {pier_width:.2f}m < {MIN_PIER_STRUCTURAL}m "
                     "结构最小值。洞口无法容纳。")
    elif pier_width < MIN_PIER_THERMAL:
        lines.append(f"  ! 警告：窗间墙 {pier_width:.2f}m < {MIN_PIER_THERMAL}m。"
                     "窗间墙处热桥严重。请加宽墙体或缩小洞口。")
    elif pier_width < MIN_PIER_RECOMMENDED:
        lines.append(f"  提示：窗间墙 {pier_width:.2f}m < 建议值 {MIN_PIER_RECOMMENDED}m。"
                     "建议加宽以改善热工性能和立面比例。")
    else:
        lines.append(f"  窗间墙宽度合格（建议最小值 ≥ {MIN_PIER_RECOMMENDED}m）")

    return "\n".join(lines)


def center_text(text, width):
    """在指定字符宽度内居中文本；必要时截断。"""
    if len(text) > width:
        text = text[:width]
    return text.center(width)


# ============================================================================
# 模式 2：立面热工计算
# ============================================================================

def validate_facade(facade):
    errors = []
    if "width" not in facade or facade["width"] <= 0:
        errors.append("立面的 'width' 必须为正数（米）。")
    if "height" not in facade or facade["height"] <= 0:
        errors.append("立面的 'height' 必须为正数（米）。")
    if "wall_layers" not in facade or not facade["wall_layers"]:
        errors.append("立面必须包含 'wall_layers' 数组。")
    else:
        errors.extend(validate_layers(facade["wall_layers"]))

    for i, op in enumerate(facade.get("openings", [])):
        label = f"第 {i + 1} 个洞口"
        if "type" not in op:
            errors.append(f"{label}：缺少 'type'（window/door/balcony_door）。")
        if "width" not in op or op["width"] <= 0:
            errors.append(f"{label}：'width' 必须为正数。")
        if "height" not in op or op["height"] <= 0:
            errors.append(f"{label}：'height' 必须为正数。")
        if "u_value" not in op or op["u_value"] <= 0:
            errors.append(f"{label}：'u_value' 必须为正数。")

    for i, tb in enumerate(facade.get("thermal_bridges", [])):
        label = f"第 {i + 1} 个热桥"
        if "psi" not in tb or tb["psi"] < 0:
            errors.append(f"{label}：'psi' 不得为负数。")
        if "length" not in tb or tb["length"] <= 0:
            errors.append(f"{label}：'length' 必须为正数。")

    return errors


def calculate_facade(facade, rsi_internal, rsi_external):
    """
    完整的复合立面分析：
    1. 自动布置洞口，并使窗间墙宽度相等
    2. 根据构造层计算不透明墙体的 U 值
    3. 按 ISO 13789 计算面积加权的综合 U 值
    4. 计算热桥贡献（洞口周边 + 用户自定义热桥）
    """
    fw = facade["width"]
    fh = facade["height"]
    total_area = fw * fh

    # --- 布局 ---
    positioned, pier_width, piers = generate_layout(
        fw, fh, facade.get("openings", [])
    )

    # --- 墙体 U 值 ---
    wall_result = calculate_wall_uvalue(
        facade["wall_layers"], rsi_internal, rsi_external
    )
    wall_u = wall_result["u_value"]

    # --- 处理已定位的洞口 ---
    opening_results = []
    total_opening_area = 0.0
    total_window_area = 0.0
    total_door_area = 0.0
    component_losses = []

    for op in positioned:
        op_type = op["type"]
        op_name = op.get("name", op_type)
        area = op["width"] * op["height"]
        perim = 2 * (op["width"] + op["height"])
        total_opening_area += area

        if op_type == "window":
            total_window_area += area
            default_psi = DEFAULT_PSI_WINDOW
        elif op_type == "balcony_door":
            total_window_area += area
            default_psi = DEFAULT_PSI_BALCONY_DOOR
        else:
            total_door_area += area
            default_psi = DEFAULT_PSI_DOOR

        psi = op.get("psi", default_psi)
        area_loss = op["u_value"] * area
        perim_loss = psi * perim

        opening_results.append({
            "name": op_name,
            "type": op_type,
            "x_m": op["x"],
            "sill_m": op["sill"],
            "width_m": op["width"],
            "height_m": op["height"],
            "area_m2": round(area, 2),
            "u_value": op["u_value"],
            "perimeter_m": round(perim, 2),
            "psi": psi,
            "loss_area_WK": round(area_loss, 3),
            "loss_perim_WK": round(perim_loss, 3),
            "loss_total_WK": round(area_loss + perim_loss, 3),
        })

        component_losses.append({"name": f"{op_name}（面积）", "WK": area_loss})
        component_losses.append({"name": f"{op_name}（周边）", "WK": perim_loss})

    opaque_area = total_area - total_opening_area
    if opaque_area < 0:
        opaque_area = 0.0
    opaque_loss = wall_u * opaque_area
    component_losses.insert(0, {"name": "不透明墙体", "WK": opaque_loss})

    # --- 用户自定义热桥 ---
    bridges = facade.get("thermal_bridges", [])
    bridge_results = []
    total_bridge_loss = 0.0
    for tb in bridges:
        loss = tb["psi"] * tb["length"]
        total_bridge_loss += loss
        bridge_results.append({
            "name": tb.get("name", "热桥"),
            "psi_WmK": tb["psi"],
            "length_m": tb["length"],
            "loss_WK": round(loss, 3),
        })
        component_losses.append({
            "name": f"{tb.get('name', '热桥')}（psi={tb['psi']}）",
            "WK": loss,
        })

    total_loss = sum(c["WK"] for c in component_losses)
    u_composite = total_loss / total_area if total_area > 0 else 0
    wwr = (total_window_area / total_area * 100) if total_area > 0 else 0

    loss_area_sum = sum(o["loss_area_WK"] for o in opening_results)
    loss_perim_sum = sum(o["loss_perim_WK"] for o in opening_results)

    def pct(v):
        return round(v / total_loss * 100, 1) if total_loss > 0 else 0

    return {
        "facade": {
            "width_m": fw,
            "height_m": fh,
            "total_area_m2": round(total_area, 2),
            "opaque_area_m2": round(opaque_area, 2),
            "opening_area_m2": round(total_opening_area, 2),
            "window_area_m2": round(total_window_area, 2),
            "door_area_m2": round(total_door_area, 2),
            "wwr_pct": round(wwr, 1),
        },
        "layout": {
            "pier_width_m": pier_width,
            "pier_count": len(piers),
            "openings_positioned": opening_results,
            "piers": piers,
        },
        "wall_buildup": wall_result,
        "openings": opening_results,
        "thermal_bridges": bridge_results,
        "heat_loss": {
            "wall_WK": round(opaque_loss, 3),
            "wall_pct": pct(opaque_loss),
            "openings_WK": round(loss_area_sum, 3),
            "openings_pct": pct(loss_area_sum),
            "perimeters_WK": round(loss_perim_sum, 3),
            "perimeters_pct": pct(loss_perim_sum),
            "bridges_WK": round(total_bridge_loss, 3),
            "bridges_pct": pct(total_bridge_loss),
            "total_WK": round(total_loss, 3),
        },
        "u_composite": round(u_composite, 4),
        "meets_passive_house": u_composite <= COMPLIANCE_TARGETS["passive_house_wall"],
        "meets_code": u_composite <= COMPLIANCE_TARGETS["code_wall"],
    }


# ============================================================================
# 输出格式化
# ============================================================================

def format_simple_output(result):
    lines = [
        "=== 传热系数（U 值）计算器 —— 简单墙体构造 ===",
        f"{'构造层':<25} {'厚度(mm)':>10} {'导热系数(W/mK)':>12} {'R(m2K/W)':>12}",
        "-" * 62,
        f"{'Rsi（内表面）':<25} {'--':>10} {'--':>12} {result['rsi_internal']:>12.4f}",
    ]
    for layer in result["layers"]:
        lines.append(
            f"{layer['name']:<25} {layer['thickness_mm']:>10} "
            f"{layer['conductivity']:>12.4f} {layer['r_value']:>12.4f}"
        )
    lines.extend([
        f"{'Rse（外表面）':<25} {'--':>10} {'--':>12} {result['rsi_external']:>12.4f}",
        "-" * 62,
        f"总厚度：           {result['total_thickness_mm']:,} mm",
        f"总热阻 R 值：      {result['total_r_value']:.4f} m2K/W",
        f"传热系数 U 值：    {result['u_value']:.4f} W/m2K",
        "",
        f"被动房（墙体）：0.15 W/m2K —— "
        f"{'符合' if result['u_value'] <= 0.15 else '不符合'}",
        f"常见规范限值（墙体）：0.30 W/m2K —— "
        f"{'符合' if result['u_value'] <= 0.30 else '不符合'}",
    ])
    return "\n".join(lines)


def format_facade_output(result):
    f = result["facade"]
    wb = result["wall_buildup"]
    hl = result["heat_loss"]
    layout = result["layout"]
    pier_w = layout["pier_width_m"]

    lines = []

    # --- 立面图 ---
    diagram = draw_facade_elevation(
        f["width_m"], f["height_m"],
        layout["openings_positioned"], pier_w
    )
    lines.append(diagram)

    # --- 几何汇总 ---
    lines.extend([
        "",
        "=" * 72,
        "  复合立面热工分析",
        "=" * 72,
        "",
        "--- 几何信息 ---",
        f"  立面：             {f['width_m']:.1f}m × {f['height_m']:.1f}m = {f['total_area_m2']:.2f} m2",
        f"  不透明墙体：       {f['opaque_area_m2']:.2f} m2 ({f['opaque_area_m2']/f['total_area_m2']*100:.1f}%)",
        f"  洞口：             {f['opening_area_m2']:.2f} m2 ({f['opening_area_m2']/f['total_area_m2']*100:.1f}%)",
        f"  窗墙比 WWR：       {f['wwr_pct']:.1f}%",
        f"  窗间墙宽度：       {pier_w:.2f}m（共 {layout['pier_count']} 段）",
    ])

    # --- 墙体构造 ---
    lines.extend([
        "",
        "--- 不透明墙体构造 ---",
        f"  {'构造层':<20} {'厚度':>7} {'导热系数':>10} {'R 值':>10}",
        f"  {'-'*49}",
        f"  {'Rsi（内表面）':<20} {'--':>7} {'--':>10} {wb['rsi_internal']:>10.4f}",
    ])
    for layer in wb["layers"]:
        lines.append(
            f"  {layer['name']:<20} {str(layer['thickness_mm'])+'mm':>7} "
            f"{layer['conductivity']:>10.4f} {layer['r_value']:>10.4f}"
        )
    lines.extend([
        f"  {'Rse（外表面）':<20} {'--':>7} {'--':>10} {wb['rsi_external']:>10.4f}",
        f"  {'-'*49}",
        f"  墙体 U 值：{wb['u_value']:.4f} W/m2K  |  "
        f"厚度：{wb['total_thickness_mm']}mm",
    ])

    # --- 洞口表 ---
    if result["openings"]:
        lines.extend([
            "",
            "--- 洞口（按从左至右定位，周边 psi 自动识别）---",
            f"  {'名称':<18} {'类型':<13} {'x(m)':>5} {'尺寸':>9} "
            f"{'窗台':>5} {'U':>5} {'损失':>8}",
            f"  {'-'*67}",
        ])
        for op in result["openings"]:
            lines.append(
                f"  {op['name']:<18} "
                f"{{'window': '窗', 'door': '门', 'balcony_door': '阳台门'}.get(op['type'], op['type']):<13} "
                f"{op['x_m']:>5.2f} "
                f"{op['width_m']:.1f}x{op['height_m']:.1f}m "
                f"{op['sill_m']:>4.1f}m "
                f"{op['u_value']:>5.2f} "
                f"{op['loss_total_WK']:>7.2f}W/K"
            )

    # --- 热桥 ---
    if result["thermal_bridges"]:
        lines.extend([
            "",
            "--- 附加热桥 ---",
            f"  {'名称':<28} {'psi(W/mK)':>10} {'长度':>8} {'损失':>10}",
            f"  {'-'*58}",
        ])
        for tb in result["thermal_bridges"]:
            lines.append(
                f"  {tb['name']:<28} {tb['psi_WmK']:>10.3f} "
                f"{tb['length_m']:>7.1f}m {tb['loss_WK']:>9.3f}W/K"
            )

    # --- 热损失分项 ---
    lines.extend([
        "",
        "--- 热损失分项 ---",
        f"  不透明墙体：         {hl['wall_WK']:>8.2f} W/K  ({hl['wall_pct']:>5.1f}%)",
        f"  洞口（面积）：       {hl['openings_WK']:>8.2f} W/K  ({hl['openings_pct']:>5.1f}%)",
        f"  洞口周边：           {hl['perimeters_WK']:>8.2f} W/K  ({hl['perimeters_pct']:>5.1f}%)",
        f"  附加热桥：           {hl['bridges_WK']:>8.2f} W/K  ({hl['bridges_pct']:>5.1f}%)",
        f"  {'-'*42}",
        f"  合计：               {hl['total_WK']:>8.2f} W/K  (100.0%)",
    ])

    # --- 结果 ---
    lines.extend([
        "",
        "=" * 72,
        f"  综合 U 值：          {result['u_composite']:.4f} W/m2K",
        f"  （按 ISO 13789 面积加权计算，含全部热桥）",
        "=" * 72,
        "",
        f"  被动房：0.15 —— "
        f"{'符合' if result['meets_passive_house'] else '不符合'}",
        f"  规范目标：0.30 —— "
        f"{'符合' if result['meets_code'] else '不符合'}",
    ])

    # --- 建议 ---
    lines.append("")
    lines.append("--- 建议 ---")

    if f["wwr_pct"] > 40:
        lines.append(
            f"  ! 窗墙比 WWR={f['wwr_pct']:.0f}% 超过 40%。"
            "请减少玻璃面积或升级为三玻系统。"
        )

    worst_op = max(result["openings"], key=lambda o: o["loss_total_WK"],
                   default=None)
    if worst_op:
        savings = worst_op["area_m2"] * 0.4
        lines.append(
            f"  热损失最大的洞口：{worst_op['name']} "
            f"（{worst_op['loss_total_WK']:.2f} W/K）。"
            f"将 U 值改善 0.4 可节省 {savings:.1f} W/K。"
        )

    worst_tb = max(result["thermal_bridges"],
                   key=lambda t: t["loss_WK"], default=None)
    if worst_tb and worst_tb["psi_WmK"] > 0.10:
        lines.append(
            f"  最不利热桥：{worst_tb['name']} "
            f"（psi={worst_tb['psi_WmK']:.2f}，{worst_tb['loss_WK']:.2f} W/K）。"
            "建议采用隔热断桥连接件。"
        )

    return "\n".join(lines)


# ============================================================================
# 主程序
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="带立面布局引擎的传热系数（U 值）计算器。",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
模式 1 —— 简单墙体：
  %(prog)s --layers '[{"name":"砖墙","thickness_mm":102,"conductivity":0.77}]'

模式 2 —— 自动布局的复合立面：
  %(prog)s --facade '{
    "width":7,"height":3,
    "wall_layers":[{"name":"EPS 保温层","thickness_mm":150,"conductivity":0.034}],
    "openings":[
      {"type":"window","name":"W1","width":1.2,"height":1.5,"u_value":1.2},
      {"type":"door","name":"D1","width":0.9,"height":2.1,"u_value":1.8},
      {"type":"window","name":"W2","width":1.2,"height":1.5,"u_value":1.2}
    ]
  }'

  洞口按列出顺序从左至右布置。
  自动计算相等的窗间墙宽度。
  门的默认 sill=0（地面），窗的默认 sill=0.9m。
  可在每个洞口中通过 "sill" 字段覆盖。

  洞口类型：window、door、balcony_door
  添加 "count":N 可重复一个洞口（展开为 N 个独立实例）。
  添加 "psi":value 可覆盖洞口周边热桥 psi。

  热桥（用户自定义）：
    "thermal_bridges": [{"name":"阳台板","psi":0.50,"length":3.6}]
        """,
    )

    parser.add_argument("--layers", type=str, default=None)
    parser.add_argument("--facade", type=str, default=None)
    parser.add_argument("--rsi-internal", type=float, default=0.13)
    parser.add_argument("--rsi-external", type=float, default=0.04)
    parser.add_argument("--json", action="store_true")

    args = parser.parse_args()

    if args.rsi_internal < 0 or args.rsi_external < 0:
        print("错误：表面热阻不得为负数。", file=sys.stderr)
        sys.exit(1)

    if args.facade and args.layers:
        print("错误：请使用 --layers 或 --facade，不能同时使用。", file=sys.stderr)
        sys.exit(1)

    if not args.facade and not args.layers:
        print("错误：请提供 --layers 或 --facade。使用 --help 查看帮助。", file=sys.stderr)
        sys.exit(1)

    # --- 模式 1 ---
    if args.layers:
        try:
            layers = json.loads(args.layers)
        except json.JSONDecodeError as e:
            print(f"错误：JSON 无效：{e}", file=sys.stderr)
            sys.exit(1)
        if not isinstance(layers, list):
            print("错误：--layers 必须是 JSON 数组。", file=sys.stderr)
            sys.exit(1)
        errors = validate_layers(layers)
        if errors:
            for e in errors:
                print(f"错误：{e}", file=sys.stderr)
            sys.exit(1)

        result = calculate_wall_uvalue(layers, args.rsi_internal, args.rsi_external)
        if args.json:
            result["meets_passive_house"] = result["u_value"] <= 0.15
            result["meets_code"] = result["u_value"] <= 0.30
            print(json.dumps(result, indent=2))
        else:
            print(format_simple_output(result))

    # --- 模式 2 ---
    elif args.facade:
        try:
            facade = json.loads(args.facade)
        except json.JSONDecodeError as e:
            print(f"错误：JSON 无效：{e}", file=sys.stderr)
            sys.exit(1)
        if not isinstance(facade, dict):
            print("错误：--facade 必须是 JSON 对象。", file=sys.stderr)
            sys.exit(1)

        errors = validate_facade(facade)
        if errors:
            for e in errors:
                print(f"错误：{e}", file=sys.stderr)
            sys.exit(1)

        # 检查洞口是否能够容纳
        total_op_w = sum(
            o["width"] * o.get("count", 1)
            for o in facade.get("openings", [])
        )
        if total_op_w >= facade["width"]:
            print(f"错误：洞口总宽度（{total_op_w:.2f}m）≥ "
                  f"立面宽度（{facade['width']:.2f}m）。", file=sys.stderr)
            sys.exit(1)

        result = calculate_facade(facade, args.rsi_internal, args.rsi_external)

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(format_facade_output(result))


if __name__ == "__main__":
    main()
