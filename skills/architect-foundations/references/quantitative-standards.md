---
name: quantitative-standards
description: 注册建筑师专业参考：quantitative-standards。
license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---

# 定量标准参考
## 建筑设计数值、经验法则与规范派生指标

> Sources: Neufert Architects' Data (5th Ed.), Architectural Graphic Standards (12th Ed.),
> IBC 2021, ASHRAE 62.1-2022, ASHRAE 90.1-2022, BS EN standards, Passive House Institute,
> CIBSE Guide A, Metric Handbook (6th Ed.), ADA/ABA Standards, NBC India 2016.

---

## 1. 人体尺寸标准

### 1.1 人体测量数据（成年男性第 95 百分位 / 成年女性第 5 百分位）

| 尺寸 | 男性第 95 百分位 | 女性第 5 百分位 | 设计用途 |
|------------------------------|-----------|------------|-----------------------------|
| Standing height              | 1870 mm   | 1500 mm    | Clearance above head        |
| Standing eye height          | 1745 mm   | 1405 mm    | Signage, display placement  |
| Standing shoulder height     | 1535 mm   | 1215 mm    | Handrail upper limit        |
| Standing elbow height        | 1165 mm   | 930 mm     | Counter heights             |
| Seated eye height (chair)    | 1310 mm   | 1070 mm    | Sightline calculation       |
| Seated eye height (wheelchair)| 1180 mm  | 1070 mm    | Accessible counter design   |
| Forward reach (standing)     | 600-1800 mm range        | Shelf/switch placement      |
| Side reach (wheelchair)      | 230-1370 mm range        | ADA operable part range     |
| Wheelchair footprint         | 700 x 1200 mm           | Minimum turning clearance   |
| Wheelchair 180 turn          | 1500 mm diameter         | Accessible toilet/corridor  |
| Wheelchair T-turn            | 1525 x 1525 mm          | Alternative to 180 turn     |

Source: Neufert Ch. 1; ADA/ABA 304-308; BS 8300:2018.

### 1.2 人体工学工作高度

| 表面/设施 | 高度（mm） | 备注 |
|------------------------|-------------|---------------------------------|
| Kitchen worktop        | 850-950     | 900 standard; adjust to user    |
| Desk (seated)          | 720-760     | 740 typical; adjustable 650-850 |
| Standing desk          | 950-1100    | Adjustable preferred            |
| Reception counter      | 1050-1150   | With accessible section at 750  |
| Bar counter            | 1050-1150   | With footrail at 250 from floor |
| Dining table           | 720-760     | Chair seat 430-460              |
| Bathroom vanity        | 800-850     | Accessible: max 865, knee 685   |
| Handrail               | 900-1000    | Stair: 900; guard: 1100 min     |

---

## 2. 门与洞口尺寸

### 2.1 门宽

| 类型 | 最小值（mm） | 标准值（mm） | 备注 |
|---------------------------|----------|---------------|-----------------------------|
| Single leaf residential   | 762      | 900           | 838 common in US            |
| Accessible (clear width)  | 915      | 915           | ADA 404.2.3; measured leaf  |
| Corridor single           | 900      | 1000          | 1050 for hospital           |
| Double leaf               | 1500     | 1800          | Each leaf 750-900           |
| Fire door (single)        | 838      | 900           | Must be self-closing        |
| Service/back-of-house     | 900      | 1050          | Allow trolley passage       |
| Loading dock overhead     | 2400     | 3000          | Height 3000-4200            |
| Garage (single car)       | 2400     | 2700          | Height 2100 min             |
| Garage (double car)       | 4200     | 4800          | Height 2100 min             |

### 2.2 门高

| 场景 | 最小值（mm） | 标准值（mm） | 最大值（mm） | 备注 |
|---------------|----------|---------------|----------|--------------------------|
| Residential   | 2040     | 2100          | 2400     | 2100 code minimum        |
| Commercial    | 2100     | 2200          | 3000     | Full height trending     |
| Accessible    | 2032     | 2100          | --       | ADA 404.2.3              |
| Overhead/roll | 3000     | 3600          | 5000     | Vehicle clearance driven |

### 2.3 门洞操作净空（ADA 404.2.4）

| 接近方向 | 拉侧 | 推侧 |
|--------------------|------------|------------|
| Front approach     | 1525 depth | 1220 depth |
| Hinge approach     | 1525 depth, 915 beside | 1065 depth, 610 beside |
| Latch approach     | 1525 depth, 610 beside | 1220 depth, 610 beside |

---

## 3. 楼梯与坡道尺寸

### 3.1 楼梯几何尺寸

| 参数 | 最小值 | 优选值 | 最大值 | 来源 |
|-----------------------|--------|----------|--------|----------------------|
| Riser height          | 125 mm | 165 mm   | 180 mm | IBC 1011.5.2         |
| Tread depth           | 254 mm | 280 mm   | 330 mm | IBC 1011.5.2         |
| Blondel formula       | --     | 2R+T=600-640 mm     | --     | Neufert              |
| Nosing projection     | --     | 19-32 mm | 38 mm  | IBC 1011.5.5         |
| Width (min, no handrail deduction) | 1100 mm | 1200 mm | -- | IBC 1011.2 |
| Headroom              | 2032 mm| 2200 mm  | --     | IBC 1011.3           |
| Handrail height       | 865 mm | 900 mm   | 965 mm | IBC 1014.2           |
| Handrail extension top| 305 mm | 305 mm   | --     | IBC 1014.6           |
| Handrail extension bot| 305+tread depth | -- | --   | IBC 1014.6           |
| Max rise between landings | -- | 3660 mm  | 3660 mm| IBC 1011.8           |
| Landing depth         | = width| = width  | --     | IBC 1011.6           |

### 3.2 坡道几何尺寸

