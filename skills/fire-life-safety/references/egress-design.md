# Egress Design -- Deep Reference

## Overview

Egress design is among the architect's most critical responsibilities. A well-
designed egress system is invisible to occupants during normal use but becomes
the difference between life and death in a fire or emergency. This reference
covers stair configurations, refuge areas, firefighting access, travel distance
tables, stair width calculations with worked examples, evacuation modeling
basics, and case studies of egress design in complex buildings.

---

## Section 1: Stair Configurations

### Conventional Enclosed Stair

The most common escape stair configuration:
- Single straight-run or return stair enclosed in fire-rated walls
- Enclosure rating: 1 hr for stairs serving 4 or fewer stories; 2 hr for
  more than 4 stories (IBC 1023.2; ADB similar by height)
- Typical plan dimensions:
  - Single straight run: 3000 x 6000 mm (fits 1100 mm stair + 2 landings)
  - Return stair (U-shape): 2700 x 5400 mm minimum (2 x 1100 mm flights +
    150 mm center gap + walls)
  - Scissor stair core: see below

**Stair geometry requirements (IBC 1011):**
- Riser height: 102-178 mm (4-7 in); uniform within flight
- Tread depth: minimum 279 mm (11 in); uniform within flight
- Nosing: maximum 32 mm (1.25 in) projection; radius max 13 mm (0.5 in)
- Landing: minimum depth equal to stair width; minimum width equal to stair width
- Headroom: minimum 2030 mm (80 in) measured vertically from tread nosing to
  soffit above
- Handrails: both sides, continuous, 865-965 mm (34-38 in) above tread nosing;
  extensions per ADA at top and bottom

### Scissor Stairs

Two independent stairs interlocking within a single structural core, each
serving alternate floors or both serving every floor with separate entries:

- Each stair is a fully independent fire-rated enclosure
- Fire-rated wall (minimum 2 hr) separates the two stairs within the core
- Each stair has its own smoke lobby at every floor
- Each stair discharges independently at ground level (separate exit
  discharge paths to the public way)
- Ventilation: each stair independently pressurized or naturally ventilated

**Advantages:**
- Compact core: significant floor area savings compared to two separate cores
- Structural efficiency: single core for lateral stability
- Two protected escape routes from every floor

**Limitations:**
- Complexity: smoke lobby design at each floor requires careful spatial planning
- Common wall: while fire-rated, a single construction defect could compromise
  both stairs (IBC and ADB require demonstration that stairs are truly
  independent)
- Pressurization: air handling for two independent systems within one core is
  complex

**Typical plan arrangement:**
- Core dimensions: approximately 5400 x 6000 mm minimum for two 1100 mm stairs
  with lobbies
- Each stair: 1100 mm clear width between walls
- Each lobby: minimum 1500 mm depth for wheelchair refuge + door swings
- Separating wall: continuous from foundation to roof, 2-hour fire-rated minimum

### Pressurized Stairs

Stairs with mechanical pressurization to resist smoke infiltration:

**IBC requirements (Section 909.20, Section 403.5.4 for high-rise):**
- Minimum pressure: 12.5 Pa (0.05 in w.g.) with all doors closed
- Maximum pressure: 87 Pa (0.35 in w.g.) to allow door opening (max 133 N /
  30 lbf force at door handle)
- Door opening: system must maintain minimum pressure with one door open on
  the fire floor; air velocity through open door >= 0.75 m/s (some codes
  require 1.0 m/s per BS EN 12101-6)

**System components:**
- Supply fan: typically at roof level, sized for total leakage + one open door flow
- Fresh air intake: located away from smoke exhaust outlets (minimum 3 m
  horizontal, 5 m recommended)
- Pressure relief: barometric dampers or variable-speed drive to prevent
  over-pressurization
- Backup power: standby generator (high-rise requirement)
- Commissioning: air flow and pressure testing at completion; annual testing
  per fire code

**Design considerations:**
- Stack effect in tall buildings: temperature difference between interior and
  exterior creates significant pressure differentials, especially in winter.
  Fan sizing must account for worst-case stack effect.
- Wind effect: wind pressure on building facades affects pressurization.
  Multiple inlets on different facades or ducted intake recommended.
