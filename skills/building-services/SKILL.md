---
name: building-services
description: >
  Comprehensive building services knowledge for architects covering HVAC system
  selection and spatial impact, plumbing and drainage design, electrical systems
  and power distribution, vertical transportation (elevators and escalators),
  fire protection systems (sprinklers, detection, smoke control), and MEP
  coordination strategies including ceiling void allocation, riser sizing, plant
  room planning, and BIM integration.
---

# Building Services for Architects

## Section 1: HVAC Systems for Architects

Mechanical ventilation, heating, and cooling systems are the single largest consumer of building volume after the primary structure. The architect's HVAC decisions at concept stage — system type, plant room location, riser positions, ceiling void depth — are largely irreversible. This section equips architects to make informed selections and understand spatial consequences.

### Space Allowances: Mechanical Plant as Percentage of GFA

| Building Type | Mechanical Plant (% of GFA) | Notes |
|---|---|---|
| Commercial office (air-conditioned) | 5-8% | Higher end for prestige/lab-grade |
| Commercial office (mixed-mode) | 3-5% | Reduced mechanical plant |
| Hospital / healthcare | 8-12% | Extensive air handling, medical gases, redundancy |
| Hotel | 5-7% | Central plant + individual room FCUs |
| Residential (apartments) | 2-4% | Minimal central plant if individual systems |
| Retail (shopping centre) | 4-6% | Anchor tenants often have own plant |
| School / university | 3-5% | Varies with ventilation strategy |
| Laboratory | 8-15% | High air-change rates, fume cupboards, specialist extract |
| Data centre | 25-40% | Cooling-dominated; massive plant requirement |

### System Type 1: Natural Ventilation

- **Description**: Relies on wind-driven and buoyancy-driven airflow through operable windows, trickle vents, and/or ventilation shafts. No mechanical cooling. Heating by radiators, underfloor heating, or convectors.
- **Spatial impact on architecture**:
  - Floor plate depth: Maximum 12-15m (single-sided ventilation 2.5x floor-to-ceiling height; cross-ventilation up to 5x)
  - No ceiling void for ductwork — 50-150mm for surface pipework/wiring only
  - No AHU plant rooms required
  - Ventilation shafts/stacks may be required for buoyancy-driven ventilation (0.5-1.5m² per stack)
  - Heating plant room: 0.5-1.0% of GFA (boiler room)
- **Energy performance**: 0 kWh/m²/yr for ventilation energy (heating energy 30-60 kWh/m²/yr)
- **Noise ratings**: NR 25-35 (dependent on external noise — problematic on busy roads)
- **Best-fit building types**: Low-rise residential, schools (in temperate climates), low-rise offices in rural/suburban settings
- **Limitations**: Cannot control humidity. Dependent on external conditions. Not suitable for deep plans, noisy sites, polluted environments, or climates with sustained temperatures above 28C.

### System Type 2: Mixed-Mode / Hybrid Ventilation

- **Description**: Natural ventilation used when external conditions permit; mechanical ventilation and cooling activated when natural ventilation is insufficient. Requires automated facade (actuated windows/louvres) and BMS integration.
- **Spatial impact on architecture**:
  - Floor plate depth: 12-18m (wider than pure natural vent due to mechanical backup)
  - Ceiling void: 200-400mm (reduced ductwork for supplementary mode)
  - AHU plant rooms: 1.5-3% of GFA
  - Riser shafts: Smaller than fully air-conditioned — 0.5-1.0m² per floor per riser
- **Energy performance**: 40-70 kWh/m²/yr (total HVAC energy), 30-50% less than full air conditioning
- **COP**: Variable — depends on proportion of mechanical operation
- **Best-fit building types**: Offices (progressive clients), universities, libraries, civic buildings
- **Exemplar**: The Hive, Worcester (2012); Bloomberg HQ, London (2017)

### System Type 3: Fan Coil Units (FCU) + Fresh Air

- **Description**: Centralised fresh air supply (via AHU) provides ventilation air only (typically 10-12 L/s per person). Individual fan coil units at ceiling level provide local heating/cooling using chilled/hot water from central plant. 4-pipe system (separate heating and cooling circuits) is standard for commercial buildings.
- **Spatial impact on architecture**:
  - Ceiling void: 350-500mm (AHU ductwork: 300-400mm rectangular; FCU: 200-300mm high; pipework: 100-150mm)
  - AHU plant room: 2-3% of GFA
  - Chiller plant (roof or basement): 1-2% of GFA
  - Riser shafts: 0.5-0.8m² per floor (4 pipes + fresh air duct)
  - FCU access panels in ceiling: 600x600mm per unit, at 3-6m spacing
- **Ductwork dimensions**: Fresh air main duct: 400x300mm to 800x400mm (depending on floor area served). Branch to each FCU: 200x150mm flex duct.
- **Pipework dimensions**: CHW/HHW mains: 50-100mm diameter. Branch to FCU: 15-22mm diameter.
- **Energy performance**: COP 3.5-5.0 (chiller). Total HVAC energy: 80-120 kWh/m²/yr.
- **Noise ratings**: NR 35-40 (FCU noise can be problematic in quiet spaces — specify low-noise units)
- **Best-fit building types**: Hotels (individual room control), residential apartments (with central plant), commercial offices, hospitals (patient rooms)

### System Type 4: Variable Air Volume (VAV)

