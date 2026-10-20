<h1 align="center">OmniAiLab Global Registered Architect</h1>

<p align="center">
  <b>A code-routing, design-review and documentation-audit Skill for registered architects — jurisdiction first</b><br>
  29 modules: 18 professional design modules + 10 jurisdictional code packs + 7 calculators ｜ 883 reference documents ｜ ~1.13M lines of source material<br>
  Project intake → code routing → programme &amp; massing → technical coordination → performance verification → construction documents → compliance review<br>
  Codes are routed and cross-checked, never turned into approvals ｜ Zero hard dependencies, works offline ｜ Structure / fire / accessibility require a locally licensed sign-off
</p>

<p align="center">
  <a href="https://github.com/tomatoparkdao/registered-architect"><img src="https://img.shields.io/badge/version-1.1.0-1f6feb?style=flat-square" alt="version 1.1.0"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2ea043?style=flat-square" alt="license MIT"></a>
  <a href="https://www.omniailabx.com/"><img src="https://img.shields.io/badge/platform-OmniAiLab-8957e5?style=flat-square" alt="platform OmniAiLab"></a>
  <img src="https://img.shields.io/badge/jurisdictions-10-0e8a16?style=flat-square" alt="10 jurisdictions">
  <img src="https://img.shields.io/badge/modules-29-0969da?style=flat-square" alt="29 modules">
  <img src="https://img.shields.io/badge/works%20with-Codex_%7C_Claude_%7C_WorkBuddy_%7C_OmniAiLab-6f42c1?style=flat-square" alt="works with Codex / Claude / WorkBuddy / OmniAiLab">
</p>

<p align="center">
  <a href="README.md">简体中文</a>　｜　<b>English</b>
</p>

> © OmniAiLab ｜ Developer: Mochiball ｜ OmniAiLab Global Registered Architect (omniailabx.com) — unauthorised copying, distribution or redistribution is prohibited.

This is not a massing generator. It is a **code-routing framework that establishes which jurisdiction you are in before it answers anything**. Its first move is not drawing — it is determining which country, which city, and which tier of mandatory standards govern the project. If that cannot be established, it lists the gaps instead of borrowing another country's numbers and carrying on.

The same massing study meets a different review in Dubai, Munich and Singapore: Dubai looks at Civil Defence pre-approval and façade cladding, Munich at the Brandschutznachweis and the state LBO, Singapore at the SCDF Fire Code together with ETTV/RTTV. This Skill turns that divergence into **routable structure** — regulator, code hierarchy and mandatory tier first, then scheme, technology, fire, accessibility, energy and documentation.

**It is the code map and cross-check list in a registered architect's hands, not a replacement for the architect.**

## At a Glance

