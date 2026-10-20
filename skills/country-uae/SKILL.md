---
name: country-uae
description: >
  United Arab Emirates architectural code and regulatory reference. Covers the federal regulatory
  framework (UAE Fire and Life Safety Code of Practice 2018 by General Civil Defence, Federal
  Law 29/2006 + 2/2014 + 1/2020 for People of Determination, ESMA standards) plus the seven
  Emirates' independent codes: Dubai Building Code 2021 (DBC), Dubai Civil Defence regulations,
  Trakhees regulations for free zones, Dubai Green Building Regulations & Specifications 2011
  + Al Sa'fat 2016, Dubai Universal Design Code 2017; Abu Dhabi International Building Code
  2013 (ADIBC, IBC-derived), Estidama Pearl Building Rating System 2010, DMA Accessibility
  Code; Sharjah Department of Planning and Survey rules; northern emirates' deferral patterns
  to Abu Dhabi or Dubai codes. Includes climate zone hot-arid design overlays, sandstorm/
  thermal expansion loads, ADM/DM approval workflows, RERA Dubai project registration,
  developer-master-developer-end-customer hierarchies (Emaar, Aldar, Nakheel masterplan
  compliance), DEWA/ADDC utility coordination, and the cross-walk between IBC, ASCE 7, NFPA,
  and UAE national amendments. Practitioner-grade clause-level reference for design teams
  working in any of the seven Emirates.
version: 1.1.0
license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
author: OmniAiLab
developer: Mochiball
agent_created: true
开源仓库: https://github.com/tomatoparkdao/registered-architect
---

# 国家：阿拉伯联合酋长国

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。

适用于七个酋长国（阿布扎比、迪拜、沙迦、阿治曼、乌姆盖万、哈伊马角、富查伊拉）的建筑规范与法规参考。当提及阿联酋城市、AED 货币、“Civil Defence”、“ADM”/“DM”/“DDA”、“Estidama”/“Al Sa'fat”/“Mostadamah”、“Trakhees”、酋长国开发商名称（Emaar、Aldar、Nakheel、Dubai Holding、Mubadala）或 DBC/ADIBC/UAE FLS 规范时启用本技能。

---

## 1. 法规层级

阿联酋采用 **C 型架构（联邦框架 + 酋长国自治）**。七个酋长国各自拥有建筑主管机构，每个酋长国内还可能存在次级管辖区（总体开发商、自由区）。

### 1.1 联邦级主管机构

| 主管机构 | 范围 | 主要工具 |
|---|---|---|
| **General Directorate of Civil Defence (GDCD)** | Fire & life safety, federal | UAE Fire and Life Safety Code of Practice 2018 (with addenda); pre-2018 version was 2011 + amendments |
| **Emirates Authority for Standardization & Metrology (ESMA, now MoIAT)** | Product/material standards | UAE.S series of standards; mandatory for many materials (cement UAE.S GSO 1914) |
| **Ministry of Energy and Infrastructure (MoEI)** | Federal infrastructure, building permitting policy | -- |
| **Ministry of Community Development (MoCD)** | Disability rights / accessibility | Federal Law No. 29/2006 + 14/2009 + 1/2020 (People of Determination); National Policy 2017 |
| **Federal Authority for Nuclear Regulation (FANR)** | Hazardous occupancies near Barakah | -- |
| **TDRA** | Telecoms/digital infra | -- |

### 1.2 酋长国级主管机构

| 酋长国 | 主要建筑主管机构 | 自由区/特殊主管机构 |
|---|---|---|
| **Abu Dhabi** | Department of Municipalities and Transport (DMT, formerly DPM/DUPM) -- which administers Abu Dhabi City Municipality (ADM), Al Ain Municipality, Al Dhafra Municipality | ADGM (Abu Dhabi Global Market), KIZAD, Khalifa Industrial Zone, Masdar City Free Zone |
| **Dubai** | Dubai Municipality (DM) -- DDM (Department of Development Management); Dubai Land Department (DLD) for ownership | Trakhees (Ports, Customs & Free Zone Corp -- PCFC) for: Jebel Ali Free Zone, Dubai Maritime City, Dubai Industrial City, Dragon City. Dubai Development Authority (DDA) for: Dubai Internet City, Dubai Media City, Knowledge Park, DIFC. DSO (Dubai Silicon Oasis Authority). MAHE (Dubai Healthcare City Authority - DHCA) |
| **Sharjah** | Sharjah Planning and Survey Department (Sharjah Municipality) | Sharjah Airport International Free Zone (SAIF), Hamriyah Free Zone (HFZA) |
| **Ajman** | Ajman Municipality and Planning Department | Ajman Free Zone Authority (AFZA) |
| **Umm Al Quwain** | UAQ Municipality | Ahmed bin Rashid Free Zone |
| **Ras Al Khaimah** | RAK Municipality | RAK Free Trade Zone (RAKEZ) |
| **Fujairah** | Fujairah Municipality | Fujairah Free Zone (FFZ), Creative City |

