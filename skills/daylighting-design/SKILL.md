---
name: daylighting-design
description: Natural daylighting strategies, solar geometry, glare control, artificial lighting integration, and visual comfort for architectural design
user-invocable: true
---

# Daylighting Design

Comprehensive knowledge base for natural daylighting strategies, solar geometry, shading device design, glare control, artificial lighting integration, and visual comfort optimization. Invoke this skill when addressing questions about window design, daylight simulation, shading calculations, lighting zones, circadian lighting, daylight metrics (sDA, ASE, UDI, DF), or any design decision involving natural light in buildings.

---

## Section 1: Daylight Metrics

### 1.1 Daylight Factor (DF)

The Daylight Factor is the ratio of internal illuminance at a point on the working plane to the simultaneous unobstructed external horizontal illuminance under a CIE overcast sky, expressed as a percentage.

**Formula:** DF (%) = (E_internal / E_external) × 100

**Components:**
- Sky Component (SC) — direct light from visible sky through the window
- Externally Reflected Component (ERC) — light reflected from external surfaces (ground, adjacent buildings)
- Internally Reflected Component (IRC) — light reflected from internal room surfaces (ceiling, walls, floor)

**Typical CIE overcast sky reference illuminance:** 10,000-15,000 lux (design value: 10,000 lux for conservative analysis)

**DF Targets by Space Type:**

| Space Type | Average DF Target | Minimum Point DF | Notes |
|---|---|---|---|
| Residential — living rooms | ≥ 2.0% | ≥ 0.5% | BS 8206-2, BS EN 17037 |
| Residential — bedrooms | ≥ 1.5% | ≥ 0.3% | Some codes accept ≥ 1.0% |
| Residential — kitchens | ≥ 2.0% | ≥ 0.6% | Task lighting critical |
| Office — open plan | ≥ 2.0% | ≥ 0.7% | 300 lux at desk level |
| Office — private/cellular | ≥ 1.5% | ≥ 0.5% | Window proximity advantage |
| Schools — classrooms | ≥ 2.0% | ≥ 0.7% | Uniformity ratio ≥ 0.3 |
| Schools — laboratories | ≥ 2.5% | ≥ 0.8% | High visual task demand |
| Hospitals — wards | ≥ 2.0% | ≥ 0.5% | Patient wellbeing critical |
| Hospitals — operating theatres | Artificial only | N/A | Controlled lighting required |
| Retail — general sales | ≥ 2.0% | ≥ 0.5% | Display lighting supplements |
| Libraries — reading areas | ≥ 2.5% | ≥ 0.8% | 500 lux on reading plane |
| Museums — galleries | 1.0-3.0% | Variable | UV control critical; max 200 lux for sensitive works |

**Uniformity:** Minimum-to-average DF ratio should be ≥ 0.3 (0.4 preferred). Values below 0.3 indicate excessive contrast between window-side and room-depth zones.

**Limitations of DF:** Assumes CIE overcast sky only; ignores building orientation, climate, direct sunlight, and temporal variation. Use Climate-Based Daylight Modelling (CBDM) for performance-based analysis.

### 1.2 Spatial Daylight Autonomy (sDA300/50%)

sDA measures the percentage of floor area that receives at least 300 lux from daylight alone for at least 50% of occupied hours annually.

**Standard:** IES LM-83-12 (Approved Method for Spatial Daylight Autonomy and Annual Sunlight Exposure)

**Calculation Method:**
1. Define analysis grid (typically 0.76 m / 30 in above floor, grid spacing ≤ 0.6 m)
2. Use annual climate-based simulation (hourly timestep, TMY weather data)
3. At each grid point, count hours where daylight illuminance ≥ 300 lux
4. Point passes if ≥ 50% of occupied hours meet threshold
5. sDA = percentage of passing grid points / total grid points

**Performance Targets:**
- sDA ≥ 55% — acceptable (LEED v4 Daylight credit Option 1: 2 points)
- sDA ≥ 75% — preferred (LEED v4 Daylight credit Option 1: 3 points)
- sDA ≥ 40% — minimum for EN 17037 Level I (Minimum)
- sDA ≥ 50% — EN 17037 Level II (Medium)
- sDA ≥ 65% — EN 17037 Level III (High)

**LEED v4.1 BD+C:** Daylight Credit EQ Credit — Demonstrate sDA300/50% ≥ 55% in ≥ 55% of regularly occupied floor area (2 points) or ≥ 75% of regularly occupied floor area (3 points), AND ASE1000,250 ≤ 10%.

### 1.3 Annual Sunlight Exposure (ASE1000,250)

ASE measures the percentage of floor area that receives at least 1,000 lux of direct sunlight for 250 or more occupied hours per year. It is a glare risk indicator.

**Threshold:** ASE1000,250 ≤ 10% of regularly occupied floor area

