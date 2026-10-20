---
name: country-australia
description: >
  澳大利亚建筑规范与法规参考。涵盖由 Australian Building Codes Board（ABCB）发布的《国家建筑规范》
  2022（NCC 2022）——第一卷（第 2–9 类《澳大利亚建筑规范》）、第二卷（第 1 + 10 类——住宅规定）、第三卷
  （《澳大利亚管道规范》）；澳大利亚标准包括 AS/NZS 1170.0-2002 + 1170.1-2002
  + 1170.2-2021 wind + 1170.3-2003 snow + 1170.4-2007 seismic, AS 3600-2018 concrete, AS
  4100-2020 steel, AS 1684-2010 residential timber, AS 1170.4 seismic, AS 1530.1/.2/.3/.4/.8
  fire test methods, AS 4072 service penetration sealing, AS 1428.1-2021 accessibility, AS
  1428.4 tactile, AS/NZS 4586 slip resistance, AS 1668 ventilation, AS 1680 lighting; the
  Disability (Access to Premises -- Buildings) Standards 2010 + Disability Discrimination
  Act 1992; the 7-star NatHERS (Nationwide House Energy Rating Scheme) mandatory for new
  Class 1 housing from 2022; state-specific overlays (NSW Planning + Environmental Planning
  Instruments, Victoria Plumbing Regulations, Queensland Sustainable Building Code, WA Building
  Code, SA Planning + Building Code, ACT + NT); BCA performance + DTS pathways; the BASIX
  (NSW) sustainability assessment; Green Building Council of Australia Green Star ratings;
  and the Australian climate zones (8 zones) with cyclonic wind regions (A0, A1-5, B, C, D).
version: 1.1.0
license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
author: OmniAiLab
developer: Mochiball
agent_created: true
开源仓库: https://github.com/tomatoparkdao/registered-architect
---

# 国家：澳大利亚

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。

适用于澳大利亚任何州或领地项目的建筑规范与法规参考。当提及澳大利亚城市/州（悉尼、墨尔本、布里斯班、珀斯、阿德莱德、堪培拉、霍巴特、达尔文）、AUD 货币、“NCC”/“BCA”/“AS”/“AS/NZS”/“NatHERS”/“BASIX”/“Premises Standards”、Green Star 或州缩写（NSW、VIC、QLD、WA、SA、TAS、ACT、NT）时启用本技能。

---

## 1. 法规层级

澳大利亚采用具有 **Archetype B（国家示范+州采纳）** 特征并兼具 **Archetype E（基于性能）** 特征的体系。NCC 是统一的性能型规范，由各州《建筑法》采纳，并在 A1–A8 附录中发布州级差异。

### 1.1 主管机构层级

```
第 1 级——国家层面
  澳大利亚建筑规范委员会（ABCB）——发布 NCC；联邦与州联合机构
  Standards Australia——发布 AS / AS/NZS 标准
  联邦政府：
    - 《1992 年残障歧视法》（DDA）——由澳大利亚人权委员会执行
    - 《2010 年残障（场所通行——建筑）标准》——与 NCC 对应
    - 国家建筑规范战略
  澳大利亚统计局 + IBM——气候与地震数据
  澳大利亚地球科学局——地震与洪水
  气象局——气候数据

第 2 级——州/领地
  8 个辖区各自设有：
    建筑法/建筑法规
    建筑主管机构（监管机构）
    建筑测量师注册机构
    规划体系（独立于建筑管控）
  NSW: Department of Customer Service (Building Commissioner); Department of Planning
  VIC: Victorian Building Authority (VBA); Department of Transport and Planning
  QLD: Queensland Building and Construction Commission (QBCC); Department of Energy + Public Works
  WA: Building Commissioner (Department of Mines + Industry Regulation + Safety -- DMIRS); Department of Planning, Lands + Heritage
  SA: Office of the Building Authority (now Construction Industry Training Board oversight); Plan SA
  TAS: Department of Justice -- Consumer, Building + Occupational Services
  ACT: Access Canberra (Environment, Planning + Sustainable Development)
  NT: Department of Infrastructure, Planning + Logistics

第 3 级——地方层面
  地方议会（Council、Shire、Borough）——通常为规划主管部门
    + 建筑测量师（私人竞争执业）
    + 议会规划官员
  消防与救援（州级机构）——性能化方案咨询
  州环境保护主管部门——污染控制

第 4 级——项目层面
  注册建筑测量师——评估 NCC 合规性并签发建筑许可
  注册建筑从业人员——建筑师（《建筑师法》+ 各州建筑师委员会）、工程师（通常通过 Engineers Australia 特许资格）
  消防工程师（FPA Australia 认证）——性能化方案
  无障碍顾问（AAAA 认证）——无障碍建议
  NatHERS 认证评估员——住宅能源评级
  Section J / Part J6 评估员——商业建筑能源评估
```