| 参数 | 最小值 | 优选值 | 最大值 | 来源 |
|-----------------------|---------|----------|---------|---------------------|
| Slope                 | --      | 1:15     | 1:12    | ADA 405.2           |
| Cross slope           | --      | 1:50     | 1:48    | ADA 405.3           |
| Width (clear)         | 915 mm  | 1200 mm  | --      | ADA 405.5           |
| Rise per run          | --      | 600 mm   | 760 mm  | ADA 405.6           |
| Landing length        | 1525 mm | 1525 mm  | --      | ADA 405.7           |
| Edge protection height| 50 mm   | 100 mm   | --      | ADA 405.9           |

---

## 4. 吊顶高度与层高

### 4.1 最小净高

| 空间类型 | 最小值（m） | 典型值（m） | 高端值（m） | 来源 |
|-------------------------|---------|-------------|-------------|----------------|
| Residential habitable   | 2.40    | 2.55-2.70   | 3.00-3.60   | IBC 1208.2     |
| Residential non-hab     | 2.10    | 2.30        | --          | IBC 1208.2     |
| Office (open plan)      | 2.70    | 2.75-3.00   | 3.30-4.00   | Metric Handbook |
| Office (cellular)       | 2.50    | 2.70        | 3.00        | Metric Handbook |
| Retail (ground floor)   | 3.50    | 4.00-5.00   | 6.00+       | Neufert         |
| Supermarket             | 3.50    | 4.00-5.00   | 6.00        | Industry std    |
| Restaurant              | 2.70    | 3.00-3.50   | 4.50+       | Neufert         |
| Hotel room              | 2.60    | 2.70-2.80   | 3.20        | Metric Handbook |
| Hospital ward           | 2.70    | 3.00-3.30   | 3.60        | HTM 08-01       |
| Classroom               | 2.70    | 3.00-3.30   | 3.60        | BB103           |
| Assembly/auditorium     | 3.00    | 4.00-6.00   | 12.00+      | Project-specific|
| Warehouse               | 6.00    | 8.00-10.00  | 12.00-15.00 | Neufert         |
| Parking (clear)         | 2.10    | 2.40        | 2.70        | IBC 406.4       |

### 4.2 典型层高

| 建筑类型 | 典型值（m） | 包含内容 |
|-------------------------|-------------- |-----------------------------------|
| Residential apartment   | 2.80-3.10    | 150 slab + ceiling void           |
| Office (steel frame)    | 3.60-4.00    | 600-1000 ceiling void + 150 floor |
| Office (RC frame)       | 3.30-3.80    | Flat slab or beam-slab            |
| Retail (ground floor)   | 4.50-6.00    | Greater services, higher ceiling  |
| Hospital                | 4.00-4.50    | Heavy MEP, interstitial possible  |
| Hotel                   | 3.10-3.40    | Compact services distribution     |
| Parking (per level)     | 3.00-3.30    | Sloped or flat deck               |

---

## 5. 结构经验法则

### 5.1 跨高比

| 构件 | 简支 | 连续 | 悬臂 | 来源 |
|--------------------------------|-----------------|-------------|------------|-----------------|
| RC one-way slab                | L/28            | L/32        | L/10       | ACI 318 Table 9.3.1.1 |
| RC two-way slab (flat plate)   | L/30            | L/33        | L/8        | ACI 318         |
| RC two-way slab (with beams)   | L/33            | L/36        | --         | ACI 318         |
| Post-tensioned slab            | L/40            | L/48        | L/15       | PTI manual      |
| RC beam                        | L/12            | L/18        | L/6        | ACI 318         |
| RC deep beam                   | L/4-L/6         | --          | --         | Project-specific|
| Steel beam (W-shape)           | L/20            | L/24        | L/8        | AISC manual     |
| Steel plate girder             | L/10-L/12       | L/12-L/15   | L/5        | AISC manual     |
| Steel truss (parallel chord)   | L/10            | L/12-L/15   | L/5        | Structural ref  |
| Steel open web joist           | L/20-L/24       | --          | --         | SJI catalog     |
| Glulam beam                    | L/15            | L/20        | L/7        | NDS/Eurocode 5  |
| CLT floor panel                | L/25            | L/30        | L/10       | CLT Handbook    |
| LVL beam                       | L/16-L/20       | L/20-L/24   | L/8        | Manufacturer    |
| Precast hollow-core slab       | L/30-L/35       | --          | --         | PCI manual      |
| Precast double-tee             | L/25-L/30       | --          | --         | PCI manual      |
| Composite steel deck slab      | L/28-L/32       | --          | --         | SDI manual      |

### 5.2 典型柱截面尺寸（方形钢筋混凝土柱，正常荷载）

| 支承楼层数 | 轻荷载（5 kPa） | 中荷载（7.5 kPa） | 重荷载（10+ kPa） |
|-------------------|--------------------|--------------------|-----------------|
| 1-3               | 300 x 300 mm      | 350 x 350 mm      | 400 x 400 mm   |
| 4-8               | 400 x 400 mm      | 450 x 450 mm      | 500 x 500 mm   |
| 9-15              | 500 x 500 mm      | 550 x 550 mm      | 600 x 600 mm   |
| 16-25             | 600 x 600 mm      | 700 x 700 mm      | 800 x 800 mm   |
| 25+               | 700+ x 700+ mm    | 800+ x 800+ mm    | 900+ x 900+ mm |

Note: Highly dependent on concrete grade (C30-C60), reinforcement ratio (1-4%), and slenderness.

### 5.3 各体系典型跨度范围

| 体系 | 经济跨度（m） | 最大跨度（m） |
|---------------------------------|-------------------|-------------------|
| RC flat slab                    | 6-9               | 12                |
| RC beam-slab                    | 6-12              | 15                |
| PT flat slab                    | 8-12              | 16                |
| PT beam-slab                    | 10-18             | 22                |
| Composite steel beam + deck     | 9-15              | 20                |
| Steel castellated beam          | 12-18             | 25                |
| Precast hollow-core             | 6-16              | 18                |
| Precast double-tee              | 15-25             | 30                |
| Steel truss                     | 20-40             | 80+               |
| Glulam portal frame             | 15-30             | 50                |
| CLT floor                       | 4-8               | 10                |
| Timber I-joist                  | 4-7               | 9                 |

