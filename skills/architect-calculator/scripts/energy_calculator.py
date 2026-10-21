#!/usr/bin/env python3
"""
能耗计算器

采用度日法估算年度供暖和制冷能耗需求，考虑围护结构传热损失、通风损失和室内得热。

用法：
    python energy_calculator.py --floor-area 500 --envelope-area 800 \\
        --average-u-value 0.35 --heating-degree-days 3000 --cooling-degree-days 500
    python energy_calculator.py --floor-area 500 --envelope-area 800 \\
        --average-u-value 0.35 --heating-degree-days 3000 --cooling-degree-days 500 --json
"""

import argparse
import json
import sys

from _support import AGENT_HINT, build_parser


def validate_inputs(args):
    """校验全部输入参数。"""
    errors = []
    if args.floor_area <= 0:
        errors.append("建筑面积必须为正数。")
    if args.envelope_area <= 0:
        errors.append("围护结构面积必须为正数。")
    if args.average_u_value <= 0:
        errors.append("平均 U 值必须为正数。")
    if args.heating_degree_days < 0:
        errors.append("供暖度日数不得为负数。")
    if args.cooling_degree_days < 0:
        errors.append("制冷度日数不得为负数。")
    if args.ventilation_rate < 0:
        errors.append("通风率不得为负数。")
    if args.internal_gains < 0:
        errors.append("室内得热不得为负数。")
    return errors


def calculate(args):
    """采用度日法执行能耗需求计算。"""
    # 用于体积计算的假定层高
    ceiling_height = 3.0  # meters
    volume = args.floor_area * ceiling_height  # m3

    # 传热损失系数（W/K）
    transmission_coeff = args.average_u_value * args.envelope_area

    # 通风热损失系数（W/K）
    # Q_vent = 0.33 * n * V（其中 0.33 = rho_air * cp_air / 3600）
    ventilation_coeff = 0.33 * args.ventilation_rate * volume

    # 总热损失系数
    total_loss_coeff = transmission_coeff + ventilation_coeff

    # 年传热损失（kWh/年）
    # Q = HLC * HDD * 24 / 1000
    transmission_loss = transmission_coeff * args.heating_degree_days * 24 / 1000
    ventilation_loss = ventilation_coeff * args.heating_degree_days * 24 / 1000

    # 室内得热抵消量（kWh/年）
    # 假定供暖季室内得热可利用
    # 根据 HDD 估算供暖季小时数
    heating_season_hours = min(args.heating_degree_days / 10 * 24, 8760)
    internal_gains_annual = args.internal_gains * args.floor_area * heating_season_hours / 1000

    # 供暖需求
    heating_demand = max(0, transmission_loss + ventilation_loss - internal_gains_annual)

    # 制冷需求
    # 制冷季传热得热
    cooling_transmission = transmission_coeff * args.cooling_degree_days * 24 / 1000

    # 制冷季太阳得热和室内得热
    cooling_season_hours = min(args.cooling_degree_days / 5 * 24, 4380)
    internal_gains_cooling = args.internal_gains * args.floor_area * cooling_season_hours / 1000

    # 太阳得热估算（简化：制冷季约为建筑面积的 15 W/m2）
    solar_gain_rate = 15.0  # W/m2
    solar_gains = solar_gain_rate * args.floor_area * cooling_season_hours / 1000

    cooling_demand = max(0, cooling_transmission + internal_gains_cooling + solar_gains)

    # 总需求和 EUI
    total_demand = heating_demand + cooling_demand
    eui = total_demand / args.floor_area if args.floor_area > 0 else 0

    # 被动房目标核查
    heating_eui = heating_demand / args.floor_area if args.floor_area > 0 else 0
    cooling_eui = cooling_demand / args.floor_area if args.floor_area > 0 else 0
    meets_passive_house_heating = heating_eui <= 15.0
    meets_passive_house_cooling = cooling_eui <= 15.0

    # 单位建筑面积热损失
    specific_heat_loss = total_loss_coeff / args.floor_area if args.floor_area > 0 else 0

    return {
        "floor_area_m2": round(args.floor_area, 2),
        "envelope_area_m2": round(args.envelope_area, 2),
        "average_u_value_W_m2K": round(args.average_u_value, 4),
        "building_volume_m3": round(volume, 2),
        "heating_degree_days": round(args.heating_degree_days, 1),
        "cooling_degree_days": round(args.cooling_degree_days, 1),
        "ventilation_rate_ACH": round(args.ventilation_rate, 2),
        "internal_gains_W_m2": round(args.internal_gains, 2),
        "transmission_loss_coeff_W_K": round(transmission_coeff, 2),
        "ventilation_loss_coeff_W_K": round(ventilation_coeff, 2),
        "total_loss_coeff_W_K": round(total_loss_coeff, 2),
        "specific_heat_loss_W_m2K": round(specific_heat_loss, 4),
        "transmission_loss_kWh": round(transmission_loss, 2),
        "ventilation_loss_kWh": round(ventilation_loss, 2),
        "internal_gains_offset_kWh": round(internal_gains_annual, 2),
        "heating_demand_kWh": round(heating_demand, 2),
        "cooling_demand_kWh": round(cooling_demand, 2),
        "total_demand_kWh": round(total_demand, 2),
        "eui_kWh_m2_yr": round(eui, 2),
        "heating_eui_kWh_m2_yr": round(heating_eui, 2),
        "cooling_eui_kWh_m2_yr": round(cooling_eui, 2),
        "meets_passive_house_heating": meets_passive_house_heating,
        "meets_passive_house_cooling": meets_passive_house_cooling,
        "passive_house_target_kWh_m2": 15.0,
    }


