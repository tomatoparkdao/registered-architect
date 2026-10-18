---
name: geographic-foundations
description: >
  Architect Skills 插件的自动激活地理背景路由器。检测建筑问题涉及的国家或司法辖区，并路由至相应国家法规档案（印度、阿联酋、沙特、美国、英国、德国、新加坡、日本、中国、澳大利亚）。编码全球法规格局：各主管机构发布哪些规范、国家/州/市级法规层级、按版本年份划分的规范采用状态、各辖区主要能源/抗震/消防/无障碍规范，以及国家规范与国际参考体系（IBC、NFPA、Eurocode、ISO、ASCE）的对应关系。精确记录各国采用的 Eurocode 国家附录、各州/酋长国/联邦州/都道府县发布的修订，以及国际标准通过引用适用的场合。当用户问题中出现地理背景（城市名、项目地点、语言线索、规范引用）时触发国家技能；未声明具体辖区时提供全球框架比较。
user-invocable: false
---

# 地理基础

自动激活层，用于检测地理背景，并将建筑问题路由至正确的国家法规档案。在任何规范、生命安全、结构或规划分析之前加载。

---

## 1. 地理背景检测

当用户问题包含以下任一信号时，应在应用 `building-codes`、`fire-life-safety` 或 `accessibility-design` 的通用内容*之前*，先路由至指定国家技能。

### 1.1 直接检测触发器

| 信号类别 | 示例 | 路由至 |
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

### 1.2 间接/推断触发器

- **场地气候描述**（“干热”“热带季风”“地中海”“温带海洋性”“亚寒带”“湿润亚热带”）与城市名称结合 → 解析城市 → 国家。
- **文化线索**（“vastu 合规”“qibla 朝向”“风水”“minka”“haveli”“带 majlis 的庭院住宅”）→ 推断国家/地区（分别对应印度、中东北非、中国/香港、日本、印度等语境）。
- **标准组织引用**（“BIS 规范”“DIN 测试”“JIS 标记”“GB 盖章”“BSI 认证”）→ 推断国家。
- **监管机构名称**（“民防审批”“Trakhees”“Tatweer”“MoHUA”“MLIT”“Bauamt”）→ 推断国家。
- **专有名词中的语言线索**（“brise-soleil”+“ECBC”印度用法；德语“rohbau”；日语“shikkui”；阿拉伯语“majlis”；印尼语“joglo”；新加坡“shophouse”）。

### 1.3 默认行为

如果在用户第一条消息后仍无法确定地理背景，只提出**一个**澄清问题：*“该项目属于哪个司法辖区？这会影响规范合规、结构设计荷载、能源目标和无障碍标准。”*

如果用户表述含糊或项目跨境（国际事务所、设计竞赛、总体规划研究），采用**国际参考规范组合**（IBC + Eurocodes + ASCE 7 + ASHRAE + ISO 21542 无障碍 + ISO 23932 消防），并明确说明假设。

---

## 2. 全球法规层级

每个国家属于五种法规原型之一。原型决定条文级问题的回答方式。

### 2.1 原型 A——统一国家规范

单一国家规范统一适用，不存在州/市级差异；城市通过引用方式采纳。

- **新加坡**（《建筑管制法》+《建筑管制条例》，由 BCA 统一管理）
- **沙特阿拉伯**（SBCNC 发布的沙特建筑规范 SBC 201-1001 系列，自 2018 年起在所有地区强制实施）
- **法国**（《建筑与住宅法典》；各省通过引用采纳——不属于本技能的一级国家，仅作背景参考）

### 2.2 原型 B——国家示范规范 + 州/省采纳

国家发布示范规范，但各州/省采纳某一版本或进行修改。从业者必须核对当地版本。

- **美国**（ICC 发布 IBC/IRC/IECC/IFC；各州/县采纳特定年份版本。加利福尼亚州另有 Title 24；纽约、芝加哥、佛罗里达发布重要修订。）
- **澳大利亚**（ABCB 发布 NCC 2022；各州通过《建筑法》管理，并在附录中发布州级差异。）
- **印度**（BIS 发布 NBC 2016；各州/联邦属地发布自己的建筑细则和开发控制条例——DCR/DCPR。规范本身不具有法律强制力。）
- **加拿大**（《加拿大国家建筑规范 2020》；各省采纳不同版本——安大略 OBC、不列颠哥伦比亚 BCBC、魁北克独立体系。不属于一级国家。）

### 2.3 原型 C——联邦框架 + 州/邦主权