### 5.4 基础经验法则

| 基础类型 | 假定承载力 | 深度规则 | 备注 |
|----------------------|--------------------------|---------------------|------------------------|
| Strip footing        | 75-150 kPa              | Width = 2-3x wall   | For loadbearing walls  |
| Pad footing          | 100-300 kPa             | Depth = 1-1.5x size | Isolated columns       |
| Raft                 | 50-100 kPa              | Depth = L/10-L/15   | Poor ground, uniform   |
| Bored pile           | 200-1000+ kPa (end)     | Dia 450-1500mm      | Capacity per pile varies|
| CFA pile             | 150-600 kPa (end)       | Dia 300-900mm       | Quick installation     |
| Screw pile           | 50-500 kN per pile       | Dia 76-400mm shaft  | Light structures       |

---

## 6. 环境与能源目标

### 6.1 按气候区划分的 U 值（W/m²K）

| 要素 | CZ 1–2（炎热） | CZ 3–4（混合） | CZ 5–6（寒冷） | CZ 7–8（严寒） | Passive House |
|------------------|---------------|-----------------|----------------|---------------------|---------------|
| External wall    | 0.70          | 0.45            | 0.32           | 0.25                | 0.10-0.15     |
| Roof             | 0.35          | 0.27            | 0.20           | 0.15                | 0.10-0.15     |
| Ground floor     | 0.52          | 0.34            | 0.26           | 0.20                | 0.10-0.15     |
| Window (total)   | 3.69          | 2.56            | 2.00           | 1.50                | 0.80          |
| Door             | 3.00          | 2.27            | 1.50           | 1.20                | 0.80          |

Sources: ASHRAE 90.1-2022 Table 5.5; Passive House Institute criteria.

### 6.2 太阳得热系数（SHGC）/ g 值

| 朝向/气候 | 最大 SHGC（炎热） | 最大 SHGC（混合） | 最小 SHGC（寒冷） | 备注 |
|----------------------------|---------------- |-------------------|------------------|--------------------|
| South (N.Hem) / passive    | 0.25            | 0.40              | 0.50-0.60        | Maximize winter gain|
| West / East (all)          | 0.25            | 0.25-0.35         | 0.40             | Control afternoon  |
| North (N.Hem)              | 0.40            | 0.40              | 0.40-0.60        | Diffuse light only |
| Skylight                   | 0.25            | 0.30              | 0.40             | High solar exposure|

Note: g-value (European) approximately equals SHGC x 1.0 (they are nearly equivalent metrics).

### 6.3 采光系数目标

| 空间类型 | 最小 DF | 建议 DF | 来源 |
|-------------------------|-----------|----------------|-------------------|
| Residential living      | 1.5%      | 2.0%+          | BS 8206-2         |
| Residential kitchen     | 1.5%      | 2.0%+          | BS 8206-2         |
| Residential bedroom     | 1.0%      | 1.5%+          | BS 8206-2         |
| Office (general)        | 2.0%      | 2.5-5.0%       | CIBSE LG7         |
| Classroom               | 2.0%      | 3.0-5.0%       | BB90/CIBSE LG5    |
| Hospital ward           | 1.5%      | 2.0%+          | HTM/CIBSE LG2     |
| Retail (general)        | 1.5%      | 2.0-3.0%       | CIBSE LG6         |
| Library reading room    | 2.0%      | 3.0-5.0%       | CIBSE LG7         |
| Art studio / lab        | 4.0%      | 5.0-8.0%       | Neufert           |
| Corridor / circulation  | 0.5%      | 1.0%           | --                |

### 6.4 按 EN 12464-1 / CIBSE SLL 的照度水平（lux）

| 空间类型 | 最小值（lux） | 维持值（lux） | 备注 |
|-------------------------|-----------|-------------------|----------------------|
| Corridor/circulation    | 50        | 100               | Emergency: 1 lux     |
| Stairway                | 100       | 150               |                      |
| Office (general)        | 300       | 500               | Task: 750 at desk    |
| Meeting room            | 300       | 500               |                      |
| Reception               | 200       | 300               |                      |
| Classroom               | 300       | 500               | Whiteboard: 500      |
| Library reading         | 300       | 500               |                      |
| Retail (general)        | 300       | 500               | Display: 750-1000    |
| Supermarket             | 300       | 500               |                      |
| Hospital ward           | 100       | 300               | Exam: 1000           |
| Operating theatre       | --        | 1000              | Surgical: 10000-100000|
| Restaurant              | 50        | 150-300           | Atmosphere-dependent |
| Hotel room              | 100       | 200               | Reading: 300-500     |
| Industrial fine work    | 500       | 750-1000          |                      |
| Parking (indoor)        | 50        | 75-100            |                      |

---

## 7. 通风量（ASHRAE 62.1-2022）

### 7.1 室外空气要求

| 空间类型 | 每人（L/s） | 每面积（L/s/m²） | 默认密度（m²/人） |
|---------------------------|-------------------|--------------------|-----------------------------|
| Office                    | 2.5               | 0.3                | 20                          |
| Conference/meeting        | 2.5               | 0.3                | 5                           |
| Lecture hall              | 3.8               | 0.3                | 1.5                         |
| Classroom (age 9+)       | 5.0               | 0.6                | 4                           |
| Classroom (age 5-8)      | 5.0               | 0.6                | 3                           |
| Retail (sales floor)     | 3.8               | 0.6                | 7                           |
| Restaurant dining         | 3.8               | 0.9                | 7                           |
| Hotel bedroom/living     | 2.5               | 0.3                | 10                          |
| Lobby/reception          | 2.5               | 0.3                | 10                          |
| Hospital patient room    | 2.5               | 0.6                | 10                          |
| Hospital operating       | Special: 100% OA, 15-25 ACH total  ||| AIA/ASHRAE 170   |
| Gym/exercise             | 10.0              | 0.6                | 7                           |
| Museum gallery           | 3.8               | 0.6                | 4                           |
| Corridor                 | --                | 0.3                | --                          |
| Parking garage           | --                | 3.8                | --                          |

