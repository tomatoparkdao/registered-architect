#!/usr/bin/env python3
"""
U-Value Calculator for Architects
===================================
Calculates thermal transmittance for both simple wall build-ups and
composite facade assemblies with windows, doors, balconies, and
linear/point thermal bridges.

Facade mode auto-composes openings with equal pier widths, symmetry
around doors, sill height alignment, and generates a proportional
ASCII facade elevation diagram.

MODE 1 -- Simple Wall Build-Up:
  python uvalue_calculator.py --layers '[
    {"name":"Brick","thickness_mm":102,"conductivity":0.77},
    {"name":"PIR Insulation","thickness_mm":100,"conductivity":0.022},
    {"name":"Concrete block","thickness_mm":100,"conductivity":0.15}
  ]'

MODE 2 -- Composite Facade (auto-layout + thermal calculation):
  python uvalue_calculator.py --facade '{
    "width": 7.0, "height": 3.0,
    "wall_layers": [
      {"name":"Render","thickness_mm":15,"conductivity":0.50},
      {"name":"EPS","thickness_mm":150,"conductivity":0.034},
      {"name":"Concrete","thickness_mm":200,"conductivity":1.40},
      {"name":"Plaster","thickness_mm":13,"conductivity":0.16}
    ],
    "openings": [
      {"type":"window","name":"W1","width":1.2,"height":1.5,"u_value":1.2},
      {"type":"door","name":"D1 Entrance","width":0.9,"height":2.1,"u_value":1.8},
      {"type":"window","name":"W2","width":1.2,"height":1.5,"u_value":1.2}
    ]
  }'

  Openings are laid out LEFT-TO-RIGHT in the order given, with equal
  pier widths computed automatically. Doors sit at ground level (sill=0),
  windows default to sill=0.9m. Override sill with "sill" field.
"""

import argparse
import json
import math
import sys


# ============================================================================
# Constants
# ============================================================================

DEFAULT_PSI_WINDOW = 0.04
DEFAULT_PSI_DOOR = 0.06
DEFAULT_PSI_BALCONY_DOOR = 0.05

MIN_PIER_STRUCTURAL = 0.20   # absolute structural minimum (m)
MIN_PIER_THERMAL = 0.40      # minimum to avoid severe thermal bridging (m)
MIN_PIER_RECOMMENDED = 0.60  # recommended for good practice (m)

DEFAULT_SILL_WINDOW = 0.90   # metres above floor
DEFAULT_SILL_DOOR = 0.00     # ground level

COMPLIANCE_TARGETS = {
    "passive_house_wall": 0.15,
    "code_wall": 0.30,
}

DIAGRAM_TARGET_WIDTH = 74  # characters wide for ASCII diagram


# ============================================================================
# Mode 1: Simple Wall
# ============================================================================

def validate_layers(layers):
    errors = []
    if not layers:
        errors.append("At least one layer is required.")
        return errors
    for i, layer in enumerate(layers):
        label = f"Layer {i + 1}"
        if "name" not in layer:
            errors.append(f"{label}: missing 'name'.")
        if "thickness_mm" not in layer:
            errors.append(f"{label}: missing 'thickness_mm'.")
        elif layer["thickness_mm"] <= 0:
            errors.append(f"{label}: thickness_mm must be positive.")
        if "conductivity" not in layer:
            errors.append(f"{label}: missing 'conductivity'.")
        elif layer["conductivity"] <= 0:
            errors.append(f"{label}: conductivity must be positive.")
    return errors


