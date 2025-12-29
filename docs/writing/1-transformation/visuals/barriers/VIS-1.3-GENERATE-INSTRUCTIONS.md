# VIS-1.3: Barriers to AI Transformation - NotebookLM Generation Instructions

**Infographic**: Five Barriers to AI Transformation at Festivals
**Status**: Ready to generate (IMPROVED prompt based on evaluation)
**Estimated time**: ~17 minutes

**⚠️ PROMPT UPDATED:** December 28, 2025 - Based on evaluation of Variants 1-3 (see VIS-1.3-EVALUATION-REPORT.md)

**Critical improvements added:**
- ✅ Pure white background requirement (NOT cream/beige)
- ✅ 30%+ white space minimum emphasized
- ✅ 14pt minimum body text for print readability
- ✅ Equal segment sizing requirement reinforced
- ✅ Common issues flagged in AVOID section

---

## Step 1: Upload Source to NotebookLM (2 min)

1. **Go to NotebookLM**: [https://notebooklm.google.com/](https://notebooklm.google.com/)
2. **Create new notebook**: Click "+ New notebook" or "New"
3. **Name it**: `EventAI - Transformation Barriers`
4. **Upload source**:
   - Click "Add sources" or drag-and-drop
   - Upload file: `VIS-1.3-source.md` (this folder)
   - Wait for processing (~10-30 seconds)

---

## Step 2: Generate Infographic (10 min)

### Access Infographic Feature

1. Click **"Infographic"** option in content generation menu
2. Or find "Create infographic" button

### Configuration

**Detail Level**: **Detailed** (comprehensive barrier explanation)

**Orientation**: **Square** or **Portrait** (pentagon/radial works best in square format)

### Customization Prompt

**Copy and paste this entire prompt into the NotebookLM customization field:**

```
Pentagon infographic: 5 Major Barriers to AI Transformation at festivals

⚠️ CRITICAL: Pure white background #FFFFFF (NOT cream/beige), 30%+ white space, 14pt+ body text, exactly equal segments

STRUCTURE: Pentagon with 5 equal wedges from center. Each wedge: icon + title + stat + brief description.

BARRIERS (clockwise from top):

1. ECONOMIC CONSTRAINTS (Coral #FF6B6B)
   Icon: Money bag, declining chart | Stat: "$566K Investment • 80% No ROI"
   Text: "Most see no impact. Only 6% high performers."

2. DATA QUALITY (Sunlight #F6AD55)
   Icon: Database warning | Stat: "Cold-Start Problem"
   Text: "Annual festivals = 1 training opportunity/year."

3. REGULATORY UNCERTAINTY (Amber #ED8936)
   Icon: Gavel, EU flag | Stat: "€35M Fines"
   Text: "EU AI Act bans real-time biometrics. 40+ festivals banned facial recognition."

4. TECHNICAL COMPLEXITY (Blue #4299E1)
   Icon: Tangled wires, gears | Stat: "10+ Vendor Integrations"
   Text: "Temporary environments, harsh conditions create integration debt."

5. ETHICAL TENSIONS (Purple #6B46C1)
   Icon: Balance scales | Stat: "Serendipity vs. Optimization"
   Text: "Over-optimization risks festival magic, creates filter bubbles."

STYLE:
- Colors: #FF6B6B, #F6AD55, #ED8936, #4299E1, #6B46C1 on PURE WHITE #FFFFFF
- Typography: Bold Inter titles (24-28pt), stats (48-56pt), Source Sans body (14-16pt minimum)
- Design: Semi-flat, rounded corners (8-12px), 2-3px outlines, minimal decoration
- Layout: 30%+ white space, equal wedges, generous padding (10-12px inside segments)
- Festival context icons (not generic business), professional tone

AVOID: Cream/beige background, text <14pt, cramped layout, unequal segments, generic imagery
```

### Generate

1. Click **"Generate Infographic"**
2. Wait **1-2 minutes** (Nano Banana Pro processing)
3. Image will appear when ready

---

## Step 3: Review & Download (5 min)

### Quality Checklist

✅ **Content Accuracy**:
- [ ] All 5 barriers present and labeled correctly
- [ ] Key statistics match source material
  - $566K investment ✅
  - 80%+ no ROI ✅
  - €35M fines ✅
  - 40+ festivals banned facial recognition ✅
- [ ] Icons appropriate for each barrier type
- [ ] Equal visual weight given to each barrier

✅ **EventAI Style**:
- [ ] Colors match palette (coral, sunlight, amber, blue, purple)
- [ ] Typography readable (Inter headings, Source Sans Pro body)
- [ ] Clean white background
- [ ] Minimal decoration (high data-ink ratio)

✅ **Visual Structure**:
- [ ] Pentagon/radial OR vertical stacked (clear structure)
- [ ] Each barrier distinct and identifiable
- [ ] Center title present and prominent
- [ ] Layout clean and scannable

✅ **Festival Context**:
- [ ] Icons relate to festival operations (not generic business)
- [ ] Professional tone appropriate for educational use
- [ ] Not generic business barriers imagery

✅ **Accessibility**:
- [ ] Text legible at intended display size
- [ ] High contrast between text and backgrounds
- [ ] Information not color-dependent (icons + text + color)

### If Unsatisfactory

**Option 1**: Regenerate with same prompt (may get variation)
**Option 2**: Adjust prompt to emphasize problematic element
**Option 3**: Try different detail level (Brief or Comprehensive)

Generate **2-3 variations** and select best.

---

## Step 4: Download & Save (2 min)

### Download

1. Click download icon (down arrow)
2. File format: **PNG** (high resolution)
3. Save to your computer

### Rename and Move

1. **Rename file**: `transformation-infographic-barriers-1.png` (increment number for variants)
2. **Move to**: `docs/writing/1-transformation/visuals/barriers/` (this folder)

### Verify Quality

1. Open in image viewer
2. Check resolution (should be high-res, print-ready)
3. Zoom in to verify text is crisp
4. Check all 5 barriers are clearly visible

---

## Step 5: Convert to WebP (1 min)

### Convert using todd-image-convert

```bash
cd docs/writing/1-transformation/visuals/barriers
todd-image-convert transformation-infographic-barriers-*.png --output-format webp --resolution 1080p --replace
```

This will create `transformation-infographic-barriers-{1,2,3}.webp` files optimized for web use.

---

## Step 6: Evaluate & Select Winner (5 min)

### Run Evaluation

```bash
/ig-evaluate docs/writing/1-transformation/visuals/barriers/*.webp
```

The evaluation will assess:
- EventAI style compliance (color palette, typography, layout)
- Best practices adherence (Tufte principles, data-ink ratio)
- Data accuracy (all statistics verified against source)
- Festival context integration
- Accessibility compliance

### Select Winner

Based on evaluation scores:
- Choose highest-scoring variant
- Or manually select if specific element preferred
- Document selection rationale

---

## Expected Outcome

### What You Should Have

**File**: `transformation-infographic-barriers-{N}.png` (where N is winning variant)

**Content**:
- Pentagon/radial or vertical stacked diagram showing 5 barriers
- Each barrier with icon, title, key statistic, description
- EventAI visual style (purple, coral, amber, blue, sunlight colors)
- Clean, professional, educational presentation
- Festival context (not generic business)

**File size**: Likely 2-5 MB (high-resolution PNG)
**Resolution**: Print-ready (minimum 2400x1800px for square)

---

## Troubleshooting

### Problem: Barriers not equally weighted

**Solution**:
- Emphasize "equal visual weight" in prompt
- Specify "pentagon with five equal segments" or "five equal horizontal bands"
- Regenerate with stronger geometric structure requirement

### Problem: Too generic (business barriers, not festival-specific)

**Solution**:
- Emphasize festival context in prompt
- Request festival-specific icons and metaphors
- Regenerate with "educational infographic for festival industry professionals"

### Problem: Color palette doesn't match EventAI style

**Solution**:
- Include exact hex codes in prompt (#FF6B6B, #F6AD55, #ED8936, #4299E1, #6B46C1)
- Regenerate with emphasis on EventAI brand colors
- Verify prompt includes all 5 specific colors

### Problem: Statistics incorrect or missing

**Solution**:
- Check source document uploaded correctly
- Verify NotebookLM processed all barrier details
- Regenerate with explicit statistics in prompt

### Problem: Layout unclear or cluttered

**Solution**:
- Try "Comprehensive" detail level for more structure
- Specify exact layout: "Pentagon with 5 equal wedges" or "5 horizontal bands"
- Emphasize "generous white space, minimal decoration"

---

## Next Steps After Success

🎉 **Congratulations!** VIS-1.3 complete!

### Update Visual Content Plan

Mark VIS-1.3 as complete in [VISUAL-CONTENT-PLAN.md](../../VISUAL-CONTENT-PLAN.md):
- Change status from 📋 to ✅
- Note winning variant number
- Record generation date

### Reference in Draft

Add to [transformation.draft.md](../drafts/transformation.draft.md) after "The Barriers: Why Transformation Is Not Inevitable" section:

```markdown
![Five Barriers to AI Transformation at Festivals: Economic Constraints ($566K investment, 80% no ROI), Data Quality (cold-start problem), Regulatory Uncertainty (€35M fines), Technical Complexity (10+ vendor integrations), and Ethical Tensions (serendipity vs. optimization). All five must be addressed for successful AI deployment.](../visuals/barriers/transformation-infographic-barriers.webp)
```

### Continue with Remaining Visuals

**Transformation topic** has 4 total infographics planned:
- ✅ VIS-1.1: AI Adoption Timeline (complete!)
- ✅ VIS-1.2: Before/After Comparison (complete!)
- 🎯 VIS-1.3: Barriers (in progress - you are here!)
- 📋 VIS-1.4: Confidence Matrix for 2030-2035 Predictions

After VIS-1.3, only VIS-1.4 remains to complete the transformation visuals package!

---

## Related Documentation

- **NotebookLM Workflow**: [../../../lemmy/workflows/notebooklm-workflows.md](../../../lemmy/workflows/notebooklm-workflows.md)
- **Infographic Prompt Template**: [../../../lemmy/prompts/notebooklm/infographic.prompt.md](../../../lemmy/prompts/notebooklm/infographic.prompt.md)
- **EventAI Style Guide**: [../../../lemmy/style-guide/eventai-visual-identity.md](../../../lemmy/style-guide/eventai-visual-identity.md)
- **Visual Content Plan**: [../../VISUAL-CONTENT-PLAN.md](../../VISUAL-CONTENT-PLAN.md)
- **Evaluation Command**: [/.claude/commands/ig-evaluate.md](/.claude/commands/ig-evaluate.md)

---

*VIS-1.3 Generation Package*
*Created: December 28, 2025*
*Part of: Lemmy Multi-AI Content Generation System*
*Ready to generate - follow steps above!*