### 1.2 各州采纳情况

NCC 2022 由各州通过《建筑法》采纳：
- **NSW**: Environmental Planning + Assessment Act 1979 + Environmental Planning + Assessment Regulation 2021
- **VIC**: Building Act 1993 + Building Regulations 2018
- **QLD**: Building Act 1975 + Building Regulation 2021
- **WA**: Building Act 2011 + Building Regulations 2012
- **SA**: Planning, Development + Infrastructure Act 2016 + Planning, Development + Infrastructure (General) Regulations 2017
- **TAS**: Building Act 2016 + Building Regulations 2016
- **ACT**: Building Act 2004 + Building (General) Regulation 2008
- **NT**: Building Act 1993 + Building Regulations 1993

各州将 **州级差异**作为 NCC 的组成部分发布（列入相关卷册附录）。例如，NSW 有丛林火灾和洪水叠加规定；QLD 有气旋和白蚁规定；WA 北部有气旋规定；NT 有热带气旋规定。

---

## 2. NCC 2022 结构

**2022 年《国家建筑规范》**（本文撰写时现行，定期更新）由三卷组成：

| 卷册 | 范围 | 建筑类别 |
|---|---|---|
| **第一卷——澳大利亚建筑规范（BCA）** | 商业、公共、多住宅建筑 | 第 2 类（公寓）、第 3 类（酒店／宿舍）、第 4 类（第 5–9 类中的住宅）、第 5 类（办公）、第 6 类（商店）、第 7 类（储藏）、第 8 类（工厂）、第 9a 类（医院）、9b 类（集会）、9c 类（养老照护） |
| **第二卷——住宅规定** | 单户／双户住宅及附属建筑 | 第 1a、1b、10a 类（车库／棚屋）、10b 类（围栏／墙）、10c 类（私人丛林火灾避难所） |
| **第三卷——澳大利亚管道规范（PCA）** | 给排水 | 所有类别 |

### 2.1 建筑分类（NCC 第一卷 A6 部分）

| 类别 | 描述 |
|---|---|
| **1a** | 单户住宅：独立屋或联排住宅中的一户 |
| **1b** | 寄宿屋、客房、旅舍（低层且不超过规定规模） |
| **2** | 多户住宅：公寓 |
| **3** | 酒店、大型寄宿屋、背包客旅舍、宿舍 |
| **4** | 第 5–9 类内的独立使用住宅单元（看护人公寓） |
| **5** | 办公建筑 |
| **6** | 商店和餐厅——商业集会与零售 |
| **7a** | 停车场 |
| **7b** | 储藏建筑 |
| **8** | 实验室、工厂、车间 |
| **9a** | 医院、医疗保健 |
| **9b** | 集会（剧院、学校、宗教场所） |
| **9c** | 老年照护和住宅照护 |
| **10a** | 车库、棚屋（非居住） |
| **10b** | 围栏、挡土墙、游泳池 |
| **10c** | 私人丛林火灾避难所 |

