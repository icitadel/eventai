# VIS-5.2 Generation Instructions

## Dynamic Pricing Mechanics: System/Algorithm Diagram

**Visual ID**: VIS-5.2
**Type**: System Flow Diagram (Horizontal Process)
**Platform**: NotebookLM
**Status**: Ready to generate
**Estimated Time**: ~15 minutes

---

## Quick Reference

**Input**: `dynamic-pricing.content.md` (prepared source document)
**Output**: `analytics-infographic-dynamic-pricing.png`
**Platform**: NotebookLM (https://notebooklm.google.com)

---

## Step-by-Step Generation Workflow

### STEP 1: Create New NotebookLM Notebook

1. Navigate to **https://notebooklm.google.com**
2. Click **"+ New notebook"**
3. Name it: `EventAI VIS-5.2 - Dynamic Pricing Mechanics`

---

### STEP 2: Upload Source Document

1. Click **"+ Sources"** button
2. Select **"Upload"** → **"Text files"**
3. Navigate to: `/docs/writing/5-analytics/visuals/dynamic-pricing/dynamic-pricing.content.md`
4. Click **"Upload"**
5. Wait for processing
6. Verify source appears in Sources panel

---

### STEP 3: Apply EventAI Visual Style

In the NotebookLM chat interface, paste this **exact customization prompt**:

```
Create a horizontal system flow diagram showing Dynamic Pricing Algorithm mechanics with three vertical lanes: Input Layer (left), Processing Layer (center), Output Layer (right). Show real-time data flowing left-to-right through the system, with emphasis on human review approval in the processing layer.

LAYOUT:
- Three vertical lanes clearly separated (Input | Processing | Output)
- Horizontal arrows showing data flow left-to-right
- Processing layer shows: Demand forecasting → Price elasticity → Revenue optimization → Human review & approval → Implementation
- Human review section prominently highlighted (95% of changes reviewed, 85-95% approved)
- Tomorrowland case study callout box (separate visual element)

INPUT LAYER (Left):
Show five input sources flowing toward center:
1. Current demand (sales velocity, inventory remaining, conversion rates)
2. Time factors (days to event, day of week, time of day)
3. Competitor pricing (real-time price intelligence)
4. Historical patterns (previous year demand, seasonality)
5. External factors (weather forecast, social sentiment, macro events)

PROCESSING LAYER (Center):
Show five processing stages in sequence:
1. Demand forecasting (ML model, predictive analytics)
2. Price elasticity (demand curves, customer segments)
3. Revenue optimization solver (maximize price × quantity)
4. Human review & approval (95% reviewed, show approval/rejection icons, 85-95% approval rate)
5. Implementation & distribution (real-time updates across all channels)
Human review section should show: checkmarks for approved, X marks for rejected, examples of rejection reasons

OUTPUT LAYER (Right):
Show three output types:
1. New ticket price (show example: $49 early bird → $119 day-of, note: up to 20-30% variance)
2. Real-time updates (frequency: every 1-6 hours, urgency messaging example)
3. A/B testing (test variants, measure conversion, rollback logic)
Include results box: Yield improvement, revenue per seat, conversion metrics

STYLE REQUIREMENTS:
- Colors: Sky blue (#4299E1) for input data, deep purple (#6B46C1) for AI processing, electric coral (#FF6B6B) for human review/approval decisions, green (#48BB78) for positive outcomes
- Ethical constraints sidebar: Use amber (#ED8936) for price floor/ceiling/variance caps/transparency requirements
- Typography: Inter for headings (bold, 24-36pt), Source Sans Pro for labels (12-14pt), Inter for statistics (36-48pt)
- Design: Semi-flat style, flow arrows showing clear direction, rounded corners (8-12px), 2-3px outlines
- Festival context where relevant (ticket pricing imagery, price tags, urgency messaging examples)

KEY STATISTICS TO HIGHLIGHT:
- Tomorrowland yield improvement: 78%
- Average ticket price: $150 (static) → $265 (dynamic)
- Human review rate: 95% of changes reviewed
- Approval rate: 85-95%
- Price variance: 143% markup over weeks (e.g., $49 → $119)
- Weekly variance: ±15-20% common
- A/B test win rate: 65-75%
- Conversion lift: +18% with dynamic pricing + urgency

CASE STUDY CALLOUT (Tomorrowland):
- Create separate visual callout box showing:
  - 78% yield improvement
  - Avg ticket $265 (vs $150 static)
  - Customer opposition: 91% → 34% with transparency
  - Key lesson: "Dynamic pricing optimal but requires transparency for customer trust"

ETHICAL SAFEGUARDS (Amber sidebar):
- Price floor: $35-50 minimum
- Price ceiling: $150-200 maximum
- Variance cap: ±20% day-over-day, ±5% intra-hour
- Transparency: Show price history, explain drivers, allow customer alerts
- Fairness messaging: "Price based on WHEN you buy, not WHO you are"

OVERALL MOOD: Clear, educational, showing both AI algorithm and human oversight. Emphasize algorithm accuracy, ethical constraints, and customer trust. Professional yet accessible.

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
   - **Orientation**: Landscape (for left-to-right flow)
   - **Size**: Largest available

**Wait time**: ~45-120 seconds

---

### STEP 5: Review Generated Visual

#### ✅ CONTENT ACCURACY CHECKLIST

- [ ] **Input layer** shows five sources (demand, time, competitor, historical, external)
- [ ] **Processing layer** shows five stages (forecasting, elasticity, optimization, human review, implementation)
- [ ] **Output layer** shows three outputs (new price, real-time updates, A/B testing)
- [ ] **Human review section** clearly shows approval/rejection with 95% review rate, 85-95% approval
- [ ] **Tomorrowland case study** shows 78% yield improvement, $265 avg price, opposition 91% → 34%
- [ ] **Ethical constraints sidebar** shows price floor/ceiling/variance caps
- [ ] **Price variance examples** shown: $49 → $119 (143% markup)
- [ ] **A/B testing logic** visible (test, measure, rollback if <5% lift)
- [ ] **Statistics accurate** (±15-20% weekly variance, ±5-10% intra-day, +18% conversion lift)
- [ ] **No fabricated data** beyond source document

#### ✅ STYLE COMPLIANCE CHECKLIST

- [ ] **Input layer** uses sky blue color
- [ ] **Processing layer** uses deep purple for algorithm
- [ ] **Human review** uses electric coral for approval/rejection
- [ ] **Outputs** use green for positive outcomes
- [ ] **Ethical constraints** use amber for safeguards
- [ ] **Flow arrows** clearly show left-to-right data movement
- [ ] **Tomorrowland callout** visually distinct from main diagram
- [ ] **Typography** clean and readable (Inter/Source Sans Pro)
- [ ] **Semi-flat design** with subtle depth
- [ ] **Festival context** visible (ticket imagery, price tags)

#### ✅ LAYOUT QUALITY CHECKLIST

- [ ] **Three lanes clearly defined** (Input, Processing, Output)
- [ ] **Horizontal flow obvious** with arrows showing direction
- [ ] **Human review prominent** (separate section, highlighted color)
- [ ] **Case study callout** visually separated
- [ ] **Ethical constraints sidebar** adjacent to main flow
- [ ] **Text legible** at full resolution
- [ ] **Balanced composition** (not overcrowded)
- [ ] **Statistics easily readable** at a glance

---

### STEP 6: Regenerate if Needed

**If visual is close but has minor issues:**
- "Make the human review section larger and more prominent (95% reviewed, 85-95% approved)"
- "Add example rejection reasons in the approval section (ethical concerns, brand risk)"
- "Increase size of Tomorrowland case study callout"
- "Make flow arrows more obvious with directional labels"

**If visual misses major requirements:**
- Return to STEP 3, revise the prompt
- Example: "The five input sources are not clearly labeled"
- Example: "The human review approval/rejection decision-making is not visible"
- Example: "Ethical constraints (price floor/ceiling) are missing"

**Typical iteration count**: 1-3 generations

---

### STEP 7: Download and Save

1. Click **"Download"** button
2. Rename to: `analytics-infographic-dynamic-pricing.png`
3. Move to: `/docs/writing/5-analytics/visuals/dynamic-pricing/`

**File location**:
```
/docs/writing/5-analytics/visuals/dynamic-pricing/analytics-infographic-dynamic-pricing.png
```

---

### STEP 8: Optimize for Web (Optional)

```bash
convert analytics-infographic-dynamic-pricing.png \
  -quality 85 \
  analytics-infographic-dynamic-pricing.webp
```

**Target**: WebP under 500KB

---

### STEP 9: Document Results

Create: `VIS-5.2-ANALYSIS.md`

```markdown
# VIS-5.2 Generation Analysis

**Visual ID**: VIS-5.2 - Dynamic Pricing Mechanics
**Generated**: [Date]
**Platform**: NotebookLM
**Iterations**: [Number]
**Final file**: analytics-infographic-dynamic-pricing.png

## What Worked Well

- [e.g., "Clear left-to-right flow showing data inputs to outputs"]
- [e.g., "Human review section clearly highlighted"]
- [e.g., "Tomorrowland case study effectively illustrated"]

## What Needed Adjustment

- [Note any prompt modifications]
- [e.g., "Had to emphasize the 95% human review rate more explicitly"]
- [e.g., "Ethical constraints sidebar required separate prompt iteration"]

## Lessons for Future Visuals

- [Insights for VIS-5.3, VIS-5.4]

## Content Accuracy Notes

- [Verification of statistics against source]

---

*Generation completed: [Date and time]*
```

---

## Troubleshooting

### Issue: NotebookLM doesn't generate a visual

**Solution**: Type `Generate this as an infographic`

### Issue: Three lanes not clearly separated

**Solution**: Re-prompt with: "Make three vertical lanes very clear with distinct background colors or vertical dividers. Label each lane: Input Layer | Processing Layer | Output Layer"

### Issue: Human review section not prominent

**Solution**: Re-prompt with: "Make human review section the visual center, with large approval/rejection checkmarks, 95% review rate, and 85-95% approval statistics prominently displayed"

### Issue: Missing ethical constraints

**Solution**: Re-prompt with: "Add amber-colored sidebar showing ethical safeguards: Price floor $35-50, Price ceiling $150-200, Variance cap ±20% day-over-day, Transparency requirements"

### Issue: Tomorrowland case study missing or unclear

**Solution**: Re-prompt with: "Add a separate callout box for Tomorrowland case study: 78% yield improvement, avg ticket $265 (vs $150), customer opposition 91% → 34% with transparency"

### Issue: Statistics fabricated or incorrect

**Solution**: Re-prompt with: "Use ONLY these statistics: 78% Tomorrowland yield, $265 avg price, 95% review rate, 85-95% approval rate, ±15-20% weekly variance, +18% conversion lift"

---

## Quality Standards

**Minimum requirements for VIS-5.2 approval:**

1. ✅ Three lanes clearly defined (Input, Processing, Output)
2. ✅ Horizontal flow obvious with arrows
3. ✅ Human review prominent (95% reviewed, 85-95% approved)
4. ✅ Five input sources visible
5. ✅ Five processing stages visible
6. ✅ Price variance examples shown ($49 → $119)
7. ✅ Tomorrowland case study visible (78% yield)
8. ✅ Ethical constraints sidebar (price floor/ceiling/variance)
9. ✅ Colors used correctly (blue inputs, purple algorithm, coral review, green outcomes, amber safeguards)
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

## Evaluation Learnings (December 30, 2025)

### ✅ What Worked Exceptionally Well

**Variant #3 achieved 95/100 - Outstanding quality (PUBLICATION-READY)**

1. **Strategic Saturation Mastery (Tufte Principle)**
   - ✅✅ **95% HUMAN REVIEW** coral box at 100% saturation - immediate attention
   - ✅ Less saturated backgrounds (30-40% opacity) - excellent readability
   - ✅ Strategic contrast directs eye to critical information (human oversight)
   - **Lesson**: Applying privacy-safety-matrix learnings produced first-batch publication quality

2. **Outstanding Festival Context (96/100)**
   - ✅✅ Ticket imagery and price tags - immediate "event pricing" signal
   - ✅ Shopping icons (cart, tags) - consumer purchasing context
   - ✅ Festival-specific visual vocabulary (not generic business diagrams)
   - **Lesson**: Festival context creates EventAI brand identity (recognizable, distinctive)

3. **Professional + Whimsy Balance Perfection**
   - ✅ Professional foundation (clean structure, evidence-based, credible)
   - ✅ Whimsical accents (ticket imagery, colorful layers, curved connectors)
   - ✅ Appropriate for business/academic audience
   - **Lesson**: Can have festival personality WITHOUT sacrificing credibility

4. **White Space Excellence**
   - ✅ 35-40% white space despite information density
   - ✅ Clear separation between layers (input, processing, output)
   - ✅ Breathing room around key elements
   - **Lesson**: White space elevates perceived quality dramatically

5. **Data Accuracy: 100/100**
   - ✅ All statistics verified against source material
   - ✅ Tomorrowland 78% yield improvement - exact match
   - ✅ 95% human review rate - exact match
   - ✅ No hallucinations or unsupported claims
   - **Lesson**: Gemini (Nano Banana) accurately translates content to visual

### ⚠️ Minor Improvements for Future Iterations

**Minor issues (not blockers for publication):**

1. **Micro-Text Size (Low Priority)**
   - Some text in ethical constraints section ~11-12pt
   - For print: Should increase to 14pt minimum
   - For screen: Current size acceptable
   - **Fix for next iteration**: Specify "Minimum 14pt all text" in prompt

### ❌ What to Avoid (Lessons from Variant #1 & #2)

**Variant #1 (85%):**
- ❌ **Limited festival context** (~70/100) → Generic system icons (graphs, gears)
- ❌ **Insufficient white space** (~25-30%) → Feels dense
- ❌ **Less strategic saturation** → Backgrounds similar opacity throughout
- **Lesson**: Festival context is essential for EventAI brand identity

**Variant #2 (89%):**
- ⚠️ **Still limited festival context** (~75/100) → Generic icons (cart, calendar, magnifying glass)
- ⚠️ **Human review not emphasized** → Missed opportunity for strategic saturation
- ⚠️ **Less saturated backgrounds not fully applied** → Similar opacity across sections
- **Lesson**: Strategic saturation on critical elements (95% human review) makes the difference

### 🎯 Prompt Refinements Already Applied (Variant #3 Success)

**These were already in the prompt and worked perfectly:**

1. **Strategic Saturation Strategy** ⭐ Applied from Privacy-Safety-Matrix
   ```
   🚨 CRITICAL: Use LESS saturated backgrounds (30-40% opacity) for input/processing/output layers. Reserve FULL saturation (100%) for emphasis: 95% HUMAN REVIEW coral box. Strategic contrast = Tufte principle.
   ```
   ✅ **Result**: Perfect execution in Variant #3

2. **Festival-Specific Visual Elements** ⭐ Applied Successfully
   ```
   Include festival/event-specific visual elements: ticket imagery, price tags, shopping icons. These create EventAI's distinctive visual vocabulary.
   ```
   ✅ **Result**: Outstanding festival context (96/100)

3. **Professional + Whimsy Balance** ⭐ Achieved
   ```
   Professional foundation (clean structure, evidence-based) + whimsical accents (ticket imagery, colorful layers). Appropriate for business/academic audience.
   ```
   ✅ **Result**: Perfect balance in Variant #3

4. **White Space Target** ⭐ Exceeded
   ```
   Target: 30%+ white space. Use strategic emptiness to separate layers and create breathing room.
   ```
   ✅ **Result**: 35-40% white space achieved

### 📊 Score Comparison: First Batch Success

**VIS-5.2 Dynamic Pricing (First Batch):**
- Variant #1: 85/100 (Good)
- Variant #2: 89/100 (Strong)
- Variant #3: 95/100 ✅✅ (Outstanding - PUBLICATION-READY)

**VIS-4.4 Privacy-Safety-Matrix (Comparison):**
- Batch 1 Best: 88/100 (Variant #3 - NOT publication-ready, needed Batch 2)
- Batch 2 Best: 93/100 (Variant #5 - PUBLICATION-READY)

**Key Achievement:**
- ✅ Dynamic Pricing achieved 95% on FIRST batch (no iteration needed!)
- ✅ Applied learnings from privacy-safety-matrix perfectly
- ✅ Strategic saturation + festival context = immediate success

### 🏆 Publication Status

**Status**: ✅ **APPROVED FOR PUBLICATION** (Variant #3, 95/100)

**No Batch 2 needed** - First-batch quality exceeds 90% threshold

**Recommendation:** Use Variant #3 for VIS-5.2 in Analytics chapter

---

*VIS-5.2 Generation Instructions*
*Created: December 29, 2025*
*Updated: December 30, 2025 (Evaluation learnings added)*
*Status: ✅ Generated, evaluated, Variant #3 approved for publication (95%)*
*Part of: EventAI Visual Content Strategy (Section 5: Analytics)*
