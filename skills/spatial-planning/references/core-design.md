# Core Design — Comprehensive Reference

## 1. Core Design Principles

The vertical core is the single most consequential spatial element in any multi-storey building. It determines:
- Structural lateral stability (shear walls, braced frames)
- Vertical transportation capacity and quality of service
- Fire egress strategy and code compliance
- MEP distribution efficiency and maintenance access
- Floor plate usability, lettable area, and tenant subdivision flexibility

A well-designed core is compact, structurally efficient, code-compliant, and positioned to maximize the quality and quantity of usable space surrounding it.

### 1.1 Core Location Principles

| Core Position | Floor Plate Efficiency | Structural Performance | Daylight Impact | Tenant Flexibility |
|---|---|---|---|---|
| Central | Highest (min travel) | Excellent (torsion resistance) | Core blocks center; perimeter clear | Good but inflexible center zone |
| Side | High | Good (requires additional bracing) | Core wall limits one side; rest clear | Excellent open floor plate |
| End | Moderate | Fair (eccentric; needs supplementary) | One end lost; rest excellent | Very good single-direction floor |
| Dual (both ends) | Moderate | Good (balanced) | Both ends lost; middle excellent | Good for long floor plates |
| Split (2 offset) | Moderate | Very good (tuned for torsion) | Interrupts floor plate twice | Moderate complexity |
| External | Moderate | Requires transfer at base | No impact on interior daylight | Excellent interior freedom |

### 1.2 Core Area as Percentage of Gross Floor Plate

| Building Type | Typical Floor Plate GFA | Core Area | Core % |
|---|---|---|---|
| Residential tower (economy) | 500–700 m² | 35–55 m² | 7–9% |
| Residential tower (premium) | 700–1200 m² | 50–80 m² | 6–8% |
| Office tower (small) | 800–1200 m² | 160–280 m² | 20–25% |
| Office tower (large) | 1500–2500 m² | 375–625 m² | 22–28% |
| Office tower (supertall) | 2500–4000 m² | 700–1200 m² | 28–35% |
| Hotel | 600–1000 m² | 50–80 m² | 8–10% |
| Hospital | 2000–4000 m² | 200–400 m² | 8–12% |

---

## 2. Dimensioned Core Layouts by Building Type

### 2.1 Residential Tower — Single Stair Core (UK model, <18 m building height)

**Configuration:** 1 escape stair, 2 elevators, service risers, refuse chute, small lobby.

**Floor plate:** 500–700 m² GFA, 6–8 apartments per floor.

**Core dimensions:** approximately 4.5 m x 9.0 m = 40.5 m²

**Layout (from left to right, top to bottom):**

```
+------------------------------------------+
|  STAIR A     |  LIFT 1  |  LIFT 2  |RISER|
|  2400x4800   |  1600x   |  2000x   | 800 |
|  (1200 clear |  1400    |  1400    | x   |
|   width stair)|  (8-per) | (13-per) |2400 |
|              |          |          |     |
+--------------+----------+----------+-----+
|           LOBBY  4500 x 2400             |
|  (access to all apartments)              |
+------------------------------------------+
|  REFUSE |  DRY    |  WET    |  ELEC |DATA|
|  CHUTE  |  RISER  |  RISER  |  RISER|RISR|
|  600x600|  400x400|  400x600|  600x |400x|
|         |         |         |  400  |400 |
+------------------------------------------+
```

**Component dimensions:**
- Stair A: 2400 mm x 4800 mm shaft (1200 mm clear width, 2 x 8 risers per flight, 150 mm riser, 280 mm going)
- Lift 1: 8-person (630 kg), shaft 2150 x 1900 mm
- Lift 2: 13-person (1000 kg), shaft 2550 x 1900 mm (accessible/furniture lift)
- Lobby: 4500 x 2400 mm (meets 1500 mm wheelchair turning circle, 1.5 m clearance in front of lift doors)
- Refuse chute: 500 mm diameter in 600 x 600 mm fire-rated enclosure
- Service risers: see Section 4

**Compliance notes:**
- Single stair permitted for residential buildings <11 m in England/Wales (Approved Document B), <18 m in Scotland
- Stair pressurization not required <18 m but smoke ventilation at head of stair (1.0 m² AOV or mechanical)
- Maximum travel distance from flat entrance door to stair: 7.5 m (enhanced, open plan) or 30 m (protected corridor) per ADB

