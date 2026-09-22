# Independent Site Audit Checklist

Inspect only the user's scope and related paths needed to explain a finding. Do not require a full-site pass, every browser, a fixed competitor count or a fixed issue count. Record pass, fail, not run or not applicable with evidence; do not use an aggregate score as a launch gate. Chinese counterpart: [检测清单](audit-checklist-zh.md).

## Evidence And Data Reliability

- Verify callable tools, valid authorization, the correct site/project and relevant readable data for PostHog, GA4 or the backend. An installed plugin does not prove usable data.
- Without a connection, accept PDFs, spreadsheets, reports, data documents or screenshots. Record source, date, page/sheet and readability.
- Without any data, compare the actual site with relevant benchmarks. Keep observations; do not invent metrics.
- For data used, record period, timezone, unit, denominator, device/channel, funnel sequence and missing/duplicate events. Include only detail needed for the question.
- Use the site's actual event definitions. Distinguish code hooks, browser requests and platform receipt. Order records cannot reconstruct untracked browsing or abandonment.
- Do not compare platforms, dates or units without reconciling definitions. Prefer the site's own comparable historical baseline.
- Missing data limits dependent conclusions; it does not block independent UI checks or reproducible defect fixes.

## Traffic And Landing-Page Fit (When Relevant And Supported)

- Ad or search promises match the actual landing-page content.
- Inspect relevant channel/device differences; aggregate bounce rate does not identify a visual cause.
- Explain new/returning visitor differences using source and sample, without a required ratio.
- Language, currency, units, shipping and payment suit actual users. Do not infer visual taste or information density from nationality or region.

## Understand The Page

- The product, use case, key differences and next action are clear.
- Information order supports the buying task; primary/secondary actions are distinguishable and popups do not block essential content.
- Images show product, scale, detail or use context needed for decisions and have a source.
- Price, discounts, financing, inventory and shipping wording are accurate. Warranty, returns and support are discoverable when needed.
- Reviews, certifications and outcome claims have evidence; content is not invented to fill a layout.
- A static image is not a defect. Motion is used only when it aids understanding or feedback and respects reduced-motion preferences.

## Choose A Product

- Navigation, categories and product cards help find the target product; links and SKUs are correct.
- Comparison, sorting, filters and recommendations serve actual shopping tasks; empty results have a recovery path.
- Specs, variants, bundles, subscriptions and quantity reflect the item and price being purchased.
- Changing options does not silently misselect items, discard input or put the purchase button in the wrong state.
- Accessories and cross-sell help without blocking the main purchase action.

## Complete A Purchase

- Add-to-cart has clear loading, success and failure feedback; repeated clicks do not cause unintended duplicate actions.
- Cart items, quantities, prices, discounts and subtotal are correct and remain consistent after changes.
- Costs, delivery coverage and estimated arrival are clear when known, with consistent promises across pages.
- Checkout options, required fields and payment methods suit intended users; recommendations to remove signup or inputs have specific supporting evidence.
- Errors explain the issue and recovery; keyboard focus and entered data are preserved appropriately.
- Real purchase, payment or outbound notification checks follow task authorization and test-environment rules. A static demo is not a completed transaction.

## Visual, Mobile And Accessibility

- Check long text, image crops, overflow, overlays and layout shifts at relevant phone and desktop sizes.
- Type scale, line length, contrast, spacing and action hierarchy make content readable while following existing brand rules.
- Touch targets, keyboard navigation, focus, form labels and error states work.
- Fixed bars, sticky actions and dialogs are used only when justified, without obscuring content or safe areas.
- Informative images have meaningful alternative text. Decorative images may have empty alt and should not distract assistive technology.
- Component states are consistent. Give concrete requirements instead of vague aesthetic adjectives.

## Technology And Content (Select For The Change)

- Actual links, images, required resources and affected interactions work. A successful HTTP status alone does not prove functionality.
- Performance findings identify tool, device, network, test date and lab/real-user source.
- Cite current technical standards or project budgets used; arbitrary scores and page-weight limits are not universal launch gates.
- When SEO is in scope, inspect titles, descriptions, heading structure, internal links and existing structured data. Parseable JSON-LD does not prove accurate content.
- Reuse effective event names. Add events only when needed and check trigger, properties and deduplication.
- Separate static checks, browser actions and production checks. Choose browser coverage for the change and user environment.

## Feedback And Benchmarks

- Record feedback context, device, source and reproducibility. One severe defect can justify a fix without rising feedback volume.
- Select relevant benchmarks, distinguishing direct competitors from cross-category references; no fixed count or monitoring cadence is required.
- Preserve concrete URL, date, region, viewport, state and real screenshots. Explain transferable and inapplicable parts.
- Do not replace page evidence with generated images or search snippets, or copy another brand's prices, policies or promises.

## Findings And Handoff

- Give each finding a stable ID and classify it as a reproduced defect, experience risk or unverified growth hypothesis.
- Link issue → screenshot/source → change → component/implementation location → acceptance action. Do not pad the findings.
- Explain priority through user impact, evidence and effort; assign ownership to the actual team.
- Do not promise uplift without evidence. Report deployment, functional verification and proven conversion impact separately.
- Produce short reports only for stages actually performed and explain unresolved inputs and their effects.
