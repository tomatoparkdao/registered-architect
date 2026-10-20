---
name: adjacency-methods
description: 注册建筑师专业参考：adjacency-methods。
license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---

# 邻接分析方法参考

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab AI建筑与室内设计总设计师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。

本参考全面介绍建筑策划中的邻近性分析、邻接矩阵、泡泡图、垂直分区分析和策划测试。

---

## 1. 邻接分析基础

### 1.1 目的

邻接分析将空间之间的功能关系转化为空间组织逻辑，连接建筑策划（需要哪些空间）与设计（空间放置在哪里）。缺乏严谨的邻接分析，建筑会出现：
- 交通空间过多（浪费面积和能源）
- 工作流程低效（工作人员需要走无谓的距离）
- 使用者困惑（导向性差）
- 环境冲突（不相容功能之间产生噪声、气味、振动）
- 安防漏洞（分区之间缺乏受控访问）

### 1.2 邻接关系类型

| 关系类型 | 定义 | 空间影响 |
|------------------|-----------|---------------------|
| 直接邻接 | 空间共用一面带连接门的墙 | 无需走廊，便利性最高 |
| 近邻 | 同层空间，步行距离不超过 30 m | 由短走廊连接，属于同一部门分区 |
| 同层 | 位于同一楼层，但不一定靠近 | 由主要交通系统连接 |
| 同一建筑分区 | 位于同一翼楼或区段 | 由次要交通系统连接 |
| 视觉联系 | 空间之间必须保持视线 | 采用玻璃隔断、开放平面或俯瞰关系 |
| 声学分隔 | 空间之间不得传递声音 | 实墙 STC 45+，设置缓冲区 |
| 受控访问 | 空间之间的通行需要安全许可 | 气闸、门禁读卡器、接待台 |
| 设备服务连接 | 空间共用管线、燃气或数据基础设施 | 湿墙背靠背、共用管井 |
| 垂直邻接 | 相邻楼层空间之间有直接联系 | 专用电梯、自动扶梯或内部楼梯 |

### 1.3 影响邻接评分的因素

为关系评分时，应根据以下标准评估每一对空间：

1. **使用者流量**：每小时有多少人往返这些空间？流量大 = 必须邻接。
2. **时间紧迫性**：移动延误是否会造成危害？（例如急诊科至手术室的延误可能危及生命）
3. **共享资源**：空间是否共用设备、人员或物资？
4. **环境兼容性**：噪声、气味、振动或安防等级是否相容？
5. **运营顺序**：空间是否属于连续的工作流程？
6. **公共与私密**：空间是否服务不同的访问群体？
7. **设备服务**：空间是否共用建筑设备服务基础设施？
8. **日光与景观**：空间是否争用同一面外墙？

---

## 2. 邻近矩阵方法

### 2.1 评分系统

标准四级评分：

| 分值 | 标签 | 含义 | 图示约定 |
|-------|-------|---------|-------------------|
| 4 | 必须 | 必须直接邻接（共用墙/门） | 红色粗实线 |
| 3 | 期望 | 应靠近（同一分区、短距离步行） | 橙色中等实线 |
| 2 | 中性 | 对邻近性没有明显偏好 | 不画线 |
| 1 | 不宜 | 应分隔（噪声、安防、不相容） | 蓝色虚线 |
| 0 | 禁止 | 任何情况下均不得邻接 | 红色双虚线 |

部分从业者使用六级或加权系统。为保证简洁和可靠性，推荐使用四级系统。

### 2.2 Matrix Construction Process

**步骤 1：**在两个轴向列出所有部门或主要空间组。建筑级矩阵采用 8–20 个组；大型建筑建立嵌套矩阵（先建筑级，再部门级）。

**步骤 2：**系统处理每一对关系，依据第 1.3 节标准评分。应邀请相关方参与，建筑师不应单独评分。

**步骤 3：**逐行阅读并验证：“部门 X 与 A 必须相邻，与 B、C 宜相邻，与 D 中性，与 E 不宜相邻。”检查其是否符合运营逻辑。

**步骤 4：**识别集群：具有相互 4 分关系的部门群组形成自然分区。

**步骤 5：**识别冲突：某一对空间彼此得分为 1，但同时与第三个空间均为 4 分时，会形成设计挑战。

### 2.3 Weighted Proximity Matrix

对于复杂项目，应按重要性对评分加权：

