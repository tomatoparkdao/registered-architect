# Specification Writing Guide — Deep Reference

Comprehensive reference on architectural specification systems, performance vs. prescriptive methods, submittals, testing standards, quality assurance, and common errors.

---

## 1. Purpose of Specifications

Specifications are the written component of construction documents that describe materials, products, workmanship standards, and quality requirements. They complement drawings (which describe geometry, location, and quantity) by defining qualitative requirements.

**Key Principle:** Drawings show WHAT and WHERE; specifications describe HOW and to WHAT STANDARD.

**Contractual Status:** Specifications are contract documents. Ambiguity or conflict between specifications and drawings creates contractual risk. Most contracts establish a hierarchy: specifications take precedence over drawings for quality/material matters; drawings take precedence for dimensions/quantities.

---

## 2. Specification Systems

### 2.1 NBS (National Building Specification) — UK/International

The most widely used specification system in the UK, Australia, and parts of Europe and Asia.

**Structure:**
- Organized by work sections corresponding to trade packages
- Each section contains: scope, general requirements, materials, workmanship, and completion criteria
- Clauses are pre-written templates customized by the specifier

**Key Work Sections (NBS format):**
- A — Preliminaries/General conditions
- C — Demolition/Alteration/Renovation
- D — Groundwork
- E — In-situ concrete/Large precast concrete
- F — Masonry
- G — Structural/Carcassing metal/timber
- H — Cladding/Covering
- J — Waterproofing
- K — Linings/Sheathing/Dry partitioning
- L — Windows/Doors/Stairs
- M — Surface finishes
- N — Furniture/Equipment
- P — Building fabric sundries
- Q — Paving/Planting/Fencing/Site furniture
- R — Disposal systems
- S — Piped supply systems
- T — Mechanical heating/cooling/refrigeration
- U — Ventilation/Air conditioning
- V — Electrical supply/power/lighting
- W — Communications/Security/Control
- X — Transport systems (lifts, escalators)
- Y — Mechanical/Electrical services measurement
- Z — Building fabric reference specification

**NBS Chorus / NBS Source:**
Cloud-based specification platform; linked to manufacturer product data; BIM-integrated (NBS objects with specification data embedded). Industry standard for UK practice.

### 2.2 CSI MasterFormat — North America

The Construction Specifications Institute (CSI) MasterFormat is the standard specification organization system in the USA and Canada.

**Division Structure (50 divisions, key ones listed):**

| Division | Title | Content |
|---|---|---|
| 00 | Procurement and Contracting | Bidding requirements, contracts, bonds |
| 01 | General Requirements | Summary, price and payment, administrative, QA/QC, temporary facilities |
| 02 | Existing Conditions | Survey, demolition, hazmat abatement |
| 03 | Concrete | Cast-in-place, precast, reinforcement, formwork |
| 04 | Masonry | Unit masonry, stone, manufactured stone |
| 05 | Metals | Structural steel, miscellaneous metals, stairs, railings |
| 06 | Wood, Plastics, and Composites | Rough carpentry, finish carpentry, millwork, FRP |
| 07 | Thermal and Moisture Protection | Insulation, waterproofing, roofing, cladding, sealants |
| 08 | Openings | Doors, windows, curtain wall, glazing, hardware |
| 09 | Finishes | Plaster, gypsum board, flooring, painting, wall coverings |
| 10 | Specialties | Signage, lockers, toilet accessories, fire protection specialties |
| 11 | Equipment | Kitchen, laundry, medical, laboratory |
| 12 | Furnishings | Furniture, window treatments, fabrics |
| 13 | Special Construction | Swimming pools, clean rooms, seismic protection |
| 14 | Conveying Equipment | Elevators, escalators, dumbwaiters |
| 21 | Fire Suppression | Sprinkler systems |
| 22 | Plumbing | Domestic water, drainage, fixtures |
| 23 | HVAC | Heating, cooling, ventilation, controls |
| 25 | Integrated Automation | Building management systems |
| 26 | Electrical | Power distribution, lighting |
| 27 | Communications | Data, voice, AV, security |
| 28 | Electronic Safety and Security | Fire alarm, access control, CCTV |
| 31-35 | Earthwork through Waterway/Marine | Site and civil |
| 40-48 | Process Integration through Electrical | Industrial/process |

