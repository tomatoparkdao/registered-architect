---
name: architect-calculator
description: >
  Seven Python-based architectural calculators for common design computations:
  area and density calculations (GFA, NGA, unit count, population, parking),
  thermal U-value analysis for multi-layer constructions, daylight factor
  estimation using BRE methodology, egress compliance checking (occupant load,
  exit width, travel distance), structural gravity load and tributary area
  calculations, annual energy demand estimation via degree-day method, and
  construction cost estimation by building type, quality, and region.
---

# Architect Calculator

A suite of seven command-line Python calculators for rapid architectural
design computations. Each calculator accepts parameters via command-line
arguments, validates inputs, and produces either human-readable or
JSON-structured output.

All scripts are located in the `scripts/` directory and can be run with:

```
python scripts/<calculator_name>.py [arguments]
```

Add `--json` to any command for structured JSON output suitable for
piping into other tools or automation workflows.

---

## 1. Area Calculator (`area_calculator.py`)

Calculates development density metrics from site area and floor area
ratio (FAR), including gross floor area, net usable area, residential
unit count, estimated population, and parking requirement.

### Parameters

| Parameter          | Flag               | Default | Unit   | Description                          |
|--------------------|--------------------|---------|--------|--------------------------------------|
| Site Area          | `--site-area`      | Required| m2     | Total site/plot area                 |
| Floor Area Ratio   | `--far`            | Required| ratio  | Permitted FAR / plot ratio           |
| Net-to-Gross Ratio | `--ntg-ratio`      | 0.80    | ratio  | NGA as fraction of GFA (0.0-1.0)    |
| Avg Unit Size      | `--avg-unit-size`  | 85      | m2     | Average residential unit area        |
| Persons per Unit   | `--persons-per-unit`| 2.5    | persons| Average household size               |
| Parking Ratio      | `--parking-ratio`  | 1.0     | spaces | Parking spaces per dwelling unit     |

### Example

```bash
python scripts/area_calculator.py --site-area 5000 --far 2.5 --ntg-ratio 0.82
```

### Sample Output

```
=== Area & Density Calculator ===
Site Area:            5,000.00 m2
Floor Area Ratio:     2.50
---------------------------------------
Gross Floor Area:     12,500.00 m2
Net-to-Gross Ratio:   0.82
Net Gross Area:       10,250.00 m2
---------------------------------------
Average Unit Size:    85.00 m2
Estimated Units:      120
Persons per Unit:     2.50
Estimated Population: 300
---------------------------------------
Parking Ratio:        1.00 spaces/unit
Parking Spaces:       120
```

---

## 2. U-Value Calculator (`uvalue_calculator.py`)

Calculates the thermal transmittance (U-value) of a multi-layer wall,
roof, or floor construction by summing thermal resistances of each layer
plus surface resistances.

### Parameters

| Parameter       | Flag              | Default | Unit        | Description                     |
|----------------|-------------------|---------|-------------|---------------------------------|
| Layers         | `--layers`        | Required| JSON string | Array of layer objects           |
| Rsi Internal   | `--rsi-internal`  | 0.13    | m2K/W       | Internal surface resistance      |
| Rsi External   | `--rsi-external`  | 0.04    | m2K/W       | External surface resistance      |

Each layer object: `{"name": "...", "thickness_mm": N, "conductivity": N}`

### Example

```bash
python scripts/uvalue_calculator.py --layers '[
  {"name": "Brick", "thickness_mm": 102, "conductivity": 0.77},
  {"name": "Cavity air gap", "thickness_mm": 50, "conductivity": 0.18},
  {"name": "Mineral wool", "thickness_mm": 100, "conductivity": 0.035},
  {"name": "Concrete block", "thickness_mm": 140, "conductivity": 1.13},
  {"name": "Plaster", "thickness_mm": 13, "conductivity": 0.16}
]'
```

### Sample Output

```
=== U-Value Calculator ===
Layer                Thickness(mm)  Conductivity(W/mK)  R-value(m2K/W)
---------------------------------------------------------------------------
Rsi (internal)       --             --                   0.1300
Brick                102            0.770                0.1325
Cavity air gap       50             0.180                0.2778
Mineral wool         100            0.035                2.8571
Concrete block       140            1.130                0.1239
Plaster              13             0.160                0.0813
Rse (external)       --             --                   0.0400
---------------------------------------------------------------------------
Total R-value:       3.6425 m2K/W
U-value:             0.2745 W/m2K

Passive House target (wall):   0.15 W/m2K  -- DOES NOT MEET
Typical code target (wall):    0.30 W/m2K  -- MEETS TARGET
```

