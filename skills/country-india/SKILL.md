---
name: country-india
description: >
  India-specific architectural code and regulatory reference. Covers the National Building Code
  of India (NBC 2016), Energy Conservation Building Code (ECBC 2017) and ECBC for Residential
  Buildings (ECBC-R 2018, also called Eco-Niwas Samhita), Indian Standards for structural
  design (IS 456:2000 concrete, IS 800:2007 steel, IS 875 Parts 1-5 loads, IS 1893:2016 seismic,
  IS 13920:2016 ductile detailing, IS 1904 foundations), the Rights of Persons with Disabilities
  Act 2016 and Harmonised Guidelines & Space Standards for Universal Accessibility 2021 (MoHUA),
  state-level Development Control Regulations (Mumbai DCPR 2034, Delhi MPD 2041, Bangalore BBMP,
  Chennai CMDA, Hyderabad GHMC, Kolkata KMC, Pune PMC, Ahmedabad AUDA), municipal building
  bye-laws, GRIHA and IGBC green rating systems, RERA (Real Estate Regulatory Authority) under
  the RERA Act 2016, fire safety per NBC Part 4 and state fire services rules, and the
  approval workflow involving Municipal Corporations, Development Authorities, State Fire
  Services NOC, and aviation/environmental clearances. Practitioner-grade clause-level
  reference for design teams working on projects in any Indian state or Union Territory.
license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---

# 国家：印度

适用于印度任何州或联邦属地项目的建筑规范与法规参考。当项目位于印度、提及印度城市、印度卢比或 “square feet built-up” / “carpet area” / “lakh” / “crore” 等面积或金额单位，或提及 NBC、ECBC、IS 系列规范时启用本技能。

---

## 1. 法规层级

印度采用 **B 型架构（国家示范 + 州采纳）**，国家框架与各州/市执行之间存在显著差异。

### 1.1 主管机构层级

```
LEVEL 1 -- 国家框架（指导性，州采纳后除外）
  - Bureau of Indian Standards (BIS) -- publishes NBC 2016 + IS codes
  - Ministry of Housing and Urban Affairs (MoHUA) -- urban policy
  - Bureau of Energy Efficiency (BEE) -- ECBC 2017, ECBC-R 2018
  - Ministry of Environment, Forest and Climate Change (MoEFCC) -- EIA notifications
  - National Disaster Management Authority (NDMA) -- guidelines
  - Directorate General of Civil Aviation (DGCA) -- height NOC near aerodromes

LEVEL 2 -- 州级框架（具有法律约束力）
  - State Town & Country Planning Department -- planning laws
  - State Fire Services -- Fire NOC, periodic renewal
  - State Pollution Control Board -- Consent to Establish/Operate
  - State Electricity Regulatory Commission -- electrical sanction

LEVEL 3 -- 地方框架（具有法律约束力，按项目适用）
  - Municipal Corporation OR Development Authority -- Building Permit
    + MCGM (Greater Mumbai), MCD (Delhi), BBMP (Bangalore), GCC (Chennai),
      GHMC (Hyderabad), KMC (Kolkata), PMC (Pune), AMC (Ahmedabad),
      MCC (Chandigarh), etc.
    + MMRDA, DDA, BDA, CMDA, HMDA, KMDA -- jurisdictional Development Authorities
  - District Magistrate / Collector -- land use, NA conversion
  - Local Fire Services -- on-site NOC

LEVEL 4 -- 项目专项许可
  - EC (Environmental Clearance) for >20,000 sqm built-up (EIA 2006 + amendments)
  - Aviation NOC if within 20-km of aerodrome reference point
  - Heritage NOC if within heritage precinct (ASI/SHA)
  - Coastal Regulation Zone (CRZ) clearance per CRZ 2019
  - Forest clearance if on forest land
  - Defence/Army NOC if within designated zones
  - RERA registration if >500 sqm or >8 apartments (RERA Act 2016)
```

### 1.2 NBC 2016 的法律地位

《印度国家建筑规范 2016》（NBC 2016，BIS SP 7:2016，共两卷、约 3,500 页）在国家层面属于*指导性文件*，仅在以下情况下具有约束力：

- 州政府正式采纳（大多数州已全部或部分采纳）。
- 市政机构在 Building Bye-Laws 中引用（大多数主要城市如此）。
- 法院命令或 RERA 裁决引用具体条款。

NBC 2016 分为 **12 个部分**（P1 至 P12），其中若干部分进一步划分为章节：

