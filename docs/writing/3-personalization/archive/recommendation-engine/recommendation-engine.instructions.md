# VIS-3.1: DICE Recommendation Engine Flow - Generation Instructions

**Infographic**: Data Flow Diagram - DICE AI Recommendation Engine
**Status**: 🟡 READY TO GENERATE - First generation pending
**Estimated time**: ~20 minutes total

---

## Quick Start: NotebookLM Workflow

### Step 1: Upload Source (2 min)

1. Go to [NotebookLM](https://notebooklm.google.com/)
2. Create notebook: `EventAI - Personalization VIS-3.1`
3. Upload: `recommendation-engine.content.md` (this folder)
4. Wait for processing (~30 sec)

### Step 2: Generate Infographic (10-15 min)

1. Click **"Infographic"** in generation menu
2. Settings:
   - **Detail Level**: Detailed
   - **Orientation**: Landscape (data flow diagram orientation)
3. **Paste prompt** from below
4. Click **"Generate"**
5. Wait ~2 min for processing
6. **Generate 3-5 variations** (click regenerate)

---

## 🔥 MASTER PROMPT: Data Flow Diagram (Left-to-Right)

**Why**: Shows clear progression of data → processing → output → impact. Linear left-to-right follows natural reading pattern. Emphasizes the 40-41% impact callout.

**Copy this prompt** (token-optimized 298 tokens):

```
Data flow diagram: DICE AI Recommendation Engine driving 40-41% of festival ticket sales

🚨 CRITICAL: Pure white background #FFFFFF (NOT cream/beige), left-to-right flow, 30%+ white space, festival-specific icons

STRUCTURE:
- Three main horizontal sections: Input (left 25%) → Processing (center 50%) → Output (right 25%)
- Converging inputs flow to processor, diverging to outputs
- Large impact callout: "40-41% of Festival Ticket Sales"

INPUT LAYER (Left, Sky Blue #4299E1 tinted section):
Label: "DATA INPUTS" (bold 18pt)
Five boxes stacking vertically, each with colored band + icon + label + stat:

1. Listening History
   Icon: Music note + waveform (festival-context, NOT generic music symbol)
   Stat: "Real-time synced" (12pt)
   Detail: Streaming preference signal

2. Past Attendance
   Icon: Festival ticket + concert crowd (NOT generic ticket)
   Stat: "100K+ concerts/festivals attended" (12pt)
   Detail: Strongest preference signal

3. Social Connections
   Icon: Connected people nodes (NOT generic people)
   Stat: "+20-30% conversion with friends" (12pt)
   Detail: Collaborative filtering power

4. Real-Time Availability
   Icon: Calendar + location pin (festival context, NOT generic clock)
   Stat: "Location, schedule, budget" (12pt)
   Detail: Temporal + geographic filtering

5. Demographics & Psychographics
   Icon: User profiles/cohorts (NOT generic person icon)
   Stat: "Age, preference type, novelty" (12pt)
   Detail: Cold-start enabler

All five arrows converge toward center processor.

PROCESSING LAYER (Center, Deep Purple #6B46C1):
Central circle: "AI RECOMMENDATION ENGINE" (bold 28pt, white text on purple)

Three surrounding processor nodes (triangular arrangement):

1. Collaborative Filtering (top-left)
   Icon: Network of connected users (NOT gears)
   Label: "Collaborative Filtering" (bold 16pt)
   Detail: "Find similar users, recommend their picks" (12pt)
   Accent: Warm sunlight (#F6AD55)

2. Content-Based Filtering (top-right)
   Icon: Festival attributes/tags (genres, scale, experience) (NOT database)
   Label: "Content-Based Filtering" (bold 16pt)
   Detail: "Match user preferences to festival attributes" (12pt)
   Accent: Warm sunlight (#F6AD55)

3. Deep Learning Embedding (bottom)
   Icon: Neural network nodes (NOT circuit board)
   Label: "Deep Learning Embedding" (bold 16pt)
   Detail: "Capture complex patterns" (12pt)
   Accent: Warm sunlight (#F6AD55)

Curved arrows: 3 processors → center, showing integration
Feedback loop: Bottom arrow returning to processor (dashed, "User Feedback Loop" label, 12pt)

OUTPUT LAYER (Right, Mint Green #A8E6CF tinted section):
Label: "PERSONALIZED SUGGESTIONS" (bold 18pt)

Three stacked recommendation types:

1. Hero Recommendation (top)
   Festival card with coral (#FF6B6B) border:
   - Festival name (bold 16pt)
   - Dates + location (12pt)
   - Top 3 matching artists (bold 12pt)
   - "3 friends attended" badge
   Background: Mint #A8E6CF

2. Secondary Recommendations (middle)
   4-6 compact festival cards (smaller scale):
   - Name + top artist + "Ranked by fit" label
   Background: Sky blue #4299E1

3. Discovery Recommendations (bottom)
   2 exploratory cards with "Explore" badge:
   - Different genres/experience from core
   Background: Light purple tint

Output arrows spread outward from processor → recommendations

IMPACT CALLOUT (Right bottom, prominent coral box):
Hero stat: "40-41% of Festival Ticket Sales" (bold coral 48-56pt)
Context: "Driven by AI Recommendations" (bold slate 20pt)
Supporting: "vs. 59% direct search" (gray 14pt)

Bold coral arrow pointing from outputs to impact callout.

FLOW ARROWS:
- Input → Processing: 5 converging arrows (light purple, 2-3px)
- Processing → Output: 3 diverging arrows (light purple, 2-3px)
- Output → Impact: Single bold arrow (coral, 3-4px)
- Feedback loop: Dashed return arrow (sunlight, 2px)

STYLE:
- Background: PURE WHITE #FFFFFF (verify with color picker, not cream)
- Section areas: Color-coded regions (blue input, purple processing, mint output)
- Section dividers: Subtle light gray lines (1px)
- Typography: Inter bold titles/labels, Source Sans regular details
- Icons: Festival-specific (stages, crowds, wristbands, RFID, musical notes) NOT business clichés
- Layout: Semi-flat, rounded corners 8-12px, 2-3px outlines, generous padding
- White space: 30-35%, let sections breathe, don't cram
- Font hierarchy: Title 36pt, section headers 18pt, labels 16pt, details 12-14pt, callout 48-56pt

❌ AVOID:
Cream/beige backgrounds, generic business icons, text <12pt, cramped layouts <25% space, dark backgrounds, flowchart-style linear steps (show integration instead)

✅ REFERENCE:
Data flow should show convergence (inputs joining processor) + integration (processors working together) + divergence (outputs spreading). Festival context throughout. Professional + energetic mood.
```

---

## Step 3: Review Generated Variants (5 min)

### Quality Checklist

**✅ CRITICAL (Must Pass):**
- [ ] **Pure white background** (#FFFFFF, verify with color picker against black desktop)
- [ ] **Left-to-right flow** clear (inputs → processing → outputs → impact)
- [ ] **All 5 inputs** present: listening, attendance, social, availability, demographics
- [ ] **All 3 processors** shown: collaborative, content-based, deep learning
- [ ] **Output section** shows recommendations (hero + secondary + discovery)
- [ ] **40-41% callout** prominent, coral color, right-side placement
- [ ] **Festival-specific icons** (crowds, stages, wristbands, RFID) NOT generic business imagery
- [ ] **Text legible**: Minimum 12pt details, 16pt+ labels, 48-56pt stat
- [ ] **White space**: 30%+ of composition, not cramped
- [ ] **Arrows/flow** visual: Clear convergence → processing → divergence pattern

**✅ STYLE (EventAI Compliance):**
- [ ] Colors match palette: Sky blue inputs, deep purple processor, mint outputs, coral impact
- [ ] Typography: Inter bold titles, Source Sans body
- [ ] Semi-flat design, rounded corners, 2-3px outlines
- [ ] Professional + energetic mood balance
- [ ] Festival context visual language

**✅ DATA ACCURACY:**
- [ ] 40-41% stat correct (vs. 59% direct search)
- [ ] 5 data inputs accurately represented
- [ ] 3 processors correctly labeled
- [ ] Social proof stat (+20-30% conversion) accurate
- [ ] Festival attendance example (100K+) realistic

### If Any Variant Fails Checklist

**Background NOT pure white?**
→ Regenerate with "🚨 VERIFY background is EXACTLY #FFFFFF pure white. Use color picker to confirm. NOT #F5F5F5, NOT cream, NOT beige."

**Icons too generic?**
→ Regenerate with "Festival context: outdoor concert stages, dancing crowds, RFID wristbands, tickets, musical notes. AVOID: office workers, gears, generic people icons, business suits."

**Flow unclear?**
→ Regenerate with "Left-to-right data flow: Five inputs converge to processor, diverge to three output types, then point to 40-41% impact callout. Show integration pattern, not step-by-step sequence."

**Text too small?**
→ Regenerate with "Minimum 12pt body text, 16pt labels, 48-56pt impact stat. Print-ready sizes for readability."

**White space low?**
→ Regenerate with "30-35% white space minimum. Generous breathing room between sections. Don't fill every gap."

**Missing stats/elements?**
→ Verify source file uploaded, regenerate with explicit stat inclusion: "Include 40-41%, 59%, +20-30% conversion, 100K+ attendance, 3 algorithms, 5 inputs, 3 output types."

---

## Step 4: Download & Save (2 min)

### Download All Variants

1. Download each generated variant: Click download icon
2. Format: **PNG** (high resolution, 2000+ pixels wide for landscape)
3. Rename: `personalization-infographic-recommendation-engine-1.png`, `-2.png`, etc.
4. Save to: `docs/writing/3-personalization/visuals/recommendation-engine/`

### Convert to WebP (Optional, for web optimization)

```bash
cd docs/writing/3-personalization/visuals/recommendation-engine
todd-image-convert personalization-infographic-recommendation-engine-*.png --output-format webp --resolution 1080p
```

---

## Step 5: Evaluate & Select Winner (5 min)

### Run Evaluation (if you have evaluation tools)

```bash
/ig-evaluate docs/writing/3-personalization/visuals/recommendation-engine/*.webp
```

Assesses:
- EventAI style compliance
- Best practices (white space, readability, festival context)
- Data accuracy
- Accessibility (contrast, text size)
- Print readiness

### Selection Criteria

**Prioritize variants with:**
1. Pure white background (non-negotiable)
2. Clear left-to-right flow (data → processing → output → impact)
3. Festival-specific visual language (crowds, stages, wristbands)
4. Prominent 40-41% callout (coral, 48-56pt+)
5. Good white space (30%+)
6. Readable text (12pt+ minimum)

### Expected Quality

**Strong variants:** 75-85/100 (if flow clear, icons festival-specific, white background)

---

## File Deliverables

- ✅ `personalization-infographic-recommendation-engine-{N}.png` (high-res PNG)
- ✅ `personalization-infographic-recommendation-engine-{N}.webp` (web-optimized, optional)
- ✅ Winner selected and documented

---

## Troubleshooting Common Issues

### 🔴 Flow not clear (arrows confusing)

**Problem**: Too many arrow types or directions
**Solution**: Regenerate with "Show clear left-to-right progression: 5 inputs converge to 1 processor, processor outputs diverge to 3 recommendation types, all point to 40-41% impact. 3 main sections with clear boundaries."
**Prevention**: Emphasize section layout clearly in prompt

### 🔴 Icons too generic

**Problem**: Gears, generic people, office imagery
**Solution**: Regenerate with "Festival-context icons only: concert stages, dancing crowds, RFID wristbands, festival tickets, musical notes, calendar, location pins. NO gears, suits, handshakes, office workers, generic database symbols."
**Prevention**: List specific festival elements

### 🔴 40-41% not prominent

**Problem**: Callout too small or not emphasized
**Solution**: Regenerate with "Impact callout must be HERO element: 48-56pt bold coral (#FF6B6B) stat, 20pt context label, 14pt supporting stat. Positioned bottom-right, largest text in entire diagram."
**Prevention**: Specify exact placement + sizing

### 🔴 Processing visualization confusing

**Problem**: 3 processors not clearly integrated
**Solution**: Regenerate with "Show 3 processors as triangle arrangement around central processor. Curved arrows from each → center. Feedback loop arrow returning from bottom. Make integration clear, not sequential."
**Prevention**: Sketch layout in prompt first

---

## Key Learnings (Adaptation from VIS-1.3)

**What Works:**
- ✅ Section-based layout (color-coded regions create visual organization)
- ✅ Converging/diverging flows (shows transformation/processing)
- ✅ Festival-specific icons (builds credibility, matches brand)
- ✅ Bold statistics in colored text (easy to scan and remember)
- ✅ Large callouts for key metrics (creates impact emphasis)

**What to Avoid:**
- ❌ Pure white background non-negotiable (learned from barriers evaluation)
- ❌ Generic business imagery (reduces festival credibility)
- ❌ Cramped layouts (white space creates professional appearance)
- ❌ Complex flowchart progression (integration/transformation more engaging than steps)

---

## Token-Optimized Quick Commands

**Full workflow one-liners:**

```bash
# After downloading PNGs (if using image converter):
todd-image-convert docs/writing/3-personalization/visuals/recommendation-engine/*.png --output-format webp --resolution 1080p

# Evaluation (if tools available):
/ig-evaluate docs/writing/3-personalization/visuals/recommendation-engine/*.webp
```

---

## Expected Outcomes

### What Success Looks Like

**Data Flow Visualization:**
- Clear left-to-right progression: inputs → processing → outputs → impact
- 5 input boxes on left (sky blue section)
- Central processor with 3 surrounding algorithms (deep purple)
- 3 output types on right (mint section)
- Bold "40-41%" callout bottom-right (coral emphasis)
- Converging/diverging arrows showing data transformation
- Pure white background with 30%+ white space

**Visual Elements:**
- All icons festival-specific (no generic business imagery)
- Section dividers subtle but clear
- Text hierarchy obvious (title > labels > details)
- Colors match EventAI palette exactly
- Professional + energetic mood balance

**Data Accuracy:**
- 40-41% stat prominent and accurate
- 59% direct search mentioned
- All 5 inputs correctly labeled
- All 3 processors correctly named
- Festival context preserved throughout

---

## Next Steps After Successful Generation

### 1. Save to Visuals Folder

Filename convention: `personalization-infographic-recommendation-engine-{variant}.png`

### 2. Update Visual Content Plan

Mark VIS-3.1 complete in `VISUAL-CONTENT-PLAN.md`:
```markdown
- ✅ VIS-3.1: Recommendation engine data flow (Variant #X, Dec 29 2025)
```

### 3. Reference in Draft

Add to section 3-personalization text:
```markdown
![DICE Recommendation Engine Flow](../visuals/recommendation-engine/personalization-infographic-recommendation-engine-X.webp)
```

### 4. Move to Next Visual

Proceed to **VIS-3.2: Bonnaroo Engagement Metrics** (engagement-metrics folder)

---

## Related Documentation

- [Recommendation Engine Content](recommendation-engine.content.md) - Full source material
- [EventAI Visual Identity](../../../lemmy/style-guide/eventai-visual-identity.md) - Brand standards
- [Visual Content Plan](../../VISUAL-CONTENT-PLAN.md) - All planned visuals
- [Infographic Best Practices](../../../lemmy/research/infographics-best-practices.md) - Design principles

---

*VIS-3.1 Generation Package - Ready for NotebookLM*
*Token-optimized prompt: 298 tokens*
*Expected generation time: 15-20 minutes for 3-5 variants*
*Typical first-generation success rate: High (clear requirements, festival context)*