**Calculation:**
- Uses direct sun only (excludes diffuse sky)
- Same analysis grid as sDA
- Counts hours of ≥ 1,000 lux direct beam illuminance per point
- Point fails if ≥ 250 hours exceed threshold
- ASE = percentage of failing points

**Interpretation:**
- ASE ≤ 3% — excellent glare control
- ASE 3-7% — acceptable with operable shading
- ASE 7-10% — marginal; requires automated shading
- ASE > 10% — fails LEED; visual discomfort likely; redesign fenestration/shading

**Critical:** ASE can be reduced without harming sDA by adding external shading devices that block direct sun while admitting diffuse sky light.

### 1.4 Useful Daylight Illuminance (UDI)

UDI classifies daylight illuminance at each analysis point into four bins, evaluated hourly across the year.

**Bins:**
- UDI-f (fell-short): < 100 lux — insufficient daylight; electric lighting required
- UDI-s (supplementary): 100-300 lux — useful but may need supplementary electric light
- UDI-a (autonomous): 300-3,000 lux — ideal range; daylight sufficient, no glare risk
- UDI-e (exceeded): > 3,000 lux — potential glare and overheating risk

**Targets:**
- Maximize UDI-a (300-3,000 lux): aim for ≥ 50% of occupied hours at ≥ 50% of floor area
- Minimize UDI-e: aim for < 5% of occupied hours at perimeter zones
- UDI-f + UDI-s indicates electric lighting dependency

**Advantages over DF:** Climate-specific, accounts for orientation, captures both insufficient and excessive daylight conditions, annual temporal resolution.

### 1.5 Daylight Glare Probability (DGP)

DGP is a luminance-based metric predicting the probability of glare from a specific viewpoint. Calculated from high-dynamic-range (HDR) luminance maps using Evalglare (part of Radiance).

**Classification:**
- DGP < 0.35 (35%) — imperceptible glare (best practice target)
- DGP 0.35-0.40 — perceptible glare
- DGP 0.40-0.45 — disturbing glare
- DGP > 0.45 — intolerable glare

**Simplified DGP (DGPs):** Vertical eye illuminance-based approximation: DGPs = 6.22 × 10⁻⁵ × E_v + 0.184 (where E_v = vertical illuminance at eye in lux). Valid for DGP < 0.45.

### 1.6 Additional Metrics

- **Daylight Autonomy (DA):** Percentage of occupied hours a single point receives ≥ target illuminance from daylight. Point-based predecessor to sDA.
- **Continuous Daylight Autonomy (cDA):** Gives partial credit for values below threshold (e.g., 200 lux counts as 200/300 = 0.67 at 300 lux target).
- **Mean Daylight Factor:** Area-weighted average DF across analysis grid.
- **Vertical Illuminance (E_v):** Illuminance on a vertical plane at eye height; critical for circadian stimulus (target ≥ 250 melanopic lux at eye level during morning hours).
- **View Factor:** Solid angle of sky visible from a point; correlates strongly with DF.

---

## Section 2: Daylighting Strategies

### 2.1 Side-Lighting (Window Design)

The most common daylighting strategy. Daylight enters through vertical apertures in exterior walls.

**Key Parameters:**
- **Window Head Height (H_w):** Determines depth of daylight penetration. Effective daylit zone depth = 1.5× to 2.5× window head height. Rule of thumb: 2.0× H_w for side-lit rooms.
- **Window-to-Wall Ratio (WWR):** Total glazed area / gross exterior wall area. Typical ranges: 25-40% for energy-optimized designs; 40-60% for daylight-prioritized; > 60% requires high-performance glazing and shading.
- **Sill Height:** 0.8-1.0 m typical for view windows; lower sills (0.3-0.5 m) for seated occupants; higher sills (1.5-2.1 m) for clerestories.
- **Plan Depth Limit:** Maximum room depth for adequate side-lighting = 2.5 × H_w. Beyond this, DF drops below 1% and electric lighting becomes primary.

**WWR by Orientation (temperate climates, 40-55°N):**
- North: 30-50% WWR (diffuse light, low solar gain, minimal glare)
- South: 25-40% WWR (controllable with horizontal overhangs, high winter gain)
- East: 20-30% WWR (morning glare risk, difficult to shade)
- West: 15-25% WWR (afternoon glare and overheating, hardest orientation to shade)

**DF Improvement:** Each 10% increase in WWR adds approximately 0.5-1.0% to average DF (diminishing returns above 50% WWR due to room surface reflectance limits).

**Cost:** Standard window assemblies $300-800/m²; high-performance triple glazing $600-1,200/m².

**Best For:** All building types; universal applicability.

### 2.2 Top-Lighting

Light enters from roof-level apertures. Up to 3× more efficient than side-lighting per unit aperture area because light enters from directly overhead.

**Types:**