| 因素 | 权重 |
|--------|--------|
| 患者/用户安全 | 5 |
| 运营效率 | 4 |
| 共享资源 | 3 |
| 员工便利性 | 2 |
| 环境质量 | 3 |
| 安全防护 | 4 |

加权得分 = 各因素（得分 × 权重）之和。这样可形成连续尺度而非 4 级离散尺度，适合优化算法。

---

## 3. 泡泡图分析

### 3.1 目的

泡泡图将抽象矩阵转化为二维空间布置，是从数据走向几何形态的第一步。

### 3.2 构建方法

1. **将每个部门绘制为圆形**，按相对面积缩放（非精确比例，仅作示意）
2. **将 4 分关系对相互接触**或重叠
3. **将 3 分关系对置于邻近位置**并以连线连接
4. **将 2 分关系对保持无连线**并留出中等距离
5. **将 1 分关系对远距离布置**，用虚线表示所需分隔
6. **反复迭代**，直至满足全部关系或识别出冲突
7. **叠加到场地上**，检验朝向、通行和体量影响

### 3.3 规则与约定

- Circles represent departments or space groups, not individual rooms
- Circle area is proportional to department floor area
- Solid thick lines = essential adjacency (score 4)
- Solid thin lines = desirable adjacency (score 3)
- Dashed lines = required separation (score 1)
- Arrows indicate one-way flow relationships
- Hatched overlap = shared space (e.g., shared waiting area)
- External connections shown as lines to site edge (main entrance, service entrance, car park)

### 3.4 常见模式

**Hub-and-Spoke:** One central department (e.g., reception, nurse station) connects to multiple surrounding departments. Common in hospitals, schools, hotels.

**Linear Sequence:** Departments arranged in a sequential flow. Common in manufacturing, food production (raw materials > prep > cooking > serving > dining).

**Cluster:** Groups of departments with strong internal adjacency but weaker connection to other clusters. Common in universities (science cluster, humanities cluster) and mixed-use buildings.

**Ring:** Departments arranged around a central space (courtyard, atrium). All departments have equal access to the centre. Common in courtyard buildings, some museums.

**Tree/Branching:** Main circulation spine with departments branching off. Common in finger-plan hospitals, long school buildings.

---

## 4. 堆叠分析

### 4.1 目的

堆叠图将水平泡泡图转化为垂直剖面，把各部门分配到不同楼层。堆叠受以下因素驱动：
- Ground-floor access requirements (public entry, loading, emergency)
- Vertical adjacency needs (surgery above ED, wards above surgery)
- Structural logic (heavy loads at lower floors)
- Services distribution (plant at basement/roof, risers through building)
- Views and daylight (premium uses at upper floors)
- Fire and egress (vulnerable populations at lower floors)

### 4.2 堆叠优先级

| 优先级 | 标准 | 示例 |
|---------------|-----------|---------|
| 1（强制） | 必须位于首层 | 主入口、零售、急诊部、装卸平台 |
| 2（高优先） | 应位于首层或二层 | 接待、公共设施、餐饮服务、无障碍设施 |
| 3（优先） | 位于低层更有利 | 重型设备、高人流部门 |
| 4（灵活） | 无明显楼层偏好 | 办公空间、教室、酒店客房 |
| 5（优先高层） | 位于高层更有利 | 行政办公、顶层公寓、观景空间、餐厅 |
| 6（地下室） | 适合地下设置 | 停车、设备机房、储藏、档案室 |

### 4.3 堆叠图格式

堆叠图是简化的建筑剖面，显示：
- Each floor as a horizontal band
- Departments as coloured blocks within each floor band, scaled to area
- Core (lifts/stairs) shown as a vertical strip connecting all floors
- External connections (entrances, loading) shown at grade
- Arrows indicating key vertical movement (e.g., patients from ED to surgery)

### 4.4 堆叠约束

| 约束 | 影响 |
|-----------|--------|
| 结构转换 | 改变楼层间柱网成本高；应对齐主要结构 |
| 设备立管 | 湿区应垂直堆叠（卫生间上下对齐、实验室上下对齐） |
| 层高 | 不同用途需要不同层高（零售 4.5 m、办公 3.9 m、住宅 3.0 m） |
| 防火分隔 | 不同用途之间需设置耐火楼板（如商业上方住宅） |
| 隔声分隔 | 上方健身房、设备机房等产生的撞击声必须与敏感用途分隔 |
| 装卸/服务 | 首层设置后勤通道，上层设置服务电梯 |
| 分期 | 建筑分期实施时，每期均应功能完整 |