def calculate_wall_uvalue(layers, rsi_internal, rsi_external):
    layer_results = []
    total_r = rsi_internal
    for layer in layers:
        thickness_m = layer["thickness_mm"] / 1000.0
        r_value = thickness_m / layer["conductivity"]
        total_r += r_value
        layer_results.append({
            "name": layer["name"],
            "thickness_mm": layer["thickness_mm"],
            "conductivity": round(layer["conductivity"], 4),
            "r_value": round(r_value, 4),
        })
    total_r += rsi_external
    u_value = 1.0 / total_r
    return {
        "layers": layer_results,
        "rsi_internal": round(rsi_internal, 4),
        "rsi_external": round(rsi_external, 4),
        "total_r_value": round(total_r, 4),
        "u_value": round(u_value, 4),
        "total_thickness_mm": sum(l["thickness_mm"] for l in layers),
    }


# ============================================================================
# Mode 2: Facade Layout Engine
# ============================================================================

def expand_openings(openings):
    """Expand count>1 into individual openings, preserving input order."""
    expanded = []
    for op in openings:
        count = op.get("count", 1)
        for i in range(count):
            item = dict(op)
            item.pop("count", None)
            if count > 1:
                base = op.get("name", op["type"])
                item["name"] = f"{base} #{i+1}"
            expanded.append(item)
    return expanded


def generate_layout(facade_width, facade_height, openings):
    """
    Position openings left-to-right with equal pier widths.

    Rules:
    - Openings are placed in INPUT ORDER (user controls composition)
    - All pier widths (gaps between openings and edges) are EQUAL
    - Doors: sill = 0.0m (ground level) unless overridden
    - Windows: sill = 0.9m unless overridden
    - Balcony doors: sill = 0.0m unless overridden
    - Validates: piers not too narrow, openings fit within facade

    Returns:
        positioned: list of dicts with added 'x', 'sill', 'x_center' fields
        pier_width: the equal pier width (metres)
        piers: list of pier dicts with 'x', 'width', 'label'
    """
    expanded = expand_openings(openings)

    total_opening_width = sum(o["width"] for o in expanded)
    remaining = facade_width - total_opening_width
    n_piers = len(expanded) + 1
    pier_width = remaining / n_piers if n_piers > 0 else remaining

    # Assign positions
    x = pier_width
    piers = []
    # Left edge pier
    piers.append({
        "label": "pier",
        "x": 0.0,
        "width": round(pier_width, 4),
    })

    for i, op in enumerate(expanded):
        # Set sill height
        if "sill" not in op:
            if op["type"] in ("door", "balcony_door"):
                op["sill"] = DEFAULT_SILL_DOOR
            else:
                op["sill"] = DEFAULT_SILL_WINDOW

        op["x"] = round(x, 4)
        op["x_center"] = round(x + op["width"] / 2, 4)
        op["head"] = round(op["sill"] + op["height"], 4)

        x_after = x + op["width"]

        # Pier after this opening
        piers.append({
            "label": "pier",
            "x": round(x_after, 4),
            "width": round(pier_width, 4),
        })

        x = x_after + pier_width

    return expanded, round(pier_width, 4), piers