- **Description**: Centralised AHUs supply conditioned air through a duct network. VAV terminal boxes at each zone modulate airflow volume to match heating/cooling demand. High airflow rates require large duct sizes.
- **Spatial impact on architecture**:
  - Ceiling void: 500-800mm (large main ducts: 600x400mm to 1200x600mm; branch ducts: 300x250mm to 500x300mm; VAV boxes: 300x400x800mm)
  - AHU plant room: 3-5% of GFA (AHUs are large: typical unit 2.0x1.5x3.0m serving 1000-2000m²)
  - Riser shafts: 1.0-2.0m² per floor (large supply and return air ducts)
  - Return air: Via ceiling plenum or ducted return (adds to void depth if ducted)
- **Ductwork dimensions**: Main supply duct: 800x400mm to 1500x800mm. Branch ducts: 300x200mm to 600x300mm. Return air duct: 70-80% of supply duct size.
- **Energy performance**: COP 3.5-5.5 (chiller). Fan energy significant — variable speed drives reduce this by 30-50%. Total HVAC energy: 90-140 kWh/m²/yr.
- **Noise ratings**: NR 30-40 (well-designed); NR 40-50 (poorly designed — duct velocity critical)
- **Best-fit building types**: Large open-plan offices (>2000m² per floor), laboratories (high air-change rates), clean rooms, trading floors
- **Limitations**: Large duct sizes increase floor-to-floor height. Not efficient for cellular offices with many small zones. Higher fan energy than water-based systems.

### System Type 5: Chilled Beams (Active and Passive)

- **Description**: Chilled water circulates through finned tubes mounted in ceiling-level units. Passive chilled beams rely on natural convection. Active chilled beams induce room air over the coil using a primary air supply from a central AHU.
- **Spatial impact on architecture**:
  - Ceiling void: 300-450mm (active chilled beams: 200-300mm high + primary air duct 150-200mm)
  - AHU plant room: 2-3% of GFA (smaller AHUs than VAV — primary air only)
  - Riser shafts: 0.6-1.0m² per floor (CHW pipes + primary air duct)
  - Chilled beam units: 300-600mm wide x 1200-3000mm long, mounted flush in ceiling grid or exposed
- **Pipework dimensions**: CHW mains: 40-80mm dia. Branch to beam: 15-22mm dia. Primary air duct: 250x200mm to 500x300mm.
- **Energy performance**: Excellent — water transports 4x more energy per unit volume than air. COP 4.0-6.0. Total HVAC: 60-90 kWh/m²/yr.
- **Noise ratings**: NR 25-30 (passive beams are silent; active beams have slight induction noise)
- **Best-fit building types**: Offices (premium), schools, universities, museums — where quiet operation and low energy are priorities
- **Limitations**: Condensation risk — chilled water temperature must stay above dew point (typically 14-16C). Not suitable for high latent loads (kitchens, swimming pools). Limited cooling capacity: 80-120 W/m² (vs 150+ W/m² for FCU/VAV).

### System Type 6: Variable Refrigerant Flow (VRF/VRV)

- **Description**: Direct expansion refrigerant system with one outdoor condensing unit serving multiple indoor fan coil units via refrigerant pipework. Heat recovery variants (3-pipe) allow simultaneous heating and cooling in different zones.
- **Spatial impact on architecture**:
  - Ceiling void: 250-350mm (indoor units: 200-250mm high; refrigerant pipes: 15-30mm dia.)
  - No central AHU plant room required (massive space saving)
  - Outdoor condensing units: roof or ground level, 800x300x900mm each (3-6 per system)
  - Riser shafts: Small — 0.2-0.4m² per floor (refrigerant pipes only; separate fresh air required)
  - Fresh air provision: Separate DOAS or heat recovery ventilation unit required
- **Refrigerant pipework**: Liquid line 6.35-15.88mm dia.; gas line 12.7-28.58mm dia. Maximum pipe run: 165m (varies by manufacturer).
- **Energy performance**: COP 3.5-5.5. Total HVAC: 70-110 kWh/m²/yr.
- **Noise ratings**: NR 30-35 (indoor units); outdoor units can be 55-65 dBA (screen or locate away from noise-sensitive facades)
- **Best-fit building types**: Multi-zone buildings (offices with diverse tenants), retrofit (small pipes suit existing buildings), hotels, residential with individual metering
- **Limitations**: Refrigerant charge limits in occupied spaces (F-gas regulations). Maximum pipe lengths limit building size. Not suitable for very large floor plates. Refrigerant leak detection required.

### System Type 7: Displacement Ventilation

- **Description**: Low-velocity conditioned air supplied at floor level (or low-level wall diffusers) rises naturally through buoyancy as it absorbs heat from occupants and equipment. Extract at ceiling level. Creates stratified temperature profile — cooler at occupied level, warmer at ceiling.
- **Spatial impact on architecture**:
  - Raised floor: 250-400mm (supply air plenum beneath raised floor)
  - Ceiling void: 200-300mm (return air only — smaller than conventional systems)
  - Floor diffusers: Swirl-type, 200-300mm diameter, at 4-6m² per diffuser
  - AHU plant room: 2-3% of GFA
- **Ductwork dimensions**: Underfloor supply through raised floor plenum — no supply ductwork above ceiling. Return ducts at ceiling: 400x300mm to 600x400mm.
- **Energy performance**: 15-30% more efficient than overhead mixing ventilation. Supply air temperature 18-20C (vs 12-14C for mixing). Total HVAC: 55-85 kWh/m²/yr.
- **Noise ratings**: NR 25-30 (very quiet — low air velocities)
- **Best-fit building types**: Auditoria, theatres, concert halls (seated audience generates buoyancy), open-plan offices with raised floors, atriums
- **Limitations**: Supply air temperature limited to 18C minimum (drafts if colder). Cooling capacity limited: 40-60 W/m². Not suitable for spaces with high ceilings and no thermal stratification benefit.

