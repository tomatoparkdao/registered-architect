#!/usr/bin/env python3
"""
Egress Calculator

Calculates egress requirements per International Building Code (IBC):
  - Occupant load from floor area and occupant load factor
  - Required number of exits
  - Minimum total exit width and width per exit
  - Maximum travel distance
  - Compliance assessment

Usage:
    python egress_calculator.py --floor-area 800 --occupancy-type B --sprinklered
    python egress_calculator.py --floor-area 800 --occupancy-type B --num-stories 4 --json
"""

import argparse
import json
import math
import sys


# Occupant load factors (m2 per person) - IBC Table 1004.5
OCCUPANT_LOAD_FACTORS = {
    "A-1": {"factor": 1.5, "name": "Assembly, fixed seats", "net": True},
    "A-2": {"factor": 1.4, "name": "Assembly, food/drink", "net": True},
    "A-3": {"factor": 1.9, "name": "Assembly, worship/recreation", "net": True},
    "A-4": {"factor": 4.6, "name": "Assembly, standing", "net": True},
    "A-5": {"factor": 1.4, "name": "Assembly, outdoor", "net": True},
    "B":   {"factor": 9.3, "name": "Business", "net": False},
    "E":   {"factor": 1.9, "name": "Educational", "net": True},
    "F-1": {"factor": 18.6, "name": "Factory, moderate hazard", "net": False},
    "F-2": {"factor": 18.6, "name": "Factory, low hazard", "net": False},
    "H-1": {"factor": 9.3, "name": "High hazard, detonation", "net": False},
    "H-2": {"factor": 9.3, "name": "High hazard, accelerated burning", "net": False},
    "H-3": {"factor": 9.3, "name": "High hazard, physical", "net": False},
    "I-1": {"factor": 18.6, "name": "Institutional, supervised", "net": False},
    "I-2": {"factor": 22.3, "name": "Institutional, incapacitated", "net": False},
    "I-3": {"factor": 11.1, "name": "Institutional, restrained", "net": False},
    "M":   {"factor": 5.6, "name": "Mercantile", "net": False},
    "R":   {"factor": 18.6, "name": "Residential", "net": False},
    "S-1": {"factor": 46.5, "name": "Storage, moderate hazard", "net": False},
    "S-2": {"factor": 46.5, "name": "Storage, low hazard", "net": False},
    "U":   {"factor": 46.5, "name": "Utility", "net": False},
}

# Maximum travel distances (meters) - IBC Table 1017.2
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
    """Validate all input parameters."""
    errors = []
    if args.floor_area <= 0:
        errors.append("Floor area must be a positive number.")
    occ = args.occupancy_type.upper()
    if occ not in OCCUPANT_LOAD_FACTORS:
        valid = ", ".join(sorted(OCCUPANT_LOAD_FACTORS.keys()))
        errors.append(f"Invalid occupancy type '{args.occupancy_type}'. "
                      f"Valid types: {valid}")
    if args.num_stories < 1:
        errors.append("Number of stories must be at least 1.")
    return errors


def calculate(args):
    """Perform egress calculations."""
    occ = args.occupancy_type.upper()
    occ_info = OCCUPANT_LOAD_FACTORS[occ]
    occ_factor = occ_info["factor"]
    occ_name = occ_info["name"]

    # Occupant load
    occupant_load = math.ceil(args.floor_area / occ_factor)

    # Number of exits required (IBC 1006.2)
    if occupant_load <= 500:
        num_exits = 2
    elif occupant_load <= 1000:
        num_exits = 3
    else:
        num_exits = 4

    # Special: single exit allowed for small occupant loads in certain occupancies
    # (simplified -- full code has more nuance)
    if occupant_load <= 49 and args.num_stories <= 1 and occ not in ("H-1", "H-2", "H-3"):
        num_exits = max(1, num_exits)
        # Still require 2 for safety in most cases
        if occupant_load > 10:
            num_exits = 2

    # Exit width calculation
    # Stair width factor: 7.6 mm/person; other components: 5.1 mm/person
    if args.num_stories > 1:
        width_factor = 7.6  # stairs
    else:
        width_factor = 5.1  # level components

    if args.sprinklered:
        width_factor *= 0.75  # Sprinkler reduction per IBC

    total_exit_width_mm = math.ceil(occupant_load * width_factor)
    width_per_exit_mm = math.ceil(total_exit_width_mm / num_exits)

    # Minimum door width
    min_door_width_mm = 813  # 32 inches clear

    # Use the larger of calculated and minimum
    effective_width_per_exit = max(width_per_exit_mm, min_door_width_mm)

    # Travel distances
    sprinkler_key = "sprinklered" if args.sprinklered else "unsprinklered"
    travel_info = TRAVEL_DISTANCES.get(occ, {"unsprinklered": 61.0, "sprinklered": 76.0})
    max_travel = travel_info[sprinkler_key]
    max_travel_ft = round(max_travel * 3.28084)

    # Common path and dead end limits
    max_common_path = 23.0  # 75 ft default
    max_dead_end = 6.1  # 20 ft without sprinklers
    if args.sprinklered:
        max_dead_end = 15.0  # 50 ft with sprinklers

    # For B, F, S occupancies, common path can be longer
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
    """Format results for human-readable output."""
    lines = [
        "=== Egress Calculator ===",
        f"Floor Area:        {result['floor_area_m2']:,.2f} m2",
        f"Occupancy Type:    {result['occupancy_type']} ({result['occupancy_name']})",
        f"Sprinklered:       {'Yes' if result['sprinklered'] else 'No'}",
        f"Number of Stories: {result['num_stories']}",
        "---------------------------------------",
        f"Occupant Load Factor:   {result['occupant_load_factor_m2']:.1f} m2/person",
        f"Occupant Load:          {result['occupant_load']:,} persons",
        "---------------------------------------",
        f"Required Exits:         {result['required_exits']}",
        f"Min Exit Width (total): {result['total_exit_width_mm']:,} mm",
        f"Width per Exit:         {result['width_per_exit_mm']:,} mm",
        f"Min Door Width:         {result['min_door_width_mm']:,} mm (32 inches)",
        f"Effective per Exit:     {result['effective_width_per_exit_mm']:,} mm",
        "---------------------------------------",
        f"Max Travel Distance:    {result['max_travel_distance_m']:.1f} m "
        f"({result['max_travel_distance_ft']} ft) "
        f"[{'sprinklered' if result['sprinklered'] else 'unsprinklered'}]",
        f"Max Common Path:        {result['max_common_path_m']:.1f} m",
        f"Max Dead End:           {result['max_dead_end_m']:.1f} m",
        "",
        "COMPLIANCE: Review travel distances on plans against limits above.",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Egress Calculator: compute occupant load, required exits, "
                    "exit widths, and travel distances per IBC."
    )
    parser.add_argument("--floor-area", type=float, required=True,
                        help="Net floor area in m2")
    parser.add_argument("--occupancy-type", type=str, required=True,
                        help="IBC occupancy classification (e.g., A-1, B, E, M, R)")
    parser.add_argument("--sprinklered", action="store_true",
                        help="Building is sprinklered")
    parser.add_argument("--num-stories", type=int, default=1,
                        help="Number of stories (default: 1)")
    parser.add_argument("--json", action="store_true",
                        help="Output results as JSON")

    args = parser.parse_args()

    errors = validate_inputs(args)
    if errors:
        for error in errors:
            print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)

    # Normalize occupancy type to uppercase
    args.occupancy_type = args.occupancy_type.upper()

    result = calculate(args)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(format_output(result))


if __name__ == "__main__":
    main()
