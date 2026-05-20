---
name: fire-life-safety
description: >
  Comprehensive fire and life safety design expertise covering fire strategy
  development, compartmentation and fire barrier design, means of egress design
  including travel distances and stair sizing, fire resistance ratings and
  structural fire protection methods, smoke control systems (natural and mechanical),
  active fire protection systems (sprinklers, detection, alarm, emergency lighting),
  fire door specifications, and fire strategy coordination between architect and
  fire engineer.
---

# Fire and Life Safety Design

This skill provides practitioner-grade knowledge of fire and life safety design
for architectural practice. It covers the architect's role in fire strategy,
compartmentation, egress design, structural fire protection, smoke control, and
active fire protection systems. All dimensional values are metric with imperial
equivalents where standard practice requires.

---

## Section 1: Fire Strategy Development

### The Architect's Role

The architect is the primary coordinator of fire strategy in building design.
While fire engineers provide specialist analysis (computational fire modeling,
structural fire engineering, smoke control design), the architect is responsible
for integrating fire safety into the architectural concept from the earliest
design stage.

Fire safety is not an add-on. Buildings that treat fire protection as an
afterthought suffer from: compromised spatial quality (corridors widened at
the expense of usable space), increased cost (fire-rated construction added
where it could have been avoided by better planning), and occupant risk
(egress paths that are long, confusing, or difficult to maintain).

### Fire Safety Objectives

1. **Life safety:** Ensure all occupants can evacuate or reach a place of
   safety before conditions become untenable. This is the primary objective
   and is non-negotiable.

2. **Property protection:** Limit fire damage to the area of origin or
   a defined compartment. Relevant for insurance, business continuity,
   and heritage buildings.

3. **Business continuity:** Design systems to minimize downtime after a fire
   event. Particularly important for: hospitals (defend-in-place), data centers,
   manufacturing, and critical infrastructure.

4. **Environmental protection:** Prevent fire-related contamination of soil,
   water, and air. Relevant for: chemical storage, waste facilities, sites
   near waterways.

5. **Firefighter safety:** Provide safe access for fire service operations.
   Firefighting shafts, wet/dry risers, fire command centers, adequate water
   supply.

### Prescriptive vs Performance-Based Approach

**Prescriptive approach:**
- Follow code provisions directly (IBC, Approved Document B, NBC, etc.)
- Advantages: straightforward, well-understood, defensible
- Limitations: may be overly conservative, may not address novel building
  configurations, does not account for specific building use patterns

**Performance-based approach:**
- Establish fire safety objectives, define design fire scenarios, demonstrate
  through engineering analysis that objectives are met
- Methods: computational fire modeling (FDS, CFAST), evacuation modeling
  (Pathfinder, STEPS, Simulex), structural fire analysis (FEA with fire
  curves), smoke control analysis (CFD)
- Advantages: can optimize design, accommodate complex geometries, provide
  a more accurate risk assessment
- Limitations: requires specialist fire engineer, peer review, AHJ acceptance

**Hybrid approach (most common):**
- Follow prescriptive code for most provisions
- Use performance-based analysis for specific challenges: atrium smoke control,
  travel distance extensions, reduced fire resistance periods, alternative
  egress strategies

### Fire Strategy Report Content

A fire strategy report (also called fire safety strategy, fire engineering
report, or basis of fire safety design) should include:

1. Building description: use, occupancy, construction, geometry
2. Applicable codes and standards
3. Design fire scenarios (size, location, growth rate)
4. Compartmentation strategy and fire resistance schedule
5. Means of escape: travel distances, exit widths, evacuation strategy
6. Fire detection and alarm design
7. Sprinkler/suppression system scope
8. Smoke control strategy
9. Structural fire protection specification
10. Fire service access and facilities
11. Building management fire safety provisions
12. Drawings: compartmentation plans, egress plans, fire service access plans

---

## Section 2: Compartmentation

### Purpose

Fire compartmentation divides a building into distinct zones that contain
fire and smoke for a defined period, allowing occupants to evacuate, limiting
property damage, and providing safe zones for defend-in-place strategies.

### Compartment Sizing

