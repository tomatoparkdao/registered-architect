# Drawing Standards Reference

Comprehensive reference for architectural drawing standards covering CAD
layer conventions, BIM standards, sheet sizes, title blocks, revision
management, issue status codes, markup conventions, and coordination checks.

---

## 1. AIA CAD Layer Guidelines

### 1.1 Layer Naming Convention

The AIA CAD Layer Guidelines (based on the U.S. National CAD Standard)
use a structured naming format:

```
Discipline - Major Group - Minor Group (optional) - Status (optional)
```

**Format**: `A-WALL-FULL-N` where:
- `A` = Discipline designator
- `WALL` = Major group (4 characters)
- `FULL` = Minor group (4 characters, optional)
- `N` = Status code (optional)

### 1.2 Discipline Designators

| Code | Discipline                |
|------|--------------------------|
| A    | Architectural            |
| C    | Civil                    |
| E    | Electrical               |
| F    | Fire Protection          |
| G    | General                  |
| H    | Hazardous Materials      |
| I    | Interiors                |
| L    | Landscape                |
| M    | Mechanical               |
| O    | Operations               |
| P    | Plumbing                 |
| Q    | Equipment                |
| R    | Resource                 |
| S    | Structural               |
| T    | Telecommunications       |
| X    | Other Disciplines        |
| Z    | Contractor/Shop Drawings |

### 1.3 Standard Architectural Layers

| Layer Name        | Description                              | Color | Line Weight |
|-------------------|------------------------------------------|-------|-------------|
| A-WALL            | Walls -- general                         | 4     | 0.50mm      |
| A-WALL-FULL       | Full-height walls                        | 4     | 0.50mm      |
| A-WALL-PRHT       | Partial-height walls                     | 4     | 0.35mm      |
| A-WALL-PATT       | Wall hatching/patterns                   | 8     | 0.13mm      |
| A-DOOR            | Doors                                    | 3     | 0.35mm      |
| A-DOOR-IDEN       | Door identification tags                 | 7     | 0.25mm      |
| A-GLAZ            | Windows and glazing                      | 3     | 0.35mm      |
| A-GLAZ-IDEN       | Window identification tags               | 7     | 0.25mm      |
| A-FLOR            | Floor information                        | 3     | 0.25mm      |
| A-FLOR-PATT       | Floor patterns/finishes                  | 8     | 0.13mm      |
| A-CLNG            | Ceiling information                      | 5     | 0.25mm      |
| A-CLNG-GRID       | Ceiling grid                             | 8     | 0.13mm      |
| A-ROOF            | Roof outline                             | 4     | 0.35mm      |
| A-ROOF-PATT       | Roof hatching                            | 8     | 0.13mm      |
| A-COLS            | Columns                                  | 5     | 0.50mm      |
| A-STRS            | Stairs                                   | 3     | 0.35mm      |
| A-ELEV            | Elevators                                | 3     | 0.35mm      |
| A-FURN            | Furniture                                | 8     | 0.18mm      |
| A-EQPM            | Equipment                                | 8     | 0.18mm      |
| A-ANNO-DIMS       | Dimensions                               | 1     | 0.18mm      |
| A-ANNO-TEXT       | Text annotations                         | 7     | 0.18mm      |
| A-ANNO-NOTE       | General notes                            | 7     | 0.18mm      |
| A-ANNO-SYMB       | Symbols (section marks, tags)            | 7     | 0.25mm      |
| A-ANNO-TTLB       | Title block                              | 7     | 0.35mm      |
| A-AREA-IDEN       | Area identification                      | 2     | 0.18mm      |
| A-DETL            | Detail components                        | 4     | 0.35mm      |
| A-GRID            | Column grid lines                        | 8     | 0.13mm      |
| A-GRID-IDEN       | Grid identification bubbles              | 7     | 0.25mm      |

### 1.4 Status Codes

| Code | Meaning                                |
|------|----------------------------------------|
| D    | Demolition (existing to be removed)    |
| E    | Existing to remain                     |
| F    | Future work (not in current contract)  |
| M    | Items to be moved                      |
| N    | New work                               |
| T    | Temporary work                         |

---

## 2. BIM Standards

### 2.1 BS 1192 / ISO 19650

BS 1192 (superseded by ISO 19650) establishes the framework for managing
information over the whole life cycle of a built asset using BIM.

**Key principles:**
- Common Data Environment (CDE) for all project information
- Naming conventions for files, models, and documents
- Information containers organized by discipline, zone, and stage
- Status and suitability codes control information use

### 2.2 ISO 19650 Information Management Framework

| Part     | Scope                                        |
|----------|----------------------------------------------|
| 19650-1  | Concepts and principles                      |
| 19650-2  | Delivery phase of assets                     |
| 19650-3  | Operational phase of assets                  |
| 19650-5  | Security-minded approach to information management |

**Common Data Environment (CDE) States:**

