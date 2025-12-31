# VIS-5.4 Generation Instructions

## Predictive Analytics Use Cases Matrix: Grid/Application Framework

**Visual ID**: VIS-5.4
**Type**: Matrix/Grid Visualization (Multi-Dimensional)
**Platform**: NotebookLM
**Status**: Ready to generate
**Estimated Time**: ~20 minutes (most complex visual)

---

## Quick Reference

**Input**: `use-cases-matrix.content.md` (prepared source document)
**Output**: `analytics-infographic-use-cases-matrix.png`
**Platform**: NotebookLM (https://notebooklm.google.com)

---

## Step-by-Step Generation Workflow

### STEP 1: Create New NotebookLM Notebook

1. Navigate to **https://notebooklm.google.com**
2. Click **"+ New notebook"**
3. Name it: `EventAI VIS-5.4 - Predictive Analytics Use Cases Matrix`

---

### STEP 2: Upload Source Document

1. Click **"+ Sources"** button
2. Select **"Upload"** → **"Text files"**
3. Navigate to: `/docs/writing/5-analytics/visuals/use-cases-matrix/use-cases-matrix.content.md`
4. Click **"Upload"**
5. Wait for processing
6. Verify source appears in Sources panel

---

### STEP 3: Apply EventAI Visual Style

In the NotebookLM chat interface, paste this **exact customization prompt**:

```
Create a comprehensive matrix/grid visualization showing Predictive Analytics Applications across four functional areas. The layout should be a 4-row by 4-5 column grid where each row represents a function area (color-coded) and each column represents a use case application.

OVERALL LAYOUT:
- Four horizontal rows representing four function areas: Demand Forecasting | Resource Allocation | Risk Management | Revenue Optimization
- Four to five columns per row showing specific applications
- Each cell contains: Icon/visual, vendor name(s), key ROI metric, implementation timeline, complexity indicator
- Color-coded rows: Deep purple for Demand, Electric coral for Resource, Sky blue for Risk, Green for Revenue
- Bottom sections: Complexity legend, Scale note, Privacy callout

ROW 1: DEMAND FORECASTING (Deep Purple)
Four applications shown as cells:
1. Ticket Sales Forecasting - DICE, Qcue - "40-41% algo influence" - "4-8 weeks" - RED (HIGH)
2. Merchandise Demand - Qcue, Eventbrite - "15-20% inventory reduction" - "3-4 weeks" - YELLOW (MEDIUM)
3. Food & Beverage - Tomorrowland, Toast - "10-15% margin improvement" - "3-6 weeks" - YELLOW-RED (MEDIUM-HIGH)
4. Parking & Transportation - ParkWhiz, Uber - "5-10% revenue increase" - "3-4 weeks" - YELLOW (MEDIUM)

ROW 2: RESOURCE ALLOCATION (Electric Coral)
Four applications:
1. Staff Scheduling (Legion WFM) - Legion, Shiftboard - "13x ROI, 8-month payback" - "4-6 months" - RED (HIGH, enterprise-only)
2. Vendor Placement - Eventbrite - "10-15% vendor revenue increase" - "2-3 weeks" - YELLOW (MEDIUM)
3. Inventory Optimization - Tomorrowland, Toast - "8-12% margin improvement" - "3-4 weeks" - YELLOW (MEDIUM)
4. Equipment Maintenance - SAP, IoT - "20-30% emergency cost reduction" - "4-8 weeks" - RED (HIGH)

ROW 3: RISK MANAGEMENT (Sky Blue)
Three applications:
1. Crowd Safety & Density - Telstra Purple, Lollapalooza - "90% alert reach, prevents stampedes" - "3-6 months" - YELLOW-RED (MEDIUM-HIGH)
2. Weather Impact Forecasting - Dark Sky, OpenWeather - "2-5% revenue protection" - "1-2 weeks" - GREEN (LOW-MEDIUM)
3. Financial Risk Prediction - Custom - "3-5% recovery potential" - "2-3 weeks" - YELLOW (MEDIUM)

ROW 4: REVENUE OPTIMIZATION (Green)
Four applications:
1. Dynamic Pricing - Qcue, Tomorrowland, TickPick - "78% yield improvement ($265 avg vs $150)" - "4-8 weeks" - RED (HIGH)
2. Upsell Targeting - Qcue, DICE - "8-12% conversion lift, +3-5% revenue" - "2-3 weeks" - YELLOW (MEDIUM)
3. Sponsorship Value Optimization - Sportradar - "75-85% renewal (vs 50%), $100K-500K value" - "4-6 weeks" - YELLOW-RED (MEDIUM-HIGH)
4. VIP Package Optimization - Qcue - "15-20% performance improvement, $200K-800K value" - "3-4 weeks" - YELLOW (MEDIUM)

COMPLEXITY LEGEND (Bottom):
Show color-coded complexity indicators:
- GREEN circle: Low complexity (1-2 weeks) - weather integration only
- YELLOW circle: Medium complexity (2-4 weeks) - merchandise, vendor placement, upsell, VIP, financial risk
- RED circle: High complexity (4-8+ weeks) - tickets, staff, equipment, crowd safety, sponsorship, dynamic pricing

SCALE NOTE (Bottom):
Display prominently: "Most applications viable at all scales | EXCEPTION: Legion WFM only viable at enterprise scale ($5M+ annual labor, 1M+ transactions)"

PRIVACY CALLOUT (Bottom):
Display: "All personalization requires GDPR/CCPA explicit opt-in. Transparency increases consent from 20% (passive) to 40-50% (explicit)."

STYLE REQUIREMENTS:
- Row colors: Deep purple (#6B46C1) for Demand, Electric coral (#FF6B6B) for Resource, Sky blue (#4299E1) for Risk, Green (#48BB78) for Revenue
- Complexity indicators: Green (#48BB78) for LOW, Yellow (#ECC94B) for MEDIUM, Red (#F56565) for HIGH
- Typography: Inter for row headers (bold, 18-24pt), Inter for cell headers (bold, 12-14pt), Source Sans Pro for cell content (11-13pt)
- Cell design: Semi-flat style, rounded corners (6-8px), 2-3px outlines, icons representing each use case
- Grid layout: Clean grid with clear cell boundaries, professional scannable format
- Icons: Use relevant icons (ticket, merchandise box, staff, crowd, weather, money, etc.)
- Background: White background with subtle row color backgrounds for visual separation

KEY METRICS TO HIGHLIGHT:
- 40-41% DICE ticket sales influenced by AI
- 78% Tomorrowland yield improvement (dynamic pricing)
- 13x Legion WFM ROI (enterprise-only, 8-month payback)
- 90% Lollapalooza emergency alert reach
- 8-12% upsell conversion lift
- 75-85% sponsorship renewal rate (vs 50% without metrics)
- 15-20% VIP optimization improvement
- 18% Tomorrowland waste reduction (inventory)

OVERALL MOOD: Educational grid showcasing comprehensive breadth of AI/predictive analytics applications across event operations. Shows real vendors, documented ROI, implementation reality and complexity. Professional, comprehensive, suitable for decision-makers evaluating where to invest in analytics.

Generate this as a high-resolution infographic suitable for academic curriculum and executive decision-making use.
```

**Press Enter** and wait for NotebookLM to acknowledge.

---

### STEP 4: Generate the Infographic

1. NotebookLM will respond to your prompt
2. Look for **"Generate visual"** or **"Create infographic"** option
3. If it doesn't appear, type: `Generate this as an infographic`
4. Select generation parameters:
   - **Detail level**: High (for curriculum use)
   - **Orientation**: Landscape (for wide matrix)
   - **Size**: Largest available (to accommodate grid)

**Wait time**: ~45-120 seconds

---

### STEP 5: Review Generated Visual

#### ✅ CONTENT ACCURACY CHECKLIST

- [ ] **Four rows present**: Demand (purple), Resource (coral), Risk (blue), Revenue (green)
- [ ] **Demand row shows 4 applications**: Tickets, merchandise, food/beverage, parking
- [ ] **Resource row shows 4 applications**: Staff scheduling, vendor placement, inventory, equipment
- [ ] **Risk row shows 3 applications**: Crowd safety, weather, financial risk
- [ ] **Revenue row shows 4 applications**: Dynamic pricing, upsell, sponsorship, VIP
- [ ] **Each cell shows**: Vendor name, ROI/metric, timeline, complexity indicator
- [ ] **Key metrics correct**:
  - Ticket: 40-41% algo influence
  - Tomorrowland dynamic pricing: 78% yield
  - Legion WFM: 13x ROI, 8-mo payback
  - Lollapalooza: 90% alert reach
  - Upsell: 8-12% conversion lift
  - Sponsorship: 75-85% renewal (vs 50%)
- [ ] **Complexity legend present**: GREEN (LOW), YELLOW (MEDIUM), RED (HIGH)
- [ ] **Scale note visible**: Legion WFM enterprise-only
- [ ] **Privacy callout included**: GDPR/CCPA opt-in note
- [ ] **No fabricated statistics** beyond source document

#### ✅ STYLE COMPLIANCE CHECKLIST

- [ ] **Row colors correct**: Purple (Demand), Coral (Resource), Blue (Risk), Green (Revenue)
- [ ] **Complexity indicators visible**: RED circles on high-complexity items, YELLOW on medium, GREEN on low
- [ ] **Grid layout clean** with clear cell boundaries
- [ ] **Icons present** representing each use case (tickets, staff, crowds, etc.)
- [ ] **Typography readable** (Inter for headers, Source Sans Pro for body)
- [ ] **Semi-flat design** with subtle depth
- [ ] **Rounded corners** and clean outlines on cells
- [ ] **Color coding consistent** (green outcomes, purple demand, coral resources, blue risk)

#### ✅ LAYOUT QUALITY CHECKLIST

- [ ] **Grid structure obvious** (four rows clearly separated by color)
- [ ] **All cells populated** with information
- [ ] **Vendor names visible** in cells
- [ ] **ROI metrics easy to scan** at a glance
- [ ] **Complexity indicators prominent** (color-coded circles)
- [ ] **Timeline readable** (3-4 weeks, 4-8 weeks, etc.)
- [ ] **Bottom sections visible**: Legend, scale note, privacy callout
- [ ] **Text legible** at full resolution
- [ ] **Balanced composition** (not overcrowded)

---

### STEP 6: Regenerate if Needed

**If visual is close but has minor issues:**
- "Make the complexity indicators (RED/YELLOW/GREEN circles) more prominent"
- "Increase vendor names font size so they're more readable"
- "Add clearer visual separation between the four rows"
- "Make the scale note more prominent (Legion WFM enterprise-only)"

**If visual misses major requirements:**
- Return to STEP 3, revise the prompt
- Example: "The grid structure is not clear, cells are hard to distinguish"
- Example: "Complexity legend is missing at the bottom"
- Example: "The scale note about Legion WFM enterprise-only is missing"
- Example: "Privacy callout is missing"

**Typical iteration count**: 1-3 generations (this is more complex than previous visuals)

---

### STEP 7: Download and Save

1. Click **"Download"** button
2. Rename to: `analytics-infographic-use-cases-matrix.png`
3. Move to: `/docs/writing/5-analytics/visuals/use-cases-matrix/`

**File location**:
```
/docs/writing/5-analytics/visuals/use-cases-matrix/analytics-infographic-use-cases-matrix.png
```

---

### STEP 8: Optimize for Web (Optional)

```bash
convert analytics-infographic-use-cases-matrix.png \
  -quality 85 \
  analytics-infographic-use-cases-matrix.webp
```

**Target**: WebP under 500KB

---

### STEP 9: Document Results

Create: `VIS-5.4-ANALYSIS.md`

```markdown
# VIS-5.4 Generation Analysis

**Visual ID**: VIS-5.4 - Predictive Analytics Use Cases Matrix
**Generated**: [Date]
**Platform**: NotebookLM
**Iterations**: [Number]
**Final file**: analytics-infographic-use-cases-matrix.png

## What Worked Well

- [e.g., "Clear four-row grid structure with color-coding"]
- [e.g., "All 15 use cases fit cleanly in matrix format"]
- [e.g., "Complexity indicators easy to scan"]
- [e.g., "Vendor examples provide concrete context"]

## What Needed Adjustment

- [Note any prompt modifications]
- [e.g., "Had to emphasize grid structure more explicitly"]
- [e.g., "Complexity legend required separate iteration"]
- [e.g., "Scale note (Legion enterprise-only) needed prominence"]

## Lessons for Future Visuals

- [Insights for complex multi-dimensional visualizations]
- [e.g., "Matrix format works well for showing breadth of applications"]
- [e.g., "Color-coding by function makes scanning easier"]

## Content Accuracy Notes

- [Verification of all 15 use cases against source]
- [Verification of ROI metrics and vendor names]
- [Verification of complexity assessments]

---

*Generation completed: [Date and time]*
```

---

## Troubleshooting

### Issue: NotebookLM doesn't generate a visual

**Solution**: Type `Generate this as an infographic`

### Issue: Grid structure not clear (cells hard to distinguish)

**Solution**: Re-prompt with: "Make the grid structure very clear with distinct visual separation between rows. Use row colors (purple, coral, blue, green) as background for each row's cells. Add clear gridlines or cell outlines."

### Issue: Complexity legend missing

**Solution**: Re-prompt with: "Add complexity legend at bottom showing: GREEN circle (Low, 1-2 weeks), YELLOW circle (Medium, 2-4 weeks), RED circle (High, 4-8+ weeks). Show examples in legend (e.g., GREEN = Weather, RED = Dynamic Pricing)"

### Issue: Scale note not prominent

**Solution**: Re-prompt with: "Add prominent note at bottom: 'Most applications viable at all scales | EXCEPTION: Legion WFM only viable at enterprise scale ($5M+ labor, 1M+ transactions)'"

### Issue: Privacy callout missing

**Solution**: Re-prompt with: "Add privacy note at bottom: 'All personalization requires GDPR/CCPA explicit opt-in. Transparency increases consent from 20% (passive) to 40-50% (explicit).'"

### Issue: Vendor names or ROI metrics not readable

**Solution**: Re-prompt with: "Make vendor names and ROI metrics larger and bolder. Each cell should clearly show: [Icon] [Vendor Name] [Key Metric] [Timeline] [Complexity]"

### Issue: Not all 15 use cases visible

**Solution**: Re-prompt with: "Ensure all 15 use cases are present and readable: 4 Demand + 4 Resource + 3 Risk + 4 Revenue. Adjust cell size to fit all content."

### Issue: Statistics fabricated or incorrect

**Solution**: Re-prompt with: "Use ONLY these statistics: 40-41% (DICE), 78% (Tomorrowland), 13x (Legion), 90% (Lollapalooza), 8-12% (upsell), 75-85% (sponsorship)"

---

## Quality Standards

**Minimum requirements for VIS-5.4 approval:**

1. ✅ Four functional rows present (Demand, Resource, Risk, Revenue)
2. ✅ All 15 use cases present and labeled
3. ✅ Each cell shows: Vendor, ROI metric, timeline, complexity
4. ✅ Colors correct (purple demand, coral resource, blue risk, green revenue)
5. ✅ Complexity indicators visible (RED/YELLOW/GREEN circles)
6. ✅ Row color coding consistent and clear
7. ✅ Grid structure obvious (cells clearly separated)
8. ✅ Complexity legend visible at bottom
9. ✅ Scale note visible (Legion enterprise-only)
10. ✅ Privacy callout included
11. ✅ Key statistics accurate (40-41%, 78%, 13x, 90%, 8-12%, 75-85%)
12. ✅ Vendor names readable
13. ✅ Text legible at full resolution
14. ✅ No fabricated data

**Do not proceed until ALL criteria are met.**

---

## Time Estimate

| Step | Time |
|------|------|
| 1. Create notebook | 1 min |
| 2. Upload source | 1 min |
| 3. Apply style prompt | 2 min |
| 4. Generate | 2-3 min |
| 5. Review | 4-6 min (more complex grid) |
| 6. Iterate | 5-15 min (may need adjustments) |
| 7. Download & save | 1 min |
| 8. Optimize | 2 min |
| 9. Document | 3-5 min |
| **TOTAL** | **20-30 min** |

---

*VIS-5.4 Generation Instructions*
*Created: December 29, 2025*
*Part of: EventAI Visual Content Strategy (Section 5: Analytics)*