**Skylights:**
- Horizontal or slightly tilted (5-15° for drainage)
- Aperture area: 3-5% of floor area provides DF ≈ 2-4% below skylight
- Risk: overheating and excessive brightness directly below; use diffusing glazing or baffles
- Suitable glazing: translucent polycarbonate, opal glass, prismatic diffusers, aerogel-filled panels

**Monitor Roofs (Raised Clerestory):**
- Vertical or near-vertical glazing on raised roof section
- Can be oriented north for glare-free diffuse light
- Effective for deep-plan single-storey buildings (factories, galleries, studios)
- Depth of light throw: 1.0-1.5× monitor height

**Sawtooth Roofs:**
- Repeated asymmetric profiles with north-facing glazing (Southern Hemisphere: south-facing)
- Provides uniform illumination across large floor plates
- Optimal pitch: 30-45° for glazed face; 15-25° for opaque face
- DF achievable: 3-6% uniform
- Classic industrial typology; revived in modern schools and offices

**Light Wells:**
- Vertical shaft from roof to lower floors
- W:H ratio ≥ 1:3 for reasonable bottom illuminance (DF ≈ 0.5-1.0% at base)
- Reflective lining (white paint ρ ≥ 0.85, or mirrored surfaces ρ ≥ 0.92) essential
- Can combine with atrium for multi-storey distribution

**Cost:** Skylights $400-1,500/m²; monitor roofs +15-25% over standard roof; sawtooth +20-35%.

**Best For:** Single-storey buildings, top floors of multi-storey, galleries, industrial, retail.

### 2.3 Atrium Lighting

Atria serve as internal daylight distributors, bringing light into deep-plan multi-storey buildings.

**Design Parameters:**
- **Well Index (WI):** WI = H × (W + L) / (2 × W × L) where H = atrium height, W = width, L = length. Lower WI = more light at base.
- **Target:** WI ≤ 2.0 for DF ≥ 2% at ground floor; WI ≤ 1.5 for DF ≥ 3%
- **Aspect Ratio:** Width-to-height ratio ≥ 1:3 (minimum); 1:2 preferred; 1:1 ideal but area-expensive
- **Surface Reflectances:** Atrium walls ρ ≥ 0.6 (white: 0.7-0.85); floor ρ ≥ 0.3
- **Roof Glazing:** Clear or fritted glass; ETFE cushions; operable vents for ventilation

**Borrowed Light:** Rooms facing atrium receive side-light from atrium void. Glazed atrium-facing walls critical.

**Exemplars:** Ford Foundation HQ (Roche Dinkeloo), Bradbury Building (Wyman), National Gallery East Wing (Pei), Rijksmuseum atrium (Cruz y Ortiz).

**Cost:** Atrium construction premium +20-40% over equivalent solid floor area; long-term energy savings in lighting 30-50%.

### 2.4 Light Shelves

Horizontal reflective elements mounted at or near window mid-height, dividing the window into a lower view zone and an upper daylight zone.

**Design Rules:**
- Mount height: 2.0-2.4 m above floor (above eye level of seated occupants)
- Shelf depth (external): 0.6-1.2 m (effective throw into room = 1.5-2.0× external shelf depth)
- Shelf depth (internal): 0.3-0.8 m (secondary redistribution)
- Shelf surface: highly reflective (ρ ≥ 0.85); specular aluminum, white painted metal
- Upper glazing above shelf: clear or lightly tinted (maximize VLT)
- Lower glazing below shelf: can be tinted, fritted, or with blinds for glare control

**Performance:**
- Increases DF at room depth by 0.5-1.5%
- Improves uniformity ratio by 30-60%
- Reduces near-window DF excess by 10-20%
- Most effective on south-facing facades (Northern Hemisphere) within ±30° of due south
- Minimal effect on north-facing facades (diffuse sky, no direct beam to redirect)
- Reduced effectiveness at latitudes > 55° (low sun angles bypass shelf)

**Cost:** $200-600/linear meter installed.

**Best For:** Offices, schools, libraries — any space requiring uniform daylighting over depth.

### 2.5 Clerestory Windows

High-level glazing strips positioned above adjacent lower roof zones or above partitions. Bring light deep into floor plates without occupying wall area at eye level.

**Design Rules:**
- Head height: 3.0-5.0 m above floor for effective penetration
- Light throw: 1.5-2.5× clerestory head height
- Orientation: north-facing for diffuse light; south-facing with overhangs for controlled direct light
- Can combine with light shelves or reflective ceilings

**Performance:** DF improvement 1.0-2.5% in rear zone of room; excellent uniformity.

**Best For:** Churches, galleries, double-height spaces, stepped-section buildings.

### 2.6 Light Pipes and Tubular Daylighting Devices (TDDs)

Cylindrical or rectangular ducts that transport daylight from roof-level collector to interior spaces without direct facade access.

**Components:** Roof dome collector → highly reflective tube lining (ρ ≥ 0.98, 3M Silverlux or similar specular film) → ceiling diffuser.