- Elevator shaft interaction: elevator shafts can act as chimneys; consider
  elevator lobby pressurization or vestibule design to prevent smoke migration
  through elevator shaft to stair.

### Smoke Lobbies (Protected Lobbies)

A fire-rated vestibule between the occupied floor and the stair enclosure,
providing an additional barrier to smoke entering the stair:

- Minimum area: 5 m² (BS 9999) or sufficient for wheelchair refuge +
  door swings
- Rating: same as stair enclosure walls
- Doors: self-closing, smoke-sealed (FD30S minimum UK; 20-min smoke door IBC)
- Ventilation: natural vent (1.0 m² openable) or mechanical (pressurization
  or extract)
- Required by: ADB for all escape stairs in buildings > 11 m; IBC for
  smokeproof enclosures in high-rise; BS 9999 for all protected stairs in
  risk profiles C2/C3

---

## Section 2: Refuge Areas

### Definition and Purpose

A refuge area (area of rescue assistance per IBC; protected refuge per ADB)
is a location within a building where persons who cannot use stairs can wait
safely for assisted evacuation.

### Design Requirements

**Location:**
- Adjacent to every escape stair at every level above and below exit discharge
- Within the stair enclosure or in the smoke lobby
- Must not obstruct the flow of evacuating occupants through the stair

**Size:**
- IBC: 760 x 1220 mm (30 x 48 in) clear floor space per wheelchair space
- ADB/BS 9999: 900 x 1400 mm per wheelchair space
- Number: minimum 1 per stair per floor; 2 per floor if > 200 occupants
  on that floor

**Communication:**
- Two-way voice communication between refuge and fire command center or
  building entrance (IBC 1009.8)
- Visual indicator at refuge showing system is operational
- Instructions signage at refuge: "Area of Rescue Assistance / Two-way
  communication provided / Persons unable to use stairs should wait here
  for assistance"

**Protection:**
- Same fire rating as stair enclosure
- Smoke-sealed construction (fire-rated walls and self-closing doors)
- Pressurization or natural ventilation as per stair enclosure

### Evacuation Devices

Increasingly, buildings provide evacuation devices at refuge areas:
- Evacuation chairs: stair-descent devices operated by trained staff;
  stored at each refuge area; weight capacity typically 136-182 kg (300-400 lb)
- Evacuation mats/sheets: for persons who cannot sit in an evacuation chair
- Emergency evacuation elevator: per IBC 3008 or BS EN 81-76; under control
  of fire service or trained building staff

### Exceptions

IBC Section 1009.3 Exception: refuge areas are not required in buildings
equipped throughout with an NFPA 13 sprinkler system. This exception is
based on the premise that sprinklers will control the fire and allow
sufficient time for assisted evacuation by fire service using elevators.

UK ADB: refuge areas required regardless of sprinkler provision.

---

## Section 3: Firefighting Access

### Fire Service Vehicle Access

- Minimum road width: 6.0 m (20 ft) for aerial apparatus per IFC Appendix D
  (3.7 m / 12 ft for standard apparatus)
- Road surface: designed for fire apparatus loading (minimum 34,000 kg / 75,000 lb
  for aerial apparatus)
- Clear height: 4.1 m (13.5 ft) minimum under any overhead obstruction
- Turning radius: minimum 12.2 m (40 ft) inside, 15.2 m (50 ft) outside
- Dead-end roads: turnaround required (hammerhead, cul-de-sac, or equivalent)
  per IFC

### Firefighter Access Points

- Minimum 1 fire department access door per 61 m (200 ft) of building perimeter
  at ground level
- Access doors: openable from exterior without key; size minimum 915 x 2032 mm
  (36 x 80 in)
- Identification: "FIRE DEPT. ACCESS" sign or reflective marker per AHJ

### Firefighting Shaft Components

| Component | IBC High-Rise | ADB > 18 m | BS 9999 |
|------------------------------|-------------|------------|---------|
| Fire service elevator | Required | Required | Required |
| Protected lobby | Required | Required | Required |
| Fire main (standpipe/riser) | Wet standpipe Class I | Dry riser 18-60 m; Wet riser > 60 m | Per risk profile |
| Lobby size | Per accessibility | Min 5 m² | Min 5 m² |
| Lobby ventilation | Pressurization | Natural 1.0 m² or mech. | Natural or mechanical |

