---
name: geographic-foundations
description: >
  Auto-activated geographic context router for the Architect Skills plugin. Detects the country
  or jurisdiction of any architectural query and routes to the correct country-specific dossier
  (India, UAE, Saudi Arabia, USA, UK, Germany, Singapore, Japan, China, Australia). Encodes the
  global regulatory landscape: which authority issues which code, the hierarchy between
  national/state/municipal regulation, code adoption status by version year, the dominant
  energy/seismic/fire/accessibility codes per jurisdiction, and the cross-walk between national
  codes and the international reference systems (IBC, NFPA, Eurocodes, ISO, ASCE). Maintains a
  precise inventory of which country uses which Eurocode National Annex, which states/emirates/
  Lander/prefectures publish their own modifications, and where international standards apply
  by reference. Triggers country-specific skills when geographic context is detected in user
  query (city name, project location, language cues, code reference) and supplies global
  framework comparisons when no specific jurisdiction is declared.
user-invocable: false
---

# Geographic Foundations

Auto-activated layer that detects geographic context and routes architectural queries to the correct country-specific regulatory dossier. Loads before any code, life-safety, structural, or planning analysis.

---

## 1. Geographic Context Detection

When a user query includes any of the following signals, route to the named country skill *before* applying generic content from `building-codes`, `fire-life-safety`, or `accessibility-design`.

### 1.1 Direct Detection Triggers

| Signal Class | Examples | Route To |
|---|---|---|
| Country name | "India", "Bharat", "Republic of India" | `country-india` |
| Country name | "UAE", "Emirates", "Dubai", "Abu Dhabi" | `country-uae` |
| Country name | "Saudi", "KSA", "Kingdom of Saudi Arabia", "Riyadh" | `country-saudi-arabia` |
| Country name | "USA", "United States", "America" | `country-usa` |
| Country name | "UK", "Britain", "England", "Scotland", "Wales", "Northern Ireland" | `country-uk` |
| Country name | "Germany", "Deutschland", "DE" | `country-germany` |
| Country name | "Singapore", "SG" | `country-singapore` |
| Country name | "Japan", "Nippon", "JP" | `country-japan` |
| Country name | "China", "PRC", "Zhongguo" | `country-china` |
| Country name | "Australia", "AU", "Oz" | `country-australia` |
| Code reference | "IBC", "IRC", "IECC", "ASCE 7" | `country-usa` (then `building-codes` for IBC depth) |
| Code reference | "NBC India", "ECBC", "IS 1893", "IS 875" | `country-india` |
| Code reference | "NBC 2016" | `country-india` (disambiguate from "NBC Canada") |
| Code reference | "Approved Document", "AD-B", "Part L", "Part M" | `country-uk` |
| Code reference | "GEG", "DIN 18040", "LBO", "MBO" | `country-germany` |
| Code reference | "SBC 201", "SBC 301", "SBC 601", "SBC 801" | `country-saudi-arabia` |
| Code reference | "Dubai Building Code", "DBC", "ADIBC", "Estidama" | `country-uae` |
| Code reference | "NCC", "BCA Vol 1", "AS 1428", "AS/NZS 1170" | `country-australia` |
| Code reference | "Building Standards Act", "Kenchiku Kijun Hou" | `country-japan` |
| Code reference | "GB 50016", "GB 50352", "GB 50011", "JGJ" | `country-china` |
| Code reference | "BCA Singapore", "URA", "SCDF Fire Code" | `country-singapore` |
| City name | "Mumbai", "Delhi", "Bangalore", "Chennai", "Hyderabad", "Kolkata", "Pune", "Ahmedabad" | `country-india` |
| City name | "Dubai", "Abu Dhabi", "Sharjah", "Ajman" | `country-uae` |
| City name | "Riyadh", "Jeddah", "Mecca", "Medina", "Dammam", "NEOM" | `country-saudi-arabia` |
| City name | "New York", "Los Angeles", "Chicago", "San Francisco", "Boston", "Seattle", "Miami", "Houston" | `country-usa` |
| City name | "London", "Manchester", "Birmingham", "Edinburgh", "Glasgow", "Cardiff", "Belfast" | `country-uk` |
| City name | "Berlin", "Munich", "Hamburg", "Frankfurt", "Cologne", "Stuttgart" | `country-germany` |
| City name | "Tokyo", "Osaka", "Yokohama", "Kyoto", "Sapporo", "Fukuoka" | `country-japan` |
| City name | "Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Chengdu", "Chongqing", "Hong Kong" | `country-china` (HK = SAR but follows BD Hong Kong codes; flag) |
| City name | "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Canberra", "Hobart" | `country-australia` |
| Currency cue | "USD" (with site/cost) | `country-usa` (probable) |
| Currency cue | "INR", "Lakh", "Crore" | `country-india` |
| Currency cue | "AED", "Dirham" | `country-uae` |
| Currency cue | "SAR", "Riyal" | `country-saudi-arabia` |
| Currency cue | "GBP", "Pound" | `country-uk` |
| Currency cue | "EUR" (with EU country context) | route to relevant country (`country-germany` if no other cue) |
| Currency cue | "SGD" | `country-singapore` |
| Currency cue | "JPY", "Yen" | `country-japan` |
| Currency cue | "CNY", "RMB", "Yuan" | `country-china` |
| Currency cue | "AUD" | `country-australia` |