---

## 5. Program Testing

### 5.1 Fit-on-Floor Testing

Once stacking is determined, test whether each floor's assigned departments actually fit on the floor plate:

1. **Calculate floor plate NIA** = GIA - core - structure - risers
2. **Sum departmental areas** assigned to that floor
3. **Add intra-floor circulation** (10-15% for simple layouts, 15-25% for complex)
4. **Compare NIA available vs. NIA required**
5. **Check floor plate depth** for daylight compliance (max 12-15m from window for office/residential)

### 5.2 Circulation Testing

Test whether the building's circulation system supports the adjacency requirements:

| 测试 | 方法 | 通过标准 |
|------|--------|--------------|
| 疏散距离 | 测量每对 4 分关系空间质心之间的距离 | 关键相邻关系小于 30 m |
| 走廊宽度 | 检查部门间高峰流量 | 一般最小 1.5 m，医院病床走廊 2.4 m |
| 导向复杂度 | 统计从入口到各部门的决策点 | 公共区域少于 3 个转弯 |
| 疏散 | 检查至最近出口的距离 | 按消防规范（IBC：设置喷淋 75 m，无喷淋 60 m） |
| 无障碍 | 检查所有公共路线是否无台阶 | 所有公共区域 100% 无台阶到达 |

### 5.3 Conflict Resolution

当相邻关系要求发生冲突（复杂建筑中较为常见）时：

1. **Identify the conflict:** Space A needs to be adjacent to both B and C, but B and C must be separated.
2. **Evaluate priorities:** Which adjacency is more critical? Use weighted scores.
3. **Design solutions:**
   - Intermediate buffer space between B and C
   - Vertical adjacency (A on floor between B and C)
   - Dedicated connecting corridor from A to the less-critical partner
   - Duplicate a function (e.g., satellite imaging suite near both ED and outpatient)
4. **Document the resolution** and the compromise accepted.

---

## 6. Worked Examples

### 6.1 Hospital (150-Bed District General)

**Departments:** Emergency (ED), Diagnostic Imaging, Operating Theatres, Inpatient Wards, Outpatient Clinics, Maternity, Pathology Lab, Administration, Facilities/Plant

**Adjacency Matrix:**

|  | ED | Imaging | Surgery | Wards | OPD | Maternity | Path Lab | Admin | Facilities |
|--|---:|--------:|--------:|------:|----:|---------:|---------:|------:|-----------:|
| 急诊（ED） | -- | 4 | 4 | 3 | 2 | 2 | 3 | 1 | 1 |
| 影像 | -- | -- | 3 | 2 | 4 | 2 | 2 | 1 | 1 |
| 手术部 | -- | -- | -- | 4 | 2 | 3 | 3 | 1 | 1 |
| 病房 | -- | -- | -- | -- | 2 | 3 | 2 | 2 | 2 |
| 门诊（OPD） | -- | -- | -- | -- | -- | 2 | 2 | 2 | 1 |
| 妇产科 | -- | -- | -- | -- | -- | -- | 2 | 1 | 1 |
| 病理实验室 | -- | -- | -- | -- | -- | -- | -- | 1 | 2 |
| 行政 | -- | -- | -- | -- | -- | -- | -- | -- | 2 |
| 设施管理 | -- | -- | -- | -- | -- | -- | -- | -- | -- |

**Stacking Solution:**
- **地下室：**机房/设施、病理实验室（气动管道连接各层）、停车场
- **首层：**急诊科（救护车通行）、影像科（邻近急诊）、主入口、门诊部（公众入口）、产科（可设置独立入口）
- **二层：**手术部（位于急诊上方，便于垂直转运）、日间手术、CSSD
- **三层：**住院病区（位于手术部上方，便于术后转运）
- **四层：**产科病区（若未设于首层）、其他住院病区
- **屋面层：**停机坪（如有需要）、其他设备

**Key Design Moves:**
- ED and Imaging share a dedicated CT scanner at their interface
- Pneumatic tube system connects Pathology Lab to ED, Surgery, and Wards
- Dedicated patient lift connects ED (ground) to Surgery (first) to Wards (second)
- Public circulation (outpatients, visitors) separated from clinical circulation (staff, patients in beds)

### 6.2 Secondary School (1200 Pupils, 8 Form Entry)

**Departments:** Administration, Science, Humanities, Creative Arts, Technology, Sports, Library/Media, Dining, Sixth Form

