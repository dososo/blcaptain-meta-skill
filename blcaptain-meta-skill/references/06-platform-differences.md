# 平台差异

## 加载时机

当需要适配 Claude Skills、Codex Skills、通用 Agent Skills，或需要说明安装路径、元数据、验证工具和平台边界时加载。

## 差异速览

| 维度 | Claude Skills | Codex Skills | 通用 Agent Skills |
| --- | --- | --- | --- |
| 入口 | `SKILL.md` 与资源目录 | 技能目录、项目规则、插件、工具上下文 | 任意可被发现和加载的能力包 |
| 路由 | frontmatter、描述、上下文 | 技能描述、项目规则、工具元数据、用户请求 | name、description、manifest、索引 |
| 资源 | `references/`、`scripts/`、`assets/` | 取决于 Codex 环境和插件能力 | 平台自定义 |
| 验证 | 触发、执行、资源加载、forward-test | 结构校验、工具调用、项目规则遵守 | 路由、执行、权限、可移植 |

## Codex 适配

- `SKILL.md` frontmatter 只放 `name` 和 `description`。
- 新建 Skill 时优先使用官方 `skill-creator/scripts/init_skill.py`。
- UI 元数据放 `agents/openai.yaml`。
- 用 `quick_validate.py` 做基础结构校验。
- 保持入口短，资源按需加载。

## Claude 适配

- 保持标准 `SKILL.md` 入口。
- 明确资源目录用途。
- 避免把平台外字段塞进入口正文。
- forward-test 时用 fresh context。

## 通用适配

- 保留 `manifest.json`，说明 owner、version、review cadence、maturity、risk。
- 将平台差异写成 adapter 说明，不假设各平台字段对称。
- 不把某个平台的工具路径写成唯一真理。

## 发布说明边界

有些平台不建议在 Skill 包里放 README、安装指南、宣传页。人类发布页可以放仓库外层、网站或社区，不必进入 Agent 会加载的 Skill 目录。

