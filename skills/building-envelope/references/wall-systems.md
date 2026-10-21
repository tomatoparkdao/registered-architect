---
name: wall-systems
description: 注册建筑师专业参考：wall-systems。
version: 1.1.0
license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
author: OmniAiLab
developer: Mochiball
agent_created: true
开源仓库: https://github.com/tomatoparkdao/registered-architect
---

# 墙体系统——综合参考

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。

## 1. 分层构造与性能数据

### 1.1 传统砌体夹腔墙（砖/砌块）

**构造层次（由外向内）：**

| 层次 | 材料 | 厚度（mm） | 导热系数（W/mK） | R 值（m²K/W） |
|---|---|---|---|---|
| 1 | 饰面砖 | 102.5 | 0.77 | 0.13 |
| 2 | 净空夹腔（通风） | 50 | — | 0.18 |
| 3 | 矿棉保温（满填） | 150 | 0.034 | 4.41 |
| 4 | 密实混凝土砌块 | 140 | 1.13 | 0.12 |
| 5 | 轻质抹灰 | 13 | 0.18 | 0.07 |
| — | 内表面热阻 | — | — | 0.13 |
| — | 外表面热阻 | — | — | 0.04 |
| **Total** | | **455.5** | | **5.08** |

**U 值 = 1/5.08 = 0.197 W/m²K**

达到 U ≤ 0.18：将保温层增加至 175 mm（R = 5.15，U = 0.174）。

**耐火等级：**REI 120（整体不燃）
**隔声：**Rw 50–55 dB（带 50 mm 夹腔）
**隐含碳：**85–120 kgCO2e/m²
**成本：**$150–250/m²（含安装）

### 1.2 局部填充 + PIR 的砌体夹腔墙

**构造层次：**

| 层次 | 材料 | 厚度（mm） | 导热系数（W/mK） | R 值（m²K/W） |
|---|---|---|---|---|
| 1 | 饰面砖 | 102.5 | 0.77 | 0.13 |
| 2 | 剩余通风夹腔 | 50 | — | 0.18 |
| 3 | PIR 保温板（覆箔） | 100 | 0.022 | 4.55 |
| 4 | 加气混凝土砌块（保温型） | 140 | 0.11 | 1.27 |
| 5 | 点粘石膏板 | 12.5 | 0.25 | 0.05 |
| — | Rsi + Rse | — | — | 0.17 |
| **Total** | | **405** | | **6.35** |

**U 值 = 1/6.35 = 0.157 W/m²K**（满足并优于 Part L 2021）

**耐火等级：**REI 120（砌体后方 PIR 防火等级为 B-s1,d0）
**隔声：**Rw 52–56 dB
**隐含碳：**75–105 kgCO2e/m²（PIR 每千克隐含碳高于矿棉，但所需厚度更小）
**成本：**$170–280/m²

### 1.3 保温混凝土模板（ICF）

**构造层次：**

| 层次 | 材料 | 厚度（mm） | 导热系数（W/mK） | R 值（m²K/W） |
|---|---|---|---|---|
| 1 | 网格抹灰层（外侧） | 10 | 0.50 | 0.02 |
| 2 | EPS 模板（外叶） | 75 | 0.034 | 2.21 |
| 3 | 钢筋混凝土芯 | 200 | 1.63 | 0.12 |
| 4 | EPS 模板（内叶） | 75 | 0.034 | 2.21 |
| 5 | 石膏板 | 12.5 | 0.25 | 0.05 |
| — | Rsi + Rse | — | — | 0.17 |
| **Total** | | **372.5** | | **4.78** |

**U 值 = 1/4.78 = 0.209 W/m²K**

达到 U ≤ 0.18：两侧均采用 100 mm EPS（R = 5.86，U = 0.17）。

**耐火等级：**REI 120–240（混凝土芯；EPS 由抹灰 + 石膏板保护）
**隔声：**Rw 52–58 dB（200 mm 混凝土质量）
**隐含碳：**130–180 kgCO2e/m²
**成本：**$180–300/m²

### 1.4 木框架（平台框架）——标准型

**构造层次：**