### 2.2 性能路径与 DTS

NCC 2022 **基于性能**。每项性能要求（PR）可通过以下任一路径满足：
- **视为满足（DTS）方案**——遵循规范中的规定性做法。
- **性能方案**——通过工程化替代方案证明符合 PR。

性能方案常用于消防工程（由 FPA Australia 认可）、结构工程、无障碍（替代路径）和能源设计。

### 2.3 气候区（NCC 2022 附表 1）

澳大利亚按能源设计划分为 **8 个气候区**：

| 区域 | 描述 | 城市 |
|---|---|---|
| **1** | 夏季炎热湿润／冬季温暖 | 达尔文、凯恩斯、汤斯维尔 |
| **2** | 夏季温暖湿润／冬季温和 | 布里斯班、黄金海岸、洛坎普顿 |
| **3** | 夏季炎热干燥／冬季温暖 | 艾丽斯泉、查理维尔、坦南特克里克 |
| **4** | 夏季炎热干燥／冬季凉爽 | 米尔迪拉、布罗肯希尔 |
| **5** | 夏季温暖／冬季凉爽 | 悉尼、珀斯、阿德莱德 |
| **6** | 夏季温和温暖／冬季寒冷 | 墨尔本、堪培拉（边缘）、霍巴特（边缘） |
| **7** | 凉爽温带 | 堪培拉、霍巴特、芒特甘比尔 |
| **8** | 高山 | 霍瑟姆山、布勒山、特雷德博、摇篮山 |

---

## 3. 防火安全（NCC 第一卷 C、D、E 节）

### 3.1 节与部分

| 部分 | 主题 |
|---|---|
| **C 节——耐火** | C1 耐火、消防分区和开口保护 |
| **D 节——通行与疏散** | D1 逃生规定、D2 出口构造、D3 残障人士通行 |
| **E 节——系统与设备** | E1 消防、E2 烟气危害管理、E3 电梯安装、E4 应急照明和出口标志 |

### 3.2 耐火性能与建造类型（C 节）

| 类型 | 描述 | 要求条件 |
|---|---|---|
| **A 型——最高** | 最高耐火等级，适用于最大、最高的建筑 | 4 层以上；大面积楼层 |
| **B 型——中等** | 中等耐火等级，适用于中层建筑 | 2–3 层且规模中等 |
| **C 型——最低** | 所需最低等级，适用于小型低层建筑 | 1 层或小面积楼层 |

每种类型均为结构构件、墙体、楼板等规定耐火等级（FRL），按 AS 1530.4 + EN 13501-2 以 REI（结构承载／隔热／完整性）分钟表示。

### 3.3 Travel Distances (NCC Vol 1 Part D1)

| 建筑类别 | 设置喷淋（m） | 未设置喷淋（m） |
|---|---|---|
| 2（公寓） | 至替代出口通道 6m；总计 20–40m（按布局） | 按第 2 类具体要求 |
| 3（酒店） | 至替代通道 6m；总计 20–40m | 按第 3 类 |
| 5（办公） | 至替代出口 20m；总计 40–60m | 30 + 60m |
| 6（商店） | 20m + 40m | 30 + 60m |
| 9a（医院） | 替代出口 6m + 20–30m | 更严格 |
| 9b（集会） | 20 + 40m | 30 + 60m |

### 3.4 Stair Width (NCC Vol 1 Part D2)

- 第 2 类：最小 1.0m
- 第 3 类：1.0m
- 第 5／6／7／8／9 类：最小 1.0m，按容量确定；设计上可自愿采用 1.2m
- 第 9a／9c 类：1.2m

### 3.5 外墙与可燃覆层（NCC 第一卷 C1.9 + C1.10 部分）