**Adjacency Matrix:**

|  | Admin | Science | Human. | Creative | Tech | Sports | Library | Dining | 6th Form |
|--|------:|--------:|-------:|---------:|-----:|-------:|--------:|-------:|---------:|
| 行政 | -- | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 理科 | -- | -- | 2 | 2 | 3 | 1 | 3 | 2 | 3 |
| 人文 | -- | -- | -- | 2 | 2 | 1 | 4 | 2 | 3 |
| 创意 | -- | -- | -- | -- | 3 | 1 | 2 | 2 | 2 |
| 技术 | -- | -- | -- | -- | -- | 1 | 2 | 2 | 2 |
| 体育 | -- | -- | -- | -- | -- | -- | 1 | 3 | 2 |
| 图书馆 | -- | -- | -- | -- | -- | -- | -- | 2 | 4 |
| 餐饮 | -- | -- | -- | -- | -- | -- | -- | -- | 2 |
| 6th Form | -- | -- | -- | -- | -- | -- | -- | -- | -- |

**Key Adjacency Logic:**
- Admin must front the main entrance for safeguarding (visitors sign in at reception) -- score 4 to entrance, implicit
- Science and Technology share services (gas, water, extraction) -- score 3
- Sports separated from all teaching departments -- noise, vibration (score 1)
- Library central to Humanities and Sixth Form -- study resource (score 4)
- Dining adjacent to Sports for hall dual-use potential and kitchen servicing (score 3)
- Creative Arts and Technology share making/messy activities -- adjacency supports shared workshops (score 3)

**Stacking Solution (3-storey):**
- **首层：**主入口+行政、餐厅+厨房、体育馆（独立建筑或翼楼）、技术教室（重型设备、首层、服务入口）
- **二层：**科学教室（管线可从首层上升）、创意艺术、部分人文学科
- **三层：**其余人文学科、图书馆/媒体中心、六年级中心

### 6.3 Office Building (15,000 m2 GIA, Multi-Tenant Speculative)

**Departments (generic for spec office):** Reception/Lobby, Retail (ground floor), Office Floors (multi-tenant), Building Management, Car Park, Cycle/End-of-Trip, Plant

**Adjacency Matrix:**

|  | Reception | Retail | Office | Bldg Mgmt | Car Park | Cycle/EoT | Plant |
|--|----------:|-------:|-------:|----------:|---------:|----------:|------:|
| Reception | -- | 3 | 4 | 2 | 2 | 3 | 1 |
| Retail | -- | -- | 1 | 1 | 2 | 2 | 1 |
| Office | -- | -- | -- | 2 | 2 | 3 | 1 |
| Bldg Mgmt | -- | -- | -- | -- | 3 | 2 | 4 |
| Car Park | -- | -- | -- | -- | -- | 3 | 2 |
| Cycle/EoT | -- | -- | -- | -- | -- | -- | 1 |
| Plant | -- | -- | -- | -- | -- | -- | -- |

**Stacking Solution:**
- **地下二层：**停车场、主机房
- **地下一层：**停车场、自行车停车、到达终点设施（淋浴/储物柜）、楼宇管理办公室（靠近机房）
- **首层：**接待/大厅（通高）、零售单元（沿街）、办公入口与零售分开
- **二至十一层：**投机型办公楼层，每层NIA 1200-1500 m²
- **屋面：**次级设备（冷却塔、AHU）、可设置屋顶露台

**Key Design Moves:**
- Separate lobby cores for office (secure lift access) and retail (direct street entry)
- End-of-trip facilities adjacent to cycle parking with direct lift access to office floors
- Retail servicing from basement loading dock, separate from office servicing
- Building management with direct access to both basement plant and roof plant via service lift

### 6.4 Mixed-Use Development (Podium + Tower)

**Components:** Retail (ground/first), Office (podium floors 2-5), Residential (tower floors 6-25), Car Park (basement), Shared Amenity

**Adjacency Matrix:**

|  | Retail | Office | Residential | Car Park | Amenity |
|--|-------:|-------:|------------:|---------:|--------:|
| Retail | -- | 2 | 1 | 2 | 2 |
| Office | -- | -- | 1 | 3 | 2 |
| Residential | -- | -- | -- | 3 | 4 |
| Car Park | -- | -- | -- | -- | 1 |
| Amenity | -- | -- | -- | -- | -- |

