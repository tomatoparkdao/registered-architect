#!/usr/bin/env python3
"""
结构荷载计算器

计算用于柱尺寸初步估算的竖向荷载：
  - 每层恒载和活载
  - 根据分担面积计算的每层总荷载
  - 多层建筑的累计柱荷载
  - 荷载组合值（按 ASCE 7 / IBC 的 1.2D + 1.6L）
  - 钢筋混凝土柱初步尺寸

用法：
    python structural_load_calculator.py --tributary-area 36 --num-floors 8
    python structural_load_calculator.py --tributary-area 36 --num-floors 8 --occupancy-type office --json
"""

import argparse
import json
import math
import sys


# 按使用类型划分的典型活载（kN/m2）
LIVE_LOADS = {
    "residential":  {"load": 1.9, "name": "住宅"},
    "office":       {"load": 2.4, "name": "办公"},
    "retail":       {"load": 4.8, "name": "零售（首层）"},
    "assembly":     {"load": 4.8, "name": "集会"},
    "storage":      {"load": 6.0, "name": "仓储（轻型）"},
    "parking":      {"load": 2.4, "name": "停车库"},
    "hospital":     {"load": 3.8, "name": "医院"},
    "school":       {"load": 1.9, "name": "学校／教室"},
    "hotel":        {"load": 1.9, "name": "酒店客房"},
    "library":      {"load": 7.2, "name": "图书馆书库"},
    "industrial":   {"load": 6.0, "name": "轻型工业"},
}


def validate_inputs(args):
    """校验全部输入参数。"""
    errors = []
    if args.tributary_area <= 0:
        errors.append("分担面积必须为正数。")
    if args.num_floors < 1:
        errors.append("层数至少为 1。")
    if args.dead_load <= 0:
        errors.append("恒载必须为正数。")
    occ = args.occupancy_type.lower()
    if occ not in LIVE_LOADS and args.live_load is None:
        valid = ", ".join(sorted(LIVE_LOADS.keys()))
        errors.append(f"未知使用类型“{args.occupancy_type}”。"
                      f"有效类型：{valid}。"
                      f"或直接指定 --live-load。")
    if args.live_load is not None and args.live_load <= 0:
        errors.append("活载必须为正数。")
    return errors


def calculate(args):
    """执行结构荷载计算。"""
    occ = args.occupancy_type.lower()

    # 确定活载
    if args.live_load is not None:
        live_load = args.live_load
        occ_name = "用户指定"
    elif occ in LIVE_LOADS:
        live_load = LIVE_LOADS[occ]["load"]
        occ_name = LIVE_LOADS[occ]["name"]
    else:
        live_load = 2.4  # 默认采用办公活载
        occ_name = "默认值（办公）"

    dead_load = args.dead_load
    total_per_floor = dead_load + live_load

    # 每层荷载
    load_per_floor = args.tributary_area * total_per_floor

    # 柱总荷载（未组合）
    total_column_load = load_per_floor * args.num_floors

    # 荷载组合值（ASCE 7 LRFD：1.2D + 1.6L）
    factored_per_floor = args.tributary_area * (1.2 * dead_load + 1.6 * live_load)
    factored_total = factored_per_floor * args.num_floors

    # 柱初步尺寸（钢筋混凝土）
    # 假定 fc' = 35 MPa，箍筋柱 phi = 0.65
    # Pu = phi * 0.80 * (0.85 * fc' * Ag + fy * Ast)
    # 简化式：Ag_required = Pu / (0.4 * fc')
    fc_prime = 35.0  # MPa
    ag_required_mm2 = (factored_total * 1000) / (0.4 * fc_prime)  # convert kN to N
    column_dim_mm = math.ceil(math.sqrt(ag_required_mm2) / 50) * 50  # round up to 50mm

    # 最小柱截面尺寸
    column_dim_mm = max(column_dim_mm, 300)

    # 分担面积尺寸（假定为正方形）
    trib_dim = math.sqrt(args.tributary_area)

    return {
        "tributary_area_m2": round(args.tributary_area, 2),
        "tributary_dimension_m": round(trib_dim, 2),
        "num_floors": args.num_floors,
        "occupancy_type": occ_name,
        "dead_load_kN_m2": round(dead_load, 2),
        "live_load_kN_m2": round(live_load, 2),
        "total_load_kN_m2": round(total_per_floor, 2),
        "load_per_floor_kN": round(load_per_floor, 2),
        "total_column_load_kN": round(total_column_load, 2),
        "factored_load_kN": round(factored_total, 2),
        "factored_load_formula": "1.2D + 1.6L",
        "preliminary_column_mm": column_dim_mm,
        "preliminary_column_desc": f"~{column_dim_mm}x{column_dim_mm} mm RC (fc'={fc_prime:.0f} MPa)",
        "concrete_strength_MPa": fc_prime,
        "ag_required_mm2": round(ag_required_mm2),
    }


def format_output(result):
    """将结果格式化为便于阅读的输出。"""
    lines = [
        "=== 结构荷载计算器 ===",
        f"分担面积：          {result['tributary_area_m2']:,.2f} m2 "
        f"(~{result['tributary_dimension_m']:.1f}m x {result['tributary_dimension_m']:.1f}m)",
        f"层数：              {result['num_floors']}",
        f"使用类型：          {result['occupancy_type']}",
        "---------------------------------------",
        f"恒载：              {result['dead_load_kN_m2']:.2f} kN/m2／层",
        f"活载：              {result['live_load_kN_m2']:.2f} kN/m2／层",
        f"每层合计：          {result['total_load_kN_m2']:.2f} kN/m2",
        "---------------------------------------",
        f"每层荷载：          {result['load_per_floor_kN']:,.2f} kN",
        f"柱总荷载：          {result['total_column_load_kN']:,.2f} kN（{result['num_floors']} 层）",
        f"组合荷载：          {result['factored_load_kN']:,.2f} kN（{result['factored_load_formula']}）",
        "---------------------------------------",
        f"初步柱截面：        {result['preliminary_column_desc']}",
        f"所需 Ag：           {result['ag_required_mm2']:,.0f} mm2",
        "",
        "注：仅用于初步估算，仍须进行详细结构分析。",
        "柱尺寸假定为配筋率约 2% 的箍筋钢筋混凝土柱。",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="结构荷载计算器：计算分担面积竖向荷载和柱初步尺寸。"
    )
    parser.add_argument("--tributary-area", type=float, required=True,
                        help="柱分担面积，单位为 m2")
    parser.add_argument("--num-floors", type=int, required=True,
                        help="柱支承的楼层数")
    parser.add_argument("--dead-load", type=float, default=4.5,
                        help="每层恒载，单位为 kN/m2（钢筋混凝土楼板默认值：4.5）")
    parser.add_argument("--live-load", type=float, default=None,
                        help="活载，单位为 kN/m2（覆盖按使用类型确定的值）")
    parser.add_argument("--occupancy-type", type=str, default="office",
                        help="用于自动确定活载的使用类型 "
                             "(residential/office/retail/assembly/storage/parking/"
                             "hospital/school/hotel/library/industrial)")
    parser.add_argument("--json", action="store_true",
                        help="以 JSON 输出结果")

    args = parser.parse_args()

    errors = validate_inputs(args)
    if errors:
        for error in errors:
            print(f"错误：{error}", file=sys.stderr)
        sys.exit(1)

    result = calculate(args)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(format_output(result))


if __name__ == "__main__":
    main()