### 7.2 排风量（间歇/连续）

| 空间 | 间歇（L/s） | 连续（L/s） | 来源 |
|--------------------------|--------------------|--------------------|---------------------|
| Kitchen (domestic)       | 50-60              | 12                 | ADF Part F / 62.2   |
| Bathroom (domestic)      | 25                 | 8                  | ADF Part F / 62.2   |
| WC (domestic)            | 25                 | 6                  | ADF Part F / 62.2   |
| Utility room             | 25                 | 8                  | ADF Part F           |
| Laundry (commercial)     | --                 | 10 ACH             | ASHRAE 62.1          |
| Commercial kitchen       | Varies: hood CFM based on appliance type    || NFPA 96/ASHRAE 154|

---

## 8. 室内得热

### 8.1 人员

| 活动水平 | 显热（W） | 潜热（W） | 总热量（W） | 来源 |
|--------------------------|-------------- |------------|-----------|---------------|
| Seated, at rest          | 60            | 40         | 100       | ASHRAE Fund.  |
| Seated, light work       | 70            | 45         | 115       | ASHRAE Fund.  |
| Office work              | 75            | 55         | 130       | ASHRAE Fund.  |
| Standing, light work     | 75            | 55         | 130       | ASHRAE Fund.  |
| Walking (moderate)       | 75            | 75         | 150       | ASHRAE Fund.  |
| Heavy work/exercise      | 110           | 185        | 295       | ASHRAE Fund.  |
| Dancing                  | 90            | 160        | 250       | ASHRAE Fund.  |

### 8.2 设备与照明

| 项目/空间类型 | 功率密度 | 备注 |
|--------------------------------|----------------------|------------------------------|
| Office lighting (LED)          | 8-12 W/m2            | Target 8 for LEED/BREEAM    |
| Retail lighting                | 12-18 W/m2           | Display-heavy: 20+          |
| Residential lighting           | 5-8 W/m2             | LED standard                |
| Office equipment (per desk)    | 120-200 W            | Monitor + PC + chargers     |
| Office equipment (density)     | 10-15 W/m2           | Open plan typical            |
| Trading floor equipment        | 25-40 W/m2           | High density screens         |
| Data center                    | 500-2000+ W/m2       | Cooling-dominated            |
| Server room (in office)        | 200-500 W/m2         | Supplemental cooling needed  |
| Kitchen equipment (commercial) | 200-500 W/m2         | Hood exhaust required        |
| Residential equipment          | 3-5 W/m2             | Average including standby    |
| Laboratory                     | 20-50 W/m2           | Fume hoods significant       |

---

## 9. 使用人数荷载与疏散

### 9.1 使用人数系数（IBC 表 1004.5）

| 用途 | 每人面积（m²） | 备注 |
|------------------------------------|------------------------|-------------------------------|
| Assembly, concentrated (no seats)  | 0.65 net               | Dance floor, standing event   |
| Assembly, standing                 | 0.46 net               | Standing room only            |
| Assembly, unconcentrated (chairs)  | 1.4 net                | Conference, dining            |
| Assembly, fixed seats              | Count seats            | Number of seats = occupants   |
| Business/office                    | 9.3 gross              |                               |
| Courtrooms                        | 3.7 net                |                               |
| Educational classroom              | 1.9 net                |                               |
| Educational shop/lab               | 4.6 net                |                               |
| Exercise rooms                     | 4.6 gross              |                               |
| Industrial                         | 9.3 gross              |                               |
| Institutional inpatient            | 22.3 gross             |                               |
| Institutional outpatient           | 9.3 gross              |                               |
| Mercantile (basement/ground)       | 2.8 gross              |                               |
| Mercantile (upper floors)          | 5.6 gross              |                               |
| Parking garage                     | 18.6 gross             |                               |
| Residential                        | 18.6 gross             |                               |
| Storage                            | 27.9 gross             | Low hazard                    |
| Swimming pool (water surface)      | 4.6 gross              |                               |
| Swimming pool (deck)               | 2.8 gross              |                               |

### 9.2 疏散宽度要求（IBC 1005）

| 构成要素 | 楼梯系数 | 其他系数 | 备注 |
|-------------------|--------------------|-------------------|----------------------------|
| Without sprinkler | 7.6 mm/occupant    | 5.1 mm/occupant   | From IBC 1005.1            |
| With sprinkler    | 5.1 mm/occupant    | 3.8 mm/occupant   | Reduced with sprinkler     |
| Min stair width   | 1120 mm            | --                | IBC 1011.2 (>50 occupants)|
| Min corridor      | --                 | 1120 mm           | IBC 1020.2 (>50 occupants)|
| Min door           | --                 | 815 mm clear      | IBC 1010.1.1               |

### 9.3 最大疏散距离（IBC 表 1017.2）

| 使用组别 | 无喷淋（m） | 有喷淋（m） |
|-----------------|-------------------|-----------------|
| A, E, F-1, M, R, S-1 | 61          | 76              |
| B               | 61                | 91              |
| F-2, S-2, U     | 76                | 122             |
| H-1             | 23                | 23              |
| H-2             | 30                | 30              |
| H-3             | 46                | 46              |
| I-1             | 61                | 76              |
| I-2             | 46                | 61              |

### 9.4 疏散共用路径（IBC 表 1006.2.1）

| 使用性质 | 最大共用路径（m） | 备注 |
|-----------|---------------------|--------------------------|
| A, E      | 23 (sprinklered)    |                          |
| B         | 30 (sprinklered)    | 23 unsprinklered         |
| R-2       | 38 (sprinklered)    | 23 unsprinklered         |
| F, S      | 23 (sprinklered)    |                          |
| I-2       | 15                  | Healthcare critical      |

---

## 10. 耐火等级（IBC 表 601）

### 10.1 要求耐火时间（小时）