**IBC (US):**
- No explicit maximum compartment size for most occupancies (controlled by
  construction type and area per floor)
- I-2 smoke compartments: max 2090 m² (22,500 ft²) per smoke compartment
  per IBC 407.5.1
- I-3 smoke compartments: max 2090 m² (22,500 ft²) per IBC 408.6

**BS 9999 (UK):**
Maximum compartment sizes by risk profile:

| Risk Profile | Max Compartment Floor Area | Max Dimension |
|--------------|---------------------------|---------------|
| A1 (low risk) | 8,000 m² | No limit |
| A2 | 4,000 m² | No limit |
| B1 | 2,000 m² | No limit |
| B2 | 1,000 m² | No limit |
| C1 (sleeping, low risk) | 2,000 m² | No limit |
| C2 | 1,000 m² | No limit |
| C3 (high dependency) | 1,000 m² | No limit |

**Approved Document B (England & Wales):**
Maximum compartment sizes by purpose group:

| Purpose Group | Height < 18 m | Height >= 18 m |
|----------------------|---------------|----------------|
| Residential (flats) | No limit* | No limit* |
| Office | 2,000 m² | 2,000 m² |
| Shop/commercial | 2,000 m² | 2,000 m² |
| Assembly/recreation | 2,000 m² | 2,000 m² |
| Industrial | 2,000 m² | 2,000 m² |
| Storage | 1,000 m² | 1,000 m² |

(*Flats: each dwelling is a compartment; common corridor/stair protected)

### Fire-Rated Construction Types

**Fire Barrier (IBC 707):**
- Continuous from floor slab to underside of floor or roof slab above
  (deck, not ceiling)
- Used for: occupancy separation, exit enclosures, shaft enclosures,
  horizontal exits
- Supports: must be supported by construction with equal or greater FRR
- Continuity: all joints, penetrations, and openings must be protected

**Fire Partition (IBC 708):**
- May terminate at underside of a fire-rated floor/ceiling or roof/ceiling
  assembly
- Used for: dwelling unit separation, sleeping unit separation, corridor walls
- Less stringent than fire barrier (can stop at ceiling if ceiling is rated)

**Fire Wall (IBC 706):**
- Structurally independent (remains standing if structure on either side
  collapses)
- Extends from foundation to roof (through roof unless roof is fire-rated)
- Creates separate buildings for code purposes
- Rating: 2 hr (A, B, E, F-2, M, R, S-2, U), 3 hr (F-1, H-3/4/5, S-1),
  4 hr (H-1, H-2)

**Smoke Barrier (IBC 709):**
- Continuous membrane from floor to floor, outside wall to outside wall
- Smoke-tight construction with smoke dampers at duct penetrations
- 1-hour minimum fire resistance
- Used for: I-2 smoke compartments, I-3 smoke compartments, ambulatory
  care smoke compartments

### Fire Door Ratings

**IBC/UL system (US):**

| Application | Door Rating | Wall Rating |
|--------------------------------------|-------------|-------------|
| Fire wall opening | 3 hr | 4 hr |
| Fire wall opening | 1.5 hr | 2 hr |
| Fire barrier -- exit enclosure | 1.5 hr | 2 hr |
| Fire barrier -- exit enclosure | 1 hr | 1 hr |
| Fire barrier -- occupancy separation | 1.5 hr | 2 hr |
| Fire barrier -- occupancy separation | 0.75 hr | 1 hr |
| Fire partition -- corridor | 0.33 hr | 0.5 hr |
| Fire partition -- corridor | 0.33 hr | 1 hr |
| Smoke barrier | 0.33 hr | 1 hr |

**British Standard / European system:**

| Designation | Integrity (min) | Insulation (min) | Typical Use |
|-------------|-----------------|-------------------|--------------------------|
| FD30 | 30 | -- | Corridor doors, flat entrance doors |
| FD30S | 30 + smoke | -- | Corridor doors (with smoke seal) |
| FD60 | 60 | -- | Stairway doors, compartment walls |
| FD60S | 60 + smoke | -- | Protected lobby doors |
| FD90 | 90 | -- | High-risk areas |
| FD120 | 120 | -- | Special applications |
| FD30/FD60 + insulation | 30/60 | 30/60 | Where insulation criterion is needed |

