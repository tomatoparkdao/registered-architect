---
name: solar-geometry
description: 注册建筑师专业参考：solar-geometry。
license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
version: 1.0.0
author: OmniAiLab
developer: Mochiball
agent_created: true
---

# 太阳几何——深度参考

涵盖建筑设计中太阳位置计算、日照路径图、遮阳掩模构建、挑檐与遮阳翼尺寸设计及阴影分析方法的综合参考。

---

## 1. 太阳位置基础

### 1.1 关键定义

- **太阳高度角（α_s）：**太阳中心与水平面之间的角度，范围为 0°（地平线）至 90°（天顶）。
- **太阳方位角（γ_s）：**从正南测量的水平角（北半球约定）。正值表示南偏西，负值表示南偏东，范围为 −180° 至 +180°。
- **太阳天顶角（θ_z）：**高度角的余角，θ_z = 90° − α_s。
- **太阳赤纬（δ）：**太阳光线与赤道面的夹角，范围为 −23.45°（北半球冬至）至 +23.45°（北半球夏至）。
- **时角（ω）：**太阳相对于太阳正午的角位移，ω = 15° ×（太阳时 − 12）。上午为负，下午为正。
- **纬度（φ）：**场地地理纬度，北半球取正值。

### 1.2 太阳赤纬计算

**Cooper 方程（近似）：**
δ = 23.45° × sin(360° × (284 + n) / 365)
其中 n = 年内日序（1 月 1 日 = 1，12 月 31 日 = 365）。

**关键赤纬值：**
| Date | Day (n) | Declination (δ) |
|---|---|---|
| March 21 (Vernal Equinox) | 80 | 0.0° |
| June 21 (Summer Solstice) | 172 | +23.45° |
| September 21 (Autumnal Equinox) | 264 | 0.0° |
| December 21 (Winter Solstice) | 355 | -23.45° |
| August 1 (Thermal peak) | 213 | +17.9° |
| February 1 | 32 | -17.1° |

### 1.3 太阳高度角计算

**通用公式：**
sin(α_s) = sin(φ) × sin(δ) + cos(φ) × cos(δ) × cos(ω)

**太阳正午（ω = 0）时：**
α_noon = 90° - |φ - δ|

可简化为：
- Summer solstice noon: α = 90° - φ + 23.45°
- Winter solstice noon: α = 90° - φ - 23.45°
- Equinox noon: α = 90° - φ

### 1.4 太阳方位角计算

**通用公式：**
cos(γ_s) = [sin(α_s) × sin(φ) - sin(δ)] / [cos(α_s) × cos(φ)]

符号约定：ω < 0（上午）时 γ_s 为负（南偏东）；ω > 0（下午）时 γ_s 为正（南偏西）。

**春分/秋分时：**
- Sunrise azimuth = -90° (due east)
- Sunset azimuth = +90° (due west)
- At all latitudes between Arctic and Antarctic circles

**At Summer Solstice (Northern Hemisphere):**
日出方位角 = −arccos(−tan(φ) × tan(δ))——东偏北
日落方位角 = +arccos(−tan(φ) × tan(δ))——西偏北

### 1.5 太阳时与钟表时间

**太阳时：**依据太阳实际位置确定，太阳正午 = 太阳位于正南（北半球）。

**换算：**
太阳时 = 钟表时间 + 均时差（EOT）+ 经度修正 − 夏令时修正

**均时差（EOT）：**用于修正地球椭圆轨道和地轴倾角的影响。
EOT（分钟）= 9.87 × sin(2B) − 7.53 × cos(B) − 1.5 × sin(B)
where B = 360° × (n - 81) / 364

**EOT Key Values:**
| Date | EOT (minutes) |
|---|---|
| Feb 12 | -14.3 (clock ahead of sun) |
| May 15 | +3.8 |
| Jul 26 | -6.5 |
| Nov 3 | +16.4 (sun ahead of clock) |
| Apr 15 / Sep 1 | ~0 |

**经度修正：**
4 minutes per degree of longitude difference from standard meridian.
修正值 = 4 ×（L_standard − L_local）分钟
where L_standard = time zone standard meridian (e.g., 0° for GMT, 75°W for EST)