| 层次 | 材料 | 厚度（mm） | 导热系数（W/mK） | R 值（m²K/W） |
|---|---|---|---|---|
| 1 | 薄砖/木饰面 | 20 | — | 0.10 |
| 2 | 通风夹腔 | 25 | — | — |
| 3 | 透汽膜 | — | — | — |
| 4 | OSB 覆板 | 9 | 0.13 | 0.07 |
| 5 | Timber studs 140 x 38 @ 600 crs with mineral wool between | 140 | MW: 0.035 / Timber: 0.13 | Combined: 3.49 (with bridging fraction 15%) |
| 6 | VCL（聚乙烯） | — | — | — |
| 7 | 设备空腔 + 保温 | 25 | 0.035 | 0.71 |
| 8 | 石膏板 | 12.5 | 0.25 | 0.05 |
| — | Rsi + Rse | — | — | 0.17 |
| **Total** | | **~232** | | **4.59** |

**热桥计算（平行路径法）：**
- 立柱间距 600 mm、宽 38 mm：热桥比例 = 38/600 = 6.3%（立柱）+ 约 8%（横撑、顶梁/底梁）≈ 15%
- R_保温 = 140/0.035 = 4.00；R_木材 = 140/0.13 = 1.08
- R_组合 = 1 / (0.15/1.08 + 0.85/4.00) = 3.49

**U 值 = 1/4.59 = 0.218 W/m²K**

达到 U ≤ 0.18：增加 50 mm 外部矿棉（R = 1.43，总 R = 6.02，U = 0.166）。

**耐火等级：**REI 30（单层石膏板）；REI 60（双层石膏板，总厚 25 mm）
**隔声：**Rw 40–48 dB（单层石膏板）；50+ dB（弹性龙骨 + 双层石膏板）
**隐含碳：**25–50 kgCO2e/m²
**成本：**$120–200/m²

### 1.5 木框架（平台框架）——增强型（被动房）

**构造层次：**

| 层次 | 材料 | 厚度（mm） | 导热系数（W/mK） | R 值（m²K/W） |
|---|---|---|---|---|
| 1 | 木材雨屏覆层 | 20 | — | 0.10 |
| 2 | 通风空腔 | 40 | — | — |
| 3 | 透湿防水膜 | — | — | — |
| 4 | 木纤维保温（外侧） | 100 | 0.038 | 2.63 |
| 5 | OSB护面板（气密层） | 15 | 0.13 | 0.12 |
| 6 | 240 mm工字木搁栅，空腔填纤维素 | 240 | 0.040 | 5.45（桥接8%） |
| 7 | 智能VCL（Intello Plus） | — | — | — |
| 8 | 设备空腔+保温 | 50 | 0.035 | 1.43 |
| 9 | 石膏板 | 12.5 | 0.25 | 0.05 |
| — | Rsi + Rse | — | — | 0.17 |
| **Total** | | **~478** | | **9.95** |

**U 值 = 1/9.95 = 0.100 W/m²K**（符合被动房标准）

**耐火等级：**REI 60（采用 2 × 12.5 mm 防火石膏板 + 喷淋）
**隔声：**Rw 52–58 dB（深夹腔中的高密度纤维素 + 弹性连接）
**隐含碳：**15–35 kgCO2e/m²（纤维素 + 木材组合可能实现负碳）
**成本：**$200–350/m²

### 1.6 填充并设外保温的钢框架

**构造层次：**

| 层次 | 材料 | 厚度（mm） | 导热系数（W/mK） | R 值（m²K/W） |
|---|---|---|---|---|
| 1 | Metal cladding panel | 1.5 | 50 | ~0 |
| 2 | Ventilated cavity | 25 | — | — |
| 3 | Breather membrane | — | — | — |
| 4 | Mineral wool (external, continuous) | 100 | 0.035 | 2.86 |
| 5 | Steel studs 150 mm with mineral wool between | 150 | MW: 0.035 / Steel: 50 | Combined: 1.95 (bridging 1% by area but high conductivity) |
| 6 | VCL | — | — | — |
| 7 | Plasterboard (2 layers) | 25 | 0.25 | 0.10 |
| — | Rsi + Rse | — | — | 0.17 |
| **Total** | | **~302** | | **5.08** |

**Note:** Steel studs create severe thermal bridging. The parallel path method underestimates this; use ISO 6946 combined method or 2D modeling (THERM). Effective U-value is typically 0.30–0.50 W/m²K without external insulation. The 100 mm external insulation (continuous, no bridging) brings effective U-value to ~0.20 W/m²K.