### 2.2 Residential Tower — Dual Stair Core (IBC model, USA)

**Configuration:** 2 escape stairs, 2–3 elevators, service risers, lobby.

**Floor plate:** 700–1200 m² GFA, 6–10 apartments per floor.

**Core dimensions:** approximately 6.0 m x 12.0 m = 72 m²

**Layout:**

```
+-----------------------------------------------------+
| STAIR A  |  LIFT 1  |  LIFT 2  | LIFT 3  | STAIR B  |
| 2700x    |  1600x   |  2000x   | 1600x   | 2700x    |
| 5400     |  1400    |  1400    | 1400    | 5400     |
|          |  (8-per) | (13-per) | (8-per) |          |
+----------+----------+----------+---------+----------+
|               LOBBY  6000 x 2400                     |
+-----------------------------------------------------+
| ELEC | DATA | WET  | DRY  | REFUSE | HVAC  | METER  |
| 600x | 400x | 400x | 400x | 600x   | 800x  | ROOM   |
| 400  | 400  | 600  | 400  | 600    | 1200  | 1500x  |
|      |      |      |      |        |       | 1000   |
+-----------------------------------------------------+
```

**Compliance notes (IBC):**
- Two stairs required for all residential buildings >1 storey or >10 occupants per floor
- Stair separation: min 1/3 diagonal distance (sprinklered) or 1/2 diagonal (unsprinklered) — IBC 1007.1.1
- Travel distance from any unit door to nearest stair: max 76 m sprinklered (IBC 1017.2)
- Common path of egress travel: max 23 m (IBC Table 1006.2.1)
- Each stair: min 1118 mm (44 in) clear width
- Elevator lobby: 2-hour fire-rated enclosure for buildings >128 m (IBC 403.6.1)

### 2.3 Office Tower — Central Core (30 storeys)

**Configuration:** 2 escape stairs, 6–8 passenger elevators (2 banks), 1 goods elevator, fire-fighting elevator, MEP risers, male/female/accessible toilets, cleaners store.

**Floor plate:** 1500–2000 m² GFA.

**Core dimensions:** approximately 18.0 m x 18.0 m = 324 m² (core ratio 18–22%)

**Schematic layout:**

```
+---------------------------------------------------------------+
|        |  LOW-RISE BANK (4 LIFTS)   |  HIGH-RISE BANK (4 LIFTS)|
| STAIR  |  2550 x 1900 each x 4      |  2550 x 1900 each x 4   |
|   A    |  (13-person, 1000 kg)       |  (13-person, 1000 kg)    |
| 2700x  |                             |                          |
| 6000   |  LOBBY 4800 x 2400          |  LOBBY 4800 x 2400       |
|        +-----------------------------+--------------------------+
|        | GOODS LIFT   | FIRE LIFT    |         STAIR B          |
|        | 2900 x 3200  | 2550 x 2400  |         2700 x 6000      |
+--------+--------------+--------------+--------------------------+
| FEMALE WC   | MALE WC     | ACC WC x2 | CLEANERS | RISERS      |
| 12 cubicles | 6 urinals   | 2200x1500 | 1500x    | ELEC|DATA|  |
| 4 basins    | 6 cubicles  | each      | 1500     | 800x|600x|  |
| 5400x3600   | 4 basins    |           |          | 600 |600 |  |
|             | 5400x3600   |           |          |     |    |  |
+-------------+-------------+-----------+----------+-----+----+  |
|        WET RISER        |  DRY RISER  |  HVAC RISER    | SMOKE |
|        600 x 600        |  300 x 300  |  1200 x 800    | SHAFT |
|                         |             |                | 600x  |
|                         |             |                | 600   |
+-------------------------+-------------+----------------+-------+
```

**Toilet provision (BS 6465-1 / IBC):**
- Office: 1 WC per 15 females, 1 WC per 25 males + 1 urinal per 25 males
- For 200 persons per floor (50/50 gender split): 7F WCs + 4M WCs + 4 urinals + 2 accessible
- Accessible WC: 1500 x 2200 mm min (1500 mm turning circle + WC pan + basin)

**Elevator bank design:**
- Low-rise bank (floors G–15): 4 elevators at 2.5 m/s
- High-rise bank (floors 15–30): 4 elevators at 4.0 m/s
- Goods lift: 2500 kg at 1.6 m/s (serves all floors)
- Firefighter lift: 1000 kg min (EN 81-72), dedicated shaft, 2-hour rated, lobby with pressurization

