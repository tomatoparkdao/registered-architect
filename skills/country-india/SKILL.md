---
name: country-india
description: >
  India-specific architectural code and regulatory reference. Covers the National Building Code
  of India (NBC 2016), Energy Conservation Building Code (ECBC 2017) and ECBC for Residential
  Buildings (ECBC-R 2018, also called Eco-Niwas Samhita), Indian Standards for structural
  design (IS 456:2000 concrete, IS 800:2007 steel, IS 875 Parts 1-5 loads, IS 1893:2016 seismic,
  IS 13920:2016 ductile detailing, IS 1904 foundations), the Rights of Persons with Disabilities
  Act 2016 and Harmonised Guidelines & Space Standards for Universal Accessibility 2021 (MoHUA),
  state-level Development Control Regulations (Mumbai DCPR 2034, Delhi MPD 2041, Bangalore BBMP,
  Chennai CMDA, Hyderabad GHMC, Kolkata KMC, Pune PMC, Ahmedabad AUDA), municipal building
  bye-laws, GRIHA and IGBC green rating systems, RERA (Real Estate Regulatory Authority) under
  the RERA Act 2016, fire safety per NBC Part 4 and state fire services rules, and the
  approval workflow involving Municipal Corporations, Development Authorities, State Fire
  Services NOC, and aviation/environmental clearances. Practitioner-grade clause-level
  reference for design teams working on projects in any Indian state or Union Territory.
---

# Country: India

Architectural code and regulatory reference for projects located in any Indian state or Union Territory. Activate this skill whenever the project location is in India, when an Indian city is referenced, when Indian rupee currency or area-units like "square feet built-up" / "carpet area" / "lakh" / "crore" appear, or when codes like NBC, ECBC, or IS series are mentioned.

---

## 1. Regulatory Hierarchy

India operates as **Archetype B (National Model + State Adoption)**, with significant deviation between national framework and state/municipal enforcement.

### 1.1 Authority Stack

```
LEVEL 1 -- NATIONAL FRAMEWORK (advisory, except where state has adopted)
  - Bureau of Indian Standards (BIS) -- publishes NBC 2016 + IS codes
  - Ministry of Housing and Urban Affairs (MoHUA) -- urban policy
  - Bureau of Energy Efficiency (BEE) -- ECBC 2017, ECBC-R 2018
  - Ministry of Environment, Forest and Climate Change (MoEFCC) -- EIA notifications
  - National Disaster Management Authority (NDMA) -- guidelines
  - Directorate General of Civil Aviation (DGCA) -- height NOC near aerodromes

LEVEL 2 -- STATE FRAMEWORK (legally binding)
  - State Town & Country Planning Department -- planning laws
  - State Fire Services -- Fire NOC, periodic renewal
  - State Pollution Control Board -- Consent to Establish/Operate
  - State Electricity Regulatory Commission -- electrical sanction

LEVEL 3 -- LOCAL FRAMEWORK (legally binding, project-specific)
  - Municipal Corporation OR Development Authority -- Building Permit
    + MCGM (Greater Mumbai), MCD (Delhi), BBMP (Bangalore), GCC (Chennai),
      GHMC (Hyderabad), KMC (Kolkata), PMC (Pune), AMC (Ahmedabad),
      MCC (Chandigarh), etc.
    + MMRDA, DDA, BDA, CMDA, HMDA, KMDA -- jurisdictional Development Authorities
  - District Magistrate / Collector -- land use, NA conversion
  - Local Fire Services -- on-site NOC

LEVEL 4 -- PROJECT-SPECIFIC CLEARANCES
  - EC (Environmental Clearance) for >20,000 sqm built-up (EIA 2006 + amendments)
  - Aviation NOC if within 20-km of aerodrome reference point
  - Heritage NOC if within heritage precinct (ASI/SHA)
  - Coastal Regulation Zone (CRZ) clearance per CRZ 2019
  - Forest clearance if on forest land
  - Defence/Army NOC if within designated zones
  - RERA registration if >500 sqm or >8 apartments (RERA Act 2016)
```

### 1.2 NBC 2016 Status

The **National Building Code of India 2016** (NBC 2016, BIS SP 7:2016, two volumes, ~3,500 pages) is *advisory* at the national level. It becomes binding only when:

- A state government formally adopts it (most have, fully or partially)
- A municipal corporation references it in its Building Bye-Laws (most major cities do)
- A specific clause is cited in a court order or RERA ruling

NBC 2016 is organized in **12 Parts** (P1 to P12), with several Parts subdivided into Sections:

| Part | Title | Content |
|---|---|---|
| Part 1 | Definitions | Glossary, references |
| Part 2 | Administration | Permit process, sanctioning authority duties |
| Part 3 | Development Control Rules + General Building Requirements | Setbacks, FAR, open spaces, common requirements |
| Part 4 | Fire and Life Safety | Compartmentation, exits, fire ratings, sprinklers (the most-cited Part) |
| Part 5 | Building Materials | IS-spec material requirements |
| Part 6 | Structural Design | Section 1 Loads; 2 Soils & Foundations; 3 Timber; 4 Masonry; 5 Concrete; 6 Steel; 7 Prefab; 8 Glass |
| Part 7 | Construction Management, Practices and Safety | Site safety, scaffolding, demolition |
| Part 8 | Building Services | Section 1 Lighting; 2 Electrical; 3 Air-conditioning; 4 Acoustics; 5 Plumbing/Drainage; 6 Lifts/Escalators |
| Part 9 | Plumbing Services | Section 1 Water Supply; 2 Drainage; 3 Solid Waste; 4 Gas Supply |
| Part 10 | Landscape, Signs and Outdoor Display | Streetscape requirements |
| Part 11 | Approach to Sustainability | NBC's sustainability framework (predates GRIHA mandate) |
| Part 12 | Asset and Facility Management | Operations & maintenance |

### 1.3 Code Adoption Status by State

| State / UT | NBC 2016 Adoption | ECBC 2017 Mandated | Notes |
|---|---|---|---|
| Maharashtra | Full (UDCPR 2020) | Yes, since 2018 | Mumbai uses MCGM DCPR 2034; rest of state uses Unified DCPR 2020 |
| Delhi NCT | Full via MPD 2041 + Building Bye-Laws 2016 | Yes, since 2017 | DDA/MCD apply NBC + DUAC review for heritage areas |
| Karnataka | Full via KMBBL 2003 (updated) | Yes, since 2018 | Bangalore zoning regs under BDA + BBMP bye-laws |
| Tamil Nadu | Full via TNCDBR 2019 | Yes, since 2018 | Chennai under CMDA Master Plan-II + TN Combined DCR & Building Rules 2019 |
| Telangana | Full via GO 168/2012 + updates | Yes, since 2017 | HMDA / GHMC bye-laws + 2020 amendments |
| Andhra Pradesh | Full via APBBR 2017 + 2020 amendments | Yes | APCRDA for Amaravati / VMRDA Vizag |
| West Bengal | Full via KMC Building Rules 2009 + amendments | Yes, since 2019 | Kolkata under KMC + KMDA; rest of state under state PWD rules |
| Gujarat | Full via GDCR 2017 (Comprehensive General Development Control Regulations) | Yes, since 2018 | Ahmedabad AUDA, Surat SUDA, Vadodara VUDA |
| Rajasthan | Full via Rajasthan Building Bye-Laws 2020 | Yes | JDA for Jaipur, AUIT for Ajmer, JODA for Jodhpur |
| Uttar Pradesh | Full via UPABBR 2008 + amendments | Yes, since 2018 | Lucknow LDA, NOIDA, Greater NOIDA Authorities |
| Kerala | Full via KMBR/KPBR 2019 (revised 2024) | Yes, since 2019 | Local Self Government Department supervises |
| Punjab | Full via PMBBR 2018 | Yes | Each Municipal Corporation has variation |
| Haryana | Full via HBC 2017 + 2019 amendments | Yes, since 2017 | HUDA / HSVP for new sectors, GMDA for Gurugram |
| Madhya Pradesh | Full via MPBBL 2012 + amendments | Yes | TPS schemes prevail in larger cities |
| Bihar | Partial; State Building Bye-Laws 2014 | Partial (large commercial only) | BMC Patna; older infrastructure |
| Odisha | Full via OBBL 2018 | Yes, since 2019 | BDA Bhubaneswar, CDA Cuttack |
| Assam | Partial; ABBL 2014 | Limited | GMDA Guwahati; northeastern states often follow Assam by reference |
| All NE States | Variable; most defer to NBC + Assam pattern | Limited | Variable adoption |
| Jammu & Kashmir | Reorganised 2019; JK Building Bye-Laws under revision | -- | UT administration; J&K Master Plan 2035 in force |
| Chandigarh UT | Chandigarh Building Rules (Urban) 2017 | Yes | Le Corbusier zoning preserved |
| Goa | GTCP Act 1974 + Regulations 2010 + 2020 amendments | Partial | Coastal restrictions paramount |

When advising on a specific project, always confirm: (i) which state, (ii) which city's Municipal Corporation or Development Authority, (iii) date of pending Building Permit application (as code version in force depends on application date).

---

## 2. Building Code Core Requirements (NBC 2016 Part 3 + Part 4)

