license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
name: country-germany
description: >
  德国建筑规范与法规参考。涵盖 Musterbauordnung（MBO 2002，2019 年最新修订）这一联邦示范文本，以及各联邦州具有约束力的 16 部 Landesbauordnungen（LBO）
  (BayBO Bavaria, BauO NRW North Rhine-Westphalia, BauO Bln Berlin, HBauO Hamburg, BauO Bbg
  Brandenburg, NBauO Lower Saxony, HBO Hesse, BauO LSA Saxony-Anhalt, SaechsBO Saxony, ThuerBO
  Thuringia, LBauO Rheinland-Pfalz, LBO BW Baden-Wuerttemberg, BauO SH Schleswig-Holstein, BauO
  M-V Mecklenburg-Vorpommern, LBO Saarland, BauO Bremen），联邦《建筑能源法》（GEG）
  GEG 2023、德国 Eurocode 国家附录（DIN EN 1990-1999/NA）、DIN 18040 无障碍系列（第 1 部分公共建筑、第 2 部分住宅、第 3 部分公共空间）、DIN 4109 隔声、DIN 4108 保温、DIN 4102/EN 13501 防火分类、适用于特殊建筑的高层建筑示范指南与特别建筑法规、适用于集会建筑的集会场所法规、工业建筑指南、医院 KrPflVO/HHRRL、消防安全证明方法、BAFA/KfW 激励认证制度、DGNB 认证、Effizienzhaus 40/55/70 标准、2024 年供热法、Bauwerksbuch（建筑文档）、TGA/HKLS 工程专业以及德国 BIM 联邦强制要求时间表。
license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
# 国家：德国

适用于德国 16 个 Bundeslaender（联邦州）项目的建筑规范与法规参考。当提及德国城市、德国语境下的 EUR 货币、“DIN”/“LBO”/“GEG”/“MBO”/“BayBO”/“Energieausweis”/“Brandschutznachweis”/“Effizienzhaus”/“DGNB”/“KfW”/“BauO”，或德国技术术语（Geschossflaechenzahl、Grundflaechenzahl、Vollgeschoss、Bauantrag、Bauvoranfrage、Rohbau）时启用本技能。

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 1. 法规层级

德国采用 **Archetype C（联邦框架+州主权）** 体系。《基本法》（Grundgesetz）将建筑法权限保留给各州。联邦 Musterbauordnung 仅为示范文本，各州分别发布具有约束力的 LBO。巴伐利亚、北莱茵-威斯特法伦、柏林等州之间存在显著差异。

### 1.1 主管机构层级

```
第 1 级——联邦（Bund）
  联邦住房、城市发展与建筑部（BMWSB）——住房/城市政策
  联邦经济与气候保护部（BMWK）——能源 + GEG
  联邦内政部（BMI）——部分安全法规
  Deutsches Institut fuer Bautechnik (DIBt) -- 产品批准、技术法规
  Bauministerkonferenz (BMK) -- 各州建筑部长政府间会议；发布 Musterbauordnung MBO（示范规范）
  Deutsche Akkreditierungsstelle (DAkkS) -- 认证
  Bundesamt fuer Bauwesen und Raumordnung (BBR) -- 联邦建筑机构
  Bundesanstalt fuer Wirtschaft und Ausfuhrkontrolle (BAFA) -- 能源激励
  KfW (Kreditanstalt fuer Wiederaufbau) -- 低息贷款 + Effizienzhaus 标准

第 2 级——州（Land）
  16 个 Bundeslaender 各自设有：
    - Landesbauordnung (LBO) -- 具有约束力的建筑规范
    - Bauministerium des Landes -- 州建筑部
    - Oberste Bauaufsicht -- 最高建筑主管部门
    - 认可机构名录（Verzeichnis der bauaufsichtlich anerkannten Stellen）

第 3 级——区/市镇（Kreis / Gemeinde / Stadt）
  市级 Bauamt（建筑主管部门），或小型市镇的 Kreisbauamt（区建筑主管部门）
  Bauaufsichtsbehoerde -- 执行 LBO
  Stadtplanungsamt -- 城市规划（实施 Bebauungsplan）
  Brandschutzdienststelle -- 消防安全
  Untere Wasserbehoerde -- 水务
  Naturschutzbehoerde -- 自然/环境保护

第 4 级——项目
  通过 Bauvorlageberechtigte（获准提交文件的注册建筑师或工程师）提交 Bauantrag（正式许可）或 Bauvoranfrage（预审咨询）
  Pruefingenieure 负责结构审查（部分州）/ Pruefsachverstaendige 负责消防审查
  Berufsfeuerwehr / Freiwillige Feuerwehr -- 消防部门审查（与 Brandschutzdienststelle 联合）
  Energieberater 负责 Energieausweis + GEG 合规认证
```

### 1.2 各州 LBO 状态

16 个 LBO 总体沿用 MBO 2002/2019，但各州均有具体差异。跨州执业时必须注意：

| 州 | LBO | 首府 | 备注 |
|---|---|---|---|
| Baden-Wuerttemberg | LBO BW（最近修订 2024） | Stuttgart | 最进步的州之一；严格整合 KfW + GEG |
| Bayern（巴伐利亚） | BayBO 2008（含修订） | Munich | 具有独立体系；遗产保护条款严格 |
| Berlin | BauO Bln 2005 + 2020 + 2023 修订 | Berlin | 城市州；Senatsverwaltung fuer Stadtentwicklung |
| Brandenburg | BauO Bbg | Potsdam | 与 MBO 高度一致 |
| Bremen | BremLBO | Bremen | 城市州 |
| Hamburg | HBauO | Hamburg | 城市州；Behoerde fuer Stadtentwicklung |
| Hessen | HBO（Hess Bauordnung） | Wiesbaden | 无障碍要求独特 |
| 梅克伦堡-前波美拉尼亚州 | BauO M-V | 什未林 | 沿海：盐雾+风荷载 |
| Niedersachsen | NBauO | Hannover | 考虑风区 |
| 北莱茵-威斯特法伦州 | BauO NRW 2018（已修订） | 杜塞尔多夫 | 人口最多；ZBau（主管建筑部门） |
| Rheinland-Pfalz | LBauO | Mainz | 与 MBO 一致 |
| Saarland | LBO | Saarbruecken | 最小州；少量调整 |
| Sachsen | SaechsBO | Dresden | 遗产保护条款独特 |
| Sachsen-Anhalt | BauO LSA | Magdeburg | 具有独立要求 |
| Schleswig-Holstein | LBO SH | Kiel | 风荷载与沿海因素 |
| Thueringen | ThuerBO | Erfurt | 与 MBO 一致 |

### 1.3 覆盖或补充 LBO 的联邦法规

尽管建筑法属于州权限，以下事项由联邦统一管辖：
- **GEG 2023**——联邦能源规范，全国具有约束力
- **Heizungsgesetz / GEG 2024 修订**——供热系统更换规则
- **DIN 标准**——技术参考标准（被 LBO 引用时具有法律约束力）
- **《建筑产品法规》（CPR/EU 305/2011）**——欧盟法规
- **《能源节约条例》EnEV（现已由 GEG 取代）**——历史法规
- **GefStoffV**——危险物质
- **ArbStaettV**——工作场所条例（工作场所尺寸、照明、通风）
- **BImSchG**——联邦污染控制（噪声 + 排放）

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 2. MBO + LBO 核心要求

### 2.1 建筑类别（Gebaeudeklassen）

MBO 2002 § 2(3) / 各州 LBO 对应条款定义 **5 类建筑类别（GK 1–5）**：

| GK | 描述 | 高度与用途 | 主要影响 |
|---|---|---|---|
| **GK 1** | 高度不超过 7 m 的独立建筑，单户/双户住宅，面积 ≤400 m²，或独立农业建筑 | 小型独立住宅/双拼住宅 | 要求较宽松，通常无需审查 Brandschutznachweis |
| **GK 2** | 高度不超过 7 m 的独立或半独立建筑，最多 2 个居住单元，总楼面面积 ≤400 m² | 独立/半独立住宅 | 要求宽松 |
| **GK 3** | 其他高度 ≤7 m 的建筑 | 联排住宅、2–3 层小型公寓 | 标准消防/结构要求 |
| **GK 4** | 高度 ≤13 m，且每个 Nutzungseinheit（使用单元）最大 400 m² | 中层公寓 | 中等要求 |
| **GK 5** | 高度 >13 m（高层阈值为 22 m）或地下建筑 | 中层办公、中层住宅 | 消防要求较高 |
| **高层建筑（特殊）** | 从最低消防车辆通行面以上的使用楼层高度 >22 m | 高层建筑 | Sonderbau；适用高层建筑指令（Musterhochhausrichtlinie 及州级规定） |

### 2.2 特殊建筑（Sonderbauten）

MBO 2002 § 2(4) 定义 Sonderbauten——因规模、用途或风险而需要特别审查的建筑。示例：
- Hochhaeuser (>22 m)
- Versammlungsstaetten（集会场所）>200 人
- Schulen、Hochschulen（学校、大学）——通常属于 Sonderbau
- Krankenhaeuser、Heime（医院、护理机构）
- Verkaufsstaetten（零售）>2000 m²
- Garagen (parking) > 100 m2
- Industriebauten（特定工业建筑）
- 各州清单中列出的其他建筑

Sonderbauten 还需适用以下附加条例：
- **MVStaettVO**——Muster-Versammlungsstaettenverordnung（集会建筑）
- **MIndBauR**——Muster-Industriebaurichtlinie（工业建筑）
- **MGarVO**——Muster-Garagenverordnung（停车建筑）
- **HochhausR**——Musterhochhausrichtlinie（高层建筑）
- **KrPflVO** / **HHRRL**——医院法规（州级）
- **MVkVO**——Muster-Verkaufsstaettenverordnung（零售建筑）

各州可原样采用 Muster（示范）版本，也可进行修改后采用。

### 2.3 规划法（Baugesetzbuch + BauNVO）

规划属于联邦权限：**Baugesetzbuch（BauGB）** + **Baunutzungsverordnung（BauNVO）**：
- **Flaechennutzungsplan（FNP）**——市镇土地利用规划（宏观分区）
- **Bebauungsplan（B-Plan）**——详细分区，对单个地块具有约束力
- **§ 34 BauGB**——“Innenbereich”建成区填充开发，应符合既有环境
- **§ 35 BauGB**——“Aussenbereich”建成区外区域，通常受到限制

**关键规划参数（BauNVO）：**
- **GRZ（Grundflaechenzahl）**——建筑基底面积与用地面积之比（例如 0.4 = 覆盖率 40%）
- **GFZ（Geschossflaechenzahl）**——地上总楼面面积与用地面积之比（类似 FAR；例如 1.2 = 120%）
- **BMZ（Baumassenzahl）**——每平方米用地的建筑体量（工业用途）
- **Vollgeschoss**——“完整楼层”，有明确法律定义；地下室/阁楼通常只计部分面积
- **Abstandsflaechen**（退界区域）——通常为建筑高度的 0.4–1.0 倍（因州和分区而异）；距用地边界至少 3 m

### 2.4 退界与密度（以 BayBO 为例）

| 用途地域（BauNVO § 3-11） | 典型 GRZ | 典型 GFZ | 典型建筑类别 |
|---|---|---|---|
| WR（纯住宅区） | 0.4 | 1.2 | GK 1-3 |
| WA（一般住宅区） | 0.4 | 1.2 | GK 1-3（可为5） |
| WB（特殊住宅区） | 0.6 | 1.6 | GK 3-5 |
| MD（村镇区） | 0.6 | 1.2 | GK 1-3 |
| MK（核心区——市中心） | 1.0 | 3.0 | GK 5+高层建筑 |
| GE (Gewerbegebiet) | 0.8 | 2.4 | 因项目而异 |
| GI (Industriegebiet) | 0.8 | 2.4+ | 因项目而异 |

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 3. 防火安全（Brandschutz）

### 3.1 Brandschutznachweis（防火安全方案）

德国大多数项目都需要 **Brandschutznachweis**，即作为 Bauantrag 一部分提交的防火安全方案。所需深度取决于建筑类别：
- **GK 1–3**：通常采用简化审查（Vereinfachte Pruefung）。
- **GK 4–5**：需要完整 Brandschutznachweis，通常由经州许可的 Pruefsachverstaendiger 或防火 Pruefingenieur 编制。
- **Sonderbauten**：除完整方案外，还需遵循适用条例的特殊条款（如 MVStaettVO）。

### 3.2 耐火等级（DIN 4102 → EN 13501-2）

德国历史上采用 DIN 4102（F30、F60、F90、F120、F180）；现已协调采用 **EN 13501-2**（R30、REI60、REI90 等），但日常仍广泛使用 DIN 4102：

| 原 DIN 4102 | 新 EN 13501-2 | 时间 |
|---|---|---|
| F30 | R30 / REI 30 | 30 min |
| F60 | REI 60 | 60 min |
| F90 | REI 90 | 90 min |
| F120 | REI 120 | 120 min |
| F180 | REI 180 | 180 min |

材料分类还包括：
- A1、A2——不可燃
- B（Brandverhalten，燃烧性能）；-s1、d0 等表示烟气和滴落物等级
- DIN 4102 保留旧字母：**A1、A2** 不可燃；**B1** schwerentflammbar（难燃）；**B2** normal entflammbar（正常可燃）；**B3** leicht entflammbar（易燃，多数用途禁止）

### 3.3 按建筑类别的防火分隔（MBO § 27–30 + DIN 4102/EN 13501）

| 要素 | GK 1–3 | GK 4 | GK 5 | 高层建筑 |
|---|---|---|---|---|
| Tragendes Bauteil（承重构件）——一般 | F30 | F60 | F90 | F90+ |
| Brandwaende（防火墙） | -- | F90/REI90（Sonderbau） | F90/REI90 | F90+ |
| Treppenraum（楼梯间） | F30 | F60 | F90 | F90+ + 加压 |
| Schachtwaende（竖井墙） | F30 | F60 | F90 | F90+ |
| Wohnungstrennwaende（住宅分隔墙） | F30 | F60 | F90 | F90+ |
| Dachhaut（屋面层） | hartdach（硬质屋面） | hartdach | hartdach | hartdach |

### 3.4 疏散距离（MBO 2002 § 35 + 特殊建筑条例）

- 一般情况：到出口或受保护楼梯/走道的最大行走距离为 **35 m**
- GK 4–5 设置喷淋并采用排烟管理时，可按 MVStaettVO 等规定增加距离
- Sonderbau 高层建筑：在使用单元内到达受保护楼梯前 ≤25 m
- **双向疏散行走**最大距离（规定从 Nutzungseinheit 任一点计算）约 30 m

### 3.5 楼梯宽度

按 MBO 2002 § 34：
- GK 3–5 主楼梯：**最小 1.00 m**（集会建筑为 1.20 m）
- Lichte Treppenbreite（净宽）：通常 1.00 m
- 楼梯最大踢面 **17 cm**；踏步 **28 cm**；舒适公式 2R+G = 63 cm

### 3.6 高层建筑（Musterhochhausrichtlinie）

适用于使用楼层高度超过 22 m 的建筑：
- 必须设置 **两部楼梯**（或根据具体方案设置一部带排烟和喷淋的楼梯）
- **楼梯排烟**或加压
- 全建筑设置**自动喷水灭火系统**
- **语音疏散**（Sprachalarmanlage）
- **Feuerwehraufzug**——满足扩展要求的消防电梯
- **Brandfallsteuerung**——火灾控制电梯
- 还需接受 **Brandschutzdienststelle** 审查
- 高度 >60 m 时，还需进行专项排烟工程分析

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 4. 能源规范（GEG 2023）

### 4.1 Gebaeudeenergiegesetz（GEG）

**Gebaeudeenergiegesetz 2023**（原 EnEV + EEWaermeG）是具有约束力的联邦能源法，整合能源、供热与可再生能源条款。

**主要要求：**
- **Primaerenergiebedarf (Qp)**：按建筑类型和参考值确定的目标
- **Hoechstwert spezifischer Transmissionswaermeverlust (HT')**：传热损失限值
- **Sommerlicher Waermeschutz**：夏季热防护（DIN 4108-2 简化计算或模拟）
- **新建建筑强制可再生热能**（自 2024 年起，Heizungsgesetz 修订后进一步收紧）：新供热系统中可再生能源占比 65%
- **Bauteilanforderungen**：构件级要求（可替代整栋建筑计算）

### 4.2 GEG 2024 修正案（Heizungsgesetz）

- 联邦供热法：自不同期限起禁止新安装化石燃料供热系统（取决于建筑年代和规模）
- Bestandsgebaeude（既有建筑）：从分阶段实施日期起，更换供热系统必须有 65% 来自可再生能源
- 优先采用热泵、区域供热和生物质能

### 4.3 Effizienzhaus（KfW）

GEG 之外的 KfW 资助标准：
- **Effizienzhaus 40** = 参考 Primaerenergiebedarf 的 40%（较少见；要求很严格）
- **Effizienzhaus 55** = 55%（常见的新建目标）
- **Effizienzhaus 70** = 70%（现已较容易；被 GEG 基准取代）
- **Effizienzhaus 100** = 基准值（不再享受补贴）

其他分类：
- **Effizienzhaus 40 EE**——强调可再生能源
- **Effizienzhaus 40 NH**——具有可持续性（Nachhaltigkeit）认证
- **Effizienzhaus 55 EE** 等

### 4.4 Energieausweis（能源性能证书）

自 2007 年（EnEV）/2014 年（全面扩展）起，新建建筑、销售和出租必须提供：
- **Verbrauchsausweis**（基于能耗——适用于有使用记录的既有建筑）
- **Bedarfsausweis**（基于需求——计算得出；新建和翻新后必须提供）
- 由具备资质的 Energieberater 出具
- 有效期 10 年
- 能源等级 A+ 至 H

### 4.5 DIN 4108 + DIN V 18599

- **DIN 4108-2**——最低热工隔绝（构件级）
- **DIN 4108-6**——年供热需求计算
- **DIN V 18599（10 个部分）**——建筑能源评估，是 GEG 计算的参考标准

### 4.6 U 值目标（GEG 2023 + KfW）

| 要素 | GEG 2023 基准 | Effizienzhaus 55 | Effizienzhaus 40 |
|---|---|---|---|
| 外墙U值（W/m2K） | 0.24-0.28 | 0.20 | 0.15 |
| 屋面/顶层楼板U值 | 0.20-0.24 | 0.16 | 0.12 |
| 地坪U值 | 0.30 | 0.20 | 0.15 |
| 窗Uw值 | 1.3 | 1.0 | 0.80 |
| 入户门U值 | 1.8 | 1.4 | 1.2 |
| 气密性n50 | 有机械通风1.5/h；无机械通风3.0/h | 1.0/h | 0.6/h（被动房水平） |

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 5. 无障碍（DIN 18040）

### 5.1 DIN 18040 系列

最常引用的无障碍标准：
- **DIN 18040-1:2010**——公共建筑（Oeffentlich zugaengliche Gebaeude）
- **DIN 18040-2:2011**——住宅（Wohnungen），带 rollstuhlgerecht “R” 标记表示完全轮椅无障碍
- **DIN 18040-3:2014**——公共空间与交通基础设施

### 5.2 关键尺寸（DIN 18040-1）

| 要素 | 尺寸 |
|---|---|
| 要素 | 尺寸 |
|---|---|
| 最小活动空间 | 1.50 m × 1.50 m |
| 门净宽 | 90 cm（宜采用）；绝对最小 80 cm |
| 门操作力 | <25 N |
| 坡道坡度 | ≤6%（1:16.7）——明显严于 ADA 的 1:12（8.33%） |
| 坡道平台 | 每行进 6 m 设置 1.50 m 平台，顶部和底部均设置 |
| 电梯轿厢 | 1.10 m × 1.40 m（Type 1）；1.10 m × 2.10 m（担架型；医院） |
| 门槛 | 最大 2 cm |
| 无障碍卫生间 | 最小 2.20 m × 2.20 m；坐便器左右两侧各至少 90 cm 净空 |
| 无障碍停车位 | 宽 3.50 m × 长 5.00 m（不单独设置通道，整个车位按无障碍需求确定） |
| 触觉引导路径 | 宽 30 cm；对比度 0.4（Michelson 对比度）；按 DIN 32984 |

### 5.3 分级方法

DIN 18040-1 区分：
- **Barrierefreiheit**（一般无障碍/无障碍通行）
- **R-Kennzeichnung**（rollstuhlgerecht——完全轮椅无障碍）——带 R 后缀的更高标准

### 5.4 LBO 要求

每个 LBO 均要求以下建筑具备无障碍条件：
- **Wohngebaeude（住宅）**——面向公众的入口、公共区域及部分住宅单元
- **Oeffentliche Gebaeude（公共建筑）**——全面符合 DIN 18040-1
- **Arbeitsstaetten（工作场所）**——按 ArbStaettV + DIN 18040-1

配置数量因州而异。通常：
- 大型项目中 1% 的住宅需无障碍
- 4 层以上的公寓需无障碍（LBO 要求设置电梯）

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 6. 声学（DIN 4109）

### 6.1 DIN 4109——隔声

**DIN 4109-1:2018**——最低要求：
- 住宅之间的墙体：R'w（表观隔声量）≥53 dB
- 住宅之间的楼板：L'n,w（撞击声）≤50 dB；R'w ≥54 dB
- 住宅与走道之间的墙体：R'w ≥52 dB

**DIN 4109-5**——更高要求（Schallschutzanforderungen erhoehter Schallschutz）：
- 住宅之间的墙体：R'w ≥56 dB

**VDI 4100**——Schallschutz im Hochbau——3 个隔声等级（SSt I、II、III），通常用于规定高于最低要求的性能。

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 7. 结构与荷载（含德国国家附录的 Eurocodes）

### 7.1 Eurocode 系列（DIN EN 1990–1999）

自 2012 年起，德国项目均采用带德国国家附录的 Eurocodes（DIN EN 1990 NA–DIN EN 1999 NA）：

| Eurocode | 主题 |
|---|---|
| DIN EN 1990 + NA | 基本原则 |
| DIN EN 1991（10 个部分）+ NA | 作用（1-1 一般、1-2 火灾、1-3 雪、1-4 风、1-5 温度、1-7 偶然作用等） |
| DIN EN 1992（3 个部分）+ NA | 混凝土 |
| DIN EN 1993（1-1 至 1-12、2、3、4、5、6 部分）+ NA | 钢结构 |
| DIN EN 1994 + NA | 组合结构 |
| DIN EN 1995（1-1 至 1-2、2 部分）+ NA | 木结构 |
| DIN EN 1996 + NA | 砌体 |
| DIN EN 1997 + NA | 岩土工程 |
| DIN EN 1998 + NA | 抗震 |
| DIN EN 1999 + NA | 铝结构 |

### 7.2 风区（DIN EN 1991-1-4 + DIN NA）

德国分为四个风区（WZ 1–4）：
- **WZ 1**——vb,0 = 22.5 m/s——西南部、中部
- **WZ 2**——vb,0 = 25.0 m/s——西部、中北部
- **WZ 3**——vb,0 = 27.5 m/s——北部海岸、中北部
- **WZ 4**——vb,0 = 30.0 m/s——北海沿岸

### 7.3 雪荷载分区（DIN EN 1991-1-3 + DIN NA）

三个雪荷载区（SLZ 1–3），另加海拔修正系数：
- **SLZ 1**——德国北部低地（sk = 0.65 + 海拔修正）
- **SLZ 2**——中部及东部部分地区（sk = 0.85 + 海拔修正）
- **SLZ 2a、3**——阿尔卑斯地区（更高；例如巴伐利亚阿尔卑斯 sk = 2.0+ kN/m²）

### 7.4 抗震（DIN EN 1998-1 + DIN NA）

德国地震活动性较低。全国大部分地区属于低地震区，莱茵地堑和施瓦本汝拉部分地区略高。抗震设计通常不是控制因素。

### 7.5 岩土工程（DIN EN 1997 + DIN NA + DIN 1054）

基础设计按 Eurocode 7 + DIN 1054；岩土勘察按 DIN EN 1997-2 + DIN 4020。

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 8. 可持续性与认证

### 8.1 DGNB（Deutsche Gesellschaft fuer Nachhaltiges Bauen）

德国主要的绿色建筑认证：
- 类别：Oekologisch（生态）、Oekonomisch（经济）、Soziokulturell-funktional（社会文化与功能）、Technisch（技术）、Prozess（过程）
- 等级：Bronze（铜）、Silver（银）、Gold（金）、Platinum（铂）
- 4 类建筑类型：新建、既有、社区、室内
- 在运营和生命周期评估方面比 LEED 更严格

### 8.2 Passivhaus 标准

起源于德国（达姆施塔特 Passivhaus Institut）。法兰克福等城市的许多社会住宅项目强制采用。五项标准：
- 供暖需求 ≤15 kWh/m²/年
- 一次能源需求（PE）≤60 kWh/m²/年（Classic；Plus/Premium 更低）
- 气密性 n50 ≤0.6/h
- 过热发生频率 ≤10%
- 供暖负荷 ≤10 W/m²

### 8.3 BNB（Bewertungssystem Nachhaltiges Bauen）

联邦政府自有的评估体系，用于联邦建筑。

### 8.4 EU Taxonomy / ESG 报告

大型项目需遵循 EU Taxonomy Climate Delegated Act 2021，并完成 CSRD 合规报告。

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 9. 许可流程（Bauantragsverfahren）

### 9.1 标准流程（Bauantrag）

1. **Bauvoranfrage**（可选）——向 Bauamt 提交预审申请，核查分区和关键问题。
2. **Bauantrag**——正式提交：总平面、平面图、剖面图、立面图、结构概念、防火方案（Brandschutznachweis）、无障碍证明（DIN 18040）、能源证明（GEG / Energieausweis）及 Statik（结构计算）。
3. **Bauvorlageberechtigung**——仅具有相应执照的建筑师或持证工程师可提交。
4. **Pruefverfahren**（审查期）——视州而定，为 6 周至 3 个月；特殊建筑更长。
5. **Auflagen**——主管机构提出的条件。
6. **Baugenehmigung**——核发许可证。
7. **Baubeginn anzeigen**——申报开工。
8. **Pruefingenieur Bestaetigung**——结构审查工程师确认 Statik。
9. **Brandschutzdienststelle Stellungnahme**——消防部门意见。
10. **Rohbauabnahme**——主体结构验收。
11. **Abnahmen**——各项专项验收。
12. **Bauabnahme**——竣工验收。
13. **Nutzungsaufnahme**——开始使用并登记 Energieausweis。

### 9.2 Vereinfachtes Verfahren

对于 GK 1–3（小型建筑），大多数州提供“Vereinfachtes Genehmigungsverfahren”（简化许可程序），审查时间更短、文件要求更少。

### 9.3 Genehmigungsfreie Verfahren

在具有有效 B-Plan 的住宅区内，GK 1–2 的部分工程可免许可（Verfahrensfrei），通常包括小型住宅扩建和附加建筑。

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 10. Quick Numeric Reference

| 参数 | 数值 | 来源 |
|---|---|---|
| 参数 | 数值 | 来源 |
| 住宅层高 | 通常 2.60–2.80 m | LBO + ArbStaettV；净高最小 2.40 m（部分州 2.30 m） |
| 办公层高 | 3.0–3.6 m | BCO 等效要求；ArbStaettV 净高最小 2.50 m |
| 门净宽 | 0.90 m（宜采用）；绝对最小 0.80 m | DIN 18040-1 / LBO |
| 坡道坡度 | 最大 1:16.7（6%） | DIN 18040-1（严于国际 8.33%） |
| 楼梯 2R+G 舒适值 | 63 cm | 德国经验法则 |
| 楼梯最大踢面 | 17 cm（住宅）、19 cm（工业） | MBO |
| 楼梯最小踏步 | 28 cm | MBO |
| 墙体 U 值（GEG 2023 基准） | 0.24–0.28 W/m²K | GEG 2023 + DIN V 18599 |
| 墙体 U 值（Effizienzhaus 40） | 0.15 W/m²K | KfW 标准 |
| 窗 U 值（GEG 2023） | 1.3 W/m²K | GEG 2023 |
| 住宅墙体隔声 R'w | 最小 53 dB | DIN 4109-1 |
| 最大行走距离 | 35 m | MBO § 35 |
| 柏林风速 vb,0 | 25 m/s | DIN EN 1991-1-4 NA |
| 慕尼黑雪荷载 sk | 0.85 + 海拔修正 kN/m² | DIN EN 1991-1-3 NA |

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 11. 应用流程

1. **确定 Bundesland**。
2. 根据高度、用途和规模确定 **Gebaeudeklasse（GK 1–5）**。
3. **确认是否属于 Sonderbau**——如属于，适用相关 Muster 条例。
4. **确认是否存在 Bebauungsplan 及其参数**（GRZ、GFZ、Vollgeschoss、Abstandsflaechen）。
5. 对一般、防火和无障碍要求适用该州的 **LBO**。
6. 对能源合规适用 **GEG 2023**（联邦强制要求）。
7. 对无障碍适用 **DIN 18040**。
8. 对结构适用含德国国家附录的 **Eurocodes**。
9. 对隔声适用 **DIN 4109**。
10. **确定审批路径**：Bauantrag（完整程序）、Vereinfachtes Verfahren（简化程序）或 Verfahrensfrei（免许可）。
11. **确认提交资格** Bauvorlageberechtigte。
12. **引用条款**：例如 “MBO 2002 § 26”、“BayBO § 26”、“GEG 2023 § 19”、“DIN 18040-1:2010 Punkt 4.5”、“DIN EN 1991-1-4/NA:2010 NDP 4.3”、“DIN 4109-1:2018 Tabelle 3”。

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 12. 权威来源

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
- **联邦建筑师协会（BAK）**——bak.de——联邦建筑师协会
- **Each Land Architektenkammer** -- regional architects' chambers

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
*交叉引用：加载 `building-codes` 了解一般规范结构（德国结构采用 Eurocode，但生命安全体系具有独特性）；加载 `fire-life-safety` 了解一般原则（并叠加 Brandschutznachweis 方法）；加载 `accessibility-design` 了解全球框架，再结合 DIN 18040；加载 `building-sustainability` 比较 Passivhaus、DGNB 与 LEED；加载 `building-envelope` 了解热工、声学和气候节点（德国南北存在多个气候区）；加载 `structural-systems` 进行基于 Eurocode 的设计。*
#

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab AI建筑与室内设计总设计师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
