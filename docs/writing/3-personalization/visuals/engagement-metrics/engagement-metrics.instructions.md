# VIS-3.2: Bonnaroo iBeacon Engagement Metrics - Generation Instructions

**Infographic**: Adoption vs. Engagement Gap Analysis - Bonnaroo iBeacon Case Study
**Status**: 🟡 READY TO GENERATE - First generation pending
**Estimated time**: ~20 minutes total

---

## Quick Start: NotebookLM Workflow

### Step 1: Upload Source (2 min)

1. Go to [NotebookLM](https://notebooklm.google.com/)
2. Create notebook: `EventAI - Personalization VIS-3.2`
3. Upload: `engagement-metrics.content.md` (this folder)
4. Wait for processing (~30 sec)

### Step 2: Generate Infographic (10-15 min)

1. Click **"Infographic"** in generation menu
2. Settings:
   - **Detail Level**: Detailed
   - **Orientation**: Landscape (side-by-side funnel + chart)
3. **Paste prompt** from below
4. Click **"Generate"**
5. Wait ~2 min for processing
6. **Generate 3-5 variations** (click regenerate)

---

## 🔥 MASTER PROMPT: Adoption Funnel + Notification Chart

**Why**: Shows two complementary stories: narrowing adoption funnel (adoption-engagement gap) + notification volume surge (fatigue driver). Side-by-side layout emphasizes both factors simultaneously.

**Copy this prompt** (token-optimized 284 tokens):

```
Bonnaroo iBeacon engagement metrics: Adoption gap and notification fatigue visualization

🚨 CRITICAL: Pure white background #FFFFFF (NOT cream/beige), funnel + bar chart layout, 30%+ white space, festival icons

STRUCTURE:
- Left (40%): Adoption funnel showing 86% download → 20% engagement narrowing, with 66% gap annotation
- Right (60%): Notification volume stacked bar chart by day (Fri-Mon)
- Center overlap: Large coral callout showing 12.6 notifications/day + gap context
- Bottom (25%): Notification category breakdown (5 types, including zero promotional year 1)

ADOPTION FUNNEL (Left section, Sky Blue #4299E1 tint):

Title: "THE ADOPTION GAP" (bold 20pt, slate)

Funnel layers top-to-bottom:
1. Base: 70K Attendees (icon: festival crowd silhouette, cheerful)
   Label: "Total festival attendees" (12pt)

2. Step 1: 60,000+ Downloads (icon: phone with checkmark, NOT generic phone)
   Stat: "86% Downloaded App" (bold 24pt, blue)
   Detail: "Map, schedule, basic features" (12pt)
   Visual width: 90% (slight narrowing)

3. Step 2: 12,000 Engaged Users (icon: person with location pin + smile, active pose)
   Stat: "20% Actively Engaged" (bold 24pt, blue)
   Detail: "Used personalization features" (12pt)
   Visual width: 20% (dramatic narrowing to show gap)

Gap visualization: Show diverging space between steps 1 and 2
Gap label: "66 Percentage Point Gap" (bold coral 28pt, positioned right side)
Gap annotation: "Why? Privacy concerns (40%), Battery drain (20%), Notification fatigue (15%), Feature discovery (15%), Other (10%)" (gray 12pt, boxed callout)

Colors: Light blue funnel sections, white space highlighting the gap

NOTIFICATION VOLUME CHART (Right section, Coral #FF6B6B tint):

Title: "NOTIFICATION SURGE" (bold 20pt, slate)

Stacked bar chart: 4 bars (Fri, Sat, Sun, Mon) showing daily notification volume

Y-axis: 0 to 35K (labeled 0, 10K, 20K, 30K, 35K)
X-axis: Days (Friday, Saturday, Sunday, Monday)

Day 1 (Friday): Bar height 15,000
Label: "15K notifications" (bold 14pt, positioned above bar)
Per-user stat: "2.5 per user avg" (gray 12pt)
Color: Light coral (#FF6B6B light tint)

Day 2 (Saturday): Bar height 32,000 (PEAK, marked with "PEAK" label)
Label: "32K notifications" (bold 14pt, larger text)
Per-user stat: "5.3 per user avg" (gray 12pt, PEAK day)
Color: Dark coral (#FF6B6B full saturation)
Icon: Small festival stage/crowd emoji indicating peak attendance

Day 3 (Sunday): Bar height 28,000
Label: "28K notifications" (bold 14pt)
Per-user stat: "4.7 per user avg" (gray 12pt)
Color: Medium coral (blend)

Day 4 (Monday): Bar height 22,000
Label: "22K notifications" (bold 14pt)
Per-user stat: "3.7 per user avg" (gray 12pt)
Color: Light coral

Total volume label: "97,000+ Notifications Over 4 Days" (bold 20pt, centered above entire chart)

Trend line: Curved line connecting tops of bars, showing peak Saturday, decline after
Grid: Horizontal lines at 10K, 20K, 30K (light gray 1px)

HERO CALLOUT BOX (Center-overlapping, positioned between funnel and chart):

Background: Electric coral (#FF6B6B) with white text
Border: 3px rounded corners, dark coral border

Primary statistic: "12.6 Notifications Per Engaged User Per Day" (bold 44-48pt, white)
Secondary context: "Notification Fatigue Threshold" (white 18pt, lighter weight)
Supporting metric: "66% Downloaded But Didn't Engage" (bold 28pt, white)
Annotation: "Privacy concerns, battery drain, and overwhelming message volume created adoption-engagement gap. Even non-commercial notifications caused fatigue." (gray 14pt, 2-3 lines, right-aligned outside box)

NOTIFICATION CATEGORY BREAKDOWN (Bottom section, light gray tint):

Title: "WHAT WERE THOSE 97K MESSAGES?" (bold 16pt, slate)

Horizontal stacked bar OR pie chart showing 5 categories:

1. Personalized Recommendations (40%, ~38,800 messages)
   Label: "40% — Recommendations" (12pt bold)
   Detail: "Artist matching, schedule suggestions" (10pt gray)
   Color: Electric coral (#FF6B6B)
   Icon: Stars or artist note

2. Friend Location Updates (25%, ~24,250 messages)
   Label: "25% — Find Friends" (12pt bold)
   Detail: "Friend proximity notifications" (10pt gray)
   Color: Warm sunlight (#F6AD55)
   Icon: Person + location pin

3. Emergency/Safety Alerts (20%, ~19,400 messages)
   Label: "20% — Safety & Info" (12pt bold)
   Detail: "Medical, lost & found, stage updates" (10pt gray)
   Color: Sky blue (#4299E1)
   Icon: Alert triangle + medical cross

4. Artist/Stage Information (10%, ~9,700 messages)
   Label: "10% — Artist Info" (12pt bold)
   Detail: "Biographies, set times, stage details" (10pt gray)
   Color: Soft mint (#A8E6CF)
   Icon: Stage + artist

5. Promotional Messages (5%, ZERO in Year 1)
   Label: "5% — Promotional (ZERO Year 1)" (12pt bold, italic)
   Detail: "Bonnaroo avoided sponsored messages Year 1 for trust-building" (10pt italic gray)
   Color: Light gray (de-emphasized to show it wasn't used)
   Icon: Trophy or trust symbol

Key insight: "Bonnaroo deliberately sent ZERO promotional/sponsored messages in Year 1 to build user trust. Despite avoiding commercial messaging, 12.6 messages/day from organic alerts still caused fatigue." (bold 12pt italic, 2-line annotation, positioned right side)

LAYOUT & SPACING:
- Left funnel: 40% width, light sky-blue background section
- Right chart: 60% width, white background
- Center callout: Positioned overlapping both sections for visual emphasis
- Bottom breakdown: Full width below, light gray background
- Dividers: Subtle light gray vertical lines (1px) between sections
- White space: 30-35% throughout entire composition
- Padding: 12-16px internal padding in all sections

STYLE:
- Background: PURE WHITE #FFFFFF (NOT cream #F5F5DC, NOT beige)
- Section backgrounds: Light tints (light blue 10% opacity, light coral 10%, light gray 5%)
- Typography: Inter bold for titles/stats, Source Sans regular for details
- Icons: Festival-specific (crowds, phones, location pins, medical symbols, artist notes, stages) NOT generic app UI
- Chart styling: Semi-flat, rounded corners 4-6px, 2px outlines
- Font hierarchy: Title 36pt, section headers 20pt, stats 24-48pt, labels 12-14pt, details 10-12pt
- Minimal decoration (high data-ink ratio)

❌ AVOID:
Cream/beige/off-white backgrounds, generic mobile app UI icons, text <10pt, cramped layouts <25% space, overly complex nested charts, dark/heavy backgrounds, decorative flourishes, graph without context

✅ REFERENCE:
Adoption funnel clearly shows narrowing with visual gap. Notification chart shows time-series with peak emphasis. Callout uses color contrast to create visual hierarchy. Festival context throughout. Professional data-viz style with readable fonts. Balance of data density and white space.
```

---

## Step 3: Review Generated Variants (5 min)

### Quality Checklist

**✅ CRITICAL (Must Pass):**
- [ ] **Pure white background** (#FFFFFF, verify with color picker against black desktop)
- [ ] **Adoption funnel** present (70K → 60K → 12K narrowing)
- [ ] **66% gap** clearly labeled and visually represented (diverging space between steps)
- [ ] **Notification chart** shows 4 bars (Fri, Sat, Sun, Mon) with correct heights
- [ ] **Peak day marked** (Saturday, 32K, visually prominent)
- [ ] **97,000+ total** labeled above chart
- [ ] **12.6 per-user stat** in prominent coral callout (44-48pt minimum)
- [ ] **Notification breakdown** (5 categories, including "ZERO promotional Year 1" callout)
- [ ] **Festival icons** (crowds, phones, location pins, medical, artist symbols) NOT generic
- [ ] **Text legible**: 10pt minimum for details, 12pt+ for labels, 44pt+ for hero stat
- [ ] **White space**: 30%+ of composition, not cramped
- [ ] **Section clarity**: Three distinct sections (funnel, chart, breakdown) visually separated

**✅ STYLE (EventAI Compliance):**
- [ ] Colors match palette: sky blue funnel, coral chart peak, gray breakdown
- [ ] Typography: Inter bold titles, Source Sans regular body
- [ ] Semi-flat design, rounded corners, subtle outlines
- [ ] Professional + accessible mood (data-driven, not blame-focused)
- [ ] Festival visual language throughout

**✅ DATA ACCURACY:**
- [ ] 86% download rate correct
- [ ] 20% engagement rate correct
- [ ] 66% gap accurate
- [ ] 97,000+ notifications total
- [ ] Daily breakdown: 15K, 32K, 28K, 22K
- [ ] 12.6 per-user average accurate
- [ ] Notification categories: 40%, 25%, 20%, 10%, 5% (zero promotional Year 1)

### If Any Variant Fails Checklist

**Background NOT pure white?**
→ Regenerate with "🚨 Background must be EXACTLY #FFFFFF pure white. Use color picker to verify. NOT #F5F5F5, NOT #F5F5DC cream, NOT #FEFDFB. Pure white only."

**Adoption funnel unclear or missing gap?**
→ Regenerate with "Funnel must show 70K → 60K → 12K narrowing. Show large white space (66%) between 86% download and 20% engagement steps. Label the gap prominently on right side."

**Notification chart missing or unclear?**
→ Regenerate with "Bar chart: 4 vertical bars showing daily notifications (Fri: 15K, Sat: 32K peak, Sun: 28K, Mon: 22K). Y-axis 0-35K. Show PEAK label on Saturday. Trend line connecting bar tops."

**12.6 stat not prominent?**
→ Regenerate with "Hero stat '12.6 Notifications Per Engaged User Per Day' must be LARGEST element after title. Bold coral, 44-48pt minimum. Positioned center-right in prominent box."

**Festival icons too generic?**
→ Regenerate with "Use festival-specific icons: concert crowds (dancing), smartphones with app checkmarks, location pins with smiles, medical cross symbols, artist/stage symbols. NO generic business icons, NO office imagery."

**Text too small or hard to read?**
→ Regenerate with "Minimum 10pt for small details, 12-14pt for most labels, 24-28pt for section headers, 44-48pt for hero stat. Print-readable sizes."

**Data numbers wrong?**
→ Verify source file uploaded correctly. Regenerate with "Key stats: 86% downloads, 20% engagement, 66% gap, 97,000 total notifications, 12.6 per user/day, 15K Fri, 32K Sat, 28K Sun, 22K Mon. Notification breakdown: 40% recommendations, 25% friend location, 20% safety, 10% artist info, 5% promotional (ZERO Year 1)."

---

## Step 4: Download & Save (2 min)

### Download All Variants

1. Download each generated variant: Click download icon
2. Format: **PNG** (high resolution, 2000+ pixels wide for landscape)
3. Rename: `personalization-infographic-engagement-metrics-1.png`, `-2.png`, etc.
4. Save to: `docs/writing/3-personalization/visuals/engagement-metrics/`

### Convert to WebP (Optional)

```bash
cd docs/writing/3-personalization/visuals/engagement-metrics
todd-image-convert personalization-infographic-engagement-metrics-*.png --output-format webp --resolution 1080p
```

---

## Step 5: Evaluate & Select Winner (5 min)

### Selection Criteria

**Prioritize variants with:**
1. Pure white background (non-negotiable)
2. Clear adoption funnel with prominent gap visualization
3. Notification chart with visible peak on Saturday
4. Large, readable 12.6 stat in prominent callout
5. Festival-specific icons throughout
6. Good white space (30%+ minimum)
7. Readable text (10pt minimum for smallest text)

### Expected Quality

**Strong variants:** 75-85/100 if:
- Funnel clear, gap prominent
- Chart shows time-series with peak
- Callout visually striking
- Festival context throughout
- Data accurate

---

## File Deliverables

- ✅ `personalization-infographic-engagement-metrics-{N}.png` (high-res PNG)
- ✅ `personalization-infographic-engagement-metrics-{N}.webp` (web-optimized, optional)
- ✅ Winner selected and documented

---

## Troubleshooting Common Issues

### 🔴 Adoption funnel unclear or missing gap visualization

**Problem**: Funnel shown as smooth narrowing without highlighting the drop from 86% to 20%
**Solution**: Regenerate with "Show dramatic narrowing from step 1 (60K downloads, 86%) to step 2 (12K engaged, 20%). Display large white gap between steps. Label right side: '66 Percentage Point Gap' with annotation of reasons (privacy, battery, fatigue)."
**Prevention**: Emphasize "gap visualization" in prompt, specify "white space shows missing 48K users"

### 🔴 Notification chart doesn't show peak

**Problem**: All bars similar height, Saturday peak not visually obvious
**Solution**: Regenerate with "Saturday bar (32K) must be visually prominent: darkest color, largest height, 'PEAK' label, largest text. Friday/Sunday/Monday bars noticeably shorter. Peak must jump out visually."
**Prevention**: Specify exact heights and visual emphasis ("darkest color," "PEAK label")

### 🔴 12.6 stat not prominent enough

**Problem**: Callout exists but stat not hero-sized
**Solution**: Regenerate with "The stat '12.6 Notifications Per Engaged User Per Day' must be LARGEST single number in entire infographic (44-48pt bold, coral color). It's the key insight. Make it impossible to miss."
**Prevention**: Explicitly state "hero stat" and size requirements

### 🔴 66% gap not explained

**Problem**: Gap shown but reasons not visible
**Solution**: Regenerate with "Next to 66% gap label, add explanation box: 'Why? Privacy concerns (40%), Battery drain (20%), Notification fatigue (15%), Feature discovery (15%), Other (10%)' in gray 12pt text. Explain the gap, don't just show it."
**Prevention**: Include explanation annotation in prompt

### 🔴 Notification category breakdown confusing

**Problem**: 5 categories hard to distinguish or understand
**Solution**: Regenerate with "Notification breakdown must be crystal clear: 5 distinct categories each with label + percentage + detail. Use color coding. Include key insight: 'ZERO promotional messages in Year 1 (trust-building strategy). Even non-commercial messages caused fatigue.'"
**Prevention**: Specify colors for each category, emphasize the Year 1 zero-promotional insight

---

## Key Learnings (Adaptation from VIS-1.3)

**What Works:**
- ✅ Comparison layouts (two stories side-by-side)
- ✅ Funnel visualization (narrowing shows impact)
- ✅ Time-series bar charts (peak visualization)
- ✅ Festival context icons (builds credibility)
- ✅ Bold statistics in callouts (creates emphasis)

**What to Avoid:**
- ❌ Pure white background non-negotiable
- ❌ Generic business icons (reduces credibility)
- ❌ Cramped layouts (white space creates professional appearance)
- ❌ Missing context/explanation (data needs narration)
- ❌ Small text (readability critical for infographics)

---

## Token-Optimized Quick Commands

**Full workflow one-liners:**

```bash
# After downloading PNGs:
todd-image-convert docs/writing/3-personalization/visuals/engagement-metrics/*.png --output-format webp --resolution 1080p

# Evaluation (if tools available):
/ig-evaluate docs/writing/3-personalization/visuals/engagement-metrics/*.webp
```

---

## Expected Outcomes

### What Success Looks Like

**Adoption Funnel:**
- Narrowing visual from 70K → 60K → 12K
- Large white gap between steps 1 and 2 showing 66% drop
- Gap reasons annotated (privacy, battery, fatigue, discovery)
- Sky blue color coding for adoption section

**Notification Chart:**
- 4 bars showing daily volume (Fri 15K, Sat 32K peak, Sun 28K, Mon 22K)
- Saturday peak visually obvious (darkest, tallest, "PEAK" label)
- Total "97,000+ Notifications" labeled above
- Per-user averages shown (2.5, 5.3, 4.7, 3.7)
- Coral color coding for chart section

**Hero Callout:**
- Large coral box, white text
- "12.6 Notifications Per Engaged User Per Day" (44-48pt bold)
- "66% Downloaded But Didn't Engage" (28pt bold)
- Context annotation explaining why

**Notification Breakdown:**
- 5 categories with colors and percentages
- Key insight: "ZERO promotional Year 1 (trust-building strategy)"
- Shows that even non-commercial messages caused fatigue

**Overall:**
- Pure white background
- Festival context icons throughout
- 30%+ white space
- Print-ready resolution
- 100% data accuracy

---

## Next Steps After Successful Generation

### 1. Save to Visuals Folder

Filename: `personalization-infographic-engagement-metrics-{variant}.png`

### 2. Update Visual Content Plan

Mark VIS-3.2 complete in `VISUAL-CONTENT-PLAN.md`:
```markdown
- ✅ VIS-3.2: Engagement metrics (Bonnaroo case study, Variant #X, Dec 29 2025)
```

### 3. Reference in Draft

Add to section 3-personalization text:
```markdown
![Bonnaroo iBeacon Engagement Metrics](../visuals/engagement-metrics/personalization-infographic-engagement-metrics-X.webp)
```

### 4. Move to Next Visual

Proceed to **VIS-3.3: Helpful vs. Intrusive Features** (helpful-intrusive folder)

---

## Related Documentation

- [Engagement Metrics Content](engagement-metrics.content.md) - Full source material
- [EventAI Visual Identity](../../../lemmy/style-guide/eventai-visual-identity.md) - Brand standards
- [Visual Content Plan](../../VISUAL-CONTENT-PLAN.md) - All planned visuals

---

*VIS-3.2 Generation Package - Ready for NotebookLM*
*Token-optimized prompt: 284 tokens*
*Bonnaroo case study: adoption-engagement gap + notification fatigue*
*Expected generation time: 15-20 minutes for 3-5 variants*