| State          | Code | Description                              |
|----------------|------|------------------------------------------|
| Work in Progress| WIP | Team internal development                |
| Shared         | S1   | Suitable for coordination                |
| Shared         | S2   | Suitable for information                 |
| Shared         | S3   | Suitable for review and comment          |
| Shared         | S4   | Suitable for stage approval              |
| Published      | A1   | Authorized for construction (BEP stage)  |
| Published      | A2   | Authorized for construction              |
| Published      | AB   | As-built                                 |
| Archive        | --   | Archived/superseded                      |

### 2.3 BIM File Naming Convention (ISO 19650)

```
Project - Originator - Zone - Level - Type - Role - Classification - Number
```

Example: `PROJ-ARC-ZZ-01-DR-A-20-0001`
- PROJ = Project code
- ARC = Originator (architect firm code)
- ZZ = Applicable to all zones
- 01 = Level 01
- DR = Drawing
- A = Architecture
- 20 = Section number per classification
- 0001 = Sequential number

### 2.4 Model Coordination Procedures

1. **Federated model assembly**: Combine discipline models weekly
2. **Clash detection**: Run automated clash reports (Navisworks, Solibri)
3. **Clash resolution meetings**: Review clashes by priority (critical,
   major, minor)
4. **Model audit**: Check for compliance with BIM Execution Plan (BEP)
5. **LOD verification**: Confirm elements meet required LOD per stage
6. **Design freeze**: Lock model elements that have been coordinated

---

## 3. Sheet Size Standards

### 3.1 ISO Standard Sheet Sizes (Metric)

| Designation | Width (mm) | Height (mm) | Area (m2)  |
|-------------|-----------|-------------|------------|
| A4          | 210       | 297         | 0.0624     |
| A3          | 297       | 420         | 0.1247     |
| A2          | 420       | 594         | 0.2494     |
| A1          | 594       | 841         | 0.4996     |
| A0          | 841       | 1189        | 0.9999     |

### 3.2 ANSI/ARCH Standard Sheet Sizes (Imperial)

| Designation | Width (in) | Height (in) | Metric Approx    |
|-------------|-----------|-------------|------------------|
| ANSI A      | 8.5       | 11          | 216 x 279mm      |
| ANSI B      | 11        | 17          | 279 x 432mm      |
| ANSI C      | 17        | 22          | 432 x 559mm      |
| ANSI D      | 22        | 34          | 559 x 864mm      |
| ANSI E      | 34        | 44          | 864 x 1118mm     |
| ARCH A      | 9         | 12          | 229 x 305mm      |
| ARCH B      | 12        | 18          | 305 x 457mm      |
| ARCH C      | 18        | 24          | 457 x 610mm      |
| ARCH D      | 24        | 36          | 610 x 914mm      |
| ARCH E      | 36        | 48          | 914 x 1219mm     |
| ARCH E1     | 30        | 42          | 762 x 1067mm     |

### 3.3 Standard Practice by Region

- **North America**: ARCH D (24"x36") most common for construction sets;
  ARCH E (36"x48") for large projects; half-size prints on ARCH B (12"x18")
- **Europe/Asia**: A1 (594x841mm) most common for construction; A0 for
  large projects; A3 for field copies
- **Middle East**: Mix of A1 and ARCH D depending on project origin

---

## 4. Title Block Content

### 4.1 Required Information

Every drawing sheet must include a title block containing:

**Project Information:**
- Project name
- Project address / location
- Project number
- Owner name and contact
- Building permit number (when issued)
- Zoning/planning reference number

**Firm Information:**
- Architect firm name and logo
- Firm address and contact information
- Architect of record license number and seal
- Firm registration number

**Sheet Information:**
- Sheet number (per numbering convention)
- Sheet title
- Drawing scale(s) -- both graphic and numeric
- Date of issue
- Drawn by (initials)
- Checked by (initials)
- Approved by (initials)

**Revision Information:**
- Revision number
- Revision date
- Revision description
- Revision mark (delta or triangle with number)

**Consultant Information (if applicable):**
- Structural engineer
- Mechanical engineer
- Electrical engineer
- Civil engineer
- Other specialty consultants

### 4.2 Title Block Layout

Standard title block occupies the right side or bottom-right corner of
the sheet. Typical dimensions:

- **Right-side strip**: 75mm wide x full sheet height (ISO standard)
- **Bottom-right block**: 180mm wide x 60mm high (common alternative)
- Revision table: above or adjacent to main title block
- Issue table: below main title block information

---

## 5. Revision Management

### 5.1 Revision Numbering

- Revisions numbered sequentially: Rev 1, Rev 2, Rev 3 (or Rev A, B, C)
- Revision number resets to 1 at each new issue milestone (design stage)
  in some practices, or runs continuously in others
- Each revision must have: number, date, description, and cloud markup

### 5.2 Revision Clouds

- Revised areas enclosed in a revision cloud (irregular curved boundary)
- Cloud accompanied by a delta symbol with the revision number
- Clouds from previous revisions typically removed when a new revision
  is issued (only current revision clouds shown)
- In BIM environments, revision clouds are scheduled and tracked by Revit
  or equivalent software

### 5.3 Revision Table Format