### Fire Door Furniture and Ironmongery

- Self-closing device: overhead closer (EN 1154 / UL 228) mandatory on
  all fire doors; min closing force per accessibility requirements
- Intumescent strips: 10 mm x 4 mm or 15 mm x 4 mm strips in rebate or
  door edge; expand at 150-200°C to seal gap between door and frame
- Smoke seals (cold smoke): flexible blade or brush seal at head and jambs;
  required for FD__S designations and IBC smoke doors
- Hinges: steel butt hinges, minimum 3 per door leaf; no rising butts on
  fire doors
- Locks and latches: must not compromise fire rating; typically tested as
  part of fire door assembly
- Hold-open devices: electromagnetic hold-open connected to fire alarm;
  releases on alarm or power failure; door closer then closes door
- Panic hardware: fire-rated panic bar or touchpad (IBC requires on assembly
  and educational exit doors for occupant loads > 50)

### Glazed Fire Barriers

Types of fire-rated glass:

| Type | Integrity | Insulation | Max Rating | Applications |
|------|-----------|------------|------------|------------------------------|
| Wired glass (6 mm) | Yes | No | 60-90 min | Obsolete in many jurisdictions; limited to small vision panels |
| Borosilicate glass | Yes | No | 60-120 min | Fire-rated vision panels, limited area |
| Ceramic glass | Yes | No | 60-180 min | Fire screens, spandrel panels, large panels |
| Intumescent gel glass | Yes | Yes | 30-120 min | Full fire barriers, corridor walls, lobby screens |

- Integrity-only glass prevents flame and hot gas passage but radiates heat.
  Maximum area limited to prevent radiant heat exposure on escape routes.
- Insulating glass (intumescent gel between layers) blocks both flame and
  radiant heat. Can be used for full fire barriers including in escape routes.

### Firestopping (Penetration Seals)

Every penetration through a fire-rated assembly must be sealed with a
listed firestop system:

- **Pipe penetrations:** intumescent pipe collars (combustible pipes --
  PVC, PE, PP); mineral wool + intumescent sealant (metal pipes with
  insulation)
- **Cable penetrations:** intumescent block, putty, or pillows; cable
  transit frames for large cable bundles
- **Duct penetrations:** fire damper (integrity only) or fire/smoke damper
  (integrity + smoke sealing); rated to match wall rating
- **Structural joints:** fire-rated joint sealant (silicone or intumescent)
  with mineral wool backing

**Cavity barriers:**
- Required in concealed spaces (above ceilings, within walls) to prevent
  unseen fire spread
- Maximum distance between cavity barriers: 20 m in any direction (ADB);
  IBC Section 718 requires draft stopping in floor/ceiling spaces of
  combustible construction at max 280 m² (3,000 ft²)
- At compartment wall/floor junctions extending into concealed spaces

---

## Section 3: Means of Egress Design

### Number of Escape Stairs

**IBC (US):**
- Based on occupancy, travel distance, and floor area
- Minimum 2 exits from each floor (with single-exit exceptions per
  Table 1006.2.1 for small, low-hazard spaces)
- 3 exits for 501-1,000 occupants per floor; 4 exits for > 1,000

**BS 9999 / Approved Document B (UK):**
- Single stair permitted for buildings up to 11 m (ADB) in certain
  occupancies with limited floor area and travel distance
- Number of stairs based on maximum travel distance from any point to
  nearest stair AND stair capacity calculation

### Travel Distances -- International Comparison

**IBC (US), sprinklered:**

| Occupancy | One Direction | Any Direction |
|-----------|---------------|---------------|
| A | -- | 76 m (250 ft) |
| B | -- | 91 m (300 ft) |
| R | -- | 76 m (250 ft) |
| S-2 | -- | 122 m (400 ft) |

**BS 9999 (UK), Risk Profile B1 (office, normal risk):**

| Escape Routes | One Direction Only | More Than One Direction |
|---------------|--------------------|-----------------------|
| Unsprinklered | 18 m | 45 m |
| Sprinklered | 27 m | 60 m |

