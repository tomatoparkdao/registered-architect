# HVAC Systems: Comprehensive Reference

This reference provides detailed technical comparison of 12 HVAC system types for architectural practice. Data covers spatial requirements, energy performance, noise levels, control strategies, maintenance access, cost comparison, embodied carbon, and building type suitability.

---

## 1. Natural Ventilation

### Operating Principle
Air movement driven by wind pressure differences across the building envelope (wind-driven) and temperature differences between inside and outside (stack/buoyancy-driven). Operable windows, trickle vents, louvres, and ventilation shafts provide openings. No mechanical cooling; heating provided by separate systems (radiators, UFH).

### Spatial Requirements
- **Ductwork**: None
- **Pipework**: Heating only — LTHW radiator circuit, 15-28mm diameter branches, 28-54mm mains
- **Plant rooms**: Boiler room only — 0.5-1.0% of GFA
- **AHU dimensions**: N/A
- **Ceiling void**: 50-150mm (surface pipework and wiring only)
- **Floor plate constraint**: Max 12-15m deep (single-sided: 2.5x floor-to-ceiling height; cross-ventilation: 5x)
- **Ventilation openings**: 5-10% of floor area as free openable area
- **Ventilation stacks**: 0.5-1.5m² per stack for buoyancy-driven systems; stack height drives airflow rate

### Energy Performance
- **Ventilation energy**: 0 kWh/m²/yr (no fans)
- **Heating energy**: 30-60 kWh/m²/yr (climate-dependent)
- **Cooling energy**: 0 kWh/m²/yr
- **Total HVAC**: 30-60 kWh/m²/yr
- **COP**: N/A (no refrigeration cycle)

### Noise Levels
- NR 25-35 internally (dependent on external noise environment)
- No mechanical noise generated
- Road/rail/aircraft noise may be problematic when windows are open

### Control Strategy
Manual (occupant-operated windows) or automated (BMS-controlled actuators on windows/louvres). Weather stations on roof provide wind speed/direction and rain data. CO2 sensors in occupied spaces trigger opening when levels exceed 800-1000 ppm.

### Maintenance Access Requirements
Minimal — window actuators, ventilation louvres, heating system. No filter changes, no fan belt replacement. Lowest maintenance cost of all HVAC systems.

### Capital Cost Comparison
- Capital cost: Very low — 50-80 $/m² (heating system + openable windows)
- Annual maintenance: 2-5 $/m²/yr

### Operational Cost Comparison
- Annual energy cost: 3-6 $/m²/yr (heating only)
- Lowest operational cost of any HVAC strategy

### Embodied Carbon
- System embodied carbon: 5-15 kgCO2e/m² (radiators, boiler, pipework only)
- Lowest embodied carbon of any HVAC strategy

### Best-Fit Building Types
- Low-rise residential (houses, low-rise apartments)
- Schools in temperate climates (BB101 compliant designs in UK)
- Low-rise offices in suburban/rural locations (temperate climates)
- Community buildings, churches, village halls

---

## 2. Mixed-Mode / Hybrid Ventilation

### Operating Principle
Natural ventilation operates when external conditions are suitable (temperature 16-26C, wind speed acceptable, air quality adequate). Mechanical ventilation and cooling activated when conditions exceed natural ventilation capability. Changeover controlled by BMS based on external temperature, CO2, humidity, and wind data.

### Spatial Requirements
- **Ductwork**: Reduced compared to full mechanical — supply ducts 300x200mm to 600x400mm (supplementary mode)
- **Pipework**: Heating circuit (LTHW) + cooling circuit (CHW if used) — 28-54mm mains
- **Plant rooms**: 1.5-3.0% of GFA (smaller AHU, possibly no chiller if mechanical mode limited)
- **AHU dimensions**: 1.0x0.8x2.0m to 1.5x1.2x3.0m (smaller than full mechanical)
- **Ceiling void**: 200-400mm
- **Floor plate constraint**: 12-18m depth (wider than pure natural due to mechanical backup)
- **Facade**: Automated openable elements (actuated windows, motorised louvres) — coordinate with facade consultant

### Energy Performance
- **Total HVAC**: 40-70 kWh/m²/yr
- **COP**: Varies by operating mode
- **Energy saving vs full mechanical**: 30-50%

### Noise Levels
- NR 25-35 (natural mode)
- NR 30-40 (mechanical mode)