**Performance:**
- Tube diameter: 250-600 mm residential; 600-1,200 mm commercial
- Effective tube length: up to 6 m for rigid tubes; up to 12 m with elbows (each 30° elbow loses ~10% flux)
- Delivers 200-600 lux at diffuser for 350 mm tube under clear sky
- DF equivalent: 0.5-1.5% over 5-8 m² floor area per tube

**Cost:** $500-2,000 per unit installed (residential); $1,500-5,000 (commercial).

**Best For:** Interior bathrooms, corridors, stairwells, storage areas needing code-compliant natural light.

### 2.7 Borrowed Light

Transmitting daylight from a well-lit space to an adjacent darker space through internal glazed partitions, transoms, fanlights, or glazed doors.

**Design Rules:**
- Internal glazing area: minimum 15-25% of partition area for meaningful contribution
- Glass type: clear float or acid-etched for privacy with light transmission
- Transom windows above doors: 300-600 mm high strips
- Sidelights flanking doors: 200-400 mm wide

**Performance:** Adds 0.3-1.0% DF to receiving space (dependent on source space illuminance).

**Best For:** Corridors, internal offices, hotel rooms facing corridors, school circulation spaces.

### 2.8 Light Wells and Courtyards

Vertical voids or open courtyards bringing daylight to lower floors of deep-plan buildings.

**Design Rules:**
- **Light well:** enclosed, often narrow (W:H ≥ 1:3 minimum for usable light at base)
- **Courtyard:** open, wider (W:H ≥ 1:2 for comfortable microclimate and good daylight)
- Bottom illuminance: for W:H = 1:2, expect DF ≈ 3-5% at courtyard floor; for W:H = 1:4, DF ≈ 0.5-1.5%
- White-painted walls increase base illuminance by 40-70% compared to brick

**Exemplars:** Islamic courtyard houses (Fez, Marrakech), Barcelona Eixample light wells, Louis Kahn's Salk Institute, Renzo Piano's Fondation Beyeler courtyard.

### 2.9 Reflective Ceilings and Splayed Reveals

**Reflective Ceilings:** White or metallic ceilings (ρ ≥ 0.8) redirect downward-reflected light from windows deeper into the room. Curved ceilings can focus light. Kahn's Kimbell Art Museum uses cycloid vaults to distribute reflected light uniformly.

**Splayed Reveals:** Window jambs angled outward at 15-30° to increase the apparent sky angle and admit more light. Increases SC by 5-15%. Traditional in thick-walled construction (600 mm+ masonry).

### 2.10 Automated Blinds and Dynamic Glazing

**Automated Blinds:**
- External roller blinds, venetian blinds, or fabric screens
- Sensor-driven: solar radiation, illuminance, occupancy
- Response time: < 60 seconds for motorized systems
- Most effective on east and west facades (rapidly changing sun position)

**Dynamic Glazing (Electrochromic):**
- Variable tint: VLT range 2-60% (e.g., SageGlass, View Smart Glass)
- Transition time: 7-20 minutes for full tint change
- Power consumption: < 5 W/m²
- Eliminates need for mechanical blinds
- Cost: $500-1,200/m² (2-3× static glazing)
- Reduces ASE to near-zero when fully tinted; maintains view connection

**Thermochromic Glazing:** Self-tinting at elevated temperatures (passive, no power). Limited VLT range. Emerging technology.

**Best For:** Premium offices, healthcare, curtain-wall facades, airports.

### 2.11 Prismatic Glazing and Daylight-Redirecting Films

Laser-cut panels, prismatic films, or micro-structured glazing that refract or redirect daylight upward toward the ceiling.

**Performance:** Redirects low-angle winter sun deep into room; blocks high-angle summer sun. Adds 0.5-1.5% DF at room depth. Can replace light shelves in retrofit applications.

### 2.12 Fiber-Optic Daylighting

Roof-mounted solar concentrators (parabolic dishes or Fresnel lenses) focus sunlight into fiber-optic cables that transport light to interior spaces.

**Performance:** Up to 50,000 lux at collector; delivery efficiency 50-70% over 10-15 m cable length; delivers 500-1,500 lux at endpoint luminaire. Niche application for high-value interior spaces (operating theaters, underground spaces).

### 2.13 Anidolic Systems

Compound parabolic concentrators (CPC) integrated into window assemblies that collect diffuse light from a wide sky angle and redirect it horizontally into the room depth.

**Performance:** 2-4× improvement in rear-zone illuminance compared to standard windows. Developed at EPFL, Lausanne. Effective at high latitudes (> 45°N) where low-angle diffuse light dominates.

### 2.14 Double-Skin Facades for Daylight

The cavity between inner and outer skins houses adjustable blinds or reflective louvers that redistribute light while managing thermal gains. Light can be reflected upward to ceiling for deeper penetration. Typical cavity depth: 0.3-1.2 m.