### 2.4 Hospital — Dual Escape Core

**Configuration:** 2 progressive horizontal evacuation zones, each with escape stair, bed elevator, passenger elevators, MEP risers.

**Floor plate:** 2500–4000 m² GFA per floor.

**Core A (one end) dimensions:** approximately 8.0 m x 15.0 m = 120 m²

**Layout per core:**

```
+--------------------------------------------------+
| STAIR    |  BED LIFT    |  PASS LIFT 1 | PASS LIFT 2 |
| 1500x    |  2400x2700   |  2000x1400   | 2000x1400   |
| 6000     |  (2500 kg)   |  (1000 kg)   | (1000 kg)   |
| (1500mm  |              |              |             |
|  wide)   |              |              |             |
+----------+--------------+--------------+-------------+
|              LOBBY  8000 x 3000                       |
|   (bed turning, wheelchair passing, trolley storage)  |
+-------------------------------------------------------+
| DIRTY    | CLEAN   | ELEC  | DATA | WET   | HVAC     |
| UTILITY  | UTILITY | RISER | RISR | RISER | RISER    |
| 2400x    | 2400x   | 800x  | 600x | 600x  | 1500x   |
| 2400     | 2400    | 600   | 600  | 800   | 1200    |
+----------+---------+-------+------+-------+----------+
```

**Hospital-specific requirements:**
- Bed elevator: min cab 1100 x 2100 mm (EN 81-70); preferred 2400 x 2700 mm for bed + 2 attendants
- Corridor width at core: min 2400 mm (bed passing), recommended 3000 mm
- Progressive horizontal evacuation: patients move horizontally into adjacent fire compartment, not down stairs
- Fire compartment size: max 750 m² for sleeping risk (NHS HTM 05-02)
- Stairs: min 1500 mm wide for evacuation of non-ambulant patients using evac chairs
- Stair lobbies: 2400 x 2400 mm min for bed/chair maneuvering
- Dedicated dirty/clean utility rooms adjacent to core on each floor

### 2.5 Retail — Distributed Cores

**Configuration:** Multiple small cores distributed across a large floor plate, each serving a zone of 2000–4000 m².

**Floor plate:** 5000–20,000 m² GFA (shopping center floor).

**Core type A (anchor zone):** 5.0 m x 8.0 m = 40 m²

```
+-------------------------------+
| STAIR   | GOODS LIFT | RISERS |
| 1500x   | 2900x3200  | 1000x  |
| 5400    | (2500 kg)  | 2400   |
|         |            | (all)  |
+-------------------------------+
```

**Core type B (mall zone):** 4.0 m x 6.0 m = 24 m²

```
+------------------------+
| STAIR   | PASS LIFT x2 |
| 1200x   | 2000x1400    |
| 4800    | each         |
+---------+--------------+
| RISERS  | CLEANERS     |
| 600x    | 1200x1200    |
| 1800    |              |
+---------+--------------+
```

**Retail-specific requirements:**
- Travel distance: max 45 m to nearest exit in sprinklered retail (IBC)
- Escalators supplement cores for customer flow (not counted as egress in most codes)
- Service corridors (BOH): min 2400 mm wide for pallet jacks, accessible from goods lifts
- Each anchor tenant requires independent goods access and fire exit
- Cores positioned to serve 30–45 m radius zones

### 2.6 Hotel — Double-Loaded Corridor with End Stairs

**Configuration:** Central elevator lobby with stairs at corridor ends. Long, narrow core distribution.

**Floor plate:** 600–1200 m² GFA, 16–30 rooms per floor.

**Central lobby core:** 6.0 m x 6.0 m = 36 m²

```
+-----------------------------------+
| LIFT 1   | LIFT 2   | LIFT 3      |
| 1600x    | 2000x    | 1600x       |
| 1400     | 1400     | 1400        |
| (8-per)  | (13-per) | (8-per)     |
+----------+----------+-------------+
|      LOBBY 6000 x 2400            |
+-----------------------------------+
| LINEN    | HOUSEKEEP | RISERS     |
| STORE    | CLOSET    | (ALL)      |
| 2400x    | 1800x     | 1200x     |
| 1800     | 1500      | 1800      |
+----------+-----------+-----------+
```

