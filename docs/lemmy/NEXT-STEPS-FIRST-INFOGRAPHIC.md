# Next Steps: Generate Your First Infographic

**Status**: Ready to Execute
**Date**: December 28, 2025
**Task**: Generate VIS-1.1 (AI Adoption Timeline 2025-2035)
**Method**: Manual NotebookLM workflow (recommended)

---

## TL;DR - What You Need to Do

1. **Open NotebookLM**: Go to [https://notebooklm.google.com/](https://notebooklm.google.com/)
2. **Follow the instructions**: Use [VIS-1.1-GENERATE-INSTRUCTIONS.md](../writing/1-transformation/visuals/VIS-1.1-GENERATE-INSTRUCTIONS.md)
3. **Estimated time**: ~17 minutes
4. **Deliverable**: `transformation-infographic-adoption-timeline.png`

**That's it!** Everything is already prepared for you.

---

## Why Manual Workflow?

Based on automation research (see [notebooklm-automation-gap-analysis.md](./research/notebooklm-automation-gap-analysis.md)):

### What We Found

✅ **NotebookLM Enterprise API EXISTS** but:
- Only supports audio overview generation
- ❌ No infographic generation endpoint
- ❌ No slide deck generation endpoint
- ❌ No video overview generation endpoint

✅ **Playwright automation IS POSSIBLE** but:
- ❌ Google authentication is a major blocker
- Requires 8-16 hours development time
- Saves ~2 hours for 20 infographics
- **Negative ROI** for one-time use

✅ **Manual workflow IS EFFICIENT**:
- ~17 minutes per infographic (well-documented)
- ~5-6 hours for all 20 infographics
- Quality review built-in (essential anyway)
- Zero setup/maintenance

### Decision

**Use manual workflow** → It's faster and higher quality for your use case

---

## Your Prepared Materials

Everything you need is ready:

### 1. Source Document
**File**: [../writing/1-transformation/visuals/VIS-1.1-source.md](../writing/1-transformation/visuals/VIS-1.1-source.md)

**Contains**:
- All data points (45%, 67.5%, 87.5%, 95% adoption rates)
- Three phases with key developments
- Timeline milestones (2025, 2028, 2032, 2035)
- Visual guidance and festival context

**Status**: ✅ Ready to upload

### 2. Generation Instructions
**File**: [../writing/1-transformation/visuals/VIS-1.1-GENERATE-INSTRUCTIONS.md](../writing/1-transformation/visuals/VIS-1.1-GENERATE-INSTRUCTIONS.md)

**Contains**:
- Step-by-step workflow (5 steps)
- Complete NotebookLM customization prompt (copy/paste ready)
- Quality checklist
- Troubleshooting guide

**Status**: ✅ Ready to follow

### 3. EventAI Style Guide
**Customization prompt includes**:
- Deep purple (#6B46C1) for major elements
- Electric coral (#FF6B6B) for emphasis (95% endpoint)
- Sky blue (#4299E1) for supporting data
- Inter typography (headings) + Source Sans Pro (body)
- Festival context: stage icons, wristbands, crowd silhouettes
- Professional + whimsical balance

**Status**: ✅ Embedded in instructions

---

## Step-by-Step Checklist

### Pre-Flight Check
- [ ] Google account logged in
- [ ] Internet connection stable
- [ ] 20 minutes available (17 min estimated + buffer)

### Execution (follow VIS-1.1-GENERATE-INSTRUCTIONS.md)

#### Step 1: Upload Source (2 min)
- [ ] Go to [https://notebooklm.google.com/](https://notebooklm.google.com/)
- [ ] Click "New notebook"
- [ ] Name: `EventAI - Transformation Timeline Test`
- [ ] Upload: `docs/writing/1-transformation/visuals/VIS-1.1-source.md`
- [ ] Wait for processing (~10-30 seconds)

#### Step 2: Generate Infographic (10 min)
- [ ] Click "Infographic" button
- [ ] Select **Detail Level**: Detailed
- [ ] Select **Orientation**: Landscape
- [ ] Paste customization prompt (from instructions file, lines 38-129)
- [ ] Click "Generate Infographic"
- [ ] Wait 1-2 minutes

#### Step 3: Review Quality (3 min)
Check against quality checklist (in instructions):
- [ ] Data accuracy: All percentages correct
- [ ] EventAI style: Colors and typography match
- [ ] Festival context: Stage icons visible, not generic imagery
- [ ] Accessibility: Text legible, high contrast

If unsatisfactory:
- [ ] Regenerate (may get different variation)
- [ ] Try 2-3 variations, select best

#### Step 4: Download & Save (2 min)
- [ ] Click download icon
- [ ] Save as: `transformation-infographic-adoption-timeline.png`
- [ ] Move to: `docs/writing/1-transformation/visuals/`
- [ ] Verify resolution (high-res PNG, 2-5 MB typical)

#### Step 5: Documentation (1 min)
- [ ] Update [VISUAL-CONTENT-PLAN.md](../writing/VISUAL-CONTENT-PLAN.md)
- [ ] Change VIS-1.1 status from 📋 to ✅
- [ ] Note generation date

### Post-Completion
- [ ] 🎉 **You have your first infographic!**
- [ ] Optional: Reference in draft with `![...](../visuals/transformation-infographic-adoption-timeline.png)`

---

## What Comes Next

### Immediate Next Infographic
After completing VIS-1.1, you can continue with:

**VIS-1.2**: Before AI vs. After AI Festival Experience
- Source: Need to create (extract from transformation.draft.md)
- Type: Comparison infographic (Portrait orientation)
- Time: ~17 minutes

**VIS-1.3**: Barriers to AI Transformation
- Source: Need to create (extract barriers section)
- Type: Pentagon/radial diagram
- Consider: Use Nano Banana instead of NotebookLM for this diagram type

**VIS-1.4**: Confidence Matrix for 2030-2035 Predictions
- Source: Need to create (extract predictions)
- Type: Matrix/grid (Square orientation)
- Time: ~17 minutes

### Scale to Full Visual Content Plan

**20 total infographics** planned across 5 topics (see [VISUAL-CONTENT-PLAN.md](../writing/VISUAL-CONTENT-PLAN.md))

**Priority order**:
1. **High Priority** (4 core concepts):
   - ✅ VIS-1.1: AI Adoption Timeline (you're doing this first!)
   - VIS-2.1: Functional vs. Critical Literacy
   - VIS-4.1: EU AI Act Risk Classification
   - VIS-5.1: Traditional vs. AI-Powered Analytics

2. **Medium Priority** (8 supporting evidence):
   - VIS-1.2, VIS-3.3, VIS-4.2, VIS-5.2, etc.

3. **Lower Priority** (8 supplementary):
   - Remaining visuals

**Estimated total time**: 5-6 hours for all 20 infographics (in one session or spread across days)

---

## Quick Reference

### File Locations
```
docs/
├── writing/
│   ├── 1-transformation/
│   │   └── visuals/
│   │       ├── VIS-1.1-source.md ← Upload this to NotebookLM
│   │       ├── VIS-1.1-GENERATE-INSTRUCTIONS.md ← Follow this
│   │       └── transformation-infographic-adoption-timeline.png ← Save here
│   └── VISUAL-CONTENT-PLAN.md ← Update status here
└── lemmy/
    ├── research/
    │   └── notebooklm-automation-gap-analysis.md ← Why manual workflow
    └── workflows/
        └── notebooklm-workflows.md ← General workflow reference
```

### Key Links
- **NotebookLM**: [https://notebooklm.google.com/](https://notebooklm.google.com/)
- **Instructions**: [VIS-1.1-GENERATE-INSTRUCTIONS.md](../writing/1-transformation/visuals/VIS-1.1-GENERATE-INSTRUCTIONS.md)
- **Source**: [VIS-1.1-source.md](../writing/1-transformation/visuals/VIS-1.1-source.md)
- **Visual Plan**: [VISUAL-CONTENT-PLAN.md](../writing/VISUAL-CONTENT-PLAN.md)

### Customization Prompt Location
Lines 38-129 in [VIS-1.1-GENERATE-INSTRUCTIONS.md](../writing/1-transformation/visuals/VIS-1.1-GENERATE-INSTRUCTIONS.md)

**Starts with**:
```
Create a comprehensive timeline infographic showing AI adoption in the festival industry from 2025 to 2035.

VISUAL STRUCTURE:
- Horizontal timeline spanning 2025 to 2035
...
```

**Ends with**:
```
...
AVOID:
- Generic business imagery (suits, offices, corporate charts)
- Clichéd AI imagery (robots, circuit brains)
- Overly complex 3D effects
- Clutter or unnecessary decorative elements
```

---

## Troubleshooting

### "NotebookLM is slow or unresponsive"
- Try different browser (Chrome recommended)
- Check internet connection
- Clear browser cache
- Try incognito/private window

### "Source file won't upload"
- Verify file is .md format (plain text markdown)
- Check file size (should be small, <100KB)
- Try copying content and pasting directly into NotebookLM text source instead

### "Infographic doesn't match EventAI style"
- Ensure entire customization prompt was copied (lines 38-129, no truncation)
- Regenerate (NotebookLM may give different results)
- Try emphasizing "exact hex codes" in prompt
- Generate 2-3 variations and select best

### "Data points are incorrect"
- Verify source document has correct percentages
- Check NotebookLM processed source correctly (view in sidebar)
- Regenerate with more explicit data listing in prompt

### "Text not legible"
- Request larger font sizes in customization prompt
- Specify "minimum 14pt body text, 24pt emphasis"
- Try "Comprehensive" detail level instead of "Detailed"
- Download and zoom to verify quality

### "Still stuck?"
- Reference full [notebooklm-workflows.md](./workflows/notebooklm-workflows.md)
- Check troubleshooting section in VIS-1.1-GENERATE-INSTRUCTIONS.md (lines 238-267)
- Start with simpler infographic (try "Concise" detail level first)

---

## Success Criteria

You'll know you're done when you have:

✅ **File**: `transformation-infographic-adoption-timeline.png`
- Located in: `docs/writing/1-transformation/visuals/`
- File size: 2-5 MB (high-resolution PNG)
- Resolution: Minimum 2400x1800px (print-ready)

✅ **Content**:
- Horizontal timeline (landscape orientation)
- Two ascending lines (major vs. small festivals)
- Three phase sections (2025-2028, 2028-2032, 2032-2035)
- Key milestones labeled (2025, 2028, 2032, 2035)
- EventAI colors (purple, coral, blue on white)
- Festival context (stage icons, wristbands)
- 95% endpoint emphasized in electric coral

✅ **Quality**:
- Data matches source (45%, 67.5%, 87.5%, 95% for major festivals)
- Text is legible at intended display size
- Professional yet energetic presentation
- No generic business imagery

✅ **Documentation**:
- VISUAL-CONTENT-PLAN.md status updated (VIS-1.1: ✅)
- Generation date noted
- Any variations or issues documented

---

## Time Estimate

**Conservative estimate**: 20 minutes (includes buffer)
**Optimistic estimate**: 15 minutes (if everything goes smoothly)
**Documented average**: 17 minutes

**Breakdown**:
- 2 min: Navigate to NotebookLM, create notebook, upload source
- 10 min: Configure, paste prompt, generate, wait
- 3 min: Review quality, potentially regenerate
- 2 min: Download, rename, move to correct folder
- 1 min: Update documentation

---

## Final Checklist

Before you start:
- [ ] Read this entire document
- [ ] Open [VIS-1.1-GENERATE-INSTRUCTIONS.md](../writing/1-transformation/visuals/VIS-1.1-GENERATE-INSTRUCTIONS.md) in separate window
- [ ] Locate [VIS-1.1-source.md](../writing/1-transformation/visuals/VIS-1.1-source.md) file path
- [ ] Google account ready
- [ ] 20 minutes available

**Ready?** → Open [https://notebooklm.google.com/](https://notebooklm.google.com/) and follow VIS-1.1-GENERATE-INSTRUCTIONS.md

---

## What If You Want Automation Anyway?

If you still want to pursue automation despite the negative ROI for 20 infographics:

### Option 1: NotebookLM Enterprise API (for audio only)
- Set up Google Cloud project
- Enable Gemini API
- Use for audio overviews (proven to work)
- Still manual for infographics (not supported)

### Option 2: Playwright Automation (high effort)
- Solve Google authentication (8-16 hours development)
- Build infographic generation script (4-8 hours)
- Test and debug (4-8 hours)
- **Total**: 16-32 hours vs. 5-6 hours manual

### Option 3: Paid Infographic APIs
- Venngage API (enterprise tier, $500+/month)
- Canva API (limited access, custom pricing)
- Piktochart API (custom pricing)
- Develop custom templates (~16-24 hours)

### Option 4: Hybrid Approach (recommended if automating)
- NotebookLM manual for infographics (fast, proven)
- Enterprise API for audio overviews (automated)
- Nano Banana API for custom diagrams (automated)
- Claude Code for prompt preparation (automated)

**See**: [notebooklm-automation-gap-analysis.md](./research/notebooklm-automation-gap-analysis.md) for full analysis

---

## Questions?

**About the process**: See [notebooklm-workflows.md](./workflows/notebooklm-workflows.md)
**About automation**: See [notebooklm-automation-gap-analysis.md](./research/notebooklm-automation-gap-analysis.md)
**About the visual plan**: See [VISUAL-CONTENT-PLAN.md](../writing/VISUAL-CONTENT-PLAN.md)
**About infographic design**: See [infographics-best-practices.md](./research/infographics-best-practices.md)

---

**🚀 You're ready! Go generate your first infographic!**

*Next Steps Document*
*Created: December 28, 2025*
*Status: Ready to Execute*
*Estimated Completion: 20 minutes*
