# Adjacency Analysis Methods Reference

Comprehensive reference on proximity analysis, adjacency matrices, bubble diagramming, stacking analysis, and program testing for architectural programming.

---

## 1. Fundamentals of Adjacency Analysis

### 1.1 Purpose

Adjacency analysis translates the functional relationships between spaces into spatial organization logic. It bridges programming (what spaces are needed) and design (where spaces go). Without rigorous adjacency analysis, buildings suffer from:
- Excessive circulation (wasted area and energy)
- Workflow inefficiencies (staff walking unnecessary distances)
- User confusion (poor wayfinding)
- Environmental conflicts (noise, odour, vibration between incompatible uses)
- Security vulnerabilities (uncontrolled access between zones)

### 1.2 Types of Adjacency Relationships

| Relationship Type | Definition | Physical Implication |
|------------------|-----------|---------------------|
| Direct Adjacency | Spaces share a wall with a connecting door | No corridor between; maximum convenience |
| Near Proximity | Spaces on same floor within 30m walking distance | Short corridor connection; same department zone |
| Same Floor | Spaces on the same level but not necessarily close | Connected by primary circulation |
| Same Building Zone | Spaces in the same wing or section | Connected by secondary circulation |
| Visual Connection | Spaces must have sightline between them | Glazed partitions, open plans, overlook |
| Acoustic Separation | Spaces must NOT transmit sound between them | Solid walls STC 45+, buffer zones |
| Controlled Access | Access between spaces requires security clearance | Airlocks, badge readers, reception desks |
| Service Connection | Spaces share infrastructure (plumbing, gas, data) | Back-to-back wet walls, shared risers |
| Vertical Adjacency | Spaces on consecutive floors with direct connection | Dedicated lift, escalator, internal stair |

### 1.3 Factors Driving Adjacency Scores

When assigning relationship scores, evaluate each pair of spaces against these criteria:

1. **User Flow Volume**: How many people move between these spaces per hour? High volume = essential adjacency.
2. **Time Criticality**: Does delay in movement cause harm? (e.g., ED to Operating Theatre = life-threatening delay)
3. **Shared Resources**: Do spaces share equipment, staff, or supplies?
4. **Environmental Compatibility**: Are noise, odour, vibration, or security levels compatible?
5. **Operational Sequence**: Are spaces part of a sequential workflow?
6. **Public vs. Private**: Do spaces serve different access groups?
7. **Servicing**: Do spaces share building services infrastructure?
8. **Daylight and Views**: Do spaces compete for the same exterior wall?

---

## 2. Proximity Matrix Method

### 2.1 Scoring System

The standard 4-point scale:

| Score | Label | Meaning | Diagram Convention |
|-------|-------|---------|-------------------|
| 4 | Essential | Must be directly adjacent (shared wall/door) | Thick solid line, red |
| 3 | Desirable | Should be nearby (same zone, short walk) | Medium solid line, orange |
| 2 | Neutral | No strong preference for proximity | No line |
| 1 | Undesirable | Should be separated (noise, security, incompatibility) | Dashed line, blue |
| 0 | Prohibited | Must not be adjacent under any circumstances | Double dashed line, red |

Some practitioners use a 6-point or weighted system. The 4-point system is recommended for simplicity and reliability.

### 2.2 Matrix Construction Process

**Step 1:** List all departments or major space groups along both axes. Use 8-20 groups for a building-level matrix. For large buildings, create nested matrices (building-level, then department-level).

**Step 2:** Work through each pair systematically. Score based on criteria in Section 1.3. Involve stakeholders -- architects should not score alone.

**Step 3:** Validate by reading each row: "Department X has essential adjacency to A, desirable to B and C, neutral to D, and undesirable to E." Does this make operational sense?

**Step 4:** Identify clusters: groups of departments with mutual score-4 relationships form natural zones.

**Step 5:** Identify conflicts: any pair with score 1 that are both score-4 to a third space creates a design challenge.

### 2.3 Weighted Proximity Matrix

For complex projects, weight the scores by importance:

| Factor | Weight |
|--------|--------|
| Patient/user safety | 5 |
| Operational efficiency | 4 |
| Shared resources | 3 |
| Staff convenience | 2 |
| Environmental quality | 3 |
| Security | 4 |

