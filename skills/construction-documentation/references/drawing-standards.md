---
name: drawing-standards
description: 注册建筑师专业参考：drawing-standards。
license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---

# 制图标准参考

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab AI建筑与室内设计总设计师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。

本参考综合介绍建筑制图标准，涵盖 CAD 图层约定、BIM 标准、图纸尺寸、标题栏、修订管理、发布状态代码、批注约定和协调检查。

---

## 1. AIA CAD 图层指南

### 1.1 图层命名约定

AIA CAD 图层指南（基于美国国家 CAD 标准）采用结构化命名格式：

```
专业 - 主组 - 次组（可选）- 状态（可选）
```

**格式：**`A-WALL-FULL-N`，其中：
- `A` = 专业标识
- `WALL` = 主组（4 个字符）
- `FULL` = 次组（4 个字符，可选）
- `N` = 状态代码（可选）

### 1.2 专业标识

| 代码 | 专业 |
|------|--------------------------|
| A | 建筑 |
| C | 土木 |
| E | 电气 |
| F | 消防 |
| G | 通用 |
| H | 危险材料 |
| I | 室内 |
| L | 景观 |
| M | 机械 |
| O | 运营 |
| P | 给排水 |
| Q | 设备 |
| R | 资源 |
| S | 结构 |
| T | 电信 |
| X | 其他专业 |
| Z | 承包商/加工图 |

### 1.3 建筑标准图层

| 图层名称 | 描述 | 颜色 | 线宽 |
|-------------------|------------------------------------------|-------|-------------|
| A-WALL            | 墙体——一般                         | 4     | 0.50mm      |
| A-WALL-FULL       | 全高墙体                        | 4     | 0.50mm      |
| A-WALL-PRHT       | 半高墙体                     | 4     | 0.35mm      |
| A-WALL-PATT       | 墙体填充/图案                   | 8     | 0.13mm      |
| A-DOOR            | 门                                    | 3     | 0.35mm      |
| A-DOOR-IDEN       | 门识别编号                 | 7     | 0.25mm      |
| A-GLAZ            | 窗及玻璃                   | 3     | 0.35mm      |
| A-GLAZ-IDEN       | 窗识别编号               | 7     | 0.25mm      |
| A-FLOR            | 楼面信息                        | 3     | 0.25mm      |
| A-FLOR-PATT       | 楼面图案/饰面                  | 8     | 0.13mm      |
| A-CLNG            | 吊顶信息                      | 5     | 0.25mm      |
| A-CLNG-GRID       | 吊顶网格                             | 8     | 0.13mm      |
| A-ROOF            | 屋面轮廓                             | 4     | 0.35mm      |
| A-ROOF-PATT       | 屋面填充                            | 8     | 0.13mm      |
| A-COLS            | 柱                                  | 5     | 0.50mm      |
| A-STRS            | 楼梯                                   | 3     | 0.35mm      |
| A-ELEV            | 电梯                                | 3     | 0.35mm      |
| A-FURN            | 家具                                | 8     | 0.18mm      |
| A-EQPM            | 设备                                | 8     | 0.18mm      |
| A-ANNO-DIMS       | 尺寸                               | 1     | 0.18mm      |
| A-ANNO-TEXT       | 文字注释                         | 7     | 0.18mm      |
| A-ANNO-NOTE       | 一般说明                            | 7     | 0.18mm      |
| A-ANNO-SYMB       | 符号（剖面标记、编号）            | 7     | 0.25mm      |
| A-ANNO-TTLB       | 标题栏                              | 7     | 0.35mm      |
| A-AREA-IDEN       | 面积识别                      | 2     | 0.18mm      |
| A-DETL            | 详图构件                        | 4     | 0.35mm      |
| A-GRID            | 柱网轴线                        | 8     | 0.13mm      |
| A-GRID-IDEN       | 轴网识别气泡              | 7     | 0.25mm      |

