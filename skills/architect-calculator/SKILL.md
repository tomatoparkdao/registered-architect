license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
name: architect-calculator
description: >
  七个基于 Python 的建筑设计计算器，用于常见设计计算：面积与开发强度计算
  （GFA、NGA、户数、人口、停车位）；多层构造传热系数（U 值）分析；采用
  BRE 方法的采光系数估算；疏散合规性校核（使用人数、出口宽度、疏散距离）；
  结构竖向荷载与柱分担面积计算；基于度日法的年度能耗估算；以及按建筑类型、
  品质和地区估算建造成本。
license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
# 建筑师计算器

这是一套用于快速建筑设计计算的七个命令行 Python 计算器。每个计算器均通过
命令行参数接收输入、校验输入内容，并输出便于阅读的结果或结构化 JSON。

所有脚本均位于 `scripts/` 目录中，可按以下方式运行：

```
python scripts/<calculator_name>.py [arguments]
```

在任意命令中添加 `--json`，即可获得适用于传递给其他工具或自动化流程的结构化
JSON 输出。

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 1. 面积计算器（`area_calculator.py`）

根据用地面积和容积率（FAR）计算开发强度指标，包括总建筑面积、净可用面积、
住宅户数、估算人口和停车位需求。

### 参数

| 参数               | 标志               | 默认值  | 单位   | 说明                                 |
|--------------------|--------------------|---------|--------|--------------------------------------|
| 用地面积           | `--site-area`      | 必填    | m2     | 用地/地块总面积                      |
| 容积率             | `--far`            | 必填    | 比值   | 允许的 FAR / 容积率                  |
| 净总面积比         | `--ntg-ratio`      | 0.80    | 比值   | NGA 占 GFA 的比例（0.0-1.0）         |
| 平均户型面积       | `--avg-unit-size`  | 85      | m2     | 住宅单元平均面积                      |
| 每户人数           | `--persons-per-unit`| 2.5    | 人    | 平均家庭规模                          |
| 停车配比           | `--parking-ratio`  | 1.0     | 车位  | 每个住宅单元对应的停车位数            |

### 示例

```bash
python scripts/area_calculator.py --site-area 5000 --far 2.5 --ntg-ratio 0.82
```

### 示例输出

```
=== 面积与开发强度计算器 ===
用地面积：            5,000.00 m2
容积率：              2.50
---------------------------------------
总建筑面积：          12,500.00 m2
净总面积比：          0.82
净建筑面积：          10,250.00 m2
---------------------------------------
平均户型面积：        85.00 m2
估算户数：            120
每户人数：            2.50
估算人口：            300
---------------------------------------
停车配比：            1.00 车位/户
停车位数：            120
```

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 2. 传热系数（U 值）计算器（`uvalue_calculator.py`）

通过汇总各构造层热阻及表面热阻，计算多层墙体、屋面或楼板构造的传热系数（U 值）。

### 参数

| 参数            | 标志              | 默认值  | 单位        | 说明                            |
|----------------|-------------------|---------|-------------|---------------------------------|
| 构造层          | `--layers`        | 必填    | JSON 字符串 | 构造层对象数组                  |
| 内表面 Rsi      | `--rsi-internal`  | 0.13    | m2K/W       | 内表面热阻                      |
| 外表面 Rsi      | `--rsi-external`  | 0.04    | m2K/W       | 外表面热阻                      |

每个构造层对象：`{"name": "...", "thickness_mm": N, "conductivity": N}`

### 示例

```bash
python scripts/uvalue_calculator.py --layers '[
  {"name": "砖墙", "thickness_mm": 102, "conductivity": 0.77},
  {"name": "空气夹层", "thickness_mm": 50, "conductivity": 0.18},
  {"name": "矿棉", "thickness_mm": 100, "conductivity": 0.035},
  {"name": "混凝土砌块", "thickness_mm": 140, "conductivity": 1.13},
  {"name": "抹灰层", "thickness_mm": 13, "conductivity": 0.16}
]'
```

### 示例输出

```
=== 传热系数（U 值）计算器 ===
构造层               厚度(mm)       导热系数(W/mK)      R 值(m2K/W)
---------------------------------------------------------------------------
Rsi（内表面）        --             --                   0.1300
砖墙                 102            0.770                0.1325
空气夹层             50             0.180                0.2778
矿棉                 100            0.035                2.8571
混凝土砌块           140            1.130                0.1239
抹灰层               13             0.160                0.0813
Rse（外表面）        --             --                   0.0400
---------------------------------------------------------------------------
总热阻 R 值：        3.6425 m2K/W
传热系数 U 值：      0.2745 W/m2K

被动房目标（墙体）：          0.15 W/m2K  —— 不符合
常见规范目标（墙体）：        0.30 W/m2K  —— 符合
```

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 3. 采光计算器（`daylight_calculator.py`）