### Control Strategy
Complex BMS integration required. Typical changeover logic:
- External temp <16C or >26C → switch to mechanical
- CO2 >900 ppm and windows unable to ventilate → switch to mechanical
- Rain detected → close windows, switch to mechanical
- Wind speed >10 m/s → close windows, switch to mechanical
- External air quality (PM2.5 > threshold) → close windows, switch to mechanical

### Maintenance Access Requirements
Both natural ventilation components (actuators, louvres) and mechanical components (AHU filters, fans, dampers) require maintenance. Moderate complexity.

### Capital Cost Comparison
- Capital cost: 120-180 $/m² (more than natural, less than full mechanical)
- Annual maintenance: 5-10 $/m²/yr

### Operational Cost Comparison
- Annual energy cost: 5-10 $/m²/yr (30-50% less than full mechanical)

### Embodied Carbon
- System embodied carbon: 15-30 kgCO2e/m²

### Best-Fit Building Types
- Offices (progressive/sustainability-focused clients)
- Universities and libraries
- Civic and cultural buildings
- Schools (particularly post-Covid with emphasis on fresh air)

---

## 3. Fan Coil Units (FCU) + Fresh Air (DOAS)

### Operating Principle
Central AHU provides conditioned fresh air (ventilation only, 10-12 L/s per person). Individual ceiling-mounted fan coil units recirculate room air over heating/cooling coils connected to centralised CHW and LTHW circuits. 4-pipe system provides simultaneous heating and cooling capability in different zones.

### Spatial Requirements
- **Fresh air ductwork**: Main duct 400x300mm to 800x400mm; branch to each FCU 200x150mm flexible duct
- **CHW/LTHW pipework**: Mains 50-100mm dia.; branches to FCU 15-22mm dia.
- **FCU units**: 300x200x900mm to 400x300x1200mm (ceiling cassette); ceiling void must accommodate unit + connections
- **Plant rooms**: AHU room 2-3% of GFA; chiller room 1-2% of GFA; boiler room 0.3-0.8% of GFA
- **AHU dimensions**: 1.5x1.0x2.5m to 2.5x1.5x4.0m (serving 500-2000m² per unit)
- **Ceiling void**: 350-500mm
- **Riser shafts**: 0.5-0.8m² per floor (4 pipes + fresh air duct)

### Energy Performance
- **Total HVAC**: 80-120 kWh/m²/yr
- **Chiller COP**: 3.5-5.0 (air-cooled); 5.0-7.0 (water-cooled)
- **FCU fan power**: 30-80W per unit

### Noise Levels
- NR 35-40 (standard FCU — can be problematic in quiet spaces)
- NR 30-35 (low-noise FCU units — premium cost)
- Noise sources: FCU fan, water flow through coil, flexible duct breakout

### Control Strategy
Each FCU controlled independently by room thermostat or BMS zone controller. Typical: proportional control of CHW/LTHW valves; fan speed switching (high/medium/low). Central AHU controlled on CO2 or occupancy-based demand ventilation.

### Maintenance Access Requirements
- **FCU**: Filter change every 3-6 months; fan motor replacement every 5-10 years. Access panel (600x600mm) in ceiling per unit.
- **AHU**: Filter change quarterly; belt replacement annually; coil cleaning annually. Walk-in maintenance space required (minimum 800mm clearance on service side).
- **Chiller**: Annual service by specialist. Clear access for refrigerant recovery and compressor replacement.

### Capital Cost Comparison
- Capital cost: 180-280 $/m² (mid-range)
- Annual maintenance: 10-18 $/m²/yr (FCU filters + central plant)

### Operational Cost Comparison
- Annual energy cost: 12-20 $/m²/yr

### Embodied Carbon
- System embodied carbon: 25-45 kgCO2e/m²

### Best-Fit Building Types
- Hotels (individual room control essential)
- Residential apartments (with central plant)
- Commercial offices (especially multi-tenant)
- Hospitals (patient rooms)

---

## 4. Variable Air Volume (VAV)

### Operating Principle
Central AHU conditions and supplies air at constant temperature (typically 13C). VAV terminal boxes at each zone modulate the volume of supply air to match the zone's heating/cooling demand. At low load, airflow reduces to minimum ventilation rate. Reheat coils in VAV boxes provide heating when needed.