在 Lacrosse（墨尔本，2014）事件和 Grenfell 事件后：
- A 型和 B 型建筑的外墙必须为不燃材料，或通过 AS 5113 验证试验
- AS 5113-2016《基于燃烧反应性能的建筑外墙分类》——澳大利亚对应 NFPA 285／BS 8414 系列的标准
- 2018 年及以后修订：3 层以上第 2／3／5／6／9 类建筑实际上禁止使用可燃 ACP 覆层

VIC、NSW、QLD 等州另有州级禁令（覆层整改计划）。

### 3.6 自动喷水灭火系统（NCC 第一卷 E1.5 部分 + AS 2118）

- 第 2／3 类 ≥4 层——设置喷淋
- 第 5 类 ≥25m——设置喷淋
- 第 6／9b 类——按使用规模确定
- 第 9a 类（医院）——通常设置喷淋
- 设计采用 AS 2118 系列

---

## 4. 能源规范（NCC J 节 + NatHERS）

### 4.1 NCC J 节——能源效率（第一卷）

适用于第 2–9 类建筑。采用性能路径并配合 DTS 规定：
- **J1 建筑围护结构**——按气候区确定 U 值和 SHGC
- **J2 外部玻璃**——面积限制和 SHGC
- **J3 建筑密封**——气密性
- **J5 空调与通风**——效率和分区
- **J6 照明与电力**——LPD 和控制
- **J7 加热供水与游泳池**
- **J8 能源监测设施**

### 4.2 NCC 2022 J 节重大更新

NCC 2022 对第一卷 J 节进行了**重大收紧**，包括：
- 按气候区设定新的热工性能目标（相较 NCC 2019 约提高 30%）
- 新的整栋建筑性能验证（J1V3、J1V4）
- 气密性限值
- 降低照明功率密度（LPD）

### 4.3 NatHERS（第二卷住宅）

**全国住宅能源评级计划：**
- 自 2023 年起（NCC 2022），所有新建第 1／第 2 类住宅强制最低 **7 星（满分 10 星）**
- 2010 年起此前为 6 星
- 软件工具：AccuRate、FirstRate5、BERS Pro
- 经认证的 NatHERS 评估师

### 4.4 BASIX（新南威尔士州）

NSW 特有、早于 NatHERS 并与其并行的评估：
- **建筑可持续性指数**——NSW 政府网络工具
- 自 2004 年起，NSW 所有新建及重大翻新住宅必须采用
- 衡量水、能源和热舒适
- 目标随场地和住宅类型变化

### 4.5 Green Star（澳大利亚绿色建筑委员会）

澳大利亚自愿性绿色建筑评级：
- **Green Star 设计与竣工**（原“新建”）
- **Green Star 室内**
- **Green Star 运行性能**
- **Green Star 社区**

评级为 4–6 星（6 星代表世界领先）。

### 4.6 隐含碳

GBCA、IES 和州级机构日益要求进行隐含碳评估：
- **NABERS** -- National Australian Built Environment Rating System -- operational ratings (4 to 6 stars)
- **NABERS Embodied** -- new module
- **TM65 Embodied Carbon Calculator** (CIBSE Australian adaptation)

---

## 5. 无障碍（NCC D3 部分 + AS 1428.1-2021 + Premises Standards 2010）

### 5.1 法定框架

- **Disability Discrimination Act 1992** -- federal anti-discrimination legislation
- **Disability (Access to Premises -- Buildings) Standards 2010** -- the "Premises Standards" -- federal regulation mirroring NCC accessibility requirements
- **NCC Part D3 (Volume 1) + Part 12.7 (Volume 2)** -- mandatory accessibility provisions
- **AS 1428.1-2021** -- General Requirements for Access -- the detailed dimensional reference
- **AS 1428.4-2009** -- Tactile Indicators (TGSIs)
- **AS 1735-2019** -- Lift requirements for accessibility
- **AS 2890.6-2009** -- Off-street parking for people with disabilities
- **AS/NZS 4586** -- Slip resistance of pedestrian surfaces

### 5.2 关键尺寸（AS 1428.1-2021）