### 1.3 总体开发商层级

尤其在迪拜和阿布扎比，**总体开发商**拥有补充酋长国规范的设计指南（DCR）。项目团队必须同时遵守两者。

- **Dubai master developers**: Emaar (Downtown Dubai, Dubai Hills, Arabian Ranches), Nakheel (Palm Jumeirah, Deira Islands, Discovery Gardens), Dubai Holding (City Walk, Madinat Jumeirah, Bluewaters), DAMAC, Meraas, Dubai Investments
- **Abu Dhabi master developers**: Aldar (Yas Island, Saadiyat, Al Raha Beach, Reem Island), Mubadala (Saadiyat Cultural District, Masdar City), Tourism Development and Investment Company (TDIC, now part of Aldar)
- Each master developer publishes **Design Review Guidelines (DRG)** -- project-specific or community-wide
- The hierarchy on a typical project: UAE Federal Code -> Emirate Code -> Master Developer DRG -> sub-developer brief

### 1.4 自由区的区别

自由区对商业运营通常采用**较宽松的监管制度**，但建筑和生命安全规范相同或更严格。Trakhees（迪拜）、JAFZA、RAKEZ 等会发布自己的建筑法规，几乎都源自 IBC 或迪拜规范，并在防火、环境等方面增加更严格条款。

---

## 2. 迪拜——建筑规范核心要求

### 2.1 Dubai Building Code 2021（DBC）

**Dubai Building Code 2021** 取代了早期迪拜市政厅临时通告和“DM Drawing Notes”。其结构源自 IBC，但包含大量迪拜专项修改，由迪拜市政厅（DM）发布。

**Chapter structure (DBC 2021):**
1. Administration
2. Definitions
3. Use and Occupancy Classification
4. Special Detailed Requirements (high-rise, atria, parking, etc.)
5. General Building Heights and Areas
6. Types of Construction
7. Fire and Smoke Protection Features
8. Interior Finishes
9. Fire Protection Systems
10. Means of Egress
11. Accessibility
12. Interior Environment
13. Energy Efficiency
14. Exterior Walls
15. Roof Assemblies
16. Structural Design
17. Soils and Foundations
18. Concrete
19-25. Other material chapters
26. Existing Buildings
27. Encroachments
28. Sustainability
A-Z. Appendices including swimming pools, mosques, towers, etc.

### 2.2 使用分类（DBC 2021 第 3 章）

与 IBC 对齐，并作出以下阿联酋专项说明：

| DBC 组别 | IBC 等效组别 | 备注 |
|---|---|---|
| A-1 through A-5 | 集会 | A-3 包括宗教建筑（清真寺）——专项章节 |
| B | 办公 | 办公、专业服务 |
| E | 教育 | 最多至 12 年级 |
| F-1, F-2 | 工厂 | F-1 中等危险，F-2 低危险 |
| H | 高危险 | DM 还要求民防部门预先批准 |
| I-1 through I-4 | 机构 | I-1 监管照护；I-2 医院；I-3 拘留；I-4 日托 |
| M | 商业 | 零售、商场；阿联酋商场法规要求严格 |
| R-1 through R-4 | 住宅 | R-1 临时居住（酒店 >30 天）；R-2 公寓；R-3 独户住宅；R-4 小型辅助生活设施 |
| S-1, S-2 | 仓储 | -- |
| U | 公用设施 | -- |

### 2.3 高度与面积限制