### Spatial Requirements
- **Supply ductwork**: Main duct 800x400mm to 1500x800mm; branch ducts 300x200mm to 600x300mm
- **Return air ductwork**: 70-80% of supply duct size (or ceiling plenum return)
- **VAV terminal boxes**: 300x400x800mm to 500x500x1200mm; one per 50-150m² zone
- **Plant rooms**: AHU room 3-5% of GFA (AHUs are large: 2.0x1.5x3.0m to 3.0x2.0x6.0m)
- **Ceiling void**: 500-800mm (large ducts are the primary consumer of ceiling void depth)
- **Riser shafts**: 1.0-2.0m² per floor (large supply and return ducts)
- **AHU dimensions**: 2.0x1.5x3.0m (small, serving 500m²) to 3.0x2.5x8.0m (large, serving 3000m²)

### Energy Performance
- **Total HVAC**: 90-140 kWh/m²/yr
- **Chiller COP**: 3.5-5.5
- **Fan energy**: Significant — variable speed drives essential (save 30-50% fan energy vs constant speed)
- **Reheat energy**: Can be significant in perimeter zones — heat recovery coils recommended

### Noise Levels
- NR 30-40 (well-designed, low duct velocities)
- NR 40-50 (poorly designed, high duct velocities)
- Critical design parameter: Main duct velocity <8 m/s; branch duct velocity <5 m/s; face velocity at diffuser <2.5 m/s

### Control Strategy
Central AHU: supply air temperature control (typically 13C constant or reset based on load). VAV boxes: airflow modulated by zone thermostat via actuated damper. Pressure-independent VAV boxes preferred (self-regulating regardless of system pressure changes).

### Maintenance Access Requirements
- **AHU**: Large walk-in plant room with 1.0m clearance all sides. Filter change quarterly. Coil cleaning annually.
- **VAV boxes**: Access panel in ceiling per box (600x600mm). Actuator/damper inspection annually.
- **Ductwork**: Cleaning access doors at 6-10m intervals in main ducts.

### Capital Cost Comparison
- Capital cost: 200-320 $/m² (higher due to large ductwork and AHU)
- Annual maintenance: 12-20 $/m²/yr

### Operational Cost Comparison
- Annual energy cost: 15-25 $/m²/yr (fan energy is significant)

### Embodied Carbon
- System embodied carbon: 30-55 kgCO2e/m² (large ductwork = more galvanised steel)

### Best-Fit Building Types
- Large open-plan offices (>2000m² per floor)
- Laboratories (high air-change rates: 6-15 ACH)
- Clean rooms (ISO Class 5-8)
- Trading floors
- Conference/event spaces with variable occupancy

---

## 5. Chilled Beams (Active)

### Operating Principle
Primary air from central AHU supplied at ceiling level through active chilled beam units. Primary air jet induces room air over a chilled water coil within the beam, providing cooling. Heating via warm water coil in the same beam or via a separate perimeter system (radiators, trench heaters).

### Spatial Requirements
- **Primary air ductwork**: 250x200mm to 500x300mm (ventilation air only — smaller than VAV)
- **CHW pipework**: Mains 40-80mm dia.; branches to beams 15-22mm dia.
- **Chilled beam units**: 300-600mm wide x 1200-3000mm long x 200-300mm deep
- **Plant rooms**: AHU room 2-3% of GFA; chiller room 1-1.5% of GFA
- **Ceiling void**: 300-450mm
- **Riser shafts**: 0.6-1.0m² per floor (CHW pipes + primary air duct)

### Energy Performance
- **Total HVAC**: 60-90 kWh/m²/yr
- **Chiller COP**: 4.0-6.0 (higher CHW temperature 14-16C allows more efficient chiller operation)
- **Fan energy**: Low — small AHU, primary air only
- **Pumping energy**: Moderate — CHW circuit to all beams

### Noise Levels
- NR 25-30 (very quiet — induction noise is minimal)
- Significantly quieter than FCU systems (no local fan)

### Control Strategy
CHW flow to each beam modulated by zone thermostat via 2-port valve. Primary air volume typically constant (ventilation rate). Condensation protection: CHW supply temperature controlled above dew point (typically 14-16C); dew point sensors on beam coils shut CHW valve if condensation detected.

### Maintenance Access Requirements
- Beam coils: Annual inspection and cleaning (dust accumulation reduces capacity by 15-30% over 5 years). Access from below via removable ceiling panels.
- AHU: Standard maintenance as per any AHU.
- No filters to change at beam level (unlike FCU).

### Capital Cost Comparison
- Capital cost: 220-340 $/m² (premium system — beams are expensive components)
- Annual maintenance: 8-14 $/m²/yr (low — no local fans or filters)

### Operational Cost Comparison
- Annual energy cost: 8-14 $/m²/yr (one of the lowest)

