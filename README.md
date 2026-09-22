# DTC Cooking（DTC 烹饪）

**当前版本：0.3.0** · [下载 Skill](https://github.com/wekobear/DTC-Cooking-skill/releases/download/v0.3.0/independent-site-audit-0.3.0.zip) · [版本说明](CHANGELOG.md)

帮助 DTC 独立站找出页面哪里让顾客看不懂、选不定、买不顺，再给出有依据、能实施的改进方案。用户说清目标后，可以从界面检查继续做到页面制作、验证和已授权的上线。

这是给 AI Agent 使用的工作流程，执行需要当前环境提供浏览器、代码或站点编辑能力；发布还需要正确的目标和账号权限。它不承诺自动提高转化率，也不要求每个用户都连接同一套工具。

## 一句话开始

```text
Use $independent-site-audit 检查 https://example.com 的商品页，说明最值得改的问题和方案。
```

也可以指定交付终点：

```text
Use $independent-site-audit 根据这个商品页和我提供的 PDF 报告，做出可操作的改版预览。
Use $independent-site-audit 检查并修改这个页面，验证后发布到项目已配置的网站，给我前后对比和线上检查结果。
```

只要求检测，就交付问题和方案；要求预览，就制作并验证页面；明确要求上线且条件具备，就继续完成发布与线上核验。普通阶段报告不会变成重复审批。

## 没有后台数据，也能开始

| 手上有什么 | 怎样做 |
| --- | --- |
| 已连接 PostHog、GA4 或商城后台 | 先核对站点和数据是否可用，再结合实际页面解释问题 |
| PDF、表格、报表、数据文档或截图 | 读取现有资料，注明来源和日期，不强制先接后台 |
| 只有网址，没有数据 | 实际查看用户页面，与相关跨品类标杆对照，说明建议和理由 |

没有数据时也给出具体方案，但不把推测写成真实流失原因。后续是否提升转化，需要实施后的证据。

## 从发现问题到交付页面

![DTC Cooking 完整流程](docs/assets/workflow.png)

[白话流程说明](docs/workflow.md) · [交互流程图 HTML](docs/workflow.html)（下载后用浏览器打开）

1. 读取网站、目标与已有工具，补问尚缺的数据和是否开启多智能体。
2. 整理资料，检查实际界面，按问题选择标杆并保存真实截图。
3. 写“页面改进说明书”（PRD）：哪里有问题、凭什么这样判断、怎么改、如何检查。
4. 按 [Vibe Designing Playbook](https://alibaba-cloud-design.github.io/vibe-designing-playbook/) 的设计方法，结合 [HeroUI](https://heroui.com/docs/react/getting-started) 制作原型，沿用目标站的品牌与业务规则。
5. 验证手机和电脑上的实际操作，再按用户要求交付或上线。

每个实际执行的大阶段留下简短报告，问题、证据、改动与验证可以对应起来。开启多智能体时按独立工作分工；关闭时由单个 Agent 完成。

## 怎样继续修改

- **Figma**：先检查插件、登录和目标文件能力，再按选择导入可编辑稿；导入不等于完整组件和交互自动保留。
- **pen.dev**：没有 Figma、但想手动调整文字、图片和排版时，推荐 [pen.dev 客户端](https://www.pen.dev/)。修改并导出后重新验证页面。
- **HTML + Tailwind CSS**：直接交付页面与预览；购买功能和数据接入按项目实际情况实现。

HeroUI、Figma 和分析工具的安装状态不会从作者电脑继承。Skill 会按当前环境检查，缺少工具时继续不依赖它的工作。

## 安装

下载并解压 [0.3.0 Skill 包](https://github.com/wekobear/DTC-Cooking-skill/releases/download/v0.3.0/independent-site-audit-0.3.0.zip)，将其中的 `independent-site-audit/` 放入工具支持的 Skill 目录，即可通过 `$independent-site-audit` 调用。已有中央 Skill 管理器时沿用其目录与软链接规则，不创建重复副本。

仓库中的 `independent-site-audit/` 是可安装目录；`docs/` 是流程说明和图，`independent-site-audit/tests/` 是静态检查脚本的验证用例。

## 本地静态检查

```bash
python3 independent-site-audit/scripts/static_site_audit.py index.html \
  --css styles.css --js script.js --required-id main \
  --require-tracking --require-mobile-css
```

脚本检查 HTML 和资源中的静态线索，不能证明按钮能用、页面响应式正确、分析端收到事件或生产发布成功。实际任务仍需浏览器与发布后的检查。

## 发布内容与隐私

公共包只包含通用 Skill、参考方法和静态检查脚本；流程图可单独下载。项目报表、客户截图、私人文档地址、本机路径、连接配置和安全扫描原始记录不随包发布。标杆池使用公开品牌入口，用户可替换为自己的资料。

当前发布验证覆盖 Skill 结构、静态脚本用例、流程分支审阅和流程图。尚未宣称已在所有商城平台完成真实发布验证。

交互图使用 Archify 生成，第三方许可见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
