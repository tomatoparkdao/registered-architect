---
name: country-germany
description: >
  Germany architectural code and regulatory reference. Covers the Musterbauordnung (MBO 2002,
  last amended 2019) federal model plus the 16 binding Landesbauordnungen (LBO) for each Bundesland
  (BayBO Bavaria, BauO NRW North Rhine-Westphalia, BauO Bln Berlin, HBauO Hamburg, BauO Bbg
  Brandenburg, NBauO Lower Saxony, HBO Hesse, BauO LSA Saxony-Anhalt, SaechsBO Saxony, ThuerBO
  Thuringia, LBauO Rheinland-Pfalz, LBO BW Baden-Wuerttemberg, BauO SH Schleswig-Holstein, BauO
  M-V Mecklenburg-Vorpommern, LBO Saarland, BauO Bremen), the federal Gebaeudeenergiegesetz
  GEG 2023, the German Eurocode national annexes (DIN EN 1990-1999/NA), the DIN 18040 series
  for accessibility (Part 1 public buildings, Part 2 dwellings, Part 3 public space), DIN 4109
  for sound insulation, DIN 4108 thermal insulation, DIN 4102/EN 13501 for fire classification,
  Musterhochhausrichtlinie + Sonderbauordnungen for special buildings, Versammlungsstaettenverordnung
  for assembly buildings, Industriebaurichtlinie for industrial, KrPflVO/HHRRL for hospitals,
  Brandschutznachweis methodology, BAFA/KfW incentive certification schemes, DGNB certification,
  Effizienzhaus 40/55/70 standards, Heizungsgesetz 2024 (Heizung Replacement Act),
  Bauwerksbuch (building documentation), TGA/HKLS engineering disciplines, and the BIM
  Deutschland federal mandate timeline.
---

# Country: Germany

Architectural code and regulatory reference for projects in any of the 16 German Bundeslaender (Federal States). Activate this skill on any German city reference, EUR currency in German context, mention of "DIN"/"LBO"/"GEG"/"MBO"/"BayBO"/"Energieausweis"/"Brandschutznachweis"/"Effizienzhaus"/"DGNB"/"KfW"/"BauO", or German technical terminology (Geschossflaechenzahl, Grundflaechenzahl, Vollgeschoss, Bauantrag, Bauvoranfrage, Rohbau).

---

## 1. Regulatory Hierarchy

Germany operates as **Archetype C (Federal Framework + Land Sovereignty)**. The Constitution (Grundgesetz) reserves building law to the Laender. The federal Musterbauordnung is a model only -- each Land issues a binding LBO. Significant variation exists between Bavaria, North-Rhine-Westphalia, Berlin, etc.

### 1.1 Authority Stack

```
LEVEL 1 -- FEDERAL (Bund)
  Bundesministerium fuer Wohnen, Stadtentwicklung und Bauwesen (BMWSB) -- housing/urban policy
  Bundesministerium fuer Wirtschaft und Klimaschutz (BMWK) -- energy + GEG
  Bundesministerium des Innern (BMI) -- some safety legislation
  Deutsches Institut fuer Bautechnik (DIBt) -- product approvals, technical regulations
  Bauministerkonferenz (BMK) -- intergovernmental Land building ministers conference;
    publishes Musterbauordnung MBO (model)
  Deutsche Akkreditierungsstelle (DAkkS) -- accreditation
  Bundesamt fuer Bauwesen und Raumordnung (BBR) -- federal building agency
  Bundesanstalt fuer Wirtschaft und Ausfuhrkontrolle (BAFA) -- energy incentives
  KfW (Kreditanstalt fuer Wiederaufbau) -- low-interest loans + Effizienzhaus standards

LEVEL 2 -- LAND (state)
  Each of 16 Bundeslaender:
    - Landesbauordnung (LBO) -- binding building code
    - Bauministerium des Landes -- state building ministry
    - Oberste Bauaufsicht -- top building authority
    - Approved Authority Schools (Verzeichnis der bauaufsichtlich anerkannten Stellen)

LEVEL 3 -- DISTRICT/MUNICIPALITY (Kreis / Gemeinde / Stadt)
  Bauamt (building authority) at city level OR Kreisbauamt (district) for smaller municipalities
  Bauaufsichtsbehoerde -- enforces LBO
  Stadtplanungsamt -- urban planning (Bebauungsplan implementation)
  Brandschutzdienststelle -- fire safety
  Untere Wasserbehoerde -- water
  Naturschutzbehoerde -- nature/environment

LEVEL 4 -- PROJECT
  Bauantrag (formal permit) OR Bauvoranfrage (preliminary inquiry) submitted via
    Bauvorlageberechtigte (a licensed architect or engineer authorized to submit)
  Pruefingenieure for structural check (in some Laender) / Pruefsachverstaendige for fire
  Berufsfeuerwehr / Freiwillige Feuerwehr -- fire dept review (joint with Brandschutzdienststelle)
  Energieberater for Energieausweis + GEG compliance certification
```