| Element              | Type IA | Type IB | Type IIA | Type IIB | Type IIIA | Type IIIB | Type IV-A | Type IV-B | Type VA | Type VB |
|----------------------|---------|---------|----------|----------|-----------|-----------|-----------|-----------|---------|---------|
| Structural frame     | 3       | 2       | 1        | 0        | 1         | 0         | 3         | 2         | 1       | 0       |
| Bearing walls (ext)  | 3       | 2       | 1        | 0        | 2         | 2         | 3         | 2         | 1       | 0       |
| Bearing walls (int)  | 3       | 2       | 1        | 0        | 1         | 0         | 3         | 2         | 1       | 0       |
| Floor construction   | 2       | 2       | 1        | 0        | 1         | 0         | 2         | 2         | 1       | 0       |
| Roof construction    | 1.5     | 1       | 1        | 0        | 1         | 0         | 1.5       | 1         | 1       | 0       |

### 10.2 常见防火分隔要求

| 条件 | 最小等级（小时） | 来源 |
|----------------------------------------|-----------------|------------------|
| Dwelling-dwelling (party wall)         | 1               | IBC 706/708      |
| Corridor wall (Group I-2)              | 1 (smoke)       | IBC 407          |
| Stair enclosure (< 4 storeys)         | 1               | IBC 713.4        |
| Stair enclosure (>= 4 storeys)        | 2               | IBC 713.4        |
| Shaft enclosure (< 4 storeys)         | 1               | IBC 713.4        |
| Shaft enclosure (>= 4 storeys)        | 2               | IBC 713.4        |
| Occupancy separation (A/B)            | 1               | IBC Table 508.4  |
| Occupancy separation (A/S-1)          | 2               | IBC Table 508.4  |
| Fire barrier (tenant separation)       | 1               | IBC 707          |

---

## 11. 声学性能

### 11.1 空气声隔声（STC / Rw）

| 相邻关系 | 最小 STC | 建议 Rw | 来源 |
|---------------------------------|---------|-----------------|-----------------------|
| Dwelling to dwelling (wall)     | 50      | 53-56           | IBC 1207 / ADE Part E|
| Dwelling to dwelling (floor)    | 50      | 53-56           | IBC 1207 / ADE Part E|
| Dwelling to corridor            | 50      | 48-50           | IBC 1207              |
| Hotel room to hotel room        | 50      | 53-55           | Industry standard     |
| Hotel room to corridor          | 45      | 48-50           | Industry standard     |
| Classroom to classroom          | 50      | 48-53           | ANSI S12.60 / BB93    |
| Classroom to corridor           | 45      | 45-48           | BB93                  |
| Office to office                | 45      | 45-50           | STC recommendation    |
| Music room to adjacent          | 55      | 60-65           | BB93                  |
| Plant room to occupied          | 55      | 55-60           | CIBSE Guide B         |

### 11.2 撞击声隔声（IIC / Ln,w）

| 相邻关系 | 最小 IIC | 目标 Ln,w | 来源 |
|---------------------------------|---------|----------------|-----------------------|
| Dwelling floor above dwelling   | 50      | 53 (max)       | IBC 1207 / ADE Part E|
| Hotel floor above room          | 55      | 48 (max)       | Industry standard     |
| Classroom floor above classroom | 50      | 58 (max)       | BB93                  |
| Office floor above office       | 45      | 60 (max)       | Recommendation        |

Note: IIC is a higher-is-better rating; Ln,w is lower-is-better.

### 11.3 混响时间（RT60）目标

| 空间类型 | 最小值（s） | 优选值（s） | 最大值（s） | 频率范围 |
|---------------------------|---------|-------------|---------|-----------------|
| Classroom (primary)       | 0.4     | 0.6         | 0.8     | 500 Hz-2 kHz    |
| Classroom (secondary)     | 0.5     | 0.6-0.8     | 1.0     | 500 Hz-2 kHz    |
| Lecture hall (100+ seats) | 0.7     | 0.8-1.0     | 1.2     | 500 Hz-2 kHz    |
| Open plan office          | 0.5     | 0.6-0.8     | 1.0     | 500 Hz-2 kHz    |
| Concert hall              | 1.8     | 1.9-2.2     | 2.4     | 500 Hz-1 kHz    |
| Opera house               | 1.2     | 1.3-1.6     | 1.8     | 500 Hz-1 kHz    |
| Recording studio          | 0.2     | 0.3-0.5     | 0.6     | Broadband        |
| Cinema                    | 0.4     | 0.5-0.7     | 0.8     | 500 Hz-2 kHz    |
| Swimming pool hall        | 1.5     | 2.0         | 2.5     | Difficult space  |
| Restaurant                | 0.5     | 0.6-0.9     | 1.0     | Atmosphere       |
| Hospital ward             | 0.5     | 0.6-0.8     | 1.0     | Comfort          |

### 11.4 背景噪声指标

| 空间类型 | NR / NC 等级 | 备注 |
|---------------------------|----------------|------------------------------|
| Bedroom (residential)     | NR 25 / NC 25  | CIBSE Guide B                |
| Living room               | NR 30 / NC 30  | CIBSE Guide B                |
| Hospital ward             | NR 30 / NC 30  | HTM 08-01                    |
| Hotel bedroom             | NR 25-30 / NC 25-30 | Luxury: NR 20         |
| Classroom                 | NR 30 / NC 30  | BB93: 35 dB LAeq30min       |
| Open plan office          | NR 35-40 / NC 35-40 | Masking beneficial     |
| Private office            | NR 30-35 / NC 30-35 |                          |
| Concert hall              | NR 15-20 / NC 15-20 | PNC 15-20 preferred    |
| Recording studio          | NR 15 / NC 15  | NC 10-15 ideal               |
| Theatre                   | NR 20-25 / NC 20-25 |                          |
| Restaurant                | NR 35-40 / NC 35-40 |                          |
| Library reading room      | NR 30 / NC 30  |                              |
| Conference room           | NR 25-30 / NC 25-30 |                          |