国家拥有联邦框架，但实际建筑法规由州/邦主权决定，每个州/邦都有自己的主要法规。

- **德国**（MBO 仅为示范规范。16 个州各有自己的州建筑法规，例如巴伐利亚 BayBO、北威州 BauO NRW、柏林 BauO Bln，具有法律约束力。能源法规为联邦统一的 GEG。）
- **阿联酋**（联邦民防规范适用于消防；各酋长国有自己的建筑规范：迪拜建筑规范 2021、阿布扎比 ADIBC 等。）
- **英国**（《建筑法规 2010》适用于英格兰；威尔士、苏格兰、北爱尔兰分别适用独立体系——威尔士 AD、苏格兰技术手册、北爱尔兰技术手册。）

### 2.4 原型 D——国家集中管理 + 强制性条文

单一国家规范包含可凌驾于其他要求之上的“强制性条文”，同时允许地方补充规定。

- **中国**（住建部发布 GB 系列规范；红色文字的“强制性条文”在全国具有法律约束力。城市发布 DB 地方补充规定——北京 DB11、上海 DGJ08、广西 DBJ45——地方规定只能更严格。）
- **日本**（《建筑基准法》+内阁令+MLIT 告示；指定城市依据《城市规划法》享有规划自主权，但结构与安全条款为国家统一规定。）

### 2.5 原型 E——基于性能结果的法规

规范规定结果目标；视为满足的路径仅具指导性。工程化方案可通过认可的验证方法获得批准。

- **澳大利亚**（NCC 2022 完全基于性能；DTS 和性能解决方案均具有法律效力。）
- **英国**（2010 年后的 Approved Documents 属于指导文件；可通过 BS 7974 消防工程报告、EN 1990 结构性能等性能路径合规。）
- **新西兰**（NZBC，不属于一级国家。）

许多一级国家属于*混合型*：例如日本允许性能验证（1998 年以前为第 38 条；1998 年后由第 37 条型式认可和 BCJ 结构性能评价替代）。

---

## 3. 对比矩阵——一级国家

### 3.1 主要规范、能源规范、消防规范与无障碍规范

| 国家 | 主要建筑规范 | 能源规范 | 消防安全 | 无障碍 |
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

### 3.2 抗震、风荷载与雪荷载规范

| 国家 | 抗震 | 风荷载 | 雪荷载/气候荷载 |
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

### 3.3 跨境设计时的规范引用层级

为非一级国家设计时，采用以下后备链：

1. **地方规范**（如存在且已有可用译本）
2. **通过引用采纳的区域规范**（例如海湾国家常引用 IBC 或 SBC）
3. **《国际建筑规范》（IBC 2024）**——北美默认规范
4. **Eurocodes**（EN 1990-1999）——欧洲默认规范，已有 30 多个国家通过采纳使用
5. **ISO 标准**（ISO 21542 无障碍、ISO 23932 消防工程、ISO 22156 竹结构、ISO 5807 管道）——通用后备规范
6. **ASHRAE 90.1 + ASHRAE 62.1 + ASHRAE 55**——通用热工、室内空气质量和舒适度后备规范

---

## 4. 气候分区对照

每个国家采用略有不同的气候分区体系，建筑师必须进行转换。

### 4.1 ASHRAE 169 / IECC 气候区（1-8）

| 分区 | 定义 | 典型一级国家城市 |
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

### 4.2 各国等效分区

| 国家 | 本国体系 | 分区 |
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

当用户给出城市时，应同时确定当地分区和 ASHRAE 分区——本插件的设计参考同时使用两者。

---

## 5. 标准交叉引用索引

当问题引用某项标准时，本表用于识别其发布国家及其他体系中的等效标准。

### 5.1 结构与混凝土

| 标准 | 国家 | 等效/后继标准 |
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

### 5.2 消防

| 标准 | 国家 | 等效标准 |
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

### 5.3 无障碍

| 标准 | 国家 | 等效标准 |
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

### 5.4 能源与可持续性

| 标准 | 国家 | 等效标准 |
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

## 6. 主管与审批机构

在提供许可、认证或审批建议时，应路由至指定主管机构。

| 国家 | 建筑审批 | 消防审批 | 能源认证 | 无障碍认证 |
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

## 7. 技能路由表

检测成功后，应*立即*加载相关国家技能，再叠加专业主题技能。

| 如果用户问题涉及…… | 始终加载 | 然后叠加 |
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

如果项目跨越多个司法辖区（国际事务所、含外国主力租户的总体规划、使馆/外交项目），每项参数采用两者中**更严格**的要求，并逐项记录来源。

