#!/usr/bin/env python3
"""
疏散计算器

按《International Building Code》（IBC）计算疏散要求：
  - 根据楼层面积和人员荷载系数计算使用人数
  - 所需出口数量
  - 最小总出口宽度和每个出口宽度
  - 最大疏散距离
  - 合规性评价

用法：
    python egress_calculator.py --floor-area 800 --occupancy-type B --sprinklered
    python egress_calculator.py --floor-area 800 --occupancy-type B --num-stories 4 --json
"""

import argparse
import json
import math
import sys


# 人员荷载系数（m2/人）— IBC Table 1004.5
OCCUPANT_LOAD_FACTORS = {
    "A-1": {"factor": 1.5, "name": "集会场所（固定座席）", "net": True},
    "A-2": {"factor": 1.4, "name": "集会场所（餐饮）", "net": True},
    "A-3": {"factor": 1.9, "name": "集会场所（宗教礼拜/娱乐）", "net": True},
    "A-4": {"factor": 4.6, "name": "集会场所（站立）", "net": True},
    "A-5": {"factor": 1.4, "name": "集会场所（室外）", "net": True},
    "B":   {"factor": 9.3, "name": "商务办公", "net": False},
    "E":   {"factor": 1.9, "name": "教育场所", "net": True},
    "F-1": {"factor": 18.6, "name": "工厂（中等危险）", "net": False},
    "F-2": {"factor": 18.6, "name": "工厂（低危险）", "net": False},
    "H-1": {"factor": 9.3, "name": "高危险场所（爆炸）", "net": False},
    "H-2": {"factor": 9.3, "name": "高危险场所（快速燃烧）", "net": False},
    "H-3": {"factor": 9.3, "name": "高危险场所（物理危害）", "net": False},
    "I-1": {"factor": 18.6, "name": "机构场所（受监管）", "net": False},
    "I-2": {"factor": 22.3, "name": "机构场所（无自救能力）", "net": False},
    "I-3": {"factor": 11.1, "name": "机构场所（受约束）", "net": False},
    "M":   {"factor": 5.6, "name": "商业", "net": False},
    "R":   {"factor": 18.6, "name": "住宅", "net": False},
    "S-1": {"factor": 46.5, "name": "仓储（中等危险）", "net": False},
    "S-2": {"factor": 46.5, "name": "仓储（低危险）", "net": False},
    "U":   {"factor": 46.5, "name": "辅助用房", "net": False},
}

# 最大疏散距离（米）— IBC Table 1017.2
TRAVEL_DISTANCES = {
    "A-1": {"unsprinklered": 61.0, "sprinklered": 76.0},
    "A-2": {"unsprinklered": 61.0, "sprinklered": 76.0},
    "A-3": {"unsprinklered": 61.0, "sprinklered": 76.0},
    "A-4": {"unsprinklered": 61.0, "sprinklered": 76.0},
    "A-5": {"unsprinklered": 61.0, "sprinklered": 76.0},
    "B":   {"unsprinklered": 61.0, "sprinklered": 91.0},
    "E":   {"unsprinklered": 61.0, "sprinklered": 76.0},
    "F-1": {"unsprinklered": 61.0, "sprinklered": 76.0},
    "F-2": {"unsprinklered": 61.0, "sprinklered": 76.0},
    "H-1": {"unsprinklered": 23.0, "sprinklered": 23.0},
    "H-2": {"unsprinklered": 23.0, "sprinklered": 30.0},
    "H-3": {"unsprinklered": 23.0, "sprinklered": 30.0},
    "I-1": {"unsprinklered": 61.0, "sprinklered": 76.0},
    "I-2": {"unsprinklered": 46.0, "sprinklered": 61.0},
    "I-3": {"unsprinklered": 61.0, "sprinklered": 76.0},
    "M":   {"unsprinklered": 61.0, "sprinklered": 76.0},
    "R":   {"unsprinklered": 61.0, "sprinklered": 76.0},
    "S-1": {"unsprinklered": 61.0, "sprinklered": 76.0},
    "S-2": {"unsprinklered": 61.0, "sprinklered": 91.0},
    "U":   {"unsprinklered": 61.0, "sprinklered": 76.0},
}


def validate_inputs(args):
    """校验全部输入参数。"""
    errors = []
    if args.floor_area <= 0:
        errors.append("楼层面积必须为正数。")
    occ = args.occupancy_type.upper()
    if occ not in OCCUPANT_LOAD_FACTORS:
        valid = ", ".join(sorted(OCCUPANT_LOAD_FACTORS.keys()))
        errors.append(f"无效使用类型“{args.occupancy_type}”。"
                      f"有效类型：{valid}")
    if args.num_stories < 1:
        errors.append("建筑层数至少为 1。")
    return errors