### 1.2 LBO Status by Land

The 16 LBOs broadly track the MBO 2002/2019 but each contains specific deviations. Practitioners working across Laender must note:

| Land | LBO | Capital | Notes |
|---|---|---|---|
| Baden-Wuerttemberg | LBO BW (last amended 2024) | Stuttgart | One of the most progressive; integrates KfW + GEG strictly |
| Bayern (Bavaria) | BayBO 2008 (with amendments) | Munich | Distinct; strict heritage clauses |
| Berlin | BauO Bln 2005 + 2020 + 2023 amend. | Berlin | City-state; Senatsverwaltung fuer Stadtentwicklung |
| Brandenburg | BauO Bbg | Potsdam | Mirrors MBO closely |
| Bremen | BremLBO | Bremen | City-state |
| Hamburg | HBauO | Hamburg | City-state; Behoerde fuer Stadtentwicklung |
| Hessen | HBO (Hess Bauordnung) | Wiesbaden | Distinct accessibility |
| Mecklenburg-Vorpommern | BauO M-V | Schwerin | Coastal: salt-air + wind |
| Niedersachsen | NBauO | Hannover | Wind-zone considerations |
| Nordrhein-Westfalen | BauO NRW 2018 (amended) | Duesseldorf | Most populated; ZBau (Zustaendige Baudienststellen) |
| Rheinland-Pfalz | LBauO | Mainz | Mirrors MBO |
| Saarland | LBO | Saarbruecken | Smallest; minor adjustments |
| Sachsen | SaechsBO | Dresden | Distinct heritage clauses |
| Sachsen-Anhalt | BauO LSA | Magdeburg | Distinct |
| Schleswig-Holstein | LBO SH | Kiel | Wind-coastal |
| Thueringen | ThuerBO | Erfurt | Mirrors MBO |

### 1.3 Federal Codes That Override or Supplement LBO

Some matters are federal sovereignty even though building law is Land:
- **GEG 2023** -- federal energy code, binding nationally
- **Heizungsgesetz / GEG amendments 2024** -- heat replacement rules
- **DIN standards** -- technical reference standards (legally binding when LBO references them)
- **Construction Products Regulation (CPR/EU 305/2011)** -- EU regulation
- **Energieeinsparverordnung EnEV (now superseded by GEG)** -- legacy
- **GefStoffV** -- hazardous substances
- **ArbStaettV** -- workplace ordinance (workplace dimensions, lighting, ventilation)
- **BImSchG** -- federal pollution control (noise + emissions)

---

## 2. MBO + LBO Core Requirements

### 2.1 Building Classes (Gebaeudeklassen)

MBO 2002 § 2(3) / parallel LBO clauses define **5 Gebaeudeklassen (GK 1-5)**:

| GK | Description | Height + Use | Key Implications |
|---|---|---|---|
| **GK 1** | Free-standing buildings up to 7 m, single/two dwellings, area ≤400 m2 OR free-standing agricultural buildings | Small detached/duplex | Lighter requirements, often no Brandschutznachweis check |
| **GK 2** | Free-standing or semi-detached up to 7 m, max 2 dwelling units, total floor area ≤400 m2 | Detached/duplex semi | Light requirements |
| **GK 3** | Other buildings ≤7 m | Townhouses, small apartments up to 2-3 storeys | Standard fire/structure |
| **GK 4** | Buildings ≤13 m + Nutzungseinheiten (use units) max 400 m2 each | Mid-rise apartments | Moderate requirements |
| **GK 5** | Buildings >13 m (i.e., up to 22 m for Hochhaus threshold) OR underground buildings | Mid-rise office, mid-rise residential | Significant fire requirements |
| **Hochhaus (special)** | >22 m occupied storeys above lowest fire-vehicle access | High-rise | Sonderbau; high-rise directive applies (Musterhochhausrichtlinie + Land-specific) |

### 2.2 Special Buildings (Sonderbauten)

MBO 2002 § 2(4) defines Sonderbauten -- buildings requiring special review due to size, use, or risk. Examples:
- Hochhaeuser (>22 m)
- Versammlungsstaetten (assembly venues) >200 occupants
- Schulen, Hochschulen (schools, universities) -- often Sonderbau
- Krankenhaeuser, Heime (hospitals, care homes)
- Verkaufsstaetten (retail) >2000 m2
- Garagen (parking) > 100 m2
- Industriebauten (specific industrial)
- Many more per Land enumeration

For Sonderbauten, additional ordinances apply:
- **MVStaettVO** -- Muster-Versammlungsstaettenverordnung (Assembly buildings)
- **MIndBauR** -- Muster-Industriebaurichtlinie (Industrial)
- **MGarVO** -- Muster-Garagenverordnung (Parking)
- **HochhausR** -- Musterhochhausrichtlinie (High-rise)
- **KrPflVO** / **HHRRL** -- Hospital regulations (Land-specific)
- **MVkVO** -- Muster-Verkaufsstaettenverordnung (Retail)

Each Land may adopt the Muster (Model) version verbatim or with modifications.

### 2.3 Planning Law (Baugesetzbuch + BauNVO)

Planning is federal: **Baugesetzbuch (BauGB)** + **Baunutzungsverordnung (BauNVO)**:
- **Flaechennutzungsplan (FNP)** -- municipality's land use plan (zoning at the broad scale)
- **Bebauungsplan (B-Plan)** -- detailed zoning, binding on individual plot
- **§ 34 BauGB** -- "Innenbereich" infill -- conforms to existing context
- **§ 35 BauGB** -- "Aussenbereich" outside built-up area -- generally restricted

**Key planning parameters (BauNVO):**
- **GRZ (Grundflaechenzahl)** -- ratio of building footprint to plot area (e.g., 0.4 = 40% coverage)
- **GFZ (Geschossflaechenzahl)** -- ratio of total above-grade floor area to plot area (similar to FAR; e.g., 1.2 = 120%)
- **BMZ (Baumassenzahl)** -- building volume per m2 plot (for industrial)
- **Vollgeschoss** -- "full storey" -- specifically defined; basements/attics often only fractional
- **Abstandsflaechen** (setback areas) -- typically 0.4-1.0 of building height (varies by Land + zone); minimum 3 m to property line

### 2.4 Setback and Density (BayBO example)

| Use District (BauNVO § 3-11) | Typical GRZ | Typical GFZ | Building Class typical |
|---|---|---|---|
| WR (reines Wohngebiet) | 0.4 | 1.2 | GK 1-3 |
| WA (allg. Wohngebiet) | 0.4 | 1.2 | GK 1-3 (5 possible) |
| WB (besonderes Wohngebiet) | 0.6 | 1.6 | GK 3-5 |
| MD (Dorfgebiet -- village) | 0.6 | 1.2 | GK 1-3 |
| MK (Kerngebiet -- city centre) | 1.0 | 3.0 | GK 5 + Hochhaus |
| GE (Gewerbegebiet) | 0.8 | 2.4 | varies |
| GI (Industriegebiet) | 0.8 | 2.4 + | varies |