| 部分 | 标题 | 内容 |
|---|---|---|
| Part 1 | 定义 | 术语表、引用 |
| Part 2 | 管理 | 许可流程、审批机构职责 |
| Part 3 | 开发控制规则 + 建筑一般要求 | 退界、FAR、开放空间、通用要求 |
| Part 4 | 防火与生命安全 | 防火分隔、出口、防火等级、喷淋（引用最多的部分） |
| Part 5 | 建筑材料 | IS 规范材料要求 |
| Part 6 | 结构设计 | 第 1 节荷载；第 2 节土壤与基础；第 3 节木结构；第 4 节砌体；第 5 节混凝土；第 6 节钢结构；第 7 节预制；第 8 节玻璃 |
| Part 7 | 施工管理、实践与安全 | 工地安全、脚手架、拆除 |
| Part 8 | 建筑设备 | 第 1 节照明；第 2 节电气；第 3 节空调；第 4 节声学；第 5 节给排水；第 6 节电梯/自动扶梯 |
| Part 9 | 给排水设备 | 第 1 节给水；第 2 节排水；第 3 节固体废物；第 4 节燃气供应 |
| Part 10 | 景观、标志和户外展示 | 街道景观要求 |
| Part 11 | 可持续性路径 | NBC 的可持续框架（早于 GRIHA 强制要求） |
| Part 12 | 资产与设施管理 | 运营与维护 |

### 1.3 各州规范采纳状态

| 州 / 联邦属地 | NBC 2016 采纳情况 | ECBC 2017 是否强制 | 备注 |
|---|---|---|---|
| Maharashtra | 完整采纳（UDCPR 2020） | 是，自 2018 年 | 孟买采用 MCGM DCPR 2034；州内其他地区采用 Unified DCPR 2020 |
| Delhi NCT | 通过 MPD 2041 + Building Bye-Laws 2016 完整采纳 | 是，自 2017 年 | DDA/MCD 执行 NBC；遗产区域需 DUAC 审查 |
| Karnataka | 通过 KMBBL 2003（更新版）完整采纳 | 是，自 2018 年 | 班加罗尔分区规定由 BDA + BBMP 细则执行 |
| Tamil Nadu | 通过 TNCDBR 2019 完整采纳 | 是，自 2018 年 | 金奈依据 CMDA Master Plan-II + TN Combined DCR & Building Rules 2019 |
| Telangana | 通过 GO 168/2012 及更新版完整采纳 | 是，自 2017 年 | HMDA / GHMC 细则 + 2020 修订 |
| Andhra Pradesh | 通过 APBBR 2017 + 2020 修订完整采纳 | 是 | APCRDA 管辖 Amaravati / VMRDA 管辖 Vizag |
| West Bengal | 通过 KMC Building Rules 2009 及修订完整采纳 | 是，自 2019 年 | 加尔各答由 KMC + KMDA 管辖；其他地区采用州 PWD 规则 |
| Gujarat | 通过 GDCR 2017 完整采纳 | 是，自 2018 年 | Ahmedabad AUDA、Surat SUDA、Vadodara VUDA |
| Rajasthan | 通过 Rajasthan Building Bye-Laws 2020 完整采纳 | 是 | JDA 管辖 Jaipur，AUIT 管辖 Ajmer，JODA 管辖 Jodhpur |
| Uttar Pradesh | 通过 UPABBR 2008 及修订完整采纳 | 是，自 2018 年 | Lucknow LDA、NOIDA、Greater NOIDA 主管机构 |
| Kerala | 通过 KMBR/KPBR 2019（2024 修订）完整采纳 | 是，自 2019 年 | 地方自治政府部门监督 |
| Punjab | 通过 PMBBR 2018 完整采纳 | 是 | 各市政公司存在差异 |
| Haryana | 通过 HBC 2017 + 2019 修订完整采纳 | 是，自 2017 年 | HUDA / HSVP 负责新分区，GMDA 负责 Gurugram |
| Madhya Pradesh | 通过 MPBBL 2012 及修订完整采纳 | 是 | 大城市以 TPS 方案为准 |
| Bihar | 部分采纳；State Building Bye-Laws 2014 | 部分（仅大型商业） | BMC Patna；基础设施较旧 |
| Odisha | 通过 OBBL 2018 完整采纳 | 是，自 2019 年 | BDA Bhubaneswar、CDA Cuttack |
| Assam | 部分采纳；ABBL 2014 | 有限 | GMDA Guwahati；东北各州常参照阿萨姆执行 |
| 所有东北州 | 不一；多数参照 NBC + Assam 模式 | 有限 | 采纳情况不一 |
| Jammu & Kashmir | 2019 年重组；JK Building Bye-Laws 修订中 | -- | 联邦属地管理；J&K Master Plan 2035 生效 |
| Chandigarh UT | Chandigarh Building Rules (Urban) 2017 | 是 | 保留勒·柯布西耶分区规划 |
| Goa | GTCP Act 1974 + Regulations 2010 + 2020 修订 | 部分 | 沿海限制优先 |

针对具体项目提供建议时，必须确认：(i) 所属州；(ii) 所在城市的市政公司或开发主管机构；(iii) Building Permit 申请日期（适用规范版本取决于申请日期）。