def draw_facade_elevation(facade_width, facade_height, positioned, pier_width):
    """
    Generate a proportional ASCII facade elevation diagram.

    The diagram uses character widths proportional to real dimensions,
    showing openings as boxes within the wall, with sill heights,
    labels, and dimension annotations.
    """
    scale = (DIAGRAM_TARGET_WIDTH - 2) / facade_width  # chars per metre (inside borders)
    min_label_width = 3  # minimum chars for any element

    # Build element sequence: pier, opening, pier, opening, ..., pier
    elements = []
    x = 0.0
    for op in positioned:
        # Pier before this opening
        op_x = op.get("x", op.get("x_m", 0))
        pw = op_x - x
        if pw > 0.001:
            elements.append({"type": "pier", "width_m": pw, "data": None})
        op_w = op.get("width", op.get("width_m", 0))
        elements.append({"type": "opening", "width_m": op_w, "data": op})
        x = op_x + op_w
    # Final pier
    pw = facade_width - x
    if pw > 0.001:
        elements.append({"type": "pier", "width_m": pw, "data": None})

    # Calculate character widths
    raw_chars = []
    for el in elements:
        c = max(min_label_width, round(el["width_m"] * scale))
        raw_chars.append(c)

    # Adjust to hit target width
    total_c = sum(raw_chars)
    target = DIAGRAM_TARGET_WIDTH - 2  # minus left and right border chars
    diff = target - total_c
    # Distribute difference across widest elements
    if diff != 0:
        sorted_indices = sorted(range(len(raw_chars)),
                                key=lambda i: raw_chars[i], reverse=True)
        for i in range(abs(diff)):
            idx = sorted_indices[i % len(sorted_indices)]
            raw_chars[idx] += 1 if diff > 0 else -1
            raw_chars[idx] = max(min_label_width, raw_chars[idx])

    char_widths = raw_chars

    lines = []
    lines.append(f"--- FACADE ELEVATION ({facade_width:.1f}m x {facade_height:.1f}m) ---")
    lines.append("")

    # --- TOP BORDER ---
    top = "+"
    for cw in char_widths:
        top += "-" * cw + "+"
    lines.append("  " + top)

    # --- UPPER WALL (above window heads, below facade top) ---
    # Show opening type labels
    row_type = "|"
    row_name = "|"
    row_size = "|"
    row_uval = "|"

    for i, el in enumerate(elements):
        cw = char_widths[i]
        if el["type"] == "pier":
            row_type += " " * cw + "|"
            row_name += " " * cw + "|"
            row_size += " " * cw + "|"
            row_uval += " " * cw + "|"
        else:
            op = el["data"]
            op_type = op["type"].upper().replace("_", " ")
            op_name = op.get("name", op["type"])
            w = op.get("width", op.get("width_m", 0))
            h = op.get("height", op.get("height_m", 0))
            size_str = f"{w:.1f}x{h:.1f}m"
            u_str = f"U={op['u_value']:.2f}"

            row_type += center_text(op_type, cw) + "|"
            row_name += center_text(op_name, cw) + "|"
            row_size += center_text(size_str, cw) + "|"
            row_uval += center_text(u_str, cw) + "|"

    lines.append("  " + row_type)
    lines.append("  " + row_name)
    lines.append("  " + row_size)
    lines.append("  " + row_uval)

    # --- SILL LINE (windows stop here, doors continue to ground) ---
    sill_row = "|"
    for i, el in enumerate(elements):
        cw = char_widths[i]
        if el["type"] == "pier":
            sill_row += " " * cw + "|"
        else:
            op = el["data"]
            sill = op.get("sill", op.get("sill_m", 0))
            if sill > 0.01:
                sill_str = f"sill {sill:.1f}m"
                sill_row += center_text(sill_str, cw) + "|"
            else:
                sill_row += center_text("(to ground)", cw) + "|"
    lines.append("  " + sill_row)

    # --- BELOW-SILL ROW (wall below windows, doors still open) ---
    below = "|"
    for i, el in enumerate(elements):
        cw = char_widths[i]
        if el["type"] == "pier":
            below += " " * cw + "|"
        else:
            op = el["data"]
            sill2 = op.get("sill", op.get("sill_m", 0))
            if sill2 > 0.01:
                below += center_text("[wall]", cw) + "|"
            else:
                below += " " * cw + "|"
    lines.append("  " + below)

    # --- BOTTOM BORDER ---
    bot = "+"
    for cw in char_widths:
        bot += "-" * cw + "+"
    lines.append("  " + bot)

    # --- DIMENSION LINE ---
    dim_row = " "
    for i, el in enumerate(elements):
        cw = char_widths[i]
        if el["type"] == "pier":
            dim_str = f"{el['width_m']:.2f}"
        else:
            dim_str = f"{el['width_m']:.2f}"
        dim_row += center_text(dim_str, cw + 1)
    lines.append("  " + dim_row)

    # --- LABEL LINE ---
    label_row = " "
    for i, el in enumerate(elements):
        cw = char_widths[i]
        if el["type"] == "pier":
            label_row += center_text("pier", cw + 1)
        else:
            op = el["data"]
            label_row += center_text(op.get("name", op["type"]), cw + 1)
    lines.append("  " + label_row)

    lines.append("")
    lines.append(f"  Equal pier width: {pier_width:.2f}m")

    # Pier quality assessment
    if pier_width < MIN_PIER_STRUCTURAL:
        lines.append(f"  !! CRITICAL: Pier {pier_width:.2f}m < {MIN_PIER_STRUCTURAL}m "
                     "structural minimum. Openings do not fit.")
    elif pier_width < MIN_PIER_THERMAL:
        lines.append(f"  ! WARNING: Pier {pier_width:.2f}m < {MIN_PIER_THERMAL}m. "
                     "Severe thermal bridging at piers. Widen wall or shrink openings.")
    elif pier_width < MIN_PIER_RECOMMENDED:
        lines.append(f"  NOTE: Pier {pier_width:.2f}m < {MIN_PIER_RECOMMENDED}m recommended. "
                     "Consider widening for better thermal performance and proportions.")
    else:
        lines.append(f"  Pier width OK (>= {MIN_PIER_RECOMMENDED}m recommended minimum)")

    return "\n".join(lines)