**示例：**纽约（74°W，EST 标准经线 75°W），6 月 21 日：
- Longitude correction = 4 × (75 - 74) = +4 minutes
- EOT ≈ -1.5 minutes
- Solar noon = 12:00 + 0:04 - 0:01.5 - 1:00 (DST) = 11:02:30 AM EDT

---

## 2. 日照路径图

### 2.1 立体投影日照路径图

使用立体投影将太阳路径投影到水平面，是建筑遮阳分析中最常见的图表类型。

**图表读取：**
- Concentric circles = altitude angles (outermost = 0°/horizon, center = 90°/zenith)
- Radial lines = azimuth angles (top = north, bottom = south for NH; reversed for SH)
- Curved lines (date lines) = sun paths for specific dates (typically monthly or solstice/equinox)
- Vertical hour lines = solar time hours

**构建方法：**
1. Calculate solar altitude and azimuth for each hour of each representative date
2. Plot altitude as radial distance: r = R × cos(α) / (1 + sin(α)) for stereographic, or r = R × (90 - α) / 90 for equidistant
3. Plot azimuth as angular position from south
4. Connect points of same date for sun path curves
5. Connect points of same hour for hour lines

### 2.2 等距投影日照路径图

高度角采用线性映射（每一度对应相同径向距离），比立体投影简单但几何精度较低，常用于教学和软件工具。

### 2.3 圆柱投影日照路径图

方位角位于水平轴（−180° 至 +180°），高度角位于垂直轴（0° 至 90°），形成矩形图。适合读取遮阳掩模叠加图，Ecotect 和 Climate Consultant 均采用此类图表。

---

## 3. 主要纬度的设计太阳角

### 3.1 赤道（纬度 0°）

| 日期 | 正午高度角 | 日出/日落方位角 | 昼长 |
|---|---|---|---|
| 春分/秋分（3月/9月21日） | 90.0° | ±90°（东/西） | 12h 00m |
| 夏至 | 66.6° | 东/西偏北±23.5° | 12h 00m |
| 冬至 | 66.6° | 东/西偏南±23.5° | 12h 00m |

**特征：**春分和秋分时太阳直射头顶。两个至日的正午高度相等且较低。太阳始终较高，所有立面均需水平遮阳；全年昼长几乎相等。

### 3.2 纬度 15°（热带——孟买、墨西哥城、达喀尔）

| 日期 | 正午高度角 | 日出/日落方位角 | 昼长 |
|---|---|---|---|
| 春分/秋分 | 75.0° | ±90° | 12h 07m |
| 夏至 | 81.6°（太阳略偏北） | ±113° | 13h 12m |
| 冬至 | 51.6° | ±67° | 10h 54m |

**特征：**5 月和 7 月太阳经过头顶（赤纬 = +15°）。夏季高度角很高，冬季适中；主要过热期为 3–10 月。

### 3.3 纬度 30°（亚热带——开罗、休斯敦、上海、新德里）

| 日期 | 正午高度角 | 日出/日落方位角 | 昼长 |
|---|---|---|---|
| 春分/秋分 | 60.0° | ±90° | 12h 09m |
| 夏至 | 83.5° | ±119° | 14h 04m |
| 冬至 | 36.6° | ±61° | 10h 04m |

**特征：**夏季太阳高度高，南立面水平挑檐有效；冬季低太阳提供有益得热。东西立面全年均较难遮阳；昼长季节变化明显。

### 3.4 纬度 45°（温带——米兰、蒙特利尔、札幌、基督城）

| 日期 | 正午高度角 | 日出/日落方位角 | 昼长 |
|---|---|---|---|
| 春分/秋分 | 45.0° | ±90° | 12h 12m |
| 夏至 | 68.5° | ±126° | 15h 37m |
| 冬至 | 21.6° | ±54° | 8h 46m |

**特征：**太阳高度角范围大（47°）。南向挑檐具有中等效果，但需应对较宽角度范围。冬季低太阳可深入室内，有利于被动太阳能供暖；夏季昼长、冬季昼短，夏季东西向遮阳至关重要。

### 3.5 纬度 60°（亚寒带——赫尔辛基、安克雷奇、奥斯陆、圣彼得堡）

