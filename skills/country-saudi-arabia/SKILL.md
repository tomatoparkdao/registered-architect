license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
name: country-saudi-arabia
description: >
  沙特阿拉伯王国建筑规范与法规参考。涵盖沙特建筑规范（SBC）国家委员会（SBCNC）发布的系列规范：SBC 201 一般建筑、SBC 301 结构荷载（源自 ASCE）、SBC 302 混凝土（源自 ACI 318）、SBC 304 土与基础、SBC 305 砌体、SBC 306 钢结构（源自 AISC）、SBC 401 电气、SBC 501 机械、SBC 601 节能、SBC 701 给排水、SBC 801 消防（与 NFPA 对齐）、SBC 901 既有建筑、SBC 1001 绿色建筑；以及民防总局法规、沙特通用无障碍规范、Mostadamah（沙特绿色建筑计划）、Vision 2030 超级项目（NEOM、Qiddiya、红海、Diriyah、ROSHN）、Amana（市政）审批流程、沙特能效中心（SEEC）计划和皇家委员会管辖区（朱拜勒/延布/欧拉）。包括麦加/麦地那特殊限制（朝觐建筑法规）、Aramco 住宅标准参考，以及针对全国三类气候区的炎热干旱、沿海湿热和高地设计附加要求。
license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
# 国家：沙特阿拉伯王国

适用于沙特阿拉伯境内项目的建筑规范与法规参考。当提及沙特城市（利雅得、吉达、麦加、麦地那、达曼、塔布克、欧拉、NEOM、胡拜尔、宰赫兰）、SAR 货币、“Amana”/“Baladiya”、皇家委员会项目、Mostadamah、SBC 规范或沙特民防（Difa'a al-Madani）时启用本技能。

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 1. 法规层级

沙特阿拉伯采用**A 型体系（统一国家规范）**：自 2018 年起，**沙特建筑规范（SBC）**对全国所有新建工程强制适用。省级差异属于行政差异（由哪个 Amana 颁发许可），而非技术差异。

### 1.1 主管机构层级

```
第 1 级——国家层面
  市政、农村事务与住房部（MoMRAH）——城市政策与规范采用
    + 沙特建筑规范国家委员会（SBCNC）——发布 SBC 系列
  沙特标准、计量与质量组织（SASO）——材料/产品
  沙特能效中心（SEEC）——能源计划
  民防总局（Mudiriat al-Difa'a al-Madani）——消防审批
  残障人士事务机构——无障碍政策
  测量与地理空间信息总局——地图、坐标
  沙特工业城与技术区管理局（MODON）
  朱拜勒和延布皇家委员会（RCJY）——独立管辖
  欧拉皇家委员会（RCU）——独立管辖
  NEOM——独立监管框架
  Qiddiya 投资公司——独立监管框架
  Red Sea Global——独立监管框架
  Diriyah Gate 开发管理局——独立监管框架

第 2 级——区域层面
  Regional Council of each Emirate (Riyadh, Mecca, Medina, Eastern, Asir, Tabuk, Qassim,
    Hail, Northern Borders, Jazan, Najran, Al-Bahah, Jouf) -- regional planning oversight

第 3 级——地方层面（许可）
  Amana / Baladiyah (Municipality) -- per city:
    Riyadh: Amanat al-Riyadh (now under Royal Commission for Riyadh City - RCRC)
    Jeddah: Amanat Jeddah
    Mecca: Amanat al-Asimah al-Muqaddasah (Holy Capital Municipality)
    Medina: Amanat al-Madinah al-Munawwarah
    Dammam: Amanat al-Mintaqah al-Sharqiyah
  + Sub-municipalities (Baladiyah Far'iyah) for districts within metropolises

第 4 级——项目层面
  Civil Defence (Difa'a al-Madani) -- pre-design + occupancy NOC
  Saudi Electricity Company (SEC) -- electrical sanction
  National Water Co (NWC) / SWCC -- water/sewer
  Ministry of Tourism -- hotel licensing
  Ministry of Health -- hospital/clinic licensing
  Ministry of Education -- school/university licensing
  Ministry of Investment (MISA) -- foreign-owned projects
```

### 1.2 超级项目特殊管辖区

Vision 2030 has spawned several **non-Amana jurisdictions** with their own building authorities:

| 超级项目 | 主管机构 | 规范路径 |
|---|---|---|
| **NEOM** | NEOM 公司（自有城市主管机构） | NEOM 建筑规范制定中；过渡期间由项目专属主管机构审批；据报道与 SBC + Eurocode 对齐，并叠加定制高性能要求 |
| **The Line** | NEOM | 特殊结构性能标准（高度 200 m、长度 170 km） |
| **Qiddiya** | Qiddiya Investment Company | Qiddiya Design Guidelines + SBC overlay |
| **Red Sea / AMAALA** | Red Sea Global | Red Sea Sustainability Standards (target LEED Platinum equivalent) + SBC + bespoke coastal-eco overlay |
| **Diriyah** | Diriyah Gate Development Authority | Salmani Architecture Guidelines (Najdi vernacular + modern); UNESCO heritage area compliance |
| **AlUla** | Royal Commission for AlUla (RCU) | RCU Master Plan + Heritage Conservation Code; UNESCO World Heritage Hegra restrictions |
| **King Salman International Airport (KSIA Riyadh)** | RCRC + GACA | Aviation code overlay |
| **King Abdullah Economic City (KAEC)** | Emaar the Economic City | KAEC Guidelines + SBC |
| **Jubail Industrial City** | RCJY | RCJY-specific industrial codes + SBC |
| **Yanbu Industrial City** | RCJY | Same |

在上述任一地区，项目团队必须同时遵守**具体主管机构的设计指南和 SBC**——超级项目指南是叠加要求，不取代 SBC。

### 1.3 圣城限制（麦加与麦地那）

- **麦加和麦地那**：仅穆斯林可长期居住/工作；非穆斯林顾问通常通过持沙特执照的沙特合作方开展工作，并采用远程审查
- 两座城市在两大圣寺（Masjid al-Haram、Al-Masjid an-Nabawi）周边区域均有**特殊高度限制**——标高、材料、色彩和标识均由**麦加/麦地那皇家委员会**与沙特遗产管理局控制
- **朝觐建筑法规**——朝觐路线上的酒店和基础设施须满足特殊人流组织要求；容量计算遵循朝觐研究院方法

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 2. 沙特建筑规范结构

沙特建筑规范（SBC）于 2007 年首次发布，并于 2018 年进行重大修订；**2018 版**为现行版本（SBCNC 定期发布更新）。全国所有建筑均须符合。

### 2.1 九部分结构

| 规范 | 标题 | 对齐/来源 |
|---|---|---|
| **SBC 201-CR** | 一般建筑要求 | IBC 2018 |
| **SBC 301-CR** | 结构——荷载 | ASCE 7-16 |
| **SBC 302-CR** | 混凝土 | ACI 318-14 |
| **SBC 303-CR** | 基础/土力学 | -- |
| **SBC 304-CR** |（注：编号随版本变化；请核对现行版） | -- |
| **SBC 305-CR** | 砌体 | TMS 402/602 |
| **SBC 306-CR** | 钢结构 | AISC 360 |
| **SBC 307-CR** | 组合结构 | AISC 360 + AISI |
| **SBC 401-CR** | 电气 | NEC 2017 (NFPA 70) |
| **SBC 501-CR** | 机械 | IMC 2018 |
| **SBC 601-CR** | 节能 | IECC 2015 + ASHRAE 90.1-2013 基础，并按 SBC 修订 |
| **SBC 701-CR** | 给排水 | IPC 2018 |
| **SBC 801-CR** | 消防 | IFC 2018 + NFPA 交叉引用 |
| **SBC 901-CR** | 既有建筑 | IEBC 2018 |
| **SBC 1001-CR** | 绿色建筑 | LEED + ASHRAE 189.1 + IgCC |

**SBC-G** (general public) and **SBC-CR** (technical/engineer) are the two reading tiers. Practitioners use SBC-CR.

### 2.2 各城市采纳年份

While SBC is technically nationally mandatory since 2018, **enforcement strength varies**:
- **Riyadh, Jeddah, Dammam, Mecca, Medina**: full SBC enforcement at Amana level since 2019
- **Tier-2 cities**: enforcement strengthening 2020-2024
- **Tier-3 / rural**: SBC formally applies but on-site practice may lag
- **Giga-projects**: own authority + SBC overlay

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 3. 建筑规范核心要求（SBC 201 + 801）

### 3.1 使用分类（SBC 201 第 3 章，与 IBC 对齐）

