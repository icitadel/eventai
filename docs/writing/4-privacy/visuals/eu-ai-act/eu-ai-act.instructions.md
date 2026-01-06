# VIS-4.1: EU AI Act Risk Classification - Generation Instructions

**Infographic**: EU AI Act Risk Classification (Three-Tier Pyramid)
**Status**: ✅ Ready to generate
**Estimated time**: ~15-20 minutes total

---

## Quick Start: NotebookLM Workflow

### Step 1: Upload Source (2 min)

1. Go to [NotebookLM](https://notebooklm.google.com/)
2. Create notebook: `EventAI - Privacy & Regulation`
3. Upload: `eu-ai-act.content.md` (this folder)
4. Wait for processing (~30 sec)

### Step 2: Generate Infographic (10-15 min)

1. Click **"Infographic"** in generation menu
2. Settings:
   - **Detail Level**: Detailed
   - **Orientation**: Portrait (pyramid requires vertical space)
3. **Paste prompt** below
4. Click **"Generate"**
5. Wait ~2 min for Nano Banana processing
6. **Generate 3 variations** (click regenerate 2 more times)

---

## 🔥 PYRAMID PROMPT (Token-optimized ~280 tokens)

```
Three-tier pyramid: EU AI Act biometric system risk classification for festivals

🚨 CRITICAL: Pure white background #FFFFFF (NOT cream/beige), three equal-height tiers (prohibited/high-risk/limited-risk), festival context, exact regulatory details

STRUCTURE:
Vertical pyramid: top tier (prohibited), middle tier (high-risk), bottom tier (limited-risk, widest)
Each tier: colored background + title + regulatory stat + practice list + icon

TIERS (Top to Bottom):

1️⃣ PROHIBITED (Red #FF6B6B - Top)
Title: "PROHIBITED" (28-32pt bold, white text)
Stat: "€35M or 7% Turnover Fine" (40-48pt bold, white)
Enforcement: "Since Feb 2, 2025" (18-20pt white)
Practices (white text, 14-16pt):
- Real-time biometric ID in public spaces
- Untargeted web scraping (Clearview AI-style databases)
- Emotion recognition systems
Icon: Prohibition symbol + enforcement badge

2️⃣ HIGH-RISK (Orange #ED8936 - Middle)
Title: "HIGH-RISK" (28-32pt bold, dark)
Stat: "Conformity Assessment Required" (32-36pt bold, orange)
Requirements (dark text, 14-16pt):
- Post-event biometric ID permitted
- Mandatory third-party assessment
- Technical documentation + human oversight
- Transparent disclosure to attendees
Real example: ✅ Danish football (DPA-approved with safeguards)
Icon: Warning symbol + checklist + badge

3️⃣ LIMITED-RISK (Green #48BB78 - Bottom, Widest)
Title: "LIMITED-RISK" (28-32pt bold, dark)
Stat: "Disclosure Only" (32-36pt bold, green)
Allowed (dark text, 14-16pt):
- Chatbots with AI disclosure
- Recommendation systems (transparent, user choice)
- No biometric data required
Icon: Checkmark + information symbol

STYLE:
- Background: Pure white #FFFFFF (exactly, not cream/beige)
- Tier colors: Red #FF6B6B, orange #ED8936, green #48BB78 (exact hex)
- Text: White on red/orange/green, dark slate #2D3748 on lighter areas
- Typography: Inter/Roboto bold titles (28-32pt), Source Sans/Lato body (14-16pt minimum)
- Icons: Regulatory context (badges, prohibition, warnings, checkmarks) NOT generic
- Borders: Midnight slate #2D3748, 2-3px, rounded corners 8-12px
- Layout: Semi-flat, equal tier heights, 25-30% white space, vertical pyramid proportions

REGULATORY DETAILS (Embed exactly):
- Prohibited: €35M or 7% global turnover fine, enforcement Feb 2, 2025
- High-risk: Post-event ID (with safeguards), conformity assessment required
- Limited-risk: AI disclosure, recommendation systems with user choice

❌ AVOID: Cream/beige backgrounds, horizontal layouts, unequal tiers, generic business icons, text <14pt, missing enforcement date

✅ REFERENCE: Three-tier pyramid (top=prohibited, middle=high-risk, bottom=limited-risk), clear regulatory labels, festival context
```

---

## Step 3: Review Generated Variants (5 min)

### Quality Checklist

**✅ CRITICAL (Must Pass):**
- [ ] **Pure white background** (#FFFFFF, not cream/beige)
- [ ] **Three tiers present** with correct names (PROHIBITED, HIGH-RISK, LIMITED-RISK)
- [ ] **Regulatory details accurate**: €35M, 7%, Feb 2 2025, conformity assessment
- [ ] **Pyramid structure**: Vertical, equal heights, proportional widths
- [ ] **Text legible**: Minimum 14pt body, clear hierarchy (stats bold/prominent)
- [ ] **Festival context**: Not generic legal diagram (references concerts, biometrics, festivals)

**✅ STYLE (EventAI Compliance):**
- [ ] Colors match palette (red #FF6B6B, orange #ED8936, green #48BB78)
- [ ] Typography clean (Inter/Roboto headings, Source Sans/Lato body)
- [ ] Semi-flat design, rounded corners, minimal decoration
- [ ] Professional + authoritative mood (regulatory content)

**✅ PYRAMID-SPECIFIC:**
- [ ] All three tiers visible and equal height
- [ ] Top tier (prohibited) narrowest, bottom tier (limited-risk) widest (or equal)
- [ ] Tiers clearly differentiated by color
- [ ] Icons present in each tier

### If Any Variant Fails Checklist

**Background NOT pure white?**
→ Regenerate: "Background must be EXACTLY #FFFFFF pure white, NOT cream/beige. Use color picker to verify."

**Regulatory stats wrong/missing?**
→ Regenerate: "Prohibited tier: €35M or 7% turnover fine, enforcement Feb 2, 2025. Exact details must appear."

**Tiers unequal/unclear?**
→ Regenerate: "Three EQUAL-HEIGHT tiers: Prohibited (top/narrow), High-Risk (middle), Limited-Risk (bottom/widest). Vertical pyramid structure."

**Text too small?**
→ Regenerate: "Minimum 14pt body text, 16pt preferred. Statistics 40-48pt (prohibited), 32-36pt (others). Print-ready sizes."

**Generic legal diagram (not festival context)?**
→ Regenerate: "Festival-specific context: biometric systems at concerts, real examples (Taylor Swift Rose Bowl, Danish football), deployment scenarios."

---

## Step 4: Download & Save (2 min)

### Download All Variants

1. Download each generated variant (PNG, high resolution)
2. Rename: `eu-ai-act-1.png`, `eu-ai-act-2.png`, `eu-ai-act-3.png`
3. Save to: `docs/writing/4-privacy/visuals/eu-ai-act/`

### Convert to WebP

```bash
cd docs/writing/4-privacy/visuals/eu-ai-act
todd-image-convert eu-ai-act-*.png --output-format webp --resolution 1080p
```

---

## Step 5: Evaluate & Select Winner (5 min)

### Run Comprehensive Evaluation

```bash
/ig-evaluate docs/writing/4-privacy/visuals/eu-ai-act/eu-ai-act-*.webp
```

### Expected Scores

**Pyramid variants**: 75-88/100 (if white background + regulatory accuracy + festival context)

### Select Winner

Choose variant with:
- Highest scores for EventAI style + regulatory accuracy
- Clear three-tier structure
- Readable statistics
- Pure white background
- Festival deployment context

---

## Quick Command

```bash
# After generating in NotebookLM and downloading PNGs:
todd-image-convert docs/writing/4-privacy/visuals/eu-ai-act/*.png --output-format webp --resolution 1080p && /ig-evaluate docs/writing/4-privacy/visuals/eu-ai-act/*.webp
```

---

## Expected Outcomes

### What Success Looks Like

**Pyramid Layout:**
- Three-tier vertical pyramid (prohibited/high-risk/limited-risk)
- Color-coded tiers (red/orange/green)
- Clear regulatory statistics and requirements
- Festival context (not generic legal infographic)
- Pure white background
- Professional + authoritative mood

### File Deliverables

- ✅ `eu-ai-act-{N}.png` (3-5 MB, high-res PNG)
- ✅ `eu-ai-act-{N}.webp` (1-3 MB, web-optimized)
- ✅ `VIS-4.1-EVALUATION-REPORT.md` (comprehensive analysis)
- ✅ Winner selected and documented

---

## Troubleshooting

### Background NOT pure white
**Solution**: Regenerate with "🚨 Background EXACTLY #FFFFFF, not cream/beige/off-white. Use color picker to verify."

### Regulatory details wrong
**Solution**: Regenerate with exact stats: "€35M fine, 7% turnover, Feb 2 2025 enforcement, conformity assessment requirement, post-event ID permitted"

### Generic legal diagram (not festival context)
**Solution**: Regenerate with "Festival-specific: Real examples (Taylor Swift Rose Bowl, Danish police football), biometric systems at concerts, festival organizer perspective"

### Tiers unclear/unequal
**Solution**: Regenerate with "Three equal-height vertical tiers: PROHIBITED (top), HIGH-RISK (middle), LIMITED-RISK (bottom). Pyramid proportions."

---

## Related Documentation

- [VIS-4.1 Source Material](eu-ai-act.content.md)
- [EventAI Visual Identity](../../../lemmy/style-guide/eventai-visual-identity.md)
- [Privacy Visual Content Plan](../../VISUAL-CONTENT-PLAN.md)
- [/ig-evaluate Command](/.claude/commands/ig-evaluate.md)

---

*VIS-4.1 Generation Package - EU AI Act Risk Classification*
*Updated: December 29, 2025*
*Ready for NotebookLM generation*
