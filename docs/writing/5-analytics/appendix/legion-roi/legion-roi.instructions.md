# VIS-5.3 Generation Instructions

## Legion WFM ROI Breakdown: Financial/ROI Visualization

**Visual ID**: VIS-5.3
**Type**: Financial Visualization (Cost-Benefit Analysis)
**Platform**: NotebookLM
**Status**: Ready to generate
**Estimated Time**: ~15 minutes

---

## Quick Reference

**Input**: `legion-roi.content.md` (prepared source document)
**Output**: `analytics-infographic-legion-roi.png`
**Platform**: NotebookLM (https://notebooklm.google.com)

---

## Step-by-Step Generation Workflow

### STEP 1: Create New NotebookLM Notebook

1. Navigate to **https://notebooklm.google.com**
2. Click **"+ New notebook"**
3. Name it: `EventAI VIS-5.3 - Legion WFM ROI Analysis`

---

### STEP 2: Upload Source Document

1. Click **"+ Sources"** button
2. Select **"Upload"** → **"Text files"**
3. Navigate to: `/docs/writing/5-analytics/visuals/legion-roi/legion-roi.content.md`
4. Click **"Upload"**
5. Wait for processing
6. Verify source appears in Sources panel

---

### STEP 3: Apply EventAI Visual Style

In the NotebookLM chat interface, paste this **exact customization prompt**:

```
Create a financial cost-benefit visualization for Legion WFM ROI analysis using a three-column layout: Investment (left) | Benefits (center) | ROI & Payback (right). Include a scale caveat section at bottom showing that this is only viable at enterprise scale.

LAYOUT:
- Three columns with clear visual separation
- Investment column (left): Stacked bar showing $566K total investment breakdown
- Benefits column (center): Stacked bar showing $7.44M total benefits breakdown
- ROI column (right): Net benefit, ROI multiplier, payback period, year-by-year cumulative
- Scale caveat section (bottom): Payback timeline by company size showing viability

INVESTMENT BREAKDOWN (Left Column):
Show stacked bar totaling $566,000 over 3 years:
1. Software licensing: $280,000 (slate gray color)
2. Implementation: $150,000 (darker slate)
3. Training & change management: $86,000 (mid-slate)
4. Maintenance & support: $50,000 (light slate)
Label clearly: "$566,000 Total Investment"

BENEFITS BREAKDOWN (Center Column):
Show stacked bar totaling $7.44M over 3 years:
1. Labor optimization: $1,400,000 (electric coral)
2. Reduced overtime: $720,000 (lighter coral shade)
3. Productivity improvement: $1,100,000 (sky blue)
4. Turnover reduction: $340,000 (lighter sky blue)
Label: "$7.44M Total Benefits (Forrester Study)"
Note: Include reference to conservative estimate of $3.56M

ROI & PAYBACK COLUMN (Right Column):
Display prominently:
- Large upward green arrow showing net benefit: $6.87M
- Large ROI number: "13x return"
- Payback period: "8-9 months"
- Year-by-year cumulative benefits:
  Year 1: +$1.75M
  Year 2: +$2.40M
  Year 3: +$2.68M

SCALE CAVEAT SECTION (Bottom, Separate Box):
Create a distinct section with amber/warning tone showing:
"ONLY viable at enterprise scale (1M+ annual transactions, $5M+ labor spend)"

Show payback timeline by company size as horizontal bars:
- Micro company (1 event/year, $500K labor): 10+ years [RED - NOT VIABLE]
- Small company (10 events/year, $1M labor): 9-12 months [YELLOW - BORDERLINE]
- Mid-market (50 events/year, $3M labor): 5-8 months [GREEN - VIABLE]
- Enterprise (200+ events/year, $7M+ labor): 2-3 months [BRIGHT GREEN - HIGHLY VIABLE]

STYLE REQUIREMENTS:
- Colors: Slate grays (#2D3748, #4A5568, #718096) for investment, electric coral (#FF6B6B) for primary benefits, sky blue (#4299E1) for secondary benefits, green (#48BB78) for net benefit, deep purple (#6B46C1) for ROI highlight, amber (#ED8936) for scale caveat
- Typography: Inter for headings (bold, 24-36pt), Source Sans Pro for labels (12-14pt), Inter for statistics (48-72pt for main ROI numbers)
- Design: Semi-flat style, stacked bars for clear breakdown, rounded corners (8-12px), 2-3px outlines
- Financial visualization mood: Professional, clear, honest about scale limitations

KEY STATISTICS TO HIGHLIGHT:
- Investment: $566,000 (3-year total)
- Benefits: $7,440,000 (Forrester) or $3,560,000 (conservative)
- ROI: 13x return on investment (1,215%)
- Payback period: 8-9 months
- Annual benefit: $2,480,000 average
- Investment breakdown: $280K software + $150K implementation + $86K training + $50K maintenance
- Benefits breakdown: $1.4M labor optimization + $720K overtime + $1.1M productivity + $340K turnover

CRITICAL CAVEAT:
Emphasize that Legion WFM is ONLY viable at enterprise scale:
- Requires 1M+ annual transactions (small companies don't have data for ML)
- Requires $5M+ annual labor spend (to justify $566K investment)
- Small companies see payback >10 years (not viable)
- Micro companies see -$516K loss even at 3 years (completely not viable)

OVERALL MOOD: Professional financial visualization, educational about ROI mechanics and scale economics. Honest disclosure that this is enterprise-only solution, not applicable to small/mid festivals.

Generate this as a high-resolution infographic suitable for academic curriculum use.
```

**Press Enter** and wait for NotebookLM to acknowledge.

---

### STEP 4: Generate the Infographic

1. NotebookLM will respond to your prompt
2. Look for **"Generate visual"** or **"Create infographic"** option
3. If it doesn't appear, type: `Generate this as an infographic`
4. Select generation parameters:
   - **Detail level**: High
   - **Orientation**: Landscape (for three-column layout)
   - **Size**: Largest available

**Wait time**: ~45-120 seconds

---

### STEP 5: Review Generated Visual

#### ✅ CONTENT ACCURACY CHECKLIST

- [ ] **Investment column** shows four cost categories totaling $566K
- [ ] **Benefits column** shows four benefit categories totaling $7.44M
- [ ] **Investment breakdown correct**: $280K software, $150K implementation, $86K training, $50K maintenance
- [ ] **Benefits breakdown correct**: $1.4M labor, $720K overtime, $1.1M productivity, $340K turnover
- [ ] **ROI displayed correctly**: "13x return" or "1,215%"
- [ ] **Payback period shown**: "8-9 months"
- [ ] **Year-by-year cumulative** visible: Y1 $1.75M, Y2 $2.4M, Y3 $2.68M
- [ ] **Scale caveat section present**: "ONLY viable at enterprise scale"
- [ ] **Scale viability chart** shows payback by company size (micro RED, small YELLOW, mid GREEN, enterprise BRIGHT GREEN)
- [ ] **No fabricated statistics** beyond source document

#### ✅ STYLE COMPLIANCE CHECKLIST

- [ ] **Investment bars** use slate gray colors (not bright colors)
- [ ] **Benefits bars** use electric coral and sky blue
- [ ] **Net benefit** highlighted in green
- [ ] **ROI** highlighted in deep purple
- [ ] **Scale caveat** has amber background or color
- [ ] **Typography** clean and readable (Inter/Source Sans Pro)
- [ ] **Stacked bar charts** clearly show breakdown
- [ ] **Financial visualization** professional and clear

#### ✅ LAYOUT QUALITY CHECKLIST

- [ ] **Three columns clearly defined** (Investment, Benefits, ROI)
- [ ] **Stacked bars easy to read** with legend
- [ ] **Scale caveat section visually distinct** at bottom
- [ ] **ROI metrics prominent** (large numbers visible at a glance)
- [ ] **Year-by-year breakdown** easy to understand
- [ ] **Payback timeline by company size** clear (with color coding)
- [ ] **Text legible** at full resolution
- [ ] **Balanced composition** (not overcrowded)

---

### STEP 6: Regenerate if Needed

**If visual is close but has minor issues:**
- "Make the $566K investment bar and $7.44M benefits bar larger for comparison"
- "Emphasize the 13x ROI number more prominently"
- "Make scale caveat section clearer with more distinct amber background"
- "Increase year-by-year cumulative numbers font size"

**If visual misses major requirements:**
- Return to STEP 3, revise the prompt
- Example: "The scale caveat showing 'only viable at enterprise scale' is missing"
- Example: "The cost breakdown ($280K software, $150K implementation, etc.) is not visible"
- Example: "The payback timeline by company size is missing or incorrect"

**Typical iteration count**: 1-3 generations

---

### STEP 7: Download and Save

1. Click **"Download"** button
2. Rename to: `analytics-infographic-legion-roi.png`
3. Move to: `/docs/writing/5-analytics/visuals/legion-roi/`

**File location**:
```
/docs/writing/5-analytics/visuals/legion-roi/analytics-infographic-legion-roi.png
```

---

### STEP 8: Optimize for Web (Optional)

```bash
convert analytics-infographic-legion-roi.png \
  -quality 85 \
  analytics-infographic-legion-roi.webp
```

**Target**: WebP under 500KB

---

### STEP 9: Document Results

Create: `VIS-5.3-ANALYSIS.md`

```markdown
# VIS-5.3 Generation Analysis

**Visual ID**: VIS-5.3 - Legion WFM ROI Breakdown
**Generated**: [Date]
**Platform**: NotebookLM
**Iterations**: [Number]
**Final file**: analytics-infographic-legion-roi.png

## What Worked Well

- [e.g., "Clear three-column layout showing investment vs benefits"]
- [e.g., "Scale caveat effectively highlighted"]
- [e.g., "Year-by-year cumulative benefits clearly shown"]

## What Needed Adjustment

- [Note any prompt modifications]
- [e.g., "Had to emphasize the enterprise-only nature more explicitly"]
- [e.g., "Needed clearer color distinction between investment costs and benefits"]

## Lessons for Future Visuals

- [Insights for VIS-5.4]

## Content Accuracy Notes

- [Verification of investment and benefits numbers against source]
- [Verification of 13x ROI calculation]
- [Verification of scale viability assertions]

---

*Generation completed: [Date and time]*
```

---

## Troubleshooting

### Issue: NotebookLM doesn't generate a visual

**Solution**: Type `Generate this as an infographic`

### Issue: Three columns not clearly defined

**Solution**: Re-prompt with: "Make three columns very distinct with clear vertical dividers. Label: Investment | Benefits | ROI & Payback"

### Issue: Investment/benefits breakdown missing

**Solution**: Re-prompt with: "Show exact cost breakdown: $280K software, $150K implementation, $86K training, $50K maintenance. Show benefit breakdown: $1.4M labor, $720K overtime, $1.1M productivity, $340K turnover"

### Issue: ROI not prominent enough

**Solution**: Re-prompt with: "Make the 13x ROI number very large and prominent in the right column. Also prominently display 8-9 month payback period"

### Issue: Scale caveat missing or unclear

**Solution**: Re-prompt with: "Add a bottom section with amber background showing that Legion is ONLY viable at enterprise scale (1M+ transactions, $5M+ labor spend). Show payback timeline by company size: micro RED 10+ years, small YELLOW 9-12 months, mid GREEN 5-8 months, enterprise BRIGHT GREEN 2-3 months"

### Issue: Statistics fabricated or incorrect

**Solution**: Re-prompt with: "Use ONLY these figures: Investment $566K, Benefits $7.44M (Forrester) or $3.56M (conservative), ROI 13x, Payback 8-9 months, Year 1 +$1.75M, Year 2 +$2.4M, Year 3 +$2.68M"

---

## Quality Standards

**Minimum requirements for VIS-5.3 approval:**

1. ✅ Three columns clearly defined (Investment, Benefits, ROI)
2. ✅ Investment breakdown visible ($280K + $150K + $86K + $50K = $566K)
3. ✅ Benefits breakdown visible ($1.4M + $720K + $1.1M + $340K = $7.44M)
4. ✅ ROI prominently displayed (13x or 1,215%)
5. ✅ Payback period shown (8-9 months)
6. ✅ Year-by-year cumulative benefits shown (Y1 $1.75M, Y2 $2.4M, Y3 $2.68M)
7. ✅ Scale caveat section visible ("ONLY viable at enterprise scale")
8. ✅ Payback timeline by company size shown (micro/small/mid/enterprise)
9. ✅ Colors used correctly (slate investments, coral/blue benefits, green ROI, amber caveat)
10. ✅ No fabricated statistics

**Do not proceed until ALL criteria are met.**

---

## Time Estimate

| Step | Time |
|------|------|
| 1. Create notebook | 1 min |
| 2. Upload source | 1 min |
| 3. Apply style prompt | 2 min |
| 4. Generate | 2-3 min |
| 5. Review | 3-5 min |
| 6. Iterate | 5-10 min |
| 7. Download & save | 1 min |
| 8. Optimize | 2 min |
| 9. Document | 3-5 min |
| **TOTAL** | **15-25 min** |

---

*VIS-5.3 Generation Instructions*
*Created: December 29, 2025*
*Part of: EventAI Visual Content Strategy (Section 5: Analytics)*