**耐火等级：**REI 60–120（不燃框架 + 防火板材）
**隔声：**Rw 45–52 dB
**隐含碳：**65–100 kgCO2e/m²
**成本：**$150–250/m²

### 1.7 结构保温板（SIP）

**构造层次：**

| 层次 | 材料 | 厚度（mm） | 导热系数（W/mK） | R 值（m²K/W） |
|---|---|---|---|---|
| 1 | External render / cladding | 15–20 | — | 0.08 |
| 2 | Breather membrane | — | — | — |
| 3 | OSB facing | 11 | 0.13 | 0.08 |
| 4 | PUR/EPS core | 167 | 0.023 (PUR) / 0.034 (EPS) | PUR: 7.26 / EPS: 4.91 |
| 5 | OSB facing | 11 | 0.13 | 0.08 |
| 6 | VCL (integral at OSB joint) | — | — | — |
| 7 | Plasterboard | 12.5 | 0.25 | 0.05 |
| — | Rsi + Rse | — | — | 0.17 |
| **Total (PUR)** | | **~217** | | **7.72** |
| **Total (EPS)** | | **~217** | | **5.37** |

**U 值：**PUR = 0.130 W/m²K；EPS = 0.186 W/m²K

**耐火等级：**REI 30（OSB 面板）；增加防火内衬后 REI 60
**隔声：**Rw 32–38 dB（轻质构造——需增加质量）
**隐含碳：**PUR 45–65 kgCO2e/m²；EPS 30–50 kgCO2e/m²
**成本：**$140–230/m²

### 1.8 带外保温的 CLT

**构造层次：**

| 层次 | 材料 | 厚度（mm） | 导热系数（W/mK） | R 值（m²K/W） |
|---|---|---|---|---|
| 1 | Rainscreen cladding (terracotta) | 30 | — | — |
| 2 | Ventilated cavity | 40 | — | — |
| 3 | Breather membrane | — | — | — |
| 4 | Wood fibre insulation | 160 | 0.038 | 4.21 |
| 5 | CLT panel (5-layer) | 140 | 0.12 | 1.17 |
| 6 | Internal finish (exposed CLT) | — | — | — |
| — | Rsi + Rse | — | — | 0.17 |
| **Total** | | **~370** | | **5.55** |

**U 值 = 1/5.55 = 0.180 W/m²K**

当 U ≤ 0.15 时：将木纤维保温增加至 200 mm（R = 5.26，总 R = 6.60，U = 0.152）。

**耐火等级：**CLT 碳化速率为 0.65 mm/min。140 mm 板材碳化后剩余结构承载能力约 90 分钟（从所有暴露面扣除碳化深度计算）。增加防火石膏板可进一步保护。
**隔声：**Rw 38–44 dB（仅 CLT）；采用室内弹性连接 + 石膏板时为 52–58 dB
**隐含碳：**−10 至 +30 kgCO2e/m²（CLT 约封存 165 kgCO2/m³；木纤维也可封存碳）
**成本：**$220–380/m²

### 1.9 预制混凝土夹芯板

**构造层次：**

| 层次 | 材料 | 厚度（mm） | 导热系数（W/mK） | R 值（m²K/W） |
|---|---|---|---|---|
| 1 | Precast concrete (external leaf) | 75 | 1.63 | 0.05 |
| 2 | XPS insulation | 120 | 0.034 | 3.53 |
| 3 | Precast concrete (internal leaf) | 150 | 1.63 | 0.09 |
| 4 | Paint / plaster skim | 3 | — | 0.02 |
| — | Rsi + Rse | — | — | 0.17 |
| **Total** | | **~348** | | **3.86** |

**U 值 = 1/3.86 = 0.259 W/m²K**

当 U ≤ 0.18 时：将 XPS 增加至 180 mm（R = 5.29，总 R = 5.62，U = 0.178）。

**热桥说明：**不锈钢或复合材料抗剪连接件连接内外叶墙，每个连接件都会形成点热桥。Thermomass 或 Schock Combar（GFRP）连接件可降低影响；对 U 值的典型影响为：不锈钢 +0.01–0.03 W/m²K，GFRP +0.001–0.005 W/m²K。

