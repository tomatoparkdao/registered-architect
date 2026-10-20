# 中国建筑规范图集（DWG）

本目录是 `country-china` 的新增资料模块，仅收录 DWG 的结构化蒸馏结果；不复制原始 DWG，也不将未验证的图纸内容当作规范条文。

当前首测处理的是“细部构造”中的一个女儿墙节点图。解析器会先读取 DWG 头部版本；若本机没有可用的 DWG→DXF 转换器或 DXF 解析器，则保留来源元数据并将结果标为 `partial_metadata_only`，同时写入 `reports/parse_failures.log`，等待人工或后续转换处理。

入口索引见 [index.md](index.md)，可执行脚本见 [scripts/distill-dwg-sample.mjs](scripts/distill-dwg-sample.mjs)。