Weighted score = sum of (score x weight) for each factor. This produces a continuous scale rather than a 4-point discrete scale, useful for optimization algorithms.

---

## 3. Bubble Diagramming

### 3.1 Purpose

Bubble diagrams translate the abstract matrix into a two-dimensional spatial arrangement. They are the first step from data to geometry.

### 3.2 Construction Method

1. **Draw each department as a circle** scaled to its relative area (not to precise scale -- this is diagrammatic)
2. **Place score-4 pairs touching** or overlapping
3. **Place score-3 pairs nearby** with a connecting line
4. **Leave score-2 pairs** without connection, at moderate distance
5. **Place score-1 pairs far apart** with a dashed line indicating required separation
6. **Iterate** until all relationships are satisfied or conflicts are identified
7. **Overlay on site** to test orientation, access, and massing implications

### 3.3 Rules and Conventions

- Circles represent departments or space groups, not individual rooms
- Circle area is proportional to department floor area
- Solid thick lines = essential adjacency (score 4)
- Solid thin lines = desirable adjacency (score 3)
- Dashed lines = required separation (score 1)
- Arrows indicate one-way flow relationships
- Hatched overlap = shared space (e.g., shared waiting area)
- External connections shown as lines to site edge (main entrance, service entrance, car park)

### 3.4 Common Patterns

**Hub-and-Spoke:** One central department (e.g., reception, nurse station) connects to multiple surrounding departments. Common in hospitals, schools, hotels.

**Linear Sequence:** Departments arranged in a sequential flow. Common in manufacturing, food production (raw materials > prep > cooking > serving > dining).

**Cluster:** Groups of departments with strong internal adjacency but weaker connection to other clusters. Common in universities (science cluster, humanities cluster) and mixed-use buildings.

**Ring:** Departments arranged around a central space (courtyard, atrium). All departments have equal access to the centre. Common in courtyard buildings, some museums.

**Tree/Branching:** Main circulation spine with departments branching off. Common in finger-plan hospitals, long school buildings.

---

## 4. Stacking Analysis

### 4.1 Purpose

Stacking diagrams translate the horizontal bubble diagram into a vertical section, assigning departments to floors. Stacking is driven by:
- Ground-floor access requirements (public entry, loading, emergency)
- Vertical adjacency needs (surgery above ED, wards above surgery)
- Structural logic (heavy loads at lower floors)
- Services distribution (plant at basement/roof, risers through building)
- Views and daylight (premium uses at upper floors)
- Fire and egress (vulnerable populations at lower floors)

### 4.2 Stacking Priorities

| Priority Level | Criterion | Examples |
|---------------|-----------|---------|
| 1 (Mandatory) | Must be at ground level | Main entrance, retail, emergency department, loading dock |
| 2 (Strong) | Should be at ground or first floor | Reception, public amenities, food service, accessible facilities |
| 3 (Preferred) | Benefit from lower floors | Heavy equipment, high-traffic departments |
| 4 (Flexible) | No strong floor preference | Office space, classrooms, hotel rooms |
| 5 (Upper preferred) | Benefit from upper floors | Executive offices, penthouses, observation, restaurant |
| 6 (Basement) | Below-grade appropriate | Car parking, plant rooms, storage, archive |

### 4.3 Stacking Diagram Format

A stacking diagram is a simplified building section showing:
- Each floor as a horizontal band
- Departments as coloured blocks within each floor band, scaled to area
- Core (lifts/stairs) shown as a vertical strip connecting all floors
- External connections (entrances, loading) shown at grade
- Arrows indicating key vertical movement (e.g., patients from ED to surgery)

### 4.4 Stacking Constraints

| Constraint | Impact |
|-----------|--------|
| Structural Transfer | Changing column grid between floors is expensive; align major structure |
| Service Risers | Wet spaces should stack vertically (WCs above WCs, labs above labs) |
| Floor-to-Floor Height | Different uses require different heights (retail 4.5m, office 3.9m, residential 3.0m) |
| Fire Separation | Different uses require fire-rated floors between them (e.g., residential above commercial) |
| Acoustic Separation | Impact noise from above (gyms, plant) must be separated from sensitive uses |
| Loading/Servicing | Back-of-house access at grade, service lifts to upper floors |
| Phasing | If building is phased, each phase should be functionally complete |

---

## 5. Program Testing

### 5.1 Fit-on-Floor Testing

