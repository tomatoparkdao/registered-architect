# 注册建筑师技能包

> [English README](README.md)

本技能包以 `registered-architect` 为总入口，面向中国大陆注册建筑师的方案设计、技术协调、规范审查与施工图工作。它基于 Architect Skills 框架，包含建筑设计全流程模块，以及中国大陆规范与审批专题资料。

## 使用范围

- 方案设计、建筑策划、建筑类型与空间规划
- 建筑防火、疏散、无障碍、声学、日照与围护设计
- 结构体系、机电协调、材料选择、绿色建筑与施工图文件
- 中国大陆项目的国家标准、地方补充标准、审批流程、气候和抗震条件梳理

规范资料仅用于辅助设计判断。对任何数值限值、条文引用或合规结论，均须核验项目所在地现行的国家强制性标准、地方标准和主管部门要求。

## 快速开始

本技能包的总入口为 [SKILL.md](SKILL.md)。中国大陆项目先阅读 [country-china](skills/country-china/SKILL.md)，再按任务选择 `skills/` 下的专项模块。

若将其作为 Claude Code 插件使用：

```bash
claude --plugin-dir "/path/to/registered-architect"
```

若复制到既有项目，请保留完整的 `skills/` 目录，以维持模块、参考资料、模板和计算器之间的链接关系。

## 技能模块

| 范畴 | 主要模块 |
| --- | --- |
| 基础与地区 | `architect-foundations`、`geographic-foundations`、`country-china` |
| 设计与策划 | `design-theory`、`concept-design`、`building-programming`、`building-typology`、`spatial-planning` |
| 技术设计 | `building-envelope`、`structural-systems`、`building-services`、`daylighting-design`、`material-selection`、`acoustic-design` |
| 规范与交付 | `building-codes`、`fire-life-safety`、`accessibility-design`、`building-sustainability`、`construction-documentation` |
| 计算工具 | `architect-calculator`：面积、传热系数、日照、疏散、结构荷载、能耗与成本计算 |

## 使用原则

1. 先明确项目所在地、建筑类型、高度、面积、火灾危险类别和设计阶段。
2. 中国大陆项目应优先适用中国国家标准与项目所在地地方标准；不要直接套用国际示例的数值。
3. 香港、澳门、台湾与中国大陆适用不同的监管体系，应分别确认。
4. 计算器结果仅为辅助数据，必须复核输入条件、单位和对应规范。
5. 输出审查意见时，应列出适用地区、待核验的标准版本、关键约束、设计响应和后续核验事项。

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
