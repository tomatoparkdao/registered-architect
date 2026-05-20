# Calculator Reference -- Formulas and Methodology

Detailed formulas, constants, and methodology behind each of the seven
architectural calculators.

---

## 1. Area Calculator

### Formulas

```
GFA = Site Area x FAR
NGA = GFA x NTG Ratio
Units = floor(NGA / Avg Unit Size)
Population = Units x Persons per Unit
Parking = Units x Parking Ratio
```

### Key Ratios

| Building Type       | Typical NTG Ratio |
|--------------------|-------------------|
| Residential (apt)  | 0.75 - 0.85      |
| Office             | 0.80 - 0.88      |
| Retail             | 0.85 - 0.92      |
| Hospital           | 0.55 - 0.65      |
| Hotel              | 0.65 - 0.75      |
| School             | 0.70 - 0.80      |

NTG ratio accounts for circulation (corridors, lobbies, stairs,
elevators), structure (columns, walls), and service spaces (mechanical
rooms, electrical rooms, storage).

### Density Benchmarks

| Density Measure         | Low Density | Medium     | High Density |
|------------------------|-------------|------------|-------------|
| FAR                    | 0.5 - 1.0  | 1.5 - 3.0 | 4.0 - 15.0 |
| Dwelling units/hectare | 30 - 50    | 75 - 150   | 200 - 500+  |
| Persons/hectare        | 75 - 125   | 200 - 400  | 500 - 1500+ |

---

## 2. U-Value Calculator

### Formula

```
R_total = Rsi + sum(thickness_i / conductivity_i) + Rse
U = 1 / R_total
```

Where:
- Rsi = internal surface resistance (m2K/W)
- Rse = external surface resistance (m2K/W)
- thickness in meters (input in mm, converted)
- conductivity in W/mK

### Surface Resistance Values (ISO 6946)

| Position         | Direction of Heat Flow | Rsi (m2K/W) | Rse (m2K/W) |
|-----------------|----------------------|-------------|-------------|
| External wall   | Horizontal           | 0.13        | 0.04        |
| Internal floor  | Upward               | 0.10        | 0.10        |
| Internal ceiling| Downward             | 0.17        | 0.17        |
| Roof            | Upward               | 0.10        | 0.04        |
| Ground floor    | Downward             | 0.17        | 0.00*       |

*Ground floor uses separate calculation method (ISO 13370).

### Target U-Values

| Element       | Passive House | Typical Code (Climate Zone 5) | Minimum Code |
|--------------|---------------|-------------------------------|-------------|
| External wall| 0.10 - 0.15   | 0.25 - 0.30                   | 0.35 - 0.45 |
| Roof         | 0.10 - 0.12   | 0.15 - 0.20                   | 0.25 - 0.30 |
| Floor        | 0.10 - 0.15   | 0.20 - 0.25                   | 0.30 - 0.40 |
| Window       | 0.80 - 1.00   | 1.40 - 1.80                   | 2.00 - 2.80 |

### Common Material Conductivities

| Material                | Conductivity (W/mK) |
|------------------------|-------------------|
| Mineral wool           | 0.032 - 0.040     |
| EPS (expanded polystyrene) | 0.032 - 0.038 |
| XPS (extruded polystyrene) | 0.028 - 0.036 |
| PIR/PUR board          | 0.020 - 0.025     |
| Phenolic foam          | 0.018 - 0.022     |
| Concrete (dense)       | 1.13 - 1.93       |
| Concrete block (medium)| 0.51 - 0.70       |
| Brick (common)         | 0.62 - 0.77       |
| Timber (softwood)      | 0.13 - 0.16       |
| Plasterboard           | 0.16 - 0.25       |
| Steel                  | 50.0              |
| Glass                  | 1.05              |
| Air gap (unventilated) | 0.14 - 0.18*      |

*Effective conductivity for simplified calculation.

---

## 3. Daylight Calculator