def center_text(text, width):
    """Center text within a given character width, truncating if needed."""
    if len(text) > width:
        text = text[:width]
    return text.center(width)


# ============================================================================
# Mode 2: Facade Thermal Calculation
# ============================================================================

def validate_facade(facade):
    errors = []
    if "width" not in facade or facade["width"] <= 0:
        errors.append("Facade 'width' must be positive (metres).")
    if "height" not in facade or facade["height"] <= 0:
        errors.append("Facade 'height' must be positive (metres).")
    if "wall_layers" not in facade or not facade["wall_layers"]:
        errors.append("Facade must include 'wall_layers' array.")
    else:
        errors.extend(validate_layers(facade["wall_layers"]))

    for i, op in enumerate(facade.get("openings", [])):
        label = f"Opening {i + 1}"
        if "type" not in op:
            errors.append(f"{label}: missing 'type' (window/door/balcony_door).")
        if "width" not in op or op["width"] <= 0:
            errors.append(f"{label}: 'width' must be positive.")
        if "height" not in op or op["height"] <= 0:
            errors.append(f"{label}: 'height' must be positive.")
        if "u_value" not in op or op["u_value"] <= 0:
            errors.append(f"{label}: 'u_value' must be positive.")

    for i, tb in enumerate(facade.get("thermal_bridges", [])):
        label = f"Thermal bridge {i + 1}"
        if "psi" not in tb or tb["psi"] < 0:
            errors.append(f"{label}: 'psi' must be non-negative.")
        if "length" not in tb or tb["length"] <= 0:
            errors.append(f"{label}: 'length' must be positive.")

    return errors