**Three-Part Section Format (CSI):**
1. **Part 1 — General:** Scope, references, submittals, quality assurance, delivery/storage, warranty
2. **Part 2 — Products:** Materials, manufacturers, fabrication, finishes
3. **Part 3 — Execution:** Examination, preparation, installation, field quality control, cleaning, protection

### 2.3 Uniclass — International (RIBA/NBS)

Unified classification system for the construction industry. More comprehensive than NBS work sections; used for BIM classification.

**Tables:**
- Co — Complexes (campus, estate)
- En — Entities (building, bridge)
- Ac — Activities (design, construction)
- SL — Spaces/Locations (rooms, zones)
- EF — Elements/Functions (wall, roof, floor)
- Ss — Systems (curtain wall system, underfloor heating)
- Pr — Products (brick, insulation board, steel beam)
- TE — Tools and Equipment

---

## 3. Specification Types

### 3.1 Performance Specification

Defines the required outcome or performance without prescribing specific products or methods.

**Advantages:**
- Allows contractor innovation and value engineering
- Focuses on what matters (performance)
- Reduces specification volume
- Suitable for design-build procurement

**Disadvantages:**
- Requires measurable performance criteria
- Harder to evaluate tenders (subjective judgment)
- Risk of cheapest-compliant solution
- Requires robust testing and verification

**Example — Performance Specification for Curtain Wall:**
```
The curtain wall system shall achieve the following performance criteria:
- Air permeability: ≤ 1.5 m³/h/m² at 600 Pa (BS EN 12152, Class AE)
- Watertightness: no water penetration at 600 Pa (BS EN 12154, Class RE 600)
- Wind resistance: ±2400 Pa serviceability, ±3600 Pa safety (BS EN 13116)
- Thermal transmittance: Ucw ≤ 1.3 W/m²K (EN 13947)
- Acoustic performance: Rw ≥ 38 dB (EN ISO 10140)
- Fire: E60 integrity, EI30 insulation at spandrel (EN 1364-4)
```

### 3.2 Prescriptive Specification

Specifies exact products, materials, dimensions, and installation methods.

**Advantages:**
- Clear and unambiguous
- Easy to price and compare tenders
- Architect controls exact material outcome
- Simple compliance verification

**Disadvantages:**
- Restricts contractor alternatives
- Architect assumes liability for product performance
- Must be updated if products become unavailable
- "Or equal" clauses create ambiguity

**Example — Prescriptive Specification for Brickwork:**
```
Facing bricks shall be Ibstock Leicester Red Stock, 215 × 102.5 × 65 mm,
compressive strength ≥ 25 MPa, water absorption 8-14%, frost resistant (F2),
laid in Flemish bond with bucket handle joints, 10 mm wide, in 1:1:6 mortar
(OPC:lime:sand) using Hanson Natural Hydraulic Lime NHL 3.5.
```

### 3.3 Proprietary Specification

Names a specific manufacturer and product. Most restrictive form.

**Use Cases:**
- When only one product meets the design intent
- When manufacturer has been involved in design development
- When client has bulk purchasing agreements
- When project involves matching existing installations

**Legal Requirement:** Most public procurement requires "or approved equal" clause to ensure fair competition. Private projects may specify sole-source.

### 3.4 Reference Standard Specification

Cites published standards as the specification basis. The standard document becomes part of the contract.

**Example:** "Structural steelwork shall comply with BS EN 1090-2, Execution Class EXC2."

**Caution:** Always specify the standard edition/year. Standards are revised; citing without a date means the current version at time of tender, which may differ from design intent.

---

## 4. Submittals and Approvals

### 4.1 Types of Submittals

| Submittal Type | Purpose | Timing | Reviewed By |
|---|---|---|---|
| Shop drawings | Detailed fabrication/installation drawings | Before fabrication | Architect + structural engineer |
| Product data | Manufacturer cut sheets, test reports | Before procurement | Architect |
| Samples | Physical material samples for approval | Before procurement | Architect + client |
| Mock-ups | Full-scale assemblies for quality benchmarking | Before production run | Architect + client + engineer |
| Test reports | Third-party test results for specified performance | Before/during installation | Engineer |
| Certificates | ISO, CE, third-party certifications | Before procurement | Architect |
| Color charts / RAL | Exact color selections | Before manufacturing | Architect + client |
| Method statements | Construction methodology descriptions | Before work starts | Project manager + HSE |
| Warranties | Written guarantees | Before practical completion | Client legal team |