DBC 采用 IBC 的“高度—结构类型”原则，但对高层建筑设置更严格上限：
- **高层建筑** = 高于消防部门最低进入标高 23 m（75 ft）的建筑——DBC 2021 第 4 章“特殊详细要求”
- **超高层** = 高度 >165 m——需第三方进行额外结构性能审查
- **巨型超高层** = 高度 >300 m——需按哈利法塔先例进行额外风洞试验、竖向疏散和避难层设计

### 2.4 退界与 FAR

迪拜综合采用 **plot ratio**（类似 FAR）、**建筑基底覆盖率**和**高度限制**。

| 分区类型 | 容积率 | 覆盖率 | 退界（典型） |
|---|---|---|---|
| Residential R1 (villa) | 0.5-0.8 | 30-40% | 6 m front, 3-5 m side/rear |
| Residential R2 (low-rise apt) | 1.5-2.5 | 50% | 6 m front, 3-5 m side/rear |
| Mixed-use mid-rise | 4-8 | 60% | 4-8 m all sides, building line per DM plot drawing |
| 塔楼区域（Marina、Downtown、JLT） | 8-20以上 | 25-40%（塔楼占地） | 塔楼退界随场地条件变化，裙房可至地界线 |
| Industrial | 0.4-1.0 | 40% | 6 m front, 4 m side/rear |

每个地块都有由迪拜土地局发布的 DM **Affection Plan**，其中规定精确控制指标。项目团队必须**首先**取得该文件。

### 2.5 迪拜专项关键条款

- **Burj Khalifa Effect**: nearby developments require shadow + wind impact studies referenced to DBC 2021 Appendix
- **Marina view corridors**: protected sight lines from waterfront
- **Solar reflectivity limits** for facades exceeding 30 m height (anti-glare to road traffic)
- **Cladding fire standard**: post-Marina Torch / Address Downtown fires, ALL external cladding (>= 15 m height) must comply with **EN 13501-1 Class A1 or A2-s1,d0** OR equivalent; **NFPA 285 testing** for assemblies; effectively prohibits combustible ACP cores

---

## 3. 阿布扎比——建筑规范核心要求

### 3.1 Abu Dhabi International Building Code 2013（ADIBC）

阿布扎比采用带有本地修改的 **2009 International Building Code**，发布为 **ADIBC 2013**（由城市规划与市政事务部发布，现为 DMT 的前身）。ADIBC 的结构与 IBC 章节对应。

配套规范：
- **AD International Residential Code (ADIRC)** -- aligned to IRC
- **AD International Fire Code (ADIFC)** -- aligned to IFC
- **AD International Mechanical Code (ADIMC)** -- aligned to IMC
- **AD International Plumbing Code (ADIPC)**
- **AD International Energy Conservation Code (ADIECC)** -- aligned to IECC
- **AD International Existing Building Code (ADIEBC)**

因此，阿布扎比从业者应以 IBC 2009 / 2012 / 2015 为基础，并叠加 ADIBC 修订表。**注意：截至 2025 年，ADIBC 尚未更新至 IBC 2018/2021/2024。**从业者必须核实当前采用状态。

### 3.2 Estidama Pearl Building Rating System（PBRS）

阿布扎比所有新建建筑均强制执行，不同于其他地区可选的 LEED。

| 建筑类型 | 最低 Pearl 等级 |
|---|---|
| 政府资助项目 | 2 Pearls |
| 所有私人新建项目 | 1 Pearl（最低合规等级） |

PBRS 包含 **7 个类别**：综合开发流程、自然系统、宜居建筑、珍贵水资源、高效能源、材料管理、创新实践。总计约 177 个分值，分为强制项和可选项，提交至市政与交通部。

### 3.3 ADIBC 退界与 FAR

阿布扎比规划依据 **Plan Abu Dhabi 2030** 及 Estidama 社区指南。退界和 FAR 按 DMT 为各分区发布的 **Detailed Master Plan (DMP)** 确定，因项目而异。Aldar 开发项目（Yas、Saadiyat、Al Raha Beach）还需遵守 Aldar DRG。

---

## 4. 防火与生命安全

### 4.1 UAE Fire and Life Safety Code of Practice 2018

**阿联酋项目引用最多的规范。**由民防总局（GDCD）发布，属于联邦规范，适用于全部 7 个酋长国。