### 2.15 Translucent Insulation and Diffusing Materials

Translucent insulating materials (TIM), aerogel panels (light transmission 40-60%, U-value 0.5-0.7 W/m²K), channel glass (Profilit), polycarbonate multiwall sheets. Provide diffuse, glare-free light while maintaining thermal performance. Suitable for north facades, stairwells, gymnasiums.

---

## Section 3: Solar Geometry and Shading

### 3.1 Solar Position

The sun's position is defined by two angles:
- **Solar Altitude (α):** Angle above the horizon (0° at horizon, 90° at zenith)
- **Solar Azimuth (γ):** Angle along the horizon from due south (Northern Hemisphere convention: 0° = south, +90° = west, -90° = east)

**Key Solar Events:**
- Summer Solstice (June 21, Northern Hemisphere): maximum altitude, longest day
- Winter Solstice (December 21): minimum altitude, shortest day
- Equinoxes (March 21, September 21): sun rises due east, sets due west; altitude at solar noon = 90° - latitude

**Solar Noon Altitude by Latitude (Equinox):**

| Latitude | Equinox Noon Alt. | Summer Solstice Noon Alt. | Winter Solstice Noon Alt. |
|---|---|---|---|
| 0° (Equator) | 90.0° | 66.5° | 66.5° |
| 15° | 75.0° | 81.5° | 51.5° |
| 30° | 60.0° | 83.5° | 36.5° |
| 45° | 45.0° | 68.5° | 21.5° |
| 60° | 30.0° | 53.5° | 6.5° |

**Formula:** Solar altitude at noon = 90° - |latitude - solar declination|
Solar declination: +23.45° at summer solstice, -23.45° at winter solstice, 0° at equinoxes.

### 3.2 Shading Device Types

**Horizontal Overhangs:**
- Most effective for south-facing facades (Northern Hemisphere)
- Block high-angle summer sun while admitting low-angle winter sun
- Overhang depth formula: D = H × tan(90° - α_cutoff) where H = distance from overhang to window sill, α_cutoff = solar altitude to be blocked
- Simplified: D = H / tan(α_cutoff)
- Design for summer solstice noon altitude; verify at equinox for partial shading

**Vertical Fins:**
- Most effective for east- and west-facing facades
- Block low-angle oblique sun in morning (east) and afternoon (west)
- Fin spacing-to-depth ratio: S/D = tan(cutoff azimuth angle from facade normal)
- Angled fins (10-15° from perpendicular to facade) improve morning/afternoon performance

**Egg-Crate (Combined Horizontal + Vertical):**
- Effective for all orientations, especially southeast and southwest
- Higher material cost but superior performance
- Common in tropical and subtropical climates

**Brise-Soleil:**
- Array of horizontal or vertical blades, fixed or adjustable
- Blade angle, spacing, and depth determine shading coefficient
- Le Corbusier's signature element (Chandigarh, Marseille)

**External Venetian Blinds:**
- Adjustable horizontal slats on building exterior
- Most effective operable shading system (blocks 85-95% of solar gain when closed)
- Wind-rated to 65-100 km/h; auto-retract in high winds
- Prevalent in Central Europe (Germany, Austria, Switzerland)

**Perforated Screens and Mashrabiya:**
- Solid screen with patterned perforations; filters light and provides privacy
- Perforation ratio 20-50% (lower = more shading, less view)
- Traditional Islamic architecture; contemporary reinterpretation by Jean Nouvel (Louvre Abu Dhabi, Institut du Monde Arabe)
- Dynamic mashrabiya: motorized rotating elements responsive to sun position

### 3.3 Shading Design Rules

**Overhang Sizing by Latitude (south-facing, Northern Hemisphere):**

| Latitude | Summer Solstice Noon Alt. | Overhang Ratio (D/H) for Full Summer Shade |
|---|---|---|
| 25° | 88.5° | 0.03 |
| 30° | 83.5° | 0.11 |
| 35° | 78.5° | 0.20 |
| 40° | 73.5° | 0.30 |
| 45° | 68.5° | 0.39 |
| 50° | 63.5° | 0.50 |
| 55° | 58.5° | 0.61 |

**Shading Coefficient (SC):** Fraction of solar radiation transmitted through a fenestration system relative to a reference single clear glass pane (SC = 1.0). Modern systems target SC 0.2-0.5.

**Solar Heat Gain Coefficient (SHGC):** Total solar heat gain (transmitted + re-radiated inward) as fraction of incident radiation. SHGC = SC × 0.87. Typical targets: SHGC 0.25-0.40 for cooling-dominated climates; SHGC 0.40-0.60 for heating-dominated.

**Cutoff Angles:** The solar altitude angle at which an overhang fully shades the window below. Design for the altitude angle at the critical overheating date (typically August 1 in Northern Hemisphere, accounting for thermal lag after solstice).

