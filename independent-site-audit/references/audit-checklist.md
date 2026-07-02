# Independent Site Audit Checklist

Use this checklist as a repeatable inspection pass. Score each item `0` absent, `1` weak, `2` acceptable, `3` strong, and attach evidence.

## Data Infrastructure

- GA4 core ecommerce events fire correctly: `page_view`, `view_item`, `add_to_cart`, `begin_checkout`, `purchase`.
- `purchase` is marked as a conversion event.
- Meta Pixel, TikTok Pixel, and Google Ads tags align with the GA4 funnel.
- UTM naming is consistent across ads, email, social, creator, and affiliate traffic.
- Cross-domain tracking works when checkout runs on Shopify checkout or another domain/subdomain.
- A base funnel exists: Sessions -> Product Page Views -> Add to Cart -> Begin Checkout -> Purchase.
- Funnel data can be segmented by device, traffic source, new/returning users, and landing page.

## Traffic Quality

- Bounce rate, conversion rate, and revenue contribution are reviewed by source/medium.
- Brand search, non-brand paid, social, email, organic, and direct traffic are diagnosed separately.
- Returning visitors convert meaningfully better than new visitors, or the gap is explained.
- Ad creative promises match the first screen of the landing page.
- SEO query intent matches the landing page content.
- High bounce is not treated as a page-design problem until traffic intent is checked.
- Social traffic with high bounce is checked for fast, clear benefit expression.
- DTC sites are not judged by marketplace-only standards such as Amazon search behavior.
- Target-market fit is checked: brand-led breathing room vs dense promotion-heavy design.

## Landing Page And Bounce Reduction

- Landing page content matches ad creative, audience, and channel intent.
- Information architecture follows the buyer decision sequence.
- Brand culture is present alongside product facts.
- Visual rhythm creates clear emphasis instead of uniform density.
- CTAs appear at meaningful decision points without excessive repetition.
- Paid landing pages load quickly.
- High-bounce pages are diagnosed by source, persona, concern, and clarity of benefit.

## Business And Positioning

- The first viewport makes the brand, category, product, or offer instantly clear.
- The hero prioritizes a product-led or use-case-led image, not vague atmosphere.
- The page names the customer job: goal, problem, setting, routine, budget, or outcome.
- The main CTA leads to the next commercial step, not a vague brand page.
- Supporting copy explains why buy here instead of Amazon, marketplace, reseller, or competitor.
- The first 3 seconds provide value clarity, not only a promotion banner.
- Popups do not block the primary CTA or appear too early without a strong reason.
- Homepage includes useful product education where the product is complex.
- Homepage categories or intent paths help users find the right product.

## Product Discovery

- Navigation exposes the main product types and shopping intents.
- Visitors can shop by goal, use case, room, problem, or product type.
- Best sellers or recommended starting points reduce choice overload.
- Product cards include clear names, images, differentiators, and direct PDP links.
- SKU names and product claims match the official catalog.
- Category sorting defaults to a conversion-friendly order such as best sellers, recommendations, or strategic products.
- Filters are usable, visible, tracked, and do not strand users in dead-end zero-result states.

## Trust And Offer

- Warranty, returns, shipping, payment, trial, support, and price policies are visible before deep checkout.
- Claims use exact policy language or are softened when evidence is missing.
- Social proof is specific: reviews, press, certifications, creators, community, or usage proof.
- Support paths are obvious: FAQ, contact, manuals, registration, setup, service, and parts.
- Risky claims are removed unless backed by current source pages.

## PDP

- PDP entry points are direct and obvious from homepage/category sections.
- Above-the-fold PDP content answers: what it is, who it is for, key benefit, price/offer, delivery, returns, and primary CTA.
- Product media includes enough angles, context, detail, scale, and video where decision pressure is high.
- Price, discount, coupon, and financing logic are easy to understand.
- Reviews, ratings, and trust guarantees are close enough to the decision area.
- Variant, bundle, comparison, financing, and subscription choices do not block purchase clarity.
- No dead ends: every major informational section has a next action.
- Typography hierarchy, price emphasis, CTA text, and supporting hints are readable and properly weighted.
- Mobile and desktop PDPs are diagnosed separately.

