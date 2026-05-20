#!/usr/bin/env python3
"""
Construction Cost Calculator

Estimates construction cost based on building type, quality level, and
geographic region. Includes professional fees, contingency, and optional
external works.

Usage:
    python cost_calculator.py --gfa 5000 --building-type office --quality premium --region europe
    python cost_calculator.py --gfa 5000 --building-type residential --json
"""

import argparse
import json
import sys


# Base cost database (USD/m2, 2025 baseline, North America standard quality)
COST_DATABASE = {
    "residential": {"basic": 1200, "standard": 1800, "premium": 2800},
    "office":      {"basic": 1400, "standard": 2100, "premium": 3200},
    "retail":      {"basic": 1000, "standard": 1500, "premium": 2400},
    "hospital":    {"basic": 2500, "standard": 3500, "premium": 5000},
    "school":      {"basic": 1300, "standard": 1900, "premium": 2800},
    "hotel":       {"basic": 1600, "standard": 2400, "premium": 3800},
}

# Regional cost adjustment factors (relative to North America)
REGIONAL_FACTORS = {
    "north-america": {"factor": 1.00, "name": "North America"},
    "europe":        {"factor": 1.05, "name": "Europe"},
    "middle-east":   {"factor": 0.85, "name": "Middle East"},
    "asia":          {"factor": 0.65, "name": "Asia"},
    "australia":     {"factor": 1.15, "name": "Australia"},
}

# Professional fee and contingency rates by quality level
FEE_RATES = {
    "basic":    {"fees": 0.10, "contingency": 0.10},
    "standard": {"fees": 0.12, "contingency": 0.075},
    "premium":  {"fees": 0.15, "contingency": 0.05},
}

# External works percentage of construction cost
EXTERNAL_WORKS_RATE = 0.10


def validate_inputs(args):
    """Validate all input parameters."""
    errors = []
    if args.gfa <= 0:
        errors.append("GFA must be a positive number.")

    btype = args.building_type.lower()
    if btype not in COST_DATABASE:
        valid = ", ".join(sorted(COST_DATABASE.keys()))
        errors.append(f"Invalid building type '{args.building_type}'. "
                      f"Valid types: {valid}")

    quality = args.quality.lower()
    if quality not in ("basic", "standard", "premium"):
        errors.append("Invalid quality level. Must be: basic, standard, or premium.")

    region = args.region.lower()
    if region not in REGIONAL_FACTORS:
        valid = ", ".join(sorted(REGIONAL_FACTORS.keys()))
        errors.append(f"Invalid region '{args.region}'. Valid regions: {valid}")

    return errors


def calculate(args):
    """Perform cost estimation calculations."""
    btype = args.building_type.lower()
    quality = args.quality.lower()
    region = args.region.lower()

    # Base cost rate
    base_rate = COST_DATABASE[btype][quality]
    regional_factor = REGIONAL_FACTORS[region]["factor"]
    region_name = REGIONAL_FACTORS[region]["name"]
    adjusted_rate = base_rate * regional_factor

    # Construction cost
    construction_cost = args.gfa * adjusted_rate

    # Professional fees
    fee_rate = FEE_RATES[quality]["fees"]
    professional_fees = construction_cost * fee_rate

    # Contingency
    contingency_rate = FEE_RATES[quality]["contingency"]
    contingency = construction_cost * contingency_rate

    # External works
    external_works = 0
    if args.include_external:
        external_works = construction_cost * EXTERNAL_WORKS_RATE

    # Total development cost
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
    """Format a number as USD currency string."""
    if value >= 1_000_000:
        return f"{value:,.0f} USD"
    else:
        return f"{value:,.0f} USD"


def format_output(result):
    """Format results for human-readable output."""
    lines = [
        "=== Construction Cost Calculator ===",
        f"Gross Floor Area:   {result['gfa_m2']:,.2f} m2",
        f"Building Type:      {result['building_type']}",
        f"Quality Level:      {result['quality_level']}",
        f"Region:             {result['region']} (factor: {result['regional_factor']:.2f})",
        "---------------------------------------",
        f"Base Cost Rate:     {result['base_rate_usd_m2']:,.2f} USD/m2",
        f"Adjusted Rate:      {result['adjusted_rate_usd_m2']:,.2f} USD/m2",
        f"Construction Cost:  {format_currency(result['construction_cost_usd'])}",
        "---------------------------------------",
        f"Professional Fees ({result['professional_fee_rate_pct']:.0f}%):  "
        f"{format_currency(result['professional_fees_usd'])}",
        f"Contingency ({result['contingency_rate_pct']:.1f}%):       "
        f"{format_currency(result['contingency_usd'])}",
    ]

    if result["include_external"]:
        lines.append(
            f"External Works ({result['external_works_rate_pct']:.0f}%):    "
            f"{format_currency(result['external_works_usd'])}"
        )
    else:
        lines.append("External Works:           -- (not included)")

    lines.extend([
        "---------------------------------------",
        f"Total Development Cost:   {format_currency(result['total_development_cost_usd'])}",
        f"Cost per m2 (total):      {result['total_cost_per_m2_usd']:,.2f} USD/m2",
        "",
        "Note: Costs are indicative estimates (2025 baseline USD).",
        "Actual costs vary by market conditions, site specifics, and scope.",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Construction Cost Calculator: estimate development cost "
                    "by building type, quality, and region."
    )
    parser.add_argument("--gfa", type=float, required=True,
                        help="Gross floor area in m2")
    parser.add_argument("--building-type", type=str, required=True,
                        help="Building type: residential, office, retail, "
                             "hospital, school, hotel")
    parser.add_argument("--quality", type=str, default="standard",
                        help="Quality level: basic, standard, premium (default: standard)")
    parser.add_argument("--region", type=str, default="north-america",
                        help="Region: north-america, europe, middle-east, asia, "
                             "australia (default: north-america)")
    parser.add_argument("--include-external", action="store_true",
                        help="Include external/site works (10%% of construction cost)")
    parser.add_argument("--json", action="store_true",
                        help="Output results as JSON")

    args = parser.parse_args()

    errors = validate_inputs(args)
    if errors:
        for error in errors:
            print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)

    result = calculate(args)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(format_output(result))


if __name__ == "__main__":
    main()