### System Type 8: Dedicated Outdoor Air System (DOAS)

- **Description**: Centralised AHU handles 100% outdoor air (ventilation), conditioning it to neutral temperature and humidity. Separate systems (radiant ceiling, chilled beams, fan coils, active chilled slab) handle local heating/cooling loads. Decouples ventilation from thermal conditioning.
- **Spatial impact on architecture**:
  - DOAS AHU: Smaller than conventional AHU (ventilation air only) — 1.5-2.5% of GFA for plant
  - Ceiling void: Dependent on local system (radiant: 100-200mm; chilled beams: 300-450mm)
  - Riser shafts: DOAS duct + local system pipework — 0.6-1.2m² per floor
- **Energy performance**: Total HVAC energy: 50-80 kWh/m²/yr (when paired with radiant system)
- **Best-fit building types**: High-performance offices, Passivhaus-adjacent designs, any building targeting ultra-low energy
- **Exemplar**: Bullitt Center, Seattle (2013); One Angel Square, Manchester (2013)

### System Type 9: District Heating and Cooling

- **Description**: Thermal energy supplied to buildings from a centralised district energy plant via underground insulated pipes. Buildings connect via heat exchangers in a plant room (energy transfer station, ETS).
- **Spatial impact on architecture**:
  - No boiler or chiller plant on site (major space saving: eliminates 2-4% of GFA)
  - ETS plant room: 0.5-1.0% of GFA (heat exchangers, pumps, meters)
  - Underground pipe entry point required at basement/ground level
  - Distribution within building: Standard LTHW/CHW pipework from ETS
- **Energy performance**: Varies by district source — CHP 80-90% efficiency; waste heat recovery can be near-zero carbon; ground-source heat pump networks COP 3.5-5.0
- **Best-fit building types**: Urban mixed-use developments, campus developments (universities, hospitals), masterplan-scale projects
- **Exemplar**: Copenhagen district heating (serves 98% of city); Olympic Park London (2012); Battersea Power Station redevelopment

---

## Section 2: Plumbing and Drainage

### Hot and Cold Water Distribution

**Cold water supply systems:**
- **Direct system**: Mains pressure to all outlets. Typical in low-rise residential. Incoming main: 25-32mm (house), 50-80mm (apartment block), 80-150mm (commercial).
- **Indirect system**: Mains fills roof-level storage tank; outlets fed by gravity. Provides storage for peak demand and pressure regulation. Tank sizing: 115 litres per person per day (office); 135 litres per person per day (residential).
- **Boosted system**: Pumped supply for tall buildings where mains pressure insufficient. Break tanks at basement; booster pumps; roof tanks or pressure vessels at upper levels. Pressure zones every 30-40m of height.

**Hot water systems:**
- **Point-of-use heaters**: Electric instantaneous or small storage (6-15 litres). Minimal pipework. Suit remote outlets.
- **Centralised calorifier**: Storage vessel heated by boiler or heat pump. Capacity: 40-60 litres per person (residential); 5-10 litres per person (office). Located in plant room.
- **Plate heat exchanger + thermal store**: More efficient than calorifier. Common in district heating connections.
- **Legionella prevention**: Store hot water at 60C minimum, distribute at 55C minimum, return at 50C minimum. Dead-legs must be <3m or have trace heating.

### Pipe Sizes (Typical)

| Pipe Function | Typical Diameter |
|---|---|
| Individual outlet (basin, WC cistern) | 15mm |
| Branch (serving 2-5 outlets) | 22mm |
| Sub-main (serving a floor or group) | 28-35mm |
| Main riser (cold water up, hot water flow/return) | 35-54mm |
| Incoming main (apartment block) | 50-80mm |
| Incoming main (commercial building) | 80-150mm |

### Drainage Systems

**Soil drainage (foul water — WCs, urinals):**
- WC branch: 100mm diameter (min. 1:40 gradient or steeper)
- Soil stack (vertical): 100mm diameter (serves up to 10 floors of residential)
- Building drain (horizontal below ground): 100-150mm (1:40 to 1:80 gradient)

**Waste drainage (basins, showers, sinks, baths):**
- Individual waste pipe: 32mm (basin), 40mm (bath/shower/sink)
- Waste branch: 50mm (multiple outlets)
- Combined waste/soil stack: 100mm (if receiving both waste and soil)

**Rainwater drainage:**
- Roof outlet sizing: Based on rainfall intensity (75mm/hr UK design standard; 150mm/hr tropical)
- Downpipe: 75mm (up to 55m² roof), 100mm (up to 130m² roof), 150mm (up to 300m² roof)
- Siphonic drainage: Higher capacity at smaller pipe sizes but requires specialist design. 56mm siphonic pipe equivalent to 100mm conventional.

### Drainage Falls

| Pipe Diameter | Minimum Gradient | Maximum Gradient |
|---|---|---|
| 50mm waste | 1:40 (25mm per metre) | 1:20 |
| 75mm waste/rainwater | 1:40 to 1:50 | 1:20 |
| 100mm soil/drain | 1:40 (minimum 1 WC) to 1:80 (5+ WCs) | 1:20 |
| 150mm drain | 1:80 to 1:150 | 1:40 |

### Wet-Room Stacking Principle