---

## 2. 建筑规范核心要求（NBC 2016 第 3、4 部分）

### 2.1 使用分类（NBC 2016 第 4 部分 3.1）

NBC 定义 **9 个使用组（A 至 I）**：

| 组别 | 使用性质 | 子分类 | 示例 |
|---|---|---|---|
| **A** | 住宅 | A-1 住宿；A-2 独户/双户；A-3 宿舍；A-4 公寓；A-5 酒店；A-6 星级酒店 | 公寓、旅舍、酒店 |
| **B** | 教育 | B-1 高中及以下学校；B-2 其他教育建筑（学院、大学） | 学校、学院 |
| **C** | 机构 | C-1 医院/疗养院；C-2 看护机构；C-3 监禁机构 | 医院、监狱、孤儿院 |
| **D** | 集会 | D-1（>1000 人）；D-2（>300、≤1000）；D-3（>100、≤300）；D-4（≤100）；D-5 户外集会；D-6 影院/剧院；D-7 体育场 | 剧院、厅堂、婚礼大厅 |
| **E** | 办公 | E-1 办公室；E-2 实验室；E-3 研究；E-4 电话呼叫中心 | 办公楼、IT 园区 |
| **F** | 商业 | F-1 零售（小型）；F-2 批发；F-3 超市/百货商店 | 商店、商场 |
| **G** | 工业 | G-1 低危险；G-2 中等；G-3 高危险 | 工厂、车间 |
| **H** | 仓储 | H-1（低）；H-2（中等） | 仓库 |
| **I** | 危险 |（专项监管） | 化工厂、军火库、油气设施 |

### 2.2 高度与面积限制

NBC 2016 **没有**与 IBC 表 504 等效的单一“高度—结构类型”表；高度和面积限制分别嵌入第 4 部分（防火）、第 3 部分（开发控制）及各州 DCR。

**关键阈值：**

| 阈值 | 触发条件 | 来源 |
|---|---|---|
| **高层建筑** | 住宅、酒店高度 >= 15 m，或其他使用组 >= 18 m（自平均地坪起算） | NBC 2016 Part 4, 3.1.40 |
| **特殊建筑** | D-1/D-2/D-6 集会组、含危险材料的 E 组工厂、H 组、面积 >500 m² 且高度 >9 m 的酒店、高度 >9 m 的医院和学校、面积 >300 m² 的地下室 | NBC 2016 Part 4, 3.1.84 |
| **EIA 阈值** | 建筑面积 >20,000 m²（按 EIA Notification 2006 及 2014、2020 修订）——B2 类由州 EIA 机构审批；>150,000 m² 或特定行业——A 类由国家 MoEFCC 审批 | EIA Notification 2006（及修订） |
| **消防 NOC 要求** | 所有高层、特殊建筑、医院、>=20 间客房的酒店；部分州对低于该阈值的项目也要求 | NBC 2016 Part 4 + 州消防规则 |
| **RERA 注册** | 项目地块 >500 m² 或住宅 >8 套 | RERA Act 2016 Sec. 3 |
| **航空 NOC** | 机场基准点 20 km 内建筑（因机场分类而异） | DGCA NOCAS 2.0 门户；并受航空运营方限制 |

### 2.3 退界与 FAR（示意值——以州级 DCR 为准）

印度各州对 FAR（Floor Area Ratio，容积率）的计算方式不同。有的计入阳台/电梯，有的排除。*必须始终向当地 DCR 核实。*

| 城市 | 典型住宅 FAR | 典型商业 FAR | 备注 |
|---|---|---|---|
| **Mumbai (MCGM DCPR 2034)** | Base 1.33, Permissible 3.0 (with premium FSI + TDR), up to 5.0 in TOD | Base 1.33, up to 5.0 with premium | Distinction: "Built-up FSI" vs "Composite FSI"; transit-oriented zones higher |
| **Delhi (MPD 2041 + Unified Building Bye-Laws 2016)** | 200-350% (varies by plot size); up to 400% mixed-use | 200-450% | "FAR" used, includes mezzanine; balconies excluded if <=10% |
| **Bangalore (BBMP Bye-Laws 2003)** | 1.75 (up to 3.25 for big plots), TDR-augmented | 1.75-3.25 | RMP 2031 increased FAR with road width |
| **Chennai (CMDA Second Master Plan)** | 1.5-2.0 (special buildings up to 2.5) | 2.0-3.5 | Premium FSI 50% extra on payment |
| **Hyderabad (GO 168 + GHMC)** | Unlimited (subject to setback + height + insurance), within Master Plan | Unlimited subject to same | Insurance premium based on height |
| **Kolkata (KMC Building Rules 2009)** | Varies by ward; 1.5-3.5 | 2.0-4.0 | "FAR" computed on plot area + 25% road area |
| **Pune (Maharashtra UDCPR 2020)** | 1.1-2.5 base, premium up to 3.5 | Same | Aligned with MCGM concept of permissible vs base |
| **Ahmedabad (Gujarat GDCR 2017)** | Up to 2.7 (RC), 4.0 (CBD) | Up to 5.0 in CBD/TOD | Aligned with state CGDCR |
| **Gurugram (HBC 2017)** | 1.45-1.75 (varies by zone) | 1.75-3.5 | Floor-Area-Ratio + ground coverage limits |
| **NOIDA (UP)** | 2.75-3.5 (group housing) | 4.0 (mixed-use) | NOIDA Building Regulations 2010 + amendments |