**Approved Document B (England & Wales):**

| Purpose Group | One Direction | More Than One Direction |
|----------------------|---------------|----------------------|
| Office (2b) | 18 m | 45 m |
| Shop (4) | 18 m | 45 m |
| Assembly (5) | 15 m | 32 m |
| Residential (flat)| 9 m (7.5 m corridor) | -- (single direction to stair in flat corridor) |
| Industrial (6) | 25 m | 45 m |
| Storage (7a) | 25 m | 45 m |

**Comparison note:** UK travel distances are significantly shorter than IBC
because the UK does not generally mandate sprinklers in the same way as the
IBC (sprinkler credit is a specific extension of the base distance, not a
near-universal requirement). When sprinklers are provided, UK distances
increase but still remain shorter than IBC.

### Stair Width Calculation

**IBC method:**
- 7.6 mm (0.3 in) per occupant for stairways
- 5.1 mm (0.2 in) per occupant for other egress components
- Minimum stair width: 1118 mm (44 in) for 50+ occupants; 914 mm (36 in)
  for < 50 occupants

**BS 9999 / ADB method:**
- Stair width based on number of persons per floor and number of floors
  served
- ADB Table 5: for simultaneous evacuation, stair width accommodates total
  population minus ground floor
- BS 9999 Table 13: discharge rates per unit width (0.6 m per person per
  minute on stairs at 1100 mm width)

**Minimum stair widths:**

| Standard | Minimum Width |
|----------|---------------|
| IBC (general) | 1118 mm (44 in) |
| IBC (< 50 occupants) | 914 mm (36 in) |
| ADB / BS 9999 | 1050 mm (between walls, up to 150 persons/floor) |
| ADB / BS 9999 | 1100 mm (151-200 persons/floor) |
| DIN 18065 (Germany) | 1000 mm (residential); 1200 mm (public) |

### Protected Stairways

Escape stairs must be enclosed in fire-rated construction to protect
occupants during evacuation:

- **IBC exit stairway enclosure (Section 1023):**
  - 1-hour enclosure for 4 or fewer stories connected
  - 2-hour enclosure for more than 4 stories connected
  - Opening protectives: 1-hour doors for 2-hour enclosure; 0.75-hour
    or 1-hour doors for 1-hour enclosure

- **ADB protected stairway:**
  - Walls: fire resistance equal to building's fire resistance period
    (30-120 min depending on height)
  - Doors: FD30S minimum (self-closing, smoke-sealed)
  - Ventilation: 1.0 m² natural ventilator at top of stair (or mechanical
    pressurization) for buildings > 18 m

### Firefighting Shafts

Required in buildings > 18 m height (UK) or > 23 m / 75 ft (IBC high-rise):

- **Fire service elevator (fire lift):** min 1100 x 1400 mm cab (UK BS EN 81-72);
  primary power + secondary (generator) power; waterproof elevator pit and
  landing; controls override to fire service operation
- **Firefighting lobby:** min 5 m² (UK); fire-rated enclosure at every floor
  (2-hour walls, FD60S doors); contains dry/wet riser outlet
- **Dry riser:** 100 mm diameter rising main with inlet at ground level and
  outlets at every floor; buildings 18-60 m height (UK). Fire service connects
  pumping appliance at ground level.
- **Wet riser:** permanently charged pressurized system; buildings > 60 m (UK)
  or per IBC standpipe requirements (Class I in high-rise exit stairways)

### Scissor Stairs

Two interlocking stairs within a single structural shaft, separated by
fire-rated construction:

- Each stair is independently fire-rated (1 or 2 hr) from the other
- Separate smoke lobbies at each level for each stair
- Common in high-rise residential where site constraints prevent two
  separate stair cores
- IBC: scissor stairs are treated as separate exits only if each has
  independent exit discharge and the separating construction meets exit
  enclosure requirements
- UK/BS 9999: accepted where demonstrated that failure of one stair does
  not compromise the other

### Disabled Refuge Areas

Areas of temporary safety for persons unable to use stairs:

- Location: at each floor landing of every escape stair (IBC Section 1009.3;
  ADB Section 4)