| 要素 | 尺寸 |
|---|---|
| 无障碍通行路径 | 净宽 1500 mm（受限情况下绝对最小 1000 mm） |
| 门净宽 | 850 mm（D1.7）；主入口优选 950 mm |
| 坡道坡度 | 最大 1:14（比 ADA／英国的 1:12 更严格）；每 9m 设置平台 |
| 横坡 | ≤ 1:40 |
| 电梯轿厢 | 1400 × 1600 mm（A 型）；1100 × 1400 mm（改造建筑 B 型） |
| 无障碍卫生间（步行障碍 + 轮椅） | 优选 1900 × 2300 mm；转移净距 1740 mm |
| 无障碍停车位 | 2.4m + 2.4m 共享区 |
| TGSI（警示／导向） | 按 AS 1428.4 设置于高差、电梯入口、楼梯顶部和底部 |
| 门五金 | 杠杆／D 形把手；作用力 ≤20 N |

### 5.3 配置数量

- **Accessible parking**: per Class + size (Vol 1 Part D3 Table D3.5): generally 1 per 50 stalls for Class 5/6; 1 per 20 for Class 9
- **Accessible WC**: per gender per public WC bank (Vol 1 F2.1); unisex options
- **Accessible apartments**: 1% Type A + Type B per multi-residential (Vol 1 D3 + Premises Standards) -- voluntary higher in many states
- **Hotel accessible rooms**: per Class 3 + capacity
- **Assembly seating**: per AS 1428.1; distributed
- **Hearing augmentation**: per assembly > 100 occupants (Part D3.7 + AS 1428.5-2010 hearing augmentation)

### 5.4 无障碍性能方案

Increasingly common in heritage buildings where DTS impossible; AAAA accredited Access Consultants design + document Performance Solutions.

---

## 6. 结构与荷载（AS / AS/NZS 标准）

### 6.1 荷载标准系列

| 标准 | 主题 | 版本 |
|---|---|---|
| **AS/NZS 1170.0** | 结构设计作用——总则 | 2002 (R2019) |
| **AS/NZS 1170.1** | 永久作用、可变作用及其他作用 | 2002 (R2019) |
| **AS/NZS 1170.2** | 风作用 | 2021（现行） |
| **AS/NZS 1170.3** | 雪和冰作用 | 2003 (R2019) |
| **AS 1170.4** | 地震作用 | 2007 (R2018) |
| **AS/NZS 1170.5** | 新西兰地震作用（联合标准） | -- |

### 6.2 风区（AS/NZS 1170.2-2021）

澳大利亚采用**风区地图** + **地形类别**：

| 区域 | 描述 | 典型地区 | R = 500 年的 V_R（m/s） |
|---|---|---|---|
| **A1-A5** | 非气旋区 | 悉尼、墨尔本、阿德莱德、珀斯都会区、堪培拉、霍巴特、内陆 | 41-50 |
| **A0** | 非气旋、低风速 | 北领地内陆部分地区 | < 41 |
| **B** | 热带（低气旋） | 昆士兰东南海岸、新南威尔士北海岸 | 50-60 |
| **C** | 气旋区 | 北领地海岸、昆士兰远北、西澳西北部 | 70-83 |
| **D** | 强气旋区 | 离岸地区、西北角 | 83-100+ |

区域 C + D 要求**抗气旋构造**——采用冲击测试玻璃、锚固屋面和可靠连接；第 1 类住宅按 AS 4055（住宅风荷载）执行。

### 6.3 抗震（AS 1170.4-2007）

澳大利亚位于**板块内部**，地震活动中等：
- 多数城市：**危险系数 Z = 0.06–0.10**（悉尼 0.08；墨尔本 0.08；珀斯 0.09；阿德莱德 0.10；布里斯班 0.06）
- 坦南特克里克、纽卡斯尔（NSW）和梅克林（WA）曾发生显著历史地震
- 地震设计类别 EDC I–V；大多数项目为 EDC II