### BRE Simplified Formula

```
DF = (Aw x T x theta) / (A_total x (1 - R^2)) x 100
```

Where:
- DF = average daylight factor (%)
- Aw = net glazed area of window (m2)
- T = glazing transmittance (typically 0.60 - 0.70 for double glazing)
- theta = visible sky angle factor (0 to 1, derived from sky angle)
- A_total = total area of all room surfaces (floor + ceiling + walls)
- R = area-weighted average reflectance of room surfaces

### Sky Angle Calculation

The visible sky angle is measured from the center of the window to the
top of any obstruction. For an unobstructed window:

```
theta_degrees = arctan((room_height - window_sill_height) / room_depth)
theta_factor = theta_degrees / 90
```

For obstructed conditions, theta is reduced based on the obstruction
angle.

### Total Room Surface Area

```
A_total = 2 x (W x D) + 2 x (W x H) + 2 x (D x H)
```

Where W = width, D = depth, H = height.

### Daylight Factor Targets

| Space Type          | Minimum DF | Recommended DF |
|--------------------|-----------|---------------|
| Living room        | 1.5%      | 2.0%          |
| Bedroom            | 1.0%      | 1.5%          |
| Kitchen            | 2.0%      | 2.5%          |
| Office             | 2.0%      | 3.0 - 5.0%   |
| Classroom          | 2.0%      | 5.0%          |
| Hospital ward      | 1.5%      | 2.5%          |
| Retail             | 2.0%      | 3.5%          |

---

## 4. Egress Calculator

### Occupant Load Factor (IBC Table 1004.5)

| Occupancy | Use                    | Factor (m2/person) | Factor (ft2/person) |
|-----------|------------------------|--------------------|---------------------|
| A-1       | Assembly, fixed seats  | 1.5 net            | 15 net              |
| A-2       | Assembly, food/drink   | 1.4 net            | 15 net              |
| A-3       | Assembly, worship      | 1.9 net            | 20 net (pews)       |
| B         | Business               | 9.3                | 100                 |
| E         | Educational            | 1.9 net            | 20 net              |
| F-1       | Factory, moderate      | 18.6               | 200                 |
| H         | High hazard            | 9.3                | 100                 |
| I-1       | Institutional, care    | 18.6               | 200                 |
| M         | Mercantile             | 5.6                | 60                  |
| R         | Residential            | 18.6               | 200                 |
| S-1       | Storage, moderate      | 46.5               | 500                 |
| U         | Utility                | 46.5               | 500                 |

### Number of Exits Required (IBC 1006.2)

| Occupant Load | Minimum Exits |
|--------------|--------------|
| 1 - 500      | 2            |
| 501 - 1000   | 3            |
| > 1000       | 4            |

### Exit Width Calculation

```
Total exit width (mm) = Occupant Load x Width Factor
Width per exit = Total width / Number of exits
```

Width factors:
- Stairs: 7.6 mm per person (0.3 inches)
- Other egress components: 5.1 mm per person (0.2 inches)
- Minimum single door width: 813 mm (32 inches clear)
- Minimum corridor width: 1118 mm (44 inches)

### Maximum Travel Distance (IBC Table 1017.2)

| Occupancy | Without Sprinklers (m/ft) | With Sprinklers (m/ft) |
|-----------|---------------------------|------------------------|
| A, E, M   | 61 / 200                  | 76 / 250              |
| B         | 61 / 200                  | 91 / 300              |
| F-1, S-1  | 61 / 200                  | 76 / 250              |
| H-1       | 23 / 75                   | 23 / 75               |
| R         | 61 / 200                  | 76 / 250              |
| U         | 61 / 200                  | 76 / 250              |

---

## 5. Structural Load Calculator

### Gravity Load Calculation

```
Load per floor = Tributary Area x (Dead Load + Live Load)
Total column load = Load per floor x Number of floors
Factored load = Tributary Area x (1.2 x DL + 1.6 x LL) x Floors
```