### 2.1 Occupancy Classification (NBC 2016 Part 4, 3.1)

NBC defines **9 Occupancy Groups (A through I)**:

| Group | Occupancy | Subdivisions | Examples |
|---|---|---|---|
| **A** | Residential | A-1 Lodging; A-2 One-family/Two-family; A-3 Dormitories; A-4 Apartment houses; A-5 Hotels; A-6 Starred Hotels | Apartments, hostels, hotels |
| **B** | Educational | B-1 Schools up to senior secondary; B-2 All others (colleges, universities) | Schools, colleges |
| **C** | Institutional | C-1 Hospitals/sanatoria; C-2 Custodial institutions; C-3 Penal institutions | Hospitals, jails, orphanages |
| **D** | Assembly | D-1 (>1000 persons); D-2 (>300, <=1000); D-3 (>100, <=300); D-4 (<=100); D-5 Outdoor assembly; D-6 Cinemas/theatres; D-7 Stadia | Theatres, halls, marriage halls |
| **E** | Business | E-1 Offices; E-2 Laboratories; E-3 Research; E-4 Tele-call centres | Offices, IT parks |
| **F** | Mercantile | F-1 Retail (small); F-2 Wholesale; F-3 Super markets/Department stores | Shops, malls |
| **G** | Industrial | G-1 Low hazard; G-2 Moderate; G-3 High hazard | Factories, mills |
| **H** | Storage | H-1 (low); H-2 (moderate) | Warehouses |
| **I** | Hazardous | (specially regulated) | Chemical plants, magazines, oil/gas |

### 2.2 Height & Area Limits

NBC 2016 has **no single height-vs-construction-type table** equivalent to IBC Table 504; instead, height/area limits are embedded in Part 4 (Fire), Part 3 (Development), and state DCRs.

**Critical thresholds:**

| Threshold | Trigger | Source |
|---|---|---|
| **High-Rise Building** | >= 15 m height (residential, hotel) OR >= 18 m (other occupancies) -- from average ground level | NBC 2016 Part 4, 3.1.40 |
| **Special Building** | Group D-1/D-2/D-6 (assembly), Group E factories with hazardous material, Group H, hotels with floor area >500 sqm + height >9 m, hospitals >9 m, schools >9 m, basement >300 sqm | NBC 2016 Part 4, 3.1.84 |
| **EIA Threshold** | >20,000 sqm built-up area (per EIA Notification 2006 + 2014 amendment + January 2020 amendment) -- Category B2 with State EIA Authority; >150,000 sqm or specific industries -- Category A with national MoEFCC | EIA Notification 2006 (and amendments) |
| **Fire NOC Required** | All high-rise buildings, special buildings, hospitals, hotels with >= 20 rooms; some states require below these thresholds too | NBC 2016 Part 4 + state Fire Services rules |
| **RERA Registration** | Project on >500 sqm OR >8 apartments | RERA Act 2016 Sec. 3 |
| **Aviation NOC** | Buildings within 20 km of aerodrome reference point (varies by airport classification) | DGCA NOCAS 2.0 portal; per aircraft operator restrictions |

### 2.3 Setback & FAR (Indicative -- state DCR governs)

FAR (Floor Area Ratio) in India is computed differently across states. Some include balconies/lifts, others exclude. *Always confirm with the local DCR.*

| City | Typical Residential FAR | Typical Commercial FAR | Notes |
|---|---|---|---|
| **Mumbai (MCGM DCPR 2034)** | Base 1.33, Permissible 3.0 (with premium FSI + TDR), up to 5.0 in TOD | Base 1.33, up to 5.0 with premium | Distinction: "Built-up FSI" vs "Composite FSI"; transit-oriented zones higher |
| **Delhi (MPD 2041 + Unified Building Bye-Laws 2016)** | 200-350% (varies by plot size); up to 400% mixed-use | 200-450% | "FAR" used, includes mezzanine; balconies excluded if <=10% |
| **Bangalore (BBMP Bye-Laws 2003)** | 1.75 (up to 3.25 for big plots), TDR-augmented | 1.75-3.25 | RMP 2031 increased FAR with road width |
| **Chennai (CMDA Second Master Plan)** | 1.5-2.0 (special buildings up to 2.5) | 2.0-3.5 | Premium FSI 50% extra on payment |
| **Hyderabad (GO 168 + GHMC)** | Unlimited (subject to setback + height + insurance), within Master Plan | Unlimited subject to same | Insurance premium based on height |
| **Kolkata (KMC Building Rules 2009)** | Varies by ward; 1.5-3.5 | 2.0-4.0 | "FAR" computed on plot area + 25% road area |
| **Pune (Maharashtra UDCPR 2020)** | 1.1-2.5 base, premium up to 3.5 | Same | Aligned with MCGM concept of permissible vs base |
| **Ahmedabad (Gujarat GDCR 2017)** | Up to 2.7 (RC), 4.0 (CBD) | Up to 5.0 in CBD/TOD | Aligned with state CGDCR |
| **Gurugram (HBC 2017)** | 1.45-1.75 (varies by zone) | 1.75-3.5 | Floor-Area-Ratio + ground coverage limits |
| **NOIDA (UP)** | 2.75-3.5 (group housing) | 4.0 (mixed-use) | NOIDA Building Regulations 2010 + amendments |

