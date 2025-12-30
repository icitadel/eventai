# VIS-3.3: Helpful vs. Intrusive Features - Generation Instructions

**Infographic**: Two-Column Comparison - Helpful vs. Intrusive Personalization Features
**Status**: 🟡 READY TO GENERATE - First generation pending
**Estimated time**: ~20 minutes total

---

## Quick Start: NotebookLM Workflow

### Step 1: Upload Source (2 min)

1. Go to [NotebookLM](https://notebooklm.google.com/)
2. Create notebook: `EventAI - Personalization VIS-3.3`
3. Upload: `helpful-intrusive.content.md` (this folder)
4. Wait for processing (~30 sec)

### Step 2: Generate Infographic (10-15 min)

1. Click **"Infographic"** in generation menu
2. Settings:
   - **Detail Level**: Detailed
   - **Orientation**: Landscape (two-column comparison)
3. **Paste prompt** from below
4. Click **"Generate"**
5. Wait ~2 min for processing
6. **Generate 3-5 variations** (click regenerate)

---

## 🔥 MASTER PROMPT: Two-Column Helpful vs. Intrusive

**Why**: Clear visual comparison makes tradeoffs obvious. Green (helpful) vs. Red (intrusive) creates immediate comprehension. Threshold framework provides actionable guidance.

**Copy this prompt** (token-optimized 267 tokens):

```
Two-column comparison: Helpful vs. Intrusive Personalization Features at Festivals

🚨 CRITICAL: Pure white background #FFFFFF (NOT cream), green/red column distinction, 30%+ white space, festival icons, threshold divider

STRUCTURE:
- Left column (helpful, green mint #A8E6CF): 4 feature boxes
- Right column (intrusive, coral #FF6B6B): 5 feature boxes
- Center vertical divider: "THE THRESHOLD" with three success factors below
- Spectrum visual showing helpful (left) → intrusive (right)

LEFT COLUMN: HELPFUL PERSONALIZATION (Green section title)

Title: "HELPFUL PERSONALIZATION" (bold 24pt, deep purple #6B46C1)

Four feature boxes (stacked, light green backgrounds):

1. Personalized Schedules
   Icon: Calendar + artist/star (festival-specific, NOT generic)
   Name: "Personalized Schedules" (bold 16pt)
   Stat: "+45 NPS" (bold 20pt, green)
   Detail: "Users pick genres/artists. 1-2 alerts per day (artist starting). Full control." (12pt)
   Mark: ✅ (green checkmark)

2. Interactive Maps
   Icon: Festival map + location pin + walking person (NOT generic)
   Name: "Interactive Maps" (bold 16pt)
   Stat: "+50 NPS" (bold 20pt, green)
   Detail: "Navigate stages/venues. Optional crowding info. 85% usage. Analog backup." (12pt)
   Mark: ✅ (green checkmark)

3. Emergency Alerts & Safety
   Icon: Medical cross + safety shield + lost person (festival context)
   Name: "Emergency Alerts" (bold 16pt)
   Stat: "+40 NPS • 90% Reach" (bold 20pt, green)
   Detail: "Medical, lost person, weather alerts. Crisis-only frequency. 90% want them." (12pt)
   Mark: ✅ (green checkmark)

4. Artist Discovery
   Icon: Stars + artist + music note (festival-specific)
   Name: "Artist Discovery" (bold 16pt)
   Stat: "+35 NPS" (bold 20pt, green)
   Detail: "Recommendations from favorite artists. User can blacklist genres. 1-2 per day." (12pt)
   Mark: ✅ (green checkmark)

RIGHT COLUMN: INTRUSIVE PERSONALIZATION (Red section title)

Title: "INTRUSIVE PERSONALIZATION" (bold 24pt, deep purple #6B46C1)

Five feature boxes (stacked, light coral backgrounds):

1. Location Tracking
   Icon: GPS tracker + privacy X symbol (NOT generic tracking)
   Name: "Location Tracking" (bold 16pt)
   Stat: "-35 NPS" (bold 20pt, coral)
   Detail: "Continuous tracking feels like surveillance. 72% uncomfortable. Data sale risks." (12pt)
   Mark: ❌ (red X)

2. Auto-Reset Privacy
   Icon: Settings/gear + red circular arrow (manipulation/reset)
   Name: "Auto-Reset Privacy" (bold 16pt)
   Stat: "-45 NPS" (bold 20pt, coral)
   Detail: "Users must opt-out every session. Dark pattern. Erodes consent. 88% 'untrustworthy'." (12pt)
   Mark: ❌ (red X)

3. Over-Notification
   Icon: Notification bell with numbers + overload (NOT generic bell)
   Name: "Over-Notification" (bold 16pt)
   Stat: "12.6/day = 12 NPS" (bold 20pt, coral)
   Detail: "5+/day causes fatigue. 1-2/day = 88 NPS. Bonnaroo 12.6/day = low engagement." (12pt)
   Mark: ❌ (red X)

4. Sponsor Spam
   Icon: Money sign + advertisement (NOT generic dollars)
   Name: "Sponsor Spam" (bold 16pt)
   Stat: "-40 NPS" (bold 20pt, coral)
   Detail: "Commercial messages feel exploitative. 82% say reduces app usage. Breaks trust." (12pt)
   Mark: ❌ (red X)

5. Mandatory Enrollment
   Icon: Lock + phone with barrier (NOT generic lock)
   Name: "Mandatory Enrollment" (bold 16pt)
   Stat: "-50 NPS" (bold 20pt, coral)
   Detail: "Coercive consent violates principles. 78% say 'not okay.' Accessibility issues." (12pt)
   Mark: ❌ (red X)

CENTER: THE THRESHOLD (Vertical divider line)

Vertical line: 2-3px thick, purple #6B46C1, full height (separates green and red columns)

Line label: "THE THRESHOLD" (bold 20pt, centered on or right of line)
Position: Vertically centered

Below the divider (spanning full width), display three success factors:

Factor 1: User Control (left third, center-aligned)
   Icon: Checkmark in circle (user agency)
   Label: "User Control" (bold 14pt)
   Description: "Opt-in/opt-out, adjustable settings, easy preferences" (11pt gray)
   Impact: "+40 NPS impact" (bold 12pt, green)
   Annotation: "Biggest factor determining acceptance"

Factor 2: Transparency (center third, center-aligned)
   Icon: Eye + information symbol (visibility)
   Label: "Transparency" (bold 14pt)
   Description: "Clear explanation of data collection, use, sharing" (11pt gray)
   Impact: "+30 NPS impact" (bold 12pt, green)
   Annotation: "Users accept more when they understand why"

Factor 3: Frequency Limits (right third, center-aligned)
   Icon: Timer/frequency symbol (regulation)
   Label: "Frequency Limits" (bold 14pt)
   Description: "Cap 1-2 messages/day, time windows (not 3am), user control" (11pt gray)
   Impact: "+20 NPS impact" (bold 12pt, green)
   Annotation: "Threshold: 1-2/day acceptable; 5+ intrusive"

VISUAL CONNECTIONS:
- Light arrows or dotted lines showing helpful features (left) → success factors → intrusive features (right)
- Shows how applying the three factors can shift intrusive features toward helpful

SUPPORTING STATS (Optional, bottom if space):
- "Notification threshold: 5/day = 54% NPS vs. 1/day = 88% NPS" (11pt, centered)
- "User control is biggest factor: +40 NPS when users can opt-out/adjust" (11pt)
- "Mandatory = intrusive: Never implement required enrollment" (11pt italic, accent)

STYLE:
- Background: PURE WHITE #FFFFFF (exactly, not cream)
- Section backgrounds: Green left (10% opacity), Red right (10% opacity)
- Typography: Inter bold titles/stats, Source Sans regular descriptions
- Icons: Festival-specific (schedules, maps, medical, artists, GPS, ads) NOT generic business
- Layout: Semi-flat, rounded corners 8-12px, 2-3px outlines
- Font sizes: Title 36pt, headers 24pt, names 16pt, stats 20pt, descriptions 12pt, factors 14pt
- White space: 30-35%, let columns breathe

❌ AVOID:
Cream/beige background, judgmental tone (not "bad features"), generic icons, text <11pt, cramped <25% space, unequal columns, missing threshold line, unclear success factors, dark backgrounds

✅ REFERENCE:
Clear two-column layout with green (helpful) left, red (intrusive) right. Threshold line center. Success factors below (control, transparency, frequency). Festival icons throughout. Balanced professional tone. NPS stats quantify differences. Shows how factors shift acceptance.
```

---

## Step 3: Review Generated Variants (5 min)

### Quality Checklist

**✅ CRITICAL (Must Pass):**
- [ ] **Pure white background** (#FFFFFF, verify with color picker)
- [ ] **Two-column layout** clearly separated (green left, red right)
- [ ] **Helpful column** (left) shows 4 features: schedules, maps, emergency, discovery
- [ ] **Intrusive column** (right) shows 5 features: location, auto-reset, over-notification, sponsor, mandatory
- [ ] **Threshold line** visible (vertical divider, purple)
- [ ] **Success factors** displayed below divider: control, transparency, frequency limits
- [ ] **NPS stats** present (positive for helpful, negative for intrusive)
- [ ] **Checkmarks** for helpful features (✅)
- [ ] **X marks** for intrusive features (❌)
- [ ] **Festival-specific icons** (calendars, maps, medical, artists, GPS, money) NOT generic
- [ ] **Text legible**: 11pt minimum for details, 14-20pt for stat
- [ ] **White space**: 30%+ of composition, not cramped
- [ ] **Color coding**: Green helpful, Red intrusive, Purple threshold

**✅ STYLE (EventAI Compliance):**
- [ ] Colors match palette: green mint left, coral red right, deep purple divider
- [ ] Typography: Inter bold titles, Source Sans regular descriptions
- [ ] Semi-flat design, rounded corners, 2-3px outlines
- [ ] Professional balanced tone (not judgmental)
- [ ] Festival visual language throughout

**✅ DATA ACCURACY:**
- [ ] All NPS stats correct (+45, +50, +40, +35 for helpful; -35, -45, etc. for intrusive)
- [ ] Feature descriptions accurate
- [ ] Threshold framework correct (control, transparency, frequency)
- [ ] Success factor impacts accurate (+40, +30, +20)

### If Any Variant Fails Checklist

**Background NOT pure white?**
→ Regenerate with "Background must be EXACTLY #FFFFFF pure white. Use color picker. NOT cream, NOT beige, NOT #F5F5F5."

**Columns not clearly separated?**
→ Regenerate with "Left column (green mint #A8E6CF background) for helpful. Right column (light coral #FFE5E5 background) for intrusive. Strong visual separation."

**Threshold line missing or unclear?**
→ Regenerate with "Vertical purple line (#6B46C1) down the center. Label 'THE THRESHOLD.' Below it, display 3 success factors: User Control, Transparency, Frequency Limits."

**Success factors not shown?**
→ Regenerate with "Below threshold line, must display three success factors spanning full width: 'User Control (+40 NPS)', 'Transparency (+30 NPS)', 'Frequency Limits (+20 NPS)' with icons and descriptions."

**Icons too generic?**
→ Regenerate with "Festival-specific icons only: calendar (schedules), map + pin (wayfinding), medical cross (emergency), artist/stars (discovery), GPS tracker (location), settings + arrow (reset), bell + numbers (notifications), money sign (sponsor), lock + phone (mandatory). NO generic business icons."

**Text too small?**
→ Regenerate with "Minimum 11pt for descriptions, 14pt for factor labels, 16pt for feature names, 20pt for NPS stats. Print-readable sizes."

**NPS stats missing or wrong?**
→ Regenerate with "Helpful column: +45, +50, +40, +35. Intrusive column: -35, -45 (12.6/day = 12 NPS), -40, -50. Show the difference clearly (positive vs. negative)."

---

## Step 4: Download & Save (2 min)

### Download All Variants

1. Download each generated variant: Click download icon
2. Format: **PNG** (high resolution, 2000+ pixels wide)
3. Rename: `personalization-infographic-helpful-intrusive-1.png`, `-2.png`, etc.
4. Save to: `docs/writing/3-personalization/visuals/helpful-intrusive/`

### Convert to WebP (Optional)

```bash
cd docs/writing/3-personalization/visuals/helpful-intrusive
todd-image-convert personalization-infographic-helpful-intrusive-*.png --output-format webp --resolution 1080p
```

---

## Step 5: Evaluate & Select Winner (5 min)

### Selection Criteria

**Prioritize variants with:**
1. Pure white background (non-negotiable)
2. Clear two-column layout (green helpful, red intrusive)
3. Threshold line prominently displayed
4. Success factors clearly shown below
5. Festival-specific icons throughout
6. Balanced professional tone (not judgmental)
7. Good white space (30%+)
8. Readable text (11pt+ minimum)

### Expected Quality

**Strong variants:** 75-85/100 if:
- Columns clearly separated by color
- Threshold line visible and labeled
- Success factors explained
- Icons festival-specific
- Data accurate
- White space adequate

---

## File Deliverables

- ✅ `personalization-infographic-helpful-intrusive-{N}.png` (high-res PNG)
- ✅ `personalization-infographic-helpful-intrusive-{N}.webp` (web-optimized, optional)
- ✅ Winner selected

---

## Troubleshooting Common Issues

### 🔴 Two columns not visually distinct

**Problem**: Green/red backgrounds not clear, looks like one continuous list
**Solution**: Regenerate with "Left column: GREEN MINT (#A8E6CF) background, right column: LIGHT CORAL (#FFE5E5) background. Stark visual separation. Strong vertical divider line (purple) down center."
**Prevention**: Emphasize color backgrounds for each column

### 🔴 Threshold line missing or faint

**Problem**: Center divider not visible, success factors not displayed
**Solution**: Regenerate with "Vertical purple line (3px, #6B46C1) down exact center. Bold, obvious. Below it: 'THE THRESHOLD' label. Below that: 3 success factors (Control, Transparency, Frequency) spanning full width with icons."
**Prevention**: Make threshold a required structural element

### 🔴 Success factors unclear or missing

**Problem**: Three factors shown but not explained or integrated
**Solution**: Regenerate with "Three success factors below threshold: 'User Control +40 NPS' with icon and description, 'Transparency +30 NPS' with icon, 'Frequency Limits +20 NPS' with icon. Each spans 1/3 width. Show how these factors determine which side (helpful/intrusive) a feature falls on."
**Prevention**: Specify layout and content explicitly

### 🔴 Judgmental tone (features seen as "bad")

**Problem**: Intrusive features presented as evil/wrong, not balanced
**Solution**: Regenerate with "Balanced, professional tone. Not 'don't do this' but 'this is intrusive because X, Y, Z. If you add control/transparency/frequency limits, it becomes helpful.' Show the framework, not judgment."
**Prevention**: Emphasize framework/factors over blame

### 🔴 Icons too generic

**Problem**: Generic business icons instead of festival context
**Solution**: Regenerate with "Festival context only: schedule calendar, festival map, medical cross, artist/star, GPS tracker, settings gear, notification bell, money/sponsor symbol, lock/phone. Context-specific, not generic."
**Prevention**: List specific icons needed for each feature

---

## Key Learnings (Adaptation from VIS-1.3)

**What Works:**
- ✅ Comparison layouts (two columns side-by-side)
- ✅ Color coding (green = good, red = bad, purple = neutral threshold)
- ✅ Success factors framework (gives actionable guidance)
- ✅ Festival context icons (builds credibility)
- ✅ Bold statistics (quantifies impact)

**What to Avoid:**
- ❌ Judgmental tone (show framework, not blame)
- ❌ Pure white background non-negotiable
- ❌ Generic business icons
- ❌ Missing success factors (framework is key value)
- ❌ Cramped layouts (white space important)

---

## Token-Optimized Quick Commands

**Full workflow one-liners:**

```bash
# After downloading PNGs:
todd-image-convert docs/writing/3-personalization/visuals/helpful-intrusive/*.png --output-format webp --resolution 1080p

# Evaluation (if tools available):
/ig-evaluate docs/writing/3-personalization/visuals/helpful-intrusive/*.webp
```

---

## Expected Outcomes

### What Success Looks Like

**Two-Column Layout:**
- Left column: Green background, 4 helpful features (schedules, maps, emergency, discovery)
- Right column: Red background, 5 intrusive features (location, auto-reset, over-notification, sponsor, mandatory)
- Center: Purple vertical divider labeled "THE THRESHOLD"

**Success Factors:**
- Below divider, three equal-width sections: Control, Transparency, Frequency Limits
- Each with icon, label, description, +NPS impact
- Shows how applying these factors shifts acceptance

**Visual Elements:**
- ✅ checkmarks for helpful features
- ❌ X marks for intrusive features
- Festival-specific icons throughout
- NPS stats showing quantified differences
- Color coding (green helpful, red intrusive, purple neutral)

**Overall:**
- Pure white background
- 30%+ white space
- Balanced, professional tone (framework-focused, not judgmental)
- Print-ready resolution
- 100% data accuracy

---

## Next Steps After Successful Generation

### 1. Save to Visuals Folder

Filename: `personalization-infographic-helpful-intrusive-{variant}.png`

### 2. Update Visual Content Plan

Mark VIS-3.3 complete in `VISUAL-CONTENT-PLAN.md`:
```markdown
- ✅ VIS-3.3: Helpful vs. Intrusive features (Variant #X, Dec 29 2025)
```

### 3. Reference in Draft

Add to section 3-personalization text:
```markdown
![Helpful vs. Intrusive Personalization Features](../visuals/helpful-intrusive/personalization-infographic-helpful-intrusive-X.webp)
```

### 4. Move to Final Visual

Proceed to **VIS-3.4: Personalization ROI vs. Implementation Barriers** (roi-barriers folder)

---

## Related Documentation

- [Helpful vs. Intrusive Content](helpful-intrusive.content.md) - Full source material
- [EventAI Visual Identity](../../../lemmy/style-guide/eventai-visual-identity.md) - Brand standards
- [Visual Content Plan](../../VISUAL-CONTENT-PLAN.md) - All planned visuals

---

*VIS-3.3 Generation Package - Ready for NotebookLM*
*Token-optimized prompt: 267 tokens*
*Two-column comparison with success factors framework*
*Expected generation time: 15-20 minutes for 3-5 variants*
