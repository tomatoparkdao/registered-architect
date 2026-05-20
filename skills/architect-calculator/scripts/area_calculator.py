#!/usr/bin/env python3
"""
Area & Density Calculator

Calculates development density metrics from site area and floor area ratio:
  - Gross Floor Area (GFA) from site area and FAR
  - Net Gross Area (NGA) from GFA and net-to-gross ratio
  - Residential unit count from NGA and average unit size
  - Estimated population from units and persons per household
  - Required parking spaces from units and parking ratio

Usage:
    python area_calculator.py --site-area 5000 --far 2.5
    python area_calculator.py --site-area 5000 --far 2.5 --ntg-ratio 0.82 --json
"""

import argparse
import json
import math
import sys


def validate_inputs(args):
    """Validate all input parameters."""
    errors = []
    if args.site_area <= 0:
        errors.append("Site area must be a positive number.")
    if args.far <= 0:
        errors.append("Floor area ratio (FAR) must be a positive number.")
    if not (0.0 < args.ntg_ratio <= 1.0):
        errors.append("Net-to-gross ratio must be between 0.0 (exclusive) and 1.0 (inclusive).")
    if args.avg_unit_size <= 0:
        errors.append("Average unit size must be a positive number.")
    if args.persons_per_unit <= 0:
        errors.append("Persons per unit must be a positive number.")
    if args.parking_ratio < 0:
        errors.append("Parking ratio cannot be negative.")
    return errors


def calculate(args):
    """Perform area and density calculations."""
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
    """Format results for human-readable output."""
    lines = [
        "=== Area & Density Calculator ===",
        f"Site Area:            {result['site_area_m2']:,.2f} m2",
        f"Floor Area Ratio:     {result['far']:.2f}",
        "---------------------------------------",
        f"Gross Floor Area:     {result['gross_floor_area_m2']:,.2f} m2",
        f"Net-to-Gross Ratio:   {result['ntg_ratio']:.2f}",
        f"Net Gross Area:       {result['net_gross_area_m2']:,.2f} m2",
        "---------------------------------------",
        f"Average Unit Size:    {result['avg_unit_size_m2']:.2f} m2",
        f"Estimated Units:      {result['estimated_units']:,}",
        f"Persons per Unit:     {result['persons_per_unit']:.2f}",
        f"Estimated Population: {result['estimated_population']:,.0f}",
        "---------------------------------------",
        f"Parking Ratio:        {result['parking_ratio']:.2f} spaces/unit",
        f"Parking Spaces:       {result['parking_spaces']:,}",
        "---------------------------------------",
        f"Density:              {result['density_units_per_hectare']:.1f} units/hectare",
        f"                      {result['density_persons_per_hectare']:.1f} persons/hectare",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Area & Density Calculator: compute GFA, NGA, unit count, "
                    "population, and parking from site area and FAR."
    )
    parser.add_argument("--site-area", type=float, required=True,
                        help="Total site/plot area in m2")
    parser.add_argument("--far", type=float, required=True,
                        help="Floor area ratio (plot ratio)")
    parser.add_argument("--ntg-ratio", type=float, default=0.80,
                        help="Net-to-gross ratio (default: 0.80)")
    parser.add_argument("--avg-unit-size", type=float, default=85.0,
                        help="Average residential unit size in m2 (default: 85)")
    parser.add_argument("--persons-per-unit", type=float, default=2.5,
                        help="Average persons per dwelling unit (default: 2.5)")
    parser.add_argument("--parking-ratio", type=float, default=1.0,
                        help="Parking spaces per dwelling unit (default: 1.0)")
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