印度 DCR 通常还限制：
- **建筑覆盖率**（与FAR分开）：住宅通常25-50%，商业50-60%
- **退界：**前3-12 m、侧3-6 m、后3-6 m（取决于地块面积及临接道路）
- **高度：**通过FAR、退界和建筑覆盖率的相互作用隐含确定；仅特殊区域（遗产、航空、国防）明确规定
- **停车：**每户1.0-2.0辆（因城市而异）；商业每50-100 m² GFA 1辆；ECS=等效车位

---

## 3. 防火安全（NBC 2016 第 4 部分 + IS 15683）

### 3.1 疏散距离

**NBC 2016 第 4 部分表 7：**

| 使用性质 | 无喷淋（m） | 有喷淋（m） |
|---|---|---|
| A 组住宅 | 22.5 | 30.0 |
| B 组教育 | 22.5 | 30.0 |
| C 组机构 | 22.5（限单层） | 30.0 |
| D 组集会 | 22.5（配烟感时最大值） | 30.0 |
| E 组办公 | 30.0 | 45.0 |
| F 组商业 | 22.5 | 37.5 |
| G 组工业 | 按危险性变化 | 变化 |
| H 组储存 | 变化 | 变化 |
| I 组危险品 | 18.0 | 22.5 |

（交叉参考：IBC 2024 对设喷淋的商业建筑允许 76.2 m。印度要求明显更严格。）

### 3.2 疏散方式——楼梯容量（NBC 2016 第 4 部分 4.4）

- **楼梯最小宽度：**高层住宅1.5 m；医院2.0 m；教育建筑集会人数>300时2.0 m；办公1.5 m
- **出口门最小宽度：**住宅1.0 m；机构/集会主出口1.5 m；大型集会2.0 m
- **尽端走廊最大长度：**大多数用途6.0 m；机构建筑（C组）4.5 m
- **容量系数：**楼梯每单位60人（一个宽度单位=500 mm）；门每单位75人。因此1.5 m楼梯=3单位=180人；1.0 m门=2单位=150人。
- **避难区：**高度>=24 m的高层住宅（A组）每层必须设置；按服务楼层上部每名使用者0.3 m²计算；邻近消防疏散楼梯，并通过2小时耐火前室进入。（重点：孟买/德里执行优先。）

### 3.3 防火分隔

**NBC 2016 第 4 部分表 22：**

| 建筑类型 / 高度 | 要求耐火等级 |
|---|---|
| 非高层、非特殊建筑 | 结构 2 小时，防火分隔墙 2 小时 |
| 高层住宅（15–45 m） | 2 小时 |
| 高层住宅（>45 m） | 3 小时 |
| 高层非住宅（18–45 m） | 2 小时 |
| 高层非住宅（>45 m） | 3 小时 |
| 特殊建筑 | 4 小时（大型集会、医院） |
| 地下室（≥2 层） | 外部 4 小时；设置自动喷水灭火系统 |

**Compartment size limits:** maximum 750 sqm per compartment in basement; 2,000 sqm above grade for office (E); 1,500 sqm assembly (D); 1,000 sqm hospital (C).

### 3.4 喷淋系统要求

- Mandatory for all **High-Rise Buildings** >= 15 m (Group A), >= 18 m others
- Mandatory for all **Special Buildings** regardless of height
- All **basements** >= 300 sqm
- All **hospitals** > 9 m height
- All **hotels** > 15 m height OR > 30 keys

喷淋系统按 **IS 15105:2002（喷淋）** + **TAC（Tariff Advisory Committee）Rules** 进行设计，以满足消防保险要求。消防工程中有时也参考 NFPA 13。

### 3.5 消防电梯（NBC 2016 第 4 部分 4.5）

- Required: all high-rise buildings (>15 m residential, >18 m others)
- Minimum 1 fire lift per 1,200 sqm floor area, minimum 2 per building
- Capacity: minimum 545 kg, dimensions per IS 14665
- Speed: 1.0 m/s minimum, to be able to reach top floor in <= 1 minute
- Fire lift lobby: enclosed, 2-hour fire-rated, positive pressurized (50 Pa)
- Communication: dedicated firefighter intercom