- Size: minimum 900 x 1400 mm (IBC: 760 x 1220 mm / 30 x 48 in clear
  floor space) per wheelchair space; clear of stair discharge path
- Communication: two-way intercom to fire command center / building
  management (IBC Section 1009.8)
- Number: one per stair per floor minimum; two per floor if > 200 occupants
  on that floor
- Not required in fully sprinklered buildings per IBC exception (occupants
  use elevator for evacuation under emergency evacuation plan)
- Signage: International Symbol of Accessibility + "Area of Rescue Assistance"

### Evacuation Strategies

**Simultaneous evacuation:**
- All occupants evacuate immediately upon alarm
- Standard for most building types (office, retail, education)
- Total evacuation time must be less than available safe egress time (ASET > RSET)

**Phased evacuation:**
- Fire floor and floor immediately above evacuate first
- Remaining floors evacuate in sequence (above fire floor, then below)
- Common in high-rise office buildings; requires voice/alarm communication system
  with zoned messaging
- Requires at minimum: sprinklers, smoke detection, compartmentation between
  floors, voice alarm

**Progressive horizontal evacuation:**
- Occupants move horizontally through fire/smoke barriers to an adjacent
  compartment on the same floor
- Standard for I-2 (hospitals) and I-3 (detention) -- defend-in-place
- Each smoke compartment must have capacity to hold its own occupants plus
  occupants from one adjacent compartment
- Smoke compartment max 2090 m² (22,500 ft²) per IBC 407.5.1

**Stay-put (residential):**
- UK residential strategy: occupants in flats not affected by fire remain
  in their flats (each flat is a fire compartment)
- Fire-affected flat occupants escape via protected corridor and stair
- Requires: fire-rated flat entrance doors (FD30S), fire-rated corridor/lobby
  walls, fire-rated stair enclosure, automatic detection in common areas
- Post-Grenfell review: simultaneous evacuation capability being required
  alongside stay-put as a backup (Building Safety Act 2022)

---

## Section 4: Structural Fire Protection

### Fire Resistance Periods

**IBC Table 601 (see building-codes SKILL.md Section 2 for full table)**

**ADB / BS 9999 minimum fire resistance periods:**

| Building Height | Residential | Non-residential |
|-----------------|-------------|-----------------|
| Up to 5 m | 30 min | 30 min |
| Up to 11 m | 30 min | 60 min |
| Up to 18 m | 60 min | 60 min |
| Up to 30 m | 90 min | 90 min |
| Over 30 m | 120 min | 120 min |

### Protection Methods

**Concrete cover to reinforcement:**
- Fire resistance achieved by minimum concrete cover over steel reinforcement
- 20 mm cover: approximately 1 hour FRR (depends on member type, loading)
- 25 mm cover: approximately 1.5 hours
- 35 mm cover: approximately 2 hours
- 50 mm cover: approximately 3-4 hours
- Governed by Eurocode 2-1-2, ACI 216.1, or BS 8110 Part 2

**Intumescent coatings (thin-film for structural steel):**
- Applied as paint-like coating (0.25-5 mm dry film thickness)
- Expands 20-50 times original thickness at 200-250°C, forming insulating char
- Fire ratings achievable: 30-120 minutes (up to 180 min for some products)
- Advantages: thin profile preserves exposed steel aesthetic; can be applied
  off-site or on-site
- Limitations: requires controlled application conditions; some products
  vulnerable to humidity; maintenance access needed for recoating (25-year
  typical life)
- Specification: dry film thickness (DFT) per fire rating, section factor
  (Hp/A) of the steel member; higher Hp/A (thinner steel) requires thicker
  coating

**Board encasement:**
- Calcium silicate board (e.g., Promat): 15-60 mm thickness for 30-240 min FRR
- Vermiculite/gypsum board: 12-50 mm thickness for 30-180 min FRR
- Advantages: precise, consistent, factory-quality finish; can be installed
  in any weather
- Limitations: visible box profile around structural members; time-consuming
  installation for complex geometries