| 组别 | 使用性质 | 子分类 |
|---|---|---|
| A | Assembly | A-1 (theaters), A-2 (food/drink), A-3 (worship/exhibit), A-4 (indoor sport), A-5 (outdoor) |
| B | Business | -- |
| E | Educational | up to 12th grade |
| F | Factory/Industrial | F-1 moderate, F-2 low hazard |
| H | High Hazard | H-1 to H-5 |
| I | Institutional | I-1 supervised; I-2 medical care; I-3 detention; I-4 day care |
| M | Mercantile | -- |
| R | Residential | R-1 transient, R-2 apartment, R-3 single-family, R-4 small care |
| S | Storage | S-1 moderate, S-2 low |
| U | Utility | -- |

### 3.2 高度与面积（SBC 201 第 5 章 + 表 504）

IBC-aligned; same Type IA through VB construction types; same height-vs-area-vs-occupancy-vs-construction matrix.

**Key Saudi-specific note**: Saudi practice often uses **Type IA or IB (fully fire-protected)** for most large buildings due to fire policy + insurance.

### 3.3 退界与 FAR——利雅得示例（RCRC）

| 分区 | FAR（有时称“建筑面积系数”） | 覆盖率 | 退界 | 高度 |
|---|---|---|---|---|
| R1别墅 | 1.0-1.5 | 50% | 前5 m、侧3 m | 12 m（通常2-3层） |
| R2（公寓） | 2.5-4.0 | 50-60% | 前5-7 m、侧3-5 m | 20-30 m |
| 商业中密度 | 4.0-6.0 | 70% | 按街道宽度公式 | 30-45 m |
| 商业高密度/CBD | 6-12 | 70-80% | 按分区要求，退界至少5 m | 100 m以上（按天际线规划） |
| 工业 | 0.8 | 50% | 前8 m | 视项目而定 |

利雅得的 **Riyadh Strategic Plan 2030** 和 **King Salman Renaissance Project (RCRC)** 正在重构分区。具体地块应确认当前的详细土地利用规划（DLUP）。

### 3.4 退界与 FAR——吉达

Jeddah's coastal high-density mid-rise pattern uses **Building Coefficient = FAR × site coverage**. Old city (Al-Balad UNESCO heritage zone) has strict conservation rules.

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 4. 防火与生命安全（SBC 801）

### 4.1 SBC 801-CR 结构

IBC/IFC-aligned. Key chapters:
- Ch. 4 General Building Heights and Areas (cross-ref SBC 201 Ch. 5)
- Ch. 5-9 Building Types and Specific Occupancies
- Ch. 10 Means of Egress (IBC Ch. 10 aligned)
- Ch. 11 Accessibility (overlap with Saudi Universal Accessibility Code)
- Ch. 14 Exterior Walls (NFPA 285 cladding alignment)
- Ch. 26-29 Fire-protection systems
- Ch. 33 Existing buildings
- Ch. 34 Special detailed requirements

### 4.2 疏散距离（SBC 801 第 10 章）

Aligned to IBC Table 1017.2 with Saudi modifications:

| 使用性质 | 有喷淋疏散距离（m） | 无喷淋（m） |
|---|---|---|
| A | 76.2 | 61.0 |
| B | 91.4 | 61.0 |
| E | 76.2 | 60.96 |
| F-1 | 76.2 | 60.96 |
| H-1 | 22.86 | 22.86 |
| H-2 | 30.48 | 30.48 |
| H-3 | 45.72 | 30.48 |
| I-2 | 60.96 | -- (req sprinklered) |
| M | 76.2 | 60.96 |
| R | 76.2 | 60.96 |
| S-1 | 76.2 | 60.96 |

### 4.3 高层建筑（SBC 801 第 4 章特殊条款）

- **Threshold**: building > 23 m (75 ft) above lowest fire-department access
- Required: 2 enclosed exit stairs (pressurized in many cases), 2-hour fire-rated lobbies, sprinklers throughout, voice evacuation, fire command centre, fire lift complying with EN 81-72 equivalent
- **Smoke control**: required atrium, mall, underground parking, high-rise per SBC 801 Ch. 28

### 4.4 外墙覆层（SBC 801 第 14 章，麦加塔吊火灾后）

Aligned to IBC Section 1402-1406 and NFPA 285:
- Buildings > 18 m (60 ft) require **NFPA 285 tested assembly** OR Class A1/A2 non-combustible
- **Storage building heat-released ban**: large-scale combustible cladding effectively prohibited
- **Approval**: Civil Defence reviews + Saudi Standards (SASO) certification of products