---

## Section 4: Glare Control

### 4.1 Glare Sources in Buildings

- **Direct sun:** Highest luminance source (~1.6 × 10⁹ cd/m²); even 0.1% of sun disc in field of view causes severe glare
- **Bright sky:** Clear sky luminance 5,000-15,000 cd/m²; overcast sky 2,000-8,000 cd/m²
- **Specular reflections:** Sun reflected from glossy surfaces (polished floors, glass desktops, screens)
- **High-luminance surfaces:** Sunlit white walls (5,000-10,000 cd/m²), luminaires

### 4.2 Glare Metrics

**Daylight Glare Probability (DGP):** Primary metric. Calculated from HDR luminance images using Evalglare.

| DGP Range | Classification | Action Required |
|---|---|---|
| < 0.35 | Imperceptible | None — best practice target |
| 0.35-0.40 | Perceptible | Acceptable for most tasks |
| 0.40-0.45 | Disturbing | Shading or redesign needed |
| > 0.45 | Intolerable | Immediate intervention required |

**Daylight Glare Index (DGI):** Older metric (Hopkinson). DGI < 22 = acceptable for offices. Largely superseded by DGP.

**Unified Glare Rating (UGR):** For electric lighting glare only (not daylight). UGR < 19 for offices; UGR < 16 for detailed drafting.

**Luminance Ratios (recommended):**
- Task to immediate surround: ≤ 3:1
- Task to distant surround: ≤ 10:1
- Window to adjacent wall: ≤ 20:1 (preferably ≤ 10:1)
- Maximum luminance in field of view: ≤ 25,000 cd/m² for transient exposure

### 4.3 Glare Control Strategies

**Ranked by Effectiveness (best to worst):**

1. **External shading devices** — intercept solar radiation before it enters building. Most effective strategy. Reduces DGP by 0.20-0.35.
2. **Building orientation** — minimize east/west glazing; favor north/south. Free; must be decided at masterplan stage.
3. **Window position and size** — avoid placing windows directly in line with seated occupant's view direction. Set workstations perpendicular to windows.
4. **Glazing selection** — low VLT glazing, solar control coatings, fritted glass. Reduces DGP by 0.05-0.15.
5. **Light shelves and louvers** — redirect direct sun upward away from occupants' eyes.
6. **Interior blinds** — roller, venetian, vertical. Least effective for solar glare (heat already inside). Reduces DGP by 0.10-0.20 but can reduce useful daylight significantly.
7. **Screen placement in offices** — orient screens perpendicular to windows; use matte screen finishes.

**Screen Orientation Rule:** In side-lit offices, computer screens should face parallel to the window wall (user seated perpendicular to window). Never place screen facing a bright window (screen washout) or user facing window (direct glare behind screen).

---

## Section 5: Artificial Lighting Integration

### 5.1 Lighting Zones

Buildings are divided into daylight response zones for electric lighting control:

- **Perimeter Daylit Zone (Zone 1):** 0-4.5 m (0-15 ft) from window wall. High daylight availability; electric lighting can be dimmed or switched off 50-80% of occupied hours.
- **Transition Zone (Zone 2):** 4.5-7.5 m (15-25 ft) from window wall. Moderate daylight; electric lighting supplementation needed 40-60% of hours.
- **Core Zone (Zone 3):** > 7.5 m (> 25 ft) from window wall. Minimal daylight contribution; electric lighting provides primary illumination. Top-lighting can extend daylit zone into core.

### 5.2 Daylight-Linked Dimming (Photoelectric Controls)

**Types:**
- **Continuous dimming:** Smooth adjustment from 100% to 1-10% output. Most energy-efficient and occupant-preferred.
- **Stepped dimming:** Discrete levels (e.g., 100%, 66%, 33%, off). Lower cost but perceptible transitions.
- **Switching:** On/off based on daylight threshold. Least preferred by occupants.

**Sensor Types:**
- **Open-loop (external):** Rooftop photosensor measures outdoor illuminance; no feedback from internal conditions. Simple but less accurate.
- **Closed-loop (internal):** Ceiling-mounted photosensor measures work plane illuminance; adjusts electric light to maintain target. Self-correcting. Preferred for LEED compliance.

**Commissioning:** Sensors must be commissioned on-site. Calibrate to target illuminance (e.g., 300-500 lux on desk). Sensitivity and set-point adjustment critical. Common failure mode: poorly aimed sensors reading ceiling reflectance instead of task plane.

**Energy Savings:** Daylight-linked dimming in perimeter zones saves 40-60% of lighting energy. Payback: 2-5 years.

### 5.3 Circadian Lighting

Lighting that supports human circadian rhythms by varying spectrum and intensity throughout the day.