---

## Section 4: Travel Distance Tables -- Consolidated International Comparison

### IBC (US) -- Maximum Travel Distance (Table 1017.2)

| Occupancy | Unsprinklered m (ft) | Sprinklered m (ft) |
|-----------|----------------------|-------------------|
| A | 61 (200) | 76 (250) |
| B | 61 (200) | 91 (300) |
| E | 61 (200) | 76 (250) |
| F-1 | 61 (200) | 76 (250) |
| F-2 | 61 (200) | 76 (250) |
| H-1 | 23 (75) | 23 (75) |
| H-2 | 23 (75) | 30 (100) |
| H-3 | NP | 30 (100) |
| I-1 | 61 (200) | 76 (250) |
| I-2 | NP | 61 (200) |
| M | 61 (200) | 76 (250) |
| R | 61 (200) | 76 (250) |
| S-1 | 61 (200) | 76 (250) |
| S-2 | 91 (300) | 122 (400) |
| U | 61 (200) | 76 (250) |

### BS 9999 (UK) -- Maximum Travel Distance

**Risk Profile A (office, commercial):**

| Condition | One Direction | More Than One Direction |
|------------|--------------|----------------------|
| Unsprinklered | 18 m | 45 m |
| Sprinklered | 27 m | 60 m |

**Risk Profile B (retail, assembly, industrial):**

| Condition | One Direction | More Than One Direction |
|------------|--------------|----------------------|
| Unsprinklered | 15 m | 32-45 m |
| Sprinklered | 22 m | 45-60 m |

**Risk Profile C (residential, sleeping):**

| Condition | One Direction | More Than One Direction |
|------------|--------------|----------------------|
| Unsprinklered | 9 m | 18-35 m |
| Sprinklered | 18 m | 35-45 m |

### Approved Document B (England & Wales)

| Purpose Group | One Direction | Alternative Directions |
|--------------------------|--------------|----------------------|
| 2a Residential (flat) | 9 m (corridor) | -- (single direction) |
| 2b Residential (institutional) | 9 m | 18 m |
| 3 Office | 18 m | 45 m |
| 4 Shop/commercial | 18 m | 45 m |
| 5 Assembly/recreation | 15 m | 32 m |
| 6 Industrial | 25 m | 45 m |
| 7a Storage/high hazard | 12 m | 25 m |
| 7b Storage/low hazard | 25 m | 45 m |

### NCC (Australia)

| Class | Single Direction | Alternative Directions |
|-------|-----------------|----------------------|
| 2 (Apartments) | 6 m | 20 m |
| 3 (Hotels) | 6 m | 20 m |
| 5 (Office) | 20 m | 40 m |
| 6 (Retail) | 20 m | 40 m |
| 7 (Storage) | 20 m | 40 m |
| 8 (Factory) | 20 m | 40 m |
| 9a (Healthcare) | 15 m | 30 m |

(Note: Australian distances are generally shorter than IBC and comparable
to UK. NCC Specification C2.4.)

---

## Section 5: Stair Width Calculations -- Worked Examples

### Example 1: 10-Story Office Building (IBC)

**Given:**
- 10-story office (Group B), 2000 m² (21,528 ft²) per floor
- Sprinklered (NFPA 13)
- 2 exit stairs

**Step 1: Occupant load per floor.**
- B occupancy: 9.3 m² gross per person
- 2000 / 9.3 = 215 occupants per floor

**Step 2: Stair width per IBC.**
- Per IBC 1005.1: stair width = occupant load × 7.6 mm per occupant
- With 2 stairs, each must accommodate total load when one is blocked:
  215 × 7.6 = 1,634 mm per stair
- Minimum stair width for 50+ occupants: 1,118 mm
- Required: 1,634 mm per stair (governs over minimum)

**Step 3: Practical stair width.**
- 1,634 mm between walls -- round up to 1,650 mm (65 in)
- With 2 handrails projecting 90 mm each: clear walking width =
  1,650 - 180 = 1,470 mm
- Provides comfortable 2-abreast flow with 3rd person passing

**Step 4: Stair core dimensions.**
- Return stair (U-shape): 2 flights × 1,650 mm + 150 mm center gap
  + 2 × 200 mm walls = 3,850 mm wide
