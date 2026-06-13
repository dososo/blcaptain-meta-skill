# 治理、发布与运营

## 加载时机

当 Skill 进入团队复用、公开发布、社区运营、版本迭代、治理审计或废弃迁移时加载。

## 治理元数据

可复用或更高层级 Skill 应声明：

```json
{
  "name": "skill-name",
  "version": "0.1.0",
  "owner": "person-or-team",
  "updated_at": "YYYY-MM-DD",
  "review_cadence": "monthly | quarterly | per-release",
  "status": "experimental | active | deprecated",
  "maturity_tier": "scaffold | production | library | governed",
  "lifecycle_stage": "scaffold | production | library | governed"
}
```

## 发布前检查

- 用户 30 秒内能理解解决什么问题。
- 用户 3 分钟内能跑第一个例子。
- 至少有一个高质量结果展示。
- 安装和调用路径清楚。
- 有反馈渠道。
- 有正例、反例、近邻和回归证据。

## 运营飞轮

```text
真实任务
→ 高质量交付
→ 沉淀 Skill
→ 产出案例
→ 内容分发
→ 用户反馈
→ gotchas / eval / 模板更新
→ 新版本
→ 更多真实任务
```

## 指标分层

创作者可观察：

- 自己复用次数。
- 首次样例成功率。
- issue / 评论 / 用户失败点。
- star / fork / 收藏 / 转发。
- 用户案例投稿。
- 模板或 PR 贡献。

平台或组织级：

- 激活率。
- 首次成功率。
- 复用率。
- 失败率。
- 误触发率。
- 留存率。

不要把拿不到的平台遥测伪装成个人创作者指标。

## 迭代记录

```markdown
# Skill 迭代记录

## 版本
## 触发原因
## 用户反馈 / 失败案例
## 修改内容
## 新增 eval
## 新增 gotchas
## 回归测试结果
## 残余风险
```

## 晋升与降级

- Scaffold 到 Production：出现稳定复用和真实路由需求。
- Production 到 Library：多团队或跨项目共享。
- Library 到 Governed：关键业务、合规、基础设施或 meta skill。
- 降级：长期无人使用、维护成本高、误触发严重或已有更好替代。