| Item | Value | Notes |
|---|---|---|
| Skill name | `registered-architect` | The unique identifier, lowercase with hyphens; tools with native Skill support call it directly, others can trigger it with a plain-language description |
| Display name | OmniAiLab Global Registered Architect | The name shown in the repo and documents; not the same thing as the callable name |
| Version | v1.1.0 | Kept in sync with `SKILL.md` and `.claude-plugin/plugin.json`; jurisdictional packs reached clause-level precision from v1.1.0 |
| Positioning | Code routing and design-review framework for registered architects | **Not a chief designer, not a design-generation tool, not a rendering engine**; it produces judgments, checklists and open items |
| Publisher / developer | OmniAiLab ／ Mochiball | Attribution and copyright as stated at the end of this file and in [LICENSE](LICENSE) |
| License | MIT | Free to use, modify and redistribute with the copyright and license notice retained |
| Repository | [tomatoparkdao/registered-architect](https://github.com/tomatoparkdao/registered-architect) | Public; `git clone` for the complete module, reference and script set |
| Requirements | Python 3.9+ (calculators only) | The seven calculators use only `argparse` / `json` / `math` / `sys`; the knowledge base reads offline with no network |
| Scale | 29 modules ／ 883 reference documents ／ ~1.13M lines | Mainland China alone contributes 848 documents (426 code and atlas entries plus 414 text fragments), the deepest pack of the ten |

## Scope: What It Does and Refuses

One table decides whether a task belongs here.

| Fit | Detail |
|---|---|
| **Fits · Jurisdiction and code routing** | Given address, occupancy, height, area, fire-hazard class and design stage, it determines the applicable mandatory tier, the authority having jurisdiction, and which local supplements apply. Ten jurisdiction packs, each standalone and mutually comparable |
| **Fits · Scheme and technical judgment** | Programming, area schedules, adjacencies, massing comparison, core and grid, envelope build-ups, structural system selection, MEP coordination, daylight and shading, room acoustics, material strategy — options with reasoning and trade-offs, not a single hand-waved answer |
| **Fits · Compliance cross-check** | Fire compartments, travel distance, egress width, accessible routes, energy targets, daylight and separation: each item lists the edition adopted, the clause relied on, local deviations and questions for the AHJ |
| **Fits · Documentation and review** | Drawing organisation, layers and line weights, annotation systems, LOD, BIM coordination, specification text, RFI/ASI, closeout and O&M records |
| **Does not fit · Approvals and sealed conclusions** | Building permits, fire-review opinions, structural seals, energy certification, accessibility certification. Output must never be described as any of these |
| **Does not fit · Final structural safety determination** | Span guidance, load paths and preliminary sections are in scope; final sections, reinforcement and seismic detailing require a structural engineer's review against current standards. Rules of thumb must never be presented as mandatory clauses |
| **Does not fit · Cross-border number transplants** | Lifting a limit from one country into another is the single most common source of error. Across jurisdictions, compare "metric — edition — applicability"; never substitute equivalent values |

## Quick Start

The entry point is [SKILL.md](SKILL.md). Once installed, stating the project context plainly in your first message matters more than any prompt trick.

```bash
# Option 1 — mount directly as a Claude Code plugin
claude --plugin-dir "/path/to/registered-architect"

# Option 2 — copy into your host agent's skills directory (use your tool's real path)
cp -R registered-architect ~/.claude/skills/registered-architect
cp -R registered-architect ~/.codex/skills/registered-architect
cp -R registered-architect ~/.workbuddy/skills/registered-architect

# Option 3 — read-only reference, no installation
git clone https://github.com/tomatoparkdao/registered-architect.git
```

When copying into an existing project, **keep the entire `skills/` tree intact**: once the relative links between modules, references, templates and calculators break, routing collapses.

Five items in the first message save a round of questions:

```text
Jurisdiction: Dubai, UAE
Occupancy and size: hotel, 18 storeys, 32,000 m2 above grade, podium F&B
Stage: design development, preparing for Civil Defence pre-approval
Known constraints: 6 m setback, 75 m height cap, developer facade-coverage requirement
Task: review egress and accessible routes, list items for Civil Defence confirmation
```

## How It Works: Three Layers of Progressive Loading

Nothing is loaded up front. The name and description stay resident, module bodies load on demand, references and scripts only when explicitly needed — the only way to navigate 883 documents without drowning the context.

| Layer | Loaded content | Trigger | Typical size |
|---|---|---|---|
| Layer 0 | Skill name and description | Always visible, used to decide whether this task belongs here | Tens of lines |
| Layer 1 | The module's `SKILL.md` body | Loaded when a task type matches; carries method, criteria and red lines | 400–600 lines |
| Layer 2 | Documents under `references/`, templates, `scripts/` calculators | Read only when specific clauses, tables, build-ups or numbers are needed | Per file |

The routing order is fixed. Skipping a step produces errors:

```text
Input (address / occupancy / area / stage)
        │
        ▼
geographic-foundations ── country, city, code number, currency, climate, material systems
        │
        ├─ identified ──► skills/country-<jurisdiction>/SKILL.md   tiers, AHJ, review path
        │
        └─ not identified ──► fall back to IBC / Eurocodes / ASCE / ISO references,
        │                     and require the user to confirm jurisdiction (never guess)
        ▼
Select the professional module ── design / technical / compliance / documentation
        │
        ▼
Output: applicable constraints → design response → evidence and edition → open items → owner
```

## Modules (29)

18 professional modules, 10 jurisdictional packs, one calculator set. The `references/` count shows how deep each module can reach.

| # | Module | Layer | What it covers |
|---|---|---|---|
| 1 | `architect-foundations` | Base | Architect and theorist matrix (Vitruvius to Kéré), quantitative rules of thumb, 28 building subtypes, design-quality framework, five anti-pattern families, module routing |
| 2 | `geographic-foundations` | Base | Identifies jurisdiction from country, city, code number, currency, climate and material systems, then routes; falls back to international references and asks for confirmation rather than assuming |
| 3 | `design-theory` | Design | Architectural history, movements, manifestos, design philosophy, formal language, critical regionalism, phenomenology, design criticism; separates historical fact, theoretical reading and project advice |
| 4 | `concept-design` | Design | Concept generation, massing studies, solar envelope, wind comfort, view corridors, shadow impact, contextual height, FAR/GFA optimisation, naturally ventilated massing |
| 5 | `building-programming` | Design | Briefs, area standards, adjacency matrices, flow diagrams, occupant capacity, equipment schedules, zoning and capacity checks; areas are planning inputs requiring client and code verification |
| 6 | `building-typology` | Design | Residential, office, hotel, retail, schools, hospitals, libraries, theatres, sports, industrial and mixed-use: spatial organisation, typical floors, circulation, daylight, structure, operations |
| 7 | `spatial-planning` | Design | Cores, vertical transport, public and service circulation, floor efficiency, back-of-house, loading, parking, restrooms, plant rooms, shafts, egress; plans must also pass accessibility, fire and structural grid checks |
| 8 | `building-envelope` | Technical | Brick and concrete walls, curtain walls, double skins, timber walls, metal panels, insulation, air and water tightness, glazing, spacers, coatings, dynamic glass; judged against climate, orientation, humidity and whole-life carbon |
| 9 | `structural-systems` | Technical | Concrete, steel, timber, masonry, precast, cable-stayed, space frame, shell and composite spans and detailing; **never size members from a rule-of-thumb table** — the engineer of record confirms |
| 10 | `building-services` | Technical | Natural and mixed-mode ventilation, VAV/VRF, chilled beams, heat pumps, heat recovery, plumbing, rainwater, fire water, electrical, lighting, low voltage, BMS, plant rooms, rooftop equipment, MEP coordination |
| 11 | `daylighting-design` | Technical | DF, sDA, ASE, UDI, VLT, SHGC, solar altitude and azimuth, shading geometry, daylight atria, sawtooth roofs; simulations must state weather file, timestep and occupancy assumptions |
| 12 | `acoustic-design` | Technical | Wall and floor separation, window acoustics, impact sound, flanking transmission, equipment noise, reverberation time, clarity, spaciousness, isolation, variable acoustics; junctions, perforations, doors and workmanship matter as much as the specification |
| 13 | `material-selection` | Technical | Compares materials on performance, regulation, durability, maintenance, cost, embodied carbon, recyclability, supply chain, workmanship and appearance; product data never replaces samples, testing and supplier confirmation |
| 14 | `building-codes` | Compliance | IBC occupancy groups and Type I–V construction, height and area limits, egress, fire separation, plumbing fixture counts, plus IBC / Building Regulations / Eurocodes / NCC / NBC comparison |
| 15 | `fire-life-safety` | Compliance | Occupant load, exit count, travel distance, stairs and corridors, fire lifts, compartments, smoke control, detection, sprinklers, fire lanes, refuge areas; state the edition and local amendments |
| 16 | `accessibility-design` | Compliance | ADA, ISO, EN, BS, DIN, AS, GB and BCA comparison; continuous accessible routes, doors, ramps, lifts, restrooms, parking, tactile, auditory and cognitive support |
| 17 | `building-sustainability` | Compliance | Passive design, energy modelling, operational and embodied carbon, water, materials, health, ecology, certification; LEED, BREEAM, WELL, Green Star, NABERS, DGNB, CASBEE thresholds shift, so confirm the version first |
| 18 | `construction-documentation` | Delivery | Drawing indexes, layers and line weights, annotation and symbols, hatching, revision clouds, LOD, BIM coordination, specifications, RFI/ASI, mock-ups, site testing, closeout, warranties, O&M |
| 19 | `architect-calculator` | Tooling | Seven standard-library calculators: area density, U-value, daylight factor, egress, structural load, energy, cost |

How the references are layered (Markdown files under `references/`, excluding each module's own `SKILL.md`):

| Location | Documents | What lives there |
|---|---|---|
| `skills/*/references/` (18 professional modules) | 35 | One to four topical references per module: ADA and accessibility systems, room acoustics, envelope build-ups, case libraries, calculation methods. `architect-foundations` is the thickest at four |
| `skills/country-china/references/standards/` | 426 | Chinese code and atlas entries: GB mandatory codes, JGJ industry standards, local DB rules and national drawing atlases, named by code number for clause-level lookup |
| `skills/country-china/references/standards/text/` | 414 | Body-text fragments of those entries for clause citation and cross-search; unrecognised scans are flagged separately and never quoted as clauses |
| Other nine jurisdictions | 0 each | Single-file packs: everything sits in each jurisdiction's own `SKILL.md`, with no secondary unpacking |
| **Total** | **883** | Read as layer 2 on demand, never injected into context all at once |

## Ten Jurisdictions

One pack per jurisdiction, stating the regulatory model, code hierarchy, authorities and review focus. **Across jurisdictions you compare; you never substitute.**

| Jurisdiction | Regulatory model | Core codes | Review focus |
|---|---|---|---|
| China | Centralised national control with mandatory clauses (type D) | GB 50352-2019, GB 50016-2014 (2018 ed.), GB 50011-2010 (2016 amend.), GB 55015-2021, GB 50189-2015, GB 50763-2012, JGJ series, local DB standards | Mandatory vs. recommended standards, sunlight-spacing rights, energy rules across five thermal zones, seismic intensity 6–9; **Hong Kong and Macao are handled separately**, never under mainland rules |
| United States | Model codes adopted state by state, city by city | IBC 2024, IRC, IECC 2024, IFC, NFPA 101, NFPA 70, ADA 2010, ANSI A117.1, ASCE 7-22, ACI 318, AISC 360, AWC NDS | State amendments diverge sharply (CA Title 24, NYC, FL HVHZ, Chicago, MA, WA); AHJ interpretation outranks the printed clause |
| United Kingdom | Central regulations, local enforcement, duty-holder chain rebuilt in 2022 | Building Regulations 2010 and Approved Documents A–S, Building Safety Act 2022, BSR/HRB regime, BS 9991, BS 9999, BS 8300, NPPF, London Plan | Accountable Person and Golden Thread evidence for higher-risk buildings; Scotland, Wales and Northern Ireland are not copies of England |
| Germany | Federal framework act plus 16 state building codes | MBO, BauGB, BauNVO, GEG 2023, DIN 18040, DIN 4109, DIN 4108, DIN 4102 / EN 13501, Eurocodes with national annexes | Sonderbau special buildings, Brandschutznachweis fire proof, DGNB, BAFA/KfW subsidies and Passivhaus stacked on top |
| Japan | National act, local ordinances, private evaluation bodies | Building Standards Act, Fire Service Act, City Planning Act, Heart Building Law, AIJ recommendations, BCJ structural evaluation, CASBEE | Zoning, FAR and building coverage, shadow and slant-line limits, fire zones, two-tier seismic design; planning clauses often constrain massing before architecture does |
| Singapore | Concentrated but split across BCA, SCDF and URA | Building Control Act, BCA Regulations, SCDF Fire Code 2018, BCA Code on Accessibility, Green Mark 2021, URA Master Plan, SS EN Eurocodes | ETTV/RTTV envelope targets, fire egress and maintainability, master-plan compliance; confirm each authority separately |
| Australia | NCC nationally, planning and approval by state | NCC 2022 Vol 1–3, AS/NZS 1170 series, AS 3600, AS 4100, AS 1684, AS 1428.1-2021, AS 5113, NatHERS 7-star, BASIX, Green Star, NABERS | Performance Solutions vs. Deemed-to-Satisfy, state approval differences, bushfire / cyclone / flood overlay, wind regions A–D |
| India | National codes plus state and municipal development control | NBC 2016, ECBC 2017, IS 456, IS 800, IS 875, IS 1893, IS 13920, state DCRs, RERA, EIA, CRZ, GRIHA, IGBC | Development control (FAR, setbacks, parking) is decided jointly by national codes and state or municipal rules; prepare to the stricter one |
| UAE | Emirate-specific regimes; Dubai and Abu Dhabi differ | Dubai Building Code 2021, ADIBC, UAE Fire & Life Safety Code 2018, Dubai Universal Design Code, Estidama, Al Sa'fat | High-rise and façade cladding fire performance, refuge floors, Civil Defence pre-approval, developer design guidelines that often exceed statutory minima |
| Saudi Arabia | National Building Code plus giga-project jurisdictions | SBC 201 series, SBC 801, Saudi Universal Accessibility Code, Mostadamah, Amana approval | NEOM, Qiddiya, the Red Sea, Diriyah, AlUla, RCRC, Makkah and Madinah may each run their own review path; one SBC pass is not enough |

## Seven Calculators

Early-stage and cross-check use only. **Numbers for submission must be recomputed by a licensed professional against the current code.** All scripts use the Python standard library alone.

| Script | Computes | Key arguments | Used for |
|---|---|---|---|
| `area_calculator.py` | Development density: GFA, net area, units, population, parking | `--site-area` `--far` `--ntg-ratio` `--avg-unit-size` `--persons-per-unit` `--parking-ratio` | Site acquisition and early-stage capacity checks |
| `uvalue_calculator.py` | Assembly U-value from layered build-ups | `--layers` `--facade` `--rsi-internal` `--rsi-external` | Energy-code benchmarking, build-up comparison |
| `daylight_calculator.py` | Daylight factor estimate | `--room-width/depth/height` `--window-width/height/sill-height` `--glazing-transmittance` `--average-reflectance` | Compliance pre-check for classrooms, offices, dwellings |
| `egress_calculator.py` | Egress width and exit count | `--floor-area` `--occupancy-type` `--sprinklered` `--num-stories` | Core and stair count decisions at scheme stage |
| `structural_load_calculator.py` | Load take-down and preliminary member sizing | `--tributary-area` `--num-floors` `--dead-load` `--live-load` `--occupancy-type` | Order-of-magnitude grid and slab depth |
| `energy_calculator.py` | Energy intensity estimate | `--floor-area` `--envelope-area` `--average-u-value` `--heating/cooling-degree-days` `--ventilation-rate` `--internal-gains` | Comparing energy strategies at scheme stage |
| `cost_calculator.py` | Order-of-magnitude cost | `--gfa` `--building-type` `--quality` `--region` `--include-external` | Budget conversations and option selection |

```bash
# Human-readable summary
python skills/architect-calculator/scripts/area_calculator.py \
  --site-area 5000 --far 2.5 --ntg-ratio 0.82

# Add --json for piping and record-keeping
python skills/architect-calculator/scripts/egress_calculator.py \
  --floor-area 1800 --occupancy-type business --sprinklered --num-stories 12 --json
```

## Six-Stage Workflow

| Stage | Input | Action | Output |
|---|---|---|---|
| 1 Intake | Address, site boundary, survey, programme, areas, storeys, budget, schedule, client goals, operating model | Collect and check the basics; log unknowns as assumptions instead of guessing | Project summary + assumption schedule |
| 2 Code routing | Stage 1 summary | Identify authorities and code tiers; separate mandatory requirements, guidance, developer requirements, certification criteria and client preference | Route table + conflict priority + open-items list |
| 3 Programme and massing | Routing outcome | Area schedule, adjacency matrix, circulation; massing options checked simultaneously against daylight, views, wind, fire, accessibility, structure and buildability | Area schedule + adjacency matrix + massing comparison |
| 4 Technical coordination | Selected massing | Fix structural grid, slab depths, core, shafts, plant rooms, envelope systems, vertical transport, fire systems, shading, maintenance routes | Coordination list + interface register |
| 5 Performance verification | Technical scheme | Area, U-value, daylight, egress, loading, energy, acoustic, carbon and cost checks at the appropriate stage — labelled by who produced them | Performance table (calculator / simulation / engineer review in separate columns) |
| 6 Delivery | All upstream conclusions | Drawings, models, schedules, specifications, material schedules, performance notes, submission documents, risk register; every revision keeps version, date, reason, owner | Deliverable pack + revision log |

## Review Output Templates

### Project summary

```text
Project:
Location:            country / state or province / city / special jurisdiction
Authorities:         AHJ, civil defence, planning, fire (list separately)
Occupancy and class:
Site area / GFA / storeys / height:
Stage:               scheme / design development / construction documents / submission
Codes and editions:  code number + edition + verification date
```

### Key assumptions

| ID | Assumption | Area of impact | Confirmed by | Status |
|---|---|---|---|---|
| A-01 | Site boundary and survey are accurate | Massing, areas, setbacks, fire lanes | Client / surveyor | Open |
| A-02 | Occupancy class and operating model are fixed | Fire class, occupant load, equipment loads | Client / architect | Open |
| A-03 | Current editions of codes are adopted | Validity of every compliance conclusion | Architect / AHJ | Open |
| A-04 | Structural and MEP consultants are engaged | Grid, floor-to-floor, shafts, plant rooms | Project manager | Open |

### Constraints and responses

| Constraint | Content | Design response | Evidence or open item |
|---|---|---|---|
| Planning | Height, setbacks, FAR / plot ratio, coverage | Massing control and floor allocation | Planning permit, zoning clauses, height limits |
| Fire | Occupant load, exits, fire resistance, sprinklers | Compartmentation and egress strategy | Code clauses + AHJ pre-approval comments |
| Accessibility | Continuous routes, ramps, lifts, restrooms | Universal design routes and junction details | Accessibility code edition + measured site conditions |
| Environmental | Daylight, energy, thermal performance, carbon | Envelope and systems strategy | Simulation report, energy-code limits, certification criteria |
| Structural | Wind, seismic, snow, loads | Structural system and grid | Structural engineer's review |
| Construction | Site, lifting, materials, programme | Phasing and junction design | Contractor and method statements |

### Risk register

| Risk | Probability | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Code edition changes | Medium | High | Record verification date, monitor, re-confirm before submission | Architect |
| Ambiguous local interpretation | Medium | High | Submit pre-application enquiries early, keep written answers | Project manager |
| Uncoordinated critical dimensions | Medium | Medium | Cross-discipline model review and clash detection | BIM lead |
| Material supply or performance shortfall | Medium | Medium | Pre-approve alternates and suppliers, keep equivalence evidence | Materials consultant |
| Insufficient maintenance access | Low | High | Maintainability review, verify equipment replacement routes | MEP consultant |

## Example Prompts

```text
Compare three massing options for a 12-storey residential block at 40 degrees north,
covering daylight, wind, structure and fire implications.

Review this hotel's egress and accessible-route strategy against the Singapore SCDF Fire Code
and BCA Code on Accessibility; cite clause numbers, give a verdict per item, and name the
authority to confirm each open question.

Produce an area schedule, adjacency matrix, core options and preliminary grid for a 5,000 m2 office.

Compare double glazing, triple glazing and dynamic glass on U-value, SHGC, VLT, cost and
whole-life impact.

Build an envelope, BREEAM, acoustic and construction-documentation checklist for a UK project.

Verify occupancy classification, fire separation, parking, FAR and accessibility under India's
NBC, and list what must be confirmed with the authority.

Use the calculators to estimate U-values, egress capacity, structural loads and preliminary cost
for a 2,000 m2 building, and state every assumption behind the numbers.
```

## Deliverable Naming

A fixed prefix keeps the review chain traceable; the order is the work order.

| File | Content | Audience |
|---|---|---|
| `01_project-brief.md` | Project summary, key assumptions, stage | Client, project manager |
| `02_code-route.md` | Jurisdiction determination, code tiers, editions, verification dates | Architect, AHJ |
| `03_program.md` | Programme, area schedule, adjacencies | Client, operator |
| `04_concept-options.md` | Concept, massing comparison, environmental response | Client, design review |
| `05_performance.md` | Environmental, structural, fire and accessibility performance | Specialist consultants |
| `06_materials.md` | Envelope and material strategy, equivalence evidence | Materials consultant, contractor |
| `07_documentation.md` | Drawings, specifications, BIM coordination | Contractor, reviewer |
| `08_review-log.md` | Review comments, RFI, ASI, decision record | Whole project team |

## Repository Layout

```text
registered-architect/
├── SKILL.md                          # Entry point: principles, module guide, deliverables
├── README.md                         # Chinese README (default)
├── README_EN.md                      # English README
├── LICENSE                           # OmniAiLab MIT License
├── .claude-plugin/plugin.json        # Plugin metadata and keywords
└── skills/
    ├── architect-foundations/        # Auto-loaded base layer
    ├── geographic-foundations/       # Jurisdiction detection and routing
    ├── design-theory/  concept-design/  building-programming/
    ├── building-typology/  spatial-planning/
    ├── building-envelope/  structural-systems/  building-services/
    ├── daylighting-design/  acoustic-design/  material-selection/
    ├── building-codes/  fire-life-safety/  accessibility-design/
    ├── building-sustainability/  construction-documentation/
    ├── architect-calculator/         # Seven scripts plus calculation references
    └── country-{china,usa,uk,germany,japan,singapore,australia,india,uae,saudi-arabia}/
        ├── SKILL.md                  # Jurisdiction pack body
        └── references/standards/     # China: 426 code and atlas entries + 414 text fragments
```

## Limits of Responsibility

This line has to be explicit, or every recommendation gets misread as a conclusion.

| Matter | What this Skill can do | Who must confirm finally |
|---|---|---|
| Code applicability and clause location | Determine jurisdiction, list code tiers, locate clauses, flag editions and local deviations | The AHJ and the registered architect of record |
| Fire and life safety | Travel distance, exit count, compartmentation strategy, smoke control and detection recommendations | Fire authority plus a locally qualified fire engineer |
| Structural safety | System selection, span guidance, load paths, preliminary calculations | Structural engineer, reviewed and sealed against current standards |
| Accessibility | Route, ramp, lift and restroom compliance comparison | Accessibility reviewer and the architect of record |
| Energy and certification | Target pre-check, envelope and systems strategy, criteria comparison | Energy consultant and certification body (LEED / BREEAM / Green Mark, etc.) |
| Cost | Order-of-magnitude estimate and option comparison | Cost consultant and the client's budget decision |
| Drawings and construction documents | Drawing organisation, layers and annotation, LOD, coordination lists | Internal design review + the construction-document review authority |

When input is insufficient it lists the gaps instead of assuming critical conditions. When codes are uncertain it states the edition, the basis for the reading, likely local deviations, and the questions to put to the AHJ, planning or fire authority.

## Common Failure Modes

| Failure | Consequence | Correct approach |
|---|---|---|
| Applying one country's numeric limits in another | The whole scheme collapses at submission | Route the jurisdiction first; compare metric and applicability, never substitute values |
| Using an outdated edition without a verification date | Conclusions are untraceable and liability is undefined | Every conclusion carries code number + edition + verification date |
| Presenting rules of thumb as mandatory clauses | Misleads client and contractor, creates closeout risk | Label experience values as guidance; mandatory requirements must cite clause numbers |
| Optimising plan area while ignoring fire, structure, MEP and maintenance space | Late rework; the core and shafts no longer fit | Run all four discipline checks from scheme stage |
| Comparing capital cost only | Whole-life cost ends up higher | Compare across the life cycle, including maintenance and replacement |
| Giving conclusions without assumptions | Nothing can be verified or defended | Attach assumptions, evidence and open items to every judgment |
| Describing AI output as a seal, approval or certification | Legal and professional liability | Distinguish recommendation / verification / approval / certification at all times |

## FAQ

| Question | Answer |
|---|---|
| Is it China-only? | No. Ten jurisdiction packs, China being one of them and the deepest (848 documents). With no clear jurisdiction it falls back to international references and asks you to confirm. |
| Can calculator output go straight into a submission? | No. Calculators support early design and cross-checking; submission values must be recomputed and signed by a licensed professional against the current code. |
| What if the city has no dedicated code? | It states the gap, uses the next tier up as a provisional reference, and lists the questions to put to the AHJ or local planning authority. |
| Can it compare codes across countries? | Yes, provided the comparison names the metric, the edition, the scope, and the parts that cannot be equated. |
| Does it need network access or external software? | No. Knowledge base, templates and calculators all work offline; CAD, BIM, rendering and analysis tools are optional integrations, not dependencies. |
| Is its output a design deliverable? | It is supporting material for design judgment and review — not a sealable construction document, and not an approval. |

## Scale

| Item | Count | Notes |
|---|---|---|
| Professional modules | 18 | Spanning base, design, technical, compliance and delivery layers |
| Jurisdiction packs | 10 | China, USA, UK, Germany, Japan, Singapore, Australia, India, UAE, Saudi Arabia |
| Calculators | 7 | Standard library only; `--json` for records |
| Reference documents | 883 | Including 848 for mainland China: 426 code and atlas entries + 414 text fragments |
| Knowledge base | ~1.13M lines of Markdown | 919 files, module bodies plus references |
| Architects and theorists | 50+ | Vitruvius to Kéré, with representative works and applicable context |
| Architectural movements | 20+ | Modernism, postmodernism, critical regionalism, parametricism, phenomenology and more |
| Building types | 28+ | Residential, commercial, institutional, industrial, special subtypes |
| Structural systems | 15+ | Concrete, steel, timber, masonry, precast, cable, space frame, shell, composite |
| Sustainability schemes | 8+ | LEED, BREEAM, WELL, Green Star, NABERS, DGNB, CASBEE, Estidama, Mostadamah |
| Reference cases | 100+ | For precedent analysis and detailing comparison |
| Dimensions and rules of thumb | 200+ | Floor-to-floor, grids, efficiency, corridors, parking, lifts, fire resistance |

## Version History

| Version | Change | Impact |
|---|---|---|
| v1.1.0 | Jurisdiction packs upgraded to clause-level precision (code numbers, edition years, local amendments, review paths); China code and atlas fragment library added | Jurisdiction routing and clause location |
| v1.0.0 | Framework release: 18 professional modules + 10 jurisdictions + 7 calculators | Everything |
| OmniAiLab edition | Unified metadata, MIT license, attribution and delivery boundaries; natural-language transition with code numbers, paths and identifiers preserved | Documentation and metadata |

## License and Attribution

Released under the **MIT License**; see [LICENSE](LICENSE). Free to use, modify and redistribute with the copyright and license notice retained.

- Publisher: OmniAiLab
- Developer: Mochiball
- Platform: [omniailabx.com](https://www.omniailabx.com/)
- Repository: [tomatoparkdao/registered-architect](https://github.com/tomatoparkdao/registered-architect)

Code references support design judgment only. Any numeric limit, clause citation or compliance conclusion must be verified against the mandatory national standards, local standards and authority requirements in force where the project sits, and reviewed and signed by a locally licensed professional.

---
> © OmniAiLab ｜ Developer: Mochiball ｜ OmniAiLab Global Registered Architect (omniailabx.com) — unauthorised copying, distribution or redistribution is prohibited.