---

## 8. 决策树

```
用户提出问题
    |
    +--- 检测到地理信号？--- 是 ---> 加载 country-<x> 技能
    |                                                  |
    |                                                  +--> 继续加载主题技能
    |                                                       （building-codes、fire-life-safety 等）
    |                                                       通过国家视角进行筛选
    |
    +--- 未检测到信号 ----> 询问“哪个司法辖区？”
                                  或明确采用 IBC + Eurocode + ISO 默认值
```

加载国家技能后：

```
COUNTRY SKILL ACTIVE
    |
    +--- 是否存在次国家变体？（州、酋长国、联邦州、都道府县、市）
    |       e.g., "Mumbai" --> MCGM DCPR 2034 supplement
    |       e.g., "Dubai" --> DBC 2021 vs Abu Dhabi ADIBC 2013
    |       e.g., "NYC" --> IBC 2024 + NYC BC 2022 amendments
    |       e.g., "Bavaria" --> BayBO + DIN-based Brandschutznachweis
    |       e.g., "California" --> IBC + Title 24 Part 6 (energy) + Part 11 (CalGreen)
    |
    +--- 当前生效规范的版本年份？
    |       Older codes still in force for permits issued before transition.
    |       Practitioner must know permit-issue date vs current code year.
    |
    +--- 许可阶段？
            申请前——规划/分区规则为主
            设计深化——结构 + 围护 + 生命安全
            施工——材料测试 + 检查
            使用——最终认证 + 调试
```

---

## 9. 应用工作流

1. 使用第 1 节触发器**检测地理位置**。
2. 使用第 2 节法规原型 + 国家技能第 1 节**确定次国家差异**。
3. **确定现行规范版本**——过渡日期各异；如有实质影响，应询问用户许可申请日期。
4. **优先应用国家技能条文**；仅在国家技能未覆盖时，使用 `building-codes`、`fire-life-safety`、`accessibility-design`、`building-sustainability` 补充通用原则。
5. **精确引用条文**：采用“[规范名称] [版本年份] [章节/条款/条文编号]”格式，例如“IBC 2024，第 1006.2.1 节，表 1006.2.1”或“GEG 2023 第 19 段”。
6. **标记更严格的地方覆盖条款**——若州/市规范严于国家规范，以地方条款为准。
7. 使用第 6 节**确定审批主管机构**。
8. 用户要求进行基准比较时，**与国际参考进行交叉核对**（例如比较 ECBC 2017 墙体 U 值、ASHRAE 90.1-2022 与被动房标准）。

---

## 10. 地理基础不应触发的情形

- 没有项目语境的纯理论/先例问题（“什么是批判地域主义？”——由 `design-theory` 处理）
- 没有司法辖区的纯类型学问题（“什么是庭院平面？”——由 `spatial-planning` 或 `building-typology` 处理）
- 数学/计算问题（“计算该构造的 U 值”——由 `architect-calculator` 处理）
- 明确以国际/跨境默认标准提出的问题（“被动房有什么要求？”——由 `building-sustainability` 处理）

其他涉及真实地点设计决策的情形，均应触发本技能。

---

*来源：ICC（国际规范委员会）——IBC/IRC/IECC/IFC 2024 版；NFPA——NFPA 101 2024 + NFPA 70 2023；BSI——《建筑法规 2010》+ A-S 批准文件 2010-2025；DIBt + 各邦——MBO 2002/2019 + 现行 16 部邦建筑法规；BIS——NBC 2016 + 现行 IS 规范；BEE——ECBC 2017 + ECBC-R 2018；印度 MoHUA——《统一指南 2021》；SBCNC——2018 年沙特建筑规范九部分系列；阿联酋民防——《阿联酋消防与生命安全规范 2018》；迪拜市政府——《迪拜建筑规范 2021》；阿布扎比市政与交通部——ADIBC 2013 + Estidama Pearl 评级；新加坡 BCA——《建筑管制法》+《建筑管制条例 2003》+ 2021 更新 + SCDF 消防规范 2018；日本 MLIT——《建筑基准法》+ 内阁令 + 最新告示；中国住建部——GB 50352-2019、GB 50016-2014（2018 年版）、GB 50011-2010、GB 55015-2021；澳大利亚 ABCB——NCC 2022 第 1-3 卷；ISO——21542:2021、23932:2018；CEN——EN 1990-1999 Eurocode 系列现行版本及国家附录；ASHRAE——90.1-2022、62.1-2022、55-2020、169-2021。*
#

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab AI 建筑与室内设计总设计师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
