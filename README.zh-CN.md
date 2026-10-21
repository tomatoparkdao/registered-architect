<h1 align="center">OmniAiLab 全球注册建筑师</h1>

<p align="center">
  <b>面向全球注册建筑师的规范路由、设计核验与交付审查 Skill —— 先定辖区，再谈设计</b><br>
  29 个模块：18 项专业设计能力 ＋ 10 个司法辖区法规专题 ＋ 1 个计算器模块（7 个脚本） ｜ 839 份中国条文 ＋ 4335 张图集图纸（83 本图册） ｜ 约 420 万行资料<br>
  项目定位 → 法规路由 → 功能与体量 → 技术协调 → 性能验证 → 施工图交付 → 合规审查<br>
  规范只做路由与核验，不作审批结论 ｜ 零硬依赖可离线 ｜ 结构 / 消防 / 无障碍须当地持证人员复核签署
</p>

<p align="center">
  <a href="https://github.com/tomatoparkdao/registered-architect"><img src="https://img.shields.io/badge/%E7%89%88%E6%9C%AC-1.2.0-1f6feb?style=flat-square" alt="版本 1.2.0"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/%E8%AE%B8%E5%8F%AF-MIT-2ea043?style=flat-square" alt="许可 MIT"></a>
  <a href="https://www.omniailabx.com/"><img src="https://img.shields.io/badge/%E5%B9%B3%E5%8F%B0-OmniAiLab-8957e5?style=flat-square" alt="平台 OmniAiLab"></a>
  <a href="https://discord.gg/vdgTEpXMh3"><img src="https://img.shields.io/badge/%E7%A4%BE%E5%8C%BA-Discord-5865f2?style=flat-square" alt="开源社区 Discord"></a>
  <a href="https://www.omniailabx.com/plugin#desktop-download"><img src="https://img.shields.io/badge/Agent-%E4%B8%8B%E8%BD%BD%E6%9C%80%E6%96%B0%E7%89%88-2ea043?style=flat-square" alt="下载最新 Agent"></a>
  <img src="https://img.shields.io/badge/%E5%9C%B0%E5%8C%BA-10_%E4%B8%AA%E5%8F%B8%E6%B3%95%E8%BE%96%E5%8C%BA-0e8a16?style=flat-square" alt="10 个司法辖区">
  <img src="https://img.shields.io/badge/%E6%A8%A1%E5%9D%97-29_%E9%A1%B9-0969da?style=flat-square" alt="29 项模块">
  <img src="https://img.shields.io/badge/%E5%85%BC%E5%AE%B9-Codex_%7C_Claude_%7C_WorkBuddy_%7C_OmniAiLab-6f42c1?style=flat-square" alt="兼容 Codex / Claude / WorkBuddy / OmniAiLab">
</p>

<p align="center">
  <b>简体中文</b>　｜　<a href="README_EN.md">English</a>
</p>

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。

它不画方案，也不替你签字——**开工第一件事是确认这个项目受哪一级强制性标准管**：先用地址、用途、高度、面积与设计阶段判定司法辖区与主管部门，再沿规范层级拆到具体条文，然后才进入功能与体量、技术协调、性能验证、施工图与合规审查。你在每个环节末尾只需回答"继续"或"这里不对"。一个 Skill 覆盖 10 个司法辖区、18 项专业能力与 7 个计算器，把"这个数从哪来、哪一版、哪天核的"写进每条结论，让设计判断变成可追溯、可复核、可交审查的记录。