def calculate_facade(facade, rsi_internal, rsi_external):
    """
    Full composite facade analysis:
    1. Auto-layout openings with equal pier widths
    2. Calculate opaque wall U-value from layers
    3. Area-weighted composite U-value per ISO 13789
    4. Thermal bridge contributions (perimeter + user-defined)
    """
    fw = facade["width"]
    fh = facade["height"]
    total_area = fw * fh

    # --- Layout ---
    positioned, pier_width, piers = generate_layout(
        fw, fh, facade.get("openings", [])
    )

    # --- Wall U-value ---
    wall_result = calculate_wall_uvalue(
        facade["wall_layers"], rsi_internal, rsi_external
    )
    wall_u = wall_result["u_value"]

    # --- Process positioned openings ---
    opening_results = []
    total_opening_area = 0.0
    total_window_area = 0.0
    total_door_area = 0.0
    component_losses = []

    for op in positioned:
        op_type = op["type"]
        op_name = op.get("name", op_type)
        area = op["width"] * op["height"]
        perim = 2 * (op["width"] + op["height"])
        total_opening_area += area

        if op_type == "window":
            total_window_area += area
            default_psi = DEFAULT_PSI_WINDOW
        elif op_type == "balcony_door":
            total_window_area += area
            default_psi = DEFAULT_PSI_BALCONY_DOOR
        else:
            total_door_area += area
            default_psi = DEFAULT_PSI_DOOR

        psi = op.get("psi", default_psi)
        area_loss = op["u_value"] * area
        perim_loss = psi * perim

        opening_results.append({
            "name": op_name,
            "type": op_type,
            "x_m": op["x"],
            "sill_m": op["sill"],
            "width_m": op["width"],
            "height_m": op["height"],
            "area_m2": round(area, 2),
            "u_value": op["u_value"],
            "perimeter_m": round(perim, 2),
            "psi": psi,
            "loss_area_WK": round(area_loss, 3),
            "loss_perim_WK": round(perim_loss, 3),
            "loss_total_WK": round(area_loss + perim_loss, 3),
        })

        component_losses.append({"name": f"{op_name} (area)", "WK": area_loss})
        component_losses.append({"name": f"{op_name} (perim)", "WK": perim_loss})

    opaque_area = total_area - total_opening_area
    if opaque_area < 0:
        opaque_area = 0.0
    opaque_loss = wall_u * opaque_area
    component_losses.insert(0, {"name": "Opaque wall", "WK": opaque_loss})

    # --- User-defined thermal bridges ---
    bridges = facade.get("thermal_bridges", [])
    bridge_results = []
    total_bridge_loss = 0.0
    for tb in bridges:
        loss = tb["psi"] * tb["length"]
        total_bridge_loss += loss
        bridge_results.append({
            "name": tb.get("name", "Bridge"),
            "psi_WmK": tb["psi"],
            "length_m": tb["length"],
            "loss_WK": round(loss, 3),
        })
        component_losses.append({
            "name": f"{tb.get('name', 'Bridge')} (psi={tb['psi']})",
            "WK": loss,
        })

    total_loss = sum(c["WK"] for c in component_losses)
    u_composite = total_loss / total_area if total_area > 0 else 0
    wwr = (total_window_area / total_area * 100) if total_area > 0 else 0

    loss_area_sum = sum(o["loss_area_WK"] for o in opening_results)
    loss_perim_sum = sum(o["loss_perim_WK"] for o in opening_results)

    def pct(v):
        return round(v / total_loss * 100, 1) if total_loss > 0 else 0

    return {
        "facade": {
            "width_m": fw,
            "height_m": fh,
            "total_area_m2": round(total_area, 2),
            "opaque_area_m2": round(opaque_area, 2),
            "opening_area_m2": round(total_opening_area, 2),
            "window_area_m2": round(total_window_area, 2),
            "door_area_m2": round(total_door_area, 2),
            "wwr_pct": round(wwr, 1),
        },
        "layout": {
            "pier_width_m": pier_width,
            "pier_count": len(piers),
            "openings_positioned": opening_results,
            "piers": piers,
        },
        "wall_buildup": wall_result,
        "openings": opening_results,
        "thermal_bridges": bridge_results,
        "heat_loss": {
            "wall_WK": round(opaque_loss, 3),
            "wall_pct": pct(opaque_loss),
            "openings_WK": round(loss_area_sum, 3),
            "openings_pct": pct(loss_area_sum),
            "perimeters_WK": round(loss_perim_sum, 3),
            "perimeters_pct": pct(loss_perim_sum),
            "bridges_WK": round(total_bridge_loss, 3),
            "bridges_pct": pct(total_bridge_loss),
            "total_WK": round(total_loss, 3),
        },
        "u_composite": round(u_composite, 4),
        "meets_passive_house": u_composite <= COMPLIANCE_TARGETS["passive_house_wall"],
        "meets_code": u_composite <= COMPLIANCE_TARGETS["code_wall"],
    }