Once stacking is determined, test whether each floor's assigned departments actually fit on the floor plate:

1. **Calculate floor plate NIA** = GIA - core - structure - risers
2. **Sum departmental areas** assigned to that floor
3. **Add intra-floor circulation** (10-15% for simple layouts, 15-25% for complex)
4. **Compare NIA available vs. NIA required**
5. **Check floor plate depth** for daylight compliance (max 12-15m from window for office/residential)

### 5.2 Circulation Testing

Test whether the building's circulation system supports the adjacency requirements:

| Test | Method | Pass Criteria |
|------|--------|--------------|
| Travel Distance | Measure from each score-4 pair's centroids | < 30m for essential adjacencies |
| Corridor Width | Check peak flow between departments | Min 1.5m general, 2.4m hospital bed corridor |
| Way-Finding Complexity | Count decision points from entrance to each department | < 3 turns for public areas |
| Egress | Check travel distance to nearest exit | Per fire code (IBC: 75m sprinklered, 60m unsprinklered) |
| Accessibility | Check all public routes for step-free access | 100% step-free to all public areas |

### 5.3 Conflict Resolution

When adjacency requirements conflict (common in complex buildings):

1. **Identify the conflict:** Space A needs to be adjacent to both B and C, but B and C must be separated.
2. **Evaluate priorities:** Which adjacency is more critical? Use weighted scores.
3. **Design solutions:**
   - Intermediate buffer space between B and C
   - Vertical adjacency (A on floor between B and C)
   - Dedicated connecting corridor from A to the less-critical partner
   - Duplicate a function (e.g., satellite imaging suite near both ED and outpatient)
4. **Document the resolution** and the compromise accepted.

---

## 6. Worked Examples

### 6.1 Hospital (150-Bed District General)

**Departments:** Emergency (ED), Diagnostic Imaging, Operating Theatres, Inpatient Wards, Outpatient Clinics, Maternity, Pathology Lab, Administration, Facilities/Plant

**Adjacency Matrix:**

|  | ED | Imaging | Surgery | Wards | OPD | Maternity | Path Lab | Admin | Facilities |
|--|---:|--------:|--------:|------:|----:|---------:|---------:|------:|-----------:|
| ED | -- | 4 | 4 | 3 | 2 | 2 | 3 | 1 | 1 |
| Imaging | -- | -- | 3 | 2 | 4 | 2 | 2 | 1 | 1 |
| Surgery | -- | -- | -- | 4 | 2 | 3 | 3 | 1 | 1 |
| Wards | -- | -- | -- | -- | 2 | 3 | 2 | 2 | 2 |
| OPD | -- | -- | -- | -- | -- | 2 | 2 | 2 | 1 |
| Maternity | -- | -- | -- | -- | -- | -- | 2 | 1 | 1 |
| Path Lab | -- | -- | -- | -- | -- | -- | -- | 1 | 2 |
| Admin | -- | -- | -- | -- | -- | -- | -- | -- | 2 |
| Facilities | -- | -- | -- | -- | -- | -- | -- | -- | -- |

**Stacking Solution:**
- **Basement:** Plant/Facilities, Pathology Lab (pneumatic tube to all floors), Car Park
- **Ground Floor:** ED (ambulance access), Imaging (adjacent to ED), Main Entrance, OPD (public access), Maternity (separate entrance possible)
- **First Floor:** Operating Theatres (above ED for vertical transfer), Day Surgery, CSSD
- **Second Floor:** Inpatient Wards (above surgery for post-op)
- **Third Floor:** Maternity Ward (if not at ground), additional Inpatient Wards
- **Roof Level:** Helipad (if required), additional plant

**Key Design Moves:**
- ED and Imaging share a dedicated CT scanner at their interface
- Pneumatic tube system connects Pathology Lab to ED, Surgery, and Wards
- Dedicated patient lift connects ED (ground) to Surgery (first) to Wards (second)
- Public circulation (outpatients, visitors) separated from clinical circulation (staff, patients in beds)

### 6.2 Secondary School (1200 Pupils, 8 Form Entry)

**Departments:** Administration, Science, Humanities, Creative Arts, Technology, Sports, Library/Media, Dining, Sixth Form

**Adjacency Matrix:**