Bathrooms, kitchens, and other wet rooms should be stacked vertically through the building to minimise horizontal drainage runs. Horizontal drains require falls (25-40mm per metre) which consume floor void depth. Non-stacked wet rooms create:
- Longer pipe runs
- Deeper floor voids to accommodate falls
- More penetrations through structural elements
- Greater risk of leaks above occupied spaces

**Design rule**: All wet rooms should be within 3m horizontal distance of a soil/waste stack.

### Riser Sizing

| Service | Typical Riser Size | Notes |
|---|---|---|
| Cold water (residential, per 8-10 apartments) | 150x150mm duct (35-54mm pipe + insulation) | Insulation for condensation prevention |
| Hot water (residential, per 8-10 apartments) | 150x150mm duct (35-54mm pipe + insulation) | Flow and return pipes |
| Soil/waste stack (per group of bathrooms) | 150x150mm duct (100mm pipe) | Access required at each floor |
| Combined services riser (residential) | 600x400mm duct | CW, HW, soil, waste, rainwater, gas |
| Rainwater stack | 100x100mm duct (75-100mm pipe) | Internal or external |

---

## Section 3: Electrical Systems

### Power Distribution Hierarchy

1. **Incoming supply**: From utility transformer or on-site substation. Voltage: 400V 3-phase (UK/EU) or 480V 3-phase (US). Incoming cable: typically via underground duct to main switchroom at ground/basement level.
2. **Main switchboard (MSB)**: Located in main electrical switchroom. Distributes power to sub-main distribution boards via vertical bus-bar risers or cable risers.
3. **Sub-main distribution boards**: Located on each floor (or every 2-3 floors in residential). Size: typically 800x2000mm wall-mounted panel.
4. **Final distribution boards**: Local to each tenancy or zone. Feed final circuits (lighting, small power, dedicated equipment).
5. **Final circuits**: Ring mains (UK: 32A, serving 100m² floor area) or radial circuits (US: 20A, serving 50-80m² floor area).

### Typical Electrical Loads by Building Type

| Building Type | Small Power (W/m²) | Lighting (W/m²) | Total Electrical (W/m²) | Notes |
|---|---|---|---|---|
| Commercial office (standard) | 25-35 | 10-12 | 50-80 | Includes IT loads |
| Commercial office (trading floor) | 50-80 | 10-12 | 80-150 | High-density IT |
| Residential (apartment) | 15-25 | 5-8 | 30-50 | Per unit |
| Hotel (guest room) | 10-15 | 5-8 | 20-40 | Per room |
| Retail (general) | 15-25 | 12-18 | 40-60 | Higher lighting |
| Hospital (general areas) | 20-30 | 8-12 | 50-80 | Excludes specialist equipment |
| Hospital (operating theatre) | 50-100 | 15-20 | 100-200 | High specialist loads |
| School / university | 15-25 | 8-12 | 30-50 | IT rooms higher |
| Laboratory | 40-80 | 10-15 | 80-150 | Varies widely by type |
| Data centre | 500-2000 | 5-10 | 500-2000+ | IT load dominant |
| Warehouse / industrial | 5-15 | 5-10 | 15-30 | Excludes process loads |

### Emergency Power

- **Standby generator**: Diesel generator providing backup power during mains failure. Sizing: 30-50% of building total load (life safety + critical systems). Location: basement or roof (with fuel storage, exhaust flue, acoustic enclosure). Space requirement: 1.0-2.5m² per 100 kVA. Typical office generator: 200-500 kVA (5-10m² generator room).
- **Uninterruptible Power Supply (UPS)**: Battery backup for zero-interruption supply to critical loads (IT, medical equipment, security). Typically 5-30 minutes autonomy. Battery room: 0.5-2.0m² per 100 kVA.
- **Essential circuits**: Life safety lighting, fire alarm, smoke extract fans, firefighting lift, sprinkler pumps — must have secondary power supply (generator or battery).

### Lightning Protection

- **Requirement**: BS EN 62305 risk assessment determines need. Generally required for buildings over 20m, buildings with high occupancy, or buildings with sensitive equipment.
- **Components**: Air termination network (roof conductors at 10-20m mesh), down conductors (at 10-20m spacing around perimeter), earth electrodes (ring earth at foundation level).
- **Spatial impact**: Down conductors run inside or outside the facade — coordinate with cladding design. Test clamps required at 1.5m above ground level.

### Electrical Riser Sizing

| Building Type | Electrical Riser Size (per floor) | Notes |
|---|---|---|
| Residential (per 8-10 apartments) | 400x200mm | Bus-bar riser or cable tray |
| Commercial office (per floor of 1000m²) | 600x400mm | Bus-bar or cable ladder |
| Hospital (per floor) | 800x400mm | Separated essential and normal circuits |

### Lighting Power Density Targets (ASHRAE 90.1 / CIBSE)

| Space Type | ASHRAE 90.1 LPD (W/m²) | CIBSE Target (W/m²) | Maintained Illuminance (lux) |
|---|---|---|---|
| Open-plan office | 9.8 | 8-10 | 300-500 |
| Private office | 10.1 | 8-10 | 300-500 |
| Retail (general) | 11.8 | 12-15 | 300-500 |
| Retail (accent/display) | 16.1 | 15-20 | 500-1000 |
| Classroom | 10.5 | 8-10 | 300-500 |
| Hospital ward | 8.1 | 6-8 | 100-300 |
| Corridor / circulation | 5.4 | 4-6 | 100-150 |
| Car park | 1.8 | 2-3 | 75-100 |
| Warehouse | 6.0 | 5-8 | 150-300 |