# ============================================================================
# Output Formatting
# ============================================================================

def format_simple_output(result):
    lines = [
        "=== U-Value Calculator -- Simple Wall Build-Up ===",
        f"{'Layer':<25} {'Thick(mm)':>10} {'Cond(W/mK)':>12} {'R(m2K/W)':>12}",
        "-" * 62,
        f"{'Rsi (internal)':<25} {'--':>10} {'--':>12} {result['rsi_internal']:>12.4f}",
    ]
    for layer in result["layers"]:
        lines.append(
            f"{layer['name']:<25} {layer['thickness_mm']:>10} "
            f"{layer['conductivity']:>12.4f} {layer['r_value']:>12.4f}"
        )
    lines.extend([
        f"{'Rse (external)':<25} {'--':>10} {'--':>12} {result['rsi_external']:>12.4f}",
        "-" * 62,
        f"Total thickness:   {result['total_thickness_mm']:,} mm",
        f"Total R-value:     {result['total_r_value']:.4f} m2K/W",
        f"U-value:           {result['u_value']:.4f} W/m2K",
        "",
        f"Passive House (wall): 0.15 W/m2K -- "
        f"{'MEETS' if result['u_value'] <= 0.15 else 'DOES NOT MEET'}",
        f"Typical code (wall):  0.30 W/m2K -- "
        f"{'MEETS' if result['u_value'] <= 0.30 else 'DOES NOT MEET'}",
    ])
    return "\n".join(lines)


