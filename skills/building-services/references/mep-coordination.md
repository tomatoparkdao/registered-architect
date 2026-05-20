# MEP Coordination: Comprehensive Reference

This reference provides detailed guidance on mechanical, electrical, and plumbing coordination for architectural practice, including zone planning, ceiling void allocation, service route hierarchies, riser shaft sizing, plant room sizing, below-ground services, roof plant screening, and coordination case studies.

---

## 1. Zone Planning: Horizontal Distribution

### Ceiling Void Zone Allocation

The ceiling void must be organised in horizontal layers with a clear hierarchy. Working downward from the structural soffit:

**Layer 1 — Structural zone (immediately below slab soffit)**
- Downstand beams, drop panels, post-tensioned tendon profiles
- Nothing installed here without structural engineer approval
- Zero tolerance for clashes — relocate services, not structure

**Layer 2 — Primary horizontal distribution (50-150mm below structure)**
- Main HVAC supply and return ductwork (largest cross-section elements)
- Main cable trays and bus-bar trunking
- Primary CHW/LTHW/CW mains
- Sprinkler main headers
- Run parallel to or perpendicular to primary structure (not diagonal — complicates coordination)
- Minimum 25mm clearance between services; 50mm preferred for insulated pipes

**Layer 3 — Secondary distribution (below primary zone)**
- Branch ductwork from main to terminal units
- Secondary cable trays
- Branch pipework
- Sprinkler distribution pipes
- Crossover zone: where primary services in one direction cross secondary services in the perpendicular direction

**Layer 4 — Terminal zone (closest to ceiling plane)**
- Fan coil units, chilled beam units, VAV boxes
- Sprinkler drops and heads
- Light fittings (recessed)
- Smoke detectors, speakers, access points
- Cable drops to floor below (via perimeter trunking or floor boxes)

**Layer 5 — Ceiling finish**
- Suspended ceiling grid and tiles (15-25mm)
- Or plasterboard ceiling on framing (25-50mm)
- Or exposed soffit with painted services (0mm — services are the ceiling)

### Typical Layer Depths

| Layer | Residential (mm) | Office (mm) | Hospital (mm) | Laboratory (mm) |
|---|---|---|---|---|
| Primary distribution | 100-200 | 250-400 | 350-600 | 400-700 |
| Secondary distribution | 50-100 | 100-200 | 150-300 | 200-400 |
| Terminal equipment | 50-100 | 100-200 | 150-300 | 150-300 |
| Ceiling finish | 15-25 | 15-25 | 15-25 | 15-25 |
| **Total void** | **215-425** | **465-825** | **665-1225** | **765-1425** |

### Horizontal Zone Planning

In plan, services follow defined routes:
- **Primary routes**: Along corridors, parallel to the building's long axis. Width: 1.5-3.0m corridor zone accommodates all primary services.
- **Secondary routes**: Perpendicular to primary, into occupied zones. Branching from corridor to perimeter.
- **Service-free zones**: Keep structure-to-structure connections clear (punching shear zones at columns, shear wall junctions).
- **Coordination strips**: Define 600mm-wide coordination strips in plan at primary/secondary intersections. All crossovers occur here, allowing sectional coordination.

---

## 2. Vertical Distribution: Riser Shaft Design

### Riser Types and Sizing

**Electrical risers:**
- Bus-bar trunking: 200x200mm to 300x300mm (100-3200A rating)
- Cable trays (stacked): 400x200mm to 600x400mm
- Segregation required: HV/LV separation 300mm minimum; power/data separation 150mm minimum
- Size per floor: 0.4-0.6m² (office); 0.3-0.4m² (residential)
- Access: Lockable door at each floor, 600x2100mm minimum

**Data/telecoms risers:**
- Cable trays or basket: 300x200mm to 400x300mm
- Fibre optic backbone + copper distribution
- Size per floor: 0.2-0.4m² (office); 0.1-0.2m² (residential)
- May combine with electrical riser if segregation maintained

**Water risers (cold water, hot water flow and return):**
- Pipes: 28-80mm diameter (insulated)
- Insulation: 19-32mm (cold water, to prevent condensation); 25-50mm (hot water, to prevent heat loss)
- Isolation valves at each floor
- Size per floor: 0.3-0.5m² (combined CW + HW)
- Access: Removable panels at each floor, 450x450mm minimum

