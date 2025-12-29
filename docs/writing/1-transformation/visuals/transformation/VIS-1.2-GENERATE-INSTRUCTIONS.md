# VIS-1.2 Generation Instructions

## Before/After Comparison Infographic

**Visual ID**: VIS-1.2
**Type**: Comparative Infographic (Side-by-side)
**Platform**: NotebookLM
**Status**: Ready to generate
**Estimated Time**: ~15 minutes

---

## Quick Reference

**Input**: `VIS-1.2-source.md` (prepared source document)
**Output**: `transformation-infographic-before-after.png`
**Platform**: NotebookLM (https://notebooklm.google.com)

---

## Step-by-Step Generation Workflow

### STEP 1: Create New NotebookLM Notebook

1. Navigate to **https://notebooklm.google.com**
2. Click **"+ New notebook"**
3. Name it: `EventAI VIS-1.2 - Before After Comparison`

**Why this matters**: Separate notebooks prevent cross-contamination between different visuals.

---

### STEP 2: Upload Source Document

1. Click **"+ Sources"** button
2. Select **"Upload"** → **"Text files"**
3. Navigate to: `/docs/writing/1-transformation/visuals/VIS-1.2-source.md`
4. Click **"Upload"**
5. Wait for processing (typically 10-15 seconds)
6. Verify source appears in the Sources panel

**Verification**: You should see "VIS-1.2-source.md" listed with a document icon.

---

### STEP 3: Apply EventAI Visual Style

In the NotebookLM chat interface, paste this **exact customization prompt**:

```
Create a side-by-side comparison infographic showing "Before AI" vs "After AI" festival experiences across three dimensions: Discovery & Ticketing, On-Site Experience, and Post-Festival. Use a horizontal layout with three bands stacked vertically.

LAYOUT:
- Three horizontal comparison bands (Discovery, On-Site, Post-Festival)
- Each band split vertically: Before AI (left) | After AI (right)
- Clear visual divider between Before/After (subtle vertical line or color shift)
- Statistics and callouts positioned prominently in each band

STYLE REQUIREMENTS:
- Colors: Deep purple (#6B46C1) for AI elements, electric coral (#FF6B6B) for statistics, sky blue (#4299E1) for data points, midnight slate (#2D3748) for text
- Before AI side: Muted grayscale tones to show traditional approach
- After AI side: Full EventAI brand colors to show enhanced experience
- Typography: Inter for headings (bold, 24-36pt), Source Sans Pro for body (14-16pt), Inter for statistics (48-72pt)
- Design: Semi-flat style, rounded corners (8-12px), 2-3px outlines, minimal decoration
- Context: Festival-specific imagery (stages, crowds, wristbands, mobile apps) NOT generic tech imagery

CONTENT FOCUS:
- Band 1 (Discovery): Manual browsing vs AI recommendations | Stat: "40-41% of tickets from AI"
- Band 2 (On-Site): Paper maps vs real-time apps | Stat: "20% engagement with contextual notifications"
- Band 3 (Post-Festival): Manual photos vs AI-generated recaps | Privacy note: "Requires explicit opt-in"

KEY STATISTICS TO HIGHLIGHT:
- 40-41% ticket sales via AI recommendations
- 20% engagement rate (Bonnaroo notifications)
- 90% emergency alert reach (Lollapaloola)
- 44-56% users decline notifications when asked explicitly

PRIVACY ELEMENTS:
- Clearly mark privacy-sensitive features with lock icons or amber warning tones
- Include "Requires opt-in" callouts for post-festival AI features
- Show user control as a key differentiator

OVERALL MOOD: Professional yet energetic, educational rather than promotional, showing both benefits AND privacy considerations of AI transformation.

Generate this as a high-resolution infographic suitable for academic curriculum use.
```

**Press Enter** and wait for NotebookLM to acknowledge the style requirements.

---

### STEP 4: Generate the Infographic

1. NotebookLM will respond to your prompt (usually with text)
2. Look for **"Generate visual"** or **"Create infographic"** option
3. If the option appears, click it
4. If it doesn't appear automatically, type: `Generate this as an infographic`
5. Select generation parameters:
   - **Detail level**: High (for curriculum use)
   - **Orientation**: Landscape (for side-by-side comparison)
   - **Size**: Largest available (typically 1792x1024 or higher)

**Wait time**: ~45-120 seconds for generation

---

### STEP 5: Review Generated Visual

Check the generated infographic against these quality criteria:

#### ✅ CONTENT ACCURACY CHECKLIST

- [ ] **Discovery section** shows Before (manual browsing, static pricing) vs After (AI recommendations, dynamic pricing)
- [ ] **On-Site section** shows Before (paper maps, uniform experience) vs After (real-time apps, personalization)
- [ ] **Post-Festival section** shows Before (manual photos) vs After (AI-generated recaps)
- [ ] **40-41% statistic** appears for AI ticket sales
- [ ] **20% engagement rate** appears for contextual notifications
- [ ] **Privacy callouts** included for opt-in requirements
- [ ] **No fabricated statistics** beyond those in source document

#### ✅ STYLE COMPLIANCE CHECKLIST

- [ ] **EventAI colors** used (deep purple, electric coral, sky blue)
- [ ] **Before AI side** uses muted/grayscale tones
- [ ] **After AI side** uses full brand colors
- [ ] **Festival context** visible (stages, crowds, wristbands) not generic tech stock imagery
- [ ] **Typography** is clean and readable (Inter/Source Sans Pro or close equivalents)
- [ ] **Semi-flat design** with subtle depth, not overly 3D or flat
- [ ] **Rounded corners** and clean outlines present

#### ✅ LAYOUT QUALITY CHECKLIST

- [ ] **Three bands clearly defined** (Discovery, On-Site, Post-Festival)
- [ ] **Left/Right split obvious** with clear visual divider
- [ ] **Statistics prominent** and easy to read at a glance
- [ ] **Text legible** at full size (will be readable when printed)
- [ ] **Balanced composition** (not overcrowded or too sparse)
- [ ] **Privacy elements** visually distinct (lock icons, warning colors, opt-in notes)

---

### STEP 6: Regenerate if Needed

**If the visual is close but has minor issues:**
- Click **"Regenerate"** or modify the prompt slightly
- Example: "Make the statistics larger and use electric coral color"
- Example: "Add more festival context imagery (stages, crowds)"
- Example: "Increase contrast between Before and After sides"

**If the visual misses major requirements:**
- Return to STEP 3, revise the prompt with more explicit instructions
- Focus on the specific element that's missing
- Example: "Privacy callouts are missing—add lock icons and 'Requires opt-in' text in amber color"

**Typical iteration count**: 1-3 generations to achieve desired result

---

### STEP 7: Download and Save

1. Click **"Download"** button on the generated infographic
2. NotebookLM will download as: `notebooklm-infographic-[timestamp].png`
3. Rename file to: `transformation-infographic-before-after.png`
4. Move to: `/docs/writing/1-transformation/visuals/`
5. Verify file size is reasonable (typically 2-10 MB for high-res PNG)

**File location**:
```
/docs/writing/1-transformation/visuals/transformation-infographic-before-after.png
```

---

### STEP 8: Optimize for Web (Optional)

If the PNG is very large (>5 MB), create a WebP version:

**Using ImageMagick (if installed):**
```bash
convert transformation-infographic-before-after.png \
  -quality 85 \
  transformation-infographic-before-after.webp
```

**Using online converter:**
- Visit: https://squoosh.app
- Upload PNG
- Select WebP format, quality 85
- Download optimized version

**Target**: WebP under 500KB for web use, retain original PNG for print/high-res

---

### STEP 9: Document Results

Create a brief analysis file: `VIS-1.2-ANALYSIS.md`

**Template:**

```markdown
# VIS-1.2 Generation Analysis

**Visual ID**: VIS-1.2 - Before/After Comparison
**Generated**: [Date]
**Platform**: NotebookLM
**Iterations**: [Number of regenerations needed]
**Final file**: transformation-infographic-before-after.png

## What Worked Well

- [List successful elements, e.g., "Clear side-by-side comparison"]
- [e.g., "Statistics prominently displayed"]
- [e.g., "Privacy callouts effectively highlighted"]

## What Needed Adjustment

- [Note any prompt modifications needed]
- [e.g., "Had to request larger statistics in iteration 2"]
- [e.g., "Privacy elements required explicit prompt addition"]

## Lessons for Future Visuals

- [Insights that would apply to VIS-1.3, VIS-1.4, etc.]
- [e.g., "NotebookLM defaults to too much decoration—explicitly request minimal style"]

## Content Accuracy Notes

- [Any statistics or facts that were initially incorrect and had to be corrected]
- [Verification against source document]

---

*Generation completed: [Date and time]*
```

---

## Troubleshooting

### Issue: NotebookLM doesn't generate a visual, only text

**Solution**: Explicitly type `Generate this as an infographic` or `Create a visual representation`

### Issue: Generated visual uses wrong colors

**Solution**: Re-prompt with: "Use these exact colors: deep purple #6B46C1, electric coral #FF6B6B, sky blue #4299E1"

### Issue: Too much generic tech imagery (laptops, cloud icons)

**Solution**: Re-prompt with: "Replace all generic tech imagery with festival context: stages, crowds, wristbands, festival apps on phones"

### Issue: Statistics are fabricated or incorrect

**Solution**: Re-prompt with: "Use ONLY these statistics from the source document: [list exact stats]"

### Issue: Before/After comparison not visually clear

**Solution**: Re-prompt with: "Make the left/right split more obvious with a vertical divider line and stronger color contrast"

### Issue: Privacy elements missing or unclear

**Solution**: Re-prompt with: "Add lock icons and amber warning colors for all privacy-sensitive features, include 'Requires opt-in' callouts"

---

## Quality Standards

**Minimum requirements for VIS-1.2 approval:**

1. ✅ All three comparison dimensions present (Discovery, On-Site, Post-Festival)
2. ✅ Before/After clearly differentiated visually
3. ✅ Key statistics accurate (40-41%, 20%, privacy opt-out rates)
4. ✅ EventAI colors used correctly
5. ✅ Festival context (not generic tech stock imagery)
6. ✅ Privacy callouts clearly marked
7. ✅ Text readable at full resolution
8. ✅ No fabricated data or statistics

**Do not proceed to use the visual until ALL criteria are met.**

---

## Time Estimate Breakdown

| Step | Estimated Time |
|------|----------------|
| 1. Create notebook | 1 min |
| 2. Upload source | 1 min |
| 3. Apply style prompt | 2 min |
| 4. Generate visual | 2-3 min |
| 5. Review quality | 3-5 min |
| 6. Iterate (if needed) | 5-10 min |
| 7. Download & save | 1 min |
| 8. Optimize (optional) | 2 min |
| 9. Document | 3-5 min |
| **TOTAL** | **15-25 min** |

---

## Related Documentation

- **Source document**: [VIS-1.2-source.md](VIS-1.2-source.md)
- **Visual plan**: [README.md](README.md)
- **Main draft**: [../drafts/transformation.draft.md](../drafts/transformation.draft.md)
- **NotebookLM workflow**: [../../../lemmy/workflows/notebooklm-workflows.md](../../../lemmy/workflows/notebooklm-workflows.md)
- **EventAI style guide**: [../../../lemmy/style-guide/eventai-visual-identity.md](../../../lemmy/style-guide/eventai-visual-identity.md)

---

*VIS-1.2 Generation Instructions*
*Created: December 28, 2025*
*Part of: EventAI Visual Content Strategy + Lemmy Multi-AI System*
