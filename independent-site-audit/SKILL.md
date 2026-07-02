---
name: independent-site-audit
description: Audit independent ecommerce/DTC sites and Shopify-style brand sites for conversion, trust, UX, traffic quality, landing pages, cart/checkout, cross-market design fit, user feedback, competitor monitoring, content claims, mobile readiness, analytics hooks, technical performance, and launch acceptance. Use when asked to do 独立站检测, 独立站快速审核, 独立站诊断, 网站分析, 网站体检, 首页/PDP审计, 转化率诊断, 跳出率治理, 落地页审核, 购物车/结账诊断, 增长设计分析, 改版验收, homepage/PDP audit, conversion review, growth diagnosis, redesign QA, or to turn a live/local ecommerce site into a prioritized findings report and verification checklist.
---

# Independent Site Audit

## Overview

Use this skill to inspect an independent ecommerce site end to end: tracking reliability, traffic quality, full-funnel leakage, landing-page fit, homepage/category/PDP/cart/checkout friction, trust claims, user feedback, competitor gaps, cross-market design fit, mobile UX, visual interaction, technical performance, and acceptance readiness.

Default to funnel-first, evidence-first work. First locate where users drop off, then use behavior and page evidence to explain why, and only then recommend changes. Separate what is directly observed from what is inferred, and mark assumptions when analytics, ad data, or internal policy docs are missing.

中文使用方式：用这个 Skill 做独立站检测时，默认输出中文报告，除非用户明确要求英文或双语。重点不是泛泛点评页面好不好看，而是先用漏斗数据判断“哪里漏”，再用行为证据和页面检查解释“为什么漏”，最后给可执行改法。

## Quick Audit Mode

When the user wants a fast review or only provides a URL/screenshots, run a lightweight audit instead of blocking on full analytics access:

1. State data limitations up front.
2. Inspect homepage, one collection/category page, one representative PDP, cart entry, checkout entry, support/policy pages, and mobile layout.
3. Use `references/quick-audit-zh.md` for a Chinese rapid pass.
4. Produce 5-10 prioritized issues with page/element, evidence, why it hurts conversion, suggested fix, owner, and priority.
5. Add a "needs data confirmation" section for GA4, ads, heatmaps, checkout, and customer feedback items.

## Core Workflow

1. Define the audit frame and data access.
   - Capture target URL or local files, market, language, target customer, product category, funnel goal, known constraints, and the user's desired output.
   - 中文：先确认检测对象、市场/语言、目标用户、品类、核心转化目标、已知约束，以及用户想要报告、清单、改版建议还是验收结果。
   - Ask for or inspect available analytics: GA4, GTM, ad pixels, UTM rules, heatmaps/session recordings, ad creatives, email/social traffic, and checkout domain setup.
   - If live facts, prices, policies, competitors, or product details may have changed, browse or otherwise verify current pages before making claims.
   - If the user provides analytics, ad accounts, heatmaps, or customer support logs, use them as higher-priority evidence than generic best practices.

2. Validate data infrastructure before diagnosis.
   - Confirm core ecommerce events exist and are not duplicated: `page_view`, `view_item`, `add_to_cart`, `begin_checkout`, `purchase`.
   - Confirm `purchase` is marked as conversion, pixels align across Meta/TikTok/Google Ads, UTM naming is usable, and cross-domain tracking works for Shopify or external checkout.
   - Build or request a funnel view: `Sessions -> Product Page Views -> Add to Cart -> Begin Checkout -> Purchase`, segmented by device and traffic source.
   - If tracking is broken, make this a P0 finding and treat downstream conversion conclusions as provisional.

3. Diagnose traffic quality.
   - Segment performance by source/medium, campaign, landing page, new vs returning users, and device.
   - Compare ad promise against landing-page content. Low conversion may be a traffic-intent problem rather than a site UX problem.
   - Use the decision rule: high bounce by paid traffic suggests ad/landing mismatch; high bounce by organic suggests search-intent mismatch; normal bounce with later leakage requires funnel-stage diagnosis.

4. Diagnose market fit, landing-page fit, and bounce reasons.
   - Compare independent-site behavior against marketplace behavior. Do not apply Amazon-style standards directly to DTC sites.
   - Check whether the target market expects a brand-led, breathable, restrained DTC experience or a dense, promotion-heavy marketplace experience.
   - For paid/social landing pages, compare audience, creative promise, information architecture, visual rhythm, CTA placement, and loading speed.
   - If bounce is high, identify the channel, likely user concern, and whether the core benefit is unclear. Consider lightweight benefit reinforcement, FAQ, social proof, logistics promise, or official-site advantage.

5. Diagnose the full funnel.
   - Inspect homepage, key collection/category pages, at least one representative PDP, cart/checkout entry points, policy/support pages, and mobile navigation.
   - 中文：至少看首页、核心分类页/集合页、代表性商品详情页、购物车入口、政策/售后页、移动端导航。
   - Record desktop and mobile screenshots when visual QA matters.
   - Extract product/SKU map, offer claims, warranty/returns/shipping claims, CTAs, navigation paths, forms, tracking hooks, and external assets.
   - Keep source URLs with every factual claim. Do not invent traffic share, conversion uplift, warranty scope, delivery guarantees, or compliance claims.
   - Diagnose by stage: homepage first screen/CTA/brand trust/product education, category sorting/filter/product cards, PDP first screen/media/price/proof/CTA/typography/mobile-vs-PC/variants, cart feedback/fees/confidence/GMV formula, checkout guest checkout/forms/payment/errors/shipping transparency.