### Embodied Carbon
- System embodied carbon: 20-40 kgCO2e/m² (less ductwork, less equipment than VAV)

### Best-Fit Building Types
- Premium commercial offices
- Schools and universities
- Museums and galleries (quiet, stable conditions)
- Courthouses, libraries

---

## 6. Passive Chilled Beams

### Operating Principle
Chilled water coils mounted at ceiling level without primary air supply. Room air rises to ceiling by natural convection, passes over chilled coil, and descends as cooled air. Ventilation provided separately (openable windows, trickle vents, or small DOAS unit).

### Spatial Requirements
- **No ductwork** (ventilation separate)
- **CHW pipework**: Mains 40-80mm dia.; branches 15-22mm dia.
- **Beam units**: 300-600mm wide x 1200-2400mm long x 150-250mm deep
- **Ceiling void**: 200-350mm (beam + pipework only)
- **Plant rooms**: Chiller room 1-1.5% of GFA; small ventilation unit 0.5-1.0%

### Energy Performance
- **Total HVAC**: 50-75 kWh/m²/yr
- **Cooling capacity**: Limited — 40-80 W/m² (passive) vs 80-120 W/m² (active)

### Noise Levels
- NR 20-25 (silent — no moving parts at beam)

### Best-Fit Building Types
- Offices with natural ventilation strategy (supplementary cooling only)
- Residential (high-end, ceiling cooling)
- Heritage buildings (minimal visual impact)

---

## 7. Variable Refrigerant Flow (VRF/VRV)

### Operating Principle
Direct expansion refrigerant system. Outdoor condensing units on roof connect to multiple indoor fan coil units via small-diameter copper refrigerant pipes. 2-pipe heat pump systems provide heating or cooling (all zones same mode). 3-pipe heat recovery systems allow simultaneous heating and cooling in different zones by redistributing rejected heat.

### Spatial Requirements
- **No ductwork** for heating/cooling (refrigerant pipes replace water pipes and ductwork)
- **Refrigerant pipework**: Liquid line 6.35-15.88mm dia.; gas line 12.7-28.58mm dia. (much smaller than CHW pipes)
- **Indoor units**: Ceiling cassette 570x570x245mm (4-way); wall-mounted 800x290x225mm; ducted 700x300x800mm
- **Outdoor units**: 800x300x900mm to 1650x765x1985mm per system (grouped on roof or ground)
- **Ceiling void**: 250-350mm
- **Riser shafts**: 0.2-0.4m² per floor (refrigerant pipes only — very compact)
- **Plant rooms**: No AHU plant room required for heating/cooling (major saving)
- **Fresh air**: Separate DOAS or HRV unit required — 0.5-1.5% of GFA

### Energy Performance
- **Total HVAC**: 70-110 kWh/m²/yr
- **COP (cooling)**: 3.5-5.5 (at rated conditions)
- **COP (heating)**: 3.0-5.0 (heat pump mode; degrades below -5C ambient)
- **SEER**: 5.0-8.0 (seasonal efficiency, part-load dominant)

### Noise Levels
- NR 30-35 (indoor units — cassette type)
- NR 25-30 (indoor units — ducted type with acoustic flex duct)
- Outdoor units: 55-65 dBA at 1m (screen from noise-sensitive boundaries)

### Control Strategy
Individual indoor unit control via wired/wireless thermostat or central controller. Refrigerant flow modulated by electronic expansion valve at each unit. Central controller optimises compressor speed (inverter-driven) to match total system demand. 3-pipe systems redirect rejected heat from cooling zones to heating zones.

### Maintenance Access Requirements
- Indoor units: Filter cleaning monthly; fan motor/coil inspection annually. Ceiling access panel per unit.
- Outdoor units: Annual service (coil cleaning, refrigerant charge check). Clear access on all sides (300mm minimum).
- Refrigerant leak detection: Required by F-gas regulation. Sensors in mechanical ventilation return air or in occupied spaces.

### Capital Cost Comparison
- Capital cost: 160-260 $/m² (competitive, especially for retrofit)
- Annual maintenance: 8-15 $/m²/yr

### Operational Cost Comparison
- Annual energy cost: 10-18 $/m²/yr

### Embodied Carbon
- System embodied carbon: 20-40 kgCO2e/m²
- Refrigerant GWP: R410A (GWP 2088) being phased out; R32 (GWP 675) or R290 (GWP 3, propane) replacing