**耐火等级：**REI 120–240（不燃）
**隔声：**Rw 52–58 dB
**隐含碳：**110–170 kgCO2e/m²
**成本：**$220–420/m²

### 1.10 单元式双层玻璃幕墙（透明区）

**构造层次：**

| 层次 | 材料 | 厚度（mm） | 性能 |
|---|---|---|---|
| 1 | Outer glass: 8 mm toughened + low-e coating | 8 | SHGC: 0.30; VLT: 60% |
| 2 | Argon-filled cavity | 16 | Sealed IGU |
| 3 | Inner glass: 6.8 mm laminated (6 + 0.76 PVB) | 6.8 | Safety; acoustic benefit |
| 4 | Aluminum frame with polyamide thermal break | — | 30 mm break depth |
| — | | **~130** total depth | |

**U 值（玻璃中心）：**1.1 W/m²K
**U 值（整块板，含框架）：**1.6–2.0 W/m²K（框架比例约 20%）
**SHGC:** 0.25–0.35
**VLT:** 55–65%
**隔声：**Rw 34–38 dB（夹胶内片改善低频隔声）
**隐含碳：**100–150 kgCO2e/m²
**成本：**$500–900/m²

### 1.11 三层玻璃幕墙（高性能）

**构造层次：**

| 层次 | 材料 | 厚度（mm） | 性能 |
|---|---|---|---|
| 1 | Outer glass: 6 mm toughened + solar control low-e | 6 | Surface 2 coating |
| 2 | Argon cavity | 14 | |
| 3 | Middle glass: 4 mm float + low-e | 4 | Surface 5 coating |
| 4 | Argon cavity | 14 | |
| 5 | Inner glass: 6.8 mm laminated | 6.8 | Safety glass |
| 6 | Timber-aluminum frame | — | Timber inner, alu outer |
| — | | **~160** total depth | |

**U 值（玻璃中心）：**0.5–0.6 W/m²K
**U 值（整块板）：**0.8–1.1 W/m²K
**SHGC:** 0.20–0.35
**VLT:** 45–55%
**隔声：**Rw 38–44 dB
**隐含碳：**120–170 kgCO2e/m²（增加玻璃 + 框架）
**成本：**$700–1300/m²

### 1.12 雨屏——钢框架上的陶土板

**构造层次：**

| 层次 | 材料 | 厚度（mm） | 导热系数（W/mK） | R 值（m²K/W） |
|---|---|---|---|---|
| 1 | Terracotta panel | 30 | 1.00 | 0.03 |
| 2 | Ventilated cavity | 50 | — | — |
| 3 | Breather membrane | — | — | — |
| 4 | Mineral wool insulation (continuous) | 150 | 0.034 | 4.41 |
| 5 | Concrete/block backing wall | 200 | 1.13 | 0.18 |
| 6 | Plaster skim | 13 | 0.18 | 0.07 |
| — | Rsi + Rse | — | — | 0.17 |
| **Total** | | **~443** | | **4.86** |

**U 值 = 0.206 W/m²K**（将保温层增加至 180 mm 时 U = 0.174）

注：支架热桥增加约 0.02–0.04 W/m²K；采用隔热支架时增加 +0.005–0.01 W/m²K。

**耐火等级：**全系统不燃（陶土、矿棉、混凝土）。满足高度超过 18 m 建筑的 BS 8414 / BR 135。
**隔声：**Rw 52–60 dB（混凝土基层质量 + 保温层）
**隐含碳：**90–140 kgCO2e/m²
**成本：**$300–500/m²

### 1.13 雨屏——木框架上的纤维水泥板

**构造层次：**

| 层次 | 材料 | 厚度（mm） | 导热系数（W/mK） | R 值（m²K/W） |
|---|---|---|---|---|
| 1 | Fiber cement panel (Equitone, Marley Eternit) | 12 | 0.50 | 0.02 |
| 2 | Ventilated cavity | 40 | — | — |
| 3 | Breather membrane | — | — | — |
| 4 | Wood fiber insulation | 80 | 0.038 | 2.11 |
| 5 | OSB sheathing | 9 | 0.13 | 0.07 |
| 6 | Timber studs 140 mm with cellulose | 140 | 0.040 | 3.15 (8% bridging) |
| 7 | Smart VCL | — | — | — |
| 8 | Service void | 25 | 0.035 | 0.71 |
| 9 | Plasterboard | 12.5 | 0.25 | 0.05 |
| — | Rsi + Rse | — | — | 0.17 |
| **Total** | | **~319** | | **6.28** |