6. Audit trust, user feedback, competitors, and visual interaction.
   - Horizontal: compare against category expectations, direct competitors, marketplaces, and high-performing adjacent DTC patterns.
   - Vertical: inspect the site's own funnel from first impression to product choice to checkout confidence.
   - 中文：横向看竞品/品类常识/平台心智，纵向看本站从首屏、选品、信任、PDP、加购到结账的完整链路。
   - Prefer specific bottlenecks over generic advice: choice friction, trust friction, mobile hesitation, PDP uncertainty, offer mismatch, support ambiguity, or tracking blind spots.
   - Check trust elements: returns, warranty, service channels, logistics, secure payment, reviews, media/KOL proof, UGC, company info, and FAQ.
   - Use user feedback when available: group complaints by rising trend and usage scenario before turning them into product/design requirements.
   - Treat competitor monitoring as a recurring mechanism: direct competitors first, then cross-category references when the site is already mature.
   - Check visual and interaction quality: banner interaction, product education animation, typography hierarchy, button consistency, spacing rhythm, and restrained brand-color use.

7. Audit technical performance and critical functions.
   - Check performance and compatibility when relevant: LCP, INP, CLS, mobile/desktop performance, page weight, image optimization, browser/device support, add-to-cart, discount code, payment, email confirmation, and conversion pixels.

8. Prioritize opportunities and produce the deliverable.
   - Rate each finding by impact, effort, confidence, and risk.
   - Use the impact x effort matrix: immediate fixes, priority projects, low-cost cleanup, and defer/drop.
   - Assign likely owner: UI/design, operations, marketing/BM, product, development, user operations, or analytics.
   - Tie every recommendation to a user job or business lever: reduce choice friction, clarify value, increase trust, improve discoverability, improve speed, reduce support burden, or make measurement cleaner.
   - Identify claim guardrails: phrases that must be verified, softened, removed, or backed by source links.
   - Use `references/report-template.md` when the user wants a client-ready report.
   - Use `references/audit-checklist.md` when the user wants a checklist, scorecard, or repeatable QA pass.
   - Use `references/report-template-zh.md` for a Chinese client-ready report.
   - Use `references/audit-checklist-zh.md` for a Chinese checklist, scorecard, or repeatable QA pass.
   - Use `references/quick-audit-zh.md` when the user wants a fast Chinese independent-site review.
   - Use `references/conversion-methodology-zh.md` when the task needs a complete 8-stage diagnostic SOP, analytics/event checks, traffic-quality diagnosis, funnel-stage baselines, cross-market design audit, user feedback, competitor monitoring, collaboration rhythm, or execution cadence.
   - Include quick wins, deeper redesign ideas, verification steps, and unresolved questions.
   - Keep recommendations implementable: name the section/page, proposed change, rationale, evidence, and expected measurement.

9. Verify implementation or redesign work.
   - For local HTML/CSS/JS deliverables, run or adapt `scripts/static_site_audit.py`.
   - Add task-specific checks for required sections, allowed claims, SKU coverage, PDP links, image alt text, JSON-LD parsing, mobile breakpoints, sticky CTAs, and analytics events.
   - For live pages, verify important URLs and remote assets return successful statuses.
   - Do browser QA at desktop and mobile sizes when layout, interaction, or visual hierarchy is part of the work.

## Output Standards

Every audit should include:

- Executive diagnosis: the main conversion problem in 2-4 sentences.
- 中文执行摘要：用 2-4 句话说清楚最大的转化阻力和最值得先改的位置。
- Data reliability note: whether tracking and funnel data are trustworthy.
- Traffic quality diagnosis: whether the visitor intent matches the landing experience.
- Market and landing-page fit: whether design rhythm, promotion density, and benefit expression match the target market/channel.
- Evidence table: page/element, observation, impact, confidence, source.
- Prioritized recommendations: impact, effort, owner or discipline, suggested metric, and next validation method.
- Claim and compliance guardrails: unsupported or risky language to avoid.
- Verification checklist: what to test before publishing.

When producing implementation acceptance notes, mirror this structure:

- Growth design strategy.
- Implemented conversion levers.
- Claim and SKU guardrails.
- Acceptance checks run.
- Files or pages touched.

## Resource Use

- Read `references/audit-checklist.md` for category-by-category inspection criteria.
- Read `references/report-template.md` when writing a structured report.
- Read `references/audit-checklist-zh.md` when the user wants Chinese deliverables or asks for 独立站检测/网站分析 in Chinese.
- Read `references/report-template-zh.md` when writing a Chinese structured report.
- Read `references/quick-audit-zh.md` when the user wants to quickly review a site with limited data.
- Read `references/conversion-methodology-zh.md` when the task needs a complete 8-stage diagnostic SOP, analytics/event checks, traffic-quality diagnosis, funnel-stage baselines, cross-market design fit, feedback systems, competitor monitoring, or execution rhythm.
- Use `scripts/static_site_audit.py` for local static checks, then add project-specific assertions instead of relying on the generic script alone.