---

## 3. Fire Safety (Brandschutz)

### 3.1 Brandschutznachweis (Fire Safety Concept)

Most German projects require a **Brandschutznachweis** -- a Fire Safety Concept submitted as part of the Bauantrag. The required level depends on Gebaeudeklasse:
- **GK 1-3**: simplified (Vereinfachte Pruefung) typically
- **GK 4-5**: full Brandschutznachweis required, often by a Pruefsachverstaendiger or Pruefingenieur for Brandschutz (state-licensed)
- **Sonderbauten**: full + special clauses per applicable ordinance (MVStaettVO etc.)

### 3.2 Fire-Resistance Classes (DIN 4102 → EN 13501-2)

Germany historically used DIN 4102 (F30, F60, F90, F120, F180); now harmonised to **EN 13501-2** (R30, REI60, REI90 etc.) with DIN 4102 still in everyday use:

| Old DIN 4102 | New EN 13501-2 | Time |
|---|---|---|
| F30 | R30 / REI 30 | 30 min |
| F60 | REI 60 | 60 min |
| F90 | REI 90 | 90 min |
| F120 | REI 120 | 120 min |
| F180 | REI 180 | 180 min |

Plus material classifications:
- A1, A2 -- non-combustible
- B (non-combustible Brandverhalten); -s1, d0 etc. smoke + droplet
- DIN 4102 retains old letters: **A1, A2** non-combustible; **B1** schwerentflammbar (low flammability); **B2** normal entflammbar; **B3** leicht entflammbar (forbidden in most uses)

### 3.3 Compartmentation per Gebaeudeklasse (MBO § 27-30 + DIN 4102/EN 13501)

| Element | GK 1-3 | GK 4 | GK 5 | Hochhaus |
|---|---|---|---|---|
| Tragendes Bauteil (load-bearing) -- general | F30 | F60 | F90 | F90+ |
| Brandwaende (firewall) | -- | F90/REI90 (Sonderbau) | F90/REI90 | F90+ |
| Treppenraum (stair shaft) | F30 | F60 | F90 | F90+ + pressurization |
| Schachtwaende (shaft walls) | F30 | F60 | F90 | F90+ |
| Wohnungstrennwaende (apt sep walls) | F30 | F60 | F90 | F90+ |
| Dachhaut | hartdach (hard) | hartdach | hartdach | hartdach |

### 3.4 Travel Distances (MBO 2002 § 35 + Sonderbau ordinances)

- General: max **35 m** travel distance to an exit OR a protected stair/corridor
- For GK 4-5 with sprinklers + smoke management: extensions per MVStaettVO etc.
- Sonderbau Hochhaus: ≤25 m within unit before reaching protected stair
- Max **two-direction travel** (paragraph regulating distance from any point in a Nutzungseinheit) ~30 m

### 3.5 Stair Width

Per MBO 2002 § 34:
- GK 3-5 main stair: **mind. 1.00 m** (1.20 m for assembly buildings)
- Lichte Treppenbreite (clear width): 1.00 m typ
- Stair max riser **17 cm**; tread **28 cm**; comfort 2R+G = 63 cm

### 3.6 Hochhaus (Musterhochhausrichtlinie)

For buildings >22 m occupied storeys:
- **Two stairs** required (or one with smoke extraction + sprinklers per specific concept)
- **Smoke extraction stairs** OR pressurization
- **Sprinklers** throughout building
- **Voice evacuation** (Sprachalarmanlage)
- **Feuerwehraufzug** -- firefighter elevator with extended specifications
- **Brandfallsteuerung** -- fire-control elevator
- **Brandschutzdienststelle** review additionally
- For >60 m: additional smoke-control engineered analysis

---

## 4. Energy Code (GEG 2023)

