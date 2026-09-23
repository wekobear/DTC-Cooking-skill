# DTC-Cooking（DTC 烹饪）

**当前版本：0.3.2** · [下载 Skill](https://github.com/wekobear/DTC-Cooking-skill/releases/download/v0.3.2/dtc-cooking-0.3.2.zip) · [版本说明](CHANGELOG.md)

DTC-Cooking 像顶尖厨师拆解烹饪技术一样，拆解 DTC 独立站的问题：从准备食材、处理食材，到控火、调味、摆盘、上桌品尝，把每一步为什么做、怎样做、怎样判断做好了讲清楚。这里的“食材”是你的网站、目标和已有资料，最终要端上桌的是有依据、能实施的页面改进，让顾客更容易看懂商品、做出选择、完成购买。

这是面向支持 Agent Skills 的通用 Agent 工作流程。**优先推荐 Codex**，作为串联 Skill、MCP/插件、浏览器、代码修改与多智能体协作的首选环境；也可用于 Claude Code、Cursor 等支持该格式的工具。执行能力取决于当前环境的工具、连接和权限，发布需要正确的目标与账号权限。它不承诺自动提高转化率，也不要求每个用户都连接同一套工具。

品牌名保留 **DTC-Cooking**，供工具识别的目录名和 `SKILL.md` 中的 `name` 统一为 `dtc-cooking`，遵循 [Agent Skills 命名规范](https://agentskills.io/specification#name-field)。

## 一句话开始

Codex 中使用：

```text
使用 $dtc-cooking 检查 https://example.com 的商品页，说明最值得改的问题和方案。
```

也可以指定交付终点：

```text
使用 $dtc-cooking 根据这个商品页和我提供的 PDF 报告，做出可操作的改版预览。
使用 $dtc-cooking 检查并修改这个页面，验证后发布到项目已配置的网站，给我前后对比和线上检查结果。
```

只要求检测，就交付问题和方案；要求预览，就制作并验证页面；明确要求上线且条件具备，就继续完成发布与线上核验。普通阶段报告不会变成重复审批。

## 没有后台数据，也能开始

| 手上有什么 | 怎样做 |
| --- | --- |
| 已连接 PostHog、GA4 或商城后台 | 先核对站点和数据是否可用，再结合实际页面解释问题 |
| PDF、表格、报表、数据文档或截图 | 读取现有资料，注明来源和日期，不强制先接后台 |
| 只有网址，没有数据 | 实际查看用户页面，与相关跨品类标杆对照，说明建议和理由 |

没有数据时也给出具体方案，但不把推测写成真实流失原因。后续是否提升转化，需要实施后的证据。

## 六道工序，把问题变成能落地的改法

![DTC-Cooking 完整流程](docs/assets/workflow.png)

[白话流程说明](docs/workflow.md) · [交互流程图 HTML](docs/workflow.html)（下载后用浏览器打开）

| 烹饪工序 | 在独立站里做什么 | 交付什么 |
| --- | --- | --- |
| **准备食材** | 看清网站、购买目标和本次终点，确认可用后台或现成资料；都没有就走页面与标杆对照路线 | 任务与资料说明 |
| **处理食材** | 辨别资料是否可靠，实际走一遍手机和电脑上的购买过程，对照相关标杆 | 问题清单、资料依据和真实截图 |
| **控火** | 决定先解决什么、这次改到哪里，把投入放在最值得改的问题上 | 页面改进说明书（PRD）：问题、理由、改法和检查方法 |
| **调味** | 按 [Vibe Designing Playbook](https://alibaba-cloud-design.github.io/vibe-designing-playbook/) 安排信息、视觉和交互，用 [HeroUI](https://heroui.com/docs/react/getting-started) 的组件思路细化方案 | 页面设计与组件说明 |
| **摆盘** | 做成可操作的网页，选择 Figma、pen.dev 或 HTML + Tailwind CSS 交付，检查手机和电脑上的实际操作 | 可运行预览、代码或可编辑稿、检查结果 |
| **上桌品尝** | 按用户授权发布并检查真实线上页面，再用后续资料判断顾客是否更容易选购和下单 | 线上检查与恢复说明；有后续数据时给出效果判断 |

厨师会按菜品安排工序，DTC-Cooking 也按你的需求推进：只要检测与方案，就做到问题分析和改进说明；局部小修直接处理相关部分，不强迫六步全跑。每个实际执行的大阶段留下简短报告，问题、证据、改动与验证可以对应起来。启动时询问是否开启多智能体；开启后按独立工作分工，关闭时由单个 Agent 完成。

## 怎样继续修改

- **Figma**：先检查插件、登录和目标文件能力，再按选择导入可编辑稿；导入不等于完整组件和交互自动保留。
- **pen.dev**：没有 Figma、但想手动调整文字、图片和排版时，推荐 [pen.dev 客户端](https://www.pen.dev/)。修改并导出后重新验证页面。
- **HTML + Tailwind CSS**：直接交付页面与预览；购买功能和数据接入按项目实际情况实现。

HeroUI、Figma 和分析工具的安装状态不会从作者电脑继承。Skill 会按当前环境检查，缺少工具时继续不依赖它的工作。

## 安装与跨 Agent 调用

下载并解压 [0.3.2 Skill 包](https://github.com/wekobear/DTC-Cooking-skill/releases/download/v0.3.2/dtc-cooking-0.3.2.zip)，将整个 `dtc-cooking/` 放入所用工具的 Skill 目录，保留其中的参考文件和脚本。以下以项目内安装为例：

| 工具 | 项目内目录 | 手动调用 |
| --- | --- | --- |
| **Codex（优先推荐）** | `.agents/skills/dtc-cooking/` | `使用 $dtc-cooking 检查这个商品页并给出方案` |
| Claude Code | `.claude/skills/dtc-cooking/` | `/dtc-cooking 检查这个商品页并给出方案` |
| Cursor | `.cursor/skills/dtc-cooking/` | 在 Agent 聊天输入 `/`，选择 `dtc-cooking`，再描述任务 |

其它支持 Agent Skills 的工具，按各自的安装目录与调用方式使用同一份 `dtc-cooking/`。已有中央 Skill 管理器时沿用其目录与软链接规则，不创建重复副本。`agents/openai.yaml` 是 Codex 的展示与默认提示扩展，通用执行流程保留在 `SKILL.md` 和参考文件中；缺少某个插件或多智能体能力时，按实际能力继续可完成的工作。

从 0.3.1 升级时，将原安装目录改为 `dtc-cooking` 并更新入口软链接及调用示例；大小写不敏感的文件系统可先改为临时名，再改为小写。先保留自己的定制，再更新新版内容，避免同时保留新旧两个安装入口。重载后检查工具是否列出 `dtc-cooking`。

安装与调用依据：[Codex](https://developers.openai.com/codex/skills)、[Claude Code](https://code.claude.com/docs/en/skills)、[Cursor](https://cursor.com/docs/skills)。以上是格式与官方用法说明，本次未进行三款 Agent 的实际加载和完整流程测试。

仓库中的 `dtc-cooking/` 是可安装目录；`docs/` 是流程说明和图，`dtc-cooking/tests/` 是静态检查脚本的验证用例。

## 本地静态检查

```bash
python3 dtc-cooking/scripts/static_site_audit.py index.html \
  --css styles.css --js script.js --required-id main \
  --require-tracking --require-mobile-css
```

脚本检查 HTML 和资源中的静态线索，不能证明按钮能用、页面响应式正确、分析端收到事件或生产发布成功。实际任务仍需浏览器与发布后的检查。

## 发布内容与隐私

公共包只包含通用 Skill、参考方法和静态检查脚本；流程图可单独下载。项目报表、客户截图、私人文档地址、本机路径、连接配置和安全扫描原始记录不随包发布。标杆池使用公开品牌入口，用户可替换为自己的资料。

当前发布验证覆盖 Skill 结构、静态脚本用例、流程分支审阅和流程图。尚未宣称已在所有商城平台完成真实发布验证。

交互图使用 Archify 生成，第三方许可见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
