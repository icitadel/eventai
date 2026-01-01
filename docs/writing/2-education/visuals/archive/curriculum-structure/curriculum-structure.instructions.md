# VIS-2.4: Proposed AI Literacy Curriculum - Generation Instructions

**Infographic**: 15-Week Educational Course Structure
**Status**: 📋 READY TO GENERATE
**Estimated time**: ~15-20 minutes

---

## Quick Start: NotebookLM Workflow

### Step 1: Upload Source (2 min)

1. Go to [NotebookLM](https://notebooklm.google.com/)
2. Create notebook: `EventAI - Education - Curriculum Structure`
3. Upload: `curriculum-structure.content.md` (this folder)
4. Wait for processing (~30 sec)

### Step 2: Generate Infographic (10-15 min)

1. Click **"Infographic"** in generation menu
2. Settings:
   - **Detail Level**: Standard
   - **Orientation**: Portrait (educational course structure)
3. **Paste prompt**: Use `curriculum-structure.prompt.md` (this folder)
4. Click **"Generate"**
5. Wait ~2 min for Nano Banana processing
6. **Generate 3 variations** (click regenerate 2 more times)

### Step 3: Quality Check (3-5 min)

For each variant, verify:

#### Visual Hierarchy
- ✅ Portrait orientation (taller than wide, ~9:16 or 3:5 ratio)
- ✅ 4 distinct modules stack vertically (blue → teal → purple → coral)
- ✅ Week ranges clearly visible on left (1-4, 5-8, 9-12, 13-15)
- ✅ Module headers stand out from body text
- ✅ 5 major deliverables labeled with icons (chatbot, case study, ethics, debate, policy paper)
- ✅ Learning progression callouts visible ("Understanding" → "Evaluation" → "Decision-Making")

#### Educational Structure Completeness
- ✅ **Module 1 (Weeks 1-4)**: Fundamentals, hands-on chatbot project visible
- ✅ **Module 2 (Weeks 5-8)**: Evaluation, GDPR/regulation, Paris 2024 case study shown
- ✅ **Module 3 (Weeks 9-12)**: Ethics, algorithmic bias, ethical framework project shown
- ✅ **Module 4 (Weeks 13-15)**: Industry perspectives, debate, final policy paper shown
- ✅ Progressive deepening visible (color intensity increases, topics get more complex)

#### Factual Accuracy - Module Content
- ✅ **Module 1**: AI fundamentals, festival examples (Coachella, Glastonbury, Tomorrowland, SXSW), hands-on chatbot
- ✅ **Module 2**: Evidence assessment, GDPR/EU AI Act regulations, Paris 2024 Olympic facial recognition (180,000 faces)
- ✅ **Module 3**: NIST facial recognition bias study, Uber dynamic pricing case study, algorithmic bias concepts
- ✅ **Module 4**: Guest lectures (vendor, ops manager, legal expert), facial recognition debate, final policy paper (3,000-4,000 words)
- ✅ All deliverables mentioned with proper week assignments

#### EventAI Style Compliance
- ✅ Background: Pure white #FFFFFF (NOT beige, NOT cream, NOT off-white)
- ✅ Module colors: Sky blue #4299E1 (Module 1), Teal #17A2B8 (Module 2), Deep purple #6B46C1 (Module 3), Coral #FF6B6B (Module 4)
- ✅ Text color: Midnight slate #2D3748 (high contrast, readable)
- ✅ Typography: Inter bold headers, Source Sans Pro body
- ✅ Festival context icons ONLY: stages, crowds, security gates, event apps, wristbands, headsets
- ✅ NO generic corporate imagery (no gears, lightbulbs, money bags, handshakes)
- ✅ White space ≥30% (NOT cramped)
- ✅ Rounded corners 8-12px on module cards
- ✅ Semi-flat style with subtle depth (NOT overly 3D)
- ✅ Professional + energetic mood (educational but engaging, NOT boring)

#### Accessibility
- ✅ Text readable at 12-14pt minimum (no tiny text)
- ✅ WCAG AA contrast ratios met (dark text on light background)
- ✅ Not color-dependent: icons and labels clarify meaning beyond color alone
- ✅ Visual flow is clear and logical (top to bottom progression)

#### Portrait Orientation Specific
- ✅ Aspect ratio shows "taller than wide" (portrait, not landscape)
- ✅ Vertical flow: modules stack downward naturally
- ✅ Week numbers integrated into left margin or side
- ✅ Content doesn't feel squished or horizontally cramped
- ✅ Readable without requiring horizontal scrolling on phone/tablet

### Step 4: Save (2 min)

1. **Select best variant** (or top 2-3 for comparison)
2. Download high-resolution PNG (preferred) or WebP
3. Save as: `curriculum-structure-1.png`, `curriculum-structure-2.png`, etc.
4. Place in this folder

### Step 5: Evaluate (Optional)

Use `/ig-evaluate` command to assess quality:
```bash
/ig-evaluate curriculum-structure-1.png
```

This will generate `curriculum-structure.eval.md` with detailed scoring.

---

## Alternative: Nano Banana Direct (if NotebookLM unavailable)

### Option A: Google AI Studio

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Select **Imagen 3** model
3. Paste the full prompt from `curriculum-structure.prompt.md`
4. Set aspect ratio to **portrait** (9:16 or 3:5)
5. Generate 3-4 variations
6. Download best result

### Option B: Gemini API (Programmatic)

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

with open("curriculum-structure.prompt.md") as f:
    prompt = f.read()

model = genai.GenerativeModel('imagen-3.0-generate-001')
response = model.generate_images(
    prompt=prompt,
    number_of_images=4,
    safety_filter_level="block_only_high",
    aspect_ratio="9:16"  # Portrait orientation
)

for i, image in enumerate(response.images):
    image.save(f"curriculum-structure-{i+1}.png")
```

---

## Common Issues & Fixes

### Issue: Landscape orientation instead of portrait
**Fix**: Explicitly state in prompt regeneration: "Aspect ratio MUST be portrait (9:16 or 3:5), taller than wide, NOT landscape"

### Issue: Modules not clearly distinguished (color blending)
**Fix**: Add to prompt: "Strong color separation between modules: Module 1 = sky blue #4299E1, Module 2 = teal #17A2B8, Module 3 = deep purple #6B46C1, Module 4 = coral #FF6B6B. Each module color must be visually distinct."

### Issue: Deliverables not visible or labeled
**Fix**: Add: "Show all 5 deliverables prominently: Week 4 chatbot (🤖), Week 8 Paris 2024 case study (📋), Week 12 ethical assessment (⚖️), Week 14 debate (🎤), Week 15 policy paper (📄). Each must have icon and label."

### Issue: Generic corporate icons instead of festival imagery
**Fix**: Add: "Festival-specific icons ONLY: stages, crowds, security gates, event apps, wristbands, headsets. NO generic corporate imagery (gears, lightbulbs, money bags, handshakes, gavel)"

### Issue: White space too cramped or text too small
**Fix**: Add: "White space ≥30%. Text sizes: Module headers 28-32pt, week numbers 20-24pt, body text 12-14pt. Plenty of breathing room between modules."

### Issue: Beige/cream background instead of pure white
**Fix**: Add: "Background MUST be pure white #FFFFFF (NOT cream, NOT beige, NOT off-white)"

### Issue: Missing regulatory/ethical content details
**Fix**: Add: "Make visible: GDPR (Module 2), EU AI Act (Module 2), NIST bias study (Module 3), Uber pricing case (Module 3), Paris 2024 Olympic facial recognition (Module 2), three ethical frameworks (Module 3)"

### Issue: Learning progression not apparent
**Fix**: Add: "Show clear learning progression: Stage 1 'Understanding' (Weeks 1-4), Stage 2 'Evaluation' (Weeks 5-12), Stage 3 'Decision-Making' (Weeks 13-15). Use color intensification to show deepening."

---

## Expected Output Quality

**Target Scores** (from /ig-evaluate):
- Visual Clarity: 85-95/100 (portrait orientation clear, modules distinct)
- Information Accuracy: 90-100/100 (all curriculum details correct)
- EventAI Style: 80-95/100 (colors, typography, festival context)
- Accessibility: 80-90/100 (readable, high contrast, logical flow)
- Overall: 85-95/100

**Acceptable Range**: 80-100 (most categories)
**Red Flags**: <70 in any category requires regeneration

---

## Next Steps After Generation

1. ✅ Save best variant(s) to this folder
2. ✅ Run `/ig-evaluate` to document quality (optional but recommended)
3. ✅ Convert to WebP using `/todd-image-convert` for web optimization
4. ✅ Update status in `../../README.md`
5. ✅ Reference in education draft: `![Proposed AI Literacy Curriculum](visuals/curriculum-structure/curriculum-structure-1.png)`

---

## Quality Criteria Summary

### MUST HAVE:
- ✅ Portrait orientation (taller than wide)
- ✅ 4 modules with progressive colors (blue → teal → purple → coral)
- ✅ All 5 deliverables visible with icons
- ✅ Week ranges clearly marked (1-4, 5-8, 9-12, 13-15)
- ✅ Learning progression labeled
- ✅ Festival context imagery (NOT generic)
- ✅ Pure white background
- ✅ EventAI color palette
- ✅ Text readable (12pt+)
- ✅ White space ≥30%

### SHOULD HAVE:
- ✅ Key curriculum details visible (GDPR, bias, ethics, debate, etc.)
- ✅ Rounded corners on module cards
- ✅ Semi-flat style with subtle depth
- ✅ Professional + energetic mood
- ✅ Color bar or visual indicator on left margin for each module

### NICE TO HAVE:
- Visual flow lines showing progression
- Mini-icons representing key concepts per module
- Week-specific callouts for major milestones
- Festival names mentioned (Coachella, Glastonbury, Paris 2024, etc.)

---

## Related Files

- [curriculum-structure.content.md](./curriculum-structure.content.md) - Full curriculum details
- [curriculum-structure.prompt.md](./curriculum-structure.prompt.md) - Token-optimized generation prompt
- [../../README.md](../../README.md) - Education section visual overview

**Part of**: EventAI Curriculum - Topic 2: Education - VIS-2.4
**Last Updated**: December 29, 2025