### 3.6 避难层（高层 > 24 m，NBC 第 4 部分 4.6.6.4）

- **Refuge floor** required every 24 m (Mumbai stricter: every 7 floors via DCPR 2034)
- Refuge area: minimum 15 sqm OR 0.3 sqm/person served, whichever larger
- Refuge floor not to be used for any other purpose (no storage, no AHU); fully ventilated to atmosphere

---

## 4. 能源规范

### 4.1 ECBC 2017（商业建筑）

**Energy Conservation Building Code 2017**（BEE、MoP）适用于：
- 连接负荷 >= 100 kW 或合同需求 >= 120 kVA 的建筑/建筑群
- 或建筑面积 >= 500 m²

截至 2025 年，在已采纳该规范的 21 个州，适用于**所有新建商业建筑**。目标是相对于基准情景节能 25–50%。

**三个合规等级：**

| 等级 | 相对基准的节能率 | 标记 |
|---|---|---|
| **ECBC** | 25% | ECBC-compliant |
| **ECBC+** | 35% | ECBC+ |
| **SuperECBC** | 50% | SuperECBC |

**五个气候区（ECBC 2017 + IS 3792:1978）：**

| 区域 | HDD（基准 21C）+ CDH（基准 25C） | 城市 |
|---|---|---|
| **炎热干燥** | CDH > 6000 K-h，HDD 低 | Ahmedabad、Jaipur、Nagpur、Jodhpur |
| **温暖湿润** | 高湿度（>= 75%），CDH > 6000 | Mumbai、Chennai、Kolkata、Goa、Vizag |
| **综合** | 极端条件混合 | Delhi、Lucknow、Kanpur、Allahabad |
| **温和** | 全年温度适中 | Bangalore、Pune、Hyderabad（边缘）、Coimbatore |
| **寒冷** | HDD > 3000 | Shimla、Srinagar、Leh、Gangtok、Darjeeling |

**ECBC 2017 规定性 U 值目标（W/m²K）：**

| 要素 | 炎热干燥 | 温暖湿润 | 综合 | 温和 | 寒冷 |
|---|---|---|---|---|---|
| 屋顶（24 小时使用） | 0.33 | 0.33 | 0.33 | 0.33 | 0.33 |
| 外墙（24 小时使用） | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 |
| 外墙（日间使用） | 0.85 | 0.85 | 0.85 | 0.85 | 0.55 |
| 玻璃 U 因子（最大） | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 |
| 玻璃 SHGC（最大，WWR <= 40%） | 0.27 | 0.27 | 0.27 | 0.27 | 0.62（采暖） |

（ECBC+ 和 SuperECBC 会进一步收紧这些指标。寒冷区为利用太阳能采暖允许更高 SHGC。）

### 4.2 ECBC-R 2018 / Eco-Niwas Samhita

适用于**住宅**建筑，分为两部分：
- **Part 1 (ENS 2018)：**建筑围护结构——按气候区定义 RETV（住宅围护结构传热值）目标
- **Part 2 (ENS 2021)：**机电系统

**RETV 目标：**

| 气候区 | RETV 限值（W/m²） |
|---|---|
| Composite | 15 |
| Hot-Dry | 15 |
| Warm-Humid | 15 |
| Temperate | 15 |
| Cold | -- (U-thermal transmittance limit instead: Uroof <= 1.2, Uwall <= 1.8) |

### 4.3 绿色建筑评级

| 体系 | 运营机构 | 建筑类型 | 等级 |
|---|---|---|---|
| **GRIHA**（Green Rating for Integrated Habitat Assessment） | TERI + MNRE | 新建、大型建筑 | 1–5 星 |
| **GRIHA SVA Griha** | 同上 | 小型住宅（<= 2,500 m²） | -- |
| **GRIHA EB** | 同上 | 既有建筑 | -- |
| **IGBC LEED India** | CII Indian Green Building Council | 所有类型 | Certified / Silver / Gold / Platinum |
| **IGBC Green New Buildings** | 同上 | 印度专项体系 | 同上 |
| **EDGE** | IFC（世界银行） | 保障性住房/中小企业 | Certified / Advanced / Zero Carbon |
| **LEED v4.1** | USGBC（国际） | 所有类型 | Certified / Silver / Gold / Platinum |

自 2014 年起，GRIHA 对**所有 CPWD（中央公共工程部）项目**强制执行，许多州 PWD 也予以采用。

---

## 5. 无障碍

### 5.1 法定框架

