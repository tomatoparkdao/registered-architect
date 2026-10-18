---
name: specification-guide
description: 注册建筑师专业参考：specification-guide。
license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---

# 规格编写指南——深度参考

关于建筑规格体系、性能化与规范性方法、报审文件、测试标准、质量保证和常见错误的综合参考。

---

## 1. 规格的目的

规格是施工文件的书面组成部分，用于描述材料、产品、施工工艺标准和质量要求。图纸描述几何形态、位置和数量，规格则通过定义定性要求对其进行补充。

**核心原则：**图纸说明“是什么”和“在哪里”；规格说明“如何做”以及“达到什么标准”。

**合同地位：**规格属于合同文件。规格与图纸之间的歧义或冲突会产生合同风险。多数合同会建立优先级：质量/材料事项以规格优先，尺寸/数量事项以图纸优先。

---

## 2. 规格体系

### 2.1 NBS（国家建筑规格）——英国/国际

这是英国、澳大利亚以及欧洲和亚洲部分地区使用最广泛的规格体系。

**结构：**
- 按与专业工程包对应的工作分部分组。
- 每个分部包含：范围、一般要求、材料、施工工艺和竣工标准。
- 条款采用预先编写的模板，由编制人员定制。

**主要工作分部（NBS 格式）：**
- A — 前期准备/一般条件
- C — 拆除/改造/翻修
- D — 土方工程
- E — 现浇混凝土/大型预制混凝土
- F — 砌体
- G — 结构金属/木材骨架
- H — 饰面/覆盖层
- J — 防水
- K — 内衬/覆板/干式隔墙
- L — 窗/门/楼梯
- M — 表面饰面
- N — 家具/设备
- P — 建筑构造杂项
- Q — 铺装/种植/围栏/场地家具
- R — 排水系统
- S — 管道供给系统
- T — 机械供暖/制冷/制冷设备
- U — 通风/空气调节
- V — 电气供给/电力/照明
- W — 通信/安防/控制
- X — 运输系统（电梯、自动扶梯）
- Y — 机电服务计量
- Z — 建筑构造参考规格

**NBS Chorus / NBS Source：**
基于云的规格平台，与制造商产品数据关联，并与 BIM 集成（嵌入规格数据的 NBS 对象）。是英国实践的行业标准。

### 2.2 CSI MasterFormat——北美

美国和加拿大采用建筑规格协会（CSI）MasterFormat 作为标准规格组织体系。

**分部结构（共 50 个分部，列出主要分部）：**

| 分部 | 标题 | 内容 |
|---|---|---|
| 00 | 采购与合同 | 招标要求、合同、担保 |
| 01 | 一般要求 | 总则、价格与付款、行政管理、质量保证/质量控制、临时设施 |
| 02 | 既有条件 | 测量、拆除、有害物质处理 |
| 03 | 混凝土 | 现浇、预制、钢筋、模板 |
| 04 | 砌体 | 砌块砌体、石材、人造石 |
| 05 | 金属 | 结构钢、杂项金属、楼梯、栏杆 |
| 06 | 木材、塑料及复合材料 | 粗木作、精木作、细木作、FRP |
| 07 | 保温与防潮 | 保温、防水、屋面、饰面、密封胶 |
| 08 | 开口部 | 门、窗、幕墙、玻璃、五金 |
| 09 | 饰面 | 抹灰、石膏板、地面、涂装、墙面覆盖物 |
| 10 | 专项工程 | 标识、储物柜、卫生间配件、消防专项设施 |
| 11 | 设备 | 厨房、洗衣、医疗、实验室 |
| 12 | 家具及陈设 | 家具、窗饰、织物 |
| 13 | 特殊建造 | 游泳池、洁净室、抗震保护 |
| 14 | 垂直运输设备 | 电梯、自动扶梯、传菜梯 |
| 21 | 灭火系统 | 自动喷水灭火系统 |
| 22 | 给排水 | 生活给水、排水、卫生器具 |
| 23 | 暖通空调 | 采暖、制冷、通风、控制 |
| 25 | 综合自动化 | 建筑管理系统 |
| 26 | 电气 | 配电、照明 |
| 27 | 通信 | 数据、语音、音视频、安全 |
| 28 | 电子安全与安防 | 火灾报警、门禁、CCTV |
| 31-35 | 土方工程至水道/海事工程 | 场地与土木 |
| 40-48 | 工艺集成至电气工程 | 工业/工艺 |