---

## 3. Daylight Calculator (`daylight_calculator.py`)

Estimates average daylight factor for a side-lit room using the BRE
simplified formula.

### Parameters

| Parameter             | Flag                      | Default | Unit  |
|----------------------|---------------------------|---------|-------|
| Room Width            | `--room-width`            | Required| m     |
| Room Depth            | `--room-depth`            | Required| m     |
| Room Height           | `--room-height`           | Required| m     |
| Window Width          | `--window-width`          | Required| m     |
| Window Height         | `--window-height`         | Required| m     |
| Window Sill Height    | `--window-sill-height`    | Required| m     |
| Glazing Transmittance | `--glazing-transmittance` | 0.65    | ratio |
| Average Reflectance   | `--average-reflectance`   | 0.50    | ratio |

### Example

```bash
python scripts/daylight_calculator.py \
  --room-width 4.0 --room-depth 6.0 --room-height 3.0 \
  --window-width 2.5 --window-height 1.8 --window-sill-height 0.9
```

### Sample Output

```
=== Daylight Factor Calculator ===
Room:     4.00m W x 6.00m D x 3.00m H
Window:   2.50m W x 1.80m H (sill at 0.90m)
---------------------------------------
Window Area:             4.50 m2
Total Room Surface Area: 96.00 m2
Window-to-Floor Ratio:   18.75%
Glazing Transmittance:   0.65
Average Reflectance:     0.50
Visible Sky Angle:       60.1 deg
---------------------------------------
Average Daylight Factor: 2.34%

Assessment: ADEQUATE (target >= 2.0% for habitable rooms)
```

---

## 4. Egress Calculator (`egress_calculator.py`)

Calculates occupant load, required number of exits, minimum exit widths,
and travel distance compliance per IBC.

### Parameters

| Parameter       | Flag               | Default  | Description                     |
|----------------|--------------------|---------|---------------------------------|
| Floor Area      | `--floor-area`     | Required | Net floor area in m2            |
| Occupancy Type  | `--occupancy-type` | Required | IBC occupancy (A-1 to U)        |
| Sprinklered     | `--sprinklered`    | False    | Flag: building is sprinklered   |
| Num Stories     | `--num-stories`    | 1        | Number of stories               |

### Example

```bash
python scripts/egress_calculator.py --floor-area 800 --occupancy-type B --sprinklered --num-stories 4
```

### Sample Output

```
=== Egress Calculator ===
Floor Area:        800.00 m2
Occupancy Type:    B (Business)
Sprinklered:       Yes
Number of Stories: 4
---------------------------------------
Occupant Load Factor:   9.3 m2/person
Occupant Load:          86 persons
---------------------------------------
Required Exits:         2
Min Exit Width (total): 1,376 mm
Width per Exit:         688 mm
Min Door Width:         813 mm (32 inches)
---------------------------------------
Max Travel Distance:    91.0 m (300 ft) [sprinklered]
Max Common Path:        23.0 m (75 ft)
Max Dead End:           15.0 m (50 ft)

COMPLIANCE: Review travel distances on plans.
```

---

## 5. Structural Load Calculator (`structural_load_calculator.py`)

Calculates tributary area gravity loads for preliminary structural sizing.

### Parameters

| Parameter       | Flag               | Default | Unit     | Description                  |
|----------------|--------------------|---------|---------|-----------------------------|
| Tributary Area  | `--tributary-area` | Required| m2       | Column tributary area        |
| Num Floors      | `--num-floors`     | Required| integer  | Number of supported floors   |
| Dead Load       | `--dead-load`      | 4.5     | kN/m2    | Dead load per floor          |
| Live Load       | `--live-load`      | auto    | kN/m2    | Live load (auto per occ.)    |
| Occupancy Type  | `--occupancy-type` | office  | string   | For auto live load selection  |

### Example

```bash
python scripts/structural_load_calculator.py --tributary-area 36 --num-floors 8 --occupancy-type office
```

### Sample Output