**U 值 = 0.159 W/m²K**

**耐火等级：**纤维水泥为 A2-s1,d0；木纤维/纤维素为 B/C 类，高度超过 18 m 的建筑需进行消防工程设计，通常还需设置喷淋。
**隔声：**Rw 48–55 dB
**隐含碳：**20–45 kgCO2e/m²（纤维素 + 木材碳封存）
**成本：**$180–300/m²

### 1.14 ETICS（外墙外保温复合系统）/ EIFS

**构造层次：**

| 层次 | 材料 | 厚度（mm） | 导热系数（W/mK） | R 值（m²K/W） |
|---|---|---|---|---|
| 1 | Silicone render + mesh | 8 | 0.70 | 0.01 |
| 2 | EPS (expanded polystyrene) insulation | 200 | 0.031 | 6.45 |
| 3 | Adhesive + mechanical fixings | — | — | — |
| 4 | Concrete/block backing wall | 200 | 1.13 | 0.18 |
| 5 | Plaster skim | 13 | 0.18 | 0.07 |
| — | Rsi + Rse | — | — | 0.17 |
| **Total** | | **~421** | | **6.88** |

**U 值 = 0.145 W/m²K**

**耐火等级：**EPS 可燃（Euroclass E）。高度超过 18 m 的建筑应采用矿棉（A1/A2），或为 EPS 设置防火隔离带（每层及开口周边设置矿棉条）。许多国家现已要求高度超过 18 m 的建筑采用 A1/A2 保温材料。
**隔声：**Rw 48–55 dB（基层墙体质量）
**隐含碳：**70–110 kgCO2e/m²（EPS 方案）；80–120（矿棉方案）
**成本：**$120–220/m²（最经济的外保温方案）

### 1.15 双层表皮立面（通风式）

**构造层次：**

| 层次 | 材料 | 厚度（mm） | 性能 |
|---|---|---|---|
| 1 | Outer glass skin (single-glazed, toughened) | 10 | Weather protection, solar pre-heating |
| 2 | Ventilated cavity (with blinds) | 200–800 | Natural/mechanical ventilation; blinds for solar control |
| 3 | Inner glass skin (double/triple IGU) | 30–50 | Thermal insulation, acoustic |
| 4 | Aluminum/steel frame system | — | Supporting both skins |

**U 值（组合）：**0.8–1.5 W/m²K（内层表皮性能 + 夹腔效应）
**SHGC:** 0.10–0.30 (with blinds deployed)
**隔声：**Rw 42–52 dB（双层表皮 + 夹腔吸声）
**隐含碳：**150–250 kgCO2e/m²（两层完整玻璃表皮）
**成本：**$800–2000/m²

**优点：**隔声性能优异（适合噪声较大的城市场地）；高层建筑可实现自然通风；整合式遮阳受天气保护；具备夜间冷却潜力。
**缺点：**成本很高；维护复杂（需清洁夹腔）；夹腔通风不当时存在过热风险；增加结构荷载；隐含碳较高。

---

## 2. Fire Performance Summary

| Wall System | Achievable Rating | Combustibility | Notes |
|---|---|---|---|
| Masonry cavity | REI 120–240 | A1 throughout | Gold standard for fire |
| ICF | REI 120–240 | A1 (concrete) + EPS (E) | EPS protected by concrete/render |
| Timber frame | REI 30–60 | D/E (timber, OSB) | Fire lining dependent; sprinklers for tall |
| Steel frame | REI 60–120 | A1 (steel, boards) | Fire-rated boards required |
| SIPs | REI 30–60 | D (OSB) + E (EPS/PUR core) | Limited to low-rise without extra fire protection |
| CLT | REI 60–120 | D (timber) | Charring calculation per EN 1995-1-2 |
| Curtain wall | E30–EW60 (glass) | A1 (alu, glass) | Spandrel panel fire backing required |
| Rainscreen | REI 120+ | Varies by panel; backing wall governs | BS 8414 test for >18 m buildings |
| Precast concrete | REI 120–240 | A1 | Excellent inherent fire performance |
| ETICS | REI per backing wall | EPS=E, MW=A1 | Fire barriers at floors for >18 m |