**Soil and waste risers:**
- Soil stack: 100mm diameter
- Waste stack: 50mm diameter (or combined with soil stack)
- Vent pipe: 50-75mm diameter (may terminate above roof or use AAV)
- Size per floor: 0.2-0.3m² per stack
- Access: Rodding access at base and changes of direction

**HVAC risers:**
- Supply air duct: Varies widely — 300x300mm (small FCU system) to 1200x800mm (VAV system for large floor)
- Return air duct: 70-80% of supply duct size
- CHW/LTHW pipes: 50-150mm diameter
- Size per floor: 0.5-3.0m² depending on system and floor area served
- Fire dampers at every floor penetration

**Sprinkler riser:**
- Flow and return: 65-150mm diameter (depending on hazard class)
- Valve set (flow switch, drain, test valve) at each floor: 600x400x200mm
- Size per floor: 0.2-0.3m²

**Smoke extract shaft:**
- Dedicated fire-rated shaft
- Minimum 1.0m² cross-section (building-specific calculation)
- Fire-rated construction (typically 120 minutes)
- Smoke extract fans at roof level

### Riser Location Strategy

- **Adjacent to cores**: Risers should be adjacent to or within the building core, close to lifts and stairs. This centralises vertical distribution and minimises horizontal pipe/duct runs.
- **Paired risers**: On opposite sides of the core for redundancy and to reduce horizontal distribution lengths. Two smaller risers are often better than one large riser for deep-plan buildings.
- **Perimeter risers**: Electrical and data risers may be at the perimeter to serve raised floor outlets, reducing cable lengths in the floor void.
- **Fire-rated enclosure**: All risers penetrating fire compartment floors must be fire-rated (typically 60 or 120 minutes). Riser walls: 100mm blockwork or 2x15mm Type F plasterboard on metal stud.
- **Access from common areas**: Risers should be accessible from corridors or service areas, not from within tenancies (for maintenance access without disturbing occupants).

---

## 3. Service Route Hierarchies

### Priority Hierarchy for Clash Resolution

When services conflict in the coordination process, the following hierarchy applies:

1. **Gravity drainage** (soil, waste, rainwater) — Cannot be rerouted easily; requires falls. Highest priority.
2. **Primary HVAC ductwork** — Large cross-section, difficult to reroute. Second priority.
3. **Primary pipework** (CHW/LTHW mains, sprinkler mains) — Large diameter, insulated.
4. **Cable trays and bus-bar** — Can bend and reroute more easily than ducts.
5. **Secondary HVAC branches** — Smaller, more flexible.
6. **Secondary pipework** — Smaller diameter, flexible routing.
7. **Sprinkler distribution** — Small pipes, highly flexible routing.
8. **Terminal equipment** — FCUs, VAV boxes, light fittings — located last to avoid all above.

### Crossover Strategy

Where services running in different directions must cross (e.g., east-west ductwork crosses north-south pipework):

- **Ductwork reduces height at crossover**: Transition from rectangular to wider, shallower section (e.g., 600x400mm becomes 800x300mm for a local crossover zone)
- **Pipework dips or rises**: Small-diameter pipes (<50mm) can dip below ductwork; larger pipes should maintain level and duct transitions around them
- **Dedicated crossover zones**: Define 1-2 crossover locations per structural bay. All intersections occur here, simplifying coordination.
- **Avoid diagonal routes**: All services run orthogonally (parallel to structural grid). Diagonal routes create unpredictable crossovers.

---

## 4. Plant Room Sizing: Rules of Thumb

### Central Mechanical Plant

| Equipment | Sizing Rule | Typical Dimensions |
|---|---|---|
| Air Handling Unit (AHU) | 1 AHU per 500-2000m² floor area | 2.0x1.5x3.0m (small) to 3.0x2.5x8.0m (large) |
| Chiller (air-cooled) | 100-200 W/m² cooling load | 3.0x1.0x2.2m per 200-500 kW |
| Chiller (water-cooled) | 100-200 W/m² cooling load | 2.5x0.8x1.5m per 200-1000 kW |
| Cooling tower | Rejects chiller heat | 2.0x2.0x3.0m per 500 kW; requires open-air location |
| Boiler (gas) | 50-100 W/m² heating load | 1.5x0.8x1.5m per 200-500 kW |
| Heat pump (ASHP) | 80-150 W/m² | 2.0x0.8x1.8m per 50-100 kW; external location |
| Buffer/thermal store | 10-50 litres/kW | 1.0m dia. x 2.0m high per 1000 litres |
| Plate heat exchanger | Matches boiler/chiller capacity | 0.8x0.3x1.2m per 200-500 kW |
| Pumps (CHW/LTHW) | Matched to system flow rate | 0.8x0.4x0.5m per duty pump + standby |
| Calorifier (hot water) | 40-60 litres/person (residential) | 1.0m dia. x 2.0m high per 1000 litres |