```
=== Structural Load Calculator ===
Tributary Area:    36.00 m2
Number of Floors:  8
---------------------------------------
Dead Load:         4.50 kN/m2 per floor
Live Load:         2.50 kN/m2 per floor (office)
Total per Floor:   7.00 kN/m2
---------------------------------------
Load per Floor:    252.00 kN
Total Column Load: 2,016.00 kN (8 floors)
Factored Load:     2,822.40 kN (1.2D + 1.6L)
---------------------------------------
Preliminary Column: ~400x400 mm RC (fc'=35 MPa)
```

---

## 6. Energy Calculator (`energy_calculator.py`)

Estimates annual heating and cooling energy demand using the degree-day
method.

### Parameters

| Parameter           | Flag                   | Default | Unit    | Description                    |
|--------------------|------------------------|---------|---------|-------------------------------|
| Floor Area          | `--floor-area`         | Required| m2      | Conditioned floor area         |
| Envelope Area       | `--envelope-area`      | Required| m2      | Total envelope area            |
| Average U-value     | `--average-u-value`    | Required| W/m2K   | Area-weighted average U        |
| Heating Degree Days | `--heating-degree-days`| Required| Kd      | Annual HDD (base 18C)         |
| Cooling Degree Days | `--cooling-degree-days`| Required| Kd      | Annual CDD (base 24C)         |
| Ventilation Rate    | `--ventilation-rate`   | 0.5     | ACH     | Air changes per hour           |
| Internal Gains      | `--internal-gains`     | 5.0     | W/m2    | Internal heat gains            |

### Example

```bash
python scripts/energy_calculator.py \
  --floor-area 500 --envelope-area 800 --average-u-value 0.35 \
  --heating-degree-days 3000 --cooling-degree-days 500
```

### Sample Output

```
=== Energy Calculator ===
Floor Area:           500.00 m2
Envelope Area:        800.00 m2
Average U-value:      0.35 W/m2K
---------------------------------------
Heating Degree Days:  3,000 Kd
Cooling Degree Days:  500 Kd
Ventilation Rate:     0.50 ACH
Internal Gains:       5.00 W/m2
---------------------------------------
Transmission Loss:    6,720.00 kWh/yr
Ventilation Loss:     4,050.00 kWh/yr
Internal Gains:       -2,190.00 kWh/yr
Heating Demand:       8,580.00 kWh/yr
---------------------------------------
Cooling Demand:       2,356.00 kWh/yr
---------------------------------------
Total Demand:         10,936.00 kWh/yr
EUI:                  21.87 kWh/m2/yr

Passive House target: 15 kWh/m2/yr -- DOES NOT MEET
```

---

## 7. Cost Calculator (`cost_calculator.py`)

Estimates construction cost based on building type, quality level, and
geographic region.

### Parameters

| Parameter        | Flag                | Default      | Description                        |
|-----------------|---------------------|--------------|------------------------------------|
| GFA              | `--gfa`             | Required     | Gross floor area in m2             |
| Building Type    | `--building-type`   | Required     | residential/office/retail/hospital/school/hotel |
| Quality          | `--quality`         | standard     | basic/standard/premium             |
| Region           | `--region`          | north-america| north-america/europe/middle-east/asia/australia |
| Include External | `--include-external`| False        | Flag: include site works           |

### Example

```bash
python scripts/cost_calculator.py --gfa 5000 --building-type office --quality premium --region europe
```

### Sample Output

```
=== Construction Cost Calculator ===
Gross Floor Area:   5,000.00 m2
Building Type:      Office
Quality Level:      Premium
Region:             Europe
---------------------------------------
Base Cost Rate:     2,800.00 USD/m2
Construction Cost:  14,000,000 USD
---------------------------------------
Professional Fees (12%):  1,680,000 USD
Contingency (7.5%):       1,050,000 USD
External Works:           --
---------------------------------------
Total Development Cost:   16,730,000 USD
Cost per m2 (total):      3,346.00 USD/m2
```

---

## Methodology Reference

Detailed formulas and methodology for each calculator are documented in
`references/calculator-reference.md`.

## Error Handling

All calculators validate inputs and provide clear error messages:
- Missing required parameters display usage help
- Out-of-range values are rejected with explanatory messages
- Invalid occupancy types list accepted values
- Malformed JSON input shows expected format

## Integration

JSON output (`--json` flag) enables integration with:
- Other scripts in the pipeline
- Spreadsheet tools (parse JSON)
- Web dashboards
- Automated reporting systems
- BIM parameter injection