Indian DCRs typically also limit:
- **Ground Coverage** (separate from FAR): often 25-50% residential, 50-60% commercial
- **Setbacks**: front 3-12 m, side 3-6 m, rear 3-6 m (depends on plot size + abutting road)
- **Height**: implicit via FAR + setback + ground coverage interaction; explicit only for special zones (heritage, aviation, defence)
- **Parking**: 1.0-2.0 cars per dwelling (city-dependent); commercial = 1 per 50-100 sqm GFA; ECS = Equivalent Car Space

---

## 3. Fire Safety (NBC 2016 Part 4 + IS 15683)

### 3.1 Travel Distances

**NBC 2016 Part 4 Table 7:**

| Occupancy | Without Sprinkler (m) | With Sprinkler (m) |
|---|---|---|
| Group A Residential | 22.5 | 30.0 |
| Group B Educational | 22.5 | 30.0 |
| Group C Institutional | 22.5 (limited single-storey) | 30.0 |
| Group D Assembly | 22.5 (max with smoke detection) | 30.0 |
| Group E Business | 30.0 | 45.0 |
| Group F Mercantile | 22.5 | 37.5 |
| Group G Industrial | varies by hazard | varies |
| Group H Storage | varies | varies |
| Group I Hazardous | 18.0 | 22.5 |

(Cross-reference: IBC 2024 allows 76.2 m for sprinklered business. India is significantly more restrictive.)

### 3.2 Means of Egress -- Stair Capacity (NBC 2016 Part 4, 4.4)

- **Minimum stair width** -- High-rise residential 1.5 m; Hospital 2.0 m; Educational 2.0 m for assembly capacity >300; Business 1.5 m
- **Minimum exit door width** -- 1.0 m (residential), 1.5 m (institutional/assembly main exit), 2.0 m (large assembly)
- **Maximum dead-end corridor** -- 6.0 m (most occupancies), 4.5 m for institutional (Group C)
- **Capacity factor** -- Stair: 60 persons per unit (one unit width = 500 mm); Doors: 75 persons per unit. So 1.5 m stair = 3 units = 180 persons; 1.0 m door = 2 units = 150 persons.
- **Refuge area** -- Mandatory on every floor for high-rise residential (Group A) of height >= 24 m; calculated as 0.3 sqm per occupant of upper floors served; located adjacent to fire-escape stair, accessed via 2-hour fire-rated lobby. (Critical: this is a Mumbai/Delhi enforcement priority.)

### 3.3 Fire Compartmentation

**NBC 2016 Part 4 Table 22:**

| Building Type / Height | Required Fire Rating |
|---|---|
| Non-high-rise, non-special | 2-hour structural, 2-hour compartment walls |
| High-rise residential (15-45 m) | 2-hour |
| High-rise residential (>45 m) | 3-hour |
| High-rise non-residential (18-45 m) | 2-hour |
| High-rise non-residential (>45 m) | 3-hour |
| Special buildings | 4-hour (large assemblies, hospitals) |
| Basement (>= 2 levels) | 4-hour external; sprinklered |

**Compartment size limits:** maximum 750 sqm per compartment in basement; 2,000 sqm above grade for office (E); 1,500 sqm assembly (D); 1,000 sqm hospital (C).

### 3.4 Sprinkler Requirements

- Mandatory for all **High-Rise Buildings** >= 15 m (Group A), >= 18 m others
- Mandatory for all **Special Buildings** regardless of height
- All **basements** >= 300 sqm
- All **hospitals** > 9 m height
- All **hotels** > 15 m height OR > 30 keys

Sprinkler systems are designed per **IS 15105:2002 (sprinklers)** + **TAC (Tariff Advisory Committee) Rules** for fire insurance purposes. NFPA 13 is sometimes referenced for fire engineering.

### 3.5 Fire Lifts (NBC 2016 Part 4, 4.5)

