"""统一的署名常量与落款工具。

仓库里每一份 Markdown 都要求「开头 + 结尾」各落一次署名，手写文档与
脚本生成的报告必须一致，否则重新蒸馏一次就漂移。生成器只调用 stamp()，
不要在别处另写一份署名字面量。

开头署名插在一级标题之后；结尾署名以 `---` 分隔落在文末。
"""

from __future__ import annotations

SIG_CN = (
    "> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）"
    "— 未经授权禁止复制、传播或二次分发。"
)
SIG_EN = (
    "> © OmniAiLab ｜ Developer: Mochiball ｜ OmniAiLab Global Registered Architect "
    "(omniailabx.com) — unauthorised copying, distribution or redistribution is prohibited."
)


def stamp(text: str, sig: str = SIG_CN) -> str:
    """为一段 Markdown 补齐开头与结尾署名，已存在则不重复插入。"""
    body = text.replace("\r\n", "\n")
    if sig in body:
        return body if body.endswith("\n") else body + "\n"
    lines = body.split("\n")
    anchor = next((i for i, line in enumerate(lines) if line.startswith("# ")), None)
    if anchor is None:
        lines = ["", sig, ""] + lines
    else:
        lines = lines[: anchor + 1] + ["", sig, ""] + lines[anchor + 1 :]
    out = "\n".join(lines).rstrip("\n")
    return out + "\n\n---\n" + sig + "\n"