**End stair cores (x2):** 2.7 m x 5.4 m = 14.6 m² each

```
+-----------------+
| STAIR           |
| 1200 clear width|
| 2700 x 5400    |
| (fire-rated     |
|  enclosure)     |
+-----------------+
```

**Hotel-specific requirements:**
- Corridor: 1350–1500 mm wide (guests with luggage, housekeeping carts)
- Max corridor length (dead-end): 15 m sprinklered to nearest stair (IBC)
- Room doors: recessed 300 mm from corridor wall (Neufert recommendation, prevents door collision)
- Linen/housekeeping stores: one per floor, adjacent to elevator lobby, 10–15 m² per 20 rooms
- Room service elevator: one dedicated service elevator per 150 rooms
- Firefighter access: per IBC 403 for buildings >128 m

---

## 3. Structural Role of the Core

### 3.1 Core as Lateral System

In most buildings over 10 storeys, the core provides the primary lateral resistance:

**Shear wall core:**
- Concrete walls 200–500 mm thick (increasing with height)
- Coupled shear walls between stair/lift openings via link beams (coupling ratio 40–70%)
- Typical stiffness: sufficient for buildings up to ~40 storeys without additional lateral systems
- Wall reinforcement: 0.25–4% depending on height and seismic zone

**Core + outrigger system (for supertall):**
- Core provides primary shear and moment resistance
- Outrigger trusses (1–2 storey deep) connect core to perimeter mega-columns at 1/3 and 2/3 height
- Belt trusses engage multiple perimeter columns
- Reduces core overturning moment by 20–40%
- Example: Shanghai Tower, Taipei 101

**Core stiffness-to-weight ratio:**
- Target: building natural period T = 0.1 × number of storeys (rule of thumb)
- For 40-storey office: T ≈ 4.0 s; wind design dominates over seismic in most non-seismic regions
- Core wall thickness sized for H/500 drift limit (total) and h/400 inter-storey drift (IBC/Eurocode)

### 3.2 Core Construction Sequence

- Core typically constructed in advance of floor slabs (jump-form or slip-form)
- Jump-form cycle: 1 floor every 4–7 days per core
- Slip-form: continuous pour at 150–300 mm/hour (24/7 operation); for simple cores
- Floor slabs connect to core via starter bars or couplers
- Tolerances: ±15 mm plumb over 30 storeys (BS 5606)

---

## 4. MEP Riser Shaft Sizing

### 4.1 Electrical Risers

| Building Type | Floor Area (m²) | Riser Size (W x D mm) | Notes |
|---|---|---|---|
| Residential (per core) | 500–700 | 400 x 400 | Consumer units, sub-mains |
| Office (per core) | 1500–2000 | 800 x 600 | Busbar rising main, distribution boards |
| Office (large, per core) | 2000–3000 | 1000 x 800 | Dual busbar, generator feeds |
| Hotel | 600–1000 | 600 x 400 | Consumer units, emergency lighting |
| Hospital | 2000–4000 | 1200 x 800 | Essential/non-essential separation, IPS |

### 4.2 Data / Telecommunications Risers

| Building Type | Riser Size (W x D mm) | Notes |
|---|---|---|
| Residential | 300 x 300 | Fiber spine, copper to units |
| Office | 600 x 600 | Multiple carriers, fiber + copper, cable trays |
| Hospital | 800 x 600 | Redundant paths, nurse call, BMS, telemetry |

**Separation:** Min 300 mm from electrical risers or in separate fire-rated compartment to prevent EMI.

### 4.3 Water Risers (Potable + Fire)

| Component | Pipe Diameter (mm) | Riser Space (mm) | Notes |
|---|---|---|---|
| Cold water (residential, per stack) | 35–54 | 150 x 150 | Boosted above 10 storeys |
| Hot water (residential, per stack) | 28–42 | 150 x 150 | Secondary return above 10 storeys |
| Fire wet riser | 100–150 | 300 x 300 | Landing valve each floor, 2-hour enclosure |
| Fire dry riser | 100 | 300 x 300 | Inlet at ground, outlet valves per floor |
| Sprinkler main | 100–150 | 300 x 300 | Zone valves at plant floors |

### 4.4 Waste / Drainage Risers