| 项目 | 值 | 说明 |
|---|---|---|
| 模块体系 | 29 个模块 / 83 本图册 / 4335 张图纸 | 18 项专业设计能力 ＋ 10 个司法辖区法规专题 ＋ `architect-calculator`（7 个脚本）；中国资料库含 839 份条文（425 条目 ＋ 414 分片）、198 个规范编号、314 份可检索文档 |
| Skill 调用名（唯一标识） | `registered-architect` | 全小写连字符写法；支持 skill 的工具直接用它调起，不支持的工具用自然语言描述也能触发 |
| 显示名 | OmniAiLab 全球注册建筑师 | 仓库页面与文档里显示的名字，不是调用名；定位是规范路由与核验，不是方案创作 |
| 版本 | v1.2.0 | 与 `SKILL.md`、`.claude-plugin/plugin.json` 及三份 README 保持一致；1.2.0 起加入图集图纸层与「条文 ↔ 图纸」双向路由 |
| 出品 / 开发者 | OmniAiLab ／ Mochiball | — |
| 许可 | MIT（见 [LICENSE](LICENSE)） | 使用与二次分发以该文件为准；标准原文只引用、不转售 |
| 配套文档 | [README.md](README.md) ／ [README_EN.md](README_EN.md) ／ [SKILL.md](SKILL.md) | 如何调用、模块清单、六阶段流程、口径速查、避坑总表、常见问题与交付物清单 |
| 仓库 | [tomatoparkdao/registered-architect](https://github.com/tomatoparkdao/registered-architect) | 全部模块、参考资料与计算器；**当前为私有仓库**，公开后可直接 `git clone` 与提 issue |
| 运行要求 | Python 3.9+（仅计算器需要） | 计算器零第三方依赖；不装 Python 也能读完全部资料，只是少了初算这一步 |
| 原生平台 | [OmniAiLab 中国站](https://www.omniailabx.com/) ／ [海外站](https://omniailab.cn/) | 需要效果图与动画时走平台；**未接入时规范核验照常运行** |

调用名是**全小写连字符**写法（`registered-architect`），不是「OmniAiLab 全球注册建筑师」这个显示名。支持 skill 的工具直接用调用名最稳；不支持原生 skill 的工具，用自然语言描述"这个项目在中东，消防疏散要核哪些条文"也能触发。

> **名字里的一个坑**：仓库根目录只有一份 `SKILL.md`，那是**入口**（全局原则 + 模块路由）；
> `skills/<模块>/SKILL.md` 是 29 份**能力单元**，各自带 front-matter 与署名，由入口按需加载。
> 调用时点名 `registered-architect` 即可——逐个挂载模块，会让同一份条文资料被加载两次。

---


## 先判断"在哪个辖区"，再谈怎么做设计

同一个体量方案，放在迪拜、慕尼黑和新加坡要过的审查完全不同：迪拜看民防预审与外墙覆层，慕尼黑看 Brandschutznachweis 与州级 LBO，新加坡看 SCDF Fire Code 与 ETTV/RTTV。**所以第一步不是画图，是确认这个项目受哪一级强制性标准管、主管部门是谁。**

确认不了就先列缺失项，而不是套一个别国的数值继续往下算。这条规矩贯穿全部 29 个模块。

| 适用范围 | 具体是什么 |
|---|---|
| **适用 · 辖区定位与法规路由** | 拿到地址、用途、高度、面积、火灾危险类别与设计阶段，判定适用哪一级强制性标准、主管部门是谁、哪些是地方补充规定；十个辖区各有独立专题，可交叉比较 |
| **适用 · 方案与技术判断** | 功能策划、面积表、邻接关系、体量比较、核心筒与柱网、围护构造、结构体系选型、机电协调、采光遮阳、房间声学、材料策略——给的是有依据的选项与权衡，不是拍脑袋的单一答案 |
| **适用 · 合规交叉校核** | 防火分区、疏散距离、出口数量、无障碍路径、节能指标、日照与间距：逐项列出采用版本、条文依据、地方差异和待 AHJ 确认的问题 |
| **不适用（明确说不）** | 建筑许可、消防审查意见、结构签章、能源认证、无障碍认证——只能由主管部门与当地持证专业人员出具；本技能的输出不得被表述为上述任何一项 |

---

## 一句话

把项目条件交给它——哪怕只是"迪拜一栋 18 层酒店，方案深化，准备民防预审"——它会先定辖区与规范层级，再按六阶段推进到可交付的判断、清单与文件；你在每个阶段末尾只需要回答"确认"或"要改哪里"。

**它不说"这个方案符合规范"，它说"这条按 GB 50016-2014（2018 年版）第 5.3.1 条属一类高层公共建筑，你的分区差约 200 m²，须与消防部门确认"**——每一条结论都带编号、版本、位置和待核验事项，错了能查到是哪一步、哪一版、谁确认的。

## 能力一览

**它不是"把规范条文塞进上下文的检索器"，而是一套会先问清辖区、会把口径写进结论、会把做不到的部分如实说出来的核验系统。**

| 层面 | 具体有什么 |
|---|---|
| **① 辖区路由优先** | `geographic-foundations` 从国家、城市、规范编号、货币、气候与材料体系识别辖区，再路由到对应专题。识别不出来就回落到 IBC / Eurocodes / ASCE / ISO 参考，**并明确要求你确认**，绝不替你假定 |
| **② 十个辖区做到条文级** | 中国、美国、英国、德国、日本、新加坡、澳大利亚、印度、阿联酋、沙特：监管体系、主管部门、规范层级、版本年份、地方修订与审查路径，逐项写清；跨辖区只比较、不替换 |
| **③ 十八项专业模块** | 设计理论、概念、策划、类型、空间、围护、结构、机电、采光、声学、材料、规范、消防、无障碍、可持续、施工图：每项都给方法、判据与红线，不是词条堆砌 |
| **④ 四层渐进加载** | 名称常驻、模块正文按需、条文资料次之、图纸与配方最后读。13917 份 Markdown 与 4335 张图纸不会一次塞进上下文——这是它能在 420 万行资料里不迷路的唯一办法 |
| **⑤ 七个可复算的计算器** | 面积密度、U 值、采光系数、疏散、结构荷载、能耗、造价：纯标准库，`--json` 可留档；**结果只作初算，报审值须持证人员重算** |
| **⑥ 判断有出处** | 每条结论写规范编号 + 版本 + 核验日期；经验值标注为"参考"，强制要求必须引条号；区分强制 / 推荐 / 指南 / 主管口径四种效力 |
| **⑦ 不假装做到** | 不把建议写成审批结论，不把方案深度当施工图，不把计算器结果当报审值，不把别国数值当本地答案；缺资料就说缺，并给出补齐路径 |
| **⑧ 条文与图纸互串** | 中国资料库里 198 个规范编号与 4335 张图集图纸双向打通：查到条文能列出对应图册与图号，拿到做法图能倒推条文。`ATLAS_ROUTING.md` 给主题表与反向索引，`CODE_RELATIONS.md` 给规范互引链。**图纸只作做法参考，不作合规依据** |

### 能力清单（29 项，按层次）

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

### 十个司法辖区

每个辖区一个专题文件，写清监管体系、规范层级、主管部门与审查重点。**跨辖区只能比较，不能等效替换。**

| 辖区 | 监管体系 | 核心规范 | 审查重点 |
|---|---|---|---|
| 中国 | 国家集中管理 + 强制性条文（D 型） | GB 50352-2019、GB 50016-2014（2018 年版）、GB 50011-2010（2016 修订）、GB 55015-2021、GB 50189-2015、GB 50763-2012、JGJ 系列、地方 DB | 强制性工程建设规范与推荐性标准的区分、日照间距、五类热工气候区节能、六至九度抗震；**香港、澳门单独处理**，不套大陆口径 |
| 美国 | 州与市分别采用模式规范 | IBC 2024、IRC、IECC 2024、IFC、NFPA 101、NFPA 70、ADA 2010、ANSI A117.1、ASCE 7-22、ACI 318、AISC 360、AWC NDS | 州级修订差异极大（CA Title 24、NYC、FL HVHZ、Chicago、MA、WA），AHJ 解释权高于纸面条文 |
| 英国 | 中央法规 + 地方执行，2022 年后责任链重构 | Building Regulations 2010 及 Approved Documents A–S、Building Safety Act 2022、BSR / HRB 制度、BS 9991、BS 9999、BS 8300、NPPF、London Plan | 高风险建筑（HRB）的 Accountable Person 与 Golden Thread 证据链；苏格兰、威尔士、北爱尔兰并非英格兰规则的复制 |
| 德国 | 联邦框架法 + 16 州自订 LBO | MBO、BauGB、BauNVO、GEG 2023、DIN 18040、DIN 4109、DIN 4108、DIN 4102 / EN 13501、Eurocodes 及国家附录 | Sonderbau 专项建筑、Brandschutznachweis 防火证明、DGNB、BAFA/KfW 补贴与 Passivhaus 叠加要求 |
| 日本 | 国家法 + 地方条例 + 民间评价 | Building Standards Act、消防法、City Planning Act、Heart Building Law、AIJ Recommendations、BCJ 结构性能评价、CASBEE | 用途地域、容积率与建蔽率、日影与斜线限制、防火地域、两级抗震设计；体量方案常被规划条款先卡死 |
| 新加坡 | 集中监管（BCA / SCDF / URA 各管一段） | Building Control Act、BCA Regulations、SCDF Fire Code 2018、BCA Code on Accessibility、Green Mark 2021、URA Master Plan、SS EN Eurocodes | ETTV / RTTV 围护指标、消防疏散与维护安全、总体规划符合性；三部门口径须分别确认 |
| 澳大利亚 | NCC 全国统一 + 州级规划与审批 | NCC 2022 Vol 1–3、AS/NZS 1170 系列、AS 3600、AS 4100、AS 1684、AS 1428.1-2021、AS 5113、NatHERS 7-star、BASIX、Green Star、NABERS | 性能条款与"视为符合"条款的取舍、州级审批差异、丛林火灾 / 气旋 / 洪水叠加风险、风区 A–D |
| 印度 | 国家规范 + 州 / 市政开发控制规则 | NBC 2016、ECBC 2017、IS 456、IS 800、IS 875、IS 1893、IS 13920、州级 DCR、RERA、EIA、CRZ、GRIHA、IGBC | 开发控制（FAR、退界、停车）由国家规范与州 / 市政规则共同决定，两者冲突时按更严格者准备 |
| 阿联酋 | 酋长国分立，迪拜与阿布扎比不同体系 | Dubai Building Code 2021、ADIBC、UAE Fire & Life Safety Code 2018、Dubai Universal Design Code、Estidama、Al Sa'fat | 高层与外墙覆层防火、避难层、民防（Civil Defence）预审、主开发商设计指南常严于法定规范 |
| 沙特 | 国家建筑规范 + 专项开发辖区 | SBC 201 系列、SBC 801、Saudi Universal Accessibility Code、Mostadamah、Amana 审批 | NEOM、Qiddiya、红海、Diriyah、AlUla、RCRC、麦加与麦地那可能各有独立审查流程，不能套 SBC 一套走完 |

### 七个计算器

早期设计与交叉校核用，**报审数值必须由持证人员按现行规范重算**。全部只用 Python 标准库。

| 脚本 | 算什么 | 关键参数 | 用在哪 |
|---|---|---|---|
| `area_calculator.py` | 开发密度：GFA、净面积、套数、人口、车位数 | `--site-area` `--far` `--ntg-ratio` `--avg-unit-size` `--persons-per-unit` `--parking-ratio` | 拿地与方案前期的容量校核 |
| `uvalue_calculator.py` | 围护传热系数 U 值（分层构造） | `--layers` `--facade` `--rsi-internal` `--rsi-external` | 节能规范对标、构造比选 |
| `daylight_calculator.py` | 采光系数初算 | `--room-width/depth/height` `--window-width/height/sill-height` `--glazing-transmittance` `--average-reflectance` | 教室、办公、住宅的采光合规预判 |
| `egress_calculator.py` | 疏散宽度与出口数量 | `--floor-area` `--occupancy-type` `--sprinklered` `--num-stories` | 方案阶段就要定的核心筒与楼梯数量 |
| `structural_load_calculator.py` | 荷载汇集与构件初算 | `--tributary-area` `--num-floors` `--dead-load` `--live-load` `--occupancy-type` | 柱网与楼板厚度的量级判断 |
| `energy_calculator.py` | 能耗强度初估 | `--floor-area` `--envelope-area` `--average-u-value` `--heating/cooling-degree-days` `--ventilation-rate` `--internal-gains` | 方案阶段的节能路线比较 |
| `cost_calculator.py` | 造价初估 | `--gfa` `--building-type` `--quality` `--region` `--include-external` | 业主预算与方案取舍 |

---

## 快速开始

### 一、装到哪：按你用的工具

```bash
# Claude Code 插件方式
claude --plugin-dir "/path/to/registered-architect"

# 放进宿主 Agent 的 skills 目录（用你所用工具的实际路径）
cp -R registered-architect ~/.claude/skills/registered-architect
cp -R registered-architect ~/.codex/skills/registered-architect
cp -R registered-architect ~/.workbuddy/skills/registered-architect

# 只做只读参考，不安装
git clone https://github.com/tomatoparkdao/registered-architect.git
```

复制到既有项目时，**必须保留完整的 `skills/` 目录**：模块、参考资料、模板与计算器之间的相对链接一旦断开，路由就失效。

### 二、资料从哪来（三选一）

| 方式 | 怎么做 | 适合 |
|---|---|---|
| **用仓库自带资料** | 直接用 `skills/*/references/`、`skills/country-china/references/standards/`（条文）与 `china-architectural-standards/batch/drawings/`（图纸） | 大多数项目；中国条文分片可全文检索，做法图可按主题定位 |
| **接自己的项目资料** | 把任务书、图纸、当地批文放进项目目录，让它读取后再判断 | 已有设计成果或地方批文 |
| **只用方法论** | 不喂资料，只问"这个阶段该核什么、按哪一版" | 早期策划、方案评审 |

### 三、启动指令

第一次对话直接给出这五项，缺一项它会先问：

```text
国家/城市：阿联酋 迪拜
用途与规模：酒店，18 层，地上 32,000 m²，含裙房餐饮
设计阶段：方案深化，准备报民防预审
已知约束：地块退界 6 m，限高 75 m，主开发商有外墙覆盖要求
要你做的事：核验疏散与无障碍路径，列出待民防确认的问题
```

### 四、启动前必须想清楚的两件事

1. **辖区到城市级**：国家 + 州 / 省 / 酋长国 + 城市 + 特别管辖区（如 NEOM、迪拜的主开发商区域）。只给国家，它只能给国家级口径。
2. **阶段决定深度**：方案阶段核的是分区、疏散、退界与容量；施工图阶段核的是构造、图层、标注与协调。同一句话在不同阶段得到的清单完全不同。

### 五、全程你只需要回答两种话

- **"确认"** —— 这一阶段的口径、版本与结论成立，可以往下走。
- **"要改哪里"** —— 指出位置即可，它会回到对应阶段重算，并把受影响的结论一起作废。

---

## 全流程总览

```text
① 项目理解   地址 / 用地 / 测绘 / 功能 / 面积 / 层数 / 预算 / 阶段
      │      未知项进假设清单，不猜
      ▼
② 法规路由   辖区 → 监管体系 → 主管部门 → 规范层级（强制 / 推荐 / 地方 / 主管口径）
      │      冲突项记优先级；跨辖区只比较、不替换
      ▼
③ 功能与体量 面积表 / 邻接矩阵 / 流线 / 体量选项
      │      同步过日照、风、消防、无障碍、结构、施工，不单指标优化
      ▼
④ 技术协调   结构网格 / 板厚 / 核心筒 / 管井 / 设备房 / 围护 / 竖向交通 / 消防系统 / 遮阳 / 维护路径
      ▼
⑤ 性能验证   面积 / U 值 / 采光 / 疏散 / 荷载 / 能耗 / 声学 / 碳 / 造价
      │      标注是计算器算的、模拟出的，还是工程师复核的
      ▼
⑥ 设计交付   图纸 / 模型 / 表格 / 规范文本 / 材料表 / 审批文件 / 风险登记
             每次修订留版本、日期、原因、责任人
```

### 五条不可协商的专业逻辑

| # | 逻辑 | 落在哪一步 | 破了会怎样 |
|---|---|---|---|
| R1 | **辖区未定，不下合规结论** | 阶段 2 法规路由；识别失败时回落国际参考并要求你确认 | 结论看起来成立，报审阶段被整条推翻，返工从方案重做 |
| R2 | **数值必须带编号、版本与核验日期** | 每条结论、每张性能验证表、每份交付文件 | 无法追溯是哪一版、哪一天，责任边界说不清 |
| R3 | **强制性优先，地方只能更严** | 辖区专题的规范层级与冲突优先级判断 | 用地方规定或指南覆盖强制条文，属于实质性违规 |
| R4 | **计算器只做初算** | 阶段 5 性能验证；`architect-calculator` 全部脚本 | 把工具结果当报审值提交，审查不通过且责任在提交方 |
| R5 | **建议不等于审批** | 全部输出；交付文件的措辞约定 | 建议被读成承诺，签章权与责任边界同时错位 |

## 逐阶段操作细则

| 阶段 | 输入 | 动作 | 输出 |
|---|---|---|---|
| 1 项目理解 | 地址、用地边界、现状测绘、功能、面积、层数、预算、进度、业主目标、运营模式 | 收集并核对基础信息，把未知项写进假设清单，不猜 | 项目摘要 + 关键假设表 |
| 2 法规路由 | 阶段 1 摘要 | 识别主管部门与法规层级，区分强制性要求、推荐指南、主开发商要求、认证条款与业主偏好 | 法规路由表 + 冲突优先级 + 待确认清单 |
| 3 功能与体量 | 法规路由结论 | 建面积表、邻接矩阵、流线；出体量选项并同步看日照、视线、风、消防、无障碍、结构与施工 | 面积表 + 邻接矩阵 + 体量比选 |
| 4 技术协调 | 选定体量 | 定结构网格、楼板厚度、核心筒、管井、设备房、围护系统、竖向交通、消防系统、遮阳与维护路径 | 技术协调清单 + 关键接口表 |
| 5 性能验证 | 技术方案 | 按阶段做面积、U 值、采光、疏散、荷载、能耗、声学、碳与成本计算，标清谁算的 | 性能验证表（计算器 / 模拟 / 工程师复核分列） |
| 6 设计交付 | 全部前置结论 | 出图纸、模型、表格、规范文本、材料表、性能说明、审批文件与风险登记；每次修订留版本、日期、原因、责任人 | 交付包 + 修订记录 |

## 节点动作：平面未确认，不出正式图

这一步和"阶段"不是一回事，它是由阶段结论触发的动作，必须等前面确认完才发生。

| 红线 | 具体规则 | 触发条件 | 为什么这么定 |
|---|---|---|---|
| 平面未确认 | 不出正式平面图、不出报审包、不出施工图深度文件 | 阶段 3 的体量或平面尚未得到业主书面确认 | 一旦出图，业主会当结论用；平面一改，全部作废重出 |
| 辖区未确认 | 不引用具体数值，只写"待确认适用版本" | 路由无法定位到城市、州省或特别辖区 | 引错版本比不引更危险：它看起来像结论，还带着条文号 |
| 未过复核 | 不写"符合规范"，只写"按 X 条核对通过 / 待确认" | 结论涉及消防、结构、无障碍或节能的最终判定 | 写死就变成承诺，而签章权不在工具手里 |

## 规范口径速查

| 口径 | 正确写法 | 常见错误 | 怎么自查 |
|---|---|---|---|
| 条文引用 | GB 50016-2014（2018 年版）第 5.3.1 条 | 只写"规范要求"，不写编号与版本 | 全文搜"规范要求"，每处补编号与条号 |
| 数值 | 12 m（GB 50016-2014 第 5.5.17 条，核验日期 2026-10） | 12 m，无出处、无版本、无日期 | 每个数字后面都该找得到括号 |
| 地方规定 | 地方标准只能更严，不得降低国标要求 | 用地方规定覆盖强制性条文 | 冲突时取更严值，并把两者都写明 |
| 单位 | 统一 SI：面积 m²、长度 m、荷载 kN/m² | 混用 ft / ㎡ / kgf，导致量级错误 | 检查表头是否写明单位 |
| 效力层级 | 强制 > 推荐 > 指南 > 主管口径（口径可严于条文） | 把指南当强制，或把强制当参考 | 每条要求标注属于哪一档 |
| 版本 | 结论旁写核验日期 | 引用 2014 版却按 2018 修订判断 | 版本号与日期必须成对出现 |

## 避坑总表

| 错误 | 后果 | 正确做法 |
|---|---|---|
| 把一个国家的法规数值直接用于另一个国家 | 整套方案在报审阶段被推翻，返工成本最高 | 先做辖区路由，只比较指标与适用范围，不做等效替换 |
| 使用过时版本且不注明核验日期 | 结论不可追溯，责任边界无法界定 | 每条结论写规范编号 + 版本 + 核验日期 |
| 把经验规则当成强制条文 | 误导业主与施工方，埋下验收与索赔风险 | 经验值标注为"参考"，强制要求必须引条号 |
| 只优化平面面积，忽略消防、结构、机电与维护空间 | 后期返工，核心筒与管井无处安放 | 方案阶段就同步过四类专业条件 |
| 只比初始造价，忽略运行与替换成本 | 全生命周期成本反而更高 | 按寿命周期比较，含维护、替换与能耗 |
| 只给结论不给假设 | 无法复核，也无法追责 | 每条判断附假设、证据与待确认事项 |
| 把 AI 建议写成签章、审批或认证结论 | 法律与职业责任风险 | 明确区分"建议 / 核验 / 审批 / 认证"四种性质 |

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
        └── references/
            ├── standards/            # 中国：425 条规范与图集 + 414 份正文分片
            ├── ATLAS_ROUTING.md      # 主题 ↔ 83 本图册 ↔ 198 个规范编号（双向）
            ├── CODE_RELATIONS.md     # 规范互引图谱（587 条边）
            └── china-architectural-standards/
                └── batch/drawings/   # 4335 张图纸：几何 / 图层 / 文字 / 重绘配方
```

## 交付物清单

| 文件 | 内容 | 谁看 |
|---|---|---|
| `01_project-brief.md` | 项目摘要、关键假设、设计阶段与已知约束，作为后续变更比较的全流程基线 | 业主、项目经理、各专业负责人 |
| `02_code-route.md` | 辖区判定、规范层级、版本与核验日期、待确认问题清单及对应主管部门 | 建筑师、AHJ、消防与规划主管部门 |
| `03_program.md` | 功能清单、面积表、邻接关系与容量校核，附面积计算口径与净面积约定 | 业主、运营方、建筑策划顾问 |
| `04_concept-options.md` | 概念、体量比较与环境响应，逐条写明取舍理由、代价与放弃原因 | 业主、评审专家、设计团队 |
| `05_performance.md` | 环境、结构、消防、无障碍性能验证结果与复核分工，标明谁算的 | 各专业顾问、施工图审查机构 |
| `06_materials.md` | 围护与材料策略、等效性能证明、样品封样清单与替代方案 | 材料顾问、承包商、供应商 |
| `07_documentation.md` | 图纸目录、规范文本、BIM 协调记录与各阶段交付深度说明 | 施工方、施工图审查机构 |
| `08_review-log.md` | 审查意见、RFI、ASI 与决策记录，含责任人、时间与关闭状态 | 全项目组、业主代表、审计 |

## 常见问题

| 问题 | 回答 |
|---|---|
| 只适用于中国项目吗？ | 不是。十个辖区各有专题，中国只是其中之一，也是资料最厚的一个（839 份条文 ＋ 4335 张图纸）。无明确辖区时它会回落到国际参考并要求你确认。 |
| 图集图纸能当条文用吗？ | 不能。图册讲的是「怎么做」，规范讲的是「必须怎么做」。抓图只用于核对构造层序与节点表达，合规结论必须落在规范编号与条款上；图纸里未标注的材料与厚度一律按待确认处理。 |
| 有图集但没有对应条文怎么办？ | 两张表都会如实标出缺口：`ATLAS_ROUTING.md` 里主题下没有规范条目的，说明本地资料未覆盖，需补资料或走当地主管部门口径，不能拿图集顶上。 |
| 计算器结果能直接报审吗？ | 不能。计算器用于早期设计与交叉校核；报审数值须由持证人员按现行规范重算并签署。 |
| 项目所在城市没有专门规范怎么办？ | 它会说明缺失，采用上一级规范作暂定参考，并列出需要向 AHJ 或地方规划部门确认的问题清单。 |
| 可以比较不同国家的法规吗？ | 可以，但必须限定比较指标、版本、适用范围，并说明哪些部分不可等效。 |
| 需要联网或外部软件吗？ | 不需要。知识库、模板与计算器全部离线可用；CAD、BIM、渲染与分析软件只是可选对接对象，不是依赖。 |
| 用起来报错、加载不上、或者卡住了怎么办？ | 先下载最新 OmniAiLab 桌面 Agent（[omniailabx.com/plugin#desktop-download](https://www.omniailabx.com/plugin#desktop-download)），它内置本技能最新版本与依赖，多数环境问题装完就消失；仍不通再去 Discord 带上报错原文。 |
| 它的输出算不算设计成果？ | 算设计判断与审查意见的支撑材料，不算可签章的施工图或审批文件。 |

## 推荐工具与模型

本技能不绑定任何工具。下表只是"能对接什么"，不是"必须装什么"。

| 用途 | 可选工具 | 本技能怎么对待 | 没装怎么办 |
|---|---|---|---|
| 读图与出图 | AutoCAD / Revit / ArchiCAD / Rhino | 只作对接；本技能输出判断与清单，不产出 DWG | 用 PDF 图纸或截图也能核，精度降一档并注明 |
| 模型与协调 | IFC / 任意 BIM 协作平台 | 关键尺寸以模型为准，但合规结论仍须复核 | 用二维图纸加尺寸表替代，注明协调未完成 |
| 规范原文 | 主管部门官网、官方标准发布平台 | 内置分片用于检索，采信前须核对官方现行版本 | 用内置分片定位条号，最终以官方文本为准 |
| 条文全文检索 | `grep`、VS Code、任意文本搜索 | 中国 425 条规范 + 414 份分片可全文检索；4335 张图纸的标题与文字标注同样可搜 | 直接读对应模块的 `references/` 目录 |
| 数值计算 | 内置 7 个计算器（Python 3.9+） | 零第三方依赖；结果标注口径与假设 | 手算并写明公式与假设条件 |
| 协同与提问 | [Discord 开源社区](https://discord.gg/vdgTEpXMh3) | 做法讨论、口径争议、问题反馈 | 提 issue，附辖区与规范原文 |

## 基础设备要求

| 项 | 要求 | 为什么 | 不满足会怎样 |
|---|---|---|---|
| 操作系统 | Windows / macOS / Linux | 纯 Markdown 加 Python 标准库，无平台绑定 | 无影响，任意系统都能读，不需要额外运行时 |
| Python | 3.9+（仅计算器需要） | 七个脚本只用 argparse / json / math / sys | 计算器不可用，其余资料照常阅读，只是少了初算这一步 |
| 磁盘 | 约 60 MB | 中国大陆条文分片占大头，其余模块只有几 MB | 可只保留项目需要的辖区，体积降到几 MB |
| 内存 | 无特殊要求 | 按需读取单文件，不做全库索引 | 无影响，老机器也能跑 |
| 网络 | 非必需 | 离线可用；核验现行规范或拉取更新时才需要 | 结论须标注"版本未经在线核验"，报审前补核一次 |
| GPU | 不需要 | 本技能不涉及任何生成式内容 | 无影响；需要效果图时另走 OmniAiLab 平台 |

## 品牌与创作工具独占

| 项 | 规则 | 判定依据 | 违规会怎样 |
|---|---|---|---|
| 规范整理与判据 | OmniAiLab 自有 | 目录组织、交叉索引、判据口径与检查清单由本项目整理撰写 | 失去可追溯性，说不清结论怎么来的 |
| 标准原文 | 引用不转售 | 条文引用标注编号与版本；不打包转售任何标准文本 | 版权风险，且用户可能拿到过期版本 |
| 生成式图像 / 视频 | 不走本技能 | 本技能不产出效果图；需要时交由 OmniAiLab 平台完成 | 效果图被当成尺寸依据，是最常见的误用 |
| 第三方工具 | 只做适配声明 | 不附带其代码，也不依赖其存在 | 用户以为装上就有，实际跑不通 |
| 对外名称 | `registered-architect` / OmniAiLab 全球注册建筑师 | 调用名与显示名不得混用；不是"总设计师" | 定位错位，被当成方案创作工具 |

## 配套操作手册

本仓库不额外发行 PDF 手册，README 即操作说明；深度资料都在仓库内，可离线查阅。

| 想查什么 | 去哪看 | 里面有什么 | 什么时候看 |
|---|---|---|---|
| 调用方式与模块职责 | [SKILL.md](SKILL.md) | 四条工作原则、模块指引、交付内容与免责边界 | 第一次用、或不确定该调哪个模块时 |
| 具体条文与做法 | `skills/<模块>/SKILL.md` + `references/` | 每个模块的方法、判据、红线与专题参考资料 | 手上已有明确任务，需要具体做法时 |
| 中国规范条目 | `skills/country-china/references/standards/` | 425 条规范与图集、414 份正文分片、专题路由表 | 需要定位条号时 |
| 中国图集图纸 | `skills/country-china/references/china-architectural-standards/` | 4335 张图纸、83 本图册、覆盖率与失败清单 | 条文查到了，要立刻看构造大样时 |
| 条文 ↔ 图纸互查 | [ATLAS_ROUTING.md](skills/country-china/references/ATLAS_ROUTING.md) ／ [CODE_RELATIONS.md](skills/country-china/references/CODE_RELATIONS.md) | 主题表、反向索引、规范互引链 | 不知道某个做法该查哪本图册或哪条规范时 |
| 计算器参数与口径 | `skills/architect-calculator/` | 7 个脚本的参数说明、单位约定与计算参考 | 要做量级判断，又不想到处找公式时 |
| 署名与许可 | [LICENSE](LICENSE) | MIT 全文与署名约定 | 二次分发、商用或做衍生作品前 |

## 获取帮助

遇到问题、想讨论口径或提建议——按这个顺序找最省时间：

| 渠道 | 地址 | 适合用来 |
|---|---|---|
| **最新桌面 Agent** | [omniailabx.com/plugin#desktop-download](https://www.omniailabx.com/plugin#desktop-download) | **先装这个**：技能加载失败、资料查不到、计算器报错、结论卡住，都先升级到这里，它内置最新版技能与依赖 |
| **开源社区（Discord）** | [discord.gg/vdgTEpXMh3](https://discord.gg/vdgTEpXMh3) | 做法讨论、口径争议、使用问题；响应最快，也适合认识同行 |
| **仓库 issue** | [tomatoparkdao/registered-architect/issues](https://github.com/tomatoparkdao/registered-architect/issues) | 反馈 bug、提功能建议；留在仓库里便于检索与追踪 |
| **本 README** | [避坑总表](#避坑总表) · [常见问题](#常见问题) | 断网也能查，多数问题在这里就能解决 |
| **中国条文索引** | `skills/country-china/references/standards/` | 找具体规范条目、图集与专题路由 |
| **OmniAiLab 官方** | [omniailabx.com](https://www.omniailabx.com/) | 平台、账号与生态相关；专业方法问题仍走上面几条 |

> 提问时带上**辖区（国家 + 城市）、建筑用途与规模、当前阶段、采用的规范版本与原文**，
> 比"这个合规吗"更容易一次问清。

## 文档地图

| 想了解 | 看这里 | 里面有什么 |
|---|---|---|
| 总入口与工作原则 | [SKILL.md](SKILL.md) | 四条工作原则、模块指引、交付内容与免责边界，是全部模块的共同前提 |
| 十个辖区的法规专题 | `skills/country-*/SKILL.md` | 监管体系、主管部门、规范层级、版本年份、地方修订与审查路径 |
| 中国条文 | `skills/country-china/references/standards/` | 425 条规范与图集条目、414 份正文分片、资料清单与专题路由表 |
| 中国图集图纸 | `skills/country-china/references/china-architectural-standards/` | 4335 张蒸馏图纸（一图一目录）、83 本图册、覆盖率与失败清单 |
| 条文与图纸互查 | [ATLAS_ROUTING.md](skills/country-china/references/ATLAS_ROUTING.md) ／ [CODE_RELATIONS.md](skills/country-china/references/CODE_RELATIONS.md) | 14 个主题的双向检索、198 个编号的反向索引、587 条互引边 |
| 十八项专业能力 | `skills/<模块>/SKILL.md` | 每项能力的方法、判据、红线与参考资料，一模块一文件 |
| 计算器用法 | `skills/architect-calculator/` | 7 个脚本的参数、单位、适用边界与计算参考 |
| 插件元数据 | [.claude-plugin/plugin.json](.claude-plugin/plugin.json) | 调用名、版本、关键词与作者信息，供宿主工具识别 |
| 英文说明 | [README_EN.md](README_EN.md) | 与本文同结构的英文版，章节与表格一一对应 |
| 许可与署名 | [LICENSE](LICENSE) | MIT 全文与署名约定，二次分发前必读 |

## 贡献

本仓库以 **MIT** 许可开源（全文见 [LICENSE](LICENSE)），欢迎参与。贡献遵循一个前提：**只提交可核验的规范口径与专业方法，来源必须写清**——条文编号、版本年份、官方出处缺一不可。

| 方向 | 具体内容 | 提交位置 | 验收标准 |
|---|---|---|---|
| 新增辖区专题 | 监管体系、主管部门、规范层级与审查路径 | `skills/country-<辖区>/` | 每条要求能核验到官方来源，注明版本年份 |
| 补充专业模块 | 一项能力的职责、输入、判据与红线 | `skills/<模块>/` | 结构对齐现有 18 份，含 front-matter 与署名 |
| 补充条文资料 | 可公开引用的条文摘要与图集索引 | `skills/country-china/references/standards/` | 标注编号、版本、出处，不整段复制受版权保护文本 |
| 修正与补全 | 错字、过时口径、断链、计数不一致、表格未撑满、中英文不同步 | 直接提 PR 或 issue | 改动范围单一，说明复现步骤与依据 |
| 新增外部依赖 | 先做许可核查并在 PR 中说明来源 | 见 [LICENSE](LICENSE) | 缺来源说明不与合并 |

**改完至少跑这两条**：

```bash
python -m py_compile skills/architect-calculator/scripts/*.py       # 计算器语法检查
python skills/architect-calculator/scripts/area_calculator.py --site-area 5000 --far 2.5 --json
```

讨论与结对修改在 [Discord 开源社区](https://discord.gg/vdgTEpXMh3) 进行；正式结论请落到 issue 或 PR，便于追溯。

## 许可与法律

| 项 | 内容 |
|---|---|
| 本仓库许可 | **MIT**，全文见 [LICENSE](LICENSE) |
| 标准文本 | 条文仅作引用与索引，版权归原发布机构；不转售、不打包分发标准全文 |
| 署名硬约定 | 每份 Markdown 的 front-matter 含 `author: OmniAiLab` / `developer: Mochiball`，开头与结尾各附标准署名行 |
| 不得冒充自主开发 | 不把第三方文档或标准文本宣称为 OmniAiLab 原创 |
| 免责 | 结构安全、消防、无障碍、机电负荷与当地法规符合性不在本系统结论范围内，须由持证专业人员在项目所在地复核签署；方案深度成果不得当作施工图；计算器结果不得作为报审数值；造价为方案阶段估算，不构成结算依据 |
| 责任限制 | 使用本 Skill 直接或间接造成的任何损失，作者与维护者不承担责任 |

## 出处与致谢

- 出品与维护：**OmniAiLab**（[omniailabx.com](https://www.omniailabx.com/)）
- 开发者：**Mochiball**
- 规范整理（[`skills/`](skills/)）、辖区专题与判据口径由本项目**独立整理撰写**，来源为各国公开发布的规范文本与通用工程惯例；不复制、不改写任何第三方文档，条文引用仅到编号与版本层级。
- 本 Skill 不产出图像与视频；确需效果图时交由 **OmniAiLab** 平台完成，且不得作为尺寸依据。
- 对 AutoCAD / Revit / ArchiCAD / IFC 等工具只做**适配声明与降级路径**，不附带其代码，也不依赖其存在。
- 开源社区：[Discord · discord.gg/vdgTEpXMh3](https://discord.gg/vdgTEpXMh3) —— 用法讨论、口径争议与贡献协作都在这里。

---

<div align="right">

**简体中文** ｜ [English](README_EN.md)

</div>

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
