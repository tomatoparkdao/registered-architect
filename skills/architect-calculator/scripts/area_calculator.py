#!/usr/bin/env python3
"""
面积与密度计算器

根据用地面积和容积率计算开发密度指标：
  - 根据用地面积和 FAR 计算总建筑面积（GFA）
  - 根据 GFA 和得房率计算净建筑面积（NGA）
  - 根据 NGA 和平均套型面积计算住宅套数
  - 根据套数和每户人数估算人口
  - 根据套数和停车配比计算所需停车位

用法：
    python area_calculator.py --site-area 5000 --far 2.5
    python area_calculator.py --site-area 5000 --far 2.5 --ntg-ratio 0.82 --json
"""

import argparse
import json
import math
import sys

from _support import AGENT_HINT, build_parser


def validate_inputs(args):
    """校验全部输入参数。"""
    errors = []
    if args.site_area <= 0:
        errors.append("用地面积必须为正数。")
    if args.far <= 0:
        errors.append("容积率（FAR）必须为正数。")
    if not (0.0 < args.ntg_ratio <= 1.0):
        errors.append("得房率必须大于 0.0 且小于或等于 1.0。")
    if args.avg_unit_size <= 0:
        errors.append("平均套型面积必须为正数。")
    if args.persons_per_unit <= 0:
        errors.append("每户人数必须为正数。")
    if args.parking_ratio < 0:
        errors.append("停车配比不得为负数。")
    return errors


def calculate(args):
    """执行面积和密度计算。"""
    gfa = args.site_area * args.far
    nga = gfa * args.ntg_ratio
    units = math.floor(nga / args.avg_unit_size)
    population = units * args.persons_per_unit
    parking = math.ceil(units * args.parking_ratio)

    return {
        "site_area_m2": round(args.site_area, 2),
        "far": round(args.far, 2),
        "gross_floor_area_m2": round(gfa, 2),
        "ntg_ratio": round(args.ntg_ratio, 2),
        "net_gross_area_m2": round(nga, 2),
        "avg_unit_size_m2": round(args.avg_unit_size, 2),
        "estimated_units": units,
        "persons_per_unit": round(args.persons_per_unit, 2),
        "estimated_population": round(population, 1),
        "parking_ratio": round(args.parking_ratio, 2),
        "parking_spaces": parking,
        "site_coverage_pct": round((gfa / args.far) / args.site_area * 100, 1)
            if args.far > 0 else 0,
        "density_units_per_hectare": round(units / (args.site_area / 10000), 1)
            if args.site_area > 0 else 0,
        "density_persons_per_hectare": round(population / (args.site_area / 10000), 1)
            if args.site_area > 0 else 0,
    }


def format_output(result):
    """将结果格式化为便于阅读的输出。"""
    lines = [
        "=== 面积与密度计算器 ===",
        f"用地面积：            {result['site_area_m2']:,.2f} m2",
        f"容积率：              {result['far']:.2f}",
        "---------------------------------------",
        f"总建筑面积：          {result['gross_floor_area_m2']:,.2f} m2",
        f"得房率：              {result['ntg_ratio']:.2f}",
        f"净建筑面积：          {result['net_gross_area_m2']:,.2f} m2",
        "---------------------------------------",
        f"平均套型面积：        {result['avg_unit_size_m2']:.2f} m2",
        f"估算套数：            {result['estimated_units']:,}",
        f"每户人数：            {result['persons_per_unit']:.2f}",
        f"估算人口：            {result['estimated_population']:,.0f}",
        "---------------------------------------",
        f"停车配比：            {result['parking_ratio']:.2f} 个车位/户",
        f"停车位数量：          {result['parking_spaces']:,}",
        "---------------------------------------",
        f"密度：                {result['density_units_per_hectare']:.1f} 户/公顷",
        f"                      {result['density_persons_per_hectare']:.1f} 人/公顷",
    ]
    return "\n".join(lines)


def main():
    parser = build_parser(
        description="面积与密度计算器：根据用地面积和 FAR 计算 GFA、NGA、套数、"
                    "人口和停车位。"
    )
    parser.add_argument("--site-area", type=float, required=True,
                        help="总用地面积，单位为 m2")
    parser.add_argument("--far", type=float, required=True,
                        help="容积率（地积比）")
    parser.add_argument("--ntg-ratio", type=float, default=0.80,
                        help="得房率（默认值：0.80）")
    parser.add_argument("--avg-unit-size", type=float, default=85.0,
                        help="住宅平均套型面积，单位为 m2（默认值：85）")
    parser.add_argument("--persons-per-unit", type=float, default=2.5,
                        help="每户平均人数（默认值：2.5）")
    parser.add_argument("--parking-ratio", type=float, default=1.0,
                        help="每户停车位数（默认值：1.0）")
    parser.add_argument("--json", action="store_true",
                        help="以 JSON 输出结果")

    args = parser.parse_args()

    errors = validate_inputs(args)
    if errors:
        for error in errors:
            print(f"错误：{error}", file=sys.stderr)
        print(AGENT_HINT, file=sys.stderr)
        sys.exit(1)

    result = calculate(args)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(format_output(result))


if __name__ == "__main__":
    main()