**Spray-applied fire protection (SFRM):**
- Cementitious (Portland cement + mineral aggregate): density 240-350 kg/m³
- Mineral fibre (slag wool + cement binder): density 190-320 kg/m³
- Typical thickness: 10-40 mm for 1-3 hours
- Advantages: fastest application method, conforms to complex geometries,
  lowest cost per hour of fire rating
- Limitations: rough finish (must be concealed above ceilings), overspray
  containment, cannot be applied below ~4°C, fragile if exposed

**Concrete encasement (full):**
- Steel members fully encased in concrete
- Provides 2-4 hours FRR depending on cover thickness
- Heavy, expensive, rarely used for fire protection alone in modern construction
- Still common where structural composite action (steel-concrete) is desired

### Mass Timber Fire Design

**Charring method (Eurocode 5-1-2 / NDS/AWC):**
- Standard charring rate: 0.65 mm/min for softwood (spruce, pine, fir)
- Charring rate for glulam/CLT: 0.65-0.70 mm/min
- Zero-strength layer: 7 mm below char line (wood heated but not charred
  has reduced strength)
- Effective residual section = original section - char depth - zero-strength layer

**Design process:**
1. Determine required fire resistance period (e.g., 90 minutes)
2. Calculate char depth: 0.65 mm/min × 90 min = 58.5 mm per exposed face
3. Add zero-strength layer: 58.5 + 7 = 65.5 mm per exposed face
4. Residual section = original - 65.5 mm per exposed face
5. Verify structural capacity of residual section under fire load combination
   (typically dead + 0.5 × live, reduced from ambient design loads)

**Type IV-A (encapsulated mass timber):**
- All mass timber surfaces protected by noncombustible material
- Typically 2 layers of 16 mm (5/8 in) Type X gypsum board (32 mm total)
- Gypsum provides ~60 minutes protection before charring begins
- Total fire resistance = gypsum protection time + residual timber capacity

**Type IV-C (exposed mass timber):**
- Timber may be fully exposed; fire resistance from oversized section alone
- Architectural advantage: warm, exposed wood aesthetic
- Requires larger timber dimensions to account for full charring

---

## Section 5: Smoke Control

### Purpose

Smoke is the primary cause of death in building fires. Smoke control systems
maintain tenable conditions on escape routes and in occupied spaces during
the time needed for evacuation.

### Natural Smoke Ventilation (NSHEV -- Natural Smoke and Heat Exhaust Ventilation)

**Sizing:**
- General rule: free ventilation area = 5% of floor area of the smoke
  reservoir, or 1.5 m² per 200 m² of floor area (whichever is greater)
- Smoke reservoir depth: minimum 3 m (10 ft) from ceiling to bottom of
  smoke layer (maintain clear layer height above 2.5 m for tenability)
- Inlet air: low-level openings at least equal in area to exhaust openings
- Location: at highest point of smoke reservoir (roof vents, high-level
  windows)

**Automatic opening:**
- Actuated by: smoke detection (most common), fusible link (thermal),
  fire alarm signal
- Override: manual release at ground level and adjacent to ventilator
- Fail-safe: opens on power failure (unless wind/weather concerns require
  closed default)

### Mechanical Smoke Extract

- Extract rate: determined by fire engineering analysis based on design fire
  size and smoke production rate
- Typical rates: 4-10 air changes per hour for corridor extract; higher for
  atrium and large-volume spaces
- Fans: rated for 300°C for 60 minutes (minimum) or 400°C for 120 minutes
  (for extended fire exposure); per EN 12101-3
- Ductwork: fire-rated or within fire-rated shaft; dampers at compartment
  boundaries
- Make-up air: must be provided to replace extracted smoke; typically
  low-level inlets at 75-80% of extract rate to maintain slight negative
  pressure in fire zone

### Stair and Lobby Pressurization

- Maintains positive pressure in escape stairs and lobbies to prevent smoke
  infiltration
- Pressure differential: 50 Pa (0.2 in w.g.) with all doors closed
  (BS EN 12101-6); 12.5 Pa minimum, 87 Pa maximum (IBC)
- Air velocity through open door: 0.75 m/s minimum (some codes require
  1.0 m/s) to resist smoke flow