### 1.4 状态代码

| 代码 | 含义 |
|------|----------------------------------------|
| D | 拆除（现有且将移除） |
| E | 保留现状 |
| F | 未来工程（不在当前合同内） |
| M | 待移动项目 |
| N | 新建工程 |
| T | 临时工程 |

---

## 2. BIM 标准

### 2.1 BS 1192 / ISO 19650

BS 1192（已由 ISO 19650 取代）建立了使用 BIM 管理建成资产全生命周期信息的框架。

**关键原则：**
- 所有项目信息使用统一数据环境（CDE）
- 文件、模型和文档采用统一命名约定
- 信息容器按专业、区域和阶段组织
- 通过状态和适用性代码控制信息使用

### 2.2 ISO 19650 信息管理框架

| 部分 | 范围 |
|----------|----------------------------------------------|
| 19650-1 | 概念与原则 |
| 19650-2 | 资产交付阶段 |
| 19650-3 | 资产运营阶段 |
| 19650-5 | 注重安全的信息管理方法 |

**统一数据环境（CDE）状态：**

| 状态 | 代码 | 描述 |
|----------------|------|------------------------------------------|
| 工作进行中 | WIP | 团队内部开发 |
| 共享 | S1 | 适合协调 |
| 共享 | S2 | 适合信息使用 |
| 共享 | S3 | 适合审查和评论 |
| 共享 | S4 | 适合阶段审批 |
| 已发布 | A1 | 已授权施工（BEP 阶段） |
| 已发布 | A2 | 已授权施工 |
| 已发布 | AB | 竣工图 |
| 归档 | -- | 已归档/已取代 |

### 2.3 BIM 文件命名约定（ISO 19650）

```
Project - Originator - Zone - Level - Type - Role - Classification - Number
```

Example: `PROJ-ARC-ZZ-01-DR-A-20-0001`
- PROJ = 项目代码
- ARC = 创建者（建筑事务所代码）
- ZZ = 适用于所有区域
- 01 = 01 层
- DR = 图纸
- A = 建筑
- 20 = 按分类划分的章节编号
- 0001 = 顺序号

### 2.4 模型协调流程

1. **联合模型组装：**每周合并各专业模型
2. **碰撞检测：**运行自动碰撞报告（Navisworks、Solibri）
3. **碰撞解决会议：**按优先级审查碰撞（关键、重大、一般）
4. **模型审计：**检查是否符合 BIM 执行计划（BEP）
5. **LOD 验证：**确认构件达到各阶段要求的 LOD
6. **设计冻结：**锁定已协调的模型构件

---

## 3. 图纸尺寸标准

### 3.1 ISO 标准图纸尺寸（公制）

| 代号 | 宽度（mm） | 高度（mm） | 面积（m²） |
|-------------|-----------|-------------|------------|
| A4          | 210       | 297         | 0.0624     |
| A3          | 297       | 420         | 0.1247     |
| A2          | 420       | 594         | 0.2494     |
| A1          | 594       | 841         | 0.4996     |
| A0          | 841       | 1189        | 0.9999     |

### 3.2 ANSI/ARCH 标准图纸尺寸（英制）

| Designation | Width (in) | Height (in) | Metric Approx    |
|-------------|-----------|-------------|------------------|
| ANSI A      | 8.5       | 11          | 216 x 279mm      |
| ANSI B      | 11        | 17          | 279 x 432mm      |
| ANSI C      | 17        | 22          | 432 x 559mm      |
| ANSI D      | 22        | 34          | 559 x 864mm      |
| ANSI E      | 34        | 44          | 864 x 1118mm     |
| ARCH A      | 9         | 12          | 229 x 305mm      |
| ARCH B      | 12        | 18          | 305 x 457mm      |
| ARCH C      | 18        | 24          | 457 x 610mm      |
| ARCH D      | 24        | 36          | 610 x 914mm      |
| ARCH E      | 36        | 48          | 914 x 1219mm     |
| ARCH E1     | 30        | 42          | 762 x 1067mm     |