def format_facade_output(result):
    f = result["facade"]
    wb = result["wall_buildup"]
    hl = result["heat_loss"]
    layout = result["layout"]
    pier_w = layout["pier_width_m"]

    lines = []

    # --- FACADE ELEVATION DIAGRAM ---
    diagram = draw_facade_elevation(
        f["width_m"], f["height_m"],
        layout["openings_positioned"], pier_w
    )
    lines.append(diagram)

    # --- GEOMETRY SUMMARY ---
    lines.extend([
        "",
        "=" * 72,
        "  COMPOSITE FACADE THERMAL ANALYSIS",
        "=" * 72,
        "",
        "--- GEOMETRY ---",
        f"  Facade:            {f['width_m']:.1f}m x {f['height_m']:.1f}m = {f['total_area_m2']:.2f} m2",
        f"  Opaque wall:       {f['opaque_area_m2']:.2f} m2 ({f['opaque_area_m2']/f['total_area_m2']*100:.1f}%)",
        f"  Openings:          {f['opening_area_m2']:.2f} m2 ({f['opening_area_m2']/f['total_area_m2']*100:.1f}%)",
        f"  WWR:               {f['wwr_pct']:.1f}%",
        f"  Pier width:        {pier_w:.2f}m (x{layout['pier_count']} piers)",
    ])

    # --- WALL BUILD-UP ---
    lines.extend([
        "",
        "--- OPAQUE WALL BUILD-UP ---",
        f"  {'Layer':<20} {'Thick':>7} {'Cond':>10} {'R-value':>10}",
        f"  {'-'*49}",
        f"  {'Rsi (internal)':<20} {'--':>7} {'--':>10} {wb['rsi_internal']:>10.4f}",
    ])
    for layer in wb["layers"]:
        lines.append(
            f"  {layer['name']:<20} {str(layer['thickness_mm'])+'mm':>7} "
            f"{layer['conductivity']:>10.4f} {layer['r_value']:>10.4f}"
        )
    lines.extend([
        f"  {'Rse (external)':<20} {'--':>7} {'--':>10} {wb['rsi_external']:>10.4f}",
        f"  {'-'*49}",
        f"  Wall U-value: {wb['u_value']:.4f} W/m2K  |  "
        f"Thickness: {wb['total_thickness_mm']}mm",
    ])

    # --- OPENINGS TABLE ---
    if result["openings"]:
        lines.extend([
            "",
            "--- OPENINGS (positioned left-to-right, perimeter psi auto-detected) ---",
            f"  {'Name':<18} {'Type':<13} {'x(m)':>5} {'Size':>9} "
            f"{'Sill':>5} {'U':>5} {'Loss':>8}",
            f"  {'-'*67}",
        ])
        for op in result["openings"]:
            lines.append(
                f"  {op['name']:<18} {op['type']:<13} "
                f"{op['x_m']:>5.2f} "
                f"{op['width_m']:.1f}x{op['height_m']:.1f}m "
                f"{op['sill_m']:>4.1f}m "
                f"{op['u_value']:>5.2f} "
                f"{op['loss_total_WK']:>7.2f}W/K"
            )

    # --- THERMAL BRIDGES ---
    if result["thermal_bridges"]:
        lines.extend([
            "",
            "--- ADDITIONAL THERMAL BRIDGES ---",
            f"  {'Name':<28} {'psi(W/mK)':>10} {'Length':>8} {'Loss':>10}",
            f"  {'-'*58}",
        ])
        for tb in result["thermal_bridges"]:
            lines.append(
                f"  {tb['name']:<28} {tb['psi_WmK']:>10.3f} "
                f"{tb['length_m']:>7.1f}m {tb['loss_WK']:>9.3f}W/K"
            )

    # --- HEAT LOSS BREAKDOWN ---
    lines.extend([
        "",
        "--- HEAT LOSS BREAKDOWN ---",
        f"  Opaque wall:          {hl['wall_WK']:>8.2f} W/K  ({hl['wall_pct']:>5.1f}%)",
        f"  Openings (area):      {hl['openings_WK']:>8.2f} W/K  ({hl['openings_pct']:>5.1f}%)",
        f"  Opening perimeters:   {hl['perimeters_WK']:>8.2f} W/K  ({hl['perimeters_pct']:>5.1f}%)",
        f"  Additional bridges:   {hl['bridges_WK']:>8.2f} W/K  ({hl['bridges_pct']:>5.1f}%)",
        f"  {'-'*42}",
        f"  TOTAL:                {hl['total_WK']:>8.2f} W/K  (100.0%)",
    ])

    # --- RESULT ---
    lines.extend([
        "",
        "=" * 72,
        f"  COMPOSITE U-VALUE:   {result['u_composite']:.4f} W/m2K",
        f"  (ISO 13789 area-weighted, including all thermal bridges)",
        "=" * 72,
        "",
        f"  Passive House: 0.15 -- "
        f"{'MEETS' if result['meets_passive_house'] else 'DOES NOT MEET'}",
        f"  Code target:   0.30 -- "
        f"{'MEETS' if result['meets_code'] else 'DOES NOT MEET'}",
    ])

    # --- RECOMMENDATIONS ---
    lines.append("")
    lines.append("--- RECOMMENDATIONS ---")

    if f["wwr_pct"] > 40:
        lines.append(
            f"  ! WWR={f['wwr_pct']:.0f}% exceeds 40%. "
            "Reduce glazing area or upgrade to triple glazing."
        )

    worst_op = max(result["openings"], key=lambda o: o["loss_total_WK"],
                   default=None)
    if worst_op:
        savings = worst_op["area_m2"] * 0.4
        lines.append(
            f"  Highest-loss opening: {worst_op['name']} "
            f"({worst_op['loss_total_WK']:.2f} W/K). "
            f"Upgrading U by 0.4 saves {savings:.1f} W/K."
        )

    worst_tb = max(result["thermal_bridges"],
                   key=lambda t: t["loss_WK"], default=None)
    if worst_tb and worst_tb["psi_WmK"] > 0.10:
        lines.append(
            f"  Worst bridge: {worst_tb['name']} "
            f"(psi={worst_tb['psi_WmK']:.2f}, {worst_tb['loss_WK']:.2f} W/K). "
            "Use thermal break connectors."
        )

    return "\n".join(lines)


