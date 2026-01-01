# VIS-2.3: The 71% Skills Gap Cycle - Generation Instructions

**Infographic**: Circular flow diagram showing the self-reinforcing cycle perpetuating the AI skills gap
**Status**: 📋 READY TO GENERATE
**Estimated time**: ~15-20 minutes

---

## Quick Start: NotebookLM Workflow

### Step 1: Upload Source (2 min)

1. Go to [NotebookLM](https://notebooklm.google.com/)
2. Create notebook: `EventAI - Education - Skills Gap Cycle`
3. Upload: `skills-gap-cycle.content.md` (this folder)
4. Wait for processing (~30 sec)

### Step 2: Generate Infographic (10-15 min)

1. Click **"Infographic"** in generation menu
2. Settings:
   - **Detail Level**: Standard
   - **Orientation**: Square (portrait optimized)
3. **Paste prompt**: Use `skills-gap-cycle.prompt.md` (this folder)
4. Click **"Generate"**
5. Wait ~2 min for Nano Banana processing
6. **Generate 3 variations** (click regenerate 2 more times)

### Step 3: Quality Check (3-5 min)

For each variant, check:

**Visual Hierarchy & Layout**:
- ✅ Clear circular flow with 5 distinct stages
- ✅ Arrows showing cycle direction and reinforcement
- ✅ Center callout ("The Paradox") visually prominent and separated
- ✅ Headers distinct from body text
- ✅ Key stat (71%) prominently displayed and readable
- ✅ All 5 statistics visible (71%, 42%, 0%, 3%, 18-24 months, 100%)

**Circular Diagram Quality**:
- ✅ Five stages clearly labeled and spaced evenly
- ✅ Arrows create clear directional flow
- ✅ Cycle reinforcement visually apparent (arrows cycling back)
- ✅ Not linearized—maintains circular integrity
- ✅ All five stages present: Industry → University → Graduate → Vendor → Failures

**Factual Accuracy**:
- ✅ Stage 1: "Universities don't teach AI, we train in-house"
- ✅ Stage 2: "Industry changes too fast, we can't keep up"
- ✅ Stage 3: "Graduates lack functional AND critical AI literacy"
- ✅ Stage 4: "On-the-job learning (incentivized to oversell)"
- ✅ Stage 5: "42% zero ROI, GDPR fines, wrongful arrests"
- ✅ Skills gap: 71%
- ✅ Zero ROI: 42%
- ✅ UK coverage: 0%
- ✅ Global coverage: 3/100+ programs (3%)
- ✅ Curriculum cycle: 18-24 months
- ✅ Vendor training: 100% sales-focused

**EventAI Style Compliance**:
- ✅ Background: Pure white #FFFFFF (NOT beige/cream/off-white)
- ✅ Colors: Purple #6B46C1 (cycle flow), Coral #FF6B6B (failures), Blue #4299E1 (central insight)
- ✅ Typography: Inter bold headers, Source Sans Pro body
- ✅ Festival context icons ONLY (stages, wristbands, crowds, apps—NO gears/money bags)
- ✅ White space ≥30%
- ✅ Rounded corners 8-12px
- ✅ Semi-flat with subtle depth
- ✅ Professional + whimsy balance
- ✅ High data-ink ratio

**Accessibility**:
- ✅ Text readable at 13-15pt minimum
- ✅ WCAG AA contrast ratios met
- ✅ Circular flow clear without relying on color alone
- ✅ Labels + icons clarify meaning (not color-dependent)
- ✅ Sufficient white space for readability

**Festival/Event Context**:
- ✅ Real-world examples relevant to event professionals
- ✅ Icons show actual event scenarios (not generic business imagery)
- ✅ Impact on attendee experience evident
- ✅ Sponsorship/vendor angle clear

### Step 4: Save (2 min)

1. **Select best variant** (or top 2-3 for comparison)
2. Download high-resolution PNG
3. Save as: `skills-gap-cycle-1.png`, `skills-gap-cycle-2.png`, etc.
4. Place in this folder

### Step 5: Evaluate (Optional)

Use `/ig-evaluate` command to assess quality:
```bash
/ig-evaluate skills-gap-cycle-1.png
```

This will generate `skills-gap-cycle.eval.md` with detailed scoring.

---

## Alternative: Nano Banana Direct (if NotebookLM unavailable)

### Option A: Google AI Studio

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Select **Imagen 3** model
3. Paste the full prompt from `skills-gap-cycle.prompt.md`
4. Generate 3-4 variations
5. Download best result

### Option B: Gemini API (Programmatic)

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

with open("skills-gap-cycle.prompt.md") as f:
    prompt = f.read()

model = genai.GenerativeModel('imagen-3.0-generate-001')
response = model.generate_images(
    prompt=prompt,
    number_of_images=4,
    safety_filter_level="block_only_high",
    aspect_ratio="1:1"  # Square for circular diagram
)

for i, image in enumerate(response.images):
    image.save(f"skills-gap-cycle-{i+1}.png")
```

---

## Common Issues & Fixes

### Issue: Linearized instead of circular
**Fix**: Add to prompt: "MUST be circular flow diagram with arrows creating a reinforcing cycle, not linear. Five stages arranged in circle around center callout."

### Issue: Beige/cream background instead of pure white
**Fix**: Add to prompt: "Background color: Pure white #FFFFFF (NOT cream, NOT beige, NOT off-white, NOT off-white)"

### Issue: Generic business icons (gears, money bags, lightbulbs)
**Fix**: Add: "Festival/event imagery ONLY: event stages, wristbands, mobile apps, crowd scenes, venue maps, ticket scanners. NO generic corporate icons."

### Issue: Missing or unreadable key statistics
**Fix**: Add: "MUST display these stats prominently: 71% skills gap (largest, most visible), 42% zero ROI, 0% UK coverage, 3% global (3/100+), 18-24 months curriculum cycle, 100% sales-focused"

### Issue: Center callout not visually distinct
**Fix**: Add: "Center callout box must be visually separated from the cycle with strong border/background color contrast. Use blue #4299E1 for high prominence."

### Issue: Stages not clearly labeled or hard to follow
**Fix**: Add: "Each of 5 stages must have clear headline text, numbered labels (1-5), and 2-3 supporting detail points. Arrows must show directional flow."

### Issue: Coral color not prominent enough for failures
**Fix**: Add: "Stage 5 (Failures) and Vendor Training (Stage 4): Use coral #FF6B6B prominently. These stages must visually stand out as problematic/urgent."

### Issue: Too cluttered or text-heavy
**Fix**: Reduce detail level to "Concise" OR add: "White space ≥30%. Use visual hierarchy: headlines ≥24pt, body text 13-15pt. Minimize text density."

### Issue: Missing the "paradox" insight
**Fix**: Add: "Center callout must clearly articulate the paradox: Industry says 'universities don't teach this,' universities say 'industry doesn't demand this,' creating a self-reinforcing cycle."

---

## Expected Output Quality

**Target Scores** (from /ig-evaluate):
- Visual Clarity: 85-95/100
- Information Accuracy: 90-100/100 (all stats correct, cycle logic clear)
- Circular Flow: 85-95/100 (not linearized)
- EventAI Style: 80-95/100
- Accessibility: 80-90/100
- Overall: 85-95/100

**Acceptable Range**: 80-100 (most categories)
**Red Flags**: <70 in any category requires regeneration

---

## Specific Quality Checkpoints

### Circular Flow Quality
- Diagram must form a complete circle or polygon
- Five stages evenly distributed around the circumference
- Arrows flowing in one direction around the circle
- Feedback loop clearly visible (arrows returning to start)
- No linearization (not a left-to-right sequence)

### Central Insight Quality
- "The Paradox" box must be visually distinct
- Text must articulate the self-reinforcing nature
- Must connect to all five stages conceptually
- Should be positioned centrally, not off to the side

### Real-World Context Quality
- Examples must be event/hospitality-specific
- Impact on event professionals must be clear
- Not generic business use cases
- Festival/event imagery throughout

---

## Next Steps After Generation

1. ✅ Save best variant(s) to this folder
2. ✅ Run `/ig-evaluate` to document quality
3. ✅ Convert to WebP using `/todd-image-convert` for web use
4. ✅ Update status in `../../README.md`
5. ✅ Reference in education draft: `![The 71% Skills Gap Cycle](visuals/skills-gap-cycle/skills-gap-cycle-1.png)`

---

## Troubleshooting Tips

**If regeneration needed**:
1. Save the failed attempt with descriptive name: `skills-gap-cycle-failed-linear.png`
2. Review which quality checks failed
3. Add specific fixes to the prompt
4. Regenerate with updated prompt
5. Document what worked in this instructions file

**If stats are wrong**:
1. Verify source data in `skills-gap-cycle.content.md`
2. Add exact stat values to prompt
3. Consider simplifying: remove non-essential stats if too cluttered

**If circular layout doesn't work**:
1. Try specifying "Pentagon or hexagon" instead of free-form circle
2. Add: "Five segments labeled Stage 1-5, arranged in geometric circle"
3. Consider slightly larger canvas to give more room

---

## Related Files

- [skills-gap-cycle.content.md](./skills-gap-cycle.content.md) - Full source material
- [skills-gap-cycle.prompt.md](./skills-gap-cycle.prompt.md) - Token-optimized prompt
- [../../README.md](../../README.md) - Education section visual overview
- [../literacy-comparison/literacy-comparison.instructions.md](../literacy-comparison/literacy-comparison.instructions.md) - Similar workflow for comparison infographic

**Part of**: EventAI Curriculum - Topic 2: Education
**Last Updated**: December 29, 2025
