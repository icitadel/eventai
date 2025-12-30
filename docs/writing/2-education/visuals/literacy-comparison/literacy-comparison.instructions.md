# VIS-2.1: Functional vs. Critical AI Literacy - Generation Instructions

**Infographic**: Comparison of Two Types of AI Literacy
**Status**: 📋 READY TO GENERATE
**Estimated time**: ~15-20 minutes

---

## Quick Start: NotebookLM Workflow

### Step 1: Upload Source (2 min)

1. Go to [NotebookLM](https://notebooklm.google.com/)
2. Create notebook: `EventAI - Education - Literacy Comparison`
3. Upload: `literacy-comparison.content.md` (this folder)
4. Wait for processing (~30 sec)

### Step 2: Generate Infographic (10-15 min)

1. Click **"Infographic"** in generation menu
2. Settings:
   - **Detail Level**: Standard
   - **Orientation**: Landscape (side-by-side comparison)
3. **Paste prompt**: Use `literacy-comparison.prompt.md` (this folder)
4. Click **"Generate"**
5. Wait ~2 min for Nano Banana processing
6. **Generate 3 variations** (click regenerate 2 more times)

### Step 3: Quality Check (3-5 min)

For each variant, check:

**Visual Hierarchy**:
- ✅ Clear left/right split (Functional vs Critical)
- ✅ Center "Gap" callout stands out
- ✅ Headers distinct from body text
- ✅ Key stats (71%, 42%, 3%) prominently displayed

**Factual Accuracy**:
- ✅ MPI/PCMA: 7.5 hours, $300-700
- ✅ Proposed critical literacy: 15 weeks
- ✅ Academic coverage: 3/100+ programs (3%)
- ✅ Skills gap: 71%
- ✅ Zero ROI: 42%

**EventAI Style Compliance**:
- ✅ Background: Pure white #FFFFFF (NOT beige/cream)
- ✅ Colors: Blue #4299E1 (functional), Purple #6B46C1 (critical), Coral #FF6B6B (gap)
- ✅ Typography: Inter bold headers, Source Sans Pro body
- ✅ Festival context icons (NOT generic business imagery)
- ✅ White space ≥30%
- ✅ Rounded corners 8-12px
- ✅ Professional + whimsy balance

**Accessibility**:
- ✅ Text readable at 14-16pt minimum
- ✅ WCAG AA contrast ratios met
- ✅ Not color-dependent (labels + icons clarify meaning)

### Step 4: Save (2 min)

1. **Select best variant** (or top 2-3 for comparison)
2. Download high-resolution PNG
3. Save as: `literacy-comparison-1.png`, `literacy-comparison-2.png`, etc.
4. Place in this folder

### Step 5: Evaluate (Optional)

Use `/ig-evaluate` command to assess quality:
```bash
/ig-evaluate literacy-comparison-1.png
```

This will generate `literacy-comparison.eval.md` with detailed scoring.

---

## Alternative: Nano Banana Direct (if NotebookLM unavailable)

### Option A: Google AI Studio

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Select **Imagen 3** model
3. Paste the full prompt from `literacy-comparison.prompt.md`
4. Generate 3-4 variations
5. Download best result

### Option B: Gemini API (Programmatic)

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

with open("literacy-comparison.prompt.md") as f:
    prompt = f.read()

model = genai.GenerativeModel('imagen-3.0-generate-001')
response = model.generate_images(
    prompt=prompt,
    number_of_images=4,
    safety_filter_level="block_only_high",
    aspect_ratio="16:9"
)

for i, image in enumerate(response.images):
    image.save(f"literacy-comparison-{i+1}.png")
```

---

## Common Issues & Fixes

### Issue: Beige/cream background instead of pure white
**Fix**: Add to prompt: "Background color: Pure white #FFFFFF (NOT cream, NOT beige, NOT off-white)"

### Issue: Generic business icons (gears, money bags, lightbulbs)
**Fix**: Add: "Festival-specific imagery ONLY: stages, wristbands, crowds, ticket scanners, event apps. NO generic corporate icons."

### Issue: Text too small or cluttered
**Fix**: Reduce detail level to "Concise" OR add: "White space ≥30%. Text sizes: Headers 24-36pt, Body 14-16pt, Stats 48-72pt."

### Issue: Poor contrast between functional/critical sections
**Fix**: Add: "Strong visual separation between left (blue) and right (purple) sections. Center gap callout in coral."

### Issue: Missing key statistics
**Fix**: Add: "MUST include these exact stats: 71% skills gap, 42% zero ROI, 3/100+ programs, 7.5 hrs vs 15 weeks, $300-700"

---

## Expected Output Quality

**Target Scores** (from /ig-evaluate):
- Visual Clarity: 85-95/100
- Information Accuracy: 90-100/100 (all stats correct)
- EventAI Style: 80-95/100
- Accessibility: 80-90/100
- Overall: 85-95/100

**Acceptable Range**: 80-100 (most categories)
**Red Flags**: <70 in any category requires regeneration

---

## Next Steps After Generation

1. ✅ Save best variant(s) to this folder
2. ✅ Run `/ig-evaluate` to document quality
3. ✅ Convert to WebP using `/todd-image-convert` for web use
4. ✅ Update status in `../../README.md`
5. ✅ Reference in education draft: `![Functional vs. Critical AI Literacy](visuals/literacy-comparison/literacy-comparison-1.png)`

---

**Related Files**:
- [literacy-comparison.content.md](./literacy-comparison.content.md) - Full source material
- [literacy-comparison.prompt.md](./literacy-comparison.prompt.md) - Token-optimized prompt
- [../../README.md](../../README.md) - Education section visual overview

**Part of**: EventAI Curriculum - Topic 2: Education
**Last Updated**: December 29, 2025