**Key Separation Requirements:**
- Residential entrance MUST be separate from office and retail entrances (score 1 between lobbies)
- Fire separation: 2-hour fire-rated floor between different use classes
- Acoustic separation: residential above office requires impact isolation (floating floor, 50dB min)
- Structural transfer: office column grid (9m x 9m) differs from residential (6m x 7.5m) -- transfer structure at level 5/6 interface
- Services: separate risers for each use; residential services cannot pass through office floors without fire-rated enclosure
- Waste: separate refuse collection for residential and commercial

**Stacking Solution:**
- **地下一至二层：**停车场（按用途分配：住宅许可、办公日常、零售顾客）、自行车、机房
- **首层：**零售单元（沿街）、住宅大厅（独立入口）、办公大厅（独立入口）、装卸区（共用、按时间管理）
- **二层：**零售夹层或追加零售、共享配套（健身房、联合办公）
- **三至六层：**办公裙房（较大楼板，每层1500-2000 m²）
- **七层（转换层）：**住宅配套平台（泳池、露台、休息厅），同时容纳结构转换
- **八至二十六层：**住宅塔楼（较小楼板600-800 m²，每层6-8户）
- **屋面：**住宅屋顶露台、光伏阵列、次级设备

---

## 7. 相邻关系分析数字工具

### 7.1 软件选项

| 工具 | 应用 | 相邻关系功能 |
|------|------------|-------------------|
| Microsoft Excel / Google Sheets | 矩阵构建 | 半矩阵模板，按评分条件格式化 |
| dRofus | 房间任务书编制 | 内置相邻关系矩阵，可连接 BIM |
| Trelligence Affinity | 空间任务书编制 | 根据矩阵输入自动生成泡泡图 |
| Revit（配合Dynamo） | BIM集成任务书 | 使用自定义脚本测试模型中的相邻关系 |
| Grasshopper（Rhino） | 参数化任务书 | 空间装箱算法、相邻关系优化 |
| ARCHIBUS / FM:Systems | 设施管理 | 既有建筑相邻关系分析、搬迁规划 |
| SpaceS（定制工具） | 相邻关系优化 | 基于遗传算法的空间布局 |

### 7.2 Computational Adjacency Optimization

对于大型或复杂任务书，可使用计算方法优化空间布置：

1. **Graph-Based:** Represent departments as nodes and adjacency scores as edge weights. Use force-directed graph layout to find optimal 2D arrangement.
2. **Genetic Algorithm:** Encode floor assignments as chromosomes. Fitness function = sum of (adjacency score x 1/distance) for all pairs. Evolve toward optimal stacking.
3. **Simulated Annealing:** Start with random arrangement, iteratively swap departments, accept swaps that improve adjacency satisfaction (and occasionally worse swaps to escape local optima).
4. **Multi-Objective Optimization:** Balance adjacency satisfaction against other objectives (structural efficiency, daylight, views, cost) using Pareto front analysis.

---

## 8. Quality Assurance Checklist

Before finalizing adjacency analysis, verify:

- [ ] All departments included in the matrix (no orphans)
- [ ] Stakeholders validated scores (not architect assumptions alone)
- [ ] Score-4 relationships are achievable on the proposed floor plate
- [ ] No unresolved score-1 conflicts with mutual score-4 partners
- [ ] Ground-floor access requirements satisfied
- [ ] Vertical adjacencies accommodated in stacking diagram
- [ ] Service connections (wet walls, risers) aligned vertically
- [ ] Public vs. private circulation separated
- [ ] Fire compartmentation does not sever score-4 relationships
- [ ] Accessibility route connects all public departments
- [ ] Loading and servicing access does not conflict with public entrance
- [ ] Matrix updated if program changes during design

---

## References

- Pena, W. & Parshall, S. (2012). *Problem Seeking*. 5th ed. Wiley.
- Palmer, M.A. (1981). *The Architect's Guide to Facility Programming*. AIA / McGraw-Hill.
- Hershberger, R. (1999). *Architectural Programming and Predesign Manager*. McGraw-Hill.
- Duerk, D. (1993). *Architectural Programming: Information Management for Design*. Wiley.
- NHS Estates. *Health Building Notes* (HBN) Series. UK Department of Health.
- DfE (2014). *Building Bulletin 103*. UK Department for Education.
- BCO (2019). *BCO Guide to Specification*. British Council for Offices.
- Neufert, E. & Neufert, P. (2019). *Neufert Architects' Data*. 5th ed. Wiley-Blackwell.
#

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab AI建筑与室内设计总设计师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