### Plant Room Space Allowances

| Building Type | Total Plant Area (% of GFA) | Notes |
|---|---|---|
| Naturally ventilated office | 1.5-3.0% | Boiler room + minimal electrical |
| Air-conditioned office | 5-8% | AHU + chiller + boiler + electrical + generator |
| Hospital (general) | 8-12% | Extensive HVAC, medical gases, sterilisation plant, standby power |
| Hospital (specialist) | 12-18% | Operating theatres, imaging suites, laboratories |
| Hotel | 5-7% | Central boiler/chiller + laundry + kitchen extract |
| Residential (apartments) | 2-4% | Central boiler/heat pump + water storage + electrical |
| Retail (shopping centre) | 4-6% | AHU per tenant zone + central chiller/boiler |
| School | 3-5% | Boiler room + ventilation units + electrical |
| Laboratory | 8-15% | Intensive AHU provision, specialist extract, emergency power |
| Data centre | 25-40% | Massive cooling plant; redundant (N+1 or 2N) systems |

### Plant Room Location Strategy

- **Basement plant**: Boilers, electrical switchgear, water tanks, sprinkler pump, generator. Requires vehicular access for equipment replacement. Minimum 4.0m clear height; 5.0m preferred for large AHUs.
- **Roof plant**: Chillers (air-cooled), cooling towers, AHUs, exhaust fans. Requires structural load allowance (500-2000 kg/m²). Acoustic screening. Crane access for installation/replacement.
- **Intermediate plant floors**: In tall buildings, mechanical floors every 20-30 storeys. Outrigger floors serve dual structural and mechanical function. Reduces riser and duct sizes.
- **Ground-floor plant**: Generator (if no basement), gas meter/governor, incoming water/electrical. Requires direct external access for maintenance and fuel delivery.

### Clearances Within Plant Rooms

- AHU: 1.0m on service side (filter/coil access); 0.6m on non-service side; 1.5m at end for fan removal
- Boiler: 1.0m all sides; 1.5m at flue connection end
- Chiller: 1.0m tube-pull side (full tube length clearance); 0.6m other sides
- Electrical switchboard: 1.0m in front of panels (BS 7671); 0.8m behind if rear access
- Minimum door: 1.2m wide x 2.1m high (larger for equipment entry — double doors 2.4m wide)
- Ceiling height: 4.0-5.0m minimum (AHU rooms with ductwork connections above units)

---

## 5. Below-Ground Services

### Service Entry Coordination

| Service | Typical Depth Below Ground (mm) | Clearance from Foundations | Entry Point |
|---|---|---|---|
| Incoming water main | 750-1350 (below frost line) | 1.0m minimum | Basement wall or ground floor slab |
| Gas supply | 450-750 | 1.0m minimum | Ground floor external wall (never into basement) |
| Electrical (HV) | 600-1000 (in duct) | 1.0m minimum | Substation or main switchroom |
| Electrical (LV) | 600-800 (in duct) | 1.0m minimum | Main switchroom |
| Telecoms/data | 450-600 (in duct) | 0.5m minimum | Comms room at ground/basement |
| Foul drainage | 600-1500+ | Must not undermine foundations | Below slab to public sewer |
| Surface water | 600-1500+ | As foul | To public sewer or SuDS |
| District heating | 600-1000 | 1.0m minimum | Basement energy centre |

### Below-Ground Coordination Rules

- **No services beneath strip/pad foundations**: Route services around foundation footprints with 1.0m minimum clearance.
- **Piled foundations**: Services routed between piles. Pile layout must accommodate service routes — coordinate at scheme design stage.
- **Raft foundations**: Services enter through raft edge (thickened upstand) or through sealed penetrations in the raft slab. Waterproofing continuity critical.
- **Service trenches**: Parallel services separated by 300mm minimum (different utilities). 600mm separation between water and sewer.
- **Drainage falls**: Below-ground drainage at 1:40 (100mm dia.) to 1:150 (150mm+ dia.) — calculate depth at building entry and at sewer connection to confirm feasibility.
- **Inspection chambers**: At every change of direction, junction, and gradient change. Max spacing 45m on straight runs. 450x450mm minimum (up to 600mm deep); 1050mm dia. or 1200x750mm (deeper than 600mm).

