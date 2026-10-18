# 全球注册建筑师技能框架

> [English README](README.md)

本技能包以 `registered-architect` 为总入口，面向全球注册建筑师与建筑设计专业人员，覆盖从设计理论到施工图文件的建筑全流程，并提供印度、阿联酋、沙特、美国、英国、德国、新加坡、日本、中国和澳大利亚十个国家/地区的法规专题。各国资料用于路由和核验，不替代当地注册专业人员或主管部门。

## 使用范围

- 方案设计、建筑策划、建筑类型与空间规划
- 建筑防火、疏散、无障碍、声学、日照与围护设计
- 结构体系、机电协调、材料选择、绿色建筑与施工图文件
- 十个国家/地区的国家、州、省、城市、酋长国及特别管辖区法规资料

规范资料仅用于辅助设计判断。对任何数值限值、条文引用或合规结论，均须核验项目所在地现行的国家强制性标准、地方标准和主管部门要求。

## 快速开始

本技能包的总入口为 [SKILL.md](SKILL.md)。先根据项目国家、地区和城市阅读 `geographic-foundations` 及对应国家专题，再按任务选择 `skills/` 下的专项模块。

若将其作为 Claude Code 插件使用：

```bash
claude --plugin-dir "/path/to/registered-architect"
```

若复制到既有项目，请保留完整的 `skills/` 目录，以维持模块、参考资料、模板和计算器之间的链接关系。

## 技能模块

| 范畴 | 主要模块 |
| --- | --- |
| 基础与地区 | `architect-foundations`、`geographic-foundations`、十个国家/地区专题 |
| 设计与策划 | `design-theory`、`concept-design`、`building-programming`、`building-typology`、`spatial-planning` |
| 技术设计 | `building-envelope`、`structural-systems`、`building-services`、`daylighting-design`、`material-selection`、`acoustic-design` |
| 规范与交付 | `building-codes`、`fire-life-safety`、`accessibility-design`、`building-sustainability`、`construction-documentation` |
| 计算工具 | `architect-calculator`：面积、传热系数、日照、疏散、结构荷载、能耗与成本计算 |

## 使用原则

1. 先明确项目所在地、建筑类型、高度、面积、火灾危险类别和设计阶段。
2. 应优先适用项目所在地现行强制性标准、地方标准和主管部门要求；不要直接套用其他国家的数值。
3. 不同国家、地区、州、省、城市和特别管辖区可能采用不同监管体系，应分别确认。
4. 计算器结果仅为辅助数据，必须复核输入条件、单位和对应规范。
5. 输出审查意见时，应列出适用地区、待核验的标准版本、关键约束、设计响应和后续核验事项。

## 工作机制

技能采用渐进式加载：总入口先识别项目语境，再调用基础知识、专项技能、参考文件、模板和计算脚本。这样可在保持上下文精简的同时，按需加载深度资料。

### 三层上下文

| 层级 | 加载内容 | 加载时机 |
| --- | --- | --- |
| 第 0 层 | 技能名称和描述 | 始终可用 |
| 第 1 层 | 对应 `SKILL.md` 正文 | 调用专项技能时 |
| 第 2 层 | 参考文件、模板和脚本 | 明确需要时 |

### 专项模块路由

- 基础层：建筑师与理论家、定量经验规则、建筑类型分类、设计质量框架和反模式目录。
- 设计层：设计理论、概念设计、建筑策划、建筑类型和空间规划。
- 技术层：围护结构、结构体系、建筑服务、采光、声学和材料选择。
- 合规层：建筑规范、消防生命安全、无障碍和可持续性。
- 交付层：施工图文件、规范编制和计算器。

## 计算器

`architect-calculator` 包含七个 Python 计算器，分别用于面积策划、传热系数、日照估算、疏散合规、结构荷载、能源需求和成本估算。使用计算器前应确认单位、输入边界和适用地区；计算结果不能单独作为审批或认证结论。

## 国家/地区法规专题

技能包提供以下法规路由：

- 印度：NBC、ECBC、IS 系列、州级 DCR、GRIHA、IGBC、RERA、EIA、CRZ 和 DGCA。
- 阿联酋：Dubai Building Code、ADIBC、UAE Fire & Life Safety Code、Estidama、Al Sa'fat 和无障碍规范。
- 沙特：SBC 系列、Mostadamah、Saudi Universal Accessibility Code 以及 NEOM、Qiddiya、红海、Diriyah、AlUla 等专项辖区。
- 美国：IBC、IRC、IECC、IFC、NFPA、ADA、ASCE、ACI、AISC、AWC 以及州和城市规范。
- 英国：Building Regulations、Approved Documents、Building Safety Act、BS 规范、BREEAM、London Plan 及苏格兰、威尔士、北爱尔兰体系。
- 德国：MBO、各州 LBO、GEG、DIN、Eurocodes、Sonderbau、DGNB 和 Passivhaus。
- 新加坡：BCA、SCDF Fire Code、Green Mark、Code on Accessibility、URA 和新加坡国家附录。
- 日本：Building Standards Act、消防法、两级抗震、AIJ、BCJ、CASBEE 和城市计划法规。
- 中国：GB、JGJ、地方 DB、绿色建筑标识、日照、气候分区和抗震烈度体系。
- 澳大利亚：NCC、AS/NZS、州级规划、Green Star、NABERS、NatHERS 和风区体系。

