# Design System Strategy: High-End Strategic Editorial

## 1. Overview & Creative North Star: "The Digital Sovereign"
This design system is built to convey absolute authority and precision. Our Creative North Star is **"The Digital Sovereign"**—a visual language that feels curated, bespoke, and expensive. We are moving away from the "SaaS-dashboard" aesthetic and toward a high-end technical report style that mirrors the gravitas of a global consulting firm’s white paper.

To break the "template" look, we utilize **Intentional Asymmetry**. Large-scale typography (Display-LG) should be used as a structural anchor, often offset against data-rich components. We embrace the "void"—using the `24 (8.5rem)` spacing token not just as a gap, but as a luxury element that allows the executive reader to focus on high-value insights.

---

## 2. Colors: Tonal Depth over Structural Lines
The palette is rooted in `surface (#121317)`, a deep midnight that serves as our canvas. We do not use lines to separate ideas; we use light and depth.

### The "No-Line" Rule
**Explicit Instruction:** Do not use 1px solid borders to section content. Boundaries must be defined solely through background color shifts. 
- A hero section using `surface` might transition into a content block using `surface-container-low (#1a1b20)`. 
- Content hierarchy is established by the transition from `surface-container-lowest` to `surface-container-highest`, creating a natural focal flow without the visual clutter of "boxes."

### Surface Hierarchy & Nesting
Treat the UI as a series of physical layers. 
- **Level 0 (Base):** `surface` or `surface-dim` for the global background.
- **Level 1 (Sections):** `surface-container` for major content blocks.
- **Level 2 (Elements):** `surface-container-high` for interactive cards or data modules.

### The "Glass & Gradient" Rule
To highlight 'Value' and 'Cutting-Edge' insights, use `primary (#00daf3)` and `tertiary (#66dd8b)` sparingly but impactfully. 
- **Signature Textures:** Apply a linear gradient from `primary` to `on_primary_container` (0% to 100%) at a 135-degree angle for high-level CTA backgrounds or key data trend lines.
- **Glassmorphism:** For floating overlays (modals or tooltips), use `surface_variant` at 60% opacity with a `20px` backdrop-blur. This ensures the sophisticated "midnight" depths bleed through, maintaining a unified visual field.

---

## 3. Typography: The Editorial Voice
We pair the architectural strength of **Manrope** for headers with the Swiss-precision of **Inter** for data and body.

*   **Authority (Manrope):** Use `display-lg (3.5rem)` for singular, high-impact statements. The tight tracking and bold weight of Manrope convey a "C-suite" presence.
*   **Precision (Inter):** Use `body-md (0.875rem)` for technical reporting. Ensure `on_surface_variant (#c4c6cc)` is used for secondary descriptions to keep the visual hierarchy clear.
*   **The "Value" Highlight:** Specific metrics or "Value" callouts should utilize `title-lg` but be colored in `tertiary (#66dd8b)` to immediately draw the eye to the positive ROI or strategic advantage.

---

## 4. Elevation & Depth: Tonal Layering
Traditional drop shadows are too "web-standard." We use **Ambient Shadows** and **Tonal Lifts**.

*   **The Layering Principle:** Instead of a shadow, place a `surface-container-highest (#343439)` card on a `surface (#121317)` background. The contrast in hex value provides all the "lift" required.
*   **Ambient Shadows:** When an element must float (e.g., a strategic menu), use a shadow with a `48px` blur and `4%` opacity, tinted with `primary`. This mimics the way high-end LED displays emit light.
*   **The "Ghost Border" Fallback:** If accessibility requires a container edge, use `outline-variant` at 15% opacity. It should be felt, not seen.

---

## 5. Components: Precision Modules

### Buttons
- **Primary:** No border. Gradient fill (Primary to Primary-Container). `Rounded-MD (0.375rem)`. Text in `on_primary_fixed`.
- **Secondary:** Glassmorphic. Background: `surface-bright` at 10% opacity with a Ghost Border.
- **Tertiary/Ghost:** Pure text using `label-md`, colored in `primary`.

### Cards & Data Modules
- **Rule:** Forbid divider lines. Use `spacing-6 (2rem)` to separate internal card elements.
- **Header:** Use `title-sm` in `primary` to label the data category.
- **Value:** Use `display-sm` for the primary metric to ensure it is the first thing an investor sees.

### Input Fields
- **State:** Unfocused inputs should be `surface-container-lowest` with no border. 
- **Focus:** Transition background to `surface-container-high` and add a `primary` Ghost Border. This creates a "lighting up" effect rather than a mechanical change.

### Strategic Highlights (Custom Component)
- **The "Insight Ribbon":** A thin, vertical gradient line of `tertiary` to the left of a `body-lg` paragraph. This marks "Value Insights" in the report without requiring a bulky box.

---

## 6. Do’s and Don’ts

### Do
*   **DO** use whitespace as a luxury. If a page feels "full," increase the spacing between sections to `20 (7rem)`.
*   **DO** use `tertiary (#66dd8b)` exclusively for positive growth, "Value," and "Success" metrics.
*   **DO** use `surface-bright` for hover states on dark containers to create a "sheen" effect.

### Don’t
*   **DON'T** use 100% white (#FFFFFF). Always use `on_surface (#e3e2e8)` to reduce eye strain and maintain the "midnight" premium vibe.
*   **DON'T** use sharp corners. Stick to the `md (0.375rem)` for components and `xl (0.75rem)` for large containers to soften the high-tech edge.
*   **DON'T** use standard "Slide Transitions." If animating, use slow, staggered fades (600ms+) to mimic a high-end cinematic experience.