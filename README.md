<h1 align="center">OmniAiLab 全球注册建筑师</h1>

<p align="center">
  <b>面向全球注册建筑师的规范路由、设计核验与交付审查 Skill —— 先定辖区，再谈设计</b><br>
  29 个模块：18 项专业设计能力 ＋ 10 个司法辖区法规专题 ＋ 7 个计算器 ｜ 883 份参考文档 ｜ 约 113 万行专业资料<br>
  项目定位 → 法规路由 → 功能与体量 → 技术协调 → 性能验证 → 施工图交付 → 合规审查<br>
  规范只做路由与核验，不作审批结论 ｜ 零硬依赖可离线 ｜ 结构 / 消防 / 无障碍须当地持证人员复核签署
</p>

<p align="center">
  <a href="https://github.com/tomatoparkdao/registered-architect"><img src="https://img.shields.io/badge/%E7%89%88%E6%9C%AC-1.1.0-1f6feb?style=flat-square" alt="版本 1.1.0"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/%E8%AE%B8%E5%8F%AF-MIT-2ea043?style=flat-square" alt="许可 MIT"></a>
  <a href="https://www.omniailabx.com/"><img src="https://img.shields.io/badge/%E5%B9%B3%E5%8F%B0-OmniAiLab-8957e5?style=flat-square" alt="平台 OmniAiLab"></a>
  <img src="https://img.shields.io/badge/%E5%9C%B0%E5%8C%BA-10_%E4%B8%AA%E5%8F%B8%E6%B3%95%E8%BE%96%E5%8C%BA-0e8a16?style=flat-square" alt="10 个司法辖区">
  <img src="https://img.shields.io/badge/%E6%A8%A1%E5%9D%97-29_%E9%A1%B9-0969da?style=flat-square" alt="29 项模块">
  <img src="https://img.shields.io/badge/%E5%85%BC%E5%AE%B9-Codex_%7C_Claude_%7C_WorkBuddy_%7C_OmniAiLab-6f42c1?style=flat-square" alt="兼容 Codex / Claude / WorkBuddy / OmniAiLab">
</p>

<p align="center">
  <b>简体中文</b>　｜　<a href="README_EN.md">English</a>
</p>