**Key Concepts:**
- **Melanopic Lux:** Weighted illuminance based on intrinsically photosensitive retinal ganglion cell (ipRGC) sensitivity (peak ~480 nm, blue-cyan). Defined by CIE S 026.
- **Melanopic/Photopic (M/P) Ratio:** Higher M/P ratio = more circadian stimulus per unit visual illuminance. Daylight M/P ≈ 1.0-1.1; warm white LED (2700K) M/P ≈ 0.45; cool white LED (6500K) M/P ≈ 0.9.

**Targets (WELL Building Standard v2):**
- ≥ 250 melanopic equivalent daylight illuminance (M-EDI) at eye level for ≥ 4 hours/day (between 9 AM and 1 PM)
- Occupied spaces: tunable CCT range 2700-6500K

**Tunable White LEDs:**
- Morning (7-10 AM): high CCT (5000-6500K), high intensity (300-500 lux at eye)
- Midday (10 AM-2 PM): medium-high CCT (4000-5000K)
- Afternoon (2-5 PM): medium CCT (3500-4000K)
- Evening (after 5 PM): low CCT (2700-3000K), reduced intensity (< 200 lux at eye)

### 5.4 Lighting Power Density (LPD) Targets

**ASHRAE 90.1-2019 (Building Area Method):**

| Space Type | LPD (W/m²) | LPD (W/ft²) |
|---|---|---|
| Office | 9.8 | 0.91 |
| Retail — general | 11.8 | 1.10 |
| Hospital/Healthcare | 9.7 | 0.90 |
| School/Classroom | 10.2 | 0.95 |
| Hotel/Motel — guest room | 7.5 | 0.70 |
| Warehouse | 6.1 | 0.57 |
| Manufacturing | 11.2 | 1.04 |
| Library | 10.6 | 0.99 |
| Museum | 10.1 | 0.94 |
| Religious building | 9.5 | 0.88 |
| Restaurant | 9.8 | 0.91 |
| Parking garage | 2.3 | 0.21 |

**Title 24 (California):** Generally 10-20% stricter than ASHRAE 90.1.

**Passive House / Ultra-low energy:** Target < 5.0 W/m² for all spaces using high-efficacy LED (> 130 lm/W).

### 5.5 Emergency Lighting

**Requirements (IBC, BS 5266, EN 1838):**
- Minimum illuminance: 1 lux along escape routes at floor level
- Open areas: 0.5 lux minimum
- High-risk task areas: 10% of normal illuminance or 15 lux (whichever is greater)
- Duration: 1-3 hours (building-dependent; 3 hours typical for assembly occupancies)
- Battery backup or generator-fed circuits
- Monthly functional test; annual full-duration test

---

## Section 6: Daylighting Design Process

### 6.1 Eight-Step Daylighting Design Workflow

**Step 1: Establish Performance Targets**
Define daylight metrics targets based on building type, certification goals, and occupant needs:
- Residential: DF targets per BS EN 17037 or local codes
- Office/LEED: sDA300/50% ≥ 55%, ASE1000,250 ≤ 10%
- BREEAM: HEA 01 Visual Comfort credit (daylight factor or CBDM route)
- WELL: Feature L03 Circadian Lighting Design (melanopic targets)

**Step 2: Orient Building and Fenestration**
- Elongate building on east-west axis (long facades face north and south)
- Minimize east and west glazing (hardest to shade, worst glare)
- Position primary occupied spaces on south facade (controlled solar access)
- Place service spaces (stairs, toilets, storage) on east/west or as buffer zones

**Step 3: Size Windows (WWR by Orientation)**
Use initial WWR estimates:
- South: 30-40% with horizontal shading
- North: 35-50% (no shading needed in Northern Hemisphere)
- East: 20-30% with vertical fins
- West: 15-25% with vertical fins or deep reveals
Adjust for plan depth, ceiling height, and internal reflectances.

**Step 4: Design Shading Devices**
- Calculate overhang depth from latitude and cutoff angle
- Select shading type per orientation (horizontal south, vertical east/west, egg-crate corners)
- Design for critical overheating date (not solstice — account for 4-6 week thermal lag)
- Integrate with facade architecture and maintenance access

**Step 5: Select Glazing**
Balance Visual Light Transmittance (VLT) and Solar Heat Gain Coefficient (SHGC):
- High VLT (> 0.65) for north facades
- Moderate VLT (0.45-0.65) with low SHGC (< 0.35) for south with shading
- Low VLT (0.30-0.45) for unshaded east/west (or use dynamic glazing)
- Double or triple glazing: U-value 1.0-1.6 W/m²K (double), 0.5-0.8 W/m²K (triple)

**Step 6: Simulate**
- **Tools:** Radiance (gold standard ray-tracer), Daysim (annual daylight), DIVA-for-Rhino, Ladybug/Honeybee (Grasshopper-based), ClimateStudio, Sefaira, Velux Daylight Visualizer
- **Method:** Climate-Based Daylight Modelling (CBDM) using TMY/EPW weather files
- **Grid:** Analysis points at work plane height (0.76 m office, 0.85 m residential), spacing ≤ 0.5 m
- **Output:** sDA, ASE, UDI, DF maps, DGP for critical viewpoints, annual illuminance profiles

