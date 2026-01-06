# VIS-4.3: Consent Architecture Spectrum - Generation Instructions

**Infographic**: Consent Architecture Spectrum (Coercive to Voluntary)
**Status**: ✅ Ready to generate
**Estimated time**: ~15-20 minutes total

---

## Quick Start: NotebookLM Workflow

### Step 1: Upload Source (2 min)

1. Go to [NotebookLM](https://notebooklm.google.com/)
2. Create notebook: `EventAI - Privacy & Regulation`
3. Upload: `consent-spectrum.content.md` (this folder)
4. Wait for processing (~30 sec)

### Step 2: Generate Infographic (10-15 min)

1. Click **"Infographic"** in generation menu
2. Settings:
   - **Detail Level**: Detailed
   - **Orientation**: Landscape (spectrum requires horizontal space)
3. **Paste prompt** below
4. Click **"Generate"**
5. Wait ~2 min for Nano Banana processing
6. **Generate 3 variations** (click regenerate 2 more times)

---

## 🔥 SPECTRUM PROMPT (Token-optimized ~310 tokens)

```
Horizontal spectrum: Consent Architecture Spectrum from Coercive to Voluntary designs for festival biometric systems

🚨 CRITICAL: Pure white background #FFFFFF, left-to-right gradient (red → orange → green), three distinct sections, real consent examples, GDPR principles embedded, festival context

STRUCTURE:
Horizontal spectrum bar with three sections (left=coercive red, middle=problematic orange, right=voluntary green)
Top: Gradient spectrum visualization
Each section: Examples with icons, titles, user agency assessment, legal status
Bottom: GDPR principles callout box

THREE SECTIONS (Left to Right):

LEFT SECTION: COERCIVE (Red #FF6B6B) - Non-Compliant
Background: Dark red, restrictive feel
Examples (4 boxes):
1. Mandatory Facial Recognition
   "Facial ID required. No alternatives."
   Icon: Prohibition symbol, single locked path
   User choice: Zero
   Legal status: PROHIBITED (Article 9 violation)

2. Bundled Consent
   "Accept liability + biometrics + marketing + analytics OR deny entry"
   Icon: Package with lock
   User choice: All or nothing
   Legal: VIOLATES Article 7 (not granular)

3. Pre-Checked Boxes
   "☑ Yes, use my face for security" (already checked when page loads)
   Icon: Checkbox marked, no user interaction
   User choice: Must actively uncheck
   Legal: ILLEGAL (silence ≠ consent)

4. Hidden in Terms
   "Biometric policy in paragraph 43(d) of 50-page document"
   Icon: Scroll, small text, magnifying glass needed
   User choice: Not practically available
   Legal: VIOLATES Article 9 (not informed/clear)

MIDDLE SECTION: PROBLEMATIC (Orange #ED8936) - Gray Area
Background: Amber, transitional feel
Examples (3 boxes):
1. Default Opt-In
   "Biometric on by default. Disable in settings."
   Icon: Toggle switch in ON position, settings icon
   User choice: Yes unless user discovers disable option
   Legal: LIKELY VIOLATES Article 7 (default bias)

2. Soft Wall Penalties
   "Facial recognition (3 minutes) OR ID check (2 hours)"
   Icon: Two paths, one wide/fast, one narrow/slow
   User choice: Technically available, practically coercive
   Legal: VIOLATES autonomy principle (penalty for refusal)

3. Confusing Interface
   "15 toggles, unclear language, contradictory options"
   Icon: Question marks, tangled paths, confused
   User choice: Users consent without understanding
   Legal: VIOLATES Article 9 (not clear/easily understood)

RIGHT SECTION: VOLUNTARY (Green #48BB78) - Compliant
Background: Bright green, open accessible feel
Examples (5 boxes):
1. Clear Opt-In
   "Use facial recognition for fast entry? YES / NO"
   Icon: Two equal buttons, clear choice
   User choice: Affirmative action required (not pre-selected)
   Legal: COMPLIANT (Article 7 - freely given, unambiguous)

2. Genuine Alternatives
   "Facial ID (instant) OR Paper ID (5 min) OR Manual check (free)"
   Icon: Three equal open paths, no hierarchy
   User choice: All options equally viable, none superior
   Legal: COMPLIANT (Article 7 - not conditional)

3. Granular Controls
   "Security: Yes/No  |  Analytics: Yes/No  |  Marketing: Yes/No"
   Icon: Three separate toggle switches
   User choice: Separate consent per purpose
   Legal: COMPLIANT (Article 9 - specific/granular)

4. Plain Language
   "We scan your face at entry. Image deleted after 30 days. Not used for marketing."
   Icon: Clear text, checkmarks, no jargon
   User choice: User understands implications
   Legal: COMPLIANT (Article 9 - clear/easily understood)

5. Easy Withdrawal
   "Turn off biometrics anytime. Settings → Biometric → Off (30 seconds)"
   Icon: One-click toggle, unlocked, simple process
   User choice: Can change mind without friction
   Legal: COMPLIANT (Article 7 - easily withdrawn)

PRINCIPLES BOX (Bottom, Green background):
Article 7 (Freely Given Consent):
✅ Not coerced (choice available, no penalties for refusal)
✅ Not conditional (consent separate from other services)
✅ Affirmative action (active choice, NOT silence/pre-checked)
✅ Easily withdrawn (can change mind anytime)

Article 9 (Special Category - Biometric):
✅ Explicit consent (higher bar than standard)
✅ Clear language (easily understood, plain words)
✅ Separate (granular per purpose/use)
✅ Alternative available (no penalty for refusal)

User Agency Gradient:
RED: No choice or illusory choice (prohibited)
ORANGE: Choice + friction (problematic)
GREEN: Clear equal alternatives (compliant)

STYLE:
- Background: Pure white #FFFFFF
- Gradient: Red #FF6B6B (left) → Orange #ED8936 (middle) → Green #48BB78 (right)
- Section backgrounds: Distinct colors (red/orange/green zones)
- Text: White on dark (red/orange), dark slate #2D3748 on light (green)
- Icons: Prohibition/lock (coercive), question/warning (problematic), checkmark/unlock (voluntary)
- Typography: Inter/Roboto bold titles (20-24pt), Source Sans body (12-14pt)
- Borders: Midnight slate #2D3748, 2-3px, rounded corners 8-12px
- Layout: Semi-flat, horizontal flow left-to-right, examples in boxes
- White space: 25-30% breathing room

REGULATORY ACCURACY (Embed exactly):
- Article 7: Freely given, specific, informed, unambiguous
- Article 9: Explicit, clear, separate, alternative available
- Real examples: Festival consent flows, entry procedures, ticketing scenarios
- Festival context: NOT generic consent patterns

❌ AVOID: Cream/beige background, vertical layout, unclear progression, missing real examples, generic consent icons, text <12pt, missing GDPR principles

✅ REFERENCE: Horizontal spectrum (left=coercive red, middle=problematic orange, right=voluntary green), real consent design patterns, GDPR Article 7 + 9 principles, festival biometric consent scenarios
```

---

## Step 3: Review Generated Variants (5 min)

### Quality Checklist

**✅ CRITICAL (Must Pass):**
- [ ] **Pure white background** (#FFFFFF, not cream/beige)
- [ ] **Three sections visible**: Coercive (red), Problematic (orange), Voluntary (green)
- [ ] **Examples present**: At least 3-4 per section with icons and descriptions
- [ ] **Color gradient obvious**: Clear left-to-right progression
- [ ] **Text legible**: Minimum 12pt for all text, titles 20-24pt
- [ ] **GDPR principles visible**: Article 7 and Article 9 callouts at bottom
- [ ] **User agency gradient shown**: Spectrum of choice levels (none → friction → clear)

**✅ STYLE (EventAI Compliance):**
- [ ] Colors accurate (red #FF6B6B, orange #ED8936, green #48BB78)
- [ ] Typography clean (Inter/Roboto, Source Sans)
- [ ] Semi-flat design, rounded corners
- [ ] Professional + educational mood
- [ ] Festival context (entry, ticketing, consent scenarios)

**✅ SPECTRUM-SPECIFIC:**
- [ ] Horizontal layout (left to right progression)
- [ ] Three distinct sections clearly separated
- [ ] Examples show real consent patterns (not generic)
- [ ] Icons convey restriction/confusion/openness appropriately
- [ ] Principles box at bottom, readable

### If Any Variant Fails Checklist

**Background NOT pure white?**
→ Regenerate: "Background EXACTLY #FFFFFF pure white, NOT cream/beige. Verify with color picker."

**Spectrum unclear (hard to see progression)?**
→ Regenerate: "Clear left-to-right gradient: red (coercive, left) → orange (problematic, middle) → green (voluntary, right). Color gradient obvious."

**Examples missing or generic?**
→ Regenerate: "Real consent patterns: mandatory ID, bundled consent, pre-checked boxes (coercive); default opt-in, soft penalties (problematic); clear opt-in, genuine alternatives, granular controls, plain language, easy withdrawal (compliant)."

**GDPR principles missing?**
→ Regenerate: "Include bottom box: Article 7 requirements (freely given, specific, informed, unambiguous) and Article 9 requirements (explicit, clear, separate, alternative available)."

**Text too small?**
→ Regenerate: "Minimum 12pt for all text, 14-16pt preferred. Titles 20-24pt. Print-ready sizes."

---

## Step 4: Download & Save (2 min)

### Download All Variants

1. Download each generated variant (PNG, high resolution)
2. Rename: `consent-spectrum-1.png`, `consent-spectrum-2.png`, `consent-spectrum-3.png`
3. Save to: `docs/writing/4-privacy/visuals/consent-spectrum/`

### Convert to WebP

```bash
cd docs/writing/4-privacy/visuals/consent-spectrum
todd-image-convert consent-spectrum-*.png --output-format webp --resolution 1080p
```

---

## Step 5: Evaluate & Select Winner (5 min)

### Run Comprehensive Evaluation

```bash
/ig-evaluate docs/writing/4-privacy/visuals/consent-spectrum/consent-spectrum-*.webp
```

### Expected Scores

**Spectrum variants**: 75-88/100 (if white background + clear gradient + real examples + GDPR principles + festival context)

### Select Winner

Choose variant with:
- Highest scores for clarity + EventAI style
- Clear color gradient (red → orange → green)
- Readable examples in each section
- Visible GDPR principles
- Pure white background
- Festival consent context

---

## Quick Command

```bash
# After generating in NotebookLM and downloading PNGs:
todd-image-convert docs/writing/4-privacy/visuals/consent-spectrum/*.png --output-format webp --resolution 1080p && /ig-evaluate docs/writing/4-privacy/visuals/consent-spectrum/*.webp
```

---

## Expected Outcomes

### What Success Looks Like

**Spectrum Layout:**
- Horizontal spectrum bar (left to right)
- Three color zones (red → orange → green)
- Examples in each zone with icons and descriptions
- Clear user agency gradient
- GDPR principles box at bottom
- Pure white background
- Festival biometric consent context

### File Deliverables

- ✅ `consent-spectrum-{N}.png` (3-5 MB, high-res PNG)
- ✅ `consent-spectrum-{N}.webp` (1-3 MB, web-optimized)
- ✅ `VIS-4.3-EVALUATION-REPORT.md` (comprehensive analysis)
- ✅ Winner selected and documented

---

## Troubleshooting

### Background NOT pure white
**Solution**: Regenerate with "🚨 Background EXACTLY #FFFFFF pure white, not cream/beige. Use color picker to verify."

### Spectrum unclear (hard to see gradient)
**Solution**: Regenerate with "Horizontal spectrum, clear left-to-right gradient: red (left) → orange (center) → green (right). Color zones distinct and obvious."

### Examples missing or generic
**Solution**: Regenerate with specific patterns: "Coercive: Mandatory facial ID, bundled consent, pre-checked boxes, hidden in terms. Problematic: default opt-in, soft penalties, confusing UI. Voluntary: clear opt-in, genuine alternatives, granular controls, plain language, easy withdrawal."

### GDPR principles missing
**Solution**: Regenerate with "Bottom callout box: Article 7 (freely given, specific, informed, unambiguous) and Article 9 (explicit, clear, separate, alternative). User agency gradient (no choice → friction → clear)."

### Not festival-specific
**Solution**: Regenerate with "Festival context: Entry ticketing, consent at gate, biometric facial recognition for security or entry speed. Real examples from festival operations."

---

## Related Documentation

- [VIS-4.3 Source Material](consent-spectrum.content.md)
- [EventAI Visual Identity](../../../lemmy/style-guide/eventai-visual-identity.md)
- [Privacy Visual Content Plan](../../VISUAL-CONTENT-PLAN.md)
- [/ig-evaluate Command](/.claude/commands/ig-evaluate.md)

---

*VIS-4.3 Generation Package - Consent Architecture Spectrum*
*Updated: December 29, 2025*
*Ready for NotebookLM generation*