使用 BRE 简化公式估算侧向采光房间的平均采光系数。

### 参数

| 参数                  | 标志                      | 默认值  | 单位  |
|----------------------|---------------------------|---------|-------|
| 房间宽度              | `--room-width`            | 必填    | m     |
| 房间进深              | `--room-depth`            | 必填    | m     |
| 房间高度              | `--room-height`           | 必填    | m     |
| 窗宽                  | `--window-width`          | 必填    | m     |
| 窗高                  | `--window-height`         | 必填    | m     |
| 窗台高度              | `--window-sill-height`    | 必填    | m     |
| 玻璃透光率            | `--glazing-transmittance` | 0.65    | 比值  |
| 平均反射比            | `--average-reflectance`   | 0.50    | 比值  |

### 示例

```bash
python scripts/daylight_calculator.py \
  --room-width 4.0 --room-depth 6.0 --room-height 3.0 \
  --window-width 2.5 --window-height 1.8 --window-sill-height 0.9
```

### 示例输出

```
=== 采光系数计算器 ===
房间：     宽 4.00m × 进深 6.00m × 高 3.00m
窗：       宽 2.50m × 高 1.80m（窗台高 0.90m）
---------------------------------------
窗面积：                 4.50 m2
房间总表面积：           96.00 m2
窗地比：                 18.75%
玻璃透光率：             0.65
平均反射比：             0.50
可见天空角：             60.1°
---------------------------------------
平均采光系数：           2.34%

评价：合格（居住房间目标值 ≥ 2.0%）
```

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 4. 疏散计算器（`egress_calculator.py`）

按 IBC 计算使用人数、所需出口数量、最小出口宽度及疏散距离合规性。

### 参数

| 参数            | 标志               | 默认值   | 说明                            |
|----------------|--------------------|---------|---------------------------------|
| 楼层面积        | `--floor-area`     | 必填     | 净楼层面积（m2）                |
| 使用类型        | `--occupancy-type` | 必填     | IBC 使用分类（A-1 至 U）        |
| 设有喷淋        | `--sprinklered`    | False    | 标志：建筑设有自动喷水灭火系统  |
| 建筑层数        | `--num-stories`    | 1        | 层数                            |

### 示例

```bash
python scripts/egress_calculator.py --floor-area 800 --occupancy-type B --sprinklered --num-stories 4
```

### 示例输出

```
=== 疏散计算器 ===
楼层面积：          800.00 m2
使用类型：          B（商务办公）
设有喷淋：          是
建筑层数：          4
---------------------------------------
人员荷载系数：          9.3 m2/人
使用人数：              86 人
---------------------------------------
所需出口数量：          2
最小总出口宽度：        1,376 mm
每个出口宽度：          688 mm
最小门宽：              813 mm（32 英寸）
---------------------------------------
最大疏散距离：          91.0 m（300 ft）[设有喷淋]
最大共用路径：          23.0 m（75 ft）
最大尽端走道：          15.0 m（50 ft）

合规提示：请在平面图上复核疏散距离。
```

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 5. 结构荷载计算器（`structural_load_calculator.py`）

计算柱分担面积的竖向荷载，用于结构初步选型。

### 参数

| 参数            | 标志               | 默认值  | 单位     | 说明                         |
|----------------|--------------------|---------|---------|-----------------------------|
| 柱分担面积      | `--tributary-area` | 必填    | m2       | 柱的分担面积                  |
| 支承层数        | `--num-floors`     | 必填    | 整数     | 所支承的楼层数                |
| 恒载            | `--dead-load`      | 4.5     | kN/m2    | 每层恒载                      |
| 活载            | `--live-load`      | 自动    | kN/m2    | 活载（按使用类型自动选取）    |
| 使用类型        | `--occupancy-type` | office  | 字符串   | 用于自动选取活载              |

### 示例

```bash
python scripts/structural_load_calculator.py --tributary-area 36 --num-floors 8 --occupancy-type office
```

### 示例输出