**三部分分部格式（CSI）：**
1. **第 1 部分——一般要求：**范围、参考文件、报审文件、质量保证、交付/储存和保修。
2. **第 2 部分——产品：**材料、制造商、加工和饰面。
3. **第 3 部分——执行：**检查、准备、安装、现场质量控制、清洁和保护。

### 2.3 Uniclass——国际（RIBA/NBS）

建筑行业统一分类体系，比 NBS 工作分部更全面，用于 BIM 分类。

**表：**
- Co — Complexes (campus, estate)
- En — Entities (building, bridge)
- Ac — Activities (design, construction)
- SL — Spaces/Locations (rooms, zones)
- EF — Elements/Functions (wall, roof, floor)
- Ss — Systems (curtain wall system, underfloor heating)
- Pr — Products (brick, insulation board, steel beam)
- TE — Tools and Equipment

---

## 3. 规格类型

### 3.1 性能规格

定义所需结果或性能，但不规定具体产品或方法。

**优点：**
- 允许承包商创新和价值工程。
- 聚焦关键事项（性能）。
- 减少规格篇幅。
- 适用于设计—建造采购。

**缺点：**
- 需要可测量的性能标准。
- 投标评审更困难（涉及主观判断）。
- 存在采用最低成本合规方案的风险。
- 需要严格的测试和验证。

**示例——幕墙性能规格：**
```
幕墙系统应达到以下性能标准：
- Air permeability: ≤ 1.5 m³/h/m² at 600 Pa (BS EN 12152, Class AE)
- Watertightness: no water penetration at 600 Pa (BS EN 12154, Class RE 600)
- Wind resistance: ±2400 Pa serviceability, ±3600 Pa safety (BS EN 13116)
- Thermal transmittance: Ucw ≤ 1.3 W/m²K (EN 13947)
- Acoustic performance: Rw ≥ 38 dB (EN ISO 10140)
- Fire: E60 integrity, EI30 insulation at spandrel (EN 1364-4)
```

### 3.2 规范性规格

规定确切的产品、材料、尺寸和安装方法。

**优点：**
- 清晰明确。
- 便于报价和比较投标。
- 建筑师可控制最终材料效果。
- 合规验证简单。

**缺点：**
- 限制承包商替代方案。
- 建筑师承担产品性能责任。
- 产品不可用时必须更新规格。
- “或同等产品”条款会造成歧义。

**示例——砖砌体规范性规格：**
```
Facing bricks shall be Ibstock Leicester Red Stock, 215 × 102.5 × 65 mm,
compressive strength ≥ 25 MPa, water absorption 8-14%, frost resistant (F2),
laid in Flemish bond with bucket handle joints, 10 mm wide, in 1:1:6 mortar
(OPC:lime:sand) using Hanson Natural Hydraulic Lime NHL 3.5.
```

### 3.3 专有规格

指定具体制造商和产品，是限制性最强的形式。

**适用情形：**
- 只有一个产品符合设计意图时。
- 制造商参与了设计深化时。
- 业主有批量采购协议时。
- 项目需要与既有安装相匹配时。

**法律要求：**多数公共采购要求加入“或经批准的同等产品”条款，以确保公平竞争；私人项目可指定单一来源。

### 3.4 参考标准规格

引用已发布的标准作为规格依据，标准文件成为合同的一部分。

**示例：**“结构钢工程应符合 BS EN 1090-2，执行等级 EXC2。”

**注意：**务必注明标准版本/年份。标准会修订；不注明日期意味着采用投标时的现行版本，可能与设计意图不同。

---

## 4. 报审文件与审批

### 4.1 报审文件类型

| 报审文件类型 | 目的 | 时间 | 审核人 |
|---|---|---|---|
| 施工图 | 详细加工/安装图 | 加工前 | 建筑师 + 结构工程师 |
| 产品资料 | 制造商样本、测试报告 | 采购前 | 建筑师 |
| 样品 | 用于审批的实体材料样品 | 采购前 | 建筑师 + 业主 |
| 样板 | 用于质量基准的足尺构造 | 批量生产前 | 建筑师 + 业主 + 工程师 |
| 测试报告 | 指定性能的第三方测试结果 | 安装前/安装期间 | 工程师 |
| 证书 | ISO、CE、第三方认证 | 采购前 | 建筑师 |
| 色卡 / RAL | 精确的颜色选择 | 制造前 | 建筑师 + 业主 |
| 施工方案 | 施工方法说明 | 开工前 | 项目经理 + HSE |
| 保修 | 书面保证 | 实际竣工前 | 业主法律团队 |

