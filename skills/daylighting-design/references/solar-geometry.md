# Solar Geometry — Deep Reference

Comprehensive reference on solar position calculation, sun path diagrams, shading mask construction, overhang and fin sizing, and shadow analysis methods for architectural design.

---

## 1. Fundamentals of Solar Position

### 1.1 Key Definitions

- **Solar Altitude (α_s):** Angle between the sun's center and the horizontal plane. Range: 0° (horizon) to 90° (zenith).
- **Solar Azimuth (γ_s):** Horizontal angle measured from due south (Northern Hemisphere convention). Positive = west of south; negative = east of south. Range: -180° to +180°.
- **Solar Zenith Angle (θ_z):** Complement of altitude. θ_z = 90° - α_s.
- **Solar Declination (δ):** Angle between the sun's rays and the equatorial plane. Range: -23.45° (winter solstice NH) to +23.45° (summer solstice NH).
- **Hour Angle (ω):** Angular displacement of the sun from solar noon. ω = 15° × (solar time - 12). Negative in morning, positive in afternoon.
- **Latitude (φ):** Geographic latitude of the site. Positive for Northern Hemisphere.

### 1.2 Solar Declination Calculation

**Cooper Equation (approximate):**
δ = 23.45° × sin(360° × (284 + n) / 365)
where n = day of year (January 1 = 1, December 31 = 365)

**Key Declination Values:**
| Date | Day (n) | Declination (δ) |
|---|---|---|
| March 21 (Vernal Equinox) | 80 | 0.0° |
| June 21 (Summer Solstice) | 172 | +23.45° |
| September 21 (Autumnal Equinox) | 264 | 0.0° |
| December 21 (Winter Solstice) | 355 | -23.45° |
| August 1 (Thermal peak) | 213 | +17.9° |
| February 1 | 32 | -17.1° |

### 1.3 Solar Altitude Calculation

**General Formula:**
sin(α_s) = sin(φ) × sin(δ) + cos(φ) × cos(δ) × cos(ω)

**At Solar Noon (ω = 0):**
α_noon = 90° - |φ - δ|

This simplifies to:
- Summer solstice noon: α = 90° - φ + 23.45°
- Winter solstice noon: α = 90° - φ - 23.45°
- Equinox noon: α = 90° - φ

### 1.4 Solar Azimuth Calculation

**General Formula:**
cos(γ_s) = [sin(α_s) × sin(φ) - sin(δ)] / [cos(α_s) × cos(φ)]

Sign convention: if ω < 0 (morning), γ_s is negative (east of south); if ω > 0 (afternoon), γ_s is positive (west of south).

**At Equinox:**
- Sunrise azimuth = -90° (due east)
- Sunset azimuth = +90° (due west)
- At all latitudes between Arctic and Antarctic circles

**At Summer Solstice (Northern Hemisphere):**
Sunrise azimuth = -arccos(-tan(φ) × tan(δ)) — northeast of east
Sunset azimuth = +arccos(-tan(φ) × tan(δ)) — northwest of west

### 1.5 Solar Time vs. Clock Time

**Solar Time:** Based on sun's actual position. Solar noon = sun at due south (NH).

**Conversion:**
Solar Time = Clock Time + Equation of Time (EOT) + Longitude Correction - Daylight Saving Offset

**Equation of Time (EOT):** Corrects for Earth's elliptical orbit and axial tilt.
EOT (minutes) = 9.87 × sin(2B) - 7.53 × cos(B) - 1.5 × sin(B)
where B = 360° × (n - 81) / 364

**EOT Key Values:**
| Date | EOT (minutes) |
|---|---|
| Feb 12 | -14.3 (clock ahead of sun) |
| May 15 | +3.8 |
| Jul 26 | -6.5 |
| Nov 3 | +16.4 (sun ahead of clock) |
| Apr 15 / Sep 1 | ~0 |

**Longitude Correction:**
4 minutes per degree of longitude difference from standard meridian.
Correction = 4 × (L_standard - L_local) minutes
where L_standard = time zone standard meridian (e.g., 0° for GMT, 75°W for EST)