# ============================================================================
# Main
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="U-Value Calculator with facade layout engine.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
MODE 1 -- Simple wall:
  %(prog)s --layers '[{"name":"Brick","thickness_mm":102,"conductivity":0.77}]'

MODE 2 -- Composite facade with auto-layout:
  %(prog)s --facade '{
    "width":7,"height":3,
    "wall_layers":[{"name":"EPS","thickness_mm":150,"conductivity":0.034}],
    "openings":[
      {"type":"window","name":"W1","width":1.2,"height":1.5,"u_value":1.2},
      {"type":"door","name":"D1","width":0.9,"height":2.1,"u_value":1.8},
      {"type":"window","name":"W2","width":1.2,"height":1.5,"u_value":1.2}
    ]
  }'

  Openings are placed LEFT-TO-RIGHT in the order you list them.
  Equal pier widths are computed automatically.
  Doors default to sill=0 (ground). Windows default to sill=0.9m.
  Override with "sill" field per opening.

  Opening types: window, door, balcony_door
  Add "count":N to repeat an opening (expands to N individual instances).
  Add "psi":value to override perimeter thermal bridge psi.

  Thermal bridges (user-defined):
    "thermal_bridges": [{"name":"Balcony slab","psi":0.50,"length":3.6}]
        """,
    )

    parser.add_argument("--layers", type=str, default=None)
    parser.add_argument("--facade", type=str, default=None)
    parser.add_argument("--rsi-internal", type=float, default=0.13)
    parser.add_argument("--rsi-external", type=float, default=0.04)
    parser.add_argument("--json", action="store_true")

    args = parser.parse_args()

    if args.rsi_internal < 0 or args.rsi_external < 0:
        print("Error: Surface resistances cannot be negative.", file=sys.stderr)
        sys.exit(1)

    if args.facade and args.layers:
        print("Error: Use --layers OR --facade, not both.", file=sys.stderr)
        sys.exit(1)

    if not args.facade and not args.layers:
        print("Error: Provide --layers or --facade. Use --help.", file=sys.stderr)
        sys.exit(1)

    # --- MODE 1 ---
    if args.layers:
        try:
            layers = json.loads(args.layers)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON: {e}", file=sys.stderr)
            sys.exit(1)
        if not isinstance(layers, list):
            print("Error: --layers must be a JSON array.", file=sys.stderr)
            sys.exit(1)
        errors = validate_layers(layers)
        if errors:
            for e in errors:
                print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

        result = calculate_wall_uvalue(layers, args.rsi_internal, args.rsi_external)
        if args.json:
            result["meets_passive_house"] = result["u_value"] <= 0.15
            result["meets_code"] = result["u_value"] <= 0.30
            print(json.dumps(result, indent=2))
        else:
            print(format_simple_output(result))

    # --- MODE 2 ---
    elif args.facade:
        try:
            facade = json.loads(args.facade)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON: {e}", file=sys.stderr)
            sys.exit(1)
        if not isinstance(facade, dict):
            print("Error: --facade must be a JSON object.", file=sys.stderr)
            sys.exit(1)

        errors = validate_facade(facade)
        if errors:
            for e in errors:
                print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

        # Check openings fit
        total_op_w = sum(
            o["width"] * o.get("count", 1)
            for o in facade.get("openings", [])
        )
        if total_op_w >= facade["width"]:
            print(f"Error: Openings total width ({total_op_w:.2f}m) >= "
                  f"facade width ({facade['width']:.2f}m).", file=sys.stderr)
            sys.exit(1)

        result = calculate_facade(facade, args.rsi_internal, args.rsi_external)

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(format_facade_output(result))


if __name__ == "__main__":
    main()