**Step 7: Optimize**
Iterative refinement:
- Adjust WWR, glazing VLT, shading depth/angle
- Test alternative strategies (light shelves, reflective ceilings, light pipes)
- Balance sDA (increase) against ASE (decrease) — these often conflict
- Check glare (DGP) at critical viewpoints and times
- Verify uniformity across floor plate

**Step 8: Integrate Electric Lighting**
- Define daylight zones (perimeter, transition, core)
- Specify daylight-linked dimming controls per zone
- Size luminaires for supplementary operation (not full-output design)
- Calculate blended lighting energy use (daylit hours + electric hours)
- Specify circadian-appropriate CCT schedules

### 6.2 Common Design Errors

1. **Oversized windows without shading** — high sDA but ASE > 10%; glare complaints; overheating
2. **Deep plan reliance on side-lighting alone** — DF drops below 0.5% beyond 8 m from facade
3. **Dark interior finishes** — ceiling reflectance < 0.7 reduces IRC significantly; DF drops 20-40%
4. **Ignoring furniture and partitions** — post-occupancy daylight lower than simulation predicts
5. **North-only daylighting assumption** — possible only in narrow-plan buildings at temperate latitudes
6. **Confusing DF with sDA** — DF is sky-condition static; sDA is annual dynamic; cannot be compared directly
7. **Ignoring maintenance** — dirty glazing loses 10-30% VLT; external shading requires cleaning access
8. **Under-commissioning controls** — daylight sensors installed but never calibrated; lights run at full power despite available daylight

### 6.3 Recommended Surface Reflectances

| Surface | Minimum ρ | Recommended ρ | Notes |
|---|---|---|---|
| Ceiling | 0.70 | 0.80-0.90 | White paint or tiles |
| Walls (upper) | 0.50 | 0.60-0.80 | Light colors |
| Walls (lower/dado) | 0.30 | 0.40-0.60 | Slightly darker acceptable |
| Floor | 0.20 | 0.30-0.40 | Carpet 0.10-0.20 is problematic |
| Furniture (desks) | 0.30 | 0.40-0.50 | Matte finish to avoid veiling reflections |
| Window reveals | 0.60 | 0.70-0.85 | White splayed reveals best |
| External ground | 0.15 | 0.20-0.30 | Grass 0.20; concrete 0.25-0.35; snow 0.70 |

### 6.4 Glazing Selection Quick Reference

| Glazing Type | VLT | SHGC | U-value (W/m²K) | Application |
|---|---|---|---|---|
| Clear single | 0.87 | 0.86 | 5.8 | Heritage; mild climates only |
| Clear double (air) | 0.79 | 0.70 | 2.8 | Residential basic |
| Low-e double (argon) | 0.70 | 0.37 | 1.3 | Standard commercial |
| Low-e triple (argon) | 0.60 | 0.30 | 0.7 | Passive House |
| Low-e triple (krypton) | 0.62 | 0.28 | 0.5 | Ultra-low energy |
| Solar control double | 0.42 | 0.25 | 1.4 | Hot climates, west facades |
| Electrochromic (tinted) | 0.02-0.60 | 0.09-0.41 | 1.3-1.7 | Adaptive facades |
| Translucent aerogel | 0.40-0.60 | 0.30-0.45 | 0.5-0.7 | Diffuse light, high insulation |

---

## Section 7: Quick Reference — Daylighting Rules of Thumb

1. Effective side-lit daylit zone depth = 2.0 × window head height
2. Top-lighting aperture area = 3-5% of floor area for DF ≈ 2-4%
3. Minimum room surface reflectance: ceiling 0.80, walls 0.50, floor 0.20
4. WWR sweet spot for energy + daylight balance: 25-40%
5. Light shelf effective throw = 1.5-2.0 × external shelf depth
6. Overhang depth for full summer shade: D = H / tan(solar altitude at cutoff)
7. sDA and ASE are inversely correlated: optimize both simultaneously
8. Daylight-linked dimming saves 40-60% perimeter zone lighting energy
9. Every 10% increase in VLT adds ~5% to sDA (all else equal)
10. Dark floors (ρ < 0.2) reduce DF by 10-15% compared to light floors (ρ 0.3-0.4)
11. 1% DF ≈ 100 lux under 10,000 lux overcast sky
12. Courtyard W:H ≥ 1:2 for habitable daylight at base
13. Clerestory light throw = 1.5-2.5 × clerestory head height above work plane
14. Circadian stimulus requires ≥ 250 melanopic EDI at eye level for ≥ 4 hours/day
15. Light pipe loses ~10% flux per 30° bend