### 4.5 民防部门设计前审批

对于任何大型项目（高层、医院、学校、酒店、商场、工业及特殊危险用途）：
1. **Concept submission** to Civil Defence -- review of fire strategy
2. **Design Development submission** -- complete fire/life safety design package
3. **Construction-phase inspections**
4. **Pre-occupancy inspection** -- Civil Defence Completion Certificate required before Amana issues Occupancy Permit

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 5. 能源规范（SBC 601）

### 5.1 SBC 601-CR 结构

Aligned to **IECC 2015 + ASHRAE 90.1-2013** with Saudi modifications. Mandatory.

**沙特气候区（SBC 601-CR 第 301.1 节）：**

| 区域 | 类型 | 城市 | ASHRAE 169 等效区 |
|---|---|---|---|
| **Zone 1** | Hot-Humid (Coast) | Jeddah, Yanbu, Jubail, Dammam, Khobar | 1B-2A margin |
| **Zone 2** | Hot-Dry (Interior) | Riyadh, Hail, Buraydah, Hofuf | 1B |
| **Zone 3** | Cooler/Highland | Abha, Taif, Tabuk, AlUla, NEOM (mountains) | 2B-3B margin |

### 5.2 SBC 601 规定性围护结构目标

| 要素 | 第 1 区（沿海湿热） | 第 2 区（内陆干燥） | 第 3 区（高地） |
|---|---|---|---|
| Wall U (W/m2K) | 0.50 | 0.45 | 0.40 |
| Roof U (W/m2K) | 0.30 | 0.25 | 0.25 |
| Window U (W/m2K) | 2.20 | 2.20 | 2.20 |
| Window SHGC | 0.30 | 0.25 | 0.40 |
| WWR max | 40% | 30% | 40% |

(Values indicative; refer to SBC 601-CR current edition tables.)

### 5.3 Mostadamah（沙特绿色建筑计划）

Saudi's voluntary-tier green rating system. Categories: Site, Water, Energy, Materials, IEQ, Innovation. Pursued by government-funded projects and increasingly by private developers (NEOM, Red Sea Global require equivalent).

### 5.4 SEEC 计划

Saudi Energy Efficiency Center mandates appliance standards (SASO labels), industrial efficiency, district cooling for new developments > 2 million sqm conditioned space.

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 6. 无障碍（SBC 801 第 11 章 + Saudi Universal Accessibility Code）

### 6.1 框架

- **SBC 801 Chapter 11** -- aligned to ANSI A117.1-2009
- **Saudi Universal Accessibility Code (2010, revised)** -- by MoMRAH + Authority of People with Disabilities
- **King Salman Center for Disability Research** standards
- **Mowaamah Certification** -- accessibility certification for workplaces
- Saudi ratified the **UN Convention on the Rights of Persons with Disabilities** (2008)

### 6.2 关键尺寸

ANSI A117.1-aligned with Saudi additions:

| 要素 | 尺寸 |
|---|---|
| Accessible route | 1.22 m clear (1.5 m preferred) |
| Door clear width | 813 mm (32 in) -- with Saudi preference for 900 mm at primary entries |
| Ramp gradient | 1:12 max, 1:20 preferred for tactile/wayfinding |
| Ramp landing | 1.5 x 1.5 m every 9 m run |
| Lift cabin | Type B 1100 x 1300 mm (typical); stretcher type 1100 x 2100 mm (hospital) |
| Accessible WC | 2.0 x 2.0 m minimum; grab rails left + right; emergency call cord |
| Accessible parking | 3.66 m + 1.52 m access aisle (ANSI dimensions); covered preferred for sun protection |
| Tactile flooring | Per ISO 23599 + Saudi Code; at all level changes, doorways, lift entries, ramp ends |
| Mosque accessibility | Wheelchair-accessible prayer area at side (not back) per Saudi guidelines; ablution stations dual-height |

### 6.3 Mowaamah 工作场所认证

Three tiers: Bronze, Silver, Gold. Requires policy + physical environment + recruitment provisions. Issued by Ministry of Human Resources and Social Development. Many Saudi commercial buildings now target Mowaamah Gold.

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 7. 结构与荷载（SBC 301）

### 7.1 SBC 301——荷载

Aligned to ASCE 7-16:

| 荷载 | 沙特专项要求 |
|---|---|
| Dead and Live | ASCE 7-16 Ch. 3-4 |
| Wind | ASCE 7-16 + Saudi wind maps; 3-second gust mapped by region |
| Seismic | Generally low (SDC A-C); higher around Tabuk + Red Sea margin (NEOM site) and Asir region |
| Snow | Highland regions only (Abha, Tabuk highlands); SBC 301 maps |
| Dust/Sand | Site-specific additive; significant near Empty Quarter (Rub' al Khali) edges |
| Thermal | Critical for facades; design thermal range up to 60 C |

### 7.2 抗震分区

Saudi Arabia has **moderate seismicity along Red Sea margin** + Tabuk + Asir; low elsewhere.

| 地区 | 抗震设计类别（SDC） | 备注 |
|---|---|---|
| 中部高原（利雅得、布赖代） | A | 最低 |
| 东部省（达曼、胡拜尔） | A-B | 低 |
| Western Coast Jeddah | B-C | Moderate |
| Tabuk, NEOM region | C-D | Higher |
| 阿西尔高地（艾卜哈） | C | 中等 |
| Northern Borders | A | Lowest |

对于 SDC D 及以上等级，必须依据 SBC 302/306 进行完整延性构造，并按 ASCE 7 开展抗震分析。

### 7.3 材料

| 材料 | 规范 |
|---|---|
| Concrete | SBC 302 (ACI 318-14 derived) |
| Steel | SBC 306 (AISC 360 derived) |
| Masonry | SBC 305 (TMS 402/602 derived) |
| Foundations | SBC 304 -- soils, calcareous/sabkha + gypsum special provisions |
| Aluminium | AA Aluminium Design Manual (referenced) |

### 7.4 土壤

Saudi has problematic soils in many regions:
- **Sabkha** (coastal salt flats around Persian Gulf, Red Sea): high sulphate + chloride, weak bearing
- **Gypsum-bearing soils** (Riyadh, Eastern Province): solubility risk
- **Calcareous soils** (coastal): variable strength
- **Expansive clays** (some Eastern + Northern areas)

Sulphate-resistant cement per SASO/SBC 302 mandatory for coastal foundations.

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 8. 施工许可流程

### 8.1 步骤（以利雅得为例）

1. **Land documentation**: Saqq (Title Deed) verification with Ministry of Justice
2. **Survey + soil report** by certified office
3. **Concept design** + plot certificate (Maska al-Aradhi) check
4. **Schematic submission** to Amana (Belady portal in Riyadh) + Civil Defence pre-approval
5. **Detailed Design submission** -- structural calculations, MEP, fire engineering report, accessibility, energy compliance per SBC 601
6. **Building Permit issuance** by Amana
7. **Construction supervision contract** mandatory -- consultant signs off on phases
8. **Milestone inspections** -- foundation, structure, MEP, completion
9. **Pre-occupancy inspections** -- Civil Defence + Amana
10. **Occupancy Certificate (Shahadat Itham al-Bina'a)** by Amana
11. Utility connections SEC + NWC + others

### 8.2 特殊流程

- **Giga-projects**: own authority handles steps 4-10 internally; SBC compliance reviewed by their consultants
- **Royal Commission projects (RCJY, RCU, RCRC)**: separate workflow within commission's design + permit office
- **Mecca/Medina holy precincts**: additional Royal Commission approval; restrictions on construction during Hajj season (~6 weeks)

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 9. 气候设计参数

### 9.1 利雅得（第 2 区——内陆炎热干燥）

| 参数 | 数值 |
|---|---|
| Cooling design DB (0.4%) | 47-48 deg C |
| Cooling MCWB | 18-20 deg C (dry) |
| Heating design DB (99.6%) | 4-6 deg C |
| Diurnal swing | 15-22 deg C summer |
| Annual CDD (base 18C) | ~3500 |
| Annual HDD (base 18C) | ~500 |
| Annual solar (GHI) | 2150 kWh/m2 |
| Wind 3-sec gust | 38-42 m/s |
| Dust storms | 8-15 events/year |

### 9.2 吉达（第 1 区——沿海炎热湿润）

| Parameter | Value |
|---|---|
| Cooling design DB | 39-41 deg C |
| Cooling MCWB | 27-29 deg C (humid -- bigger challenge) |
| Heating design DB | 13-15 deg C |
| Annual CDD | 5000+ |
| 含盐空气 | 严重腐蚀风险 |
| 西罗科/哈姆辛风事件 | 沙尘+高温 |

### 9.3 塔布克 / NEOM（第 3 区——高地）

| Parameter | Value |
|---|---|
| Cooling design DB | 38-40 deg C |
| Heating design DB | -2 to 2 deg C (snow occasionally) |
| Wind | Highest in Kingdom (NEOM coastal-mountain interaction; significant offshore site potential) |
| Annual CDD | 2000-2500 |
| Annual HDD | 1500-2000 |

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 10. 快速数值参考

| 参数 | 数值 | 来源 |
|---|---|---|
| 住宅层高 | 3.0-3.3 m | SBC 201 + 通行做法 |
| 办公层高 | 4.0-4.5 m | SBC 201 + 沙特A级办公规范 |
| 酒店净高 | 最小2.7 m | SBC 201 |
| 住宅走廊宽度 | 1.118 m（44 in） | SBC 801 第10章 |
| 办公走廊宽度 | 1.118 m（44 in） | SBC 801 第10章 |
| 楼梯宽度 | 1.118 m（44 in） | SBC 801 第10章 |
| B类疏散距离（设喷淋） | 91.4 m | SBC 801 第10章 + IBC表1017.2 |
| 高层覆层 | NFPA 285组件或A1/A2类 | SBC 801 第14章 |
| 墙体U值（第2区——利雅得） | 0.45 W/m2K | SBC 601 |
| 玻璃SHGC（第2区） | 0.25 | SBC 601 |
| 住宅停车位 | 每户1.0-1.5个 | 当地Amana DCR |
| 清真寺——礼拜区面积 | 坐姿每人0.8-1.0 m²；站姿0.6 m² | Hajj Research Institute |

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 11. 应用流程

1. **确定 Amana / Royal Commission / 超级项目管辖区**。
2. **确认当前 Amana 执行的 SBC 版本**（通常为 2018 版及最新修订）。
3. 对一般要求和分类采用 **SBC 201**。
4. 始终对防火与生命安全采用 **SBC 801**。
5. 对能源合规采用 **SBC 601**。
6. 对结构采用 **SBC 301–306**。
7. 无障碍采用 **Saudi Universal Accessibility Code + SBC 801 第 11 章**。
8. 确认民防部门在概念、SD、DD、施工和竣工阶段的预审批流程。
9. 如位于相关辖区，确认 **RCRC / RCU / NEOM 专项指南**。
10. **引用条款**：例如 “SBC 201-CR 2018 Chapter 504”、“SBC 801-CR 2018 Section 1006.2”、“SBC 601-CR 2018 Table C402.1.4”、“Saudi Universal Accessibility Code 2010 Section 4.3.1”。

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 12. 权威来源

- **Saudi Building Code National Committee (SBCNC)**——sbc.gov.sa——全部 SBC 规范。
- **Ministry of Municipal, Rural Affairs and Housing (MoMRAH)** -- momrah.gov.sa
- **General Directorate of Civil Defence** -- 998.gov.sa
- **Saudi Standards, Metrology and Quality Org (SASO)** -- saso.gov.sa
- **Saudi Energy Efficiency Center (SEEC)** -- seec.gov.sa
- **Mostadamah Green Building Program** -- via MoMRAH
- **Amanat al-Riyadh / Royal Commission for Riyadh City (RCRC)** -- rcrc.gov.sa
- **Amanat Jeddah** -- jeddah.gov.sa
- **Amanat al-Asimah al-Muqaddasah (Mecca)** -- holymakkah.gov.sa
- **Amanat al-Madinah al-Munawwarah** -- amana-md.gov.sa
- **Eastern Province Amana** -- eamana.gov.sa
- **Royal Commission for AlUla (RCU)** -- rcu.gov.sa
- **NEOM** -- neom.com (developer regulatory portal)
- **Authority of People with Disabilities** -- apd.gov.sa
- **MISA (Ministry of Investment)** -- misa.gov.sa

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
*交叉引用：加载 `building-codes` 了解 IBC 基础（SBC 201 源自 IBC）；加载 `fire-life-safety` 了解一般疏散并结合 SBC 801；加载 `building-envelope` 处理炎热干燥及沿海湿热节点；加载 `building-sustainability` 比较 Mostadamah / LEED；加载 `accessibility-design` 了解 ANSI A117.1 / Saudi UAC；加载 `structural-systems` 了解 SBC 302/306 所采用的 ACI 318 + AISC 内容。*
#

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab AI建筑与室内设计总设计师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