### 6.4 材料

| 材料 | 规范 |
|---|---|
| 混凝土 | AS 3600-2018 |
| 钢材 | AS 4100-2020 |
| 组合结构 | AS/NZS 2327 |
| 木材（通用） | AS 1720.1-2010；AS 1720.2-2006 |
| 住宅木框架 | AS 1684（多卷——木框架住宅结构设计） |
| 砌体 | AS 3700-2018 |
| 冷弯型钢 | AS/NZS 4600-2018 |
| 基础 | AS 2870-2011（住宅楼板与基础）；AS 3798-2007（压实填土）；AS 2159-2009（桩） |
| 住宅风荷载 | AS 4055-2021 |
| 气旋荷载 | AS/NZS 1170.2 区域 C + D |

### 6.5 基础设计注意事项——膨胀性土

澳大利亚许多地区存在**反应性（膨胀性）土壤**——黏土会膨胀和收缩。AS 2870 将场地分为 A 类（稳定）至 P 类（问题场地）。常见的 M 类（中等）要求基础设计考虑土体变形。

---

## 7. 州级实践

### 7.1 新南威尔士州（NSW）

- **《环境规划与评估法》1979 + 2021 年法规**
- **地方环境规划（LEP）** + 各地方政府的**开发控制规划（DCP）**
- **州环境规划政策（SEPP）**——某些情况下优先于 LEP
- **《公寓设计指南》（SEPP 65）**——住宅设计质量要求（阳光、隐私、布局、公共开放空间）
- 住宅强制采用 **BASIX**
- **丛林火灾（《2019 丛林火灾规划保护》）**及 AS 3959 丛林火灾攻击等级（BAL）评估
- 沿海场地适用 **《2016 沿海管理法》**
- **NSW 建筑专员**——Opal Tower（2018）和 Mascot Towers（2019）事件后的改革制度

### 7.2 VIC

- **2018 年建筑法规**
- 按《1987 规划与环境法》制定的**规划方案**
- **更佳公寓设计标准**——VIC 对应 NSW SEPP 65
- **6 星**能源 + 水 + 土地协同标准（2010 年起，与 NatHERS 一致）
- **Cladding Safety Victoria**——Lacrosse 事件后的计划
- **Latrobe Valley 危险场地**——历史遗留问题

### 7.3 QLD

- **1975 年建筑法 + 2021 年法规**
- 北部采用**热带气旋设计**（区域 C + D）
- 首府适用 **《2014 布里斯班城市规划》**
- 南回归线以南强制**白蚁防护**——AS 3660 系列
- **昆士兰开发规范（QDC）**——补充条款
- 洪水和侵蚀区的**沿海建筑线**限制

### 7.4 WA

- **2011 年建筑法 + 2012 年建筑法规**
- **住宅设计规范（R-Codes）**——详细住宅规划与设计要求
- 北部（皮尔巴拉、金伯利）采用**气旋设计**（区域 C + D）
- 按 WAPC 州规划政策 3.7 进行**丛林火灾攻击等级（BAL）评估**

### 7.5 SA

- **2016 年规划、开发与基础设施法**
- **规划与设计规范（P&D Code）**——全州统一规划规范（取代 72 份开发规划）
- **阿德莱德遗产** + **建筑规范变更 A2.1**

### 7.6 ACT

- **2004 年建筑法 + 2008 年建筑（通用）法规**
- **可持续发展政策**
- **堪培拉能源与水星级评级计划**（与 NatHERS 并行）

### 7.7 TAS

- **2016 年建筑法 + 2016 年法规**
- **惠灵顿山／霍巴特遗产保护**
- 寒冷气候区 7 设计

### 7.8 NT

- **1993 年建筑法 + 1993 年法规**
- **热带气旋**——以区域 C/D 为主
- **北部顶端与中部**——达尔文为第 1 类气候，艾丽斯泉为第 3 类气候
- **原住民土地**——适用独立的文化与规划制度