---

## Section 4: Vertical Transportation

### Elevator Types

| Type | Mechanism | Machine Room | Max Speed (m/s) | Max Travel (m) | Best-Fit |
|---|---|---|---|---|---|
| Traction (geared) | Motor + gearbox + ropes | Above shaft | 2.5 | 60 | Mid-rise, 5-20 floors |
| Traction (gearless) | Direct-drive motor + ropes | Above shaft | 10+ | 500+ | High-rise, express lifts |
| Machine-room-less (MRL) | Motor in shaft headroom | None (motor in shaft) | 4.0 | 75 | Most common today, up to 25 floors |
| Hydraulic | Hydraulic ram | Below shaft (pump room) | 1.0 | 18 | Low-rise, 2-6 floors, goods lifts |
| Double-deck | Two cabins, one above other | Above shaft | 10+ | 500+ | Super-tall, high-density |

### Elevator Sizing Formula

**Number of elevators required:**

n = (P x RTT) / (300 x HC)

Where:
- **P** = peak population to be served (typically 80% of building population arriving in 5 minutes for office)
- **RTT** = Round Trip Time in seconds (time for one complete cycle: loading + travel up + stops + unloading + travel down)
- **300** = 300 seconds (5-minute peak period)
- **HC** = Handling Capacity per car (typically 80% of rated capacity — e.g., 80% x 21 persons = 17 persons for a 1600kg lift)

**RTT estimation (simplified):**
RTT = 2 x H/V + (S x ts) + 2 x P x tp

Where:
- H = total travel height (m)
- V = rated speed (m/s)
- S = number of stops (probable) — approximately N x (1 - ((N-1)/N)^P) where N = number of floors
- ts = stop time (door open + close + acceleration/deceleration) ≈ 8-12 seconds
- P = passengers per trip
- tp = passenger transfer time ≈ 1.2 seconds

**Target performance (BCO standard for UK offices):**
- Waiting interval: <25 seconds (Grade A office); <30 seconds (Grade B)
- Handling capacity: 12-15% of building population in 5 minutes
- Time to destination: <90 seconds (including wait)

### Elevator Shaft Dimensions

| Rated Load (kg) | Persons | Car Internal (mm) W x D | Shaft Internal (mm) W x D | Door Width (mm) | Pit Depth (mm) | Headroom Above Top Floor (mm) |
|---|---|---|---|---|---|---|
| 630 | 8 | 1100 x 1400 | 1700 x 1900 | 800 | 1400 | 3600 |
| 1000 | 13 | 1350 x 1600 | 1950 x 2100 | 900 | 1400 | 3800 |
| 1275 | 17 | 1600 x 1600 | 2200 x 2100 | 1000 | 1400 | 3800 |
| 1600 | 21 | 1600 x 2100 | 2200 x 2600 | 1100 | 1500 | 4200 |
| 2000 | 26 | 2000 x 2100 | 2600 x 2600 | 1200 | 1500 | 4200 |
| 2500 (goods) | — | 2100 x 2700 | 2700 x 3400 | 1300 | 1500 | 4500 |

**Notes**: Shaft dimensions include structural walls (150-200mm concrete each side). Counter-weight space at rear of shaft. MRL lifts require slightly taller headroom (add 400-600mm) but eliminate machine room.

### Escalator Dimensions

| Parameter | Standard (30 degree) | High-Rise (35 degree) |
|---|---|---|
| Step width | 1000mm (standard) or 800mm (narrow) | 1000mm |
| Overall width (including balustrade) | 1200mm (800mm step) or 1400mm (1000mm step) | 1400mm |
| Incline angle | 30 degrees | 35 degrees |
| Speed | 0.5 m/s | 0.5 m/s |
| Capacity | 6000-9000 persons/hour (1000mm step) | 6000-9000 persons/hour |
| Pit depth | 1000-1200mm | 1000-1200mm |
| Headroom (minimum) | 2300mm clear above any step | 2300mm |
| Floor-to-floor height (typical) | 3500-6000mm | 3500-6000mm |
| Horizontal run-out at top and bottom | 800-1000mm flat steps before incline | 600-800mm |
| Structural opening (per pair up + down) | 2800-3200mm wide x varies long | As left |

**Planning rule**: For floor-to-floor height of 4000mm at 30 degrees: horizontal length ≈ 4000/tan(30) = 6930mm + 1600mm run-outs = 8530mm total plan length.

### Goods Lift Sizing

| Application | Rated Load (kg) | Car Internal (mm) W x D x H | Door Width x Height (mm) |
|---|---|---|---|
| Service lift (catering trolleys) | 300-500 | 1000 x 1200 x 2100 | 800 x 2000 |
| Bed lift (hospital) | 2000-2500 | 1400 x 2400 x 2300 | 1300 x 2100 |
| Goods/furniture lift | 2000-3000 | 2100 x 2700 x 2400 | 1800 x 2200 |
| Car lift (vehicle transport) | 3000-5000 | 2700 x 5500 x 2200 | 2500 x 2100 |
| Firefighting lift | 1000-1600 | Per BS EN 81-72 | 800-1100 x 2000 |

---

## Section 5: Fire Protection Systems

### Sprinkler Systems