## 目录说明

## 技能使用详解

### 基础与理论

`architect-foundations` 是自动加载的基础层，提供建筑师与理论家速查、定量经验规则、建筑类型分类、设计质量框架、反模式目录和技能路由。`design-theory` 用于建筑理论、设计哲学、建筑思潮、宣言、先例分析和设计批评。`concept-design` 用于概念生成、体量研究、形态策略、视线廊道、日照包络和风环境评估。

### 功能策划与建筑类型

`building-programming` 处理任务书、面积标准、邻接关系、人员和设备清单、功能分区及容量验证。`building-typology` 提供住宅、办公、商业、酒店、教育、医疗、文化、工业和特殊建筑的类型学比较。`spatial-planning` 处理核心筒、交通流线、净得率、服务空间、楼层组织、装卸和停车。

### 技术设计

`building-envelope` 涵盖墙体、屋面、玻璃、幕墙、保温、防潮、气密、水密和耐久性。`structural-systems` 比较钢筋混凝土、钢结构、木结构、砌体、预制和复合结构，并提供跨度、柱网、楼板和荷载路径参考。`building-services` 涵盖暖通空调、给排水、电气、消防机电、竖井、设备房、屋面设备和机电协调。

`daylighting-design` 处理日光因子、sDA、ASE、太阳几何、遮阳、采光中庭、锯齿形屋顶和日照模拟。`acoustic-design` 处理空气声、撞击声、侧向传声、混响、清晰度、隔振和演出空间声学。`material-selection` 处理材料性能、成本、生命周期、隐含碳、耐火、声学、耐久性和规范编制。

### 合规、可持续与交付

`building-codes` 提供国际规范体系、使用分类、结构、防火、能耗和无障碍的交叉参考。`fire-life-safety` 处理防火分区、疏散、楼梯、消防电梯、报警、喷淋、烟控和消防车道。`accessibility-design` 处理通用设计、无障碍路径、坡道、电梯、卫生间、停车和感官无障碍。

`building-sustainability` 处理能源、运营碳、隐含碳、被动式设计、绿色屋顶、雨水、再利用以及 LEED、BREEAM、WELL、Green Star、NABERS、DGNB、CASBEE、Estidama 和 Mostadamah。`construction-documentation` 处理图纸组织、图层、线宽、标注、LOD、规范、BIM、RFI、ASI、样板、现场质量和竣工资料。

## 示例提示词

以下提示词可作为工作入口，实际任务应补充地点、规模、用途、预算、阶段和法规版本：

1. “为北纬 40° 的 12 层住宅比较三种体量方案，说明日照、风环境、结构和消防影响。”
2. “根据新加坡 SCDF Fire Code 和 BCA Code on Accessibility，审查这个酒店的疏散与无障碍方案。”
3. “为 5,000 m² 办公楼生成面积表、邻接矩阵、核心筒选项和初步柱网。”
4. “比较双层玻璃、三层玻璃和动态玻璃的 U 值、SHGC、VLT、成本和生命周期影响。”
5. “针对英国项目建立围护结构、BREEAM、声学和施工图交付检查清单。”
6. “核验印度 NBC 使用分类、耐火分隔、停车、FAR 和无障碍要求，并列出待向主管部门确认的事项。”
7. “使用计算器估算 2,000 m² 建筑的传热系数、疏散容量、结构荷载和初步成本。”
8. “根据已确认平面方案生成材料策略、门窗表、房间声学目标和施工图备注。”

## 结果与责任边界

技能输出可以是设计判断、备选方案、表格、计算结果、检查清单、规范路由和后续行动建议。输出不得被描述为建筑许可、消防审查、结构签章、能源认证或无障碍认证。对于生命安全、结构安全、火灾、卫生、无障碍和能源等高风险事项，必须由具备当地资质的专业人员复核。

如输入信息不足，应明确列出缺失项，而不是自行假定关键条件。对于法规不确定性，应同时列出采用的版本、判断依据、可能的地方差异以及需要向 AHJ、规划部门、消防部门或其他主管机构确认的问题。

## 工具和兼容性

技能可以在支持 Markdown 技能加载的 Agent 环境中使用。计算器使用 Python 标准库和项目内脚本；不要求注册外部平台，也不要求联网才能阅读或使用基本知识。外部 CAD、BIM、渲染、分析和协作软件仅作为可选适配对象，不能被视为本技能的必需依赖。

路径、文件名、技能名、脚本名、命令、API 参数、YAML 字段、JSON Key、标准编号和专业缩写必须保持原样，以便 Agent 正确识别和调用。翻译只改变自然语言说明，不改变程序逻辑和数据结构。