- Required: all high-rise buildings (>15 m residential, >18 m others)
- Minimum 1 fire lift per 1,200 sqm floor area, minimum 2 per building
- Capacity: minimum 545 kg, dimensions per IS 14665
- Speed: 1.0 m/s minimum, to be able to reach top floor in <= 1 minute
- Fire lift lobby: enclosed, 2-hour fire-rated, positive pressurized (50 Pa)
- Communication: dedicated firefighter intercom

### 3.6 Refuge Floors (High-rise > 24 m, NBC Part 4 4.6.6.4)

- **Refuge floor** required every 24 m (Mumbai stricter: every 7 floors via DCPR 2034)
- Refuge area: minimum 15 sqm OR 0.3 sqm/person served, whichever larger
- Refuge floor not to be used for any other purpose (no storage, no AHU); fully ventilated to atmosphere

---

## 4. Energy Code

### 4.1 ECBC 2017 (Commercial)

The **Energy Conservation Building Code 2017** (BEE, MoP) applies to:
- Buildings or building complexes with connected load >= 100 kW OR contract demand >= 120 kVA
- Or built-up area >= 500 sqm

It applies to **all new commercial buildings** in 21 states that have adopted (as of 2025). Aimed at 25-50% reduction over base case.

**Three compliance levels:**

| Level | Energy Savings vs Base | Mark |
|---|---|---|
| **ECBC** | 25% | ECBC-compliant |
| **ECBC+** | 35% | ECBC+ |
| **SuperECBC** | 50% | SuperECBC |

**Five Climate Zones (ECBC 2017 + IS 3792:1978):**

| Zone | HDD (base 21C) + CDH (base 25C) | Cities |
|---|---|---|
| **Hot-Dry** | CDH > 6000 K-h, HDD low | Ahmedabad, Jaipur, Nagpur, Jodhpur |
| **Warm-Humid** | High humidity (>= 75%), CDH > 6000 | Mumbai, Chennai, Kolkata, Goa, Vizag |
| **Composite** | Mixed extremes | Delhi, Lucknow, Kanpur, Allahabad |
| **Temperate** | Moderate temperatures year-round | Bangalore, Pune, Hyderabad (margin), Coimbatore |
| **Cold** | HDD > 3000 | Shimla, Srinagar, Leh, Gangtok, Darjeeling |

**ECBC 2017 prescriptive U-value targets (W/m2K):**

| Element | Hot-Dry | Warm-Humid | Composite | Temperate | Cold |
|---|---|---|---|---|---|
| Roof (24-hr use) | 0.33 | 0.33 | 0.33 | 0.33 | 0.33 |
| Wall (24-hr use) | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 |
| Wall (daytime use) | 0.85 | 0.85 | 0.85 | 0.85 | 0.55 |
| Glass U-factor (max) | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 |
| Glass SHGC (max, WWR <= 40%) | 0.27 | 0.27 | 0.27 | 0.27 | 0.62 (heating) |

(ECBC+ and SuperECBC tighten these. Cold zone allows higher SHGC for solar heating.)

### 4.2 ECBC-R 2018 / Eco-Niwas Samhita

Applies to **residential** buildings. Two parts:
- **Part 1 (ENS 2018)**: Building envelope -- defines RETV (Residential Envelope Transmittance Value) target by climate zone
- **Part 2 (ENS 2021)**: Electro-mechanical systems

**RETV targets:**

| Climate Zone | RETV Limit (W/m2) |
|---|---|
| Composite | 15 |
| Hot-Dry | 15 |
| Warm-Humid | 15 |
| Temperate | 15 |
| Cold | -- (U-thermal transmittance limit instead: Uroof <= 1.2, Uwall <= 1.8) |

### 4.3 Green Building Ratings

| System | Operator | Building Types | Levels |
|---|---|---|---|
| **GRIHA** (Green Rating for Integrated Habitat Assessment) | TERI + MNRE | New construction, large built-up | 1-5 star |
| **GRIHA SVA Griha** | Same | Small homes (<= 2,500 sqm) | -- |
| **GRIHA EB** | Same | Existing buildings | -- |
| **IGBC LEED India** | CII Indian Green Building Council | All types | Certified / Silver / Gold / Platinum |
| **IGBC Green New Buildings** | Same | India-specific frame | Same |
| **EDGE** | IFC (World Bank) | Affordable / SME | Certified / Advanced / Zero Carbon |
| **LEED v4.1** | USGBC (international) | All | Certified / Silver / Gold / Platinum |

GRIHA is mandatory for **all CPWD (Central Public Works Department) projects** since 2014. Many State PWDs follow.

---

## 5. Accessibility

### 5.1 Statutory Framework