| Type | Description | Application | Activation |
|---|---|---|---|
| Wet-pipe | Pipes permanently charged with water | Heated buildings (most common) | Individual head activates at rated temperature (57-74C) |
| Dry-pipe | Pipes charged with compressed air; water admitted on activation | Unheated spaces (car parks, loading docks), freezing risk | Individual head; water fills pipe after air release |
| Pre-action | Dry pipe; water admitted only when fire detection system also activates | Areas with high-value contents (museums, server rooms, archives) | Detection + head activation (double interlock) |
| Deluge | All heads open (no thermal element); water floods entire zone on detection | High-hazard industrial, aircraft hangars, transformer rooms | Detection system triggers |

**Sprinkler spacing rules (BS EN 12845 / NFPA 13):**
- Light hazard (offices, hotels, residential): Maximum 4.6m between heads; 12m² coverage per head; 21m² per head (NFPA residential)
- Ordinary hazard (retail, car parks, factories): Maximum 4.0m between heads; 12m² per head
- High hazard (warehouse, industrial storage): Maximum 3.7m between heads; 9m² per head

**Sprinkler head clearance**: 25-30mm below ceiling (minimum); heads must be within 150mm of soffit level. Obstruction rules: heads must be 3x distance from obstruction as the distance the obstruction is below the ceiling.

**System sizing:**
- Light hazard design density: 2.25 mm/min over 84m² assumed maximum area of operation
- Ordinary hazard: 5.0 mm/min over 144-360m² (depending on OH group)
- Riser sizes: 65mm (light hazard, small area); 100mm (ordinary hazard); 150mm (high hazard/large buildings)
- Fire pump: Required if mains pressure/flow insufficient. Typically 100-300 L/min (light hazard); 500-2000 L/min (ordinary/high hazard). Pump room: 15-25m².

**Water storage:**
- Tank sizing: Flow rate x duration. Light hazard: 30 minutes; ordinary: 60 minutes; high hazard: 90 minutes.
- Typical tank: 20-50m³ (light hazard office); 100-300m³ (warehouse)

### Fire Detection and Alarm Systems

| Type | Detector Type | Coverage | Application |
|---|---|---|---|
| Conventional | Point detectors wired in zones | 1 detector per 50m² (smoke); 1 per 30m² (heat) | Small buildings, low budget |
| Addressable | Individual detector addresses on loop | Same coverage as conventional; faster identification | Standard for commercial buildings |
| Analogue addressable | Detectors report analogue values; panel sets thresholds | Enhanced sensitivity; pre-alarm capability | Premium offices, hospitals, heritage |
| Aspirating (VESDA) | Network of sampling pipes, central laser detector | Pipe network at ceiling; one unit per 200-500m² | High-value (data centres, clean rooms, museums) |
| Beam detector | IR beam across space | 1 beam per 500-1000m² in large open volumes | Warehouses, atria, churches, hangars |
| Linear heat detection | Cable detects temperature along its length | Along cable routes, car parks, tunnels | Cable trays, tunnels, conveyor belts |

### Smoke Control Systems

| Type | Mechanism | Application | Spatial Impact |
|---|---|---|---|
| Natural smoke ventilation | Roof vents/openable windows; buoyancy drives smoke out | Single-storey buildings, small atria | Roof openings: 2-5% of floor area; minimum 1.5m² per vent |
| Mechanical smoke extract | Powered fans extract smoke from fire zone | Multi-storey, basement, large atria | Extract fan: 3-10 m³/s per zone; ductwork: 600-1200mm dia. or equivalent |
| Smoke curtains | Motorised fabric barriers descend from ceiling | Atria, open-plan floors, shopping centres | 100-200mm housing at ceiling level; drops to 3m below ceiling |
| Pressurisation | Fans pressurise escape stairs/lobbies to prevent smoke entry | Stair cores in tall buildings (>30m), basement stairs | Supply fan: 1-5 m³/s per stair; dedicated shaft or ductwork |

**Design standards:**
- BS 7346 (components), BS EN 12101 (systems), BS 9999 (design guidance)
- Stair pressurisation: 50 Pa positive pressure with all doors closed; 10 Pa with one door open. Air velocity through open door: 0.75 m/s minimum.
- Smoke reservoir depth: 2.5-3.0m minimum beneath roof in naturally ventilated spaces; clear height below smoke layer: 2.5-3.0m.

### Fire Suppression (Specialist)

| System | Agent | Application | Spatial Impact |
|---|---|---|---|
| Gas suppression (FM-200, Novec 1230) | Clean agent gas | Server rooms, archives, museums | Cylinder storage: 1-2m² per 50m³ room volume; sealed room required |
| CO2 suppression | Carbon dioxide | Electrical switchgear, industrial | Hazardous to life — lockout system required; ventilation after discharge |
| Water mist | Fine water droplets (<1mm) | Heritage buildings, tunnels, turbine halls | Smaller pipe sizes than sprinkler (25-50mm); higher pressure (40-200 bar) |
| Foam | AFFF (aqueous film-forming foam) | Aircraft hangars, fuel storage, car showrooms | Foam tanks, proportioning equipment, foam makers |

---

## Section 6: MEP Coordination

### Spatial Coordination Strategy

The fundamental principle of MEP coordination is zone allocation: reserving specific depths in the floor/ceiling void for structure, services, and finishes in a defined hierarchy.

**Vertical zone allocation (from structural slab downward):**

1. **Structure zone**: Beam depth (or flat slab soffit). Nothing penetrates the structure without structural engineer approval.
2. **Primary services zone**: Large ducts, main cable trays, main pipe runs. Runs perpendicular to or along primary structure.
3. **Secondary services zone**: Branch ducts, secondary cable trays, sprinkler mains. Runs perpendicular to primary services.
4. **Terminal services zone**: Sprinkler drops, light fittings, FCU units, chilled beams, final circuits. Closest to ceiling.
5. **Ceiling finish**: Plasterboard, suspended tile, exposed services (if applicable).