- **Rights of Persons with Disabilities Act 2016**（RPwD Act）——取代 1995 年 PwD Act。附表定义 21 类残障，第 44–46 条强制要求建筑环境无障碍。
- **Accessibility Code of India**——并非单一文件，而是由 RPwD Act、Harmonised Guidelines 和 NBC 2016 Part 3 (3.10) 共同构成。
- **Harmonised Guidelines and Space Standards for Universal Accessibility 2021**（MoHUA，取代 2016 版 Harmonised Guidelines）——提供详细尺寸标准，应作为主要技术依据。
- **CPWD Manual for Barrier-Free Built Environment 2014**（更新版）——适用于中央政府建筑。

### 5.2 关键尺寸要求（Harmonised Guidelines 2021）

| 要素 | 要求尺寸 |
|---|---|
| 无障碍路线宽度 | 净宽 1.2 m（优选 1.5 m）；每 60 m 设置会车空间 |
| 门净宽 | 入口最小 900 mm；内部 850 mm |
| 坡道坡度 | 高差 760 mm 时最大 1:12；优选 1:15；需要触觉对比时采用 1:20 |
| 坡道平台 | 顶部/底部 1.5 × 1.5 m；水平每 9.0 m 设置中间平台 |
| 电梯轿厢 | 最小宽 1100 mm × 深 1300 mm（轮椅 + 陪同者）；医院 1100 × 2100 mm（担架通行） |
| 电梯门 | 净宽 900 mm |
| 无障碍卫生间 | 最小 1.5 m × 2.2 m；1.5 m 回转圆；850 mm AFL 设置扶手 |
| 无障碍停车位 | 3.6 m × 4.8 m + 1.2 m 通道 |
| 标识 | 触觉 + 盲文；高对比度（LRV 差值 >= 70%）；阅读高度 1.2–1.6 m |
| 触觉地面 | 所有高差、门口、坡道、楼梯边缘、电梯入口处 |
| 柜台高度 | 无障碍服务柜台最大 800 mm |

### 5.3 配置数量（RPwD + Harmonised Guidelines）

- **电梯：**面向公众的 G+1 及以上建筑必须无障碍；住宅为 G+2 及以上；单层集会建筑为 G+0。（RPwD 的解释正在趋严。）
- **无障碍卫生间：**每层至少1间；公共建筑每组公共卫生间每种性别至少1间，另设1间通用卫生间
- **无障碍停车位：**总数的2%或至少2个，取较大值
- **集会无障碍座席：**2%，配陪同座席并分散布置（不得集中）。

---

## 6. 结构设计（IS 规范）

### 6.1 荷载

| 类型 | 参考标准 |
|---|---|
| 恒载 | IS 875 (Part 1):1987 |
| 施加荷载 | IS 875 (Part 2):1987 |
| 风荷载 | IS 875 (Part 3):2015——6 个风区（基本风速 33–55 m/s） |
| 雪荷载 | IS 875 (Part 4):1987——适用范围有限 |
| 特殊荷载（冲击、振动等） | IS 875 (Part 5):1987 |
| 地震 | IS 1893 (Part 1):2016 |
| 荷载组合 | IS 875 Pt 5 + IS 1893；按极限状态设计 |

### 6.2 抗震分区（IS 1893:2016）

| 区域 | 区域系数 Z | 烈度（MMVI/MSK） | 城市 |
|---|---|---|---|
| **II** | 0.10 | VI | Bangalore, Hyderabad, Chennai (margin), Pune, Mumbai, Trivandrum |
| **III** | 0.16 | VII | Mumbai (Greater), Kolkata, Lucknow, Bhubaneswar, Ahmedabad, Surat, Jaipur |
| **IV** | 0.24 | VIII | Delhi, Jammu, Patna, Dehradun, Faridabad, Chandigarh |
| **V** | 0.36 | IX or more | Srinagar, Guwahati, Shillong, Aizawl, Imphal, Port Blair, Kutch (Bhuj), Sikkim |

**Ductile detailing** (IS 13920:2016) mandatory for all buildings in Zone III, IV, V and important structures in II.

### 6.3 风区（IS 875 第 3 部分：2015）

| 风区 | 基本风速 Vb（m/s，50 年重现期） | 城市 |
|---|---|---|
| Zone 1 | 33 | Trivandrum, Bangalore, Hyderabad |
| Zone 2 | 39 | Pune, Mumbai (inland), Chennai (margin) |
| Zone 3 | 44 | Mumbai (coastal), Kolkata, Delhi (margin) |
| Zone 4 | 47 | Bhubaneswar, Visakhapatnam |
| Zone 5 | 50 | Most coastal Tamil Nadu, Andhra coast |
| Zone 6 | 55 | Cyclone-prone Odisha, AP coast, Bay of Bengal islands |

### 6.4 材料规范