- Fan sizing: accounts for leakage through closed doors, walls, and
  when one door is open on the fire floor
- Door opening force: must not exceed 133 N (30 lbf) at the door handle
  with pressurization system operating (IBC 1010.1.3)
- Compensation: variable-speed fans or pressure-relief dampers to adjust
  for doors opening/closing

### Smoke Curtains and Fire Shutters

**Smoke curtains (fixed or automatic):**
- Fabric barriers descending from ceiling to contain smoke within a
  defined reservoir
- Deployed by: gravity (fail-safe), motor-driven from smoke detection signal
- Drop time: typically 30-60 seconds to full deployment
- Rating: per EN 12101-1 (D class for ambient smoke barriers, DH class for
  hot smoke)

**Fire shutters:**
- Steel or composite rolling/sliding shutters providing fire separation
- Rating: 1-4 hours (integrity); some provide insulation rating
- Deployed automatically on fire alarm; manual override required
- Used where fire doors are impractical (wide openings, service counters,
  conveyor openings)
- Activation: fusible link (thermal), fire alarm signal, or both

### Atrium Smoke Control

Atriums require specific smoke control analysis due to large interconnected
volumes:

**Steady-state plume calculation (simplified):**
- Mass flow rate of smoke: M = 0.071 × Qc^(1/3) × Z^(5/3) + 0.0018 × Qc
  (axisymmetric plume, NFPA 92)
  Where: M = mass flow rate (kg/s), Qc = convective heat release rate (kW),
  Z = height above fire (m)
- For balcony spill plume (fire on floor below atrium, smoke spilling over
  balcony edge): mass flow rate increases significantly -- approximately 2-3x
  axisymmetric for same height

**Design considerations:**
- Smoke reservoir at top: minimum 3 m depth
- Exhaust: mechanical or natural (powered natural ventilators)
- Makeup air: low-level, below smoke layer; velocity < 1.0 m/s to avoid
  disturbing plume
- Plugholing: exhaust point must not extract air from below smoke layer;
  per NFPA 92 critical exhaust rate calculation
- IBC 404.5: requires smoke control per Section 909 in all atriums

---

## Section 6: Active Fire Protection Systems

### Automatic Sprinkler Systems

**Wet-pipe system (most common):**
- Pipes permanently charged with water under pressure
- Activation: individual sprinkler heads actuate when ambient temperature
  reaches rated temperature (typically 68°C / 155°F for standard; 57°C for
  residential quick-response)
- Response: only heads in the fire zone activate (not all heads)
- Coverage: maximum 12 m² (130 ft²) per head for light hazard;
  9.3 m² (100 ft²) for ordinary hazard per NFPA 13
- Maximum spacing: 4.6 m (15 ft) between heads for standard coverage
- Minimum pressure: 0.5 bar (7 psi) at the most remote head
- Water density: 4.1 mm/min (0.10 gpm/ft²) light hazard to 8.1 mm/min
  (0.20 gpm/ft²) ordinary hazard Group 2

**Dry-pipe system:**
- Pipes filled with pressurized air or nitrogen; water released when
  sprinkler head actuates and air pressure drops
- Use: unheated spaces (parking garages, loading docks, freezers) where
  water would freeze
- Delay: 30-60 seconds from head activation to water delivery
- Maximum system size: 750 gallons per NFPA 13

**Pre-action system:**
- Requires two triggers: fire detection AND sprinkler head activation
- Single interlock: detection activates valve, then head must open
- Double interlock: both detection and head activation needed simultaneously
- Use: data centers, museums, libraries -- where accidental water damage
  is unacceptable

**Deluge system:**
- All heads are open (no fusible element); water released to all heads
  simultaneously when detection system activates
- Use: high-hazard areas (aircraft hangars, chemical storage, transformer
  rooms) requiring immediate total suppression
- Requires large water supply

**Residential sprinkler system (NFPA 13R / 13D):**
- NFPA 13R: for residential occupancies up to 4 stories (reduced coverage;
  sprinklers not required in closets, bathrooms < 5.1 m², attics, garages)