Structure (2018 edition):
- Chapter 1: Administration
- Chapter 2: Definitions
- Chapter 3: Means of Egress
- Chapter 4: Fire Compartmentation and Construction
- Chapter 5: Special Hazards
- Chapter 6: Active Fire Protection Systems
- Chapter 7: External Wall Cladding
- Chapter 8: High-Rise Buildings (>23 m)
- Chapter 9: Specific Occupancies (mosques, hotels, malls, hospitals, schools)
- Chapter 10: Existing Buildings
- Chapter 11: Atriums, Stage and Performance Spaces
- Chapter 12: Materials Listing and Approvals
- Chapter 13: Marina, Boat and Harbour Facilities
- Chapter 14: Tents and Membrane Structures
- Chapter 15: Petrol Stations
- Chapter 16: Detention/Correctional
- Chapter 17: Emergency Power Systems
- Chapter 18: Smoke Control
- Annex A-Z: Testing, materials, design tables

### 4.2 疏散关键参数（UAE FLS 2018 第 3 章）

| 参数 | 数值 |
|---|---|
| 最大疏散行走距离（设喷淋 B/M/R） | 91 m (300 ft) |
| 最大疏散行走距离（设喷淋 A/E） | 76 m (250 ft) |
| 最大疏散行走距离（设喷淋 I-2） | 61 m (200 ft) |
| 最大共同行走路径 | 30.5 m (100 ft)，设喷淋 B/M/R |
| 最大尽端距离 | 15.2 m (50 ft)，大多数设置喷淋的使用组 |
| 楼梯宽度 | 按人员荷载容量确定（设喷淋 7.6 mm/人；未设喷淋 7.6 mm/人并加系数） |
| 住宅公共走道最小宽度 | 50 人以上 1118 mm (44 inch)；不超过 50 人 914 mm (36 inch) |
| 避难层（高层建筑） | 高度 >150 m 的住宅建筑每高出地面 25 层设置一层；容量按 UAE FLS 第 8 章计算 |

### 4.3 高层建筑（UAE FLS 第 8 章）

- **Threshold**: 23 m above lowest fire-department access
- Required: 2 enclosed exit stairs minimum (cross-vented or pressurized), 2-hour fire-rated lobbies, sprinklers throughout, fire pumps + redundant water supply, smoke control system, fire command centre on ground floor, dedicated firefighter lifts (per UAE FLS specification, similar to EN 81-72)
- **Compartmentation**: 2-hour minimum between floors and shafts
- **Refuge floor / sky lobby**: spaced per height (significant for towers >150 m)
- **Voice evacuation system** (UAE FLS Ch. 6)

### 4.4 外墙覆层（UAE FLS 第 7 章——Address Downtown 事件后的关键条款）

在 Address Downtown Hotel（2015 年跨年夜）和 Marina Torch（2015）火灾后，UAE FLS 2018 强制要求：
- **所有高度超过 15 m 的建筑：**外墙复合系统必须达到 **Class A1 或 A2 (EN 13501-1)** 不燃等级，或达到 Class C-s1,d0 并通过 **NFPA 285** 系统试验
- **所有外部板材：**必须来自批准清单（按系统制造并测试）
- **空腔隔断：**楼板和防火分隔墙处必须设置
- **追溯适用：**现有建筑的不合规覆层必须整改（执行力度因酋长国而异；迪拜较严格，其他地区较缓慢）
- **Approval**: cladding system must be type-approved by **Civil Defence**, listed on Civil Defence approved-supplier portal

### 4.5 喷淋与探测

- **Sprinkler standard**: NFPA 13 (with UAE FLS amendments for hot-arid climates -- antifreeze provisions, water-storage volumes)
- **Detection**: NFPA 72 (with UAE FLS amendments)
- **Notification**: voice evacuation per UAE FLS Ch. 6 for occupant load > 1000 or assembly group
- **Smoke control**: NFPA 92 + UAE FLS Ch. 18 for atria, parking garages, high-rises

---

## 5. 能源规范

### 5.1 迪拜——Al Sa'fat（强制）+ Dubai Green Building Regulations & Specifications 2011

**Dubai Green Building Regulations & Specifications 2011**——所有新建建筑的原始强制最低要求，2016 年更新。