### 4.2 Approval Stamps

Standard approval actions:
- **Approved:** Proceed as submitted; no changes required
- **Approved as noted:** Proceed with minor corrections marked on submittal; no resubmission needed
- **Revise and resubmit:** Significant issues; correct and resubmit for review before proceeding
- **Rejected:** Does not comply; start over or submit alternative

**Critical Principle:** Approval of submittals does not relieve the contractor of responsibility for compliance with the contract documents. The architect's review is for general conformance only.

### 4.3 Sample and Mock-Up Requirements

**Retained Samples:**
- Brick: minimum 6 bricks showing full color and texture range
- Stone: minimum 300 × 300 mm sample per stone type
- Metal cladding: minimum 300 × 300 mm with specified finish
- Paint/coating: minimum A4-size sample on specified substrate
- Timber: minimum 300 × 150 mm showing grain, color, and finish
- Glass: minimum 300 × 300 mm of each glass type in IGU configuration
- Mortar: minimum 3 sample panels (600 × 600 mm) with specified joint profile

**Mock-Ups:**
- Purpose: establish quality benchmark; test installation methodology; verify appearance
- Typical scope: 3 m × 3 m panel of facade assembly (minimum 2 bays × 2 storeys)
- Must include window/door openings, corners, expansion joints, and flashings
- Retained on site as reference standard for duration of construction
- Weather testing of mock-ups: hose test to BS EN 1027 or AAMA 501.1

---

## 5. Material Testing and Certification

### 5.1 CE Marking / UKCA Marking

**CE Marking (EU):**
- Mandatory for products covered by harmonized European standards (hEN) or European Technical Assessments (ETA)
- Declaration of Performance (DoP) issued by manufacturer
- Notified Body involvement required for some products (structural steel, fire products)
- Key product standards: EN 197 (cement), EN 206 (concrete), EN 771 (masonry), EN 1090 (steel), EN 14080 (glulam), EN 14351 (windows/doors)

**UKCA Marking (UK post-Brexit):**
- Equivalent to CE for UK market
- UK Approved Bodies replace EU Notified Bodies
- Transitional period allowing CE marking extended; check current status

### 5.2 Key Testing Standards

**Concrete:**
- BS EN 12390 series: compressive strength (Part 3), tensile splitting (Part 6), density (Part 7)
- BS EN 12504: assessment in structures (core tests, rebound hammer, ultrasonic)
- Slump test: BS EN 12350-2

**Steel:**
- BS EN 10025: hot-rolled structural steel (mill certificate EN 10204 3.1)
- BS EN 1090: execution of steel structures (CE marking; EXC1-4)
- Charpy impact test: BS EN ISO 148-1
- Weld inspection: visual, ultrasonic (UT), magnetic particle (MPI), radiographic (RT)

**Timber:**
- BS EN 338: strength classes (C14-C50 softwood, D18-D70 hardwood)
- BS EN 14081: strength grading of structural timber (machine or visual)
- BS EN 14080: glued laminated timber — requirements
- BS EN 16351: CLT — structural properties
- Moisture content: BS EN 13183 (oven-dry or electrical resistance)

**Masonry:**
- BS EN 771: specification for masonry units (Part 1: clay, Part 2: calcium silicate, Part 3: concrete)
- BS EN 772: test methods (dimensions, compressive strength, water absorption, frost resistance)
- BS EN 1052: test methods for masonry (compressive, flexural, shear strength)
- Mortar: BS EN 998-2 (specification); BS EN 1015 (test methods)

**Glass:**
- BS EN 12150: thermally toughened glass
- BS EN ISO 12543: laminated glass
- BS EN 1279: insulating glass units (gas fill, moisture penetration, edge seal)
- BS EN 410: optical properties (VLT, SHGC)
- BS EN 673: thermal transmittance (U-value calculation)
- Impact: BS EN 12600 (pendulum test; classification 1B1 most demanding)

**Fire Testing:**
- BS EN 13501-1: reaction to fire classification (Euroclass A1 to F)
- BS EN 13501-2: fire resistance classification (R, E, I, W)
- BS 476: Parts 6 and 7 (UK fire propagation and surface spread of flame — legacy standard)
- ASTM E84: surface burning characteristics (Flame Spread Index, Smoke Developed Index) — USA
- ASTM E119: fire endurance test (walls, floors, columns) — USA
- UL 263: fire tests of building construction and materials — USA