def calculate(args):
    """执行疏散计算。"""
    occ = args.occupancy_type.upper()
    occ_info = OCCUPANT_LOAD_FACTORS[occ]
    occ_factor = occ_info["factor"]
    occ_name = occ_info["name"]

    # 使用人数
    occupant_load = math.ceil(args.floor_area / occ_factor)

    # 所需出口数量（IBC 1006.2）
    if occupant_load <= 500:
        num_exits = 2
    elif occupant_load <= 1000:
        num_exits = 3
    else:
        num_exits = 4

    # 特殊情况：特定使用类型且使用人数较少时允许单一出口
    # （简化处理，完整规范要求更细化）
    if occupant_load <= 49 and args.num_stories <= 1 and occ not in ("H-1", "H-2", "H-3"):
        num_exits = max(1, num_exits)
        # 多数情况下仍因安全原因要求 2 个出口
        if occupant_load > 10:
            num_exits = 2

    # 出口宽度计算
    # 楼梯宽度系数：7.6 mm/人；其他构件：5.1 mm/人
    if args.num_stories > 1:
        width_factor = 7.6  # 楼梯
    else:
        width_factor = 5.1  # 水平疏散构件

    if args.sprinklered:
        width_factor *= 0.75  # IBC 规定的喷淋减小系数

    total_exit_width_mm = math.ceil(occupant_load * width_factor)
    width_per_exit_mm = math.ceil(total_exit_width_mm / num_exits)

    # 最小门净宽
    min_door_width_mm = 813  # 32 inches clear

    # 取计算值和最小值中的较大者
    effective_width_per_exit = max(width_per_exit_mm, min_door_width_mm)

    # 疏散距离
    sprinkler_key = "sprinklered" if args.sprinklered else "unsprinklered"
    travel_info = TRAVEL_DISTANCES.get(occ, {"unsprinklered": 61.0, "sprinklered": 76.0})
    max_travel = travel_info[sprinkler_key]
    max_travel_ft = round(max_travel * 3.28084)

    # 共用疏散路径和尽端走道限值
    max_common_path = 23.0  # 75 ft default
    max_dead_end = 6.1  # 20 ft without sprinklers
    if args.sprinklered:
        max_dead_end = 15.0  # 50 ft with sprinklers

    # B、F、S 使用类型的共用疏散路径可更长
    if occ in ("B", "F-1", "F-2", "S-1", "S-2", "U"):
        max_common_path = 23.0 if not args.sprinklered else 30.0

    return {
        "floor_area_m2": round(args.floor_area, 2),
        "occupancy_type": occ,
        "occupancy_name": occ_name,
        "sprinklered": args.sprinklered,
        "num_stories": args.num_stories,
        "occupant_load_factor_m2": occ_factor,
        "occupant_load": occupant_load,
        "required_exits": num_exits,
        "total_exit_width_mm": total_exit_width_mm,
        "width_per_exit_mm": width_per_exit_mm,
        "min_door_width_mm": min_door_width_mm,
        "effective_width_per_exit_mm": effective_width_per_exit,
        "max_travel_distance_m": max_travel,
        "max_travel_distance_ft": max_travel_ft,
        "max_common_path_m": max_common_path,
        "max_dead_end_m": max_dead_end,
    }


def format_output(result):
    """将结果格式化为便于阅读的输出。"""
    lines = [
        "=== 疏散计算器 ===",
        f"楼层面积：          {result['floor_area_m2']:,.2f} m2",
        f"使用类型：          {result['occupancy_type']} ({result['occupancy_name']})",
        f"设有喷淋：          {'是' if result['sprinklered'] else '否'}",
        f"建筑层数：          {result['num_stories']}",
        "---------------------------------------",
        f"人员荷载系数：        {result['occupant_load_factor_m2']:.1f} m2/人",
        f"使用人数：            {result['occupant_load']:,} 人",
        "---------------------------------------",
        f"所需出口数量：        {result['required_exits']}",
        f"最小总出口宽度：      {result['total_exit_width_mm']:,} mm",
        f"每个出口宽度：        {result['width_per_exit_mm']:,} mm",
        f"最小门宽：            {result['min_door_width_mm']:,} mm（32 英寸）",
        f"每个出口有效宽度：    {result['effective_width_per_exit_mm']:,} mm",
        "---------------------------------------",
        f"最大疏散距离：        {result['max_travel_distance_m']:.1f} m "
        f"({result['max_travel_distance_ft']} ft) "
        f"[{'设有喷淋' if result['sprinklered'] else '未设喷淋'}]",
        f"最大共用路径：        {result['max_common_path_m']:.1f} m",
        f"最大尽端走道：        {result['max_dead_end_m']:.1f} m",
        "",
        "合规提示：应在平面图上对照以上限值复核疏散距离。",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="疏散计算器：按 IBC 计算使用人数、所需出口、出口宽度和疏散距离。"
    )
    parser.add_argument("--floor-area", type=float, required=True,
                        help="净楼层面积，单位为 m2")
    parser.add_argument("--occupancy-type", type=str, required=True,
                        help="IBC 使用分类（例如 A-1、B、E、M、R）")
    parser.add_argument("--sprinklered", action="store_true",
                        help="建筑设有自动喷水灭火系统")
    parser.add_argument("--num-stories", type=int, default=1,
                        help="建筑层数（默认值：1）")
    parser.add_argument("--json", action="store_true",
                        help="以 JSON 输出结果")

    args = parser.parse_args()

    errors = validate_inputs(args)
    if errors:
        for error in errors:
            print(f"错误：{error}", file=sys.stderr)
        sys.exit(1)

    # 将使用类型规范化为大写
    args.occupancy_type = args.occupancy_type.upper()

    result = calculate(args)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(format_output(result))


if __name__ == "__main__":
    main()