| 日期 | 正午高度角 | 日出/日落方位角 | 昼长 |
|---|---|---|---|
| 春分/秋分 | 30.0° | ±90° | 12h 17m |
| 夏至 | 53.5° | ±140° | 18h 52m |
| 冬至 | 6.6° | ±40° | 5h 33m |

**特征：**太阳从不升得很高，最高仅 53.5°；冬季太阳刚刚越过地平线。水平挑檐效果很小（太阳始终处于中低角度），需要垂直翼片或组合遮阳。冬季最大化日照是主要挑战；夏季昼长，至日时接近 19 小时日照。

---

## 4. 遮阳装置设计

### 4.1 挑檐尺寸计算公式

对于窗上方的水平挑檐：

**所需挑檐深度（D）：**
D = H_sill / tan(α_cutoff)

其中：
- H_sill = 挑檐底部至窗台的垂直距离
- α_cutoff = 希望实现完全遮阳时的太阳高度角

**Alternative formulation using window height:**
D = (H_overhang - H_sill_above_ground) / tan(α_cutoff)

**For partial shading (shade only upper portion):**
D = H_shade / tan(α_cutoff)
where H_shade = height of window portion to be shaded

### 4.2 按纬度确定挑檐深度——南向窗（北半球）

设计条件：夏至正午完全遮阳。窗高 1.8 m，挑檐位于窗顶。

| Latitude | Solstice Noon Alt. | Required D (m) | D/H Ratio |
|---|---|---|---|
| 20° | 86.6° | 0.11 | 0.06 |
| 25° | 88.5° | 0.05 | 0.03 |
| 30° | 83.5° | 0.20 | 0.11 |
| 35° | 78.5° | 0.36 | 0.20 |
| 40° | 73.5° | 0.54 | 0.30 |
| 45° | 68.5° | 0.71 | 0.39 |
| 50° | 63.5° | 0.89 | 0.50 |
| 55° | 58.5° | 1.10 | 0.61 |
| 60° | 53.5° | 1.33 | 0.74 |

**Note:** At latitudes 20-25°, the near-vertical sun requires minimal south-facing overhang, but east/west facades need deep protection. At latitudes > 50°, south-facing overhangs become very deep and may be impractical — combined strategies needed.

### 4.3 非南向朝向的挑檐尺寸

南向挑檐有效，因为面向南立面时太阳高度较高。东西立面太阳高度低且斜射，单独采用水平挑檐效果有限。

**East/West Facade Shading Strategy:**
- Vertical fins perpendicular to facade
- Fin depth D_fin = S × tan(θ_cutoff) where S = fin spacing, θ_cutoff = cutoff azimuth angle from facade normal
- Egg-crate (combined horizontal + vertical) for comprehensive protection
- Deep reveals or recessed windows (effective recess = 300-600 mm)

**Southeast/Southwest Facades:**
- Angled vertical fins (rotated 15-30° toward south)
- Combined horizontal overhang + angled vertical fins
- Exterior venetian blinds with automated angle adjustment

### 4.4 阴影长度与面积计算

**Shadow Length of Vertical Object:**
L_shadow = H_object / tan(α_s)

其中 L_shadow = 水平地面上的阴影长度；H_object = 物体高度；α_s = 太阳高度角。

**Shadow Direction:** Shadow falls directly opposite the solar azimuth (azimuth + 180°).

**Shadow of Horizontal Overhang on Vertical Wall:**
挑檐下方的垂直阴影落差 = D × tan(α_profile)

其中：
α_profile = profile angle = arctan(tan(α_s) / cos(γ_wall))
γ_wall = azimuth angle between sun and wall normal

**Profile Angle:** The apparent solar altitude when viewed in the plane perpendicular to the wall surface. Critical for overhang design because it accounts for oblique sun angles.

### 4.5 遮阳系数计算

**Shading fraction (SF)** of a horizontal overhang on a vertical window at a given time:

若剖面角 > 截止角：SF = 1.0（完全遮阳）
若剖面角 < 0：SF = 0.0（太阳位于墙体背后）
否则：SF = D × tan(α_profile) / H_window

其中 H_window = 挑檐下方的窗高。

**Annual shading fraction:** Integrate hourly SF values over occupied hours weighted by incident solar radiation.