### 1.2 Indirect/Inferential Triggers

- **Site climate description** ("hot-arid", "tropical monsoon", "Mediterranean", "temperate maritime", "subarctic", "humid subtropical") combined with a city name -> resolve city -> country.
- **Cultural cue** ("vastu compliance", "qibla orientation", "feng shui", "minka", "haveli", "courtyard house with majlis") -> infer country/region (India, MENA, China/HK, Japan, India respectively).
- **Standard organisation reference** ("BIS spec", "DIN-tested", "JIS-marked", "GB-stamped", "BSI-certified") -> country.
- **Regulatory authority name** ("Civil Defence approval", "Trakhees", "Tatweer", "MoHUA", "MLIT", "Bauamt") -> country.
- **Language cue in proper noun** ("brise-soleil"+"ECBC" Indian usage; "rohbau" German; "shikkui" Japanese; "majlis" Arab; "joglo" Indonesian; "shophouse" Singaporean).

### 1.3 Default Behaviour

If no geographic context is established after the first user message, ask **one** clarifying question: *"Which jurisdiction does this project sit under? It affects code compliance, structural design loads, energy targets, and accessibility standards."*

If the user is ambiguous or operating cross-border (international firm, design competition, master-plan study), apply the **international reference cluster** (IBC + Eurocodes + ASCE 7 + ASHRAE + ISO 21542 accessibility + ISO 23932 fire) and explicitly state the assumption.

---

## 2. Global Regulatory Hierarchy

Each country sits in one of five regulatory archetypes. The archetype determines how clause-level questions are answered.

### 2.1 Archetype A -- Unitary National Code

A single nationally adopted code applies uniformly with no state/municipal variation. Cities adopt by reference.