### Best-Fit Building Types
- Multi-zone offices (especially multi-tenant with individual metering)
- Retrofit projects (small pipes, no ductwork — suit existing buildings)
- Hotels (individual room control)
- Residential (with individual heat pump outdoor units or shared VRF)
- Mixed-use buildings (diverse thermal profiles)

---

## 8. Displacement Ventilation

### Operating Principle
Conditioned air supplied at low velocity (0.3-0.5 m/s) at floor level through swirl diffusers or low-wall grilles. Air temperature 18-20C (warmer than conventional supply). Warm plumes from occupants and equipment carry the air upward. Contaminants and heat rise to ceiling level where air is extracted. Creates stable thermal stratification.

### Spatial Requirements
- **Supply**: Through raised floor plenum (no ceiling supply ducts) — raised floor 250-400mm
- **Return ductwork at ceiling**: 400x300mm to 600x400mm
- **Floor diffusers**: Swirl type, 200-300mm diameter; one per 4-6m²
- **AHU plant room**: 2-3% of GFA
- **Ceiling void**: 200-300mm (return air ductwork and lighting only)
- **Total floor construction depth**: Increased by raised floor, but ceiling void reduced

### Energy Performance
- **Total HVAC**: 55-85 kWh/m²/yr
- **Energy saving vs overhead mixing**: 15-30% (higher supply temperature, less fan energy)
- **Supply air temperature**: 18-20C (vs 12-14C for mixing)
- **Cooling capacity**: Limited — 40-60 W/m² (suitable for standard office loads, not high-density)

### Noise Levels
- NR 25-30 (very quiet — low air velocities at diffuser)

### Best-Fit Building Types
- Auditoria, theatres, concert halls
- Open-plan offices with raised access floors
- Atriums and tall spaces
- Clean rooms (unidirectional flow variant)

---

## 9. Underfloor Air Distribution (UFAD)

### Operating Principle
Similar to displacement but with higher supply velocity and mixing at floor level. Conditioned air supplied through floor diffusers from a pressurised underfloor plenum. More cooling capacity than pure displacement. Occupants can control local diffusers for personal comfort.

### Spatial Requirements
- **Raised floor**: 300-450mm (pressurised plenum)
- **Floor diffusers**: Adjustable swirl type, one per 6-10m²; personal diffusers at workstations
- **Ceiling void**: 200-300mm (return air + lighting)
- **AHU plant room**: 2-3% of GFA
- **Underfloor fan-powered terminal boxes**: Optional, for perimeter zones

### Energy Performance
- **Total HVAC**: 60-90 kWh/m²/yr
- **Cooling capacity**: 60-100 W/m² (more than displacement, less than overhead VAV)
- **Fan energy**: Reduced — lower system pressure drop than overhead ducted systems

### Best-Fit Building Types
- Commercial offices with raised access floors
- Data centres (hot aisle/cold aisle cooling)
- Call centres and trading floors

---

## 10. Radiant Ceiling/Floor Systems

### Operating Principle
Heating and cooling delivered via water circulating through panels or pipes embedded in the ceiling or floor surface. Heat transfer by radiation (60%) and convection (40%). Nearly silent operation. Must be combined with DOAS for ventilation.

### Spatial Requirements
- **Radiant ceiling panels**: 15-25mm thick metal panels clipped to ceiling, or plasterboard with embedded capillary tubes
- **Embedded floor pipes**: 16-20mm dia. PEX pipes at 150-200mm centres in screed (40-65mm above pipes)
- **CHW/LTHW pipework**: Mains 40-80mm dia.
- **Ceiling void**: 100-200mm (radiant panels + pipework — minimal)
- **DOAS ventilation**: Separate ductwork for fresh air (200-400mm ceiling void for ventilation duct)

### Energy Performance
- **Total HVAC**: 45-70 kWh/m²/yr (paired with DOAS — one of the lowest)
- **Cooling capacity**: 40-80 W/m² (radiant ceiling); 25-40 W/m² (radiant floor cooling — limited by condensation)
- **Heating capacity**: 60-100 W/m² (radiant floor); 40-70 W/m² (radiant ceiling)
- **COP advantage**: High-temperature cooling water (16-18C) and low-temperature heating water (30-40C) enable heat pumps to operate at COP 5-8

### Noise Levels
- NR 20-25 (virtually silent — no moving parts)

### Best-Fit Building Types
- High-performance offices (LEED Platinum, BREEAM Outstanding targets)
- Residential (underfloor heating standard)
- Healthcare (infection control — no air movement)
- Museums and galleries (stable, quiet environment)