## Cart And Checkout

- Cart GMV is decomposed as visitors x add-to-cart rate x checkout conversion x AOV.
- Add-to-cart produces clear feedback.
- Cart entry shows a quantity change or cart drawer/update.
- Cart includes product image, name, price, quantity controls, discounts, and subtotal.
- Shipping, taxes, and other extra costs are transparent before checkout where possible.
- Cart-to-checkout dropoff above 40% triggers a focused cost/trust/payment/technical investigation.
- Guest checkout is available.
- Required checkout fields are minimized.
- Target-market payment methods are available.
- Error messages are specific and actionable.
- Shipping, discount, and financing promises remain consistent from homepage/PDP to checkout.
- Cart shows helpful decision aids such as final price, shipping threshold, local shipping, discount tags, or delivery estimate when relevant.
- Benefit messages are visually close to checkout CTA.

## Mobile UX

- Mobile first viewport retains brand/product signal, primary CTA, and enough visual context.
- Header, menu, sticky CTA, product cards, and forms remain tappable and readable.
- Text never overlaps images, buttons, cards, or subsequent sections.
- The visitor can compare products in a single-column scan without losing core specs.
- Important CTAs are reachable without excessive scrolling.

## Content And Visual System

- Section headings are consistent and scannable.
- Images show the actual product, context of use, details, or results the buyer needs to inspect.
- Visual hierarchy emphasizes commercial decisions over decorative panels.
- Repeated cards, tabs, badges, and buttons use stable dimensions and consistent states.
- Copy is concrete: product names, specs, policy terms, use cases, and objections.
- Heading, body, button, and spacing systems are consistent sitewide.
- Brand color is used with restraint and a clear pattern.

## Feedback And Competitor Monitoring

- Customer feedback is grouped by issue type, page, device, channel, and frequency.
- Issues become requirements only when volume rises and use cases are rich enough.
- Direct competitors are monitored regularly.
- Competitor changes are reviewed for relevance before entering the roadmap.

## SEO And Structured Data

- Page title and meta description match the product/category intent.
- One clear H1 exists and headings follow a readable structure.
- Images include meaningful alt text.
- JSON-LD parses successfully when present.
- Internal links use crawlable anchors and descriptive text.

## Tracking And Experiment Readiness

- Primary CTAs, product links, quiz/finder actions, forms, and nav actions have tracking hooks.
- Event names are consistent and map to funnel stages.
- The site distinguishes commercial intent clicks from engagement-only clicks.
- Recommendations include measurable success metrics: CTR, PDP views, add-to-cart, checkout start, CVR, AOV, return rate, support contact rate.
- Proposed tests include a clear hypothesis, page area, audience, and guardrail metric.

## Technical Acceptance

- Core pages and remote assets return successful HTTP statuses.
- LCP, INP, CLS, mobile score, desktop score, and total page weight are checked when performance matters.
- Images use appropriate format, dimensions, and lazy-loading strategy.
- Key flows are spot-checked across Chrome, Safari, Firefox, Edge, iOS Safari, and Android Chrome where possible.
- Slow-network behavior is checked for important commercial paths.
- No empty or placeholder links remain in commercial paths.
- Images have sources and alt text.
- Required sections and CTAs exist.
- Mobile breakpoints and sticky/mobile behaviors exist when specified.
- Interactive tabs, quizzes, menus, forms, and carousels work with keyboard/mouse/touch expectations.
- Add-to-cart, discount code, payment, confirmation email, and conversion pixels work.
- Forbidden or unverified claims are absent.

## Prioritization

- Every issue is graded by impact and fix difficulty.
- High-impact, low-effort issues become immediate quick wins.
- High-impact, high-effort issues become priority projects.
- Low-impact, low-effort issues become cleanup items.
- Low-impact, high-effort issues are deferred or dropped.
- Every recommendation has a likely owner: design, operations, marketing, product, engineering, user operations, or analytics.