**Al Sa'fat 2016**——迪拜绿色建筑评级体系，分级强制执行：
- **Bronze Sa'fa** -- mandatory minimum for all new buildings (replaces 2011 regulations as compliance route)
- **Silver Sa'fa** -- mandatory for government-funded buildings
- **Gold Sa'fa** -- voluntary upgrade
- **Platinum Sa'fa** -- voluntary highest

类别包括：生态、建筑活力、资源效能（能源、水、材料）和利益相关方参与。

**合规路径：**通过 DM 电子许可门户提交，在概念/方案设计、施工图设计和竣工后阶段分别提交 **Sa'fa Compliance Report**。

### 5.2 阿布扎比——Estidama Pearl Building Rating System

(See Section 3.2 above.) PBRS targets:
- Energy: 20-40% improvement over ASHRAE 90.1 base
- Water: 35-45% reduction (potable indoor + outdoor)
- Materials: regional sourcing, recycled content
- Indoor environment: per ADIBC + Estidama overlay

### 5.3 ASHRAE 90.1 基准

迪拜和阿布扎比均以 ASHRAE 90.1-2010（较旧项目）或 90.1-2016（因项目而异）为基准。除 Estidama/Sa'fa 评级叠加要求外，阿联酋没有独立的专有能源规范。

### 5.4 气候设计参数

在 IECC/ASHRAE 169 中，阿联酋属于单一气候区：**Zone 1B（极热、干燥）**；但沿海地区（迪拜、阿布扎比海岸、沙迦）具有强烈海洋湿度。设计条件如下：

| 参数 | 数值 |
|---|---|
| 制冷设计温度（迪拜） | 46-48°C，0.4%发生率干球温度 |
| 制冷设计湿球温度（迪拜，7月） | 30-31°C |
| 沙尘暴风事件 | 每年6-12次，峰值80 km/h |
| 年制冷度日（基准18°C） | >5000 |
| 年采暖度日（基准18°C） | 约100-300（基本可忽略） |
| 年全球水平太阳辐射 | 2200-2400 kWh/m² |
| 昼夜温差（室内） | 夏季15-20°C |

### 5.5 围护结构目标（Dubai DBC 2021 第 13 章 + Al Sa'fa）

| 要素 | 最大 U 值（W/m²K） |
|---|---|
| 屋顶（空调空间） | 0.30 |
| 外墙（空调空间） | 0.57 |
| 外墙（停车场、坡道） | 1.50 |
| 玻璃 | 1.90 |
| 玻璃 SHGC（最大值） | 0.32 |
| 可见光透射率 | 最小 0.20 |
| 天窗 | 1.90 |
| 天窗 SHGC | 0.27 |

---

## 6. 无障碍

### 6.1 联邦框架

- **Federal Law No. 29/2006** -- Protection of the Rights of People with Special Needs
- **Federal Law No. 14/2009** -- amendment
- **Federal Law No. 1/2020** (Ratification) -- ratified UN Convention on the Rights of Persons with Disabilities
- **National Policy 2017** -- "People of Determination" rebranding by HH Sheikh Mohammed bin Rashid

### 6.2 Dubai Universal Design Code 2017

由迪拜市政厅和社区发展局发布。迪拜项目团队将其作为**主要技术依据**。

关键尺寸：

| 要素 | 要求尺寸 |
|---|---|
| 无障碍通道宽度 | 净宽最小 1.5 m（优选 1.8 m） |
| 门净开口 | 室内 900 mm，入口 1000 mm |
| 坡道坡度 | 最大 1:12（优选 1:15）；每 9 m 设置 1.5 × 1.5 m 平台 |
| 横向坡度 | 最大 1:50 |
| 无障碍电梯轿厢 | 最小 1100 × 1400 mm（1 位轮椅使用者及陪同人员）；医院 1100 × 2100 mm |
| 电梯门 | 最小净宽 900 mm |
| 无障碍卫生间 | 2.0 m × 2.2 m（深度大于 UAE-DM 2014）；左右设置扶手；紧急呼叫 |
| 无障碍停车位 | 3.6 m × 5.0 m + 1.5 m 通道（或宽 6.0 m）；宜设置雨阳遮蔽 |
| 触觉地面 | 楼梯边缘、坡道、高差、门口和电梯入口前 60 cm 设置 |
| 饮水喷泉 | 双高度；较低出水口 AFFL 800 mm |

### 6.3 阿布扎比——DMA 无障碍规范