## 文件结构

```text
registered-architect/
├── SKILL.md                         # 全球注册建筑师总入口
├── README.md                        # English README
├── README.zh-CN.md                  # 简体中文 README
├── LICENSE                          # OmniAiLab MIT License
├── skills/                          # 设计、技术、合规和国家专题
│   ├── architect-foundations/
│   ├── geographic-foundations/
│   ├── architect-calculator/
│   ├── country-*/
│   └── ...
└── .claude-plugin/                 # 插件元数据
```

## 质量控制

- 每项规范结论都应注明地区、版本、条款或参考来源。
- 每项定量计算都应注明单位、输入、假设和适用范围。
- 每个方案比较都应同时说明性能、成本、施工、维护和风险。
- 每份交付文件都应进行结构、链接、路径、代码块和表格完整性检查。
- 所有法规、产品、价格、软件和认证信息都应在项目启动时重新核对时效性。

## 内容组织

```text
registered-architect/
├── SKILL.md                         # 技能总入口
├── skills/                          # 专项技能模块
│   ├── country-china/               # 中国大陆规范与实践资料
│   ├── architect-calculator/        # 计算器与计算参考
│   └── ...
├── README.md                        # English README
└── README.zh-CN.md                  # 中文 README
```

## 许可证与来源

本包采用 OmniAiLab MIT License，许可文本见 [LICENSE](LICENSE)。

## 专项技能索引

| 编号 | 技能 | 主要用途 |
| --- | --- | --- |
| 1 | `architect-foundations` | 建筑基础知识、理论家、定量规则和技能路由 |
| 2 | `geographic-foundations` | 国家、地区、气候和法规路由 |
| 3 | `design-theory` | 建筑理论、设计哲学、思潮和宣言 |
| 4 | `concept-design` | 概念生成、体量、形态和设计策略 |
| 5 | `building-programming` | 功能策划、面积标准、邻接关系和任务书 |
| 6 | `building-typology` | 住宅、办公、商业、教育、医疗和文化建筑类型 |
| 7 | `spatial-planning` | 核心筒、空间组织、流线和面积效率 |
| 8 | `building-envelope` | 墙体、屋面、玻璃、幕墙和热工性能 |
| 9 | `structural-systems` | 结构体系、跨度、荷载路径和构造类型 |
| 10 | `building-services` | HVAC、给排水、电气、机房和机电协调 |
| 11 | `daylighting-design` | 日光、太阳几何、遮阳和模拟 |
| 12 | `acoustic-design` | 隔声、房间声学、混响和噪声控制 |
| 13 | `material-selection` | 材料性能、生命周期、成本和规范编制 |
| 14 | `fire-life-safety` | 防火分区、疏散、报警、喷淋和消防策略 |
| 15 | `accessibility-design` | 无障碍、通用设计和国际法规比较 |
| 16 | `building-codes` | IBC、Eurocodes、NCC、NBC 和全球规范框架 |
| 17 | `building-sustainability` | 能源、碳、认证、被动式设计和水资源 |
| 18 | `construction-documentation` | 图纸标准、规范、BIM、RFI 和施工管理 |
| 19 | `architect-calculator` | 面积、U 值、日照、疏散、结构、能源和成本计算 |

## 交付前检查清单

1. 确认项目所在地、主管部门和适用法规版本。
2. 确认建筑用途、使用人数、面积、高度、层数和火灾危险类别。
3. 确认结构体系、围护性能、机电系统和无障碍路径。
4. 对关键尺寸、荷载、耐火、能耗、日照和声学指标进行独立复核。
5. 区分设计建议、规范核验、审批意见和专业认证结论。
6. 记录所有假设、缺失信息、待确认事项和后续责任人。

## 统计概览

| 项目 | 数量或范围 |
| --- | --- |
| 核心技能 | 18 项 |
| 地理法规专题 | 10 个国家/地区 |
| Python 计算器 | 7 个 |
| 建筑师与理论家 | 50+ |
| 建筑思潮 | 20+ |
| 可持续性认证框架 | 8+ |
| 建筑类型 | 28+ |
| 结构体系 | 15+ |
| HVAC 系统类型 | 12+ |
| 墙体构造 | 15+ |
| 楼板构造 | 11+ |
| 玻璃构造 | 14+ |
| 材料吸声系数 | 32+ |
| 参考建筑案例 | 100+ |
| 尺寸标准 | 200+ |

## 版本与维护

当前版本为 `1.0.0`。法规、标准、软件和认证体系具有时效性；每次项目使用前均应核对现行版本，并在项目记录中注明核验日期。

本 README 与英文 README 使用相同的章节组织、技能范围、法规专题、计算器说明、统计项目和许可证信息；英文名称、规范编号、程序标识符、路径和命令保持原样，以确保 Agent 能够正确识别和调用。

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab AI 建筑与室内设计总设计师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