| 材料 | 规范 |
|---|---|
| 素混凝土与钢筋混凝土 | **IS 456:2000**（修订中；IS 456:2024 草案） |
| 工作应力混凝土（适用时） | IS 456 附录 N |
| 高性能混凝土 | IS 456 + IS 1199 + 专项条款 |
| 预应力混凝土 | IS 1343:2012 |
| 一般钢结构 | **IS 800:2007**（极限状态） |
| 冷弯薄壁钢 | IS 801:1975 + IS 811:1987 |
| 组合结构 | IS 11384:1985 |
| 木结构 | IS 883:2016 + IS 4983 |
| 砌体 | IS 1905:1987 |
| 基础 | IS 1904:1986（一般），IS 6403（容许承载力），IS 2950（筏基），IS 2911（桩基，4 部分） |
| 铝 | IS 8147 |
| 玻璃 | IS 16231（4 部分） |
| 幕墙 | IS 17277:2019 |

---

## 7. 规划、分区与城市设计层级

### 7.1 RERA（房地产监管机构）

- **RERA Act 2016**——地块面积 > 500 m² 或住宅单元 > 8 套的任何住宅/商业项目均须强制注册
- State RERA authorities (e.g., MahaRERA Maharashtra, KRERA Karnataka, TNRERA Tamil Nadu) enforce
- Carpet Area definition standardized: **enclosed walkable area within apartment + internal partition walls, excluding balcony, terrace, utility area, external walls** (RERA Sec. 2(k))
- Promoter cannot use undefined area terms ("super built-up", "saleable area") in marketing without disclosure
- 买方付款的70%在完工前存入监管账户

### 7.2 海岸管制区（CRZ 2019）

适用于距高潮线 500 m 以内的项目：
- **CRZ-I**（生态敏感区）——禁止建设
- **CRZ-II**（已开发城市区）——按既有开发控制，FSI受限
- **CRZ-III**（农村区）——建设受限；200 m禁建带
- **CRZ-IV**（水体）——活动受限

### 7.3 环境许可（EIA 2006 + 修正案）

| 阈值 | 类别 | 主管机构 |
|---|---|---|
| Built-up >= 20,000 sqm AND <1,50,000 sqm | B2 | State EIA Authority (SEIAA) |
| Built-up >= 1,50,000 sqm | A | MoEFCC (Central) via EAC |
| Township projects >= 50 hectare OR >= 1,50,000 sqm built-up | A | MoEFCC |

所需材料：Form 1、Form 1A、概念规划、基线研究、EIA 报告（仅 A 类需公众听证）、EMP；EC 有效期 7 年。

### 7.4 航空 NOC（DGCA NOCAS 2.0）

在线门户为 nocas2.aai.aero。若建筑超过按其与最近机场距离计算的高度限制，则必须办理：
- Type 1 airport (international, >2,500 m runway): NOC required within 20 km
- Type 2 airport (domestic): within 8.5 km
- Helipad: within 4 km

高度限制采用圆锥面控制（坡度因机场而异）。

---

## 8. 快速数值参考

| 参数 | 数值 | 来源 |
|---|---|---|
| 住宅层高（标准） | 3.0 m | NBC Part 4 4.7.3.1（净高最小 2.75 m） |
| 办公层高 | 3.6 m | ECBC + NBC；净高最小 2.75 m |
| 最小房间面积（住宅可居住空间） | 9.5 m²（单人居住）；13.93 m²（家庭房） | NBC Part 3 4.2 |
| 最小厨房面积 | 5.5 m² | NBC Part 3 4.2.5 |
| 最小卫生间面积 | 1.8 m²，最小尺寸1.2 m | NBC Part 3 4.2.5 |
| 最小阳台进深 | 0.9 m（因州级DCR而异） | 当地DCR |
| 住宅走廊宽度 | 1.0 m（高层1.2 m） | NBC Part 4 4.4.3 |
| 医院走廊宽度 | 2.4 m | NBC Part 4 + FGI推导 |
| 办公走廊宽度 | 1.5 m | NBC Part 4 |
| 高层住宅楼梯宽度 | 1.5 m | NBC Part 4 4.4.3 + 4.5 |
| 医院楼梯宽度 | 2.0 m | NBC Part 4 |
| 踏步/踢面舒适值 | 踏步250 mm；住宅踢面175 mm；机构建筑300/150 | NBC Part 4 4.4.3 |
| 电梯容量（基本住宅） | 6人（408 kg） | NBC Part 8 Sec 6 |
| 电梯容量（高层住宅） | 13人（884 kg）+消防电梯545 kg | 同上 |
| 停车ECS（等效车位） | 25 m²（含车道的有盖车位）；23 m²无盖车位+5 m²交通面积 | 州级DCR（因地而异） |
| 两轮车停车 | 每辆1.5 m² | NBC + 当地DCR |
| 自行车停车（TOD） | 按当地DCR；孟买DCPR要求每100 m² GFA设置1个 |

---

## 9. 应用流程

针对印度项目提供建议时：

