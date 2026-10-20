<h1 align="center">OmniAiLab Global Registered Architect</h1>

<p align="center">
  <b>A code-routing, design-review and documentation-audit Skill for registered architects — jurisdiction first</b><br>
  29 modules: 18 professional design modules + 10 jurisdictional code packs + 1 calculator module (7 scripts) ｜ 883 reference documents ｜ ~1.13M lines of source material<br>
  Project intake → code routing → programme &amp; massing → technical coordination → performance verification → construction documents → compliance review<br>
  Codes are routed and cross-checked, never turned into approvals ｜ Zero hard dependencies, works offline ｜ Structure / fire / accessibility require a locally licensed sign-off
</p>

<p align="center">
  <a href="https://github.com/tomatoparkdao/registered-architect"><img src="https://img.shields.io/badge/version-1.1.0-1f6feb?style=flat-square" alt="version 1.1.0"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2ea043?style=flat-square" alt="license MIT"></a>
  <a href="https://www.omniailabx.com/"><img src="https://img.shields.io/badge/platform-OmniAiLab-8957e5?style=flat-square" alt="platform OmniAiLab"></a>
  <a href="https://discord.gg/vdgTEpXMh3"><img src="https://img.shields.io/badge/community-Discord-5865f2?style=flat-square" alt="community Discord"></a>
  <img src="https://img.shields.io/badge/jurisdictions-10-0e8a16?style=flat-square" alt="10 jurisdictions">
  <img src="https://img.shields.io/badge/modules-29-0969da?style=flat-square" alt="29 modules">
  <img src="https://img.shields.io/badge/works%20with-Codex_%7C_Claude_%7C_WorkBuddy_%7C_OmniAiLab-6f42c1?style=flat-square" alt="works with Codex / Claude / WorkBuddy / OmniAiLab">
</p>

<p align="center">
  <a href="README.md">简体中文</a>　｜　<b>English</b>
</p>

> © OmniAiLab ｜ Developer: Mochiball ｜ OmniAiLab Global Registered Architect (omniailabx.com) — unauthorised copying, distribution or redistribution is prohibited.

It does not draw the scheme, and it does not sign for you. **The first thing it does is establish which tier of mandatory standards governs the project**: address, use, height, area and design stage decide the jurisdiction and the authority, then the code hierarchy is traced down to clause level, and only then does the work move on to programme and massing, technical coordination, performance verification, construction documents and compliance review. At the end of every step you only answer "continue" or "not this one". One Skill covering 10 jurisdictions, 18 professional capabilities and 7 calculators, writing "where this number comes from, which edition, verified when" into every conclusion, so a design judgement becomes a record that can be traced, checked and handed to a reviewer.