---

## 5. 遮阳掩模构建

### 5.1 目的

遮阳掩模（或阴影角量角器叠图）叠加在日照路径图上时，可显示遮阳装置阻挡的天空角度范围。如果太阳路径落在遮蔽区域内，则该时刻窗户处于遮阳状态。

### 5.2 水平挑檐掩模

水平挑檐产生**弧段掩模**——横跨日照路径图上部的弯曲带状区域。

**Construction:**
1. Calculate the profile cutoff angle: β = arctan(H_sill / D_overhang)
2. On the sun path diagram, draw a horizontal line at altitude = β across the relevant azimuth range
3. The area above this line (higher altitudes) represents times when the window is shaded

**Width of mask:** Determined by the lateral extent of the overhang. If overhang extends infinitely, mask spans full azimuth range. If finite width, mask is bounded by azimuth angles defined by the overhang edges.

### 5.3 垂直翼片掩模

垂直翼片产生**径向掩模**——从中心向外辐射的楔形扇区。

**Construction:**
1. Calculate the horizontal cutoff angle: η = arctan(S_gap / D_fin)
   where S_gap = clear distance between fins, D_fin = fin depth
2. On sun path diagram, draw radial lines at azimuth = ±η from the facade normal
3. The area outside these radial lines (more oblique angles) represents shaded times

### 5.4 格栅式掩模

弧段（挑檐）与径向（翼片）掩模的组合，遮蔽区域为两者的交集。

### 5.5 遮阳分析软件工具

- **Ladybug Tools (Grasshopper):** SunPath, ShadingMask, and SunlightHours components
- **Climate Consultant:** Built-in sun path with shading mask overlay
- **Ecotect (legacy):** Interactive shading mask generation
- **Sefaira:** Real-time facade shading analysis
- **Autodesk Revit:** Solar analysis and shadow studies
- **SketchUp + SunHours:** Shadow range animations
- **DIVA-for-Rhino:** Radiance-based shading analysis

---

## 6. Equinox and Solstice Analysis Methods

### 6.1 阴影研究流程

标准建筑阴影研究在关键日期和时刻检查建筑体量及遮阳影响。

**Standard Dates:**
1. **Winter Solstice (December 21 NH):** Longest shadows; worst-case for solar access to adjacent properties; critical for rights-to-light analysis
2. **Summer Solstice (June 21 NH):** Shortest shadows; worst-case for overheating; maximum solar altitude
3. **Equinoxes (March 21, September 21):** Intermediate condition; sun rises due east, sets due west; symmetric shadow pattern
4. **August 1:** Thermal peak date (4-6 weeks after solstice due to thermal lag); often more relevant than solstice for overheating design

**Standard Times:**
- 9 AM, 12 PM (noon), 3 PM solar time (minimum three-point analysis)
- Full hourly analysis from sunrise to sunset for detailed studies

### 6.2 采光权与日照可达性

**UK Rights to Light (Waldram Diagram Method):**
- Statutory right under Prescription Act 1832 (20+ years of uninterrupted daylight)
- Test: ≥ 50% of room area must receive DF ≥ 0.2% (the "grumble line")
- Waldram diagram maps sky visibility from each point on the working plane
- Obstruction that reduces adequately lit area below 50% constitutes actionable nuisance

**Vertical Sky Component (VSC):**
- Percentage of unobstructed sky hemisphere visible from center of a window
- BRE Guide target: VSC ≥ 27% (equivalent to DF ≈ 2% at 1 m from window)
- New development should not reduce VSC of existing windows below 0.8 × former value

**Solar Access for Outdoor Spaces:**
- BRE Guide: at least 50% of amenity area should receive ≥ 2 hours of direct sunlight on March 21
- PAN (Scotland): living rooms should receive ≥ 3 hours of sunlight on equinox

### 6.3 太阳包络法

由 Ralph Knowles（USC）发展，用于定义场地上不会超过规定限值遮挡相邻物业的最大可建体量。

**Construction:**
1. Define solar access criteria (e.g., 4 hours of direct sun on adjacent facades on winter solstice)
2. Calculate shadow lengths and directions at the critical times
3. Draw inward from site boundaries using shadow angles as cutting planes
4. The resulting volumetric "envelope" is the maximum development form