### 4.2 审批签章

标准审批意见：
- **批准：**按提交内容继续，无需修改。
- **按批注批准：**按报审文件上的小幅修正继续，无需重新提交。
- **修改后重新提交：**存在重大问题，必须修正并经审核后方可继续。
- **拒绝：**不符合要求，需重新编制或提交替代方案。

**关键原则：**报审文件获批并不免除承包商遵守合同文件的责任。建筑师审核仅针对总体符合性。

### 4.3 样品与样板要求

**留存样品：**
- 砖：至少 6 块，展示完整的颜色和纹理范围
- 石材：每种石材至少 300 × 300 mm 样品
- 金属饰面：至少 300 × 300 mm，并包含指定饰面
- 涂料/涂层：在指定基层上提供至少 A4 尺寸样品
- 木材：至少 300 × 150 mm，展示纹理、颜色和饰面
- 玻璃：每种玻璃在 IGU 配置中至少提供 300 × 300 mm 样品
- 砂浆：至少 3 块样板（600 × 600 mm），采用指定勾缝形式

**样板：**
- 目的：建立质量基准、测试安装方法并核实外观。
- 典型范围：3 m × 3 m 立面构造板（至少 2 个开间 × 2 层）。
- 必须包含门窗洞口、转角、伸缩缝和泛水板。
- 施工期间留在现场，作为参考标准。
- 样板耐候测试：按 BS EN 1027 或 AAMA 501.1 进行淋水试验。

---

## 5. 材料测试与认证

### 5.1 CE 标志 / UKCA 标志

**CE 标志（欧盟）：**
- 对受协调欧洲标准（hEN）或欧洲技术评定（ETA）覆盖的产品为强制要求。
- 由制造商出具性能声明（DoP）。
- 某些产品（结构钢、防火产品）需要公告机构参与。
- 主要产品标准：EN 197（水泥）、EN 206（混凝土）、EN 771（砌体）、EN 1090（钢材）、EN 14080（胶合木）、EN 14351（门窗）。

**UKCA 标志（脱欧后的英国）：**
- 在英国市场等同于 CE 标志。
- 英国批准机构取代欧盟公告机构。
- 允许 CE 标志的过渡期已延长；应核实当前状态。

### 5.2 主要测试标准

**混凝土：**
- BS EN 12390 系列：抗压强度（第 3 部分）、劈裂抗拉强度（第 6 部分）、密度（第 7 部分）
- BS EN 12504：结构评定（芯样、回弹仪、超声波）
- 坍落度试验：BS EN 12350-2

**钢材：**
- BS EN 10025：热轧结构钢（轧钢厂证书 EN 10204 3.1）
- BS EN 1090：钢结构施工（CE 标志；EXC1–4）
- 夏比冲击试验：BS EN ISO 148-1
- 焊缝检验：目视、超声波（UT）、磁粉（MPI）、射线（RT）

**木材：**
- BS EN 338: strength classes (C14-C50 softwood, D18-D70 hardwood)
- BS EN 14081: strength grading of structural timber (machine or visual)
- BS EN 14080: glued laminated timber — requirements
- BS EN 16351: CLT — structural properties
- Moisture content: BS EN 13183 (oven-dry or electrical resistance)

**砌体：**
- BS EN 771: specification for masonry units (Part 1: clay, Part 2: calcium silicate, Part 3: concrete)
- BS EN 772: test methods (dimensions, compressive strength, water absorption, frost resistance)
- BS EN 1052: test methods for masonry (compressive, flexural, shear strength)
- 砂浆：BS EN 998-2（规格）；BS EN 1015（试验方法）

**玻璃：**
- BS EN 12150: thermally toughened glass
- BS EN ISO 12543: laminated glass
- BS EN 1279: insulating glass units (gas fill, moisture penetration, edge seal)
- BS EN 410: optical properties (VLT, SHGC)
- BS EN 673: thermal transmittance (U-value calculation)
- Impact: BS EN 12600 (pendulum test; classification 1B1 most demanding)

**防火测试：**
- BS EN 13501-1: reaction to fire classification (Euroclass A1 to F)
- BS EN 13501-2: fire resistance classification (R, E, I, W)
- BS 476: Parts 6 and 7 (UK fire propagation and surface spread of flame — legacy standard)
- ASTM E84: surface burning characteristics (Flame Spread Index, Smoke Developed Index) — USA
- ASTM E119: fire endurance test (walls, floors, columns) — USA
- UL 263: fire tests of building construction and materials — USA