**Example:** New York (74°W, EST standard meridian 75°W), June 21:
- Longitude correction = 4 × (75 - 74) = +4 minutes
- EOT ≈ -1.5 minutes
- Solar noon = 12:00 + 0:04 - 0:01.5 - 1:00 (DST) = 11:02:30 AM EDT

---

## 2. Sun Path Diagrams

### 2.1 Stereographic Sun Path Diagram

Projects the sun's path onto a horizontal plane using stereographic projection. The most common diagram type for architectural shading analysis.

**Reading the Diagram:**
- Concentric circles = altitude angles (outermost = 0°/horizon, center = 90°/zenith)
- Radial lines = azimuth angles (top = north, bottom = south for NH; reversed for SH)
- Curved lines (date lines) = sun paths for specific dates (typically monthly or solstice/equinox)
- Vertical hour lines = solar time hours

**Construction Method:**
1. Calculate solar altitude and azimuth for each hour of each representative date
2. Plot altitude as radial distance: r = R × cos(α) / (1 + sin(α)) for stereographic, or r = R × (90 - α) / 90 for equidistant
3. Plot azimuth as angular position from south
4. Connect points of same date for sun path curves
5. Connect points of same hour for hour lines

### 2.2 Equidistant Sun Path Diagram

Altitude mapped linearly (each degree = same radial distance). Simpler but less geometrically accurate than stereographic. Used in many educational and software tools.

### 2.3 Cylindrical Sun Path Diagram

Azimuth on horizontal axis (-180° to +180°), altitude on vertical axis (0° to 90°). Rectangular plot. Useful for reading shading mask overlays. Used in Ecotect, Climate Consultant.

---

## 3. Design Solar Angles for Major Latitudes

### 3.1 Equator (0° Latitude)

| Date | Noon Altitude | Sunrise/set Azimuth | Day Length |
|---|---|---|---|
| Equinox (Mar/Sep 21) | 90.0° | ±90° (E/W) | 12h 00m |
| June Solstice | 66.6° | ±23.5° N of E/W | 12h 00m |
| December Solstice | 66.6° | ±23.5° S of E/W | 12h 00m |

**Characteristics:** Sun passes directly overhead at equinoxes. Both solstices have equal (and lower) noon altitude. Sun is always high; horizontal shading on all facades. Nearly equal day length year-round.

### 3.2 Latitude 15° (Tropical — Mumbai, Mexico City, Dakar)

| Date | Noon Altitude | Sunrise/set Azimuth | Day Length |
|---|---|---|---|
| Equinox | 75.0° | ±90° | 12h 07m |
| June Solstice | 81.6° (sun slightly north) | ±113° | 13h 12m |
| December Solstice | 51.6° | ±67° | 10h 54m |

**Characteristics:** Sun passes overhead in May and July (declination = +15°). Very high summer altitude; moderate winter altitude. Dominant overheating period is March-October.

### 3.3 Latitude 30° (Subtropical — Cairo, Houston, Shanghai, New Delhi)

| Date | Noon Altitude | Sunrise/set Azimuth | Day Length |
|---|---|---|---|
| Equinox | 60.0° | ±90° | 12h 09m |
| June Solstice | 83.5° | ±119° | 14h 04m |
| December Solstice | 36.6° | ±61° | 10h 04m |

**Characteristics:** High summer sun enables effective horizontal overhangs on south facade. Low winter sun provides welcome solar gain. East/west facades problematic year-round. Significant seasonal variation in day length.

### 3.4 Latitude 45° (Temperate — Milan, Montreal, Sapporo, Christchurch)

| Date | Noon Altitude | Sunrise/set Azimuth | Day Length |
|---|---|---|---|
| Equinox | 45.0° | ±90° | 12h 12m |
| June Solstice | 68.5° | ±126° | 15h 37m |
| December Solstice | 21.6° | ±54° | 8h 46m |

**Characteristics:** Large altitude range (47°). South-facing overhangs moderately effective but must handle wide angle range. Low winter sun deeply penetrates interiors (beneficial for passive solar heating). Long summer days, short winter days. East/west shading critical in summer.

### 3.5 Latitude 60° (Subarctic — Helsinki, Anchorage, Oslo, St Petersburg)