def format_output(result):
    """将结果格式化为便于阅读的输出。"""
    lines = [
        "=== 能耗计算器 ===",
        f"建筑面积：            {result['floor_area_m2']:,.2f} m2",
        f"围护结构面积：        {result['envelope_area_m2']:,.2f} m2",
        f"平均 U 值：           {result['average_u_value_W_m2K']:.4f} W/m2K",
        f"建筑体积：            {result['building_volume_m3']:,.2f} m3",
        "---------------------------------------",
        f"供暖度日数：          {result['heating_degree_days']:,.0f} Kd",
        f"制冷度日数：          {result['cooling_degree_days']:,.0f} Kd",
        f"通风率：              {result['ventilation_rate_ACH']:.2f} ACH",
        f"室内得热：            {result['internal_gains_W_m2']:.2f} W/m2",
        "---------------------------------------",
        f"热损失系数：",
        f"  传热：              {result['transmission_loss_coeff_W_K']:.2f} W/K",
        f"  通风：              {result['ventilation_loss_coeff_W_K']:.2f} W/K",
        f"  合计：              {result['total_loss_coeff_W_K']:.2f} W/K",
        "---------------------------------------",
        f"传热损失：            {result['transmission_loss_kWh']:,.2f} kWh/年",
        f"通风损失：            {result['ventilation_loss_kWh']:,.2f} kWh/年",
        f"室内得热：            -{result['internal_gains_offset_kWh']:,.2f} kWh/年",
        f"供暖需求：            {result['heating_demand_kWh']:,.2f} kWh/年",
        "---------------------------------------",
        f"制冷需求：            {result['cooling_demand_kWh']:,.2f} kWh/年",
        "---------------------------------------",
        f"总需求：              {result['total_demand_kWh']:,.2f} kWh/年",
        f"EUI:                  {result['eui_kWh_m2_yr']:.2f} kWh/m2/yr",
        f"  Heating EUI:        {result['heating_eui_kWh_m2_yr']:.2f} kWh/m2/yr",
        f"  Cooling EUI:        {result['cooling_eui_kWh_m2_yr']:.2f} kWh/m2/yr",
        "",
        f"Passive House 供暖目标：{result['passive_house_target_kWh_m2']:.0f} kWh/m2/年 "
        f"-- {'满足目标' if result['meets_passive_house_heating'] else '不满足目标'}",
        f"Passive House 制冷目标：{result['passive_house_target_kWh_m2']:.0f} kWh/m2/年 "
        f"-- {'满足目标' if result['meets_passive_house_cooling'] else '不满足目标'}",
    ]
    return "\n".join(lines)


def main():
    parser = build_parser(
        description="能耗计算器：采用度日法估算年度供暖和制冷需求。"
    )
    parser.add_argument("--floor-area", type=float, required=True,
                        help="空调／供暖建筑面积，单位为 m2")
    parser.add_argument("--envelope-area", type=float, required=True,
                        help="建筑围护结构总面积，单位为 m2"
                             "（墙体 + 屋面 + 楼板）")
    parser.add_argument("--average-u-value", type=float, required=True,
                        help="面积加权平均 U 值，单位为 W/m2K")
    parser.add_argument("--heating-degree-days", type=float, required=True,
                        help="年度供暖度日数（基准 18C），单位为 Kd")
    parser.add_argument("--cooling-degree-days", type=float, required=True,
                        help="年度制冷度日数（基准 24C），单位为 Kd")
    parser.add_argument("--ventilation-rate", type=float, default=0.5,
                        help="通风率，单位为每小时换气次数（默认值：0.5）")
    parser.add_argument("--internal-gains", type=float, default=5.0,
                        help="室内得热，单位为 W/m2（默认值：5.0）")
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