---

## 8. Approval Workflow (NSW as Representative)

### 8.1 Standard Workflow

1. **开发申请（DA）**——依据 EP+A 法提交地方政府
2. **DA 前会议**——与地方政府规划师举行
3. **DA 决定**——接受公众展示和地方政府审议，有时由 JRPP（联合区域规划委员会）审查
4. **施工证书（CC）**——由地方政府或私人认证师签发，证明符合 BCA + AS
5. **施工阶段检查**——首席认证机构（PCA）在关键阶段检查：基础、结构、机电、消防系统和竣工
6. **使用证书（OC）**——使用前取得；可为临时 OC 或最终 OC
7. 许多建筑要求提供**建筑手册**和**维护计划**

### 8.2 Approval Pathways

- **地方政府 DA** + **符合性开发证书（CDC）**——依据 SEPP 豁免与符合性开发规定，对简单住宅实行自认证
- **州重大开发项目（SSD）**——由 NSW 规划、工业与环境部门审批重大项目
- **第 1 类土地与环境法院程序**——申诉与评估

### 8.3 建筑测量师

澳大利亚大多数认证由**建筑测量师**（私人竞争机制）负责，而非政府建筑部门。建筑测量师须在州主管机构注册，负责评估 NCC 合规性、签发建筑许可证／施工证书并实施检查。

---

## 9. 气候设计参数

### 9.1 Sydney (Zone 5)

| 参数 | 数值 |
|---|---|
| 冷却设计干球温度（0.4%） | 32–34 °C |
| 冷却设计湿球温度 | 22–23 °C |
| 供暖设计干球温度（99.6%） | 4–6 °C |
| 年冷度日（基准 18°C） | 600–800 |
| 年热度日（基准 18°C） | 1100–1300 |
| 500 年重现期风速 V_R | 45 m/s（A2 区） |
| 丛林火灾 | 邻近植被的郊区需进行 BAL 评估 |

### 9.2 Melbourne (Zone 6)

| 参数 | 数值 |
|---|---|
| 冷却设计干球温度 | 35–37 °C |
| 供暖设计干球温度 | 1–3 °C |
| 年热度日 | 2000+ |
| 风区 | A4 区 |

### 9.3 Darwin (Zone 1)

| 参数 | 数值 |
|---|---|
| 冷却设计干球温度 | 35–37 °C |
| 冷却设计湿球温度 | 27–28 °C |
| 年冷度日 | 4500+ |
| 年热度日 | 约 0 |
| 风区 | C 区（气旋区） |
| 气旋事件 | 每十年 1–2 次大型事件 |

### 9.4 Perth (Zone 5)

| 参数 | 数值 |
|---|---|
| 冷却设计干球温度 | 38–40 °C |
| 供暖设计干球温度 | 4–6 °C |
| 强海风（“Fremantle Doctor”） | |

### 9.5 Hobart (Zone 7)

| 参数 | 数值 |
|---|---|
| 冷却设计干球温度 | 27–29 °C |
| 供暖设计干球温度 | −2 至 0 °C |
| 年热度日 | 2700+ |

---

## 10. 数值速查