**风化/耐久性：**
- BS EN 12371: frost resistance of natural stone
- BS EN 539-1: frost resistance of clay roofing tiles
- BS EN ISO 12944: corrosion protection of steel by paint coatings (environment C1-CX, durability L/M/H)
- ASTM G154: UV accelerated weathering (QUV test)
- BS EN ISO 9227: salt spray corrosion test

### 5.3 ASTM 主要标准（北美）

| 标准 | 材料 | 测试 |
|---|---|---|
| ASTM C39 | 混凝土 | 圆柱体抗压强度 |
| ASTM C150 | 波特兰水泥 | 化学/物理要求 |
| ASTM C90 | 混凝土砌体 | 承重砌块 |
| ASTM C216 | 饰面砖 | 物理要求 |
| ASTM C270 | 砂浆 | 配比和性能规范 |
| ASTM C1048 | 玻璃 | 热增强和钢化平板玻璃 |
| ASTM A36 | 钢材 | 碳素结构钢 |
| ASTM A992 | 钢材 | 结构钢型材（W 截面） |
| ASTM A572 | 钢材 | 高强度低合金结构钢 |
| ASTM D3498 | 胶粘剂 | 建筑胶粘剂 |
| ASTM E84 | 全部材料 | 表面燃烧（火焰传播） |
| ASTM E119 | 全部材料 | 耐火性能 |
| ASTM E331 | 幕墙 | 静压下的水渗透 |
| ASTM E283 | 幕墙 | 空气渗漏 |
| ASTM E330 | 幕墙 | 结构风荷载 |

---

## 6. 现场质量保证

### 6.1 检查与测试计划（ITP）

ITP 定义所有检查和测试活动、时间、验收标准及责任方。

**标准 ITP 要素：**

| 活动 | 时间 | 方法 | 验收标准 | 责任方 | 停检/见证/审核 |
|---|---|---|---|---|---|
| 混凝土立方体试验 | 每 50 m³ 或每日 | BS EN 12390-3 | fck + 裕量 | 承包商 | 审核 |
| 钢筋保护层检查 | 浇筑前 | 保护层测定仪检测 | 规范值 ± 容差 | 承包商 | 见证 |
| 钢材焊缝检查 | 制作期间 | 目视 + UT/MPI | EN 1090 EXC2 | CSWIP 检查员 | 停检 |
| 砖墙样板批准 | 首块样板完成 | 目视 + 测量 | 与批准样品一致 | 建筑师 | 停检 |
| 幕墙样板 | 生产前 | AAMA 501.1 / EN 13050 | 通过全部标准 | 专业分包 | 停检 |
| 木材含水率检查 | 到货时 | 电阻法 | ≤18%（结构用） | 承包商 | 审核 |
| 气密性试验 | 围护结构完成时 | EN ISO 9972（鼓风门） | ≤目标值（q50 或 n50） | 专业分包 | 停检 |
| 防火封堵 | 安装后 | 目视 + 探针 | 封堵完整；提供证书 | 防火顾问 | 见证 |

### 6.2 停检点

停检点是强制检查阶段，建筑师、工程师或检查员批准前一阶段之前，工程不得继续。未经批准越过停检点施工属于违约。

**关键停检点：**
1. 基础开挖——浇筑混凝土前检查基底。
2. 钢筋——浇筑前检查保护层、间距、搭接和马凳。
3. 结构钢连接——包覆或安装幕墙前检查。
4. 防水——回填或覆盖前检查。
5. 立面样板——生产开始前批准。
6. 防火封堵——饰面遮蔽前检查。
7. 吊顶上方设备——安装吊顶前检查。
8. 竣工前气密性——如可能，在室内饰面前测试。

### 6.3 不符合项处理程序

当工程或材料不符合规格时：
1. **识别：**现场检查员或工程监理提出不符合报告（NCR）。
2. **记录：**拍照、测量并记录 NCR 详情。
3. **评估：**工程师/建筑师评估影响（结构、美观、性能）。
4. **决策：**接受现状（附理由）、整改/修复，或拒绝并更换。
5. **关闭：**确认纠正措施，更新记录并防止再次发生。

---

## 7. 常见规格错误

### 7.1 歧义与冲突

