#!/usr/bin/env python3
"""
Energy Calculator

Estimates annual heating and cooling energy demand using the degree-day
method. Accounts for transmission losses through the building envelope,
ventilation losses, and internal heat gains.

Usage:
    python energy_calculator.py --floor-area 500 --envelope-area 800 \\
        --average-u-value 0.35 --heating-degree-days 3000 --cooling-degree-days 500
    python energy_calculator.py --floor-area 500 --envelope-area 800 \\
        --average-u-value 0.35 --heating-degree-days 3000 --cooling-degree-days 500 --json
"""

import argparse
import json
import sys


def validate_inputs(args):
    """Validate all input parameters."""
    errors = []
    if args.floor_area <= 0:
        errors.append("Floor area must be a positive number.")
    if args.envelope_area <= 0:
        errors.append("Envelope area must be a positive number.")
    if args.average_u_value <= 0:
        errors.append("Average U-value must be a positive number.")
    if args.heating_degree_days < 0:
        errors.append("Heating degree days cannot be negative.")
    if args.cooling_degree_days < 0:
        errors.append("Cooling degree days cannot be negative.")
    if args.ventilation_rate < 0:
        errors.append("Ventilation rate cannot be negative.")
    if args.internal_gains < 0:
        errors.append("Internal gains cannot be negative.")
    return errors


def calculate(args):
    """Perform energy demand calculations using degree-day method."""
    # Assumed ceiling height for volume calculation
    ceiling_height = 3.0  # meters
    volume = args.floor_area * ceiling_height  # m3

    # Transmission heat loss coefficient (W/K)
    transmission_coeff = args.average_u_value * args.envelope_area

    # Ventilation heat loss coefficient (W/K)
    # Q_vent = 0.33 * n * V (where 0.33 = rho_air * cp_air / 3600)
    ventilation_coeff = 0.33 * args.ventilation_rate * volume

    # Total heat loss coefficient
    total_loss_coeff = transmission_coeff + ventilation_coeff

    # Annual transmission loss (kWh/yr)
    # Q = HLC * HDD * 24 / 1000
    transmission_loss = transmission_coeff * args.heating_degree_days * 24 / 1000
    ventilation_loss = ventilation_coeff * args.heating_degree_days * 24 / 1000

    # Internal gains offset (kWh/yr)
    # Assume gains are useful during heating season
    # Heating season hours approximated from HDD
    heating_season_hours = min(args.heating_degree_days / 10 * 24, 8760)
    internal_gains_annual = args.internal_gains * args.floor_area * heating_season_hours / 1000

    # Heating demand
    heating_demand = max(0, transmission_loss + ventilation_loss - internal_gains_annual)

    # Cooling demand
    # Transmission gains during cooling season
    cooling_transmission = transmission_coeff * args.cooling_degree_days * 24 / 1000

    # Solar and internal gains during cooling season
    cooling_season_hours = min(args.cooling_degree_days / 5 * 24, 4380)
    internal_gains_cooling = args.internal_gains * args.floor_area * cooling_season_hours / 1000

    # Solar gains estimate (simplified: ~15 W/m2 of floor area during cooling season)
    solar_gain_rate = 15.0  # W/m2
    solar_gains = solar_gain_rate * args.floor_area * cooling_season_hours / 1000

    cooling_demand = max(0, cooling_transmission + internal_gains_cooling + solar_gains)

    # Total demand and EUI
    total_demand = heating_demand + cooling_demand
    eui = total_demand / args.floor_area if args.floor_area > 0 else 0

    # Passive House compliance check
    heating_eui = heating_demand / args.floor_area if args.floor_area > 0 else 0
    cooling_eui = cooling_demand / args.floor_area if args.floor_area > 0 else 0
    meets_passive_house_heating = heating_eui <= 15.0
    meets_passive_house_cooling = cooling_eui <= 15.0

    # Heat loss per unit floor area
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
    """Format results for human-readable output."""
    lines = [
        "=== Energy Calculator ===",
        f"Floor Area:           {result['floor_area_m2']:,.2f} m2",
        f"Envelope Area:        {result['envelope_area_m2']:,.2f} m2",
        f"Average U-value:      {result['average_u_value_W_m2K']:.4f} W/m2K",
        f"Building Volume:      {result['building_volume_m3']:,.2f} m3",
        "---------------------------------------",
        f"Heating Degree Days:  {result['heating_degree_days']:,.0f} Kd",
        f"Cooling Degree Days:  {result['cooling_degree_days']:,.0f} Kd",
        f"Ventilation Rate:     {result['ventilation_rate_ACH']:.2f} ACH",
        f"Internal Gains:       {result['internal_gains_W_m2']:.2f} W/m2",
        "---------------------------------------",
        f"Loss Coefficients:",
        f"  Transmission:       {result['transmission_loss_coeff_W_K']:.2f} W/K",
        f"  Ventilation:        {result['ventilation_loss_coeff_W_K']:.2f} W/K",
        f"  Total:              {result['total_loss_coeff_W_K']:.2f} W/K",
        "---------------------------------------",
        f"Transmission Loss:    {result['transmission_loss_kWh']:,.2f} kWh/yr",
        f"Ventilation Loss:     {result['ventilation_loss_kWh']:,.2f} kWh/yr",
        f"Internal Gains:       -{result['internal_gains_offset_kWh']:,.2f} kWh/yr",
        f"Heating Demand:       {result['heating_demand_kWh']:,.2f} kWh/yr",
        "---------------------------------------",
        f"Cooling Demand:       {result['cooling_demand_kWh']:,.2f} kWh/yr",
        "---------------------------------------",
        f"Total Demand:         {result['total_demand_kWh']:,.2f} kWh/yr",
        f"EUI:                  {result['eui_kWh_m2_yr']:.2f} kWh/m2/yr",
        f"  Heating EUI:        {result['heating_eui_kWh_m2_yr']:.2f} kWh/m2/yr",
        f"  Cooling EUI:        {result['cooling_eui_kWh_m2_yr']:.2f} kWh/m2/yr",
        "",
        f"Passive House heating target: {result['passive_house_target_kWh_m2']:.0f} kWh/m2/yr "
        f"-- {'MEETS TARGET' if result['meets_passive_house_heating'] else 'DOES NOT MEET'}",
        f"Passive House cooling target: {result['passive_house_target_kWh_m2']:.0f} kWh/m2/yr "
        f"-- {'MEETS TARGET' if result['meets_passive_house_cooling'] else 'DOES NOT MEET'}",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Energy Calculator: estimate annual heating and cooling "
                    "demand using the degree-day method."
    )
    parser.add_argument("--floor-area", type=float, required=True,
                        help="Conditioned floor area in m2")
    parser.add_argument("--envelope-area", type=float, required=True,
                        help="Total building envelope area in m2 "
                             "(walls + roof + floor)")
    parser.add_argument("--average-u-value", type=float, required=True,
                        help="Area-weighted average U-value in W/m2K")
    parser.add_argument("--heating-degree-days", type=float, required=True,
                        help="Annual heating degree days (base 18C) in Kd")
    parser.add_argument("--cooling-degree-days", type=float, required=True,
                        help="Annual cooling degree days (base 24C) in Kd")
    parser.add_argument("--ventilation-rate", type=float, default=0.5,
                        help="Ventilation rate in air changes per hour (default: 0.5)")
    parser.add_argument("--internal-gains", type=float, default=5.0,
                        help="Internal heat gains in W/m2 (default: 5.0)")
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