|  | Admin | Science | Human. | Creative | Tech | Sports | Library | Dining | 6th Form |
|--|------:|--------:|-------:|---------:|-----:|-------:|--------:|-------:|---------:|
| Admin | -- | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Science | -- | -- | 2 | 2 | 3 | 1 | 3 | 2 | 3 |
| Humanities | -- | -- | -- | 2 | 2 | 1 | 4 | 2 | 3 |
| Creative | -- | -- | -- | -- | 3 | 1 | 2 | 2 | 2 |
| Technology | -- | -- | -- | -- | -- | 1 | 2 | 2 | 2 |
| Sports | -- | -- | -- | -- | -- | -- | 1 | 3 | 2 |
| Library | -- | -- | -- | -- | -- | -- | -- | 2 | 4 |
| Dining | -- | -- | -- | -- | -- | -- | -- | -- | 2 |
| 6th Form | -- | -- | -- | -- | -- | -- | -- | -- | -- |

**Key Adjacency Logic:**
- Admin must front the main entrance for safeguarding (visitors sign in at reception) -- score 4 to entrance, implicit
- Science and Technology share services (gas, water, extraction) -- score 3
- Sports separated from all teaching departments -- noise, vibration (score 1)
- Library central to Humanities and Sixth Form -- study resource (score 4)
- Dining adjacent to Sports for hall dual-use potential and kitchen servicing (score 3)
- Creative Arts and Technology share making/messy activities -- adjacency supports shared workshops (score 3)

**Stacking Solution (3-storey):**
- **Ground Floor:** Main Entrance + Admin, Dining Hall + Kitchen, Sports Hall (separate structure or wing), Technology (heavy equipment, ground level, service access)
- **First Floor:** Science (services can rise from ground), Creative Arts, some Humanities
- **Second Floor:** Remaining Humanities, Library/Media Centre, Sixth Form Centre

### 6.3 Office Building (15,000 m2 GIA, Multi-Tenant Speculative)

**Departments (generic for spec office):** Reception/Lobby, Retail (ground floor), Office Floors (multi-tenant), Building Management, Car Park, Cycle/End-of-Trip, Plant

**Adjacency Matrix:**

|  | Reception | Retail | Office | Bldg Mgmt | Car Park | Cycle/EoT | Plant |
|--|----------:|-------:|-------:|----------:|---------:|----------:|------:|
| Reception | -- | 3 | 4 | 2 | 2 | 3 | 1 |
| Retail | -- | -- | 1 | 1 | 2 | 2 | 1 |
| Office | -- | -- | -- | 2 | 2 | 3 | 1 |
| Bldg Mgmt | -- | -- | -- | -- | 3 | 2 | 4 |
| Car Park | -- | -- | -- | -- | -- | 3 | 2 |
| Cycle/EoT | -- | -- | -- | -- | -- | -- | 1 |
| Plant | -- | -- | -- | -- | -- | -- | -- |

**Stacking Solution:**
- **Basement 2:** Car Park, main plant room
- **Basement 1:** Car Park, cycle parking, end-of-trip facilities (showers/lockers), building management office (near plant)
- **Ground Floor:** Reception/Lobby (double height), Retail units (street frontage), office entrance separate from retail
- **Floors 1-10:** Speculative office floors, 1200-1500 m2 NIA per floor
- **Roof:** Secondary plant (cooling towers, AHUs), potential terrace amenity

**Key Design Moves:**
- Separate lobby cores for office (secure lift access) and retail (direct street entry)
- End-of-trip facilities adjacent to cycle parking with direct lift access to office floors
- Retail servicing from basement loading dock, separate from office servicing
- Building management with direct access to both basement plant and roof plant via service lift

### 6.4 Mixed-Use Development (Podium + Tower)

**Components:** Retail (ground/first), Office (podium floors 2-5), Residential (tower floors 6-25), Car Park (basement), Shared Amenity

**Adjacency Matrix:**

|  | Retail | Office | Residential | Car Park | Amenity |
|--|-------:|-------:|------------:|---------:|--------:|
| Retail | -- | 2 | 1 | 2 | 2 |
| Office | -- | -- | 1 | 3 | 2 |
| Residential | -- | -- | -- | 3 | 4 |
| Car Park | -- | -- | -- | -- | 1 |
| Amenity | -- | -- | -- | -- | -- |