### Typical Dead Loads

| Construction Type              | Dead Load (kN/m2) |
|-------------------------------|-------------------|
| RC slab (200mm)               | 4.8               |
| RC slab (250mm)               | 6.0               |
| Steel deck + concrete (130mm) | 3.5               |
| Timber floor (joists)         | 1.5               |
| Superimposed dead (MEP, finish)| 1.0 - 1.5        |

### Typical Live Loads (IBC Table 1607.1)

| Occupancy Type  | Live Load (kN/m2) | Live Load (psf) |
|----------------|-------------------|-----------------|
| Residential    | 1.9               | 40              |
| Office         | 2.4               | 50              |
| Retail (ground)| 4.8               | 100             |
| Assembly       | 4.8               | 100             |
| Storage (light)| 6.0               | 125             |
| Parking garage | 2.4               | 50              |
| Hospital       | 3.8               | 80              |
| School         | 1.9               | 40              |

### Preliminary Column Sizing (RC)

```
Required area = Factored Load / (0.4 x fc')
Column dimension = sqrt(Required area)
```

Where fc' is concrete compressive strength (typically 30-40 MPa).

---

## 6. Energy Calculator

### Degree-Day Method

```
Q_transmission = U_avg x A_envelope x HDD x 24 / 1000   (kWh/yr)
Q_ventilation = 0.33 x n x V x HDD x 24 / 1000          (kWh/yr)
Q_internal = q_int x A_floor x hours / 1000              (kWh/yr)

Heating Demand = Q_transmission + Q_ventilation - Q_internal
Cooling Demand = (U_avg x A_envelope x CDD x 24 / 1000)
              + (q_int x A_floor x cooling_hours / 1000)

EUI = (Heating + Cooling) / A_floor
```

Where:
- n = ventilation rate (ACH)
- V = building volume = A_floor x assumed height (3.0m)
- q_int = internal gains (W/m2)
- hours = heating season hours (HDD/avg_temp_diff x 24)

### Passive House Targets

| Criterion                    | Target Value          |
|-----------------------------|-----------------------|
| Heating demand              | <= 15 kWh/m2/yr       |
| Cooling demand              | <= 15 kWh/m2/yr       |
| Primary energy (total)      | <= 120 kWh/m2/yr      |
| Airtightness (n50)          | <= 0.6 ACH @ 50 Pa    |
| Overheating frequency       | <= 10% of hours > 25C |

---

## 7. Cost Calculator

### Cost Database (USD/m2, 2025 baseline)

| Building Type  | Basic    | Standard | Premium  |
|---------------|----------|----------|----------|
| Residential   | 1,200    | 1,800    | 2,800    |
| Office        | 1,400    | 2,100    | 3,200    |
| Retail        | 1,000    | 1,500    | 2,400    |
| Hospital      | 2,500    | 3,500    | 5,000    |
| School        | 1,300    | 1,900    | 2,800    |
| Hotel         | 1,600    | 2,400    | 3,800    |

### Regional Cost Factors

| Region         | Factor |
|---------------|--------|
| North America | 1.00   |
| Europe        | 1.05   |
| Middle East   | 0.85   |
| Asia          | 0.65   |
| Australia     | 1.15   |

### Fee and Contingency Rates

| Item               | Basic  | Standard | Premium |
|-------------------|--------|----------|---------|
| Professional Fees | 10%    | 12%      | 15%     |
| Contingency       | 10%    | 7.5%     | 5%      |
| External Works    | 8-15%  | 8-15%    | 8-15%   |

```
Construction Cost = GFA x Base Rate x Regional Factor
Professional Fees = Construction Cost x Fee Rate
Contingency = Construction Cost x Contingency Rate
External Works = Construction Cost x 0.10 (if included)
Total = Construction Cost + Fees + Contingency + External
```