- **Singapore** (Building Control Act + Building Control Regulations, administered by BCA centrally)
- **Saudi Arabia** (Saudi Building Code series SBC 201-1001 issued by SBCNC, mandatory in all regions since 2018)
- **France** (Code de la construction et de l'habitation; departments adopt by reference -- not in our Tier-1 but for context)

### 2.2 Archetype B -- National Model + State/Provincial Adoption

A national model code is issued but each state/province adopts a version (or modifies). Practitioner must check the state edition.

- **USA** (ICC publishes IBC/IRC/IECC/IFC; each state/county adopts a specific year. California adds Title 24; NYC, Chicago, Florida publish significant amendments.)
- **Australia** (NCC 2022 published by ABCB; each state administers via Building Act, with state-specific variations published as appendices.)
- **India** (NBC 2016 issued by BIS; states/UTs notify their own Building Bye-Laws and Development Control Regulations -- DCR/DCPR. Code is not legally binding by itself.)
- **Canada** (NBC of Canada 2020; provinces adopt -- Ontario OBC, BC BCBC, Quebec separate regime. Out of Tier-1.)

### 2.3 Archetype C -- Federal Framework + State/Land Sovereignty

The country has a federal framework but actual building law is state-sovereign. Each state has its own primary statute.

- **Germany** (Musterbauordnung MBO is a model only. Each of 16 Lander has its own Landesbauordnung -- e.g., BayBO Bavaria, BauO NRW, BauO Bln Berlin -- which is legally binding. Energy is federal: GEG.)
- **UAE** (Federal Civil Defence Code applies to fire; each emirate has its own building code: Dubai Building Code 2021, ADIBC Abu Dhabi, etc.)
- **UK** (Building Regulations 2010 apply to England; Wales, Scotland, Northern Ireland have separate regimes -- Welsh AD, Scottish Technical Handbooks, NI Technical Booklets.)

### 2.4 Archetype D -- Centralised National + Mandatory Strong-Form Clauses

A single national code with "mandatory provisions" that override anything else, plus permissible local supplements.

- **China** (GB series codes issued by MOHURD; "Mandatory Provisions" (qiangzhixing tiaowen) in red text are legally binding nationally. Cities publish DB local supplements -- DB11 Beijing, DGJ08 Shanghai, DBJ45 Guangxi -- which may *only* be more stringent.)
- **Japan** (Building Standards Act + Cabinet Order + MLIT Notifications; designated cities have planning autonomy under City Planning Act but structural and safety provisions are national.)

### 2.5 Archetype E -- Performance-Based Outcome Regulation

Code prescribes outcomes; deemed-to-satisfy paths are advisory. Engineered solutions admitted via approved verification methods.

- **Australia** (NCC 2022 fully performance-based; DTS and Performance Solution both legal.)
- **UK** (Approved Documents 2010+ are guidance; performance route via fire engineering reports under BS 7974, structural performance under EN 1990, etc.)
- **New Zealand** (NZBC, out of Tier-1.)

Many Tier-1 countries are *hybrid*: e.g., Japan permits performance verification (Article 38 prior to 1998; replaced by Article 37 type approval and BCJ structural performance evaluation post-1998).

---

## 3. Comparison Matrix -- Tier-1 Countries

### 3.1 Primary Code, Energy Code, Fire Code, Accessibility Code

| Country | Primary Building Code | Energy Code | Fire Safety | Accessibility |
|---|---|---|---|---|
| **India** | NBC 2016 (BIS, advisory) + state DCR/DCPR (binding) | ECBC 2017 / ECBC-R 2018 (BEE) | NBC 2016 Part 4 + IS 15683 | Harmonised Guidelines & Space Standards 2021 (MoHUA) |
| **UAE (Dubai)** | Dubai Building Code 2021 (DBC) | Al Sa'fat Dubai Green Building Regs 2011 + 2016 update | UAE Fire and Life Safety Code of Practice 2018 | Dubai Universal Design Code 2017 + Federal Law 29/2006 |
| **UAE (Abu Dhabi)** | Abu Dhabi International Building Code 2013 (ADIBC, IBC-derived) | Estidama Pearl Building Rating System 2010 | UAE FLS Code 2018 | DMA Accessibility Code 2014 |
| **Saudi Arabia** | SBC 201-CR 2018 (general) -- 9 part code system | SBC 601-CR 2018 (energy) | SBC 801-CR 2018 (fire) + Saudi Fire Code 2007 | SBC 801 Part 11 + Universal Accessibility Code (KKIA) |
| **USA** | IBC 2024 (model) + state adoption (varies 2015-2024) | IECC 2024 / ASHRAE 90.1-2022 (Energy Standard for Buildings) | NFPA 101 Life Safety Code 2024 + IBC Ch. 7-10 | ADA 2010 Standards + ANSI A117.1-2017 + Fair Housing Act |
| **UK (England)** | Building Regulations 2010 + Approved Documents A-S (2010-2025) | AD-L Vol 1 (dwellings) + Vol 2 (other), 2021 + 2025 future homes/buildings standards | AD-B Vol 1 + Vol 2 (2022 amendments post-Grenfell) | AD-M Vol 1 (dwellings) + Vol 2 (other), 2015/2020 + BS 8300-1/2:2018 |
| **Germany** | 16 Landesbauordnungen (LBO) + Musterbauordnung 2002/2019 (MBO) model | GEG 2023 (Gebaudeenergiegesetz) | LBO + Muster-Industriebaurichtlinie + DIN 4102 / EN 13501 | DIN 18040-1 (public), -2 (housing), -3 (public space) |
| **Singapore** | Building Control Act 1989 + Building Control Regulations 2003 | BCA Code on Environmental Sustainability 2018 + SS 530 | SCDF Fire Code 2018 | BCA Code on Accessibility 2019 + Universal Design Index |
| **Japan** | Building Standards Act 1950 (Kenchiku Kijun Ho) + Cabinet Order + MLIT Notifications | Act on Improvement of Energy Consumption Performance of Buildings 2015 (Kenchikubutsu Sho-Energy Ho) | Fire Service Act + Fire Service Law Enforcement Order | Heart Building Law 2006 (Barrier-Free Law) |
| **China** | GB 50352-2019 (Civil Buildings Unified Design Standard) + GB 50016-2014 (fire) + 50 other GB codes | GB 55015-2021 (General code building energy) + GB 50189-2015 (public buildings) | GB 50016-2014/2018 (fire), GB 50045-95/2005 (high-rise) | GB 50763-2012 (Accessibility) |
| **Australia** | NCC 2022 Vol 1 (Class 2-9), Vol 2 (Class 1, 10), Vol 3 (plumbing) | NCC Section J (Vol 1) + NatHERS 7-star (Vol 2 housing) | NCC Section C, D, E + AS 1530, AS 4072 series | NCC Vol 1 Part D3 + AS 1428.1-2021 + Disability (Access to Premises) Standards 2010 |

### 3.2 Seismic, Wind, Snow Loading Codes

| Country | Seismic | Wind | Snow / Climate Loads |
|---|---|---|---|
| **India** | IS 1893:2016 (Pt 1 general; Pt 2 liquid retaining; Pt 3 bridges; Pt 4 industrial) + IS 13920:2016 ductile detailing | IS 875 Pt 3:2015 | IS 875 Pt 4 (snow, limited) |
| **UAE** | ASCE 7-16 referenced; low seismicity (Zone 1-2 ASCE), but Dubai Code mandates Zone 2A | ASCE 7-16, sandstorm + thermal additional | N/A (heat instead -- ASHRAE 169 zone B1 hot-dry) |
| **Saudi Arabia** | SBC 301-CR 2018 (loads) -- ASCE 7-derived, Zone 1 (Riyadh) to 2B (Tabuk/NEOM) | SBC 301 -- ASCE 7-derived, 3-second gust map | N/A (heat); SBC 301 thermal |
| **USA** | ASCE 7-22 + ASCE 41-23 (existing) + ACI 318-19, AISC 360-22 | ASCE 7-22 (Risk Cat I-IV; 3-second gust) | ASCE 7-22 Ch. 7 (ground snow load maps) |
| **UK** | BS EN 1998-1:2004 (Eurocode 8) -- low seismicity, often waived | BS EN 1991-1-4 + UK National Annex (BS EN 1991-1-4 NA) | BS EN 1991-1-3 + UK NA (snow) |
| **Germany** | DIN EN 1998-1 + DIN EN 1998 NA (zones 0-3) | DIN EN 1991-1-4 + DIN NA (zones WZ 1-4) | DIN EN 1991-1-3 + DIN NA (zones SLZ 1-3 + elevation table) |
| **Singapore** | SS EN 1998-1 + SS NA (intra-plate; small loads) | SS EN 1991-1-4 + SS NA (tropical; 1-in-50yr 3s gust 33-35 m/s) | N/A |
| **Japan** | Building Standards Act Art. 20 + MLIT 2009 Notification + AIJ standards; Level 1 (475-yr) + Level 2 (2475-yr) design | Building Standards Act + AIJ Recommendations for Loads on Buildings 2015 | AIJ Recommendations -- regional snow load maps by city |
| **China** | GB 50011-2010 (seismic design of buildings) -- 6 zones (degree 6 to 9) | GB 50009-2012 (load code) -- 4 wind zones | GB 50009-2012 -- snow load maps |
| **Australia** | AS 1170.4-2007 (low to moderate) | AS/NZS 1170.2:2021 -- regions A, B, C (cyclonic), D (severe cyclonic) | AS/NZS 1170.3:2003 -- snow for alpine regions |

### 3.3 Code Reference Hierarchy When Designing Cross-Border

When designing for a country not in Tier-1, use this fallback chain:

1. **Local code** (if exists and translated/available)
2. **Regional code adopted by reference** (e.g., Gulf states often defer to IBC or SBC)
3. **International Building Code (IBC 2024)** -- North American default
4. **Eurocodes** (EN 1990-1999) -- European default, used in 30+ countries by adoption
5. **ISO standards** (ISO 21542 accessibility, ISO 23932 fire engineering, ISO 22156 bamboo, ISO 5807 plumbing) -- universal fallback
6. **ASHRAE 90.1 + ASHRAE 62.1 + ASHRAE 55** -- universal thermal/IAQ/comfort fallback

---

## 4. Climate Zone Cross-Walk

Every country uses a slightly different climate zone classification. The architect must translate.

### 4.1 ASHRAE 169 / IECC Climate Zones (1-8)

| Zone | Definition | Typical Tier-1 Cities |
|---|---|---|
| **1A** Very Hot Humid | CDD10C > 5000 | Singapore, Mumbai (coastal), Chennai |
| **1B** Very Hot Dry | CDD10C > 5000, HDD18C < 4500 | Doha, Dubai, Riyadh (south), Jeddah |
| **2A** Hot Humid | 3500 < CDD10C <= 5000 | Houston, Miami, Bangalore, Manila |
| **2B** Hot Dry | 3500 < CDD10C <= 5000, dry | Phoenix, Dubai (inland), Riyadh (most), Cairo |
| **3A** Warm Humid | 2500 < CDD10C <= 3500 | Atlanta, Tokyo, Shanghai, Sydney |
| **3B** Warm Dry | 2500 < CDD10C <= 3500, dry | Los Angeles, Madrid, Tabuk |
| **3C** Warm Marine | Coastal mild | San Francisco, Lisbon, Melbourne |
| **4A** Mixed Humid | 2000 < CDD10C, 3000 < HDD18C <= 4000 | Washington DC, New York, Seoul |
| **4B** Mixed Dry | Mixed climate, dry | Albuquerque |
| **4C** Mixed Marine | Mixed maritime | Seattle, London (margin to 5A), Vancouver |
| **5A** Cool Humid | 4000 < HDD18C <= 5000 | Chicago, Boston, Beijing, Toronto |
| **5B** Cool Dry | 4000 < HDD18C <= 5000, dry | Denver |
| **5C** Cool Marine | Cool maritime | Edinburgh, Hobart |
| **6A** Cold Humid | 5000 < HDD18C <= 7000 | Minneapolis, Stockholm, Helsinki, Munich, Berlin |
| **6B** Cold Dry | Cold dry | Calgary, Salt Lake City |
| **7** Very Cold | 7000 < HDD18C <= 9000 | Anchorage, Yakutsk, Inari |
| **8** Subarctic | HDD18C > 9000 | Fairbanks, Resolute, Norilsk |

### 4.2 Country-Specific Equivalent Zones

| Country | Native System | Bands |
|---|---|---|
| India | NBC 2016 + ECBC 2017 | 5 zones: Hot-Dry, Warm-Humid, Composite, Temperate, Cold |
| UAE | Estidama / Dubai Code | Single: hot-arid (CDH > 3000 K-h) |
| Saudi Arabia | SBC 601-CR | 3 zones: Z1 hot-humid coast (Jeddah/Jubail), Z2 hot-dry interior (Riyadh), Z3 cooler highlands (Abha, Taif, Tabuk) |
| USA | IECC / ASHRAE 169 | 8 numeric zones + A/B/C moisture sub-zones |
| UK | AD-L + SAP 10 | Single national methodology; regional weather files for SAP/SBEM (Region 1 Thames -- Region 21 W. Scotland) |
| Germany | GEG / DIN V 18599 + DIN 4108-6 | National test reference year cities for each region (Bremerhaven cold, Mannheim warm); 4 climate regions for SAP-equivalent |
| Singapore | BCA Green Mark + SS 530 | Single: tropical (1A ASHRAE) |
| Japan | Sho-Energy Ho + Notification 265 | 8 climate zones (Region 1 Hokkaido -- Region 8 Okinawa) |
| China | GB 50176-2016 Thermal Design | 5 zones: Severe Cold, Cold, Hot Summer Cold Winter (HSCW), Hot Summer Warm Winter (HSWW), Temperate |
| Australia | NCC + NatHERS | 8 climate zones (Zone 1 tropical Darwin -- Zone 8 alpine Mt Buller) |

When a user gives a city, resolve to BOTH the local zone and the ASHRAE zone -- design references in this plugin use both.

---

## 5. Standards Cross-Reference Index

When a query references a standard, this table identifies the issuing country and equivalent in other regimes.

### 5.1 Structural & Concrete

| Standard | Country | Equivalent / Successor |
|---|---|---|
| ACI 318-19 (concrete) | USA | EN 1992 (Europe), GB 50010 (China), IS 456 (India), AS 3600 (Australia), JASS 5 / AIJ-RC (Japan) |
| AISC 360-22 (steel) | USA | EN 1993, GB 50017, IS 800, AS 4100, AIJ-LSD |
| EN 1992 Eurocode 2 (concrete) | Europe | + national annexes; UK NA, German NA, Dutch NA etc. |
| EN 1993 Eurocode 3 (steel) | Europe | + national annexes |
| EN 1995 Eurocode 5 (timber) | Europe | + national annexes |
| EN 1996 Eurocode 6 (masonry) | Europe | + national annexes |
| EN 1998 Eurocode 8 (seismic) | Europe | + national annexes (UK NA waives in low-seismic zones) |
| IS 456:2000 (concrete) | India | Predates EN; aligned to BS 8110 lineage |
| IS 800:2007 (steel) | India | Aligned to BS 5950 lineage; revised toward limit state |
| IS 1893 series (seismic) | India | Substantially different from EN 1998; reduction factors differ |
| GB 50010-2010 (concrete) | China | Distinct theoretical basis (allowable stress historical, now ultimate limit state) |
| GB 50017-2017 (steel) | China | Adopts ULS; partial safety factors differ from EN |
| GB 50011-2010 (seismic) | China | 8-degree intensity scale (degree 6-9), distinct from EC8 |
| AS 3600-2018 (concrete) | Australia | Adopts ULS; design model close to ACI 318 |
| AS 4100-2020 (steel) | Australia | Close to AISC; minor partial factor differences |
| AS 1170 / AS 1170.4 (loads / seismic) | Australia/NZ | AS/NZS standard; distinct from EN 1991 |
| JASS / AIJ-RC (concrete) | Japan | Two-level seismic design embedded |
| AIJ-S (steel) | Japan | Two-level seismic + capacity design |
| SBC 304 (concrete) | Saudi | IBC/ACI 318 derived |
| SBC 306 (steel) | Saudi | AISC derived |

### 5.2 Fire

| Standard | Country | Equivalent |
|---|---|---|
| NFPA 101 Life Safety | USA | BS 9999 + BS 9991 (UK), DIN 4102 (DE), AS 1530/AS 4072 (AU) |
| IBC Ch. 7-10 (fire) | USA | NCC Section C/D/E (AU), AD-B (UK), GB 50016 (CN) |
| EN 13501-1 (reaction to fire) | EU | ASTM E84 (USA Class A/B/C), BS 476 (UK legacy) |
| EN 13501-2 (resistance to fire) | EU | UL 263 / ASTM E119 (USA), JIS A 1304 (JP) |
| AS 1530.1/.2/.3/.4/.8 | Australia | EN 13501 (full set) |
| BS 9999:2017 + BS 9991:2015 | UK | Performance-based fire engineering |
| BS 7974:2019 | UK | Application of fire engineering principles |
| ISO 23932 | Worldwide | Fire safety engineering -- general |
| GB 50016-2014 (2018 ed.) | China | Code for fire protection design of buildings |
| Japan Fire Service Act + FSL Enforcement Order | Japan | Distinct two-tier (preventive + structural) |

### 5.3 Accessibility

| Standard | Country | Equivalent |
|---|---|---|
| ADA 2010 + ANSI A117.1-2017 | USA | -- |
| BS 8300-1:2018 + BS 8300-2:2018 + AD-M | UK | -- |
| DIN 18040-1/-2/-3 | Germany | -- |
| EN 17210:2021 | EU | Accessibility and usability of the built environment |
| AS 1428.1-2021 + Premises Standards | Australia | -- |
| ISO 21542:2021 | Worldwide | Accessibility and usability of the built environment |
| GB 50763-2012 | China | Code for design accessibility |
| Heart Building Law 2006 + JIS S 0026 | Japan | -- |
| Harmonised Guidelines 2021 + RPwD Act 2016 | India | Rights of Persons with Disabilities Act |
| SBC 801 Part 11 | Saudi | ANSI A117.1-derived |
| Code on Accessibility 2019 (BCA) + Universal Design Index | Singapore | -- |
| Dubai Universal Design Code 2017 | UAE Dubai | -- |

### 5.4 Energy & Sustainability

| Standard | Country | Equivalent |
|---|---|---|
| ASHRAE 90.1-2022 + IECC 2024 | USA | -- |
| EN 16798 (energy performance) | EU | -- |
| AD-L 2021 + Future Buildings Standard 2025 | UK | -- |
| GEG 2023 + DIN V 18599 | Germany | -- |
| Section J NCC + NatHERS | Australia | -- |
| SS 530 + BCA Green Mark 2021 | Singapore | -- |
| Sho-Energy Ho 2015 + CASBEE | Japan | -- |
| GB 55015-2021 + GB 50189-2015 | China | -- |
| ECBC 2017 + ECBC-R 2018 + GRIHA + IGBC | India | -- |
| Estidama Pearl 2010 + Al Sa'fat 2016 + Mostadamah | UAE | -- |
| SBC 601-CR + Saudi Mostadamah Building Code | Saudi | -- |

---

## 6. Authority and Approval Bodies

When advising on permit, certification, or approval, route to the named authority.

| Country | Building Approval | Fire Approval | Energy Certification | Accessibility Certification |
|---|---|---|---|---|
| **India** | Municipal Corporation (e.g., MCGM Mumbai, MCD Delhi, BBMP Bangalore); Development Authority for new areas (DDA Delhi, MMRDA Mumbai) | State Fire Services Department + Chief Fire Officer NOC | BEE (Bureau of Energy Efficiency) for ECBC; GRIHA Council / IGBC for ratings | Chief Commissioner for Persons with Disabilities (CCPD) |
| **UAE** | Dubai: Dubai Municipality + Trakhees (DDA) for free zones; Abu Dhabi: DMT (Department of Municipalities and Transport); Sharjah: SBPD | UAE Civil Defence (federal); per-emirate Civil Defence sub-offices | Dubai: Al Sa'fat; Abu Dhabi: Estidama; both regulated by respective municipalities | Per-emirate accessibility offices; UAE federal MOCD |
| **Saudi Arabia** | Amana / Municipality (Amanat al-Riyadh, Amanat Jeddah etc.); Royal Commissions for special zones (NEOM, Yanbu) | General Directorate of Civil Defence (Mudiriat al-Difa'a al-Madani) | Saudi Energy Efficiency Center (SEEC); Mostadamah | Authority of People with Disabilities (Mowaamah for workplaces) |
| **USA** | City/County Department of Buildings (DOB NYC), Building Department LA, BPD Chicago etc.; state code adoption office | Local Fire Marshal + state Fire Marshal's office; AHJ (Authority Having Jurisdiction) per NFPA | DOE + state energy office; ASHRAE-certified commissioning agents for IECC/90.1 | Department of Justice (ADA enforcement); HUD (Fair Housing Act) |
| **UK** | Local Authority Building Control (LABC) OR Approved Inspector (private competition since 1985) | Same Building Control + Fire & Rescue Service consultation; BRR (Building Safety Regulator) for higher-risk buildings >18m | EPC issued by accredited assessor; SAP for dwellings, SBEM for non-domestic | Same Building Control + Equality and Human Rights Commission (enforcement) |
| **Germany** | Bauamt (per municipality) + state Oberste Bauaufsicht; Bauantrag submitted to local Bauaufsichtsbehoerde | Same Bauamt + Berufsfeuerwehr (city fire dept) review; Brandschutznachweis required | Energieausweis issued by qualified Energieberater; BAFA / KfW for incentive certification | Beauftragte fuer Belange behinderter Menschen (per state); review by Bauamt |
| **Singapore** | BCA (Building & Construction Authority) + URA (planning) | SCDF (Singapore Civil Defence Force) -- Fire Safety & Shelter Department | BCA Green Mark assessment; SCDF for ventilation interaction | BCA Code of Accessibility office + Universal Design Index audit |
| **Japan** | Tokutei Gyousei Cho (Designated Administrative Officer) -- typically prefecture or designated city; Confirmation Inspection Agency (private since 1998) | Same agency + Fire Department review (Shobosho); Article 7 inspection | Energy compliance by Designated Inspector under 2015 Act; CASBEE assessor | Heart Building Law approval by designated agency; specified housing under Choju Juutaku Hyouka |
| **China** | Local Construction Bureau (Jianshe Ju) + Planning Bureau (Guihua Ju); permit = Jianshe Gongcheng Guihua Xuke Zheng | Same + Public Security Fire Department (Gong'an Xiaofang); since 2019 transferred to Emergency Management Department | MOHURD (national) + provincial Construction Department; Green Building Label issued by CSGBC | Disability Persons' Federation (Canlianhui) + Construction Bureau |
| **Australia** | State Building Authority (Building Commission VIC, NSW Fair Trading, QBCC QLD); private Building Surveyor for assessment | State Fire & Rescue Service + Australian Building Codes Board for code; performance solutions via Fire Engineer (FPA Australia) | NCC Section J via Building Surveyor; NatHERS by accredited assessor (AAA) | Premises Standards via Building Surveyor; AAAA accredited Access Consultant; Human Rights Commission complaints |

---

## 7. Skill Routing Table

When detection succeeds, load the relevant country skill *immediately* and then layer specialised topical skills on top.

| If user query involves... | Always load | Then layer |
|---|---|---|
| Project in India + structural design | `country-india` | `structural-systems` (filter by IS codes) |
| Project in UAE + facade | `country-uae` | `building-envelope` (with hot-arid + sandstorm overlay) |
| Project in Riyadh + egress | `country-saudi-arabia` | `fire-life-safety` (filter by SBC 801) |
| Project in NYC + occupancy classification | `country-usa` | `building-codes` (filter by IBC 2024 + NYC BC 2022 amendments) |
| Project in London + Part L compliance | `country-uk` | `building-sustainability` (with AD-L + Future Buildings Standard) |
| Project in Berlin + accessibility | `country-germany` | `accessibility-design` (filter by DIN 18040-1/-2) |
| Project in Singapore + green rating | `country-singapore` | `building-sustainability` (filter by BCA Green Mark Platinum 2021) |
| Project in Tokyo + seismic | `country-japan` | `structural-systems` (filter by Building Standards Act Article 20 + AIJ) |
| Project in Shanghai + fire | `country-china` | `fire-life-safety` (filter by GB 50016-2014) |
| Project in Sydney + NCC | `country-australia` | `building-codes` + relevant NCC section |

If the project spans multiple jurisdictions (international firm, master plan with foreign anchor tenant, embassy/diplomatic), apply the **stricter** of the two for each parameter and document the source per item.

---

## 8. Decision Tree

```
USER QUERY ARRIVES
    |
    +--- Geographic signal detected? --- YES ---> Load country-<x> skill
    |                                                  |
    |                                                  +--> Continue with topical skill
    |                                                       (building-codes, fire-life-safety, etc.)
    |                                                       FILTERED through country lens
    |
    +--- NO signal detected ----> Ask "which jurisdiction?"
                                  OR apply IBC + Eurocodes + ISO defaults explicitly
```

Once a country skill is loaded:

```
COUNTRY SKILL ACTIVE
    |
    +--- Sub-national variant? (state, emirate, Land, prefecture, city)
    |       e.g., "Mumbai" --> MCGM DCPR 2034 supplement
    |       e.g., "Dubai" --> DBC 2021 vs Abu Dhabi ADIBC 2013
    |       e.g., "NYC" --> IBC 2024 + NYC BC 2022 amendments
    |       e.g., "Bavaria" --> BayBO + DIN-based Brandschutznachweis
    |       e.g., "California" --> IBC + Title 24 Part 6 (energy) + Part 11 (CalGreen)
    |
    +--- Version year of code in force?
    |       Older codes still in force for permits issued before transition.
    |       Practitioner must know permit-issue date vs current code year.
    |
    +--- Permit phase?
            Pre-application -- planning/zoning rules dominant
            Design Development -- structural + envelope + life-safety
            Construction -- materials testing + inspection
            Occupancy -- final certification + commissioning
```

---

## 9. Application Workflow

1. **Detect geography** using triggers in Section 1.
2. **Determine sub-national variation** using Section 2 archetype + country-skill Section 1.
3. **Identify code version in force** -- transition dates vary; ask user for permit application date if material.
4. **Apply country-skill clauses** as primary; supplement with `building-codes`, `fire-life-safety`, `accessibility-design`, `building-sustainability` for general principles only when country skill is silent.
5. **Cite clauses precisely**: use "[code title] [version year] [section/clause/article number]" format -- e.g., "IBC 2024, Section 1006.2.1, Table 1006.2.1" or "GEG 2023 paragraph 19".
6. **Flag stricter local override** -- if state/city code is more stringent than national, the local clause governs.
7. **Identify the approval authority** using Section 6.
8. **Cross-check with international reference** if the user requests benchmark (e.g., compare ECBC 2017 wall U-values vs ASHRAE 90.1-2022 vs Passive House).

---

## 10. When Geographic Foundations Should NOT Fire

- Pure theory/precedent question with no project context ("what is critical regionalism?" -- handled by `design-theory`)
- Pure typological question with no jurisdiction ("what is a courtyard plan?" -- handled by `spatial-planning` or `building-typology`)
- Mathematical/computational question ("calculate U-value of this assembly" -- handled by `architect-calculator`)
- Question explicitly framed as international/cross-border default ("what does Passive House require?" -- handled by `building-sustainability`)

In all other cases involving design decisions tied to a real location, this skill should fire.

---

*Sources: ICC (International Code Council) -- IBC/IRC/IECC/IFC 2024 editions; NFPA -- NFPA 101 2024 + NFPA 70 2023; BSI -- Building Regulations 2010 + Approved Documents A-S 2010-2025; DIBt + Lander -- MBO 2002/2019 + 16 Landesbauordnungen current editions; BIS -- NBC 2016 + IS codes current editions; BEE -- ECBC 2017 + ECBC-R 2018; MoHUA India -- Harmonised Guidelines 2021; SBCNC -- Saudi Building Code 2018 9-part series; UAE Civil Defence -- UAE Fire & Life Safety Code 2018; Dubai Municipality -- Dubai Building Code 2021; Department of Municipalities and Transport Abu Dhabi -- ADIBC 2013 + Estidama Pearl Rating; BCA Singapore -- Building Control Act + Building Control Regulations 2003 + 2021 update + SCDF Fire Code 2018; MLIT Japan -- Building Standards Act + Cabinet Order + recent Notifications; MOHURD China -- GB 50352-2019, GB 50016-2014 (2018 ed.), GB 50011-2010, GB 55015-2021; ABCB Australia -- NCC 2022 Volumes 1-3; ISO -- 21542:2021, 23932:2018; CEN -- EN 1990-1999 Eurocode suite current editions with national annexes; ASHRAE -- 90.1-2022, 62.1-2022, 55-2020, 169-2021.*