| Item | Value | Notes |
|---|---|---|
| Module system | 29 modules / 883 reference documents | 18 professional design capabilities + 10 jurisdictional code packs + `architect-calculator` (7 scripts inside); the China pack alone holds 848 documents, 96% of all references |
| Skill invocation name (unique ID) | `registered-architect` | All-lowercase with hyphens; tools that support skills invoke it directly, and tools that do not still trigger it from a natural-language description |
| Display name | OmniAiLab Global Registered Architect | The name shown on the repository page and in the docs — not the invocation name; it routes and checks codes, it does not produce schemes |
| Version | v1.1.0 | Kept identical across `SKILL.md`, `.claude-plugin/plugin.json` and all three READMEs |
| Publisher / Developer | OmniAiLab / Mochiball | — |
| License | MIT (see [LICENSE](LICENSE)) | Use and redistribution are governed by that file; standard text is quoted, never resold |
| Accompanying documents | [README.md](README.md) / [README_EN.md](README_EN.md) / [SKILL.md](SKILL.md) | Invocation, module index, six-stage workflow, terminology checks, pitfalls, FAQ and deliverable list |
| Repository | [tomatoparkdao/registered-architect](https://github.com/tomatoparkdao/registered-architect) | All modules, references and calculators; **currently a private repository** — once public, `git clone` and issues work directly |
| Requirements | Python 3.9+ (calculators only) | The calculators have zero third-party dependencies; without Python everything is still readable, you just lose the preliminary calculations |
| Native platform | [OmniAiLab China site](https://www.omniailabx.com/) / [International site](https://omniailab.cn/) | Renderings and animation come from the platform; **code checks keep working when it is not connected** |

The invocation name is **all-lowercase with hyphens** (`registered-architect`), not the display name "OmniAiLab Global Registered Architect". Tools with native skill support are best driven by the invocation name; tools without it still trigger from a natural-language description such as "this project is in the Middle East, which clauses govern fire egress".

> **One naming trap**: the repository root holds a single `SKILL.md` — that is the **entry point** (global principles plus module routing).
> Each `skills/<module>/SKILL.md` is one of 29 **capability units**, carrying its own front-matter and signature, loaded on demand by the entry point.
> Invoke `registered-architect` by name — mounting the modules individually only loads the same clause material twice.

---


## Decide the jurisdiction before the design

The same massing study meets a different review in Dubai, Munich and Singapore: Dubai looks at Civil Defence pre-approval and façade cladding, Munich at the Brandschutznachweis and the state LBO, Singapore at the SCDF Fire Code together with ETTV/RTTV. **So the first move is not drawing — it is establishing which tier of mandatory standards governs the project, and who the authority is.**

If that cannot be established, it lists the gaps instead of borrowing another country's numbers and carrying on. That rule runs through all 29 modules.

| Scope | What it covers |
|---|---|
| **Fits · Jurisdiction and code routing** | Given address, occupancy, height, area, fire-hazard class and stage, it determines the applicable mandatory tier, the authority having jurisdiction and which local supplements apply. Ten packs, each standalone and mutually comparable |
| **Fits · Scheme and technical judgment** | Programming, area schedules, adjacencies, massing comparison, core and grid, envelope build-ups, structural system selection, MEP coordination, daylight and shading, room acoustics, material strategy — options with reasoning, not a single hand-waved answer |
| **Fits · Compliance cross-check** | Fire compartments, travel distance, egress width, accessible routes, energy targets, daylight and separation: each item lists the edition adopted, the clause relied on, local deviations and open questions for the AHJ |
| **Does not fit (explicitly refused)** | Building permits, fire-review opinions, structural seals, energy certification, accessibility certification. These can only be issued by the authority and a locally licensed professional; output must never be described as any of them |

---

## In one sentence

Hand it the project conditions — even just "an 18-storey hotel in Dubai, design development, heading for Civil Defence pre-approval" — and it fixes the jurisdiction and code tier first, then walks six stages to deliverable judgments, checklists and documents. At each stage boundary you only answer "confirmed" or "change this".

**It does not say "this scheme complies"; it says "under GB 50016-2014 (2018 ed.) clause 5.3.1 this is a Class I high-rise public building, your compartment is about 200 m² short, confirm with the fire authority"** — every conclusion carries code number, edition, location and open items, so a wrong answer can be traced to the step, the edition and the person who confirmed it.

## Capabilities

**It is not a search box that stuffs clauses into context. It is a review system that asks which jurisdiction first, writes the basis into every conclusion, and states plainly what it cannot do.**

| Layer | What is inside |
|---|---|
| **① Jurisdiction routing first** | `geographic-foundations` reads country, city, code number, currency, climate and material systems to identify the jurisdiction, then routes to the matching pack. If it cannot, it falls back to IBC / Eurocodes / ASCE / ISO references and **asks you to confirm** — it never assumes |
| **② Ten packs at clause level** | China, USA, UK, Germany, Japan, Singapore, Australia, India, UAE, Saudi Arabia: regulatory model, authorities, code tiers, edition years, local amendments and review paths, item by item; across jurisdictions it compares, never substitutes |
| **③ Eighteen professional modules** | Design theory, concept, programming, typology, spatial planning, envelope, structure, MEP, daylight, acoustics, materials, codes, fire, accessibility, sustainability, documentation — each with method, criteria and red lines |
| **④ Three layers of progressive loading** | Name resident, module body on demand, references last. 883 documents are never injected at once — the only way to navigate 1.13M lines without drowning the context |
| **⑤ Seven recalculable calculators** | Area density, U-value, daylight factor, egress, structural load, energy, cost: standard library only, `--json` for records; **early-stage only — submission values must be recomputed by a licensed professional** |
| **⑥ Every judgment has a source** | Each conclusion carries code number + edition + verification date; rules of thumb are labelled as guidance; four tiers of authority (mandatory / recommended / guidance / authority interpretation) are kept distinct |
| **⑦ It does not pretend** | No recommendation dressed as an approval, no scheme stage passed off as construction documents, no calculator output as a submission value, no foreign limit as the local answer. Missing input is stated as missing, with the path to close it |

### Capability list (29, by layer)

18 professional modules, 10 jurisdictional packs, one calculator set. The `references/` count shows how deep each module can reach.

| # | Module | Layer | What it covers |
|---|---|---|---|
| 1 | `architect-foundations` | Base | Architect and theorist matrix (Vitruvius to Kéré), quantitative rules of thumb, 28 building subtypes, design-quality framework, five anti-pattern families, module routing |
| 2 | `geographic-foundations` | Base | Identifies jurisdiction from country, city, code number, currency, climate and material systems, then routes; falls back to international references and asks for confirmation rather than assuming |
| 3 | `design-theory` | Design | Architectural history, movements, manifestos, design philosophy, formal language, critical regionalism, phenomenology, criticism; separates historical fact, theoretical reading and project advice |
| 4 | `concept-design` | Design | Concept generation, massing studies, solar envelope, wind comfort, view corridors, shadow impact, contextual height, FAR/GFA optimisation, naturally ventilated massing |
| 5 | `building-programming` | Design | Briefs, area standards, adjacency matrices, flow diagrams, occupant capacity, equipment schedules, zoning and capacity checks; areas are planning inputs requiring client and code verification |
| 6 | `building-typology` | Design | Residential, office, hotel, retail, schools, hospitals, libraries, theatres, sports, industrial and mixed use: spatial organisation, typical floors, circulation, daylight, structure, operations |
| 7 | `spatial-planning` | Design | Cores, vertical transport, public and service circulation, floor efficiency, back-of-house, loading, parking, restrooms, plant rooms, shafts, egress; plans must also pass accessibility, fire and grid checks |
| 8 | `building-envelope` | Technical | Brick and concrete walls, curtain walls, double skins, timber walls, metal panels, insulation, air and water tightness, glazing, spacers, coatings, dynamic glass; judged against climate, orientation, humidity and whole-life carbon |
| 9 | `structural-systems` | Technical | Concrete, steel, timber, masonry, precast, cable-stayed, space frame, shell and composite spans and detailing; **never size members from a rule-of-thumb table** — the engineer of record confirms |
| 10 | `building-services` | Technical | Natural and mixed-mode ventilation, VAV/VRF, chilled beams, heat pumps, heat recovery, plumbing, rainwater, fire water, electrical, lighting, low voltage, BMS, plant rooms, rooftop equipment, MEP coordination |
| 11 | `daylighting-design` | Technical | DF, sDA, ASE, UDI, VLT, SHGC, solar altitude and azimuth, shading geometry, daylight atria, sawtooth roofs; simulations must state weather file, timestep and occupancy assumptions |
| 12 | `acoustic-design` | Technical | Wall and floor separation, window acoustics, impact sound, flanking transmission, equipment noise, reverberation time, clarity, spaciousness, isolation, variable acoustics; junctions and workmanship matter as much as the specification |
| 13 | `material-selection` | Technical | Compares materials on performance, regulation, durability, maintenance, cost, embodied carbon, recyclability, supply chain, workmanship and appearance; product data never replaces samples and testing |
| 14 | `building-codes` | Compliance | IBC occupancy groups and Type I–V construction, height and area limits, egress, fire separation, plumbing fixture counts, plus IBC / Building Regulations / Eurocodes / NCC / NBC comparison |
| 15 | `fire-life-safety` | Compliance | Occupant load, exit count, travel distance, stairs and corridors, fire lifts, compartments, smoke control, detection, sprinklers, fire lanes, refuge areas; state the edition and local amendments |
| 16 | `accessibility-design` | Compliance | ADA, ISO, EN, BS, DIN, AS, GB and BCA comparison; continuous accessible routes, doors, ramps, lifts, restrooms, parking, tactile, auditory and cognitive support |
| 17 | `building-sustainability` | Compliance | Passive design, energy modelling, operational and embodied carbon, water, materials, health, ecology, certification; LEED, BREEAM, WELL, Green Star, NABERS, DGNB, CASBEE thresholds shift, so confirm the version first |
| 18 | `construction-documentation` | Delivery | Drawing indexes, layers and line weights, annotation, hatching, revision clouds, LOD, BIM coordination, specifications, RFI/ASI, mock-ups, site testing, closeout, warranties, O&M |
| 19 | `architect-calculator` | Tooling | Seven standard-library calculators: area density, U-value, daylight factor, egress, structural load, energy, cost |

### Ten jurisdictions

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

### Seven calculators

Early-stage and cross-check use only. **Numbers for submission must be recomputed by a licensed professional against the current code.** All scripts use the Python standard library alone.

| Script | Computes | Key arguments | Used for |
|---|---|---|---|
| `area_calculator.py` | Development density: GFA, net area, units, population, parking | `--site-area` `--far` `--ntg-ratio` `--avg-unit-size` `--persons-per-unit` `--parking-ratio` | Site acquisition and early capacity checks |
| `uvalue_calculator.py` | Assembly U-value from layered build-ups | `--layers` `--facade` `--rsi-internal` `--rsi-external` | Energy-code benchmarking, build-up comparison |
| `daylight_calculator.py` | Daylight factor estimate | `--room-width/depth/height` `--window-width/height/sill-height` `--glazing-transmittance` `--average-reflectance` | Compliance pre-check for classrooms, offices, dwellings |
| `egress_calculator.py` | Egress width and exit count | `--floor-area` `--occupancy-type` `--sprinklered` `--num-stories` | Core and stair count decisions at scheme stage |
| `structural_load_calculator.py` | Load take-down and preliminary sizing | `--tributary-area` `--num-floors` `--dead-load` `--live-load` `--occupancy-type` | Order-of-magnitude grid and slab depth |
| `energy_calculator.py` | Energy intensity estimate | `--floor-area` `--envelope-area` `--average-u-value` `--heating/cooling-degree-days` `--ventilation-rate` `--internal-gains` | Comparing energy strategies at scheme stage |
| `cost_calculator.py` | Order-of-magnitude cost | `--gfa` `--building-type` `--quality` `--region` `--include-external` | Budget conversations and option selection |

---

## Quick start

### 1. Where to install

```bash
# As a Claude Code plugin
claude --plugin-dir "/path/to/registered-architect"

# Into your host agent's skills directory (use the real path for your tool)
cp -R registered-architect ~/.claude/skills/registered-architect
cp -R registered-architect ~/.codex/skills/registered-architect
cp -R registered-architect ~/.workbuddy/skills/registered-architect

# Read-only reference, no installation
git clone https://github.com/tomatoparkdao/registered-architect.git
```

When copying into an existing project, **keep the entire `skills/` tree intact**: once the relative links between modules, references, templates and calculators break, routing collapses.

### 2. Where the material comes from

| Route | How | Best for |
|---|---|---|
| **Use the bundled material** | Read `skills/*/references/` and `skills/country-china/references/standards/` directly | Most projects; the Chinese fragments are full-text searchable |
| **Bring your own project files** | Drop the brief, drawings and local approvals into the project folder, then ask | Projects with existing design or local approvals |
| **Method only** | No files — just ask "what should be checked at this stage, against which edition" | Early planning, design review |

### 3. The opening message

Five items save a round of questions:

```text
Jurisdiction: Dubai, UAE
Occupancy and size: hotel, 18 storeys, 32,000 m2 above grade, podium F&B
Stage: design development, preparing for Civil Defence pre-approval
Known constraints: 6 m setback, 75 m height cap, developer facade-coverage requirement
Task: review egress and accessible routes, list items for Civil Defence confirmation
```

### 4. Two things to settle first

1. **Jurisdiction down to city level**: country + state/province/emirate + city + special jurisdiction (NEOM, developer-controlled districts in Dubai). With only a country, you get only national-tier answers.
2. **Stage drives depth**: at scheme stage it checks zoning, egress, setbacks and capacity; at construction-document stage it checks build-ups, layers, annotation and coordination. The same question yields a different checklist at each stage.

### 5. Only two answers needed

- **"Confirmed"** — the basis, edition and conclusions of this stage hold; move on.
- **"Change this"** — point at what is wrong; it re-runs that stage and voids every conclusion that depended on it.

---

## Pipeline overview

```text
① Intake        address / site / survey / programme / areas / storeys / budget / stage
      │         unknowns go into the assumption log — never guessed
      ▼
② Code routing  jurisdiction → regulator → authority → code tiers (mandatory / recommended / local / interpretation)
      │         conflicts get a priority; across jurisdictions compare, never substitute
      ▼
③ Programme &   area schedule / adjacency matrix / circulation / massing options
  massing       checked against daylight, wind, fire, accessibility, structure, buildability
      ▼
④ Coordination  grid / slab depth / core / shafts / plant rooms / envelope / vertical transport / fire systems / shading / maintenance
      ▼
⑤ Performance   area / U-value / daylight / egress / loading / energy / acoustics / carbon / cost
      │         labelled: calculator, simulation, or engineer-reviewed
      ▼
⑥ Delivery      drawings / models / schedules / specifications / material schedules / submission documents / risk register
                every revision keeps version, date, reason, owner
```

### Five non-negotiable rules

| # | Rule | Why it cannot be broken |
|---|---|---|
| R1 | **No jurisdiction, no compliance answer** | The same sentence has ten different answers; route first or the answer is wrong |
| R2 | **Every number carries code number, edition and verification date** | A limit without an edition cannot be traced, and liability cannot be defined |
| R3 | **Mandatory wins; local rules may only be stricter** | Local standards may not lower the national code; across jurisdictions compare metrics, never substitute values |
| R4 | **Calculators are for early stage only** | Submission values must be recomputed and signed by a licensed professional |
| R5 | **A recommendation is not an approval** | Recommendation / verification / approval / certification are four different things; mixing them is professional risk |

## Stage-by-stage detail

| Stage | Input | Action | Output |
|---|---|---|---|
| 1 Intake | Address, site boundary, survey, programme, areas, storeys, budget, schedule, client goals, operating model | Collect and check the basics; log unknowns as assumptions instead of guessing | Project summary + assumption schedule |
| 2 Code routing | Stage 1 summary | Identify authorities and code tiers; separate mandatory requirements, guidance, developer requirements, certification criteria and client preference | Route table + conflict priority + open-items list |
| 3 Programme and massing | Routing outcome | Area schedule, adjacency matrix, circulation; massing options checked against daylight, views, wind, fire, accessibility, structure and buildability | Area schedule + adjacency matrix + massing comparison |
| 4 Technical coordination | Selected massing | Fix grid, slab depths, core, shafts, plant rooms, envelope systems, vertical transport, fire systems, shading, maintenance routes | Coordination list + interface register |
| 5 Performance verification | Technical scheme | Area, U-value, daylight, egress, loading, energy, acoustic, carbon and cost checks at the appropriate stage — labelled by who produced them | Performance table (calculator / simulation / engineer review, separate columns) |
| 6 Delivery | All upstream conclusions | Drawings, models, schedules, specifications, material schedules, performance notes, submission documents, risk register; every revision keeps version, date, reason, owner | Deliverable pack + revision log |

## Node action: no formal drawings before the plan is confirmed

This is not a stage. It is an action triggered by a stage conclusion, and it may only happen after that conclusion is confirmed.

| Red line | Rule | Why |
|---|---|---|
| Plan not confirmed | No formal plans, no submission pack, no construction-document-depth files | Once issued, the client treats them as settled; change the plan and everything is void |
| Jurisdiction not confirmed | Do not quote specific values; write "applicable edition to be confirmed" | A wrong edition is worse than none: it looks like a conclusion |
| Not reviewed | Never write "complies"; write "checked against clause X — passed / open" | Writing it down turns it into a promise, and the seal is not ours to give |

## Code-citation conventions

| Convention | Correct form | Common mistake |
|---|---|---|
| Clause citation | GB 50016-2014 (2018 ed.) clause 5.3.1 | "the code requires…" with no number or edition |
| Numeric value | 12 m (GB 50016-2014 clause 5.5.17, verified 2026-10) | 12 m with no source, edition or date |
| Local rules | Local standards may only be stricter than the national code | Using a local rule to override a mandatory clause |
| Units | SI throughout: area m², length m, load kN/m² | Mixing ft / ㎡ / kgf and tripping on magnitude |
| Authority tier | Mandatory > recommended > guidance > authority interpretation (interpretation may be stricter) | Treating guidance as mandatory, or mandatory as advisory |
| Edition | State the verification date next to the conclusion | Citing the 2014 edition while judging to the 2018 amendment |

## Pitfall table

| Failure | Consequence | Correct approach |
|---|---|---|
| Applying one country's limits in another | The whole scheme collapses at submission | Route the jurisdiction first; compare metric and applicability, never substitute values |
| Using an outdated edition without a verification date | Conclusions are untraceable and liability is undefined | Every conclusion carries code number + edition + verification date |
| Presenting rules of thumb as mandatory clauses | Misleads client and contractor, creates closeout and claim risk | Label experience values as guidance; mandatory requirements must cite clause numbers |
| Optimising plan area while ignoring fire, structure, MEP and maintenance space | Late rework; the core and shafts no longer fit | Run all four discipline checks from scheme stage |
| Comparing capital cost only | Whole-life cost ends up higher | Compare across the life cycle, including maintenance, replacement and energy |
| Giving conclusions without assumptions | Nothing can be verified or defended | Attach assumptions, evidence and open items to every judgment |
| Describing AI output as a seal, approval or certification | Legal and professional liability | Distinguish recommendation / verification / approval / certification at all times |

## Repository layout

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

## Deliverables

| File | Content | Audience |
|---|---|---|
| `01_project-brief.md` | Project summary, key assumptions, stage and known constraints — the baseline for later change comparison | Client, project manager, discipline leads |
| `02_code-route.md` | Jurisdiction determination, code tiers, editions, verification dates and open questions per authority | Architect, AHJ, fire and planning authorities |
| `03_program.md` | Programme, area schedule, adjacencies and capacity checks, with the area-calculation basis | Client, operator, programming consultant |
| `04_concept-options.md` | Concept, massing comparison and environmental response, with the reasoning and cost of each choice | Client, design review panel, design team |
| `05_performance.md` | Environmental, structural, fire and accessibility results with review responsibilities, labelled by who produced them | Specialist consultants, plan-check authority |
| `06_materials.md` | Envelope and material strategy, equivalence evidence, sample schedule and alternates | Materials consultant, contractor, suppliers |
| `07_documentation.md` | Drawing index, specifications, BIM coordination record and required level of detail per stage | Contractor, construction-document reviewer |
| `08_review-log.md` | Review comments, RFI, ASI and decision record with owner, date and closure status | Whole project team, client representative, auditor |

## FAQ

| Question | Answer |
|---|---|
| Is it China-only? | No. Ten jurisdiction packs, China being one of them and the deepest (848 documents). With no clear jurisdiction it falls back to international references and asks you to confirm. |
| Can calculator output go straight into a submission? | No. Calculators support early design and cross-checking; submission values must be recomputed and signed by a licensed professional. |
| What if the city has no dedicated code? | It states the gap, uses the next tier up as a provisional reference, and lists the questions to put to the AHJ or local planning authority. |
| Can it compare codes across countries? | Yes, provided the comparison names the metric, the edition, the scope, and the parts that cannot be equated. |
| Does it need network access or external software? | No. Knowledge base, templates and calculators all work offline; CAD, BIM, rendering and analysis tools are optional integrations, not dependencies. |
| Is its output a design deliverable? | It is supporting material for design judgment and review — not a sealable construction document, and not an approval. |

## Recommended tools and models

Nothing here is required. This table says what it can work alongside, not what you must install.

| Purpose | Optional tooling | How this Skill treats it |
|---|---|---|
| Drawing production | AutoCAD / Revit / ArchiCAD / Rhino | Integration only; this Skill produces judgments and checklists, not DWG files |
| Models and coordination | IFC / any BIM coordination platform | Key dimensions come from the model, but compliance conclusions still need review |
| Code texts | Authority websites, official standards portals | Bundled fragments are for retrieval; verify the official current edition before relying on it |
| Full-text clause search | `grep`, VS Code, any text search | 426 Chinese code entries and 414 text fragments are directly searchable |
| Numerical checks | The seven built-in calculators (Python 3.9+) | Zero third-party dependencies; every result states its basis and assumptions |
| Discussion and questions | [Discord community](https://discord.gg/vdgTEpXMh3) | Method debates, interpretation conflicts, issue reports |

## Minimum requirements

| Item | Requirement | Why | If not met |
|---|---|---|---|
| Operating system | Windows / macOS / Linux | Markdown plus the Python standard library; no platform lock-in | No impact; readable anywhere |
| Python | 3.9+ (calculators only) | The seven scripts use `argparse` / `json` / `math` / `sys` only | Calculators unavailable; all material still readable |
| Disk | About 60 MB | Mainland China fragments dominate; other modules are a few MB | Keep only the packs you need and it drops to a few MB |
| Memory | No special requirement | Files are read on demand; no whole-library indexing | No impact |
| Network | Not required | Works offline; needed only to verify current editions or pull updates | Conclusions must be marked "edition not verified online" |
| GPU | Not required | This Skill produces no generative content | No impact |

## Brand and creation-tool exclusivity

| Item | Rule | Notes |
|---|---|---|
| Curated material and criteria | OmniAiLab original | Directory structure, cross-indexing, criteria and checklists are compiled by this project |
| Standard texts | Cited, never resold | Citations carry code number and edition; no standard text is repackaged or redistributed |
| Generated images / video | Out of scope here | This Skill produces no renderings; when needed they come from the OmniAiLab platform and never serve as dimensional evidence |
| Third-party tools | Adaptation statement only | No code is bundled, no dependency is assumed; missing tools are reported honestly |
| Public naming | `registered-architect` / OmniAiLab Global Registered Architect | Callable name and display name must not be mixed; it is not a "chief designer" |

## Companion manual

No separate PDF manual is published; this README is the operating guide, and the deep material ships in the repository for offline use.

| To look up | Where | What is inside |
|---|---|---|
| Invocation and module duties | [SKILL.md](SKILL.md) | Working principles, module guide, deliverables and limits |
| Clauses and practice | `skills/<module>/SKILL.md` + `references/` | Method, criteria, red lines and topical references per module |
| Chinese code entries | `skills/country-china/references/standards/` | 426 code and atlas entries, 414 text fragments, topic-routing table |
| Calculator arguments and basis | `skills/architect-calculator/` | Parameter notes and calculation references for the seven scripts |
| Attribution and licence | [LICENSE](LICENSE) | Full MIT text and attribution convention |

## Getting help

Trying to report a problem, argue an interpretation or suggest a feature? This order is fastest:

| Channel | Address | Best for |
|---|---|---|
| **Community (Discord)** | [discord.gg/vdgTEpXMh3](https://discord.gg/vdgTEpXMh3) | Method discussion, interpretation disputes, usage questions; fastest response and a good place to meet peers |
| **Repository issues** | [tomatoparkdao/registered-architect/issues](https://github.com/tomatoparkdao/registered-architect/issues) | Bug reports and feature requests; stays searchable for the next person |
| **This README** | [Pitfall table](#pitfall-table) · [FAQ](#faq) | Works offline; most questions are answered here |
| **Chinese code index** | `skills/country-china/references/standards/` | Specific clauses, atlases and topic routing |
| **OmniAiLab official** | [omniailabx.com](https://www.omniailabx.com/) | Platform, account and ecosystem; professional method questions still go through the channels above |

> When asking, include **jurisdiction (country + city), occupancy and size, current stage, and the code edition and text you are relying on** — far more likely to be answered in one pass than "is this compliant?".

## Documentation map

| To understand | Read | What is inside |
|---|---|---|
| Entry point and principles | [SKILL.md](SKILL.md) | Four working principles, module guide, deliverables and limits |
| Ten jurisdictional packs | `skills/country-*/SKILL.md` | Regulatory model, authorities, code tiers, review paths |
| Chinese codes and atlases | `skills/country-china/references/standards/` | 426 code entries, 414 text fragments, inventory and topic routing |
| The eighteen professional modules | `skills/<module>/SKILL.md` | Method, criteria, red lines and references for each |
| Calculator usage | `skills/architect-calculator/` | Parameters, units and applicability for the seven scripts |
| Plugin metadata | [.claude-plugin/plugin.json](.claude-plugin/plugin.json) | Callable name, version, keywords and author |
| Chinese edition | [README.md](README.md) | Same structure, in Chinese |
| Licence and attribution | [LICENSE](LICENSE) | Full MIT text and attribution convention |

## Contributing

Released under **MIT** (full text in [LICENSE](LICENSE)) and open to contributions. One precondition: **submit verifiable code positions and professional methods, with the source stated** — code number, edition year and official origin are all mandatory.

| Direction | What to submit | Where |
|---|---|---|
| New jurisdiction pack | Regulatory model, authorities, code tiers and review path, verifiable against official sources | `skills/country-<jurisdiction>/` |
| New professional module | A capability's duty, inputs, criteria and red lines, structured like the existing 18 | `skills/<module>/` |
| Clause material | Publicly citable clause summaries and atlas indexes, with number, edition and origin | `skills/country-china/references/standards/` |
| Corrections | Typos, outdated positions, broken links, inconsistent counts, tables that do not fill the page on GitHub, CN/EN drift | Open a PR or issue directly |
| New external dependency | Run a licence check first and state the origin in the PR; no origin, no merge | See [LICENSE](LICENSE) |

**At minimum, run these two before opening a PR**:

```bash
python -m py_compile skills/architect-calculator/scripts/*.py       # calculator syntax check
python skills/architect-calculator/scripts/area_calculator.py --site-area 5000 --far 2.5 --json
```

Pairing and debate happen in the [Discord community](https://discord.gg/vdgTEpXMh3); formal conclusions belong in an issue or PR so they stay traceable.

## License and legal

| Item | Content |
|---|---|
| Repository licence | **MIT**, full text in [LICENSE](LICENSE) |
| Standard texts | Clauses are cited and indexed only; copyright remains with the issuing body. No standard text is resold or redistributed |
| Attribution convention | Every Markdown file carries `author: OmniAiLab` / `developer: Mochiball` in its front matter, with the standard signature line at the top and the end |
| No false authorship | No third-party document or standard text is presented as OmniAiLab original work |
| Disclaimer | Structural safety, fire, accessibility, MEP loads and local code compliance are outside the scope of this system's conclusions and must be reviewed and signed by a licensed professional in the project's jurisdiction; scheme-stage output is not construction documentation; calculator output is not a submission value; cost figures are scheme-stage estimates, not a basis for settlement |
| Limitation of liability | The authors and maintainers accept no liability for any loss arising directly or indirectly from use of this Skill |

## Credits

- Publisher and maintainer: **OmniAiLab** ([omniailabx.com](https://www.omniailabx.com/))
- Developer: **Mochiball**
- The curated material ([`skills/`](skills/)), jurisdiction packs and criteria are **independently compiled** from publicly issued codes and general engineering practice; no third-party document is copied or rewritten, and citations stop at code number and edition.
- This Skill produces no images or video; where renderings are needed they are produced on the **OmniAiLab** platform and never used as dimensional evidence.
- AutoCAD / Revit / ArchiCAD / IFC are referenced as **adaptation targets with degraded paths only**; no code is bundled and no dependency is assumed.
- Community: [Discord · discord.gg/vdgTEpXMh3](https://discord.gg/vdgTEpXMh3) — usage questions, interpretation debates and contribution coordination all happen here.

---

<div align="right">

[简体中文](README.md) ｜ **English**

</div>

---
> © OmniAiLab ｜ Developer: Mochiball ｜ OmniAiLab Global Registered Architect (omniailabx.com) — unauthorised copying, distribution or redistribution is prohibited.