---

## 6. Roof Plant Screening

### Visual Screening Requirements

- Screen must fully conceal all plant when viewed from public ground level at the building perimeter (45-degree sight line from building base, or from specific viewpoints defined in planning conditions).
- Screen height: Tallest plant item + 300mm minimum freeboard. Typical: 2.0-3.5m.
- Screen material options:
  - Perforated metal (30-50% open area): Allows airflow while concealing; anodised aluminium, weathering steel, or painted steel
  - Expanded mesh: Lightweight, high open area (40-60%), good ventilation, moderate screening
  - Timber louvre: Biophilic appearance; requires maintenance; spacing 50-100mm with 50% open area
  - Living wall / green screen: Excellent visual screening; irrigation and maintenance required
  - Matching facade material: Best visual integration; may restrict ventilation

### Acoustic Screening Requirements

- Plant noise at nearest noise-sensitive receptor must comply with planning condition (typically background noise level or background +5 dB at night).
- Acoustic louvre: 10-25 dB(A) attenuation depending on louvre depth (150mm: ~10 dB; 300mm: ~15 dB; 600mm: ~25 dB).
- Acoustic enclosure: For individual noisy items (generators, cooling towers). Attenuation 15-35 dB(A).
- Minimum setback: Plant should be 3m from roof edge to reduce noise propagation over edge.

### Structural and Access Considerations

- Plant loads: 5-15 kN/m² on plant plinths (vs 0.75-1.5 kN/m² typical roof live load). Coordinate with structural engineer at concept stage.
- Anti-vibration mounts: Required for all rotating equipment (chillers, pumps, fans, generators). Spring mounts or rubber isolators. 90-98% vibration isolation efficiency required.
- Crane access: Initial installation and future replacement of major plant (chillers, AHUs, generators). Tower crane during construction; mobile crane access for replacement — confirm route and standing location.
- Maintenance access: 800mm minimum between plant items. 1200mm for carrying tools/filters. Designated walkways with anti-slip surface.
- Fall protection: Roof-edge protection (1100mm guardrail) or fall-restraint systems for maintenance personnel.

---

## 7. Coordination Case Studies

### Case Study 1: 15-Storey Commercial Office Tower (London)

**Building parameters**: 15 storeys + 2 basements. 2,500m² per floor. 9.0m structural grid. Composite steel frame with concrete core. Target: BCO Grade A.

**HVAC system**: 4-pipe FCU + DOAS fresh air. Chilled beams on upper floors.

**Coordination challenges and solutions**:
- **Challenge**: 600mm composite beam conflicted with 500mm main supply duct at core zone.
  - **Solution**: Specified cellular beams with 350mm web openings. Primary ductwork routed through beam openings, eliminating the crossover. Floor-to-floor reduced from 4.0m to 3.75m, saving 3.75m total building height and 2,500m² of cladding.
- **Challenge**: Sprinkler main clashing with structural beam at transfer level.
  - **Solution**: Rerouted sprinkler main around beam with 90-degree bends. Added 2m of pipe run but avoided structural modification.
- **Void allocation**: Structure 600mm (cellular beam + 150mm slab), services 300mm (through beam + 200mm below), ceiling 15mm. Total void: 715mm. Clear height: 2750mm + 150mm raised floor. Floor-to-floor: 3630mm, rounded to 3750mm.

### Case Study 2: 200-Bed Hospital (UK NHS)

**Building parameters**: 4 storeys + basement. 8,000m² per floor. 7.5m structural grid. RC flat slab (275mm). Plant rooms: 10% of GFA.

**HVAC system**: Central AHU with terminal reheat. 100% fresh air in clinical zones. Recirculation in non-clinical. Operating theatres with laminar flow canopies.

**Coordination challenges and solutions**:
- **Challenge**: 1200mm ceiling void required in general ward areas, but 3600mm floor-to-floor created excessive building height.
  - **Solution**: Zoned void depth — 1200mm in corridor (primary distribution) tapering to 600mm at window wall (terminal only). Stepped ceiling design. Floor-to-floor maintained at 4200mm with 2700mm clear height in patient areas.