**Weathering/Durability:**
- BS EN 12371: frost resistance of natural stone
- BS EN 539-1: frost resistance of clay roofing tiles
- BS EN ISO 12944: corrosion protection of steel by paint coatings (environment C1-CX, durability L/M/H)
- ASTM G154: UV accelerated weathering (QUV test)
- BS EN ISO 9227: salt spray corrosion test

### 5.3 ASTM Key Standards (North America)

| Standard | Material | Test |
|---|---|---|
| ASTM C39 | Concrete | Compressive strength of cylinders |
| ASTM C150 | Portland cement | Chemical/physical requirements |
| ASTM C90 | Concrete masonry | Loadbearing units |
| ASTM C216 | Facing brick | Physical requirements |
| ASTM C270 | Mortar | Proportion and property specifications |
| ASTM C1048 | Glass | Heat-strengthened and toughened flat glass |
| ASTM A36 | Steel | Carbon structural steel |
| ASTM A992 | Steel | Structural steel shapes (W sections) |
| ASTM A572 | Steel | High-strength low-alloy structural steel |
| ASTM D3498 | Adhesive | Construction adhesive |
| ASTM E84 | All | Surface burning (flame spread) |
| ASTM E119 | All | Fire endurance |
| ASTM E331 | Curtain wall | Water penetration (static pressure) |
| ASTM E283 | Curtain wall | Air leakage |
| ASTM E330 | Curtain wall | Structural wind load |

---

## 6. Quality Assurance on Site

### 6.1 Inspection and Testing Plan (ITP)

An ITP defines all inspection and testing activities, their timing, acceptance criteria, and responsible parties.

**Standard ITP Elements:**

| Activity | Timing | Method | Acceptance Criteria | Responsibility | Hold/Witness/Review |
|---|---|---|---|---|---|
| Concrete cube tests | Every 50 m³ or daily | BS EN 12390-3 | fck + margin | Contractor | Review |
| Rebar cover check | Before pour | Cover meter survey | Spec ± tolerance | Contractor | Witness |
| Steel weld inspection | During fabrication | Visual + UT/MPI | EN 1090 EXC2 | CSWIP inspector | Hold |
| Brick panel approval | First panel complete | Visual + measurement | Match approved sample | Architect | Hold |
| Curtain wall mock-up | Before production | AAMA 501.1 / EN 13050 | Pass all criteria | Specialist | Hold |
| Timber MC check | On delivery | Electrical resistance | ≤ 18% (structural) | Contractor | Review |
| Airtightness test | At envelope completion | EN ISO 9972 (Blower door) | ≤ target (q50 or n50) | Specialist | Hold |
| Fire stopping | After installation | Visual + probe | Complete seal; cert. | Fire consultant | Witness |

### 6.2 Hold Points

A hold point is a mandatory inspection stage where work cannot proceed until the architect, engineer, or inspector has approved the previous stage. Work proceeding past a hold point without approval is a contract breach.

**Critical Hold Points:**
1. Foundation excavation — inspect formation before concrete pour
2. Reinforcement — check before concrete pour (cover, spacing, laps, chairs)
3. Structural steel connections — check before encasement or cladding
4. Waterproofing — inspect before backfill or overburden
5. Facade mock-up — approve before production begins
6. Fire stopping — inspect before concealment by finishes
7. Above-ceiling services — inspect before ceiling installation
8. Pre-completion airtightness — test before internal finishes if possible

### 6.3 Non-Conformance Procedure

When work or materials fail to meet specification:
1. **Identify:** Site inspector or clerk of works raises Non-Conformance Report (NCR)
2. **Document:** Photograph, measure, record NCR details
3. **Assess:** Engineer/architect evaluates significance (structural, aesthetic, performance)
4. **Decide:** Accept as-built (with justification), remediate/repair, or reject and replace
5. **Close:** Confirm corrective action; update records; prevent recurrence

---

## 7. Common Specification Errors

### 7.1 Ambiguity and Conflict