| Date | Noon Altitude | Sunrise/set Azimuth | Day Length |
|---|---|---|---|
| Equinox | 30.0° | ±90° | 12h 17m |
| June Solstice | 53.5° | ±140° | 18h 52m |
| December Solstice | 6.6° | ±40° | 5h 33m |

**Characteristics:** Sun never rises high — maximum 53.5°. Winter sun barely clears horizon. Horizontal overhangs minimally effective (sun always at moderate-to-low angles). Vertical fins or combined shading needed. Maximizing daylight in winter is primary challenge. Very long summer days; nearly 19 hours of light at solstice.

---

## 4. Shading Device Design

### 4.1 Overhang Sizing Formula

For a horizontal overhang above a window:

**Required overhang depth (D):**
D = H_sill / tan(α_cutoff)

Where:
- H_sill = vertical distance from bottom of overhang to window sill
- α_cutoff = solar altitude angle at which full shading is desired

**Alternative formulation using window height:**
D = (H_overhang - H_sill_above_ground) / tan(α_cutoff)

**For partial shading (shade only upper portion):**
D = H_shade / tan(α_cutoff)
where H_shade = height of window portion to be shaded

### 4.2 Overhang Depth by Latitude — South-Facing Window (NH)

Design condition: full shading at summer solstice noon. Window height 1.8 m, overhang at window head.

| Latitude | Solstice Noon Alt. | Required D (m) | D/H Ratio |
|---|---|---|---|
| 20° | 86.6° | 0.11 | 0.06 |
| 25° | 88.5° | 0.05 | 0.03 |
| 30° | 83.5° | 0.20 | 0.11 |
| 35° | 78.5° | 0.36 | 0.20 |
| 40° | 73.5° | 0.54 | 0.30 |
| 45° | 68.5° | 0.71 | 0.39 |
| 50° | 63.5° | 0.89 | 0.50 |
| 55° | 58.5° | 1.10 | 0.61 |
| 60° | 53.5° | 1.33 | 0.74 |

**Note:** At latitudes 20-25°, the near-vertical sun requires minimal south-facing overhang, but east/west facades need deep protection. At latitudes > 50°, south-facing overhangs become very deep and may be impractical — combined strategies needed.

### 4.3 Overhang Sizing for Non-South Orientations

South-facing overhangs are effective because the sun is high when facing the facade. For east and west facades, the sun is low and oblique, making horizontal overhangs ineffective alone.

**East/West Facade Shading Strategy:**
- Vertical fins perpendicular to facade
- Fin depth D_fin = S × tan(θ_cutoff) where S = fin spacing, θ_cutoff = cutoff azimuth angle from facade normal
- Egg-crate (combined horizontal + vertical) for comprehensive protection
- Deep reveals or recessed windows (effective recess = 300-600 mm)

**Southeast/Southwest Facades:**
- Angled vertical fins (rotated 15-30° toward south)
- Combined horizontal overhang + angled vertical fins
- Exterior venetian blinds with automated angle adjustment

### 4.4 Shadow Length and Area Calculations

**Shadow Length of Vertical Object:**
L_shadow = H_object / tan(α_s)

Where L_shadow = length of shadow on horizontal ground, H_object = height of object, α_s = solar altitude.

**Shadow Direction:** Shadow falls directly opposite the solar azimuth (azimuth + 180°).

**Shadow of Horizontal Overhang on Vertical Wall:**
Vertical shadow drop below overhang = D × tan(α_profile)

Where:
α_profile = profile angle = arctan(tan(α_s) / cos(γ_wall))
γ_wall = azimuth angle between sun and wall normal

**Profile Angle:** The apparent solar altitude when viewed in the plane perpendicular to the wall surface. Critical for overhang design because it accounts for oblique sun angles.

### 4.5 Shading Coefficient Calculation

**Shading fraction (SF)** of a horizontal overhang on a vertical window at a given time:

If profile angle > cutoff angle: SF = 1.0 (fully shaded)
If profile angle < 0: SF = 0.0 (sun behind wall)
Otherwise: SF = D × tan(α_profile) / H_window

Where H_window = window height below overhang.

**Annual shading fraction:** Integrate hourly SF values over occupied hours weighted by incident solar radiation.

---