| Rev | Date       | Description                | By  |
|-----|------------|---------------------------|-----|
| 3   | 2025-12-01 | Updated window schedule    | JD  |
| 2   | 2025-10-15 | Revised stair layout       | MK  |
| 1   | 2025-08-20 | Owner review comments      | JD  |

Most recent revision listed at top. Table typically shows last 5-6
revisions; earlier revisions noted as "See previous issues."

---

## 6. Issue Status Codes

### 6.1 Standard Issue Stages

| Code | Status                    | Description                                |
|------|---------------------------|--------------------------------------------|
| P    | Preliminary               | Work in progress, not for external use     |
| FR   | For Review                | Issued for review and comment              |
| FA   | For Approval              | Issued for client/authority approval       |
| FC   | For Construction          | Issued for construction (contract document)|
| FT   | For Tender/Bidding        | Issued for contractor pricing              |
| FI   | For Information           | Issued for reference only                  |
| FC-R | For Construction (Revised)| Revised during construction                |
| AB   | As-Built                  | Updated to reflect constructed conditions  |
| RD   | Record Document           | Final record of constructed work           |

### 6.2 Issue Management

- Each issue has a unique identifier (issue date or issue number)
- Transmittal letter accompanies every issue listing all sheets included
- Superseded sheets must be clearly marked or removed from field sets
- Digital issue management through project portals (Aconex, PlanGrid,
  BIM 360, Procore) tracks receipt and acknowledgment

---

## 7. Cloud Markup Conventions

### 7.1 Types of Markups

- **Revision clouds**: Indicate changes between issues
- **Review comments**: Preliminary markups for internal coordination
- **RFI references**: Clouds linking to RFI responses incorporated
- **ASI references**: Architect's Supplemental Instructions annotated
- **Scope change markers**: Identifying change order related modifications

### 7.2 Color Coding (Digital Review)

| Color   | Meaning                          |
|---------|----------------------------------|
| Red     | Critical issue, must address     |
| Orange  | Important comment, review needed |
| Yellow  | Minor comment or suggestion      |
| Green   | Approved or accepted             |
| Blue    | Information only                 |
| Purple  | Consultant coordination item     |

### 7.3 Markup Workflow

1. Author creates drawing and publishes to CDE as "Work in Progress"
2. Reviewer opens drawing and adds markup comments
3. Author addresses comments and updates drawing
4. Reviewer verifies changes and approves
5. Drawing moves to "Shared" status for coordination
6. After coordination, drawing moves to "Published" for construction

---

## 8. Drawing Coordination Checks

### 8.1 Internal Coordination (Architectural)

Before any issue, verify:
- Room numbers consistent across plans, RCPs, finish schedules
- Door tags match between plans and door schedule
- Window tags match between plans, elevations, and window schedule
- Section and detail references resolve to correct sheet and detail
- Elevation markers reference correct sheets
- Column grid labels consistent across all sheets
- Dimensions sum correctly (detail dims = overall dims)
- Floor-to-floor heights match between sections and plans
- Ceiling heights consistent between RCPs and sections
- Stair risers and treads comply with code and match floor heights
- Material indications consistent between plans, sections, and details

### 8.2 Interdisciplinary Coordination

Verify against consultant drawings:
- **Structural**: Column and beam locations match architectural plans;
  slab edges, openings, and depressions coordinated; structural depths
  match architectural sections
- **Mechanical**: Duct routing fits within ceiling plenum; equipment
  locations have required clearances; louver sizes match architectural
  elevations
- **Electrical**: Panel locations match architectural plans; light fixture
  layout matches RCP; outlet heights per architectural interior elevations
- **Plumbing**: Fixture locations match architectural plans; floor drains
  at correct locations; pipe chases sized adequately
- **Fire Protection**: Sprinkler heads coordinated with ceiling layout;
  fire-rated walls continuous through all drawings; smoke/fire dampers
  at rated wall penetrations
- **Civil**: Building footprint matches site plan; finish floor elevation
  matches grading plan; utility connections coordinated

### 8.3 Automated Coordination Tools

- **Navisworks Manage**: Federated model clash detection
- **Solibri Model Checker**: Rule-based model checking
- **BIMcollab**: Cloud-based BCF issue management
- **Revit Interference Check**: Built-in clash detection within Revit
- **Bluebeam Revu**: PDF overlay comparison for 2D coordination
- **AutoCAD DWG Compare**: Automated drawing comparison tool

### 8.4 Coordination Checklist by Phase

**Schematic Design Issue:**
- Building footprint and overall dimensions verified
- Floor-to-floor heights confirmed with structural and MEP
- Major vertical penetrations (stairs, elevators, shafts) located
- Preliminary code compliance verified

**Design Development Issue:**
- All rooms numbered and named
- All doors and windows tagged
- Structural grid finalized and coordinated
- MEP space requirements confirmed
- Ceiling heights established and verified
- Wall types assigned and rated walls identified

**Construction Document Issue:**
- All annotation complete (dimensions, keynotes, tags)
- All schedules complete and cross-referenced
- All details drawn and referenced
- All specification sections written and cross-referenced
- Clash detection run and issues resolved
- Code compliance fully documented
- Accessibility compliance verified
- QA/QC review by senior architect completed