**Applications:** Zoning regulations in solar-access-protected districts; passive solar community design; daylighting master plans.

### 6.4 日照仪与数字阴影研究

**Physical Heliodon:** Adjustable light source + tilting table that simulates sun position for any latitude, date, and time on architectural models. Used for qualitative light quality assessment.

**Digital Tools:**
- Revit/SketchUp shadow animation (date/time slider)
- Ladybug SunPath + Radiation analysis (quantitative)
- Grasshopper + Radiance (high-accuracy)
- Solar access maps (cumulative hours of direct sun per point on ground/facades)

---

## 7. 太阳几何高级应用

### 7.1 立面朝向优化

**按朝向划分的年太阳辐射（纬度45°N，kWh/m²/年）：**

| 朝向 | 总辐射 | 直射（光束） | 漫射 |
|---|---|---|---|
| 水平（屋面） | 1,250 | 780 | 470 |
| 南（垂直） | 880 | 590 | 290 |
| 东（垂直） | 640 | 370 | 270 |
| 西（垂直） | 640 | 370 | 270 |
| 北（垂直） | 360 | 70 | 290 |
| 向南倾斜45° | 1,180 | 810 | 370 |

**最佳建筑朝向：**长轴宜位于东西向±15°以内，以最大化南向面积并最小化东西向暴露。偏差至±30°时仍可接受，但性能损失约5-10%。

### 7.2 被动太阳能供暖窗尺寸

**被动太阳能供暖的南向玻璃面积（纬度45°N）：**
- 南向玻璃每m²净太阳得热：200-350 kWh/年（低辐射双层、氩气）
- 南向玻璃每m²热损失：80-150 kWh/年（取决于U值和气候）
- 净收益：100-250 kWh/m²/年
- 最佳南向玻璃比例：南墙面积的25-50%（超过40%后因过热风险收益递减）

### 7.3 光伏板朝向

**年发电量最大化的最佳倾角：**固定光伏板约等于当地纬度（±5°）。
- 纬度30°：最佳倾角25-35°
- 纬度45°：最佳倾角35-45°
- 纬度60°：最佳倾角50-60°

**方位角：**北半球正南，南半球正北。偏差±30°时年发电量损失<5%。东西向垂直板适合与早晚峰值需求匹配。

### 7.4 日晷与影钟原理

可根据阴影位置读取太阳时：
- **Hour angle to time:** Each 15° of hour angle = 1 hour. Shadow rotates clockwise (NH) at 15°/hour.
- **Analemma:** Figure-8 pattern traced by sun at same clock time over the year; caused by combined effects of orbital eccentricity and axial tilt.
- **Architectural sundials:** Can be integrated into building facades and ground planes as functional art (e.g., sundial gardens, gnomon walls).

---

## 8. 公式速查

| 参数 | 公式 |
|---|---|
| 太阳赤纬 | δ = 23.45° × sin(360° × (284+n)/365) |
| 太阳高度角（通用） | sin(α) = sin(φ)sin(δ) + cos(φ)cos(δ)cos(ω) |
| 正午太阳高度角 | α_noon = 90° - \|φ - δ\| |
| Hour angle | ω = 15° × (solar time - 12) |
| Solar azimuth | cos(γ) = [sin(α)sin(φ) - sin(δ)] / [cos(α)cos(φ)] |
| Overhang depth | D = H / tan(α_cutoff) |
| Shadow length | L = H / tan(α_s) |
| Profile angle | α_profile = arctan[tan(α_s) / cos(γ_wall)] |
| Equation of Time | EOT = 9.87sin(2B) - 7.53cos(B) - 1.5sin(B) |
| Day length (hours) | DL = (2/15) × arccos[-tan(φ) × tan(δ)] |
| Sunrise/set hour angle | ω_s = ±arccos[-tan(φ) × tan(δ)] |
| Sunrise/set azimuth | γ_s = ±arccos[sin(δ)/cos(φ)] (at equinox: ±90°) |
| Solar time correction | Solar time = clock time + EOT + 4(L_std - L_loc) - DST |
#

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab AI建筑与室内设计总设计师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