---

## 11. Ground Source Heat Pump (GSHP) Systems

### Operating Principle
Closed-loop pipe circuit buried in the ground (boreholes, horizontal trenches, or energy piles) extracts/rejects heat to/from the ground at stable temperature (10-14C in UK). Heat pump raises temperature for heating or lowers for cooling. Can provide simultaneous heating and cooling.

### Spatial Requirements
- **Boreholes**: 100-200m deep, 150mm dia., at 5-6m spacing. 1 borehole per 5-8 kW heating capacity.
- **Borehole field**: For a 5000m² office needing 250 kW heating: ~35-50 boreholes = 900-1800m² surface area during drilling (area can be landscaped/paved after installation)
- **Plant room**: 1.5-2.5% of GFA (heat pump units: 1.0x0.5x1.2m per 50 kW; buffer tanks; circulation pumps)
- **Energy piles**: Foundation piles fitted with heat exchange loops — no additional land required

### Energy Performance
- **COP (heating)**: 3.5-5.0 (ground source significantly better than air source in cold climates)
- **COP (cooling)**: 4.0-6.0 (passive cooling possible — direct ground exchange without compressor, COP >20)
- **Total HVAC**: 40-65 kWh/m²/yr

### Best-Fit Building Types
- Large commercial buildings with heating and cooling demand (balanced annual load)
- Schools, universities (heating-dominated with some cooling)
- Residential developments (shared loop systems)
- Any building targeting near-zero carbon operation

---

## 12. Air Source Heat Pump (ASHP) Systems

### Operating Principle
External air as heat source/sink. Refrigerant cycle extracts heat from outdoor air for heating (or rejects heat for cooling). Split systems (outdoor unit + indoor distribution) or monobloc (single outdoor unit with water distribution). Suitable for most building types and climates.

### Spatial Requirements
- **Outdoor units**: 900x350x800mm (residential) to 2200x900x1650mm (commercial) per 20-80 kW
- **Indoor distribution**: LTHW/CHW pipework to fan coils, radiators, underfloor heating, or AHU coils
- **Plant room**: 1.0-2.0% of GFA (heat pump, buffer tank, pumps)
- **Noise**: Outdoor unit noise 45-65 dBA at 1m — setback from boundaries and screening required

### Energy Performance
- **COP (heating)**: 2.8-4.5 (degrades significantly below -5C ambient)
- **COP (cooling)**: 3.0-5.0
- **SCOP (seasonal)**: 2.5-4.0
- **Total HVAC**: 50-80 kWh/m²/yr

### Best-Fit Building Types
- Residential (individual or communal ASHP replacing gas boilers)
- Small-medium commercial (offices, retail, schools)
- Retrofit (replacing gas boilers — electrification pathway)
- Any building targeting zero direct carbon emissions (no combustion on site)

---

## Comparative Summary Table

| System | Ceiling Void (mm) | Plant (% GFA) | Energy (kWh/m²/yr) | NR Rating | Capital ($/m²) | Maintenance ($/m²/yr) |
|---|---|---|---|---|---|---|
| Natural ventilation | 50-150 | 0.5-1.0 | 30-60 | 25-35 | 50-80 | 2-5 |
| Mixed-mode | 200-400 | 1.5-3.0 | 40-70 | 25-40 | 120-180 | 5-10 |
| FCU + fresh air | 350-500 | 3-5 | 80-120 | 35-40 | 180-280 | 10-18 |
| VAV | 500-800 | 4-7 | 90-140 | 30-50 | 200-320 | 12-20 |
| Active chilled beams | 300-450 | 3-4.5 | 60-90 | 25-30 | 220-340 | 8-14 |
| Passive chilled beams | 200-350 | 1.5-2.5 | 50-75 | 20-25 | 200-300 | 6-10 |
| VRF/VRV | 250-350 | 0.5-1.5 | 70-110 | 30-35 | 160-260 | 8-15 |
| Displacement ventilation | 200-300 | 2-3 | 55-85 | 25-30 | 180-280 | 8-14 |
| UFAD | 200-300 | 2-3 | 60-90 | 25-30 | 200-300 | 10-16 |
| Radiant + DOAS | 100-200 | 2-3 | 45-70 | 20-25 | 240-360 | 8-14 |
| GSHP system | varies | 1.5-2.5 | 40-65 | 25-30 | 280-400 | 6-12 |
| ASHP system | varies | 1.0-2.0 | 50-80 | 30-40 | 150-250 | 8-14 |