- NFPA 13D: for one- and two-family dwellings (further reduced)
- Quick-response heads: 57°C (135°F) rated, faster thermal response
- Minimum flow: per NFPA 13R/13D hydraulic calculations

### Fire Detection and Alarm

**Detection types:**

| Type | Detection Method | Response Time | Best For |
|------|-----------------|---------------|----------|
| Ionization smoke | Particle ionization change | Fast (flaming fires) | Offices, corridors (being phased out in some jurisdictions) |
| Photoelectric smoke | Light scatter/obscuration | Fast (smoldering fires) | Bedrooms, corridors, common areas |
| Heat (fixed temp) | Fusible element at set temp | Slow (fires must grow) | Kitchens, garages, dusty environments |
| Heat (rate-of-rise) | Rapid temperature increase | Moderate | Warehouses, mechanical rooms |
| Aspirating (VESDA) | Air sampling + laser detection | Very fast | Data centers, heritage, clean rooms |
| Flame (IR/UV) | Infrared/ultraviolet radiation | Very fast | Aircraft hangars, fuel storage |
| Linear heat | Cable changes resistance with temperature | Moderate | Tunnels, cable trays, conveyor belts |

**Fire alarm zoning (IBC Section 907):**
- Manual pull stations: at each exit from each floor
- Smoke detectors: in corridors, elevator lobbies, HVAC ducts
- Heat detectors: kitchens, mechanical rooms, parking garages
- Voice/alarm communication: required in high-rise, assembly > 300,
  certain E and I occupancies
- Zone size: max 1858 m² (20,000 ft²) per zone; max 91 m (300 ft)
  length per zone; each floor a separate zone

### Emergency Lighting

**IBC requirements (Section 1008):**
- Illumination: minimum 10.8 lux (1 fc) at floor along exit access;
  minimum 10.8 lux at exit discharge
- Duration: minimum 90 minutes from onset of power failure
- Power: battery backup or generator

**UK / EN requirements (BS 5266-1 / EN 1838):**
- Escape route lighting: minimum 1 lux at floor level along centerline,
  0.5 lux at edges; uniformity ratio max 40:1
- Anti-panic (open area) lighting: 0.5 lux at floor level throughout
  open areas > 60 m²
- High-risk task area: minimum 10% of maintained illuminance or 15 lux
  (whichever is greater)
- Duration: 1 hour minimum, 3 hours recommended (and required in many
  jurisdictions for sleeping accommodations)
- Monthly functional test (flick test), annual full-duration test

### Fire Extinguishers

- Placement: max 23 m (75 ft) travel distance to nearest extinguisher
  for Class A (ordinary combustibles); max 15 m (50 ft) for Class B
  (flammable liquids)
- Mounting height: handle at max 1525 mm (60 in) above floor for units
  > 18 kg (40 lb); max 1067 mm (42 in) for units > 18 kg on some
  interpretations -- verify with AHJ
- Types: ABC dry chemical (most common), CO2 (electrical/clean agent),
  water mist (heritage), wet chemical (commercial kitchens)
- Not a substitute for fixed suppression in buildings requiring sprinklers

### Dry and Wet Risers

**Dry riser:**
- Vertical pipe (100 mm / 4 in diameter minimum) with inlet at ground level
  and outlet valves at each floor
- Fire service connects pumping appliance at ground inlet to pressurize system
- Required: buildings 18-60 m height (UK ADB); IBC requires standpipe per
  Section 905
- Outlet: 65 mm (2.5 in) landing valve in firefighting lobby or stair landing

**Wet riser:**
- Permanently pressurized with water; fire pump maintains pressure
- Required: buildings > 60 m height (UK); IBC Class I standpipe in
  high-rise stairways
- Outlet: 65 mm (2.5 in) valve at each floor landing
- Pressure: 7 bar (100 psi) at topmost outlet minimum
- Water supply: dedicated fire water tank or connection to reliable public main
  with adequate flow (typically 1500 L/min for wet riser)

---

*This skill provides general fire and life safety guidance for architectural
design. All fire strategies must be developed in coordination with a qualified
fire engineer and approved by the authority having jurisdiction. Fire codes
and standards are jurisdiction-specific -- verify requirements against the
locally adopted edition.*