### 4.1 Gebaeudeenergiegesetz (GEG)

The **Gebaeudeenergiegesetz 2023** (formerly EnEV + EEWaermeG) is the binding federal energy law. Combined energy + heat + renewables provisions.

**Key requirements:**
- **Primaerenergiebedarf (Qp)** target by building type + reference
- **Hoechstwert spezifischer Transmissionswaermeverlust (HT')** -- transmission heat loss limit
- **Sommerlicher Waermeschutz** -- summer thermal protection (DIN 4108-2 simplified or simulation)
- **Mandatory renewable heat** in new buildings (since 2024; tightened by Heizungsgesetz amendment) -- 65% renewable for new heating systems
- **Bauteilanforderungen** -- component-level requirements (alternative to whole-building)

### 4.2 GEG 2024 Amendment (Heizungsgesetz)

- Federal heating law: new fossil-fuel heating systems prohibited from various deadlines (depending on building age + size)
- Bestandsgebaeude (existing buildings): replacement heating must be 65% renewable from staged dates
- Heat pumps + district heat + biomass preferred

### 4.3 Effizienzhaus (KfW)

KfW promotion standards beyond GEG:
- **Effizienzhaus 40** = 40% of reference Primaerenergiebedarf (rare; very strict)
- **Effizienzhaus 55** = 55% (common new-build target)
- **Effizienzhaus 70** = 70% (now too easy; superseded by GEG baseline)
- **Effizienzhaus 100** = baseline (no longer subsidized)

Plus categorizations:
- **Effizienzhaus 40 EE** -- with renewable energy emphasis
- **Effizienzhaus 40 NH** -- with sustainability (Nachhaltigkeit) certification
- **Effizienzhaus 55 EE** etc.

### 4.4 Energieausweis (Energy Performance Certificate)

Mandatory for new buildings, sales, lettings since 2007 (EnEV) / 2014 (full extension):
- **Verbrauchsausweis** (consumption-based -- existing buildings with use history)
- **Bedarfsausweis** (demand-based -- calculated; required for new + post-renovation)
- Issued by qualified Energieberater
- Validity 10 years
- Letter grade A+ through H

### 4.5 DIN 4108 + DIN V 18599

- **DIN 4108-2** -- minimum thermal insulation (component-level)
- **DIN 4108-6** -- annual heat demand calculation
- **DIN V 18599 (10 parts)** -- energy assessment for buildings -- the reference standard for GEG calculations

### 4.6 U-Value Targets (GEG 2023 + KfW)

| Element | GEG 2023 baseline | Effizienzhaus 55 | Effizienzhaus 40 |
|---|---|---|---|
| Aussenwand U (W/m2K) | 0.24-0.28 | 0.20 | 0.15 |
| Dach / oberste Geschossdecke U | 0.20-0.24 | 0.16 | 0.12 |
| Bodenplatte U | 0.30 | 0.20 | 0.15 |
| Fenster Uw | 1.3 | 1.0 | 0.80 |
| Eingangstuer U | 1.8 | 1.4 | 1.2 |
| Luftdichtheit n50 | 1.5/h with MV; 3.0/h without | 1.0/h | 0.6/h (Passivhaus level) |

---

## 5. Accessibility (DIN 18040)

### 5.1 DIN 18040 Series

The single most-cited accessibility standard:
- **DIN 18040-1:2010** -- Public buildings (Oeffentlich zugaengliche Gebaeude)
- **DIN 18040-2:2011** -- Dwellings (Wohnungen) -- with rollstuhlgerecht "R" mark for full wheelchair-accessible
- **DIN 18040-3:2014** -- Public space + transportation infrastructure

### 5.2 Key Dimensions (DIN 18040-1)

| Element | Dimension |
|---|---|
| Movement area minimum | 1.50 m x 1.50 m |
| Door clear width | 90 cm (preferred); 80 cm absolute min |
| Door operating force | < 25 N |
| Ramp gradient | ≤ 6% (1:16.7) -- significantly stricter than ADA's 1:12 (8.33%) |
| Ramp landing | 1.50 m every 6 m run + at top/bottom |
| Lift cabin | 1.10 m x 1.40 m (Type 1); 1.10 m x 2.10 m (stretcher; hospital) |
| Threshold | max 2 cm |
| Accessible WC | 2.20 m x 2.20 m minimum; clearance left + right of WC pan 90 cm minimum each side |
| Accessible parking | 3.50 m wide x 5.00 m long (no separate aisle; whole stall sized for access) |
| Tactile path | width 30 cm; contrast 0.4 (Michelson contrast); per DIN 32984 |

### 5.3 Hierarchical Approach

DIN 18040-1 distinguishes:
- **Barrierefreiheit** (general accessibility / barrier-freedom)
- **R-Kennzeichnung** (rollstuhlgerecht -- full wheelchair-accessible) -- higher standard with R suffix

### 5.4 LBO Requirements

Each LBO mandates accessibility for:
- **Wohngebaeude (residential)** -- public-facing entrance + common areas + a portion of dwellings
- **Oeffentliche Gebaeude (public buildings)** -- full DIN 18040-1 compliance
- **Arbeitsstaetten (workplaces)** -- per ArbStaettV + DIN 18040-1

Provision counts vary by Land. Generally:
- 1% of dwellings barrier-free in larger schemes
- Apartments accessible above 4 storeys (= lift required by LBO)

---

## 6. Acoustics (DIN 4109)

### 6.1 DIN 4109 -- Sound Insulation

**DIN 4109-1:2018** -- Minimum requirements:
- Walls between dwellings: R'w (apparent sound reduction) ≥ 53 dB
- Floors between dwellings: L'n,w (impact) ≤ 50 dB; R'w ≥ 54 dB
- Walls between dwelling + corridor: R'w ≥ 52 dB

**DIN 4109-5** -- Higher requirements (Schallschutzanforderungen erhoehter Schallschutz):
- Walls between dwellings: R'w ≥ 56 dB

**VDI 4100** -- Schallschutz im Hochbau -- 3 levels of sound protection (SSt I, II, III) -- commonly used to specify above-minimum.

---

## 7. Structural and Loads (Eurocodes with German NAs)

### 7.1 Eurocode Suite (DIN EN 1990-1999)

All German projects since 2012 use Eurocodes with the German National Annex (DIN EN 1990 NA - DIN EN 1999 NA):

| Eurocode | Topic |
|---|---|
| DIN EN 1990 + NA | Basis |
| DIN EN 1991 (10 parts) + NA | Actions (1-1 general, 1-2 fire, 1-3 snow, 1-4 wind, 1-5 thermal, 1-7 accidental, etc.) |
| DIN EN 1992 (3 parts) + NA | Concrete |
| DIN EN 1993 (parts 1-1 to 1-12, 2, 3, 4, 5, 6) + NA | Steel |
| DIN EN 1994 + NA | Composite |
| DIN EN 1995 (parts 1-1 to 1-2, 2) + NA | Timber |
| DIN EN 1996 + NA | Masonry |
| DIN EN 1997 + NA | Geotechnical |
| DIN EN 1998 + NA | Seismic |
| DIN EN 1999 + NA | Aluminium |

### 7.2 Wind Zoning (DIN EN 1991-1-4 + DIN NA)

Four wind zones (WZ 1-4) across Germany:
- **WZ 1** -- vb,0 = 22.5 m/s -- southwest, central
- **WZ 2** -- vb,0 = 25.0 m/s -- west, central north
- **WZ 3** -- vb,0 = 27.5 m/s -- north coast, central north
- **WZ 4** -- vb,0 = 30.0 m/s -- North Sea coast

### 7.3 Snow Zoning (DIN EN 1991-1-3 + DIN NA)

Three snow zones (SLZ 1-3) plus elevation factor:
- **SLZ 1** -- north German lowlands (sk = 0.65 + altitude)
- **SLZ 2** -- central + parts of east (sk = 0.85 + altitude)
- **SLZ 2a, 3** -- alpine (higher; e.g., Bavarian Alps sk = 2.0+ kN/m2)

### 7.4 Seismic (DIN EN 1998-1 + DIN NA)

Germany has low seismicity. Most of country is low-seismic; some Rhine Graben + Schwaebische Alb regions slightly higher. Seismic design typically not governing.

### 7.5 Geotechnical (DIN EN 1997 + DIN NA + DIN 1054)

Foundation design per Eurocode 7 + DIN 1054. Soil investigation per DIN EN 1997-2 + DIN 4020.

---

## 8. Sustainability & Certification

### 8.1 DGNB (Deutsche Gesellschaft fuer Nachhaltiges Bauen)

The leading German green building certification:
- Categories: Oekologisch, Oekonomisch, Soziokulturell-funktional, Technisch, Prozess
- Ratings: Bronze, Silver, Gold, Platinum
- 4 building types: new build, existing, neighbourhoods, interiors
- Stricter than LEED in operational + lifecycle assessment

### 8.2 Passivhaus Standard

Originated in Germany (Passivhaus Institut Darmstadt). Mandatory for many social housing projects in cities like Frankfurt. Five criteria:
- Heating demand ≤ 15 kWh/m2/yr
- Primary energy demand (PE) ≤ 60 kWh/m2/yr (Classic; lower for Plus/Premium)
- Airtightness n50 ≤ 0.6/h
- Frequency of overheating ≤ 10%
- Specific Heating Load ≤ 10 W/m2

### 8.3 BNB (Bewertungssystem Nachhaltiges Bauen)

Federal government's own assessment system, used for federal buildings.

### 8.4 EU Taxonomy / ESG Reporting

For larger projects: EU Taxonomy Climate Delegated Act 2021 + CSRD compliance reporting.

---

## 9. Permit Workflow (Bauantragsverfahren)

### 9.1 Standard Workflow (Bauantrag)

1. **Bauvoranfrage** (optional) -- preliminary inquiry to Bauamt to check zoning + critical issues
2. **Bauantrag** -- formal submission with: site plan, floor plans, sections, elevations, structural concept, fire concept (Brandschutznachweis), accessibility evidence (DIN 18040), energy evidence (GEG / Energieausweis), Statik (structural calculations)
3. **Bauvorlageberechtigung** -- only an architect (with appropriate license) OR licensed engineer can submit
4. **Pruefverfahren** (review period) -- depending on Land, 6 weeks to 3 months; Sonderbau longer
5. **Auflagen** -- Conditions imposed
6. **Baugenehmigung** -- Permit issued
7. **Baubeginn anzeigen** -- Notify start of construction
8. **Pruefingenieur Bestaetigung** -- Structural check engineer confirms Statik
9. **Brandschutzdienststelle Stellungnahme** -- Fire dept opinion
10. **Rohbauabnahme** -- Shell inspection
11. **Abnahmen** -- Various inspections
12. **Bauabnahme** -- Final inspection
13. **Nutzungsaufnahme** -- Begin use; Energieausweis registered

### 9.2 Vereinfachtes Verfahren

For GK 1-3 (small buildings), most Laender offer a "Vereinfachtes Genehmigungsverfahren" -- simplified procedure with shorter review periods + less documentation.

### 9.3 Genehmigungsfreie Verfahren

For GK 1-2 in residential zones with valid B-Plan, some construction is permit-free (Verfahrensfrei) -- typically minor home extensions, small additions.

---

## 10. Quick Numeric Reference

| Parameter | Value | Source |
|---|---|---|
| Floor-to-floor residential | 2.60-2.80 m typical | LBO + ArbStaettV; 2.40 m clear minimum (in some Laender 2.30 m) |
| Floor-to-floor office | 3.0-3.6 m | BCO-equivalent; 2.50 m clear min ArbStaettV |
| Door clear width | 0.90 m (preferred); 0.80 m absolute | DIN 18040-1 / LBO |
| Ramp gradient | 1:16.7 (6%) max | DIN 18040-1 (stricter than international 8.33%) |
| Stair: 2R+G comfort | 63 cm | German rule of thumb |
| Stair riser max | 17 cm (residential), 19 cm (industrial) | MBO |
| Stair tread min | 28 cm | MBO |
| Wall U-value (GEG 2023 baseline) | 0.24-0.28 W/m2K | GEG 2023 + DIN V 18599 |
| Wall U-value (Effizienzhaus 40) | 0.15 W/m2K | KfW Standards |
| Window U-value (GEG 2023) | 1.3 W/m2K | GEG 2023 |
| Sound insulation R'w wall (residential) | 53 dB minimum | DIN 4109-1 |
| Travel distance (max) | 35 m | MBO § 35 |
| Wind vb,0 Berlin | 25 m/s | DIN EN 1991-1-4 NA |
| Snow sk Munich | 0.85 + altitude kN/m2 | DIN EN 1991-1-3 NA |

---

## 11. Application Workflow

1. **Identify Bundesland**.
2. **Identify Gebaeudeklasse (GK 1-5)** based on height + use + size.
3. **Identify if Sonderbau** -- if so, apply relevant Muster ordinance.
4. **Confirm Bebauungsplan exists + parameters** (GRZ, GFZ, Vollgeschoss, Abstandsflaechen).
5. **Apply LBO of the Land** for general + fire + accessibility.
6. **Apply GEG 2023** for energy compliance (federal, binding).
7. **Apply DIN 18040** for accessibility.
8. **Apply Eurocodes with German NAs** for structural.
9. **Apply DIN 4109** for sound insulation.
10. **Identify Approval Route**: Bauantrag (full) vs Vereinfachtes Verfahren vs Verfahrensfrei.
11. **Confirm Bauvorlageberechtigte** for submission.
12. **Cite clauses**: "MBO 2002 § 26", "BayBO § 26", "GEG 2023 § 19", "DIN 18040-1:2010 Punkt 4.5", "DIN EN 1991-1-4/NA:2010 NDP 4.3", "DIN 4109-1:2018 Tabelle 3".

---

## 12. Authoritative Sources

- **Deutsches Institut fuer Bautechnik (DIBt)** -- dibt.de -- product approvals, technical guidelines
- **Bauministerkonferenz (BMK)** -- bauministerkonferenz.de -- Musterbauordnung
- **BMWSB Bundesministerium fuer Wohnen, Stadtentwicklung und Bauwesen** -- bmwsb.bund.de
- **BMWK Bundesministerium fuer Wirtschaft und Klimaschutz** -- bmwk.de -- GEG
- **Each Land Bauministerium** -- e.g., bauen.bayern.de (Bavaria), mhkbg.nrw (NRW), berlin.de/sen/sw (Berlin)
- **DIN (Deutsches Institut fuer Normung)** -- din.de -- DIN standards (paywall but reference)
- **BAFA (Bundesamt fuer Wirtschaft und Ausfuhrkontrolle)** -- bafa.de -- energy incentives
- **KfW** -- kfw.de -- Effizienzhaus standards + financing
- **DGNB** -- dgnb.de -- DGNB certification
- **Passivhaus Institut (PHI)** -- passiv.de -- Passivhaus standards
- **Bundesarchitektenkammer (BAK)** -- bak.de -- architects' chamber (federal)
- **Each Land Architektenkammer** -- regional architects' chambers

---

*Cross-references: load `building-codes` for general code structure (Germany is Eurocode-aligned for structure but unique for life-safety); `fire-life-safety` for general principles (overlaid by Brandschutznachweis methodology); `accessibility-design` for global frameworks then DIN 18040; `building-sustainability` for Passivhaus + DGNB + LEED comparison; `building-envelope` for thermal + acoustic + climate detailing (multiple climate zones in Germany north-south); `structural-systems` for Eurocode-based design.*
