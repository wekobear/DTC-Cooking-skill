# Independent Site Audit Skill

这是一个用于快速审核 DTC / Shopify / 品牌独立站转化问题的 Codex Skill。它把独立站诊断整理成可复用流程：先判断数据是否可信，再定位漏斗哪里流失，最后输出有证据、有优先级、有责任归属的优化清单。

## 能做什么

- 快速审核一个独立站首页、落地页、品类页、PDP、购物车和结账路径。
- 判断问题属于流量质量、落地页承接、首屏表达、商品发现、PDP 决策、购物车、结账、信任、移动端、技术性能还是埋点。
- 输出 5-10 个优先问题，并标注证据、影响、建议、责任归属和待验证指标。
- 在有 GA4/GTM/广告/热力图/用户反馈时，做完整 8 阶段转化诊断。
- 帮助做改版验收：检查 claim、SKU、链接、图片 alt、JSON-LD、移动端、tracking hooks 和远程资源。

## 适合什么时候用

- “帮我检测一下这个独立站哪里影响转化。”
- “这个 Shopify 站首页/PDP/购物车有什么问题？”
- “我只有一个网址，先快速看 5 个最该改的问题。”
- “根据 GA4 漏斗和页面证据，帮我定位为什么不转化。”
- “上线前帮我做一次独立站改版验收。”

## 快速上手

在 Codex 中这样调用：

```text
Use $independent-site-audit 检测一下这个网站：https://example.com
```

如果只有网址，Skill 会自动走快速审核模式：

1. 说明没有 GA4、广告、热力图时的判断限制。
2. 检查首页、品类页、代表性 PDP、购物车入口、结账入口、政策页和移动端。
3. 输出优先问题清单。
4. 单独列出需要数据确认的项目。

如果你有数据，可以这样问：

```text
Use $independent-site-audit 结合这些 GA4 漏斗数据、广告来源和热力图记录，完整诊断这个独立站转化问题。
```

## 输出格式

快速审核默认输出：

```markdown
## 快速诊断结论

2-4 句话说明最大转化阻力、主要流失环节、优先动作。

## 优先问题清单

| 优先级 | 位置 | 问题 | 证据 | 建议 | 责任归属 | 待验证指标 |
| --- | --- | --- | --- | --- | --- | --- |
| 🔴 | 首页/PDP/购物车等 | 具体问题 | 页面观察/数据 | 具体改法 | UI/运营/产品/开发/营销 | CTR/ATC/CVR 等 |

## 待数据确认

- GA4 漏斗
- 渠道跳出率
- 首页到 PDP 点击率
- PDP 到加购率
- 购物车到结账流失率
- 结账退出率
- 用户反馈/客服问题
- 竞品变化
```

## 8 阶段方法论

完整诊断按以下顺序执行：

1. 数据基础设施检查：GA4、GTM、Pixel、UTM、跨域追踪。
2. 流量质量与市场差异诊断：渠道、广告承接、SEO 意图、独立站 vs 平台、跨市场设计。
3. 全漏斗逐级诊断：首页、落地页、跳出率、品类页、PDP、购物车、结账。
4. 用户反馈体系与信任审计：反馈趋势、场景丰富度、退货、保修、客服、物流、FAQ、官网购买优势。
5. 视觉与交互体验审计：首页交互、产品教育、排版字号、品牌色、信息密度。
6. 技术性能检测：LCP、INP、CLS、移动端、图片、关键功能和转化像素。
7. 系统性问题诊断与协同机制：UI、运营、营销、产品、开发、用户运营责任归属。
8. 执行节奏与持续迭代：Quick Wins、A/B 测试、竞品监控、每周复盘。

## 文件结构

```text
independent-site-audit/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── quick-audit-zh.md
│   ├── conversion-methodology-zh.md
│   ├── audit-checklist-zh.md
│   ├── report-template-zh.md
│   ├── audit-checklist.md
│   └── report-template.md
└── scripts/
    └── static_site_audit.py
```

## 本地静态检查脚本

`scripts/static_site_audit.py` 可用于本地 HTML/CSS/JS 页面验收，例如：

```bash
python3 independent-site-audit/scripts/static_site_audit.py index.html \
  --css styles.css \
  --js script.js \
  --required-id main \
  --min-product-links 6 \
  --require-tracking \
  --require-mobile-css
```

脚本会检查标题、meta description、viewport、H1、图片 alt、链接、JSON-LD、required id/text、forbidden text、产品链接数量、tracking hooks 和移动端 CSS。

## 安装到 Codex

将 `independent-site-audit/` 放到 Codex skills 目录后即可通过 `$independent-site-audit` 调用。常见位置是：

```text
~/.codex/skills/independent-site-audit
```

如果只是想查看或复用方法论，也可以直接阅读 `references/quick-audit-zh.md` 和 `references/conversion-methodology-zh.md`。