**Key Separation Requirements:**
- Residential entrance MUST be separate from office and retail entrances (score 1 between lobbies)
- Fire separation: 2-hour fire-rated floor between different use classes
- Acoustic separation: residential above office requires impact isolation (floating floor, 50dB min)
- Structural transfer: office column grid (9m x 9m) differs from residential (6m x 7.5m) -- transfer structure at level 5/6 interface
- Services: separate risers for each use; residential services cannot pass through office floors without fire-rated enclosure
- Waste: separate refuse collection for residential and commercial

**Stacking Solution:**
- **Basement 1-2:** Car park (allocated by use: residential permit, office daily, retail customer), bicycle, plant
- **Ground Floor:** Retail units (street frontage), residential lobby (separate entrance), office lobby (separate entrance), loading dock (shared, time-managed)
- **First Floor:** Retail mezzanine or additional retail, shared amenity (gym, co-working)
- **Floors 2-5:** Office (podium, larger floor plates 1500-2000 m2)
- **Floor 6 (transfer level):** Residential amenity deck (pool, terrace, lounge) -- also accommodates structural transfer
- **Floors 7-25:** Residential tower (smaller floor plate 600-800 m2, 6-8 units per floor)
- **Roof:** Residential rooftop terrace, PV array, secondary plant

---

## 7. Digital Tools for Adjacency Analysis

### 7.1 Software Options

| Tool | Application | Adjacency Features |
|------|------------|-------------------|
| Microsoft Excel / Google Sheets | Matrix construction | Half-matrix template, conditional formatting by score |
| dRofus | Room programming | Built-in adjacency matrix, links to BIM |
| Trelligence Affinity | Space programming | Automated bubble diagrams from matrix input |
| Revit (with Dynamo) | BIM-integrated programming | Custom scripts to test adjacency in model |
| Grasshopper (Rhino) | Parametric programming | Space packing algorithms, adjacency optimization |
| ARCHIBUS / FM:Systems | Facility management | Existing building adjacency analysis, move planning |
| SpaceS (custom tool) | Adjacency optimization | Genetic algorithm-based space arrangement |

### 7.2 Computational Adjacency Optimization

For large or complex programs, computational methods can optimize spatial arrangements:

1. **Graph-Based:** Represent departments as nodes and adjacency scores as edge weights. Use force-directed graph layout to find optimal 2D arrangement.
2. **Genetic Algorithm:** Encode floor assignments as chromosomes. Fitness function = sum of (adjacency score x 1/distance) for all pairs. Evolve toward optimal stacking.
3. **Simulated Annealing:** Start with random arrangement, iteratively swap departments, accept swaps that improve adjacency satisfaction (and occasionally worse swaps to escape local optima).
4. **Multi-Objective Optimization:** Balance adjacency satisfaction against other objectives (structural efficiency, daylight, views, cost) using Pareto front analysis.

---

## 8. Quality Assurance Checklist

Before finalizing adjacency analysis, verify:

- [ ] All departments included in the matrix (no orphans)
- [ ] Stakeholders validated scores (not architect assumptions alone)
- [ ] Score-4 relationships are achievable on the proposed floor plate
- [ ] No unresolved score-1 conflicts with mutual score-4 partners
- [ ] Ground-floor access requirements satisfied
- [ ] Vertical adjacencies accommodated in stacking diagram
- [ ] Service connections (wet walls, risers) aligned vertically
- [ ] Public vs. private circulation separated
- [ ] Fire compartmentation does not sever score-4 relationships
- [ ] Accessibility route connects all public departments
- [ ] Loading and servicing access does not conflict with public entrance
- [ ] Matrix updated if program changes during design

---

## References

- Pena, W. & Parshall, S. (2012). *Problem Seeking*. 5th ed. Wiley.
- Palmer, M.A. (1981). *The Architect's Guide to Facility Programming*. AIA / McGraw-Hill.
- Hershberger, R. (1999). *Architectural Programming and Predesign Manager*. McGraw-Hill.
- Duerk, D. (1993). *Architectural Programming: Information Management for Design*. Wiley.
- NHS Estates. *Health Building Notes* (HBN) Series. UK Department of Health.
- DfE (2014). *Building Bulletin 103*. UK Department for Education.
- BCO (2019). *BCO Guide to Specification*. British Council for Offices.
- Neufert, E. & Neufert, P. (2019). *Neufert Architects' Data*. 5th ed. Wiley-Blackwell.