| Component | Pipe Diameter (mm) | Riser Space (mm) | Notes |
|---|---|---|---|
| Soil stack (WC group) | 100–150 | 250 x 250 | One per bathroom group; vertical with min offset |
| Waste stack (basin/shower) | 50–75 | 150 x 150 | Can combine with soil above ground |
| Vent stack | 75–100 | 150 x 150 | Air admittance valves (AAVs) may reduce |
| Rainwater downpipe | 75–150 | 200 x 200 | One per 100–200 m² roof area |

### 4.5 HVAC Risers

| System Type | Riser Size per Floor (W x D mm) | Notes |
|---|---|---|
| Central AHU (VAV) | 1200 x 800 (supply) + 800 x 600 (return) | Vertical risers from central plant |
| Floor-by-floor AHU | No vertical duct riser | AHU in ceiling void each floor |
| Fan coil + DOAS | 600 x 400 (OA) + 200 x 200 (condensate) | Chilled/heating water in wet riser |
| Chilled water pipes | 4 x 100–200 mm dia (flow/return x 2) | In wet riser or dedicated shaft |
| Heating water pipes | 2 x 50–100 mm dia (flow/return) | In wet riser |
| Smoke extract duct | 800 x 800 min | Fire-rated, dedicated shaft |
| Kitchen extract | 600 x 600 min | 2-hour fire-rated (grease duct) |

### 4.6 Total Riser Shaft Sizing Summary

**Typical office tower (1500 m² floor plate):**

| Riser | Size (mm) | Area (m²) |
|---|---|---|
| Electrical | 800 x 600 | 0.48 |
| Data | 600 x 600 | 0.36 |
| Water (potable) | 400 x 400 | 0.16 |
| Water (fire) | 300 x 300 | 0.09 |
| Drainage | 400 x 400 | 0.16 |
| HVAC (if central plant) | 1200 x 800 + 800 x 600 | 1.44 |
| Smoke extract | 800 x 800 | 0.64 |
| **Total riser area** | | **3.33 m²** |

Add 20% for access space, fire stopping, and future capacity: **~4.0 m²** total riser zone per floor.

---

## 5. Fire-Rating Requirements for Core Elements

| Element | ≤4 Storeys | 5–28 m Height | >28 m Height | >50 m Height |
|---|---|---|---|---|
| Stair enclosure (IBC) | 1 hour | 2 hours | 2 hours | 2 hours + pressurization |
| Elevator shaft (IBC) | 1 hour | 2 hours | 2 hours | 2 hours + lobby |
| MEP riser shaft | 1 hour | 2 hours | 2 hours | 2 hours |
| Stair doors | FD30S | FD60S | FD60S | FD60S + lobby |
| Elevator lobby | Not required | Not required | Required (IBC 403) | Required + pressurization |
| Smoke control | Natural AOV | Natural or mech | Mechanical pressurization | Mechanical + backup power |

**UK Approved Document B equivalents:**
- <5 m: 30 min enclosure, FD20S doors
- 5–18 m: 60 min enclosure, FD30S doors
- 18–30 m: 60 min enclosure, FD30S doors, pressurization or lobby
- >30 m: 120 min enclosure, FD60S doors, pressurization mandatory

---

## 6. Core Design Optimization Strategies

### 6.1 Compact Core Strategies

1. **Machine-room-less (MRL) elevators:** Eliminate machine room at roof, saving ~15 m² per elevator bank
2. **Counterweight in shaft rear:** Allows shallower shaft depth
3. **Shared lobbies:** Single lobby serving stair and elevators reduces corridor area
4. **Back-to-back toilets:** Male and female sharing one riser wall saves 3–5 m² per floor
5. **Combined riser shafts:** Electrical + data in one fire-rated enclosure (with EMI separation) saves 0.5 m² per floor
6. **Destination dispatch elevators:** Reduce required number of elevators by 15–30% through intelligent allocation

### 6.2 Flexible Core Strategies

1. **Subdivide elevator banks:** Allow independent tenant access to different elevator groups
2. **Turnstile integration:** Security gates in lobby for multi-tenant buildings
3. **Tenant toilet option:** Provide core toilet provision but allow tenants to add private facilities
4. **Pre-provisioned risers:** Oversize shafts 10–15% for future capacity (fiber, cooling, PV feeds)
5. **Modular core construction:** Prefabricated toilet/riser pods installed floor-by-floor (20–30% faster)