1. **Drawing-specification conflict:** Drawing shows concrete block; specification calls for brick. Resolution: establish clear hierarchy in contract conditions.
2. **"Or equal" without criteria:** "Manufacturer X or equal" without defining what "equal" means. Fix: define the performance criteria that constitute equality.
3. **Outdated standards:** Citing withdrawn standards (e.g., BS 476 instead of EN 13501). Always verify current status.
4. **Conflicting performance requirements:** Specifying both a prescriptive product AND performance criteria that the product may not meet. Use one approach per clause.

### 7.2 过度规定

5. **Unnecessarily restrictive tolerances:** Specifying ±1 mm where ±3 mm is adequate adds cost without benefit.
6. **Excessive testing frequency:** Requiring cube tests every 10 m³ instead of 50 m³ for standard concrete.
7. **Premium products for concealed work:** Specifying architectural-grade concrete for buried foundations.
8. **Single-source proprietary without justification:** Naming one manufacturer when multiple equivalents exist — may invite legal challenge on public projects.

### 7.3 规定不足

9. **Missing performance criteria:** Specifying "aluminium curtain wall" without U-value, air permeability, water tightness, or acoustic requirements.
10. **No sample/mock-up requirement:** Omitting mock-up for visible facade work leads to disputes about quality.
11. **Undefined finish quality:** "Fair-faced concrete" without reference sample or defined tolerance class (DIN 18217 / SCC classes).
12. **No maintenance information:** Failing to specify maintenance manuals, spare parts, or warranty documentation.

### 7.4 协调失误

13. **Uncoordinated interfaces:** Structural specification calls for S355 steel; facade specification assumes S275 connections at fixing points.
14. **Missing builder's work:** Specification for curtain wall does not include requirement for structural cast-in channels or brackets.
15. **Fire strategy gaps:** Fire-rated partition specified but no fire stopping specified at service penetrations.
16. **Inconsistent sustainability targets:** BREEAM specification requires BES 6001 responsible sourcing, but individual material sections do not reference it.

### 7.5 采购错误

17. **No lead-time awareness:** Specifying a natural stone with 16-week quarrying and import lead time on a 12-week programme.
18. **Discontinued products:** Specifying a product that has been discontinued or is only available in minimum bulk quantities.
19. **No substitution procedure:** Failing to define how substitution requests are handled, documented, and approved.
20. **Mismatched warranty periods:** Building warranty requires 12-year defects liability but specified sealant warranty is 10 years.

---

## 8. 规格最佳实践

### 8.1 编写原则

1. **使用祈使语气：**使用“The contractor shall...”，而非“The contractor should...”。
2. **具体且可测量：**使用“抗压强度 ≥30 MPa”，而非“强度足够”。
3. **每条款一个要求：**避免包含多个条件的复合条款。
4. **谨慎交叉引用：**确保引用文件列入一般要求章节。
5. **术语一致：**在一般要求中定义关键术语，并在全文一致使用。
6. **性能规格避免制造商偏向：**定义产品必须达到的性能，而不是指定制造商。
7. **包括全部验收标准：**规定测试时同时规定通过/不通过阈值。
8. **规定正向要求：**使用“应为……”，而非“不得为……”（禁止物质除外）。

### 8.2 可持续性条款

现代规格应包括：
- **隐含碳限值：**每 m² 或每功能单位的最大 kgCO2e，并以 EPD（环境产品声明）作为证据。
- **负责任采购：**BES 6001、FSC/PEFC（木材）、ASI（铝材）、ResponsibleSteel。
- **最低再生含量：**例如混凝土再生骨料 ≥25%，结构钢再生含量 ≥90%。
- **低 VOC 材料：**Greenguard Gold、法国 A+ 排放等级、EN 16516 测试。
- **材料护照：**要求制造商提供 Madaster 或同等材料护照数据。
- **可拆解设计：**可行时规定螺栓连接，并识别未来可再利用的构件。

### 8.3 协调检查清单

发布规格前：
- [ ] 所有规格分部均已与当前图纸核对。
- [ ] 结构、机械、电气和立面规格已相互交叉引用。
- [ ] 所有引用标准均已核实为现行版本。
- [ ] 样品和样板要求及审批流程已明确规定。
- [ ] 消防策略要求已纳入所有相关分部。
- [ ] Sustainability and embodied carbon requirements included
- [ ] Warranty periods coordinated with contract requirements
- [ ] Lead times checked for critical materials
- [ ] Hold points and witness points defined in ITP
- [ ] O&M manual requirements specified for all maintainable elements
#

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab AI建筑与室内设计总设计师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