---

## 3. Acoustic Performance Summary

| Wall System | Rw (dB) | Weak Point | Improvement Strategy |
|---|---|---|---|
| Masonry cavity (102.5 + 140 block) | 50–55 | Mortar joints, cavity ties | Acoustic ties, ensure full mortar |
| ICF (200 mm concrete) | 52–58 | Flanking through floor/ceiling | Resilient connections |
| Timber frame (single PB) | 40–48 | Low mass, flanking | Resilient bars, double PB, dense insulation |
| Steel frame | 42–50 | Steel stud flanking | Acoustic studs, double PB both sides |
| SIPs | 32–38 | Very low mass (lightweight panel) | Additional mass layer, resilient mount |
| CLT (140 mm) | 38–44 | Rigid panel, flanking | Resilient mount, suspended ceiling, floating floor |
| Curtain wall (double IGU) | 34–38 | Glass mass, frame seals | Laminated glass, thicker panes, asymmetric IGU |
| Rainscreen on concrete | 52–60 | Panel rattling in wind | Proper fixing, panel density |
| Precast sandwich | 52–58 | Shear connectors | GFRP connectors, acoustic mounts |

---

## 4. 隐含碳比较

| 墙体系统 | kgCO2e/m² | 碳评级 | 说明 |
|---|---|---|---|
| 木框架（标准） | 25–50 | 优秀 | 木材固碳可抵消排放 |
| 木框架（被动房） | 15–35 | 优秀 | 纤维素+木材最大化固碳 |
| CLT+木纤维 | -10至+30 | 卓越 | 可实现净负碳 |
| SIP（EPS） | 30–50 | 良好 | OSB+EPS |
| 砌体空腔墙（岩棉） | 85–120 | 中等 | 砖+砌块+水泥 |
| 钢框架 | 65–100 | 中等 | 再生钢含量有助于降低碳排放 |
| ICF | 130–180 | 较差 | 混凝土+EPS |
| 预制夹芯板 | 110–170 | 较差 | 以混凝土为主 |
| 双层幕墙 | 100–150 | 较差 | 以铝材为主 |
| 混凝土外保温系统（ETICS） | 70–120 | 中等 | 因保温类型而异 |
| 双层表皮立面 | 150–250 | 很差 | 双层玻璃+铝框 |

**基准（LETI《气候紧急设计指南》）：**
- 住宅目标：<400 kgCO2e/m² GIA（整栋建筑，结构+围护+饰面）
- 商业目标：<500 kgCO2e/m² GIA
- 围护结构通常占整栋建筑隐含碳的15–25%

---

## 5. 成本范围汇总（2024年价格，含安装，近似值）

| 墙体系统 | 低（$/m²） | 中（$/m²） | 高（$/m²） | 成本驱动因素 |
|---|---|---|---|---|
| 砌体ETICS | 120 | 170 | 220 | 抹灰饰面质量 |
| 木框架（标准） | 120 | 160 | 200 | 覆层类型 |
| 砌体空腔墙 | 150 | 200 | 250 | 砖类型、保温 |
| SIP | 140 | 185 | 230 | 板材规格 |
| 钢框架+填充墙 | 150 | 190 | 250 | 覆层+耐火等级 |
| ICF | 180 | 240 | 300 | 混凝土等级、高度 |
| 木框架（被动房） | 200 | 275 | 350 | 保温厚度、气密性 |
| 预制夹芯板 | 220 | 320 | 420 | 饰面、配筋 |
| CLT+外保温 | 220 | 300 | 380 | CLT等级、覆层 |
| 雨屏（纤维水泥） | 180 | 240 | 300 | 板材品牌、基层墙体 |
| 雨屏（陶土） | 300 | 400 | 500 | 板材规格、支架系统 |
| 雨屏（天然石材） | 400 | 550 | 700 | 石材类型、厚度 |
| 幕墙（明框、双层） | 400 | 550 | 700 | 玻璃规格、竖梃系统 |
| Curtain wall (unitized, double) | 500 | 750 | 900 | Factory finish, logistics |
| Curtain wall (triple) | 700 | 1000 | 1300 | Triple IGU, frame |
| Double-skin facade | 800 | 1400 | 2000 | Cavity depth, ventilation system |

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