- Length: assuming 3,200 mm floor-to-floor, 17 risers × 189 mm = 3,200 mm
  (riser height slightly above 178 mm maximum -- reduce to 18 risers ×
  178 mm = 3,200 mm); run = 17 treads × 279 mm = 4,743 mm + 2 landings
  × 1,650 mm = 8,043 mm total stair enclosure length
- Plan: approximately 3,850 mm × 8,100 mm for stair enclosure

### Example 2: Residential Tower (BS 9999 / ADB Method)

**Given:**
- 20-story residential tower, 8 flats per floor, 2.5 persons per flat
- Single stair with firefighting shaft
- Simultaneous evacuation capacity required (post-Grenfell)

**Step 1: Population per floor.**
- 8 × 2.5 = 20 persons per floor

**Step 2: Total simultaneous evacuation population.**
- 19 upper floors × 20 = 380 persons (ground floor evacuates directly)

**Step 3: Stair width per BS 9999 Table 13.**
- For 220+ persons in a single stair, width = 1,100 mm minimum
- Check capacity: 1,100 mm stair accommodates approximately 80 persons/min
  at 1.1 m/s descent speed (per BS 9999 calculation method)
- 380 persons / 80 persons/min = 4.75 minutes -- acceptable if ASET
  (Available Safe Egress Time) > 4.75 minutes + pre-movement time

**Step 4: Pre-movement time.**
- BS PD 7974-6 residential: 5-10 minutes for first occupant, 10-15 minutes
  for last occupant on fire floor
- Total RSET (Required Safe Egress Time) = detection time + alarm time +
  pre-movement time + travel time = 1 + 0.5 + 10 + 5 = 16.5 minutes
- ASET must exceed RSET with safety margin: ASET > 1.5 × RSET = 24.75 min

**Step 5: Stair with lobby.**
- Lobby: 2,400 × 1,800 mm minimum (wheelchair refuge + 2 door swings)
- Stair enclosure: 2,700 × 5,000 mm minimum
- Firefighting shaft adds: fire service elevator (2,100 × 1,500 mm cab +
  shaft walls), rising main cupboard

### Example 3: Concert Hall with 2,500 Seats (IBC)

**Given:**
- A-1 assembly, 2,500 fixed seats, single story, sprinklered
- 4 exits required (> 1,000 occupants)

**Step 1: Exit width calculation.**
- Level components (doors): 5.1 mm per occupant
- Total door width: 2,500 × 5.1 = 12,750 mm across all exits
- 4 exits: 12,750 / 4 = 3,188 mm per exit
- Practical: 4 pairs of double doors, each pair 1,829 mm (72 in),
  total = 4 × 1,829 = 7,316 mm... insufficient
- Revised: provide 8 exit doors at 1,118 mm (44 in) each = 8,944 mm...
  still insufficient
- Solution: provide 4 exit clusters, each with triple doors (3 × 914 mm
  = 2,742 mm per cluster), total = 10,968 mm -- still short
- Correct solution: 4 exit locations × 4 doors each (4 × 914 mm = 3,658 mm
  per location), total = 14,632 mm -- exceeds 12,750 mm requirement

**Step 2: Travel distance.**
- A-1 sprinklered: 76 m (250 ft) maximum
- Concert hall plan: exits at all 4 sides; maximum travel from center of
  rear row to nearest exit approximately 40 m -- well within limit

**Step 3: Assembly-specific.**
- Main exit (facing lobby/public way): 50% of total occupant load
  = 1,250 occupants × 5.1 mm = 6,375 mm
- Provide main exit lobby with 8 doors × 914 mm = 7,312 mm -- adequate
- Remaining exits: 1,250 × 5.1 = 6,375 mm across 3 remaining exit locations
  = 2,125 mm each; provide 3 double doors per location (3 × 914 = 2,742 mm
  each) -- adequate

**Step 4: Emergency systems.**
- Panic hardware on all exit doors (occupant load > 50 in A-1)
- Emergency voice/alarm: required (occupant load > 300)
- Emergency lighting: 10.8 lux on egress path, 90-minute duration
- Standby power for voice/alarm and emergency lighting

---

## Section 6: Evacuation Modeling Basics

### Purpose