- **Challenge**: Medical gas pipework routing conflicted with structural beam adjacent to operating theatre.
  - **Solution**: Interstitial services zone above operating theatre suite — a full-height (1800mm) walk-in service space between the structural slab and the theatre ceiling. Allows maintenance without disrupting sterile environment below.
- **Riser shafts**: 12 riser shafts per floor. Total riser area: 48m² (0.6% of floor area). Risers grouped into clinical (medical gases, specialist extract, CHW/LTHW) and non-clinical (electrical, data, general HVAC).

### Case Study 3: Mixed-Use Residential Tower (45 Storeys)

**Building parameters**: 45 storeys residential on 5-storey podium (retail/parking). 750m² typical floor. RC core + RC flat slab (PT). Podium: steel frame with PT slab.

**HVAC system**: Centralised heat pump plant at basement and roof. Individual apartment FCUs with corridors served by DOAS. Podium: VRF for retail, natural ventilation for parking.

**Coordination challenges and solutions**:
- **Challenge**: Podium grid (8.1 x 16.2m for parking) incompatible with tower grid (6.0 x 8.0m for residential).
  - **Solution**: 1200mm deep transfer slab at Level 5. Services riser locations aligned between podium and tower — risers positioned at columns that are continuous from tower through podium.
- **Challenge**: Residential ceiling void only 250mm, but corridor requires 400mm for fresh air ductwork.
  - **Solution**: Bulkhead ceiling in corridors (2400mm clear) vs 2600mm clear in apartments. Ductwork in corridor ceiling feeds through apartment entrance wall to ceiling-mounted FCU.
- **Intermediate plant floor**: Level 25 dedicated to mechanical plant. Outrigger trusses for structural bracing occupy same floor. CHW/LTHW risers sized for half-building height (22 floors above and below), reducing pipe sizes by 30% vs full-height risers.

### Case Study 4: University Science Building (4 Storeys)

**Building parameters**: 4 storeys. 3,000m² per floor. 7.5 x 9.0m grid. RC beam-slab (200mm slab + 500mm beams). Mixed laboratory and teaching spaces.

**HVAC system**: VAV for laboratories (6-12 ACH). Chilled beams for teaching spaces. Central AHU plant on roof.

**Coordination challenges and solutions**:
- **Challenge**: Laboratory fume cupboard extract ducts (400mm dia. each, 15+ fume cupboards per floor) congesting the ceiling void and risers.
  - **Solution**: Grouped fume cupboard extract into 4 manifolded risers (800x600mm each) instead of individual duct risers. Manifolds on each floor with fire/smoke dampers. Reduced riser shaft area from 18m² to 8m² per floor.
- **Challenge**: Structural beams at 600mm deep conflicted with 500mm main VAV supply duct.
  - **Solution**: Rotated ductwork to run parallel to beams (not perpendicular). At crossover points, used flat oval duct sections (750x250mm equivalent to 500x400mm rectangular) to pass below beam soffit within the available 400mm zone.
- **Void allocation**: Structure 500mm (beam), services crossing zone 200mm, primary services 500mm (parallel to beam in adjacent zone), secondary 200mm, terminals 150mm, ceiling 15mm. Effective void: 850mm (at beam) to 650mm (away from beam). Floor-to-floor: 4500mm.

### Case Study 5: Retail Shopping Centre Refurbishment

**Building parameters**: Existing 2-storey shopping centre, 1970s construction. RC frame, 10m grid. Adding new food court and cinema on existing roof.

**Coordination challenges and solutions**:
- **Challenge**: Existing ceiling void only 300mm (original natural ventilation design). New food court requires 600mm void for kitchen extract and fresh air supply.
  - **Solution**: Dropped bulkhead ceilings over service corridors (2400mm clear height) carrying primary distribution. Exposed services in dining areas as architectural feature. New extract ductwork (800x500mm) routed through structural penetrations cored through existing beams (with structural engineer approval and carbon fibre reinforcement to beams).
- **Challenge**: Existing building has no sprinkler system. New use requires sprinklers.
  - **Solution**: Surface-mounted sprinkler mains on existing soffit (painted to match). Concealed pendant heads through new ceiling tiles. Sprinkler tank and pump in new rooftop plant room on structural steel platform above existing roof slab.