| 参数 | 数值 | 来源 |
|---|---|---|
| 住宅层间高度 | 2.7–3.0 m | NCC 第 2 卷；多数房间净高最小 2.4 m |
| 办公层间高度 | 3.6–4.2 m | NCC 第 1 卷 + 行业惯例；净高 2.4 m（D1.6） |
| 酒店净吊顶高度 | 2.4 m | NCC 第 1 卷 D1.6 |
| 楼梯宽度 | 多数用途 1.0 m | NCC 第 1 卷 D1.5 |
| 踢步最大高度 | 190 mm | NCC 第 1 卷 D1.5 |
| 踏步最小深度 | 240 mm | NCC 第 1 卷 D1.5 |
| 疏散距离（设置喷淋） | 双向 40–60 m（按类别变化） | NCC 第 1 卷 D1.4 |
| 饰面（第 2/3/5–9 类且 ≥3 层） | 经 AS 5113 验证或采用不燃材料 | NCC 第 1 卷 C1.9 + C1.10 |
| 墙体 U 值（悉尼第 5 区） | 约 R2.0（W/m²K 约 0.45） | NCC 2022 J1V2 |
| NatHERS 最低星级 | 7 | NCC 2022 + 州规定 |
| 悉尼风速 V_R | 45 m/s | AS/NZS 1170.2 |
| 达尔文风速 V_R（气旋） | 70+ m/s | AS/NZS 1170.2 C 区 |
| 悉尼地震危险性 Z | 0.08 | AS 1170.4 |
| 无障碍停车位（第 5 类） | 每 50 个车位 1 个 | NCC 第 1 卷 D3.5 |

---

## 11. 应用工作流

1. **确定州／领地**。
2. **确定气候区（按 NCC 2022 为 1–8）**。
3. **确定风区（A0、A1–5、B、C、D）及丛林火灾／洪水／沿海灾害**。
4. **确定建筑类别（按 NCC 第一、二、三卷为 1–10）**。
5. **采用 NCC 2022（视情况采用第一卷或第二卷 + 第三卷）**——DTS 或性能路径。
6. **采用 NCC 引用的 AS／AS/NZS 标准**。
7. **第 1 + 第 2 类住宅能源采用 NatHERS**。
8. **第 2–9 类建筑能源采用 J 节／J1V**。
9. **无障碍采用 AS 1428.1-2021 + NCC D3 部分 + Premises Standards**。
10. **采用州级差异规定**（如 NSW SEPP 65、VIC Better Apartments、QLD QDC）。
11. **引用条款**：例如 “NCC 2022 第一卷 C1.9 部分”、“AS 1170.2-2021 第 2.3 节”、“AS 1428.1-2021 第 11.3 节”、“NSW SEPP 65 公寓设计指南目标 4D”、“AS 3959-2018 第 5 节”、“NatHERS 软件协议”。

---

## 12. 权威来源

- **Australian Building Codes Board (ABCB)** -- abcb.gov.au -- NCC + Performance Solutions
- **Standards Australia** -- standards.org.au -- AS / AS/NZS standards (commercial paywall)
- **Property Council of Australia** -- propertycouncil.com.au
- **Green Building Council of Australia (GBCA)** -- gbca.org.au -- Green Star
- **NABERS** -- nabers.gov.au -- operational ratings
- **NSW Department of Customer Service -- Building Commissioner** -- nsw.gov.au/building-commissioner
- **Victorian Building Authority (VBA)** -- vba.vic.gov.au
- **Queensland Building + Construction Commission (QBCC)** -- qbcc.qld.gov.au
- **Department of Mines, Industry Regulation + Safety WA (DMIRS)** -- dmirs.wa.gov.au
- **FPA Australia (Fire Protection Association)** -- fpaa.com.au -- fire engineers
- **AAAA (Association of Consultants in Access Australia)** -- access.asn.au
- **Australian Institute of Architects (AIA)** -- architecture.com.au
- **Geoscience Australia** -- ga.gov.au -- seismic + flood data
- **Bureau of Meteorology** -- bom.gov.au -- climate data

---

*交叉引用：加载 `building-codes` 了解一般规范结构（澳大利亚 NCC 基于性能，与 IBC 不同）；加载 `fire-life-safety` 了解 NCC C/D/E 节叠加的一般原则；加载 `accessibility-design` 了解全球框架及 AS 1428.1；加载 `building-sustainability` 对比 Green Star、NatHERS 和 NABERS；加载 `structural-systems` 了解 AS 结构标准（混凝土、钢、木材、砌体）；加载 `building-envelope` 了解 8 个气候区的围护结构细部及丛林火灾／气旋叠加规定。*
#

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