- **Rights of Persons with Disabilities Act 2016** (RPwD Act) -- supersedes 1995 PwD Act. Schedule defines 21 disability categories. Section 44-46 mandate accessibility in built environment.
- **Accessibility Code of India** -- not a single document; combines RPwD Act + Harmonised Guidelines + NBC 2016 Part 3 (3.10).
- **Harmonised Guidelines and Space Standards for Universal Accessibility 2021** (MoHUA, replaces 2016 Harmonised Guidelines) -- detailed dimensional standards; refer to this as the primary technical reference.
- **CPWD Manual for Barrier-Free Built Environment 2014** (updated) -- for central government buildings.

### 5.2 Key Dimensional Requirements (Harmonised Guidelines 2021)

| Element | Required Dimension |
|---|---|
| Accessible route width | 1.2 m clear (1.5 m preferred); passing space at 60 m intervals |
| Door clear width | 900 mm minimum (entrance); 850 mm internal |
| Ramp gradient | Max 1:12 for 760 mm rise; 1:15 preferred; 1:20 for tactile contrast required |
| Ramp landing | 1.5 x 1.5 m at top/bottom; intermediate at every 9.0 m horizontal |
| Lift cabin | Minimum 1100 mm wide x 1300 mm deep (one wheelchair + attendant); for hospitals 1100 x 2100 mm (stretcher access) |
| Lift door | 900 mm clear |
| Accessible WC | 1.5 m x 2.2 m minimum; 1.5 m turning circle; grab rails at 850 mm AFL |
| Accessible parking | 3.6 m x 4.8 m + 1.2 m access aisle |
| Signage | Tactile + Braille; high contrast (>= 70% LRV difference); height 1.2-1.6 m for reading |
| Tactile flooring | At all level changes, doorways, ramps, stair edges, lift entries |
| Counter height | 800 mm max for accessible service counters |

### 5.3 Provision Counts (RPwD + Harmonised Guidelines)

- **Lifts**: All buildings G+1 and above accessible to public; G+2 for residential; G+0 for single-storey assemblies. (RPwD interpretation has tightened this.)
- **Accessible WC**: 1 per floor minimum; in public buildings 1 per gender per public WC bank + 1 universal
- **Accessible parking**: 2% of total OR minimum 2 spaces, whichever greater
- **Accessible seats in assembly**: 2% with companion seat, distributed (not clustered)

---

## 6. Structural Design (IS Codes)

### 6.1 Loads

| Type | Reference Standard |
|---|---|
| Dead loads | IS 875 (Part 1):1987 |
| Imposed loads | IS 875 (Part 2):1987 |
| Wind loads | IS 875 (Part 3):2015 -- 6 wind zones (33-55 m/s basic wind speed) |
| Snow loads | IS 875 (Part 4):1987 -- limited applicability |
| Special loads (impact, vibration etc.) | IS 875 (Part 5):1987 |
| Seismic | IS 1893 (Part 1):2016 |
| Load combinations | IS 875 Pt 5 + IS 1893; aligned to limit state |

### 6.2 Seismic Zoning (IS 1893:2016)

| Zone | Zone Factor Z | Intensity (MMVI/MSK) | Cities |
|---|---|---|---|
| **II** | 0.10 | VI | Bangalore, Hyderabad, Chennai (margin), Pune, Mumbai, Trivandrum |
| **III** | 0.16 | VII | Mumbai (Greater), Kolkata, Lucknow, Bhubaneswar, Ahmedabad, Surat, Jaipur |
| **IV** | 0.24 | VIII | Delhi, Jammu, Patna, Dehradun, Faridabad, Chandigarh |
| **V** | 0.36 | IX or more | Srinagar, Guwahati, Shillong, Aizawl, Imphal, Port Blair, Kutch (Bhuj), Sikkim |

**Ductile detailing** (IS 13920:2016) mandatory for all buildings in Zone III, IV, V and important structures in II.

### 6.3 Wind Zoning (IS 875 Part 3:2015)

| Wind Zone | Basic Wind Speed Vb (m/s, 50-year return) | Cities |
|---|---|---|
| Zone 1 | 33 | Trivandrum, Bangalore, Hyderabad |
| Zone 2 | 39 | Pune, Mumbai (inland), Chennai (margin) |
| Zone 3 | 44 | Mumbai (coastal), Kolkata, Delhi (margin) |
| Zone 4 | 47 | Bhubaneswar, Visakhapatnam |
| Zone 5 | 50 | Most coastal Tamil Nadu, Andhra coast |
| Zone 6 | 55 | Cyclone-prone Odisha, AP coast, Bay of Bengal islands |

### 6.4 Material Codes