### Typical Ceiling Void Depths

| Building Type | Minimum Void (mm) | Typical Void (mm) | Maximum Void (mm) | Notes |
|---|---|---|---|---|
| Residential (apartment) | 200 | 300-400 | 500 | Simple services; may be flush ceiling with bulkheads |
| Hotel (guest room) | 250 | 350-450 | 550 | FCU + fresh air duct + sprinkler |
| Commercial office (standard) | 400 | 500-700 | 900 | VAV or FCU + cable trays + sprinkler |
| Commercial office (premium) | 350 | 450-600 | 700 | Chilled beams + reduced ductwork |
| Retail (shell unit) | 400 | 600-800 | 1000 | Large HVAC ducts for high cooling loads |
| Hospital (general ward) | 600 | 800-1000 | 1200 | Extensive services, medical gases, access requirements |
| Hospital (operating suite) | 800 | 1000-1500 | 2000 | Laminar flow, theatre pendants, interstitial space |
| School / university | 300 | 400-600 | 700 | Mixed-mode may reduce void |
| Laboratory | 600 | 800-1200 | 1500 | Fume extract, specialist gases, variable air volume |

### Clash Detection Process

**Stage 1: Design Coordination (pre-BIM clash detection)**
- Agree zone allocation drawings showing reserved depths for each service in section
- Define priority hierarchy: gravity drainage > primary ductwork > primary pipework > cable trays > secondary branches > terminals
- Identify coordination "hot spots": risers, plant rooms, ceiling void crossover points, low-headroom areas, transfer beam locations

**Stage 2: BIM Clash Detection**
- Model all services to agreed LOD (Level of Development):
  - LOD 200 (concept): Approximate sizes and routes
  - LOD 300 (developed design): Specific sizes, materials, connections. Sufficient for coordination.
  - LOD 350: Specific sizes plus supports, hangers, access clearances
  - LOD 400 (construction): Fabrication-ready models
- Run automated clash detection (Navisworks, Solibri, BIM Collab)
- Classify clashes: Hard (physical intersection), soft (clearance violation), workflow (sequencing)
- Resolve through weekly coordination meetings

**Stage 3: Construction Coordination**
- Produce coordinated services sections at key locations (1:20 or 1:25 scale)
- Issue combined services drawings (CSD) for each ceiling zone
- Agree installation sequence: structure → main cable trays → main ductwork → main pipework → branches → terminals → ceiling

### Riser Shaft Sizing

| Service Riser | Size per Floor (m²) | Notes |
|---|---|---|
| Electrical (bus-bar + cable trays) | 0.4-0.6 | 600x800mm typical; segregate from water |
| Data/telecoms | 0.2-0.4 | 400x600mm; may combine with electrical |
| Cold water | 0.2-0.3 | 300x400mm; insulated pipes + valve access |
| Hot water (flow + return) | 0.2-0.3 | 300x400mm; insulated pipes |
| Soil/waste stack | 0.2-0.3 | 300x400mm; access panels at each floor |
| Rainwater | 0.1-0.2 | 200x200mm (internal downpipe) |
| HVAC (supply + extract duct) | 0.5-2.0+ | Highly variable — depends on system type and floor area served |
| Gas | 0.1-0.2 | 200x200mm; fire-sealed at each floor |
| Fire sprinkler riser | 0.2-0.3 | 300x300mm; valve set at each floor |
| Smoke extract shaft | 0.5-2.0 | Building-specific; fire-rated construction |

**Combined riser strategy:**
- Group risers by type: wet risers together (water, sprinkler, drainage), dry risers together (electrical, data, HVAC)
- Minimum riser dimensions: 600mm depth for access (person entry for maintenance)
- Access doors: 600x600mm minimum at each floor level, 450x450mm for small risers
- Fire stopping: All penetrations through fire-rated floors and walls must be fire-stopped to match the fire rating of the element penetrated

### Plant Room Sizing Rules of Thumb

| Plant Room | Size (% of GFA) | Typical Location |
|---|---|---|
| Main mechanical plant (AHU, boilers, chillers) | 3-6% (office), 5-10% (hospital) | Basement and/or roof |
| Chiller plant | 0.5-1.5% | Roof (air-cooled) or basement (water-cooled with cooling tower on roof) |
| Boiler plant | 0.3-0.8% | Basement or ground floor (gas supply access, flue route to roof) |
| Main electrical switchroom | 0.3-0.5% | Ground or basement (utility connection) |
| Generator room | 0.3-0.5% | Basement (with exhaust flue to exterior) or ground level |
| UPS / battery room | 0.1-0.3% | Adjacent to IT/server rooms |
| Water tank room | 0.2-0.5% | Roof (gravity) or basement (boosted) |
| Sprinkler pump room | 0.1-0.2% | Ground or basement (near water supply) |
| Lift motor room (if applicable) | 10-15m² per lift group | Above shaft |
| BMS / controls room | 10-20m² | Central location, any floor |

### Below-Ground Services

