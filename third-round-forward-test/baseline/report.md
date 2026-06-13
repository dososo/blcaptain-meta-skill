# fresh-context baseline 测试报告

## 结论

- 是否使用 `blcaptain-meta-skill`：否。
- 是否读取 `blcaptain-meta-skill/` 中的方法论文件：否。
- 是否调用 `$blcaptain-meta-skill`：否。
- 使用的创建依据：官方 `skill-creator` 指南与脚本。
- 写入范围：仅写入本报告和 `third-round-forward-test/baseline/no-skill-xhs-article-card-pack/`。

## 创建的文件

- `third-round-forward-test/baseline/no-skill-xhs-article-card-pack/SKILL.md`
- `third-round-forward-test/baseline/no-skill-xhs-article-card-pack/agents/openai.yaml`
- `third-round-forward-test/baseline/no-skill-xhs-article-card-pack/references/xhs-six-card-system.md`
- `third-round-forward-test/baseline/no-skill-xhs-article-card-pack/references/visual-production-spec.md`
- `third-round-forward-test/baseline/no-skill-xhs-article-card-pack/scripts/plan_xhs_cards.py`
- `third-round-forward-test/baseline/report.md`

## 命令与输出

### 1. 确认工作目录

```bash
pwd
```

输出：

```text
${PROJECT_ROOT}
```

### 2. 读取官方 skill 创建说明

```bash
sed -n '1,260p' ${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/SKILL.md
sed -n '261,520p' ${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/SKILL.md
sed -n '1,260p' ${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/references/openai_yaml.md
```

输出摘要：

```text
读取成功。确认 skill 需要 SKILL.md；建议包含 agents/openai.yaml；新建 skill 应运行 init_skill.py；完成后运行 quick_validate.py。
```

### 3. 初始化 skill 目录

```bash
mkdir -p ${PROJECT_ROOT}/third-round-forward-test/baseline
python3 ${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/init_skill.py no-skill-xhs-article-card-pack --path ${PROJECT_ROOT}/third-round-forward-test/baseline --resources scripts,references --interface display_name='小红书文章卡片包' --interface short_description='把中文长文与素材转成6张小红书卡片' --interface default_prompt='Use $no-skill-xhs-article-card-pack to turn this Chinese article, avatar, and product screenshots into a six-card Xiaohongshu image-text pack.'
```

输出：

```text
Initializing skill: no-skill-xhs-article-card-pack
   Location: ${PROJECT_ROOT}/third-round-forward-test/baseline
   Resources: scripts, references

[OK] Created skill directory: ${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack
[OK] Created SKILL.md
[ERROR] short_description must be 25-64 characters (got 17).
```

### 4. 修复初始化遗留问题并生成 `openai.yaml`

```bash
mkdir -p ${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack/agents ${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack/references ${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack/scripts
python3 ${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/generate_openai_yaml.py ${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack --interface display_name='小红书文章卡片包' --interface short_description='将中文长文章和视觉素材转成小红书六图卡片创作流程与提示词' --interface default_prompt='使用 $no-skill-xhs-article-card-pack 将这篇中文长文、头像和产品截图转成 6 张小红书竖版图文卡片方案。'
chmod +x ${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack/scripts/plan_xhs_cards.py
```

输出：

```text
[OK] Created agents/openai.yaml
```

### 5. Python 语法检查

```bash
python3 -m py_compile ${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack/scripts/plan_xhs_cards.py
```

输出：

```text
无输出，退出码为 0。
```

### 6. 官方 quick_validate

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" ${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack
```

输出：

```text
Skill is valid!
```

### 7. 脚本帮助检查

```bash
${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack/scripts/plan_xhs_cards.py --help
```

输出摘要：

```text
显示参数说明成功。支持 article、--title、--audience、--product、--avatar、--screenshot、--format。
```

### 8. 脚本样例运行

```bash
python3 ${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack/scripts/plan_xhs_cards.py <(printf '%s\n' '很多团队写产品文章时，会把所有背景、功能和愿景都塞进一篇长文。问题是读者在手机上没有耐心读完整篇，所以小红书卡片需要先给出一个明确承诺。方法是先找出读者最痛的场景，再把文章拆成洞察、步骤和证据。产品截图不要当装饰，应该证明某个功能如何解决问题。最后一张卡要给出收藏理由和评论问题，让读者知道下一步怎么做。') --title '把产品长文改成小红书卡片' --audience '内容运营' --product 'AI写作产品' --avatar avatar.png --screenshot screen.png
```

输出摘要：

```text
成功生成“小红书 6 卡方案骨架”，包含主题、目标读者、产品/方法、头像、截图，以及 1 至 6 张卡的角色、标题草案、正文素材、视觉和使用素材。
```

### 9. 最终文件清单

```bash
find ${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack -maxdepth 4 -type f | sort
```

输出：

```text
${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack/SKILL.md
${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack/agents/openai.yaml
${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack/references/visual-production-spec.md
${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack/references/xhs-six-card-system.md
${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack/scripts/plan_xhs_cards.py
```

### 10. 范围检查

```bash
find ${PROJECT_ROOT}/third-round-forward-test/baseline -maxdepth 4 -type f | sort
```

输出：

```text
${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack/SKILL.md
${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack/agents/openai.yaml
${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack/references/visual-production-spec.md
${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack/references/xhs-six-card-system.md
${PROJECT_ROOT}/third-round-forward-test/baseline/no-skill-xhs-article-card-pack/scripts/plan_xhs_cards.py
${PROJECT_ROOT}/third-round-forward-test/baseline/report.md
```

```bash
git status --short -- ${PROJECT_ROOT}/third-round-forward-test/baseline
```

输出：

```text
fatal: not a git repository (or any of the parent directories): .git
```

## 失败与修复

- 初始化失败一次：`short_description` 只有 17 个字符，不符合 25 至 64 字符要求。修复方式：改为更长的中文描述，并用官方 `generate_openai_yaml.py` 重新生成 `agents/openai.yaml`。
- `py_compile` 产生了 `scripts/__pycache__/plan_xhs_cards.cpython-310.pyc`。修复方式：只删除该明确缓存文件，并移除空的 `__pycache__` 目录，避免验证产物进入 skill 包。

## 残余风险

- 未用真实中文长文章、真实头像和真实产品截图做端到端出图测试；当前验证覆盖 skill 结构、脚本语法、脚手架输出和官方 quick_validate。
- `scripts/plan_xhs_cards.py` 只生成可编辑骨架，不替代人工内容判断、视觉审美和最终图片质检。
- 该 skill 未调用图像生成或设计工具，因此没有验证实际成图中的中文排版、遮挡和截图清晰度。