| Material | Code |
|---|---|
| Plain & Reinforced Concrete | **IS 456:2000** (under revision; draft IS 456:2024) |
| Working stress concrete (where used) | IS 456 Annex N |
| High-performance concrete | IS 456 + IS 1199 + special provisions |
| Pre-stressed concrete | IS 1343:2012 |
| Steel general | **IS 800:2007** (limit state) |
| Cold-formed steel | IS 801:1975 + IS 811:1987 |
| Composite | IS 11384:1985 |
| Timber | IS 883:2016 + IS 4983 |
| Masonry | IS 1905:1987 |
| Foundations | IS 1904:1986 (general), IS 6403 (allowable bearing), IS 2950 (raft), IS 2911 (piles, 4 parts) |
| Aluminium | IS 8147 |
| Glass | IS 16231 (4 parts) |
| Curtain Wall | IS 17277:2019 |

---

## 7. Planning, Zoning & Urban Design Layer

### 7.1 RERA (Real Estate Regulatory Authority)

- **RERA Act 2016** -- mandatory registration for any residential/commercial project on plot > 500 sqm OR > 8 apartments
- State RERA authorities (e.g., MahaRERA Maharashtra, KRERA Karnataka, TNRERA Tamil Nadu) enforce
- Carpet Area definition standardized: **enclosed walkable area within apartment + internal partition walls, excluding balcony, terrace, utility area, external walls** (RERA Sec. 2(k))
- Promoter cannot use undefined area terms ("super built-up", "saleable area") in marketing without disclosure
- 70% of buyer payments held in escrow until completion

### 7.2 Coastal Regulation Zone (CRZ 2019)

For projects within 500 m of high tide line:
- **CRZ-I** (ecologically sensitive) -- no construction
- **CRZ-II** (developed urban) -- existing development controls + FSI limited
- **CRZ-III** (rural) -- limited; 200 m no-development zone
- **CRZ-IV** (water bodies) -- restricted activities

### 7.3 Environmental Clearance (EIA 2006 + amendments)

| Threshold | Category | Authority |
|---|---|---|
| Built-up >= 20,000 sqm AND <1,50,000 sqm | B2 | State EIA Authority (SEIAA) |
| Built-up >= 1,50,000 sqm | A | MoEFCC (Central) via EAC |
| Township projects >= 50 hectare OR >= 1,50,000 sqm built-up | A | MoEFCC |

Required: Form 1, Form 1A, Conceptual Plan, baseline studies, EIA report (Category A only with public hearing), EMP, EC validity 7 years.

### 7.4 Aviation NOC (DGCA NOCAS 2.0)

Online portal (nocas2.aai.aero). Required if building exceeds height limits computed from distance to nearest aerodrome:
- Type 1 airport (international, >2,500 m runway): NOC required within 20 km
- Type 2 airport (domestic): within 8.5 km
- Helipad: within 4 km

Height limits use a conical surface (slope varies by airport).

---

## 8. Quick Numeric Reference

| Parameter | Value | Source |
|---|---|---|
| Floor-to-floor height residential (standard) | 3.0 m | NBC Part 4 4.7.3.1 (min 2.75 m clear) |
| Floor-to-floor height office | 3.6 m | ECBC + NBC; min 2.75 m clear |
| Minimum room size (habitable, residential) | 9.5 sqm (single occupancy); 13.93 sqm (family room) | NBC Part 3 4.2 |
| Minimum kitchen size | 5.5 sqm | NBC Part 3 4.2.5 |
| Minimum bathroom | 1.8 sqm with min dim 1.2 m | NBC Part 3 4.2.5 |
| Minimum balcony depth | 0.9 m (varies by state DCR) | Local DCR |
| Corridor width residential | 1.0 m (1.2 m for high-rise) | NBC Part 4 4.4.3 |
| Corridor width hospital | 2.4 m | NBC Part 4 + FGI-derived |
| Corridor width office | 1.5 m | NBC Part 4 |
| Stair width residential (high-rise) | 1.5 m | NBC Part 4 4.4.3 + 4.5 |
| Stair width hospital | 2.0 m | NBC Part 4 |
| Tread/riser comfort | 250 mm tread; 175 mm riser (residential); 300/150 institutional | NBC Part 4 4.4.3 |
| Lift capacity (residential, basic) | 6-person (408 kg) | NBC Part 8 Sec 6 |
| Lift capacity (high-rise residential) | 13-person (884 kg) + fire lift 545 kg | Same |
| Parking ECS (Equivalent Car Space) | 25 sqm (covered including drive); 23 sqm uncovered + 5 sqm circulation | State DCR (varies) |
| Two-wheeler parking | 1.5 sqm per | NBC + local DCR |
| Bicycle parking (TOD) | Per local DCR; Mumbai DCPR mandates 1 per 100 sqm GFA |

---

## 9. Application Workflow

When advising on a project in India:

1. **Identify state + city + Municipal Corporation/Development Authority**.
2. **Check the in-force Building Bye-Laws version**. Indian DCRs change frequently (Mumbai DCPR 2034 replaced DCPR 1991; UDCPR 2020 unified Maharashtra; Kerala KMBR 2019 replaced 1999; etc.)
3. **Check ECBC adoption status in the state** + applicability threshold to the project.
4. **Confirm RERA registration requirement** (Sec. 3 thresholds).
5. **Confirm EIA category** based on built-up area (Sec. 7.3 above).
6. **Confirm Fire NOC requirement** + obtain pre-design Provisional NOC.
7. **Confirm Aviation NOC** if relevant (DGCA NOCAS 2.0).
8. **Confirm CRZ category** if coastal site.
9. **Apply NBC 2016** for life safety, then DCR for FAR/setback/parking, then ECBC for energy.
10. **Cite specific clauses**: "NBC 2016 Part 4 Clause 4.4.3", "ECBC 2017 Section 4.3.1.1", "IS 1893:2016 Clause 6.4.2", "Mumbai DCPR 2034 Regulation 33(10)", "MoHUA Harmonised Guidelines 2021 Section 2.5".

---

## 10. State-Specific Critical Notes

### Maharashtra / Mumbai (MCGM DCPR 2034)
- **Premium FSI** purchasable; **TDR** (Transfer of Development Rights) tradable
- Regulation 33(10) slum redevelopment, 33(7) cessed buildings, 33(9) cluster redevelopment, 33(11) gaothan
- Coastal projects subject to **MCZMA** + CRZ
- High-rise (>= 70 m) requires **High-Rise Committee** approval before MCGM permit
- Sanction in stages: IOD (Intimation of Disapproval -- ironic name, it's pre-conditions) -> CC (Commencement Certificate) -> OC (Occupation Certificate)

### Delhi NCR
- **Unified Building Bye-Laws 2016** (UBBL) applies to most agencies (MCD, NDMC, DDA)
- **MPD 2041** governs land use + density
- **HCBE (Heritage Conservation Committee)** + **DUAC (Delhi Urban Arts Commission)** review heritage zones and Lutyens' Bungalow Zone
- Gurugram has its own **Haryana Building Code 2017** + GMDA
- NOIDA / Greater NOIDA each have separate authority + bye-laws

### Karnataka / Bangalore
- **BBMP Bye-Laws 2003** + **BDA Master Plan RMP 2031** governs Bangalore
- **Tier-2 city codes** (Mysuru, Mangaluru) follow KMBBL with local amendments
- KSPCB Consent for any project > 1500 sqm

### Tamil Nadu / Chennai
- **TNCDBR 2019** (Tamil Nadu Combined Development and Building Rules 2019) updated and replaced 2008 + 2010 versions
- Multi-storey: > 4 floors or > 15 m
- **CMDA** for Chennai metropolitan; **DTCP** for rest of state

### Karnataka / Bangalore vs Telangana / Hyderabad
- Hyderabad has effectively **unlimited FAR** in many zones subject to setback + insurance premium (GO 168 + amendments)
- **TS-bPASS** -- Telangana's online single-window planning approval (instant for small plots, 21-day for large)

---

## 11. Authoritative Sources

- **Bureau of Indian Standards (BIS)** -- bis.gov.in -- NBC 2016 (SP 7), IS codes
- **Bureau of Energy Efficiency (BEE)** -- beeindia.gov.in -- ECBC 2017, ECBC-R 2018 (Eco-Niwas Samhita)
- **Ministry of Housing and Urban Affairs (MoHUA)** -- mohua.gov.in -- Harmonised Guidelines 2021
- **MoEFCC** -- moef.gov.in -- EIA Notifications, CRZ Notifications
- **State Town Planning Departments** -- portal varies by state
- **State Municipal Corporations** -- e.g., portal.mcgm.gov.in (Mumbai), mcdonline.nic.in (Delhi), bbmpgov.in (Bangalore), tnchennai.gov.in (Chennai), ghmc.gov.in (Hyderabad)
- **State Development Authorities** -- mmrda.maharashtra.gov.in (MMRDA), dda.gov.in (DDA), bda.karnataka.gov.in (BDA)
- **RERA portals** -- maharera.maharashtra.gov.in, rera.karnataka.gov.in, tnrera.in
- **GRIHA Council** -- grihaindia.org
- **IGBC (CII)** -- igbc.in

---

*Cross-references within this plugin: load `building-codes` for IBC comparison; `fire-life-safety` for general egress principles; `building-sustainability` for LEED/Passive House comparison; `structural-systems` for material-system selection within IS framework; `building-envelope` for envelope detailing in Indian climate zones.*