Evacuation modeling predicts the time required for building occupants to
reach safety. It is used in performance-based fire engineering to demonstrate
that ASET (Available Safe Egress Time) exceeds RSET (Required Safe Egress Time).

### RSET Components

```
RSET = t_detection + t_alarm + t_pre-movement + t_travel
```

- **t_detection:** Time from fire ignition to detection. Depends on detector
  type, fire growth rate, ceiling height. Typically 30s-3min.
- **t_alarm:** Time from detection to occupant notification. Typically 0-30s
  (automatic) or up to 5 min (investigation by staff before alarm).
- **t_pre-movement:** Time from alarm to start of movement. Highly variable:
  office 1-3 min, residential 5-15 min, hospital 10-20 min. Includes
  recognition, decision, and preparation.
- **t_travel:** Time to traverse exit access, exit, and exit discharge to
  place of safety. Calculated by modeling or hand calculation.

### ASET Determination

ASET is the time from ignition until conditions become untenable on the
egress path. Tenability criteria:

| Parameter | Tenability Limit |
|-----------|-----------------|
| Visibility | > 10 m (familiar), > 5 m (unfamiliar) |
| Temperature | < 60°C (sustained exposure) |
| Radiant heat flux | < 2.5 kW/m² |
| CO concentration | < 1400 ppm (30-min exposure) |
| FED (Fractional Effective Dose) | < 0.3 (conservative) |
| Smoke layer height | > 2.5 m above floor |

### Modeling Software

**Agent-based models (microscopic):**
- **Pathfinder** (Thunderhead Engineering): 3D agent-based, SFPE steering mode
  or flow mode; widely used in the US
- **STEPS** (Mott MacDonald): 3D agent-based; widely used in the UK and Asia
- **Simulex** (IES): 2D agent-based; legacy software
- **MassMotion** (Oasys): 3D agent-based; used for large transit and stadium
  projects

**Flow-based models (macroscopic):**
- Hand calculation per SFPE Handbook Chapter 64 (hydraulic flow model)
- Spreadsheet tools for simple geometries

### Key Parameters

- Walking speed: 1.2 m/s (free-flow, horizontal); 0.5-0.7 m/s (stair descent);
  0.4-0.6 m/s (stair ascent)
- Density-speed relationship: as density increases, speed decreases; at
  3.8 persons/m² (jam density), movement stops
- Door flow rate: approximately 1.3 persons/s per meter of door width
  (at optimal density)
- Stair flow rate: approximately 1.0-1.1 persons/s per meter of stair width
  (descent); reduces at higher occupant densities

---

## Section 7: Case Studies

### Case Study 1: The Shard, London (310 m, 72 Stories)

- **Egress strategy:** Phased evacuation; firefighting shaft with 2 fire service
  elevators; 3 escape stairs serving different floor zones
- **Stairs:** 2 primary stairs from top to ground; 1 additional stair serving
  lower commercial floors. Width 1,200 mm each.
- **Refuge:** Designated refuge floors at mechanical plant levels (approximately
  every 15 stories); wheelchair refuge at every stair landing
- **Smoke control:** Stair pressurization; mechanical extract in common lobbies;
  atrium smoke reservoirs at restaurant levels
- **Key innovation:** Zoned evacuation communicating via voice alarm; occupants
  above and below fire zone hold in place while fire floor evacuates

### Case Study 2: Marina Bay Sands, Singapore (200 m, 55 Stories + SkyPark)

- **Challenge:** 2,500-person rooftop SkyPark at 200 m height connected to
  3 separate towers by a horizontal span
- **Egress from SkyPark:** Dedicated exit stairs from SkyPark down through each
  tower; evacuation elevators under fire service control
- **Stairs:** Multiple stairs in each tower; scissor stair configuration in
  hotel towers for compact core
- **Smoke control:** Pressurized stairs; wind-driven smoke management at
  SkyPark (open-air conditions at 200 m altitude create extreme wind effects)
- **Key innovation:** Performance-based egress design accommodating
  3,000+ occupants at rooftop level

### Case Study 3: Crossrail Elizabeth Line Stations, London (Underground)

- **Challenge:** Deep underground stations (up to 40 m below ground) with
  platform-to-surface egress for 15,000+ persons per hour
- **Egress:** Escalator banks (6-8 escalators per station) as primary egress;
  fire-rated stairs adjacent; evacuation elevators for accessibility