### 3.3 各地区常用做法

- **北美：**施工图集最常用 ARCH D（24"x36"）；大型项目使用 ARCH E（36"x48"）；半幅打印使用 ARCH B（12"x18"）
- **欧洲/亚洲：**施工最常用 A1（594x841mm）；大型项目使用 A0；现场副本使用 A3
- **中东：**根据项目来源混用 A1 和 ARCH D

---

## 4. 标题栏内容

### 4.1 必要信息

每张图纸必须包含标题栏，内容包括：

**项目信息：**
- 项目名称
- 项目地址/位置
- 项目编号
- 业主名称和联系方式
- 建筑许可编号（签发后）
- 分区/规划参考编号

**事务所信息：**
- 建筑事务所名称和标志
- 事务所地址和联系方式
- 负责建筑师执照编号和印章
- 事务所注册编号

**图纸信息：**
- 图纸编号（按编号约定）
- 图纸标题
- 图纸比例（图示比例和数字比例）
- 发布日期
- 绘图人（姓名首字母）
- 校核人（姓名首字母）
- 批准人（姓名首字母）

**修订信息：**
- 修订编号
- 修订日期
- 修订说明
- 修订标记（带编号的三角形或 Delta 符号）

**顾问信息（如适用）：**
- 结构工程师
- 机械工程师
- 电气工程师
- 土木工程师
- 其他专业顾问

### 4.2 Title Block Layout

标准标题栏位于图纸右侧或右下角。典型尺寸：

- **右侧条带：**宽 75 mm × 图纸全高（ISO 标准）
- **右下角区块：**宽 180 mm × 高 60 mm（常用替代方案）
- 修订表：位于主标题栏上方或旁侧
- 发布表：位于主标题栏信息下方

---

## 5. 修订管理

### 5.1 修订编号

- 修订按顺序编号：Rev 1、Rev 2、Rev 3（或 Rev A、B、C）
- 在部分实践中，每个新的发布里程碑（设计阶段）修订编号重新从 1 开始，另一些实践则连续编号
- 每次修订必须包含：编号、日期、说明和云线标记

### 5.2 修订云线

- 修订区域用修订云线圈定（不规则曲线边界）
- 云线旁标注带修订编号的 Delta 符号
- 发布新修订时通常移除旧修订云线（只显示当前修订云线）
- 在 BIM 环境中，修订云线由 Revit 或同类软件编排和跟踪

### 5.3 修订表格式

| 修订 | 日期 | 说明 | 编制 |
|-----|------------|---------------------------|-----|
| 3 | 2025-12-01 | 更新窗表 | JD |
| 2 | 2025-10-15 | 修订楼梯布局 | MK |
| 1 | 2025-08-20 | 业主审查意见 | JD |

最新修订列在最上方。表格通常显示最近 5-6 次修订；更早修订注明“见此前发布版”。

---

## 6. 发布状态代码

### 6.1 标准发布阶段

| 代码 | 状态 | 描述 |
|------|---------------------------|--------------------------------------------|
| P | 初步 | 进行中，不供外部使用 |
| FR | 供审查 | 发布供审查和评论 |
| FA | 供批准 | 发布供业主/主管机构批准 |
| FC | 供施工 | 发布供施工（合同文件） |
| FT | 供招标/报价 | 发布供承包商报价 |
| FI | 供参考 | 仅供参考 |
| FC-R | 供施工（修订） | 施工期间修订 |
| AB | 竣工 | 更新以反映建成条件 |
| RD | 记录文件 | 建成工程最终记录 |

### 6.2 发布管理

- 每次发布均有唯一标识符（发布日期或发布编号）
- 每次发布均附发送函，列出所含全部图纸
- 被取代图纸必须明确标记，或从现场图纸集中移除
- 通过项目门户（Aconex、PlanGrid 等）进行数字化发布管理
  BIM 360, Procore) tracks receipt and acknowledgment