## 5. Shading Mask Construction

### 5.1 Purpose

A shading mask (or shadow angle protractor overlay) shows the angular range of sky blocked by a shading device when overlaid on a sun path diagram. If the sun path falls within the shaded region, the window is shaded at that time.

### 5.2 Horizontal Overhang Mask

A horizontal overhang produces a **segmental mask** — a curved band across the upper portion of the sun path diagram.

**Construction:**
1. Calculate the profile cutoff angle: β = arctan(H_sill / D_overhang)
2. On the sun path diagram, draw a horizontal line at altitude = β across the relevant azimuth range
3. The area above this line (higher altitudes) represents times when the window is shaded

**Width of mask:** Determined by the lateral extent of the overhang. If overhang extends infinitely, mask spans full azimuth range. If finite width, mask is bounded by azimuth angles defined by the overhang edges.

### 5.3 Vertical Fin Mask

Vertical fins produce a **radial mask** — wedge-shaped sectors emanating from the center.

**Construction:**
1. Calculate the horizontal cutoff angle: η = arctan(S_gap / D_fin)
   where S_gap = clear distance between fins, D_fin = fin depth
2. On sun path diagram, draw radial lines at azimuth = ±η from the facade normal
3. The area outside these radial lines (more oblique angles) represents shaded times

### 5.4 Egg-Crate Mask

Combination of segmental (overhang) and radial (fin) masks. The shaded region is the intersection of both.

### 5.5 Software Tools for Shading Analysis

- **Ladybug Tools (Grasshopper):** SunPath, ShadingMask, and SunlightHours components
- **Climate Consultant:** Built-in sun path with shading mask overlay
- **Ecotect (legacy):** Interactive shading mask generation
- **Sefaira:** Real-time facade shading analysis
- **Autodesk Revit:** Solar analysis and shadow studies
- **SketchUp + SunHours:** Shadow range animations
- **DIVA-for-Rhino:** Radiance-based shading analysis

---

## 6. Equinox and Solstice Analysis Methods

### 6.1 Shadow Study Protocol

Standard architectural shadow studies examine building massing and shading effects at critical dates and times.

**Standard Dates:**
1. **Winter Solstice (December 21 NH):** Longest shadows; worst-case for solar access to adjacent properties; critical for rights-to-light analysis
2. **Summer Solstice (June 21 NH):** Shortest shadows; worst-case for overheating; maximum solar altitude
3. **Equinoxes (March 21, September 21):** Intermediate condition; sun rises due east, sets due west; symmetric shadow pattern
4. **August 1:** Thermal peak date (4-6 weeks after solstice due to thermal lag); often more relevant than solstice for overheating design

**Standard Times:**
- 9 AM, 12 PM (noon), 3 PM solar time (minimum three-point analysis)
- Full hourly analysis from sunrise to sunset for detailed studies

### 6.2 Rights-to-Light and Solar Access

**UK Rights to Light (Waldram Diagram Method):**
- Statutory right under Prescription Act 1832 (20+ years of uninterrupted daylight)
- Test: ≥ 50% of room area must receive DF ≥ 0.2% (the "grumble line")
- Waldram diagram maps sky visibility from each point on the working plane
- Obstruction that reduces adequately lit area below 50% constitutes actionable nuisance

**Vertical Sky Component (VSC):**
- Percentage of unobstructed sky hemisphere visible from center of a window
- BRE Guide target: VSC ≥ 27% (equivalent to DF ≈ 2% at 1 m from window)
- New development should not reduce VSC of existing windows below 0.8 × former value

**Solar Access for Outdoor Spaces:**
- BRE Guide: at least 50% of amenity area should receive ≥ 2 hours of direct sunlight on March 21
- PAN (Scotland): living rooms should receive ≥ 3 hours of sunlight on equinox

### 6.3 Solar Envelope Method

Developed by Ralph Knowles (USC). Defines the maximum buildable volume on a site that will not overshadow adjacent properties beyond specified limits.

**Construction:**
1. Define solar access criteria (e.g., 4 hours of direct sun on adjacent facades on winter solstice)
2. Calculate shadow lengths and directions at the critical times
3. Draw inward from site boundaries using shadow angles as cutting planes
4. The resulting volumetric "envelope" is the maximum development form

