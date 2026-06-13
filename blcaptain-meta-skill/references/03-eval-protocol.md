# Eval 协议

## 加载时机

当需要设计、运行或审计 Skill 的路由测试、执行测试、失败库、fresh context、near-neighbor 或回归测试时加载。

## 测试矩阵

| 类型 | 目的 |
| --- | --- |
| 基线测试 | 记录无 Skill 时怎么失败 |
| 正例测试 | 应触发时能触发 |
| 反例测试 | 不应触发时不误触发 |
| 近邻测试 | 相似任务不污染其他 Skill |
| 执行测试 | 能产出合格交付物 |
| 压力测试 | 长输入、脏数据、多约束下稳定 |
| 回归测试 | 修改后不破坏旧能力 |

## 最低用例数

| 层级 | 最低用例 |
| --- | --- |
| Scaffold | 1 个真实输入 + 3 条路由用例 |
| Production | 3-5 个执行用例 + 正反例近邻 |
| Library | 5+ 执行用例 + 分组回归 |
| Governed | Library + 回归历史 + 晋升策略 |

## 强制规则

- forbidden-load 必须在 fresh context 或独立环境中测。
- near-neighbor 必须在多 Skill 环境中测。
- 基线测试要记录无 Skill 失败，不只记录有 Skill 成功。
- 改 description 重跑反例。
- 改正文重跑执行用例。
- 失败必须进入 gotcha、failure library 或 eval。

## Eval Result 模板

```markdown
# Eval Result

## 用例 ID
## 类型
正例 / 反例 / 近邻 / 执行 / 压力 / 回归

## Fresh context
是 / 否

## 多 Skill 环境
是 / 否

## 期望行为
## 实际行为
## 通过
是 / 否

## 失败原因
## 是否需要改 description
## 是否需要改 SKILL.md
## 是否需要新增 gotcha
```

## 失败库模板

```markdown
# Failure Case

## 失败族群
## 用户请求
## 错误行为
## 正确行为
## 应触发 / 不应触发
## 需要新增或修改的 eval
## 是否需要修改 description
```

## 常见失败族群

- `one-off-vs-reusable`：一次性问题被包装成 Skill。
- `explain-not-package`：用户只是想理解概念，却被引导建包。
- `document-export-vs-agent-skill`：用户要文档，不需要 Agent 执行能力。
- `future-outline-vs-build`：用户只是设想未来方向，却被直接开发。
- `route-near-neighbor`：相似任务误触发本 Skill。
- `context-bloat`：正文越来越长，资源分层失效。

## 工具边界

`scripts/eval_routes.py` 只验证 eval 语料结构和信号覆盖，不等同于真实模型路由。真实发布前仍需用 fresh context 或独立 Agent forward-test。