- **Travel distance:** Platform to surface > 100 m (achieved through
  performance-based analysis exceeding prescriptive UK limits)
- **Smoke control:** Platform-level mechanical extract; tunnel ventilation
  (piston effect + mechanical fans); pressurized escape routes
- **Evacuation modeling:** Extensive use of STEPS and Legion (pedestrian
  simulation) for all 10 central stations; validated against real crowd
  movement data from existing London Underground stations
- **Key innovation:** Full dynamic simulation of 40,000 simultaneous
  evacuees across the central section

### Case Study 4: Apple Park, Cupertino (4-Story Ring Building, 260,000 m²)

- **Challenge:** Single building with 12,000+ occupants; largest occupied
  floor plate in the US at approximately 65,000 m² per floor
- **Egress:** Multiple stairs distributed around the ring perimeter and at
  internal cores; travel distance managed by short distances to numerous stairs
- **Exits:** Ground-floor exit discharge to exterior at grade around full
  perimeter (ring building sits in landscape, accessible from all sides)
- **Smoke control:** Large floor plates ventilated by operable facade panels
  (natural ventilation); NFPA 13 sprinklers throughout
- **Key innovation:** The ring geometry ensures no point is far from an
  exterior exit; egress design drove the structural bay spacing and core
  locations

### Case Study 5: One World Trade Center, New York (541 m, 94 Stories)

- **Challenge:** Iconic supertall on a site defined by the memory of egress
  failures during 9/11
- **Egress:** 3 exit stairs (one more than code minimum); extra-wide stairs
  at 1,320 mm (52 in) clear width; all stairs pressurized with dedicated fans
- **Refuge:** Transfer floors every 20 stories with enlarged lobbies serving
  as refuge areas
- **Firefighting:** Firefighting shaft with dedicated fire service elevator;
  standpipe in each stair; fire command center at ground level
- **Structural fire protection:** Concrete core (inherent fire resistance);
  steel perimeter structure with spray-applied fire protection + intumescent
  coating on exposed areas
- **Bio-chemical protection:** Air filtration system for chemical/biological
  agents (unique post-9/11 requirement)
- **Key innovation:** Third stair (beyond code requirement) reflects lessons
  learned; stair width exceeds code minimum by 18% to reduce congestion;
  luminous egress markings (photoluminescent) throughout all stairs

---

## Section 8: Egress Design Best Practices

1. **Design egress first:** In complex projects, establish stair locations,
   widths, and exit discharge paths before finalizing floor plate layout.
   Egress should drive the plan, not be forced into remaining space.

2. **Remote stair placement:** IBC 1007.1.1 requires exits to be placed at
   a distance not less than 1/3 of the maximum diagonal of the floor plate
   (sprinklered) or 1/2 (unsprinklered). This maximizes the probability that
   at least one exit is remote from a fire.

3. **Intuitive wayfinding:** Escape routes should follow paths that occupants
   use daily. If the daily circulation uses the elevator lobby, the escape
   stair should be visible from or adjacent to the elevator lobby -- not
   hidden behind a service corridor.

4. **Convergence at exit discharge:** The ground floor is a bottleneck.
   When multiple stairs discharge through the ground floor (IBC allows 50%),
   ensure the ground-floor path is protected and does not merge with incoming
   occupant traffic at entrances.

5. **Maintenance of egress:** Design egress paths that remain clear under
   normal building operations. Avoid corridors used for storage (common in
   hospitals), stairs used as informal meeting spaces, and exit doors that
   are routinely locked or blocked.

6. **Counter-flow provision:** In high-rise buildings, firefighters ascend
   stairs while occupants descend. Stair width should accommodate this
   counter-flow. Additional width beyond code minimum (150-200 mm) improves
   flow and reduces congestion.

7. **Accessible egress integration:** Refuge areas should be part of the
   normal stair landing, not a dead-end alcove. Two-way communication should
   be clearly signed and regularly tested.

---

*All references are to the IBC 2021, BS 9999:2017, and Approved Document B
(2019 edition with 2020 amendments) unless otherwise noted. Verify against
the specific editions adopted by the authority having jurisdiction. Fire
engineering analysis must be performed by qualified fire engineers and
approved by the AHJ.*