```
=== 结构荷载计算器 ===
柱分担面积：        36.00 m2
楼层数：            8
---------------------------------------
恒载：              4.50 kN/m2/层
活载：              2.50 kN/m2/层（office）
每层合计：          7.00 kN/m2
---------------------------------------
每层荷载：          252.00 kN
柱总荷载：          2,016.00 kN（8 层）
组合荷载：          2,822.40 kN（1.2D + 1.6L）
---------------------------------------
初步柱截面：        约 400×400 mm RC（fc'=35 MPa）
```

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 6. 能耗计算器（`energy_calculator.py`）

采用度日法估算年度供暖和制冷能耗需求。

### 参数

| 参数                | 标志                   | 默认值  | 单位    | 说明                           |
|--------------------|------------------------|---------|---------|-------------------------------|
| 建筑面积            | `--floor-area`         | 必填    | m2      | 空调建筑面积                   |
| 围护结构面积        | `--envelope-area`      | 必填    | m2      | 围护结构总面积                 |
| 平均 U 值           | `--average-u-value`    | 必填    | W/m2K   | 面积加权平均 U 值              |
| 供暖度日数          | `--heating-degree-days`| 必填    | Kd      | 年 HDD（基准温度 18C）         |
| 制冷度日数          | `--cooling-degree-days`| 必填    | Kd      | 年 CDD（基准温度 24C）         |
| 通风换气次数        | `--ventilation-rate`   | 0.5     | ACH     | 每小时换气次数                 |
| 室内得热            | `--internal-gains`     | 5.0     | W/m2    | 室内热增益                     |

### 示例

```bash
python scripts/energy_calculator.py \
  --floor-area 500 --envelope-area 800 --average-u-value 0.35 \
  --heating-degree-days 3000 --cooling-degree-days 500
```

### 示例输出

```
=== 能耗计算器 ===
建筑面积：             500.00 m2
围护结构面积：         800.00 m2
平均 U 值：            0.35 W/m2K
---------------------------------------
供暖度日数：           3,000 Kd
制冷度日数：           500 Kd
通风换气次数：         0.50 ACH
室内得热：             5.00 W/m2
---------------------------------------
传热损失：             6,720.00 kWh/年
通风损失：             4,050.00 kWh/年
室内得热：             -2,190.00 kWh/年
供暖需求：             8,580.00 kWh/年
---------------------------------------
制冷需求：             2,356.00 kWh/年
---------------------------------------
总需求：               10,936.00 kWh/年
能耗强度 EUI：         21.87 kWh/m2/年

被动房目标：           15 kWh/m2/年 —— 不符合
```

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 7. 造价计算器（`cost_calculator.py`）

根据建筑类型、品质等级和地理区域估算建造成本。

### 参数

| 参数             | 标志                | 默认值       | 说明                               |
|-----------------|---------------------|--------------|------------------------------------|
| GFA              | `--gfa`             | 必填         | 总建筑面积（m2）                   |
| 建筑类型         | `--building-type`   | 必填         | residential/office/retail/hospital/school/hotel |
| 品质等级         | `--quality`         | standard     | basic/standard/premium             |
| 区域             | `--region`          | north-america| north-america/europe/middle-east/asia/australia |
| 包含室外工程     | `--include-external`| False        | 标志：包含场地工程                 |

### 示例

```bash
python scripts/cost_calculator.py --gfa 5000 --building-type office --quality premium --region europe
```

### 示例输出

```
=== 建造成本计算器 ===
总建筑面积：        5,000.00 m2
建筑类型：          办公
品质等级：          高标准
区域：              欧洲
---------------------------------------
基础单方造价：      2,800.00 USD/m2
建造成本：          14,000,000 USD
---------------------------------------
专业服务费（12%）：       1,680,000 USD
不可预见费（7.5%）：      1,050,000 USD
室外工程：                --
---------------------------------------
开发总成本：              16,730,000 USD
每平方米总成本：          3,346.00 USD/m2
```

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
## 方法参考

每个计算器的详细公式和方法记录在
`references/calculator-reference.md` 中。

## 错误处理

所有计算器都会校验输入并提供清晰的错误信息：
- 缺少必填参数时显示用法帮助
- 超出范围的数值会被拒绝，并说明原因
- 无效使用类型会列出可接受的值
- 格式错误的 JSON 输入会显示预期格式

## 集成

JSON 输出（`--json` 标志）可用于集成至：
- 工作流中的其他脚本
- 电子表格工具（解析 JSON）
- Web 仪表板
- 自动化报告系统
- BIM 参数写入
#

license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab AI建筑与室内设计总设计师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
