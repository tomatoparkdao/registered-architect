---
name: registered-architect
description: 面向全球注册建筑师与建筑设计专业人员的方案设计、规范审查、消防、无障碍、建筑技术与施工图工作。根据项目所在国家、地区、城市及适用规范路由到相应的法规专题；在作出合规结论前，必须核验现行强制性标准与地方要求。
version: 1.1.0
license: MIT（OmniAiLab）—— 见 LICENSE
platform: OmniAiLab
author: OmniAiLab
developer: Mochiball
agent_created: true
开源仓库: https://github.com/tomatoparkdao/registered-architect
---

# Registered Architect · 全球注册建筑师专业框架

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。

本技能包服务于全球注册建筑师和建筑设计专业人员，覆盖设计理论、功能策划、建筑类型、空间规划、围护结构、结构、机电、采光、声学、消防、无障碍、可持续性、材料、施工图和十个国家/地区法规专题。它提供设计决策与规范核验的工作框架，不替代当地注册专业人员、主管部门或现行法律法规。

## 工作原则

- 应用要求前，先明确项目所在地、建筑类型、高度、面积、火灾危险类别与设计阶段。
- 技能包内资料仅作设计指引，不是最终法律依据。涉及合规结论、数值限值或条文引用时，必须核验现行国家强制性标准、适用地方标准及主管部门要求。
- 优先采用适用的更严格强制性要求；明确说明假设条件、尚未确认的地方要求，以及需要由注册专业人员或主管部门复核的事项。
- 除非任务明确要求比较，否则应将不同国家、地区、城市、州、省、郡、酋长国或特别管辖区的规范体系分别处理。

## 模块指引

- 中国大陆的规范背景、审批、气候、抗震条件、地方补充标准与规范路由，先阅读 `skills/country-china/SKILL.md`。
- 生命安全与合规工作使用 `skills/fire-life-safety/SKILL.md`、`skills/accessibility-design/SKILL.md` 和 `skills/building-codes/SKILL.md`；中国规范要求优先于其中的国际示例。
- 功能策划、建筑类型、空间规划、围护、结构、MEP、采光、声学、可持续性、材料或施工图工作，使用 `skills/` 下对应的设计模块。
- 仅在确认输入、单位和适用地区假设后，才可使用 `skills/architect-calculator/scripts/` 下的计算器；受规范控制的决策必须独立复核。

## 交付内容

提供设计审查或建议时，应说明：待确认的适用地区与标准版本、适用约束、设计响应和后续核验事项。不得将初步建议表述为审批结论或认证结果。

## 开源社区

用法讨论、口径争议与问题反馈走开源社区：[Discord · discord.gg/vdgTEpXMh3](https://discord.gg/vdgTEpXMh3)。可复现的问题与功能建议请同时落到仓库 issue，便于检索与追踪。

---
> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