1. **确定州、城市及 Municipal Corporation/Development Authority**。
2. **核查现行 Building Bye-Laws 版本**。印度 DCR 经常更新（例如 Mumbai DCPR 2034 取代 DCPR 1991；UDCPR 2020 统一马哈拉施特拉邦；Kerala KMBR 2019 取代 1999 等）。
3. **核查州级 ECBC 采纳状态**及项目适用阈值。
4. **确认 RERA 注册要求**（第 3 节阈值）。
5. 根据建筑面积确认 **EIA 类别**（见上文第 7.3 节）。
6. **确认 Fire NOC 要求**并在设计前取得临时 NOC。
7. 如适用，**确认航空 NOC**（DGCA NOCAS 2.0）。
8. 如为沿海场地，**确认 CRZ 类别**。
9. 生命安全采用 **NBC 2016**，随后按 DCR 确定 FAR/退界/停车，能源部分采用 ECBC。
10. **引用具体条款**：例如 “NBC 2016 Part 4 Clause 4.4.3”、“ECBC 2017 Section 4.3.1.1”、“IS 1893:2016 Clause 6.4.2”、“Mumbai DCPR 2034 Regulation 33(10)”、“MoHUA Harmonised Guidelines 2021 Section 2.5”。

---

## 10. 各州关键注意事项

### Maharashtra / Mumbai (MCGM DCPR 2034)
- **高级FSI**可购买；**TDR**（开发权转让）可交易
- 第33(10)条贫民窟改造、第33(7)条征收建筑、第33(9)条集群改造、第33(11)条村落区
- 沿海项目受 **MCZMA** 和CRZ管制
- 高层建筑（>=70 m）在取得MCGM许可前需经 **高层建筑委员会**审批
- 分阶段审批：IOD（不批准通知——名称虽如此，实际为前置条件）-> CC（开工证）-> OC（使用证）

### Delhi NCR
- **Unified Building Bye-Laws 2016**（UBBL）适用于多数机构（MCD、NDMC、DDA）
- **MPD 2041** 管制土地用途和开发密度
- **HCBE（Heritage Conservation Committee）** + **DUAC（Delhi Urban Arts Commission）**审查遗产区域和 Lutyens' Bungalow Zone
- Gurugram 有自己的 **Haryana Building Code 2017** + GMDA
- NOIDA / Greater NOIDA each have separate authority + bye-laws

### Karnataka / Bangalore
- **BBMP Bye-Laws 2003** 和 **BDA Master Plan RMP 2031** 管制班加罗尔
- **二线城市规范**（Mysuru、Mangaluru）遵循带地方修订的 KMBBL
- 面积 > 1500 m² 的任何项目均需取得 KSPCB Consent

### Tamil Nadu / Chennai
- **TNCDBR 2019**（Tamil Nadu Combined Development and Building Rules 2019）更新并取代2008和2010版本
- 多层建筑：超过4层或高度超过15 m
- **CMDA** 负责金奈都市区；州内其他地区由 **DTCP** 负责

### Karnataka / Bangalore vs Telangana / Hyderabad
- 海得拉巴许多区域实际上 **FAR不设上限**，但受退界和保险附加费限制（GO 168及修订）
- **TS-bPASS**——Telangana 的在线单一窗口规划审批（小地块即时审批，大地块 21 天）

---

## 11. 权威来源

- **Bureau of Indian Standards (BIS)** -- bis.gov.in -- NBC 2016 (SP 7), IS codes
- **Bureau of Energy Efficiency (BEE)** -- beeindia.gov.in -- ECBC 2017, ECBC-R 2018 (Eco-Niwas Samhita)
- **Ministry of Housing and Urban Affairs (MoHUA)** -- mohua.gov.in -- Harmonised Guidelines 2021
- **MoEFCC** -- moef.gov.in -- EIA Notifications, CRZ Notifications
- **State Town Planning Departments** -- portal varies by state
- **State Municipal Corporations** -- e.g., portal.mcgm.gov.in (Mumbai), mcdonline.nic.in (Delhi), bbmpgov.in (Bangalore), tnchennai.gov.in (Chennai), ghmc.gov.in (Hyderabad)
- **State Development Authorities** -- mmrda.maharashtra.gov.in (MMRDA), dda.gov.in (DDA), bda.karnataka.gov.in (BDA)
- **RERA portals** -- maharera.maharashtra.gov.in, rera.karnataka.gov.in, tnrera.in
- **GRIHA Council** -- grihaindia.org
- **IGBC (CII)** -- igbc.in

---

*本插件内交叉引用：加载 `building-codes` 进行 IBC 比较；加载 `fire-life-safety` 了解一般疏散原则；加载 `building-sustainability` 比较 LEED/Passive House；加载 `structural-systems` 在 IS 框架内选择材料体系；加载 `building-envelope` 处理印度气候区围护结构节点。*
#

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab AI建筑与室内设计总设计师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
