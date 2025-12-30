# VIS-2.2: Academic AI Integration Map - Generation Instructions

**Infographic**: 3% Academic AI Coverage Disparity
**Status**: 📋 READY TO GENERATE
**Estimated time**: ~15-20 minutes

---

## Quick Start: NotebookLM Workflow

### Step 1: Upload Source (2 min)

1. Go to [NotebookLM](https://notebooklm.google.com/)
2. Create notebook: `EventAI - Education - Academic Integration`
3. Upload: `academic-integration.content.md` (this folder)
4. Wait for processing (~30 sec)

### Step 2: Generate Infographic (10-15 min)

1. Click **"Infographic"** in generation menu
2. Settings:
   - **Detail Level**: Standard
   - **Orientation**: Square or Portrait (conceptual diagram works in both)
3. **Paste prompt**: Use `academic-integration.prompt.md` (this folder)
4. Click **"Generate"**
5. Wait ~2 min for Nano Banana processing
6. **Generate 3 variations** (click regenerate 2 more times)

### Step 3: Quality Check (3-5 min)

For each variant, check:

**Visual Hierarchy**:
- ✅ 3 lit-up universities clearly prominent (Surrey, Southern Cross, Penn State)
- ✅ Many faded background institutions visible but de-emphasized
- ✅ "3/100+ = 3% coverage" stat prominently displayed
- ✅ Clear visual contrast between WITH and WITHOUT AI programs

**Factual Accuracy**:
- ✅ 3 universities correctly named (Surrey UK, Southern Cross Australia, Penn State US)
- ✅ Leeds Beckett UKCEM and UCF Rosen shown as examples WITHOUT AI
- ✅ Stats accurate: 3%, 97%, 71% skills gap
- ✅ Vicious cycle stages correct (if included)

**EventAI Style Compliance**:
- ✅ Background: Pure white #FFFFFF (NOT beige/cream)
- ✅ Colors: Purple #6B46C1 + Coral #FF6B6B (WITH AI), Gray (WITHOUT AI)
- ✅ NOT a literal geographic map (conceptual diagram only)
- ✅ Festival/event context (NOT generic academic imagery)
- ✅ White space ≥30%
- ✅ Professional + energetic mood

**Accessibility**:
- ✅ Text readable (university names at 14-16pt minimum)
- ✅ Strong contrast between lit/faded institutions
- ✅ Stats legible at 48-72pt

### Step 4: Save (2 min)

1. **Select best variant** (or top 2-3 for comparison)
2. Download high-resolution PNG
3. Save as: `academic-integration-1.png`, `academic-integration-2.png`, etc.
4. Place in this folder

### Step 5: Evaluate (Optional)

Use `/ig-evaluate` command to assess quality:
```bash
/ig-evaluate academic-integration-1.png
```

This will generate `academic-integration.eval.md` with detailed scoring.

---

## Common Issues & Fixes

### Issue: Literal geographic map instead of conceptual diagram
**Fix**: Add to prompt: "NOT a literal map with pins/locations. Use conceptual diagram showing disparity through brightness/size contrast. Stylized building icons, NOT map geography."

### Issue: Equal visual weight for all universities
**Fix**: Add: "3 universities WITH AI must be MUCH larger, brighter, more prominent than the many small faded universities WITHOUT AI. Clear David vs. Goliath visual disparity."

### Issue: Generic academic imagery (graduation caps, books, scrolls)
**Fix**: Add: "Festival/event management context. Use event-related imagery where possible. Professional but NOT boring academic style."

### Issue: Missing key statistics
**Fix**: Add: "MUST include: '3/100+ = 3%', '97% teach ZERO AI', '71% skills gap'. Stats should be prominently displayed."

### Issue: Vicious cycle too detailed/cluttered
**Fix**: Reduce cycle detail to 3-4 key points OR omit cycle if space is limited. Focus on the 3 vs. 100+ disparity as primary message.

---

## Expected Output Quality

**Target Scores** (from /ig-evaluate):
- Visual Clarity: 85-95/100
- Information Accuracy: 90-100/100 (correct universities and stats)
- EventAI Style: 80-95/100
- Accessibility: 80-90/100
- Overall: 85-95/100

**Acceptable Range**: 80-100 (most categories)
**Red Flags**: <70 in any category requires regeneration

---

## Alternative: Nano Banana Direct

If NotebookLM is unavailable, use Google AI Studio or Gemini API with the prompt from `academic-integration.prompt.md`.

---

## Next Steps After Generation

1. ✅ Save best variant(s) to this folder
2. ✅ Run `/ig-evaluate` to document quality
3. ✅ Convert to WebP using `/todd-image-convert` for web use
4. ✅ Update status in `../../README.md`
5. ✅ Reference in education draft

---

**Related Files**:
- [academic-integration.content.md](./academic-integration.content.md) - Full source material
- [academic-integration.prompt.md](./academic-integration.prompt.md) - Token-optimized prompt
- [../../README.md](../../README.md) - Education section visual overview

**Part of**: EventAI Curriculum - Topic 2: Education
**Last Updated**: December 29, 2025