市政与交通部（DMT）发布 **Abu Dhabi Accessibility and Universal Design Guidelines 2014**（正在修订）。其尺寸规定与 ADA 2010 高度一致，并增加部分符合 Estidama 的要求（感官无障碍分值）。

### 6.4 配置数量

| 建筑类型 | 无障碍配置 |
|---|---|
| 停车位 | 总数的 2%，至少 1 个（迪拜）；每 50 个车位 1 个（阿布扎比） |
| 卫生间 | 每个公共楼层至少 1 个无性别无障碍卫生间；每组公共卫生间按性别各 1 个 |
| 酒店客房 | 总数的 1%，并按比例设置无障碍淋浴间；至少 1 间 |
| 集会座席 | 1%，分散布置并配陪同座席 |
| 旅游景点 | 友好感官环境的入口；所有公共信息处设置盲文标识 |

---

## 7. 结构与荷载

### 7.1 荷载

阿联酋通常采用 **ASCE 7-16** 进行荷载设计（部分项目引用 ASCE 7-22），并增加以下阿联酋专项要求：

| 荷载 | 规范参考 |
|---|---|
| 恒载与活载 | ASCE 7-16 第 3–4 章 |
| 风荷载 | ASCE 7-16 第 26–31 章；DBC 2021 附录中的迪拜专项 3 秒阵风图（约 46 m/s，0.4% 概率） |
| 地震 | 地震烈度低；阿联酋峰值地面加速度通常 < 0.10 g；通常采用 ASCE 7-16 C–D 类场地 |
| 沙尘 | 按场地确定的附加荷载；迪拜对幕墙板要求相当于 0.5 kPa |
| 温度 | ASCE 7 第 5 章（上拔）+ 对高度 >30 m 结构进行专项高温热膨胀分析 |

### 7.2 混凝土与钢结构

| 材料 | 规范 |
|---|---|
| Concrete | ACI 318-19 (Dubai); ACI 318-14 (older Abu Dhabi projects); some EN 1992 acceptance |
| Steel | AISC 360-22 / AISC 341-22 (seismic) |
| Composite | AISC 360-22 / Eurocode 4 |
| Cold-formed steel | AISI S100 |
| Aluminium | AA Aluminium Design Manual |
| Glass curtain wall | ASCE 7 + ASTM E1300 + AAMA standards |

### 7.3 土壤

阿联酋沿海地区（迪拜、沙迦、阿布扎比）广泛存在**含钙质和石膏土层**。主要关注点：
- Sulphate attack on concrete (high-sulphate-resistant cement, ACI 201, EN 197-1 SR cement)
- Chloride ingress (ACI 222R, BS 8500-1 Class XS)
- Bearing capacity often modest -- piled foundations common above 20 m height
- High water table (Marina, Bluewaters): permanent dewatering, tanking
- Dubai Marina/Palm: heavy reclaimed sand; dynamic compaction or stone columns standard for ground-improvement

---

## 8. 规划与房地产框架

### 8.1 迪拜房地产框架

- **Freehold ownership** available for designated areas (most Dubai by 2025; Abu Dhabi expanding)
- **Land Department (DLD)** issues Title Deeds; **Affection Plan** before design
- **RERA Dubai** (Real Estate Regulatory Authority -- under DLD) -- developer registration, escrow accounts, off-plan sales regulation
- **Dubai Strata Law** (Direction 3 of 2020 + Joint Property Law) -- for ownership in towers/communities

### 8.2 建筑面积（BUA）定义

Dubai uses "Built-Up Area" (BUA) as the carpet equivalent. Critical for FAR/coverage calculation:
- Includes interior spaces, balconies (covered), terraces (covered)
- Excludes mechanical floors, lobbies in some interpretations
- Each master developer may modify -- always confirm

### 8.3 迪拜审批流程

1. **Concept design** -> DM Building Affection Plan + Trakhees/DDA initial NOC (free zones)
2. **Master Developer DRG approval** (if applicable)
3. **Schematic design** -> Civil Defence pre-approval, DM electronic submission
4. **Detailed Design** -> DM Building Permit; structural calculations submitted; Civil Defence final permit drawing
5. **Construction** -> DM site inspections, milestone approvals (foundation, structure, MEP rough-in, completion)
6. **Completion** -> DM Building Completion Certificate (BCC), DEWA/ETISALAT connections, Civil Defence Completion Certificate, eventual Title Deed

