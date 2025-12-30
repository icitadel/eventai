# VIS-5.1 Generation Instructions

## Traditional vs. AI-Powered Analytics Comparison Infographic

**Visual ID**: VIS-5.1
**Type**: Comparative Infographic (Side-by-side)
**Platform**: NotebookLM
**Status**: Ready to generate
**Estimated Time**: ~15 minutes

---

## Quick Reference

**Input**: `traditional-vs-ai.content.md` (prepared source document)
**Output**: `analytics-infographic-traditional-vs-ai.png`
**Platform**: NotebookLM (https://notebooklm.google.com)

---

## Step-by-Step Generation Workflow

### STEP 1: Create New NotebookLM Notebook

1. Navigate to **https://notebooklm.google.com**
2. Click **"+ New notebook"**
3. Name it: `EventAI VIS-5.1 - Traditional vs AI Analytics`

---

### STEP 2: Upload Source Document

1. Click **"+ Sources"** button
2. Select **"Upload"** → **"Text files"**
3. Navigate to: `/docs/writing/5-analytics/visuals/traditional-vs-ai/traditional-vs-ai.content.md`
4. Click **"Upload"**
5. Wait for processing (typically 10-15 seconds)
6. Verify source appears in the Sources panel

---

### STEP 3: Apply EventAI Visual Style

In the NotebookLM chat interface, paste this **exact customization prompt**:

```
Create a side-by-side comparison infographic showing Traditional Analytics vs AI-Powered Analytics across four dimensions: Data Sources, Forecasting Timeline, Operational Adjustments, and Business Outcomes. Use a horizontal layout with four bands stacked vertically.

LAYOUT:
- Four horizontal comparison bands (Data Sources, Forecasting, Adjustments, Outcomes)
- Each band split vertically: Traditional (left) | AI-Powered (right)
- Clear visual divider between Traditional/AI (subtle vertical line or color shift)
- Statistics and ROI callouts positioned prominently in each band

STYLE REQUIREMENTS:
- Colors: Deep purple (#6B46C1) for AI elements, electric coral (#FF6B6B) for ROI stats, sky blue (#4299E1) for data points, midnight slate (#2D3748) for text
- Traditional side: Grayscale/muted orange tones to show conventional approach
- AI side: Full EventAI brand colors to show advanced approach
- Typography: Inter for headings (bold, 24-36pt), Source Sans Pro for body (14-16pt), Inter for statistics (48-72pt)
- Design: Semi-flat style, rounded corners (8-12px), 2-3px outlines, minimal decoration
- Context: Festival/operational context (beer kegs, inventory boxes, weather icons, forecasting calendars) NOT generic business stock imagery

CONTENT FOCUS:
- Band 1 (Data Sources): Historical data only vs Real-time + historical + external data | Stat: "Data lag: minutes (AI) vs 3-7 days (traditional)"
- Band 2 (Forecasting): 4-8 weeks before, static "order 10,000 beers" vs 2 weeks + continuous adjustments | Stat: "±20% error (traditional) vs ±5-8% (AI)"
- Band 3 (Adjustments): Weekly reviews, locked-in decisions vs Continuous monitoring, real-time adjustments | Stat: "Decision speed: Days vs Minutes"
- Band 4 (Outcomes): 14% excess inventory, stockouts, missed upsell vs 1.7% excess, zero stockouts, real-time recommendations | Stat: "10-15% margin improvement = $900K per festival"

KEY STATISTICS TO HIGHLIGHT:
- Forecast accuracy: ±20% error (traditional) vs ±5-8% (AI)
- Inventory: 18% reduction in overstock with AI
- Stockout rates: <2% (AI) vs 2-5% (traditional)
- Margin improvement: 10-15% documented (based on $900K per large festival)
- ROI: 6-18x annually
- Payback period: 2-6 weeks

OPERATIONAL EXAMPLES:
- Beer case study: 14% excess inventory (traditional) reduced to 1.7% (AI) = $108K savings
- Include example of real-time adjustment: Rain forecast → auto-increase tent inventory

OVERALL MOOD: Professional yet operational, showing concrete financial and ROI benefits of AI analytics transformation.

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

- [ ] **Data Sources band** shows Traditional (historical only, manual, siloed) vs AI (real-time, automated, integrated)
- [ ] **Forecasting band** shows Traditional (4-8 weeks, static) vs AI (2 weeks + continuous)
- [ ] **Adjustments band** shows Traditional (weekly reviews, locked) vs AI (continuous, real-time)
- [ ] **Outcomes band** shows Traditional (14% excess, stockouts) vs AI (1.7% excess, zero stockouts)
- [ ] **±20% vs ±5-8% forecast accuracy** appears correctly
- [ ] **Data lag statistics** included (minutes vs 3-7 days)
- [ ] **10-15% margin improvement ($900K)** prominently displayed
- [ ] **Beer case study example** visible or referenced
- [ ] **No fabricated statistics** beyond source document

#### ✅ STYLE COMPLIANCE CHECKLIST

- [ ] **EventAI colors** used (deep purple, electric coral, sky blue)
- [ ] **Traditional side** uses grayscale/muted tones
- [ ] **AI side** uses full brand colors
- [ ] **Festival/operational context** visible (beer kegs, inventory boxes, weather icons, calendars)
- [ ] **No generic business stock imagery** (avoid corporate people, generic charts)
- [ ] **Typography** is clean and readable (Inter/Source Sans Pro)
- [ ] **Semi-flat design** with subtle depth, not overly 3D or flat
- [ ] **Rounded corners** and clean outlines present
- [ ] **ROI callouts** in electric coral for emphasis

#### ✅ LAYOUT QUALITY CHECKLIST

- [ ] **Four bands clearly defined** (Data Sources, Forecasting, Adjustments, Outcomes)
- [ ] **Left/Right split obvious** with clear visual divider
- [ ] **Statistics prominent** and easy to read at a glance
- [ ] **Text legible** at full size (will be readable when printed)
- [ ] **Balanced composition** (not overcrowded or too sparse)
- [ ] **Operational examples** visually distinct (rain → tent adjustment example)

---

### STEP 6: Regenerate if Needed

**If the visual is close but has minor issues:**
- Click **"Regenerate"** or modify the prompt slightly
- Example: "Make statistics larger and use electric coral color for all ROI numbers"
- Example: "Add more festival/operational context imagery (beer kegs, inventory boxes, weather icons)"
- Example: "Increase contrast between Traditional (grayscale) and AI (color) sides"

**If the visual misses major requirements:**
- Return to STEP 3, revise the prompt with more explicit instructions
- Focus on the specific element that's missing
- Example: "The forecast accuracy statistics (±20% vs ±5-8%) are missing or unclear"
- Example: "Need operational example: Rain forecast → auto-increase tent inventory"

**Typical iteration count**: 1-3 generations to achieve desired result

---

### STEP 7: Download and Save

1. Click **"Download"** button on the generated infographic
2. NotebookLM will download as: `notebooklm-infographic-[timestamp].png`
3. Rename file to: `analytics-infographic-traditional-vs-ai.png`
4. Move to: `/docs/writing/5-analytics/visuals/traditional-vs-ai/`
5. Verify file size is reasonable (typically 2-10 MB for high-res PNG)

**File location**:
```
/docs/writing/5-analytics/visuals/traditional-vs-ai/analytics-infographic-traditional-vs-ai.png
```

---

### STEP 8: Optimize for Web (Optional)

If the PNG is very large (>5 MB), create a WebP version:

**Using ImageMagick:**
```bash
convert analytics-infographic-traditional-vs-ai.png \
  -quality 85 \
  analytics-infographic-traditional-vs-ai.webp
```

**Using online converter**: https://squoosh.app (upload PNG, select WebP, quality 85)

**Target**: WebP under 500KB for web use, retain original PNG for print/high-res

---

### STEP 9: Document Results

Create a brief analysis file: `VIS-5.1-ANALYSIS.md`

**Template:**

```markdown
# VIS-5.1 Generation Analysis

**Visual ID**: VIS-5.1 - Traditional vs AI Analytics
**Generated**: [Date]
**Platform**: NotebookLM
**Iterations**: [Number of regenerations needed]
**Final file**: analytics-infographic-traditional-vs-ai.png

## What Worked Well

- [List successful elements, e.g., "Clear side-by-side comparison"]
- [e.g., "ROI callouts prominently displayed"]
- [e.g., "Operational examples effectively illustrated"]

## What Needed Adjustment

- [Note any prompt modifications needed]
- [e.g., "Had to emphasize forecast accuracy statistics in iteration 2"]
- [e.g., "Beer case study required explicit prompt clarification"]

## Lessons for Future Visuals

- [Insights that would apply to VIS-5.2, VIS-5.3, VIS-5.4]
- [e.g., "Operational context (beer kegs, inventory) more effective than abstract concepts"]

## Content Accuracy Notes

- [Any statistics that were initially incorrect and had to be corrected]
- [Verification against source document]

---

*Generation completed: [Date and time]*
```

---

## Troubleshooting

### Issue: NotebookLM doesn't generate a visual, only text

**Solution**: Explicitly type `Generate this as an infographic` or `Create a visual representation`

### Issue: Generated visual uses wrong colors

**Solution**: Re-prompt with: "Use exact colors: deep purple #6B46C1, electric coral #FF6B6B, sky blue #4299E1, traditional side grayscale"

### Issue: Missing operational context (beer, inventory, weather icons)

**Solution**: Re-prompt with: "Replace all generic business imagery with festival context: beer kegs, inventory boxes, weather icons, forecasting calendars, not corporate stock photos"

### Issue: Statistics are fabricated or incorrect

**Solution**: Re-prompt with: "Use ONLY these statistics: ±20% forecast error (traditional), ±5-8% (AI), 14% overstock (traditional), 1.7% (AI), 10-15% margin improvement"

### Issue: Traditional/AI comparison not visually clear

**Solution**: Re-prompt with: "Make left/right split obvious with vertical divider, use grayscale for left (traditional) and full brand colors for right (AI)"

### Issue: Four bands not clearly defined

**Solution**: Re-prompt with: "Clearly separate four bands horizontally: Data Sources | Forecasting Timeline | Operational Adjustments | Business Outcomes. Each band has distinct background color or divider"

---

## Quality Standards

**Minimum requirements for VIS-5.1 approval:**

1. ✅ All four comparison dimensions present (Data Sources, Forecasting, Adjustments, Outcomes)
2. ✅ Traditional/AI clearly differentiated visually
3. ✅ Key statistics accurate (±20% vs ±5-8%, 14% vs 1.7%, 10-15% margin improvement)
4. ✅ EventAI colors used correctly
5. ✅ Operational/festival context (not generic business stock)
6. ✅ ROI callouts clearly marked in electric coral
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

*VIS-5.1 Generation Instructions*
*Created: December 29, 2025*
*Part of: EventAI Visual Content Strategy (Section 5: Analytics)*
