#!/usr/bin/env python3
"""
采光系数计算器

采用 BRE 简化公式估算单侧采光房间的平均采光系数：

    DF = (Aw * T * theta) / (A_total * (1 - R^2)) * 100

其中：
    Aw      = 窗洞口净玻璃面积（m2）
    T       = 玻璃透光率
    theta   = 可见天空角系数（0.0 - 1.0）
    A_total = 房间所有表面的总面积（m2）
    R       = 房间表面的面积加权平均反射率

用法：
    python daylight_calculator.py --room-width 4 --room-depth 6 --room-height 3 \\
        --window-width 2.5 --window-height 1.8 --window-sill-height 0.9
    python daylight_calculator.py --room-width 4 --room-depth 6 --room-height 3 \\
        --window-width 2.5 --window-height 1.8 --window-sill-height 0.9 --json
"""

import argparse
import json
import math
import sys

from _support import AGENT_HINT, build_parser


def validate_inputs(args):
    """校验全部输入参数。"""
    errors = []
    if args.room_width <= 0:
        errors.append("房间宽度必须为正数。")
    if args.room_depth <= 0:
        errors.append("房间进深必须为正数。")
    if args.room_height <= 0:
        errors.append("房间高度必须为正数。")
    if args.window_width <= 0:
        errors.append("窗宽必须为正数。")
    if args.window_height <= 0:
        errors.append("窗高必须为正数。")
    if args.window_sill_height < 0:
        errors.append("窗台高度不得为负数。")
    if args.window_sill_height + args.window_height > args.room_height:
        errors.append("窗顶高度（窗台高度加窗高）超过房间高度。")
    if args.window_width > args.room_width:
        errors.append("窗宽超过房间宽度。")
    if not (0.0 < args.glazing_transmittance <= 1.0):
        errors.append("玻璃透光率必须大于 0.0 且小于或等于 1.0。")
    if not (0.0 < args.average_reflectance < 1.0):
        errors.append("平均反射率必须大于 0.0 且小于 1.0。")
    return errors


def calculate(args):
    """执行采光系数计算。"""
    # 窗面积
    window_area = args.window_width * args.window_height

    # 房间表面总面积
    floor_area = args.room_width * args.room_depth
    ceiling_area = floor_area
    wall_long = 2 * (args.room_depth * args.room_height)
    wall_short = 2 * (args.room_width * args.room_height)
    total_surface_area = floor_area + ceiling_area + wall_long + wall_short

    # 窗地比
    window_to_floor = (window_area / floor_area) * 100

    # 可见天空角计算
    # 从窗中部至远端墙体顶部障碍物的角度
    window_head = args.window_sill_height + args.window_height
    window_mid = args.window_sill_height + args.window_height / 2
    theta_rad = math.atan2(window_head, args.room_depth)
    theta_deg = math.degrees(theta_rad)
    theta_factor = theta_deg / 90.0

    # BRE 采光系数公式
    r = args.average_reflectance
    denominator = total_surface_area * (1 - r * r)

    if denominator <= 0:
        daylight_factor = 0.0
    else:
        daylight_factor = (window_area * args.glazing_transmittance * theta_factor) / denominator * 100

    # 评价
    if daylight_factor >= 5.0:
        assessment = "优秀（自然采光充足）"
    elif daylight_factor >= 2.0:
        assessment = "满足要求（可居住房间目标值 >= 2.0%）"
    elif daylight_factor >= 1.0:
        assessment = "临界（低于可居住房间 2.0% 目标值）"
    else:
        assessment = "不足（需补充人工照明）"

    return {
        "room_width_m": round(args.room_width, 2),
        "room_depth_m": round(args.room_depth, 2),
        "room_height_m": round(args.room_height, 2),
        "window_width_m": round(args.window_width, 2),
        "window_height_m": round(args.window_height, 2),
        "window_sill_height_m": round(args.window_sill_height, 2),
        "window_area_m2": round(window_area, 2),
        "floor_area_m2": round(floor_area, 2),
        "total_surface_area_m2": round(total_surface_area, 2),
        "window_to_floor_ratio_pct": round(window_to_floor, 2),
        "glazing_transmittance": round(args.glazing_transmittance, 2),
        "average_reflectance": round(args.average_reflectance, 2),
        "visible_sky_angle_deg": round(theta_deg, 1),
        "sky_angle_factor": round(theta_factor, 4),
        "daylight_factor_pct": round(daylight_factor, 2),
        "assessment": assessment,
    }


def format_output(result):
    """将结果格式化为便于阅读的输出。"""
    lines = [
        "=== 采光系数计算器 ===",
        f"房间：    宽 {result['room_width_m']:.2f}m x 进深 {result['room_depth_m']:.2f}m x 高 {result['room_height_m']:.2f}m",
        f"窗：      宽 {result['window_width_m']:.2f}m x 高 {result['window_height_m']:.2f}m（窗台高 {result['window_sill_height_m']:.2f}m）",
        "---------------------------------------",
        f"窗面积：                {result['window_area_m2']:.2f} m2",
        f"地面面积：              {result['floor_area_m2']:.2f} m2",
        f"房间表面总面积：        {result['total_surface_area_m2']:.2f} m2",
        f"窗地比：                {result['window_to_floor_ratio_pct']:.2f}%",
        f"玻璃透光率：            {result['glazing_transmittance']:.2f}",
        f"平均反射率：            {result['average_reflectance']:.2f}",
        f"可见天空角：            {result['visible_sky_angle_deg']:.1f} 度",
        "---------------------------------------",
        f"平均采光系数：          {result['daylight_factor_pct']:.2f}%",
        "",
        f"评价：{result['assessment']}",
    ]
    return "\n".join(lines)


def main():
    parser = build_parser(
        description="采光系数计算器：采用 BRE 简化公式估算单侧采光房间的平均采光系数。"
    )
    parser.add_argument("--room-width", type=float, required=True,
                        help="房间宽度，单位为米")
    parser.add_argument("--room-depth", type=float, required=True,
                        help="房间进深（垂直于窗墙），单位为米")
    parser.add_argument("--room-height", type=float, required=True,
                        help="房间高度，单位为米")
    parser.add_argument("--window-width", type=float, required=True,
                        help="窗宽，单位为米")
    parser.add_argument("--window-height", type=float, required=True,
                        help="窗高，单位为米")
    parser.add_argument("--window-sill-height", type=float, required=True,
                        help="窗台距地面高度，单位为米")
    parser.add_argument("--glazing-transmittance", type=float, default=0.65,
                        help="玻璃可见光透射比，0-1（默认值：0.65）")
    parser.add_argument("--average-reflectance", type=float, default=0.50,
                        help="房间表面平均反射率，0-1（默认值：0.50）")
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