---

## 12. 机电空间预留

### 12.1 设备房/机械空间（占 GFA 百分比）

| 建筑类型 | 最小比例 | 典型比例 | 备注 |
|-----------------------|--------|------------|------------------------------------|
| Office (AC)           | 5%     | 6-8%       | Higher with central plant          |
| Office (naturally vent)| 2%    | 3-4%       | Minimal HVAC                       |
| Hospital              | 8%     | 10-12%     | AHU, medical gas, generator        |
| Hotel                 | 5%     | 6-8%       | Laundry adds 1-2%                  |
| Residential           | 3%     | 3-5%       | Per unit: riser + meter            |
| Retail (shell)        | 3%     | 4-5%       | Tenant fit-out additional          |
| Laboratory            | 10%    | 12-18%     | Fume hood exhaust intensive        |
| Data center           | 30%    | 35-40%     | Cooling + power dominant           |
| School                | 4%     | 5-7%       | Plant rooms + boiler/chiller       |
| Museum/gallery        | 6%     | 8-10%      | Climate control critical           |

### 12.2 电气空间

| 构成要素 | 预留面积 | 备注 |
|------------------------|-----------------------|----------------------------------|
| Main switchroom        | 25-50 m2              | Per 10,000 m2 GFA               |
| Sub-distribution       | 5-10 m2 per floor     | Adjacent to core                 |
| Transformer room       | 15-30 m2              | Per 1000 kVA; ventilation needed |
| Generator room         | 20-40 m2              | Fuel storage + exhaust route     |
| UPS room               | 10-20 m2              | Data/critical applications       |
| Comms/server room      | 10-20 m2 per floor    | Temperature controlled           |
| Total electrical GFA   | 2-3% GFA              | All electrical spaces combined   |

### 12.3 吊顶空腔与管井

| 建筑类型 | 吊顶空腔（mm） | 楼板空腔（mm） | 备注 |
|-----------------------|-------------------|-----------------|------------------------------|
| Residential           | 150-400           | 0-100           | Minimal services             |
| Office (standard)     | 400-600           | 50-150          | Cable management              |
| Office (deep plan)    | 600-800           | 100-200         | VAV boxes, larger ductwork   |
| Office (raised floor) | 250-400           | 150-300         | Data center heritage         |
| Hospital              | 800-1200          | 0-100           | Interstitial floors possible |
| Laboratory            | 600-1000          | 100-200         | Flexible services routing    |
| Retail (ground)       | 400-600           | 0               | Exposed ceiling trending     |
| Hotel                 | 250-400           | 0               | Compact FCU systems          |

### 12.4 管井

| 服务类型 | 每层尺寸 | 备注 |
|-----------------------|----------------------|-----------------------------------|
| HVAC duct riser       | 0.5-1.5 m2          | Depends on system type            |
| Plumbing/drainage     | 0.3-0.5 m2          | Per wet core                      |
| Electrical            | 0.3-0.5 m2          | Busbar or cable tray              |
| Fire sprinkler        | 0.2-0.3 m2          | Valve sets at each floor          |
| Communications/data   | 0.3-0.5 m2          | Fiber/copper backbone             |
| Pneumatic tube (hosp) | 0.2-0.3 m2          | Hospital-specific                 |
| Smoke extract         | 0.5-2.0 m2          | Depends on floor area served      |
| Combined minimum      | 2.0-4.0 m2 total    | Per core, per floor               |

---

## 13. 停车

### 13.1 停车比例（典型分区最低值）

| 用途 | 城市（每 100m² GFA） | 郊区 | 备注 |
|----------------------|-----------------------|-------------------|------------------------------|
| Office               | 1.0-2.0 spaces        | 2.5-4.0 spaces    | Trend: reduce/eliminate      |
| Retail               | 2.0-3.0 spaces        | 4.0-5.0 spaces    | Anchor tenant higher         |
| Residential          | 0.5-1.0 per unit      | 1.0-2.0 per unit  | Studio: 0.5; 3BR: 1.5       |
| Hotel                | 0.5-0.8 per room      | 0.8-1.0 per room  | Event space adds more        |
| Hospital             | 1.5-2.5 per bed       | 2.5-4.0 per bed   | Staff + visitor + patient    |
| School               | 0.5 per classroom     | 1.0 per classroom  | Plus drop-off/bus            |
| Restaurant           | 5-10 per 100m2        | 10-15 per 100m2   | High turnover                |
| Industrial/warehouse | 0.5-1.0 per 100m2     | 1.0-2.0 per 100m2 | Truck loading separate       |

### 13.2 停车位与车道尺寸

| 类型 | 宽度（mm） | 长度（mm） | 车道宽度（mm） | 备注 |
|----------------------|------------|-------------|-------------------|--------------------|
| Standard (90 deg)    | 2400-2500  | 5400-5500   | 7200-7300         | Most common        |
| Compact (90 deg)     | 2200-2400  | 4600-4800   | 6600-7000         | Max 15-30% of total|
| Accessible           | 3600-3700  | 5400-5500   | 7200              | 1500 access aisle  |
| Van accessible       | 3600+2400  | 5400-5500   | 7200              | 2400 access aisle  |
| Parallel             | 2400       | 6700-7000   | 3600-4000         | On-street typical  |
| Angled (60 deg)      | 2500       | 5400        | 5500              | One-way aisle      |
| Bicycle              | 600        | 1800        | 1500 (aisle)      | Sheffield stand    |
| Motorcycle           | 1200       | 2400        | 3000              | Grouped preferred  |

### 13.3 坡道与车行几何

| 要素 | 数值 | 备注 |
|----------------------|--------------|-----------------------------------------|
| Ramp slope (max)     | 1:6 (17%)   | Preferred 1:8 (12.5%)                   |
| Ramp width (1-way)   | 3000-3600 mm | Plus clearance to walls                 |
| Ramp width (2-way)   | 6000-6600 mm | Center barrier above 6%                 |
| Transition slope     | 1:10 (10%)  | Top and bottom of ramp, 3m length       |
| Minimum turning radius| 7500 mm     | Inside kerb line                        |
| Clear height          | 2100-2400 mm| 2700 for vans                           |
| Column setback       | 300-500 mm   | From stall edge to column face          |