> © OmniAiLab ｜ 开发者：Mochiball ｜ 平台：[omniailabx.com](https://www.omniailabx.com/)

这不是一个“生成方案”的创作工具，而是一个**会先问清辖区再下判断**的规范核验框架。它的第一动作不是画图，是确认项目在哪个国家、哪个城市、受哪一级强制性标准约束；确认不了就先列缺失项，而不是套一个别国的数值继续往下算。

同一个体量方案，放在迪拜、慕尼黑和新加坡要过的审查完全不同：迪拜看民防预审与外墙覆层，慕尼黑看 Brandschutznachweis 与州级 LBO，新加坡看 SCDF Fire Code 与 ETTV/RTTV。本技能把这套差异做成**可路由的结构**——先把辖区的监管体系、主管部门和规范层级摆清楚，再谈方案、技术、消防、无障碍、节能与施工图。

**它是注册建筑师手里的规范地图和交叉校核清单，不是替代注册建筑师的人。**

## 基本档案

| 项目 | 值 | 说明 |
|---|---|---|
| Skill 调用名 | `registered-architect` | 唯一标识，全小写连字符写法；支持原生 Skill 的工具直接用它调起，不支持的工具用自然语言描述建筑设计与规范核验任务也能触发 |
| 显示名 | OmniAiLab 全球注册建筑师 | 仓库页面与文档中的显示名，与调用名不是同一个东西 |
| 版本 | v1.1.0 | 与 `SKILL.md`、`.claude-plugin/plugin.json` 保持一致；国家专项资料自 v1.1.0 起做到条文级精度 |
| 定位 | 注册建筑师的规范路由与设计核验框架 | **不是总设计师、不是方案创作工具、不是效果图生成器**；它输出的是判断、清单与待核验事项 |
| 出品 / 开发者 | OmniAiLab ／ Mochiball | 署名与版权见文末与 [LICENSE](LICENSE) |
| 许可 | MIT | 可自由使用、修改与再分发，保留版权与许可声明即可 |
| 开源仓库 | [tomatoparkdao/registered-architect](https://github.com/tomatoparkdao/registered-architect) | 公开仓库，可直接 `git clone` 获取完整模块、参考资料与计算脚本 |
| 运行要求 | Python 3.9+（仅计算器需要） | 七个计算器只用标准库 `argparse` / `json` / `math` / `sys`，无第三方依赖；不联网即可阅读全部知识库 |
| 规模 | 29 模块 ／ 883 份参考文档 ／ 约 113 万行 | 其中中国大陆专题 848 份（426 份规范与图集条目 + 414 份正文分片），是十个辖区里资料最厚的一个 |

## 适用范围：做与不做

判断一个任务该不该交给它，看这张表就够了。

| 适用性 | 具体内容 |
|---|---|
| **适用 · 辖区定位与法规路由** | 拿到项目地址、用途、高度、面积、火灾危险类别与设计阶段，判定适用哪一级强制性标准、主管部门是谁、哪些是地方补充规定；十个辖区各自有独立专题，可交叉比较 |
| **适用 · 方案与技术设计判断** | 功能策划、面积表、邻接关系、体量比较、核心筒与柱网、围护构造、结构体系选型、机电协调、采光遮阳、房间声学、材料策略——给的是有依据的选项与权衡，不是拍脑袋的单一答案 |
| **适用 · 合规交叉校核** | 防火分区、疏散距离、出口数量、无障碍路径、节能指标、日照与间距：逐项列出采用版本、条文依据、地方差异和待 AHJ 确认的问题 |
| **适用 · 交付与审查** | 图纸组织、图层线宽、标注体系、LOD、BIM 协调、规范文本、RFI/ASI、竣工与运维资料检查清单 |
| **不适用 · 审批与签章结论** | 建筑许可、消防审查意见、结构签章、能源认证、无障碍认证——这些只能由主管部门与当地持证专业人员出具，本技能的输出不得被表述为上述任何一项 |
| **不适用 · 结构安全最终判定** | 可给跨度参考、荷载路径与初步截面，但最终截面、配筋、抗震构造须由结构工程师按现行标准复核；经验规则不得写成强制性条文 |
| **不适用 · 跨国数值直接套用** | 把一个国家的限值搬到另一个国家是最常见的错误来源。跨辖区只能比较“指标—版本—适用范围”，不能等效替换 |

## 快速开始

技能的总入口是 [SKILL.md](SKILL.md)。装好之后，第一句话把项目语境说清楚，比任何提示词技巧都重要。

```bash
# 方式一：作为 Claude Code 插件直接挂载
claude --plugin-dir "/path/to/registered-architect"

# 方式二：放进宿主 Agent 的 skills 目录（按你所用工具的实际路径）
cp -R registered-architect ~/.claude/skills/registered-architect
cp -R registered-architect ~/.codex/skills/registered-architect
cp -R registered-architect ~/.workbuddy/skills/registered-architect

# 方式三：只做只读参考，不装
git clone https://github.com/tomatoparkdao/registered-architect.git
```

复制到既有项目时，**必须保留完整的 `skills/` 目录**：模块、参考资料、模板与计算器之间的相对链接一旦断开，路由就失效。

第一次对话建议直接给出这五项，缺一项它会先问：

```text
国家/城市：阿联酋 迪拜
用途与规模：酒店，18 层，地上 32,000 m²，含裙房餐饮
设计阶段：方案深化，准备报民防预审
已知约束：地块退界 6 m，限高 75 m，主开发商有外墙覆盖要求
要你做的事：核验疏散与无障碍路径，列出待民防确认的问题
```

## 工作机制：三层渐进加载

技能不会一次性把所有资料塞进上下文。名称与描述常驻，正文按需加载，参考资料与脚本明确需要时才读——这是它能在 883 份文档里不迷路的唯一办法。

| 层级 | 加载内容 | 加载时机 | 典型体积 |
|---|---|---|---|
| 第 0 层 | 技能名称与 description | 始终可见，用于判断“这个任务该不该用它” | 数十行 |
| 第 1 层 | 对应模块的 `SKILL.md` 正文 | 命中任务类型时加载，含该模块的方法、判据与红线 | 400–600 行 |
| 第 2 层 | `references/` 参考文档、模板、`scripts/` 计算器 | 需要具体条文、表格、构造做法或数值计算时才读 | 按文件取用 |

路由顺序是固定的，跳步就会出错：

```text
用户输入（地址 / 用途 / 面积 / 阶段）
        │
        ▼
geographic-foundations ── 识别国家、城市、规范编号、货币、气候、材料体系
        │
        ├─ 识别成功 ──► skills/country-<辖区>/SKILL.md   规范层级、主管部门、审查路径
        │
        └─ 识别失败 ──► 回落到 IBC / Eurocodes / ASCE / ISO 参考，
        │               并明确要求用户确认适用辖区（不猜）
        ▼
按任务选专业模块 ── 设计 / 技术 / 合规 / 交付 四层
        │
        ▼
输出：适用约束 → 设计响应 → 证据与版本 → 待核验事项 → 责任方
```

## 模块总览（29 项）

18 项专业能力 ＋ 10 个辖区专题 ＋ 1 组计算器。`references/` 下的文档数说明这个模块能查到多深。

| # | 模块 | 类别 | 主要能力 |
|---|---|---|---|
| 1 | `architect-foundations` | 基础 | 建筑师与理论家速查矩阵（Vitruvius → Kéré）、定量经验规则、28 个建筑子类型、设计质量框架、五类反模式目录、模块路由 |
| 2 | `geographic-foundations` | 基础 | 由国家、城市、规范编号、货币、气候与材料体系识别辖区并路由；无法识别时回落到国际参考并要求确认，不擅自假定 |
| 3 | `design-theory` | 设计 | 建筑史、思潮、宣言、设计哲学、形式语言、批判地域主义、现象学与设计批评；区分历史事实、理论解释与项目建议 |
| 4 | `concept-design` | 设计 | 概念生成、体量研究、太阳包络、风舒适、视线廊道、阴影影响、语境化高度、FAR/GFA 优化与自然通风体量 |
| 5 | `building-programming` | 设计 | 任务书、面积标准、邻接矩阵、流程图、人员容量、设备清单、功能分区与容量验证；面积是策划依据，须按运营模式与当地规范复核 |
| 6 | `building-typology` | 设计 | 住宅、办公、酒店、零售、学校、医院、图书馆、剧院、体育、工业与混合使用的空间组织、标准层、流线、采光、结构与运营比较 |
| 7 | `spatial-planning` | 设计 | 核心筒、竖向交通、公私流线、楼层效率、服务空间、装卸、停车、卫生间、机房管井与疏散；平面建议须同时过可达性、消防与结构网格 |
| 8 | `building-envelope` | 技术 | 砖墙、混凝土墙、幕墙、双层表皮、木结构墙、金属板、保温、气密、水密、玻璃与间隔条、镀膜与动态玻璃；结合气候、朝向、湿度与全生命周期碳判断 |
| 9 | `structural-systems` | 技术 | 混凝土、钢、木、砌体、预制、张弦、空间网架、壳体与复合体系的跨度与构造参考；**不得凭经验表定尺寸**，实际设计须结构工程师复核 |
| 10 | `building-services` | 技术 | 自然通风与混合模式、VAV/VRF、冷梁、热泵、热回收、给排水、雨水、消防水、电气、照明、弱电、BMS、设备房与屋面设备、机电协调 |
| 11 | `daylighting-design` | 技术 | DF、sDA、ASE、UDI、VLT、SHGC、太阳高度角与方位角、遮阳几何、采光中庭、锯齿屋顶；模拟结果须注明天气文件、时间步长与占用假设 |
| 12 | `acoustic-design` | 技术 | 墙体与楼板隔声、窗声学、撞击声、侧向传声、设备噪声、混响时间、清晰度、空间感、隔振与可变声学；须同时看构造节点、穿孔、门窗与施工质量 |
| 13 | `material-selection` | 技术 | 按性能、法规、耐久、维护、成本、隐含碳、可回收性、供应链、施工与美学比较材料；产品数据不替代样品、测试与供应商确认 |
| 14 | `building-codes` | 合规 | IBC 使用类别与 I–V 类构造、高度面积限值、疏散、防火分隔、卫生器具计算，以及 IBC / Building Regulations / Eurocodes / NCC / NBC 的横向比较 |
| 15 | `fire-life-safety` | 合规 | 占用人数、出口数量、疏散距离、楼梯与走道、消防电梯、防火分区、烟控、报警、喷淋、消防车道与避难空间；须明确采用版本及地方修订 |
| 16 | `accessibility-design` | 合规 | ADA、ISO、EN、BS、DIN、AS、GB、BCA 体系比较；连续无障碍路径、门、坡道、电梯、卫生间、停车、触觉 / 听觉 / 认知支持 |
| 17 | `building-sustainability` | 合规 | 被动式设计、能源模型、运营碳与隐含碳、水、材料、健康、生态与认证；LEED、BREEAM、WELL、Green Star、NABERS、DGNB、CASBEE 门槛会更新，用前须核版本 |
| 18 | `construction-documentation` | 交付 | 图纸目录、图层线宽、标注符号、材料填充、修订云线、LOD、BIM 协调、规范文本、RFI/ASI、样板、现场测试、收尾保修与运维资料 |
| 19 | `architect-calculator` | 工具 | 七个标准库计算器：面积密度、U 值、采光系数、疏散、结构荷载、能耗、造价 |

参考资料的分层（`references/` 下的 Markdown 份数，不含 `SKILL.md` 本身）：

| 文档位置 | 份数 | 说明 |
|---|---|---|
| `skills/*/references/`（18 个专业模块） | 35 | 每个模块 1–4 份专题参考：ADA 与无障碍体系、房间声学、围护构造、案例库、计算方法等；`architect-foundations` 最厚（4 份） |
| `skills/country-china/references/standards/` | 426 | 中国规范与图集条目：GB 强制规范、JGJ 行业标准、地方 DB 与国标图集，按编号命名，可逐条定位 |
| `skills/country-china/references/standards/text/` | 414 | 上述条目的正文分片，供条文级引用与交叉检索；扫描件未识别的部分单独标记，不当作条文使用 |
| 其余九个辖区 | 各 0 | 单文件专题，全部内容收在各自 `SKILL.md` 内，不做二次拆包 |
| **合计** | **883** | 阅读时按层加载第 2 层，不会一次性灌进上下文 |

## 十个司法辖区

每个辖区一个专题文件，写清监管体系、规范层级、主管部门与审查重点。**跨辖区只能比较，不能等效替换。**

| 辖区 | 监管体系 | 核心规范 | 审查重点 |
|---|---|---|---|
| 中国 | 国家集中管理 + 强制性条文（D 型） | GB 50352-2019、GB 50016-2014（2018 年版）、GB 50011-2010（2016 修订）、GB 55015-2021、GB 50189-2015、GB 50763-2012、JGJ 系列、地方 DB | 强制性工程建设规范与推荐性标准的区分、日照间距、五类热工气候区节能、六至九度抗震；**香港、澳门单独处理**，不套大陆口径 |
| 美国 | 州与市分别采用模式规范 | IBC 2024、IRC、IECC 2024、IFC、NFPA 101、NFPA 70、ADA 2010、ANSI A117.1、ASCE 7-22、ACI 318、AISC 360、AWC NDS | 州级修订差异极大（CA Title 24、NYC、FL HVHZ、Chicago、MA、WA），AHJ 解释权高于纸面条文 |
| 英国 | 中央法规 + 地方执行，2022 年后责任链重构 | Building Regulations 2010 及 Approved Documents A–S、Building Safety Act 2022、BSR / HRB 制度、BS 9991、BS 9999、BS 8300、NPPF、London Plan | 高风险建筑（HRB）的 Accountable Person 与 Golden Thread 证据链；苏格兰、威尔士、北爱尔兰并非英格兰规则的复制 |
| 德国 | 联邦框架法 + 16 州自订 LBO | MBO、BauGB、BauNVO、GEG 2023、DIN 18040、DIN 4109、DIN 4108、DIN 4102 / EN 13501、Eurocodes 及国家附录 | Sonderbau 专项建筑、Brandschutznachweis 防火证明、DGNB、BAFA/KfW 补贴与 Passivhaus 叠加要求 |
| 日本 | 国家法 + 地方条例 + 民间评价 | Building Standards Act、消防法、City Planning Act、Heart Building Law、AIJ Recommendations、BCJ 结构性能评价、CASBEE | 用途地域、容积率与建蔽率、日影与斜线限制、防火地域、两级抗震设计；体量方案常被规划条款先卡死 |
| 新加坡 | 集中监管（BCA / SCDF / URA 各管一段） | Building Control Act、BCA Regulations、SCDF Fire Code 2018、BCA Code on Accessibility、Green Mark 2021、URA Master Plan、SS EN Eurocodes | ETTV / RTTV 围护指标、消防疏散与维护安全、总体规划符合性；三部门口径须分别确认 |
| 澳大利亚 | NCC 全国统一 + 州级规划与审批 | NCC 2022 Vol 1–3、AS/NZS 1170 系列、AS 3600、AS 4100、AS 1684、AS 1428.1-2021、AS 5113、NatHERS 7-star、BASIX、Green Star、NABERS | 性能条款与“视为符合”条款的取舍、州级审批差异、丛林火灾 / 气旋 / 洪水叠加风险、风区 A–D |
| 印度 | 国家规范 + 州 / 市政开发控制规则 | NBC 2016、ECBC 2017、IS 456、IS 800、IS 875、IS 1893、IS 13920、州级 DCR、RERA、EIA、CRZ、GRIHA、IGBC | 开发控制（FAR、退界、停车）由国家规范与州 / 市政规则共同决定，两者冲突时按更严格者准备 |
| 阿联酋 | 酋长国分立，迪拜与阿布扎比不同体系 | Dubai Building Code 2021、ADIBC、UAE Fire & Life Safety Code 2018、Dubai Universal Design Code、Estidama、Al Sa'fat | 高层与外墙覆层防火、避难层、民防（Civil Defence）预审、主开发商设计指南常严于法定规范 |
| 沙特 | 国家建筑规范 + 专项开发辖区 | SBC 201 系列、SBC 801、Saudi Universal Accessibility Code、Mostadamah、Amana 审批 | NEOM、Qiddiya、红海、Diriyah、AlUla、RCRC、麦加与麦地那可能各有独立审查流程，不能套 SBC 一套走完 |

## 七个计算器

只做早期设计与交叉校核，**报审数值必须由持证人员按现行规范重算**。全部只用 Python 标准库。

| 脚本 | 算什么 | 关键参数 | 用在哪 |
|---|---|---|---|
| `area_calculator.py` | 开发密度：GFA、NGA、套数、人口、车位数 | `--site-area` `--far` `--ntg-ratio` `--avg-unit-size` `--persons-per-unit` `--parking-ratio` | 拿地与方案前期的容量校核 |
| `uvalue_calculator.py` | 围护传热系数 U 值（分层构造） | `--layers` `--facade` `--rsi-internal` `--rsi-external` | 节能规范对标、构造比选 |
| `daylight_calculator.py` | 采光系数初算 | `--room-width/depth/height` `--window-width/height/sill-height` `--glazing-transmittance` `--average-reflectance` | 教室、办公、住宅的采光合规预判 |
| `egress_calculator.py` | 疏散宽度与出口数量 | `--floor-area` `--occupancy-type` `--sprinklered` `--num-stories` | 方案阶段就要定的核心筒与楼梯数量 |
| `structural_load_calculator.py` | 荷载汇集与构件初算 | `--tributary-area` `--num-floors` `--dead-load` `--live-load` `--occupancy-type` | 柱网与楼板厚度的量级判断 |
| `energy_calculator.py` | 能耗强度初估 | `--floor-area` `--envelope-area` `--average-u-value` `--heating/cooling-degree-days` `--ventilation-rate` `--internal-gains` | 方案阶段的节能路线比较 |
| `cost_calculator.py` | 造价初估 | `--gfa` `--building-type` `--quality` `--region` `--include-external` | 业主预算与方案取舍 |

```bash
# 输出人类可读摘要
python skills/architect-calculator/scripts/area_calculator.py \
  --site-area 5000 --far 2.5 --ntg-ratio 0.82

# 加 --json 便于脚本串联与留档
python skills/architect-calculator/scripts/egress_calculator.py \
  --floor-area 1800 --occupancy-type business --sprinklered --num-stories 12 --json
```

## 六阶段工作流

| 阶段 | 输入 | 动作 | 输出 |
|---|---|---|---|
| 1 项目理解 | 地址、用地边界、现状测绘、功能、面积、层数、预算、进度、业主目标、运营模式 | 收集并核对基础信息，把未知项写进假设清单，不猜 | 项目摘要 + 关键假设表 |
| 2 法规路由 | 阶段 1 摘要 | 识别主管部门与法规层级，区分强制性要求、推荐指南、主开发商要求、认证条款与业主偏好 | 法规路由表 + 冲突优先级 + 待确认清单 |
| 3 功能与体量 | 法规路由结论 | 建面积表、邻接矩阵、流线；出体量选项并同步看日照、视线、风、消防、无障碍、结构与施工 | 面积表 + 邻接矩阵 + 体量比选 |
| 4 技术协调 | 选定体量 | 定结构网格、楼板厚度、核心筒、管井、设备房、围护系统、竖向交通、消防系统、遮阳与维护路径 | 技术协调清单 + 关键接口表 |
| 5 性能验证 | 技术方案 | 按阶段做面积、U 值、采光、疏散、荷载、能耗、声学、碳与成本计算，标清谁算的 | 性能验证表（计算器 / 模拟 / 工程师复核分列） |
| 6 设计交付 | 全部前置结论 | 出图纸、模型、表格、规范文本、材料表、性能说明、审批文件与风险登记；每次修订留版本、日期、原因、责任人 | 交付包 + 修订记录 |

## 审查输出模板

### 项目摘要

```text
项目名称：
项目地点：            国 / 州或省 / 城市 / 特别辖区
主管部门：            AHJ、民防、规划、消防（分别列明）
建筑用途与分类：
用地面积 / 建筑面积 / 层数 / 高度：
设计阶段：            方案 / 初设 / 施工图 / 报审
适用法规与版本：      规范编号 + 版本 + 核验日期
```

### 关键假设

| 编号 | 假设 | 影响范围 | 确认人 | 状态 |
|---|---|---|---|---|
| A-01 | 用地边界与测绘资料准确 | 体量、面积、退界、消防车道 | 业主 / 测绘单位 | 待确认 |
| A-02 | 用途分类与运营模式已定 | 消防类别、单位人数、设备负荷 | 业主 / 建筑师 | 待确认 |
| A-03 | 采用当前有效的规范版本 | 全部合规结论的有效性 | 建筑师 / AHJ | 待确认 |
| A-04 | 结构与机电顾问已介入协调 | 柱网、层高、管井、设备房 | 项目经理 | 待确认 |

### 约束与响应

| 约束类别 | 约束内容 | 设计响应 | 证据或待核验事项 |
|---|---|---|---|
| 规划 | 高度、退界、FAR / 容积率、建蔽率 | 体量控制与楼层分配 | 规划批文、分区条款、限高文件 |
| 消防 | 占用人数、出口、耐火等级、喷淋 | 防火分区与疏散方案 | 消防规范条文 + AHJ 预审意见 |
| 无障碍 | 连续路径、坡道、电梯、卫生间 | 通用设计路径与节点做法 | 无障碍法规版本 + 现场实测条件 |
| 环境 | 日照、能耗、热工、碳 | 围护与系统策略 | 模拟报告、能源规范限值、认证条款 |
| 结构 | 风、地震、雪、荷载 | 结构体系与柱网 | 结构顾问复核意见 |
| 施工 | 场地、吊装、材料、工期 | 分期方案与节点设计 | 承包商与施工方法说明 |

### 风险登记

| 风险 | 概率 | 影响 | 缓解措施 | 责任方 |
|---|---|---|---|---|
| 规范版本更新 | 中 | 高 | 记录核验日期并持续监测，报审前二次确认 | 建筑师 |
| 地方审批口径不明确 | 中 | 高 | 尽早向 AHJ 提交预审问询，保留书面答复 | 项目经理 |
| 关键尺寸未跨专业协调 | 中 | 中 | 跨专业模型审查与碰撞检查 | BIM 负责人 |
| 材料供应或性能不达标 | 中 | 中 | 预审替代材料与供应商，保留等效证明 | 材料顾问 |
| 维护空间不足 | 低 | 高 | 运维可达性审查，设备更换路径验证 | 机电顾问 |

## 示例提示词

```text
为北纬 40° 的 12 层住宅比较三种体量方案，说明日照、风环境、结构与消防影响。

按新加坡 SCDF Fire Code 与 BCA Code on Accessibility，审查这家酒店的疏散与无障碍方案，
逐条列出条号、判定结果和需要向哪个部门确认。

为 5,000 m² 办公楼生成面积表、邻接矩阵、核心筒选项与初步柱网。

比较双层玻璃、三层玻璃与动态玻璃的 U 值、SHGC、VLT、成本与生命周期影响。

针对英国项目建立围护结构、BREEAM、声学与施工图交付的检查清单。

核验印度 NBC 使用分类、耐火分隔、停车、FAR 与无障碍要求，列出待向主管部门确认的事项。

使用计算器估算 2,000 m² 建筑的 U 值、疏散容量、结构荷载与初步造价，并标注各项假设。
```

## 交付文件命名

固定前缀让审查链路可追溯，顺序即工作顺序。

| 文件 | 内容 | 谁看 |
|---|---|---|
| `01_project-brief.md` | 项目摘要、关键假设、设计阶段 | 业主、项目经理 |
| `02_code-route.md` | 辖区判定、规范层级、版本与核验日期 | 建筑师、AHJ |
| `03_program.md` | 功能清单、面积表、邻接关系 | 业主、运营方 |
| `04_concept-options.md` | 概念、体量比较与环境响应 | 业主、评审 |
| `05_performance.md` | 环境、结构、消防、无障碍性能 | 各专业顾问 |
| `06_materials.md` | 围护与材料策略、等效证明 | 材料顾问、承包商 |
| `07_documentation.md` | 图纸、规范文本、BIM 协调 | 施工方、审查方 |
| `08_review-log.md` | 审查意见、RFI、ASI、决策记录 | 全项目组 |

## 目录结构

```text
registered-architect/
├── SKILL.md                          # 总入口：原则、模块指引、交付要求
├── README.md                         # 简体中文 README（默认）
├── README_EN.md                      # English README
├── LICENSE                           # OmniAiLab MIT License
├── .claude-plugin/plugin.json        # 插件元数据与关键词
└── skills/
    ├── architect-foundations/        # 自动加载的基础层
    ├── geographic-foundations/       # 辖区识别与路由
    ├── design-theory/  concept-design/  building-programming/
    ├── building-typology/  spatial-planning/
    ├── building-envelope/  structural-systems/  building-services/
    ├── daylighting-design/  acoustic-design/  material-selection/
    ├── building-codes/  fire-life-safety/  accessibility-design/
    ├── building-sustainability/  construction-documentation/
    ├── architect-calculator/         # 7 个脚本 + 计算参考
    └── country-{china,usa,uk,germany,japan,singapore,australia,india,uae,saudi-arabia}/
        ├── SKILL.md                  # 辖区专题正文
        └── references/standards/     # 中国：426 条规范与图集 + 414 份正文分片
```

## 责任边界

这条线必须写清楚，否则输出的每一条建议都会被误读成结论。

| 事项 | 本技能能做的 | 必须由谁最终确认 |
|---|---|---|
| 法规适用与条文定位 | 判定辖区、列出规范层级、定位条文、标注版本与地方差异 | 当地主管部门（AHJ）与注册建筑师 |
| 防火与生命安全 | 疏散距离、出口数量、防火分区策略、烟控与报警体系建议 | 消防审查部门 + 具备当地资质的消防工程师 |
| 结构安全 | 体系选型、跨度参考、荷载路径、初算 | 结构工程师按现行标准复核并签章 |
| 无障碍 | 路径、坡道、电梯、卫生间做法的合规比对 | 无障碍专项审查与注册建筑师 |
| 节能与认证 | 指标预判、围护与系统策略、认证条款比对 | 能源顾问、认证机构（LEED / BREEAM / Green Mark 等） |
| 造价 | 量级估算与方案比选 | 造价咨询与业主预算决策 |
| 图纸与施工图 | 图纸组织、图层标注、LOD、协调清单 | 设计单位内部校审 + 施工图审查机构 |

输入不足时，它列缺失项而不自行假定关键条件；法规不确定时，它同时给出版本、判断依据、可能的地方差异和需要向 AHJ / 规划 / 消防确认的问题。

## 常见错误

| 错误 | 后果 | 正确做法 |
|---|---|---|
| 把一个国家的法规数值直接用于另一个国家 | 整套方案在报审阶段被推翻 | 先做辖区路由，只比较指标与适用范围，不做等效替换 |
| 使用过时版本且不注明核验日期 | 结论不可追溯，责任无法界定 | 每条结论写规范编号 + 版本 + 核验日期 |
| 把经验规则当成强制条文 | 误导业主与施工方，埋下验收风险 | 经验值标注为“参考”，强制要求必须引条号 |
| 只优化平面面积，忽略消防、结构、机电与维护空间 | 后期返工，核心筒与管井无处安放 | 方案阶段就同步过四类专业条件 |
| 只比初始造价，忽略运行与替换成本 | 全生命周期成本反而更高 | 按寿命周期比较，含维护与替换 |
| 只给结论不给假设 | 无法复核，也无法追责 | 每条判断附假设、证据与待确认事项 |
| 把 AI 建议写成签章、审批或认证结论 | 法律与职业责任风险 | 明确区分“建议 / 核验 / 审批 / 认证”四种性质 |

## 常见问题

| 问题 | 回答 |
|---|---|
| 只适用于中国项目吗？ | 不是。十个辖区各有专题，中国只是其中之一，且是资料最厚的一个（848 份条文资料）。无明确辖区时它会回落到国际参考并要求你确认。 |
| 计算器结果能直接报审吗？ | 不能。计算器用于早期设计与交叉校核；报审数值须由持证人员按现行规范重算并签署。 |
| 项目所在城市没有专门规范怎么办？ | 它会说明缺失，采用上一级规范作暂定参考，并列出需要向 AHJ 或地方规划部门确认的问题清单。 |
| 可以比较不同国家的法规吗？ | 可以，但必须限定比较指标、版本、适用范围，并说明哪些部分不可等效。 |
| 需要联网或外部软件吗？ | 不需要。知识库、模板与计算器全部离线可用；CAD、BIM、渲染与分析软件只是可选对接对象，不是依赖。 |
| 它的输出算不算设计成果？ | 算设计判断与审查意见的支撑材料，不算可签章的施工图或审批文件。 |

## 规模统计

| 项目 | 数量 | 备注 |
|---|---|---|
| 专业模块 | 18 项 | 覆盖基础、设计、技术、合规、交付五层 |
| 辖区专题 | 10 个 | 中国、美国、英国、德国、日本、新加坡、澳大利亚、印度、阿联酋、沙特 |
| 计算器 | 7 个 | 纯标准库，`--json` 可留档 |
| 参考文档 | 883 份 | 含中国大陆专题 848 份：426 条规范与图集 + 414 份正文分片 |
| 知识库规模 | 约 113 万行 Markdown | 919 个文件，含模块正文与参考资料 |
| 建筑师与理论家 | 50+ | 从 Vitruvius 到 Kéré，附代表作品与适用语境 |
| 建筑思潮 | 20+ | 现代主义、后现代、批判地域主义、参数主义、现象学等 |
| 建筑类型 | 28+ | 住宅、商业、机构、工业、特殊建筑各子类 |
| 结构体系 | 15+ | 混凝土、钢、木、砌体、预制、张弦、网架、壳体、复合 |
| 可持续性认证 | 8+ | LEED、BREEAM、WELL、Green Star、NABERS、DGNB、CASBEE、Estidama、Mostadamah |
| 参考案例 | 100+ | 用于先例分析与做法对照 |
| 尺寸与经验值 | 200+ | 层高、柱网、净得率、走廊、停车、电梯、耐火等级等 |

## 版本记录

| 版本 | 变更内容 | 影响范围 |
|---|---|---|
| v1.1.0 | 十个辖区专题升级到条文级精度（规范编号、版本年份、地方修订、审查路径）；新增中国规范与图集分片库 | 辖区路由与条文定位 |
| v1.0.0 | 全球注册建筑师技能框架：18 项专业模块 + 10 个辖区 + 7 个计算器 | 全量 |
| OmniAiLab 版 | 统一元数据、MIT 许可、署名与交付边界；自然语言中文化，保留规范编号、路径与程序标识 | 文档与元数据 |

## 许可与署名

本技能包采用 **MIT License**，许可文本见 [LICENSE](LICENSE)。可自由使用、修改与再分发，保留版权与许可声明即可。

- 出品：OmniAiLab
- 开发者：Mochiball
- 平台：[omniailabx.com](https://www.omniailabx.com/)
- 仓库：[tomatoparkdao/registered-architect](https://github.com/tomatoparkdao/registered-architect)

规范资料仅用于辅助设计判断。对任何数值限值、条文引用或合规结论，均须核验项目所在地现行的国家强制性标准、地方标准与主管部门要求，并由具备当地资质的专业人员复核签署。

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