**Applications:** Zoning regulations in solar-access-protected districts; passive solar community design; daylighting master plans.

### 6.4 Heliodon and Digital Shadow Studies

**Physical Heliodon:** Adjustable light source + tilting table that simulates sun position for any latitude, date, and time on architectural models. Used for qualitative light quality assessment.

**Digital Tools:**
- Revit/SketchUp shadow animation (date/time slider)
- Ladybug SunPath + Radiation analysis (quantitative)
- Grasshopper + Radiance (high-accuracy)
- Solar access maps (cumulative hours of direct sun per point on ground/facades)

---

## 7. Advanced Solar Geometry Applications

### 7.1 Facade Orientation Optimization

**Annual Solar Radiation by Orientation (latitude 45°N, kWh/m²/year):**

| Orientation | Total Radiation | Direct (Beam) | Diffuse |
|---|---|---|---|
| Horizontal (roof) | 1,250 | 780 | 470 |
| South (vertical) | 880 | 590 | 290 |
| East (vertical) | 640 | 370 | 270 |
| West (vertical) | 640 | 370 | 270 |
| North (vertical) | 360 | 70 | 290 |
| South tilted 45° | 1,180 | 810 | 370 |

**Optimal Building Orientation:** Long axis within ±15° of east-west for maximum south-facing area and minimum east/west exposure. Deviation up to ±30° acceptable with 5-10% performance loss.

### 7.2 Passive Solar Heating Window Sizing

**South-facing glass area for passive solar heating (latitude 45°N):**
- Net solar gain per m² of south glazing: 200-350 kWh/year (double low-e, argon)
- Heat loss per m² of south glazing: 80-150 kWh/year (depending on U-value and climate)
- Net benefit: 100-250 kWh/m²/year
- Optimal south glazing: 25-50% of south wall area (diminishing returns above 40% due to overheating risk)

### 7.3 Photovoltaic Panel Orientation

**Optimal tilt angle for annual maximum yield:** Approximately equal to latitude (±5°) for fixed panels.
- Latitude 30°: optimal tilt 25-35°
- Latitude 45°: optimal tilt 35-45°
- Latitude 60°: optimal tilt 50-60°

**Azimuth:** Due south (NH) or due north (SH). Deviation ±30° loses < 5% annual yield. East/west-facing vertical panels useful for morning/evening peak demand alignment.

### 7.4 Sundial and Shadow Clock Principles

Solar time can be read from shadow position:
- **Hour angle to time:** Each 15° of hour angle = 1 hour. Shadow rotates clockwise (NH) at 15°/hour.
- **Analemma:** Figure-8 pattern traced by sun at same clock time over the year; caused by combined effects of orbital eccentricity and axial tilt.
- **Architectural sundials:** Can be integrated into building facades and ground planes as functional art (e.g., sundial gardens, gnomon walls).

---

## 8. Quick Reference Formulas

| Parameter | Formula |
|---|---|
| Solar declination | δ = 23.45° × sin(360° × (284+n)/365) |
| Solar altitude (general) | sin(α) = sin(φ)sin(δ) + cos(φ)cos(δ)cos(ω) |
| Solar altitude at noon | α_noon = 90° - \|φ - δ\| |
| Hour angle | ω = 15° × (solar time - 12) |
| Solar azimuth | cos(γ) = [sin(α)sin(φ) - sin(δ)] / [cos(α)cos(φ)] |
| Overhang depth | D = H / tan(α_cutoff) |
| Shadow length | L = H / tan(α_s) |
| Profile angle | α_profile = arctan[tan(α_s) / cos(γ_wall)] |
| Equation of Time | EOT = 9.87sin(2B) - 7.53cos(B) - 1.5sin(B) |
| Day length (hours) | DL = (2/15) × arccos[-tan(φ) × tan(δ)] |
| Sunrise/set hour angle | ω_s = ±arccos[-tan(φ) × tan(δ)] |
| Sunrise/set azimuth | γ_s = ±arccos[sin(δ)/cos(φ)] (at equinox: ±90°) |
| Solar time correction | Solar time = clock time + EOT + 4(L_std - L_loc) - DST |