### 8.4 阿布扎比审批流程

流程与迪拜类似，但每个阶段均强制执行 **Estidama Pearl 要求**：
- Pre-construction: 1 Pearl Design Rating minimum
- Construction: 1 Pearl Construction Rating
- Operations: 1 Pearl Operations Rating

---

## 9. 快速数值参考（阿联酋/迪拜默认）

| 参数 | 数值 | 来源 |
|---|---|---|
| 住宅层高 | 3.0–3.4 m | 常用值；DBC 净高最小 2.7 m |
| 商业层高 | 4.0–4.5 m | A 级办公标准 |
| 酒店净高 | 最小 2.7 m | 品牌标准 + DBC |
| 走道宽度 | 住宅公共区 1.5 m，酒店 1.8 m | DBC + UAE FLS |
| 疏散行走距离（设喷淋 B 组） | 91 m | UAE FLS 2018 第 3 章 |
| 楼梯宽度（集会人数 >300） | 1500 mm | UAE FLS 第 3 章 + DBC |
| 外墙（高层） | A1/A2 EN 13501-1 或 NFPA 285 系统试验 | UAE FLS 第 7 章 |
| 墙体 U 值（空调空间） | 0.57 W/m²K | DBC 2021 第 13 章 |
| 玻璃 SHGC | 最大 0.32 | DBC 第 13 章 |
| 风荷载 3 秒阵风（迪拜） | 46 m/s | DBC 附录 |
| 住宅停车比例 | 每户 1.0–1.5 个 ECS，访客 0.25 个 | DBC + 总体开发商 DRG |
| 办公停车比例 | 每 50–80 m² NLA 1 个 | DBC + 总体开发商 |

---

## 10. 应用流程

1. **确定酋长国**（迪拜、阿布扎比、沙迦等）及**子管辖区**（自由区或城市辖区）。
2. 如有，**确定总体开发商**并取得其 DRG。
3. 从 DLD（迪拜）或同等机构取得 **Affection Plan**。
4. **确认覆层合规体系**：UAE FLS 第 7 章始终适用。
5. **确认 Estidama Pearl 目标**（阿布扎比）或 **Sa'fa 目标**（迪拜）。
6. 防火与生命安全始终采用 **UAE FLS 2018**。
7. 结构、围护结构和一般要求采用所在酋长国建筑规范（迪拜 DBC 2021，阿布扎比 ADIBC 2013）。
8. 采用 **ASHRAE 90.1 + 阿联酋能源附加要求**。
9. **引用条款**：例如 “UAE FLS 2018 Chapter 3 Section 3.4.2”、“DBC 2021 Chapter 13.4.1”、“Estidama PBRS 2010 RE-1 Improved Energy Performance”、“ADIBC 2013 Section 1006.2”。

---

## 11. 权威来源

- **Dubai Municipality** -- dm.gov.ae -- e-permit portal, DBC 2021, Sa'fa
- **General Directorate of Civil Defence (UAE)** -- moi.gov.ae/civildefence -- UAE FLS Code 2018
- **Department of Municipalities and Transport Abu Dhabi (DMT)** -- dmt.gov.ae -- ADIBC, Estidama Pearl
- **Dubai Land Department (DLD)** + **RERA Dubai** -- dubailand.gov.ae
- **Estidama Pearl Rating Manual** -- via DMT publications portal
- **Trakhees** -- trakhees.ae
- **Dubai Development Authority (DDA)** -- dda.gov.ae
- **Federal Authority for Government Human Resources** -- for People of Determination policies
- **Ministry of Energy and Infrastructure (MoEI)** -- moei.gov.ae

---

*交叉引用：在迪拜（DBC 源自 IBC）或阿布扎比（ADIBC 源自 IBC 2009）工作时加载 `building-codes` 了解 IBC 基础；加载 `fire-life-safety` 了解叠加 UAE FLS 的一般疏散原则；加载 `building-envelope` 处理炎热干燥气候节点；加载 `building-sustainability` 比较 Sa'fa、Estidama 与 LEED；加载 `accessibility-design` 了解全球无障碍框架，再应用 Dubai UDC 2017 的专项要求。*
#

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