---

## 7. 云线批注约定

### 7.1 Types of Markups

- **修订云线：**表示不同发布版本之间的变更
- **审查意见：**用于内部协调的初步批注
- **RFI引用：**云线链接至已纳入的RFI回复
- **ASI引用：**标注建筑师补充指令
- **范围变更标记：**标识与变更令相关的修改

### 7.2 颜色编码（数字审查）

| 颜色   | 含义                          |
|---------|----------------------------------|
| 红色     | 关键问题，必须处理     |
| 橙色  | 重要意见，需要复核 |
| 黄色  | 次要意见或建议      |
| 绿色   | 已批准或已接受             |
| 蓝色    | 仅供信息                 |
| 紫色  | 顾问协调事项     |

### 7.3 批注流程

1. Author creates drawing and publishes to CDE as "Work in Progress"
2. Reviewer opens drawing and adds markup comments
3. Author addresses comments and updates drawing
4. Reviewer verifies changes and approves
5. Drawing moves to "Shared" status for coordination
6. After coordination, drawing moves to "Published" for construction

---

## 8. 图纸协调检查

### 8.1 内部协调（建筑）

Before any issue, verify:
- Room numbers consistent across plans, RCPs, finish schedules
- Door tags match between plans and door schedule
- Window tags match between plans, elevations, and window schedule
- Section and detail references resolve to correct sheet and detail
- Elevation markers reference correct sheets
- Column grid labels consistent across all sheets
- Dimensions sum correctly (detail dims = overall dims)
- Floor-to-floor heights match between sections and plans
- Ceiling heights consistent between RCPs and sections
- Stair risers and treads comply with code and match floor heights
- Material indications consistent between plans, sections, and details

### 8.2 跨专业协调

Verify against consultant drawings:
- **结构：**柱梁位置与建筑图一致；
  slab edges, openings, and depressions coordinated; structural depths
  match architectural sections
- **机械：**风管路线适配吊顶夹层；设备
  locations have required clearances; louver sizes match architectural
  elevations
- **电气：**配电盘位置与建筑图一致；灯具
  layout matches RCP; outlet heights per architectural interior elevations
- **给排水：**洁具位置与建筑图一致；地漏
  at correct locations; pipe chases sized adequately
- **消防：**喷淋头与天花布置协调；
  fire-rated walls continuous through all drawings; smoke/fire dampers
  at rated wall penetrations
- **土建：**建筑轮廓与总平面一致；完成地坪标高
  matches grading plan; utility connections coordinated

### 8.3 自动化协调工具

- **Navisworks Manage：**联合模型碰撞检测
- **Solibri Model Checker：**基于规则的模型检查
- **BIMcollab：**基于云的BCF问题管理
- **Revit干涉检查：**Revit内置碰撞检测
- **Bluebeam Revu：**用于二维协调的PDF叠图比较
- **AutoCAD DWG Compare：**自动图纸比较工具

### 8.4 按阶段划分的协调检查清单

**方案设计阶段发布：**
- Building footprint and overall dimensions verified
- Floor-to-floor heights confirmed with structural and MEP
- Major vertical penetrations (stairs, elevators, shafts) located
- Preliminary code compliance verified

**设计深化阶段发布：**
- All rooms numbered and named
- All doors and windows tagged
- Structural grid finalized and coordinated
- MEP space requirements confirmed
- Ceiling heights established and verified
- Wall types assigned and rated walls identified

**施工图文件阶段发布：**
- All annotation complete (dimensions, keynotes, tags)
- All schedules complete and cross-referenced
- All details drawn and referenced
- All specification sections written and cross-referenced
- Clash detection run and issues resolved
- 规范合规性已完整记录
- Accessibility compliance verified
- QA/QC review by senior architect completed
#

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab AI建筑与室内设计总设计师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