1. **Drawing-specification conflict:** Drawing shows concrete block; specification calls for brick. Resolution: establish clear hierarchy in contract conditions.
2. **"Or equal" without criteria:** "Manufacturer X or equal" without defining what "equal" means. Fix: define the performance criteria that constitute equality.
3. **Outdated standards:** Citing withdrawn standards (e.g., BS 476 instead of EN 13501). Always verify current status.
4. **Conflicting performance requirements:** Specifying both a prescriptive product AND performance criteria that the product may not meet. Use one approach per clause.

### 7.2 Over-Specification

5. **Unnecessarily restrictive tolerances:** Specifying ±1 mm where ±3 mm is adequate adds cost without benefit.
6. **Excessive testing frequency:** Requiring cube tests every 10 m³ instead of 50 m³ for standard concrete.
7. **Premium products for concealed work:** Specifying architectural-grade concrete for buried foundations.
8. **Single-source proprietary without justification:** Naming one manufacturer when multiple equivalents exist — may invite legal challenge on public projects.

### 7.3 Under-Specification

9. **Missing performance criteria:** Specifying "aluminium curtain wall" without U-value, air permeability, water tightness, or acoustic requirements.
10. **No sample/mock-up requirement:** Omitting mock-up for visible facade work leads to disputes about quality.
11. **Undefined finish quality:** "Fair-faced concrete" without reference sample or defined tolerance class (DIN 18217 / SCC classes).
12. **No maintenance information:** Failing to specify maintenance manuals, spare parts, or warranty documentation.

### 7.4 Coordination Failures

13. **Uncoordinated interfaces:** Structural specification calls for S355 steel; facade specification assumes S275 connections at fixing points.
14. **Missing builder's work:** Specification for curtain wall does not include requirement for structural cast-in channels or brackets.
15. **Fire strategy gaps:** Fire-rated partition specified but no fire stopping specified at service penetrations.
16. **Inconsistent sustainability targets:** BREEAM specification requires BES 6001 responsible sourcing, but individual material sections do not reference it.

### 7.5 Procurement Errors

17. **No lead-time awareness:** Specifying a natural stone with 16-week quarrying and import lead time on a 12-week programme.
18. **Discontinued products:** Specifying a product that has been discontinued or is only available in minimum bulk quantities.
19. **No substitution procedure:** Failing to define how substitution requests are handled, documented, and approved.
20. **Mismatched warranty periods:** Building warranty requires 12-year defects liability but specified sealant warranty is 10 years.

---

## 8. Specification Best Practices

### 8.1 Writing Principles

1. **Use imperative mood:** "The contractor shall..." not "The contractor should..."
2. **Be specific and measurable:** "Compressive strength ≥ 30 MPa" not "adequate strength"
3. **One requirement per clause:** Avoid compound clauses with multiple conditions
4. **Cross-reference carefully:** Ensure referenced documents are listed in the General section
5. **Use consistent terminology:** Define key terms in General section; use them identically throughout
6. **Avoid manufacturer bias in performance specs:** Define what it must do, not who makes it
7. **Include all acceptance criteria:** If you specify a test, specify the pass/fail threshold
8. **Specify positive requirements:** "Shall be..." not "Shall not be..." (except for prohibited substances)

### 8.2 Sustainability Clauses

Modern specifications should include:
- **Embodied carbon limits:** Maximum kgCO2e per m² or per functional unit, with EPD (Environmental Product Declaration) as evidence
- **Responsible sourcing:** BES 6001, FSC/PEFC (timber), ASI (aluminum), ResponsibleSteel
- **Recycled content minimums:** e.g., ≥ 25% recycled aggregate in concrete, ≥ 90% recycled content in structural steel
- **Low-VOC materials:** Greenguard Gold, French A+ emission class, EN 16516 testing
- **Material passports:** Require manufacturers to provide Madaster or equivalent material passport data
- **Design for Disassembly:** Specify bolted connections where feasible; identify elements for future reuse

### 8.3 Coordination Checklist

Before issuing specifications:
- [ ] All specification sections reviewed against current drawings
- [ ] Structural, mechanical, electrical, and facade specifications cross-referenced
- [ ] All referenced standards verified as current editions
- [ ] Samples and mock-up requirements clearly defined with approval process
- [ ] Fire strategy requirements incorporated into all relevant sections
- [ ] Sustainability and embodied carbon requirements included
- [ ] Warranty periods coordinated with contract requirements
- [ ] Lead times checked for critical materials
- [ ] Hold points and witness points defined in ITP
- [ ] O&M manual requirements specified for all maintainable elements