External services entering the building below ground:
- **Incoming water main**: 80-150mm dia., min. 750mm deep (frost), entry at meter location
- **Gas supply**: 50-100mm dia., min. 450mm deep, entry at meter/governor
- **Electrical supply**: HV cable from substation or LV from transformer, min. 600mm deep in duct
- **Telecoms/data**: Multiple duct entries, min. 450mm deep
- **Foul drainage**: 100-225mm dia., min. 600mm deep, to public sewer or treatment
- **Surface water drainage**: 100-300mm dia., to public sewer, soakaway, or attenuation tank
- **District heating/cooling**: Insulated pre-insulated pipe (DN50-DN200), min. 600mm deep

**Coordination**: Below-ground services survey (PAS 128) essential before design. Services should not cross beneath foundations. Allow 1m clear separation between parallel services of different types. Service trenches should be accessible without excavating building foundations.

### Roof Plant Screening

Roof-mounted plant (chillers, AHUs, cooling towers, generators, exhaust fans) typically requires acoustic and visual screening:
- **Acoustic enclosure**: Required if plant noise exceeds planning limits at nearest sensitive receptor. Typically 10-25 dB(A) attenuation needed. Louvred enclosure with acoustic lining.
- **Visual screening**: Height to fully screen tallest plant item (typically 2.0-3.0m). Material to match building aesthetic (perforated metal, expanded mesh, timber louvre, living wall).
- **Access**: Maintenance access routes to all plant items. Minimum 800mm clear between plant and screen. Crane access or hatch for plant replacement.
- **Structural load**: Roof structure must be designed for plant loads. Typical: chiller 100-300 kN on 4 supports; AHU 50-200 kN; cooling tower 50-150 kN. Anti-vibration mounts required.
- **Planning impact**: Roof plant and screening count toward building height. Screen height must be included in planning application. Some authorities require 45-degree sight line analysis from ground level.

### Renewable Energy Integration

Architects must coordinate the spatial and structural requirements of on-site renewable energy systems:

- **Photovoltaic (PV) panels**: Roof area required — 6-8m² per kWp. Typical office yield: 150-180 kWh/m² panel/year (UK); 250-350 kWh/m² (southern US/Mediterranean). Weight: 12-20 kg/m² including mounting. Orientation: ideally south-facing at 30-35 degree tilt, but east-west flat arrays acceptable at 85-90% yield. Minimum 300mm gap below panels for maintenance. Avoid shading from roof plant — PV layout coordinated with plant screening.
- **Solar thermal**: 2-4m² per dwelling (domestic hot water). Higher yield than PV per m² for hot water but limited application to space heating. Pipe runs from roof to plant room (15-22mm insulated copper).
- **Wind turbines**: Building-mounted micro-turbines generally underperform. Roof-mounted or building-integrated vertical-axis turbines: 1-10 kW. Vibration and noise transfer to structure is a significant issue. Most effective as standalone mast-mounted units on exposed sites.
- **Heat pumps (ASHP/GSHP)**: See HVAC Section. Space requirements in plant room: 1.5-2.5% of GFA. External units require acoustic setback from boundaries.
- **Battery storage**: Lithium-ion battery arrays for PV storage or demand response. Space: 0.5-1.0m² per 10 kWh. Weight: 100-200 kg per 10 kWh. Ventilation and fire suppression requirements per NFPA 855. Temperature control: 15-25C operating range.

### Building Management System (BMS) and Smart Controls

The BMS integrates all building services into a single monitoring and control platform. Spatial and infrastructure requirements:

- **BMS head-end / server room**: 10-20m² (centralised PC/server, UPS, network switches)
- **BMS outstations**: One per floor or zone, mounted in riser cupboard or ceiling void (300x200x100mm controller units)
- **Cabling**: Cat 6A or fibre backbone to each outstation. BACnet/IP or Modbus protocol. Dedicated containment (50x50mm to 100x100mm trunking) separate from power cables.
- **Sensors**: Temperature (every zone), CO2 (occupied spaces), humidity (critical zones), occupancy/PIR (lighting and ventilation control), lux level (daylight dimming). Wired or wireless — wireless reduces containment but requires gateway devices.
- **Integration points**: HVAC controllers, lighting controllers (DALI), blinds/shading, access control, fire alarm (monitoring only), lifts (monitoring only), energy meters (sub-metering at distribution board level).
- **Smart building platforms**: Modern buildings increasingly deploy IoT platforms above the BMS layer for data analytics, predictive maintenance, occupancy analytics, and tenant apps. Requires robust Wi-Fi 6 / 5G infrastructure and edge computing nodes (one per 2-3 floors).

### Services Design Benchmarks by Building Type

| Parameter | Residential | Office | Hospital | School | Hotel |
|---|---|---|---|---|---|
| Heating load (W/m²) | 40-60 | 30-50 | 50-80 | 40-60 | 40-60 |
| Cooling load (W/m²) | 30-50 | 60-100 | 80-150 | 30-60 | 50-80 |
| Fresh air rate (L/s/person) | 8-12 | 10-12 | 10-15 | 5-8 | 10-12 |
| Small power (W/m²) | 15-25 | 25-35 | 20-30 | 15-25 | 10-15 |
| Lighting power (W/m²) | 5-8 | 8-12 | 8-12 | 8-10 | 5-10 |
| Hot water demand (L/person/day) | 40-60 | 3-5 | 50-80 | 3-5 | 100-150 |
| Plant room (% GFA) | 2-4 | 5-8 | 8-12 | 3-5 | 5-7 |
| Ceiling void (mm) | 200-400 | 500-800 | 800-1200 | 400-600 | 350-500 |
| Riser area (% floor area) | 1.0-1.5 | 1.5-2.5 | 2.5-4.0 | 1.0-2.0 | 1.5-2.5 |
