#!/usr/bin/env python3
"""
建造成本计算器

根据建筑类型、品质等级和地理区域估算建造成本，包含专业服务费、不可预见费和可选室外工程费。

用法：
    python cost_calculator.py --gfa 5000 --building-type office --quality premium --region europe
    python cost_calculator.py --gfa 5000 --building-type residential --json
"""

import argparse
import json
import sys

from _support import AGENT_HINT, build_parser


# 基础成本数据库（USD/m2，2025 年基准，北美标准品质）
COST_DATABASE = {
    "residential": {"basic": 1200, "standard": 1800, "premium": 2800},
    "office":      {"basic": 1400, "standard": 2100, "premium": 3200},
    "retail":      {"basic": 1000, "standard": 1500, "premium": 2400},
    "hospital":    {"basic": 2500, "standard": 3500, "premium": 5000},
    "school":      {"basic": 1300, "standard": 1900, "premium": 2800},
    "hotel":       {"basic": 1600, "standard": 2400, "premium": 3800},
}

# 区域成本调整系数（相对于北美）
REGIONAL_FACTORS = {
    "north-america": {"factor": 1.00, "name": "北美"},
    "europe":        {"factor": 1.05, "name": "欧洲"},
    "middle-east":   {"factor": 0.85, "name": "中东"},
    "asia":          {"factor": 0.65, "name": "亚洲"},
    "australia":     {"factor": 1.15, "name": "澳大利亚"},
}

# 按品质等级划分的专业服务费率和不可预见费率
FEE_RATES = {
    "basic":    {"fees": 0.10, "contingency": 0.10},
    "standard": {"fees": 0.12, "contingency": 0.075},
    "premium":  {"fees": 0.15, "contingency": 0.05},
}

# 室外工程占建造成本的比例
EXTERNAL_WORKS_RATE = 0.10


def validate_inputs(args):
    """校验全部输入参数。"""
    errors = []
    if args.gfa <= 0:
        errors.append("GFA 必须为正数。")

    btype = args.building_type.lower()
    if btype not in COST_DATABASE:
        valid = ", ".join(sorted(COST_DATABASE.keys()))
        errors.append(f"无效建筑类型“{args.building_type}”。"
                      f"有效类型：{valid}")

    quality = args.quality.lower()
    if quality not in ("basic", "standard", "premium"):
        errors.append("无效品质等级。必须为：basic、standard 或 premium。")

    region = args.region.lower()
    if region not in REGIONAL_FACTORS:
        valid = ", ".join(sorted(REGIONAL_FACTORS.keys()))
        errors.append(f"无效地区“{args.region}”。有效地区：{valid}")

    return errors


def calculate(args):
    """执行成本估算。"""
    btype = args.building_type.lower()
    quality = args.quality.lower()
    region = args.region.lower()

    # 基础成本单价
    base_rate = COST_DATABASE[btype][quality]
    regional_factor = REGIONAL_FACTORS[region]["factor"]
    region_name = REGIONAL_FACTORS[region]["name"]
    adjusted_rate = base_rate * regional_factor

    # 建造成本
    construction_cost = args.gfa * adjusted_rate

    # 专业服务费
    fee_rate = FEE_RATES[quality]["fees"]
    professional_fees = construction_cost * fee_rate

    # 不可预见费
    contingency_rate = FEE_RATES[quality]["contingency"]
    contingency = construction_cost * contingency_rate

    # 室外工程
    external_works = 0
    if args.include_external:
        external_works = construction_cost * EXTERNAL_WORKS_RATE

    # 开发总成本
    total_cost = construction_cost + professional_fees + contingency + external_works
    total_per_m2 = total_cost / args.gfa if args.gfa > 0 else 0

    return {
        "gfa_m2": round(args.gfa, 2),
        "building_type": btype.capitalize(),
        "quality_level": quality.capitalize(),
        "region": region_name,
        "base_rate_usd_m2": base_rate,
        "regional_factor": regional_factor,
        "adjusted_rate_usd_m2": round(adjusted_rate, 2),
        "construction_cost_usd": round(construction_cost, 2),
        "professional_fee_rate_pct": round(fee_rate * 100, 1),
        "professional_fees_usd": round(professional_fees, 2),
        "contingency_rate_pct": round(contingency_rate * 100, 1),
        "contingency_usd": round(contingency, 2),
        "include_external": args.include_external,
        "external_works_usd": round(external_works, 2),
        "external_works_rate_pct": round(EXTERNAL_WORKS_RATE * 100, 1) if args.include_external else 0,
        "total_development_cost_usd": round(total_cost, 2),
        "total_cost_per_m2_usd": round(total_per_m2, 2),
    }


def format_currency(value):
    """将数值格式化为美元货币字符串。"""
    if value >= 1_000_000:
        return f"{value:,.0f} USD"
    else:
        return f"{value:,.0f} USD"


def format_output(result):
    """将结果格式化为便于阅读的输出。"""
    lines = [
        "=== 建造成本计算器 ===",
        f"总建筑面积：        {result['gfa_m2']:,.2f} m2",
        f"建筑类型：          {result['building_type']}",
        f"品质等级：          {result['quality_level']}",
        f"地区：              {result['region']}（系数：{result['regional_factor']:.2f}）",
        "---------------------------------------",
        f"基础成本单价：      {result['base_rate_usd_m2']:,.2f} USD/m2",
        f"调整后单价：        {result['adjusted_rate_usd_m2']:,.2f} USD/m2",
        f"建造成本：          {format_currency(result['construction_cost_usd'])}",
        "---------------------------------------",
        f"专业服务费（{result['professional_fee_rate_pct']:.0f}%）："
        f"{format_currency(result['professional_fees_usd'])}",
        f"不可预见费（{result['contingency_rate_pct']:.1f}%）："
        f"{format_currency(result['contingency_usd'])}",
    ]

    if result["include_external"]:
        lines.append(
            f"室外工程（{result['external_works_rate_pct']:.0f}%）："
            f"{format_currency(result['external_works_usd'])}"
        )
    else:
        lines.append("室外工程：            --（未包含）")

    lines.extend([
        "---------------------------------------",
        f"开发总成本：          {format_currency(result['total_development_cost_usd'])}",
        f"每 m2 总成本：        {result['total_cost_per_m2_usd']:,.2f} USD/m2",
        "",
        "注：成本仅为指示性估算（2025 年美元基准）。",
        "实际成本会随市场条件、场地具体情况和工作范围而变化。",
    ])

    return "\n".join(lines)


def main():
    parser = build_parser(
        description="建造成本计算器：按建筑类型、品质和地区估算开发成本。"
    )
    parser.add_argument("--gfa", type=float, required=True,
                        help="总建筑面积，单位为 m2")
    parser.add_argument("--building-type", type=str, required=True,
                        help="建筑类型：residential、office、retail、"
                             "hospital, school, hotel")
    parser.add_argument("--quality", type=str, default="standard",
                        help="品质等级：basic、standard、premium（默认值：standard）")
    parser.add_argument("--region", type=str, default="north-america",
                        help="地区：north-america、europe、middle-east、asia、"
                             "australia（默认值：north-america）")
    parser.add_argument("--include-external", action="store_true",
                        help="包含室外／场地工程（建造成本的 10%%）")
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