---

## 14. 电梯尺寸

### 14.1 电梯数量经验法则

| 建筑类型 | 人口基准 | 每人口对应电梯数 | 间隔目标 |
|-------------------|---------------------|--------------------------|-------------------|
| Office (prestige) | 1 per 10-12 m2 NFA  | 1 per 200-250 persons    | 20-25 seconds     |
| Office (standard) | 1 per 12-15 m2 NFA  | 1 per 250-350 persons    | 25-35 seconds     |
| Hotel             | 1.5-1.8 per room    | 1 per 60-80 rooms        | 30-50 seconds     |
| Residential       | --                  | 1 per 90-120 units       | 40-70 seconds     |
| Hospital          | --                  | 2-3 per 100 beds         | < 30 seconds      |
| Retail            | Based on occupancy   | 1 per 5000-8000 m2       | Escalators primary|

### 14.2 电梯井道典型尺寸

| 载重量/人数 | 井道宽度（mm） | 井道深度（mm） | 门宽（mm） | 备注 |
|-------------------|------------------|-------------------|-----------------|----------------|
| 8 person (630 kg) | 1600-1700        | 1700-1800         | 800             | Min residential|
| 13 person (1000kg)| 1900-2100        | 2100-2200         | 900-1000        | Standard office|
| 21 person (1600kg)| 2200-2400        | 2500-2700         | 1100            | Large office   |
| 26 person (2000kg)| 2400-2600        | 2700-2900         | 1200            | Hospital bed   |
| Bed/stretcher     | 2200-2400        | 2700-2900         | 1200-1300       | 2100mm car depth|
| Goods (2500kg)    | 2600-3000        | 3000-3200         | 1500            | Service core   |
| Firefighter       | 2000-2200        | 2400-2600         | 1100            | Dedicated shaft|

### 14.3 底坑与顶层净空

| 速度（m/s） | 底坑深度（mm） | 顶层净空高度（mm） | 备注 |
|-------------|----------------|----------------------|--------------------|
| 1.0         | 1200-1400      | 3600-3800            | Low-rise typical   |
| 1.6         | 1400-1600      | 3800-4200            | Mid-rise typical   |
| 2.5         | 1600-2000      | 4200-4800            | High-rise          |
| 4.0+        | 2500-3000      | 5500-6500            | Supertall          |

---

## 15. 装卸与服务

### 15.1 装卸平台尺寸

