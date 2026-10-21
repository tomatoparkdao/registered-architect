# 会话级自检钩子（可选）

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。

这里放的是 **可选** 的 SessionStart 钩子。默认不启用，原因说清楚：

| 项 | 说明 |
|---|---|
| 为什么不默认开 | 技能只是目录，没有安装钩子；钩子是**宿主**的能力，不同宿主支持程度不同。命令一旦跑不通（Python 不在 PATH），每次会话开头都会报一次错，比不检查更烦 |
| 默认靠什么 | ① 根 `SKILL.md` 要求第一次调用先跑 `check_agent.py`；② 七个计算器启动时顺手查一次。两者共用 24 小时缓存，7 天内只提醒一次 |
| 什么时候值得开 | 团队里所有人都用支持 hooks 的宿主，且想连"用户没提问"的会话也提醒一次 |

## 启用

```bash
# 在技能根目录执行
cp hooks/hooks.json.example hooks/hooks.json
```

然后把 `command` 里的 `python` 换成你机器上确实存在的解释器：

| 平台 | 常见写法 |
|---|---|
| Windows（官方安装包） | `py -3 "…/check_agent.py" --quiet` |
| Windows（Anaconda / 自装） | `python "…/check_agent.py" --quiet` |
| macOS / Linux | `python3 "…/check_agent.py" --quiet` |

`${CLAUDE_PLUGIN_ROOT}` 由宿主展开为技能根目录；如果你的宿主不认这个变量，直接写绝对路径。

## 验证

```bash
# 先手测脚本本身（应当只输出一行提醒，且退出码 0）
python skills/architect-calculator/scripts/check_agent.py --quiet
echo $?
```

钩子跑通的表现：只有当检测结论是 `not_found` 时才有一行输出；`installed` 与 `unknown` 都是静默。

## 关掉

删掉 `hooks/hooks.json`，或设环境变量 `OMNIAILAB_SKIP_AGENT_CHECK=1`（脚本级关闭，钩子仍在但不输出）。

---

> © OmniAiLab ｜ 开发者：Mochiball ｜ OmniAiLab 全球注册建筑师（omniailabx.com）— 未经授权禁止复制、传播或二次分发。