| 要素 | 尺寸 | 备注 |
|---------------------------|------------------|------------------------------------|
| Dock door width           | 2400-3000 mm     | 3000 standard for articulated      |
| Dock door height          | 3600-4200 mm     | 4200 for large trucks              |
| Dock leveler depth        | 1800-2500 mm     | Hydraulic or mechanical            |
| Apron space               | 18000-21000 mm   | Minimum for articulated truck      |
| Dock height               | 1200-1350 mm     | UK: 1200; US: 1320 (52")          |
| Bay spacing (center-center)| 3600-4000 mm    | Minimum for adjacent bays          |
| Turning radius (artic.)   | 12000-13500 mm   | Inside radius                      |

### 15.2 垃圾存储预留

| 建筑类型 | 预留量 | 备注 |
|----------------------|--------------------------|---------------------------------|
| Office               | 10-15 L per person/week  | 3-5 bin types (recycling)       |
| Residential          | 60-100 L per unit/week   | Based on household size         |
| Retail               | 30-50 L per 100m2/week   | Cardboard dominant              |
| Restaurant           | 100-200 L per 100m2/week | Food waste + recycling          |
| Hotel                | 50-80 L per room/week    | Housekeeping + F&B              |

Bin store area: typically 5-15 m2 per 1000 m2 GFA, accessible to collection vehicles.

### 15.3 配送与服务车辆轨迹

| 车辆类型 | 长度（m） | 宽度（m） | 高度（m） | 转弯直径（m） |
|------------------------|-----------|-----------|------------|---------------------|
| Transit van            | 5.5-6.0   | 2.0       | 2.5        | 11.0-12.0           |
| 7.5t rigid truck       | 7.5-8.0   | 2.3       | 3.2        | 14.0-15.0           |
| 18t rigid truck        | 9.0-10.0  | 2.5       | 3.5        | 17.0-18.0           |
| Articulated truck (UK) | 16.5      | 2.55      | 4.0        | 25.0-28.0           |
| Articulated truck (US) | 19.8      | 2.6       | 4.1        | 28.0-32.0           |
| Fire appliance         | 8.5-10.0  | 2.5       | 3.5        | 17.0-19.0           |
| Refuse vehicle         | 10.0-11.0 | 2.5       | 3.5        | 19.0-22.0           |
| Ambulance              | 6.0-7.0   | 2.2       | 2.7        | 13.0-14.0           |

---

## 16. 其他关键数值

### 16.1 结构活荷载（IBC 表 1607.1 / EN 1991-1-1）

| 用途 | IBC（kPa） | EN（kPa） | 备注 |
|---------------------------|-----------|----------|---------------------------|
| Residential               | 1.9       | 1.5-2.0  | Habitable rooms           |
| Office (general)          | 2.4       | 2.5-3.0  | Open plan and cellular    |
| Office (corridors above 1st)| 3.8    | 3.0-4.0  | Higher for assembly       |
| Retail (ground floor)     | 4.8       | 4.0-5.0  | Ground level heavier      |
| Assembly (fixed seats)    | 2.9       | 4.0-5.0  | EN more conservative      |
| Assembly (movable seats)  | 4.8       | 5.0-7.5  | Crowd loading possible    |
| Library reading rooms     | 2.9       | 2.5-4.0  | Shelving much higher      |
| Library stack rooms       | 7.2       | 6.5-7.5  | Very heavy               |
| Light storage             | 6.0       | 6.0-7.5  |                           |
| Heavy storage             | 12.0      | 10.0-15.0|                           |
| Parking (cars)            | 1.9       | 2.5      | Plus concentrated load    |
| Hospital wards            | 1.9       | 2.0-4.0  | Equipment additional      |
| Stairs and corridors      | 4.8       | 3.0-5.0  | Egress loading            |
| Roofs (ordinary)          | 1.0       | 0.6-1.0  | Plus snow/rain loads      |
| Balconies                 | 2.9       | 2.5-4.0  | Edge concentration        |

### 16.2 卫生器具配置（IPC / BS 6465-1:2006+A1:2009）

| 建筑类型 | 男厕 | 男小便器 | 女厕 | 备注（每 x 人） |
|------------------|----------|-------------|-----------|--------------------------|
| 办公（1–15 人） | 1 | 1 | 1 | 每 15 人 |
| 办公（16–30 人） | 1 | 1 | 2 | 男女分设 |
| 办公（31–45 人） | 2 | 1 | 2 | |
| 办公（46–60 人） | 2 | 2 | 3 | |
| 办公（61–80 人） | 2 | 2 | 3 | |
| 集会（100 人） | 1 | 2 | 3 | 女性比例较高 |
| 集会（250 人） | 2 | 4 | 8 | 活动临时增加 |
| 餐厅（100 人） | 1 | 2 | 3 | 另设无障碍设施 |

无障碍卫生间：每层每性别至少 1 个；每层至少设置 1 个男女通用无障碍卫生间。
行动障碍者隔间：每 3 个标准隔间设置 1 个。尺寸最小 800 × 1500 mm。
无障碍卫生间面积：最小 1500 × 2200 mm（BS 8300），或净空间 1525 × 1525 mm（ADA）。

### 16.3 关键热桥 Psi 值（W/mK）

| 节点 | 默认值 | 良好做法 | 最佳做法 |
|------------------------------|---------|---------------|---------------|
| 窗上钢过梁 | 0.50 | 0.15 | 0.04 |
| 窗台 | 0.16 | 0.08 | 0.02 |
| 窗侧 | 0.15 | 0.06 | 0.01 |
| 首层地面/墙体 | 0.32 | 0.16 | 0.05 |
| 外角 | 0.15 | 0.09 | 0.02 |
| 屋面/墙体 | 0.24 | 0.12 | 0.04 |
| 阳台（无保温） | 1.00 | 0.20 | 0.04 |
| 分户墙/外墙 | 0.20 | 0.08 | 0.02 |

Source: BRE IP 1/06; Accredited Construction Details (UK); PHI certification limits.

### 16.4 气密性目标

| 标准 | 目标值（50 Pa 下 m³/h/m²） | 等效 ACH50（典型） |
|-----------------------------|---------------------------|----------------------------|
| 英格兰建筑法规 2021 | 8.0 | 约 7–8 |
| 英格兰建筑法规（新建） | 5.0 | 约 4–5 |
| 英国最佳实践 | 3.0 | 约 2.5–3 |
| Passive House | 0.6 ACH50 | 0.6 |
| EnerPHit（改造） | 1.0 ACH50 | 1.0 |
| ASHRAE 90.1-2022 | 50 Pa 下 2.0 L/s/m² | 约 3–4 ACH50 等效值 |

---

## 17. 快速参考：人均面积基准

### 17.1 人均净可用面积（功能策划）

| 空间类型 | 最小值（m²/人） | 典型值（m²/人） | 备注 |
|-------------------------|-----------------|---------------------|-----------------------|
| 开放式办公室 | 6 | 8–10 | 工位+分摊交通面积 |
| 独立办公室 | 8 | 10–15 | 单人使用 |
| 主管办公室 | 15 | 20–30 | 含会议区域 |
| Hot desk / co-working   | 5               | 6-8                 | Higher density        |
| Classroom (fixed desks) | 1.5             | 2.0-2.5             | Including teaching wall|
| 大学阶梯教室 | 0.8 | 1.0–1.5 | 固定座位 |
| 图书馆（阅览） | 2.3 | 3.0–4.5 | 另加书架通道 |
| 餐厅就餐区 | 1.2 | 1.5–1.8 | 精致餐饮：2.0+ |
| 酒店客房（经济型） | 15 | 18–22 | 仅客房面积 |
| 酒店客房（中档） | 22 | 25–30 | 含卫生间 |
| 酒店客房（豪华型） | 35 | 40–60 | 套房：60–120 |
| 医院病房（单人） | 14 | 16–20 | HBN 指南 |
| 医院病房（多人） | 7 | 8–10 | 按每床位 |

### 17.2 Gross-to-Net Ratios

| 建筑类型 | 净面积/总面积比例 | 备注 |
|-------------------------|--------------------|----------------------------------|
| 办公（高效） | 80–85% | 核心筒至立面优化 |
| 办公（标准） | 75–80% | 典型商业建筑 |
| 住宅（公寓） | 75–85% | 走廊式与点式交通差异 |
| 酒店 | 55–65% | 后勤面积占比较大 |
| 医院 | 55–65% | 交通与机电面积较大 |
| 零售（百货） | 75–80% | 销售面积占比 |
| 学校 | 60–70% | 交通及附属空间 |
| 博物馆/画廊 | 55–65% | 展示与支持空间 |
| 实验室 | 55–65% | 服务和交通面积较大 |

---

*最后更新：2026 年 4 月。始终根据现行地方规范和具体项目要求进行核验。*
*主要来源：Neufert（第 5 版）、AGS（第 12 版）、IBC 2021、ACI 318-19、AISC 360-22、*
*ASHRAE 62.1-2022、ASHRAE 90.1-2022、BS/EN 标准、CIBSE 指南、Metric Handbook（第 6 版）、*
*ADA/ABA 标准、PCI Design Handbook、CLT Handbook、PTI Manual。*
#

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab AI建筑与室内设计总设计师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
