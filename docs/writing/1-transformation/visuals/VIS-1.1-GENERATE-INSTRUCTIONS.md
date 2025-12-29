# VIS-1.1: AI Adoption Timeline - NotebookLM Generation Instructions

**Test Infographic**: AI Adoption Timeline (2025-2035)
**Status**: Ready to generate
**Estimated time**: ~17 minutes

---

## Step 1: Upload Source to NotebookLM (2 min)

1. **Go to NotebookLM**: [https://notebooklm.google.com/](https://notebooklm.google.com/)
2. **Create new notebook**: Click "+ New notebook" or "New"
3. **Name it**: `EventAI - Transformation Timeline Test`
4. **Upload source**:
   - Click "Add sources" or drag-and-drop
   - Upload file: `VIS-1.1-source.md` (this folder)
   - Wait for processing (~10-30 seconds)

---

## Step 2: Generate Infographic (10 min)

### Access Infographic Feature

1. Click **"Infographic"** option in content generation menu
2. Or find "Create infographic" button

### Configuration

**Detail Level**: **Detailed** (recommended for comprehensive timeline)

**Orientation**: **Landscape** (optimal for timeline format)

### Customization Prompt

**Copy and paste this entire prompt into the NotebookLM customization field:**

```
Create a comprehensive timeline infographic showing AI adoption in the festival industry from 2025 to 2035.

VISUAL STRUCTURE:
- Horizontal timeline spanning 2025 to 2035
- Two ascending line graphs:
  * Solid line: Major festivals (10,000+ attendees)
  * Dashed line: Small festivals (under 5,000 attendees)
- Three distinct phase sections with vertical dividers at 2028 and 2032
- Y-axis: Adoption percentage (0-100%)
- X-axis: Years (2025, 2028, 2032, 2035)

DATA POINTS TO PLOT:
Major Festivals Line (solid, deep purple):
- 2025: 45%
- 2028: 67.5%
- 2032: 87.5%
- 2035: 95%

Small Festivals Line (dashed, sky blue):
- 2025: 45%
- 2028: 30%
- 2032: 55%
- 2035: 72.5%

PHASE LABELS (above timeline, bold):
1. "Phase 1: Foundation Building (2025-2028)"
2. "Phase 2: Mainstream Integration (2028-2032)"
3. "Phase 3: Adaptive Ecosystems (2032-2035)"

MILESTONE CALLOUTS (beside timeline, connected with lines):
- 2025: "EU AI Act effective • DICE 40% AI-driven sales • $1.8B market"
- 2028: "70% major festival adoption • 5G infrastructure mature • Vendor consolidation"
- 2032: "AI = baseline expectation • Cross-festival identity • 10-15% margin gains"
- 2035: "95% major adoption • AI becomes commodity • Adaptive ecosystems"

EMPHASIS:
- The 95% endpoint at 2035 should be the largest visual element (electric coral, 56pt)
- Phase transition points (2028, 2032) should be clearly marked
- The ascending curves should be the dominant visual element

EVENTAI VISUAL STYLE:
Colors:
- Deep purple (#6B46C1): Major festival line, phase labels, primary elements
- Electric coral (#FF6B6B): 95% endpoint emphasis, key statistics
- Sky blue (#4299E1): Small festival line, supporting data
- Warm sunlight (#F6AD55): Phase transition dividers
- Midnight slate (#2D3748): Axis labels, milestone text
- Clean white background

Typography:
- Title: "AI Adoption Timeline: Festivals 2025-2035" in bold Inter, 36pt, deep purple
- Phase labels: Bold Inter, 20pt, deep purple
- Data labels at points: Bold Inter, 18pt (percentage) + 14pt (year)
- Final 95% label: Extra bold Inter, 56pt, electric coral
- Milestone callouts: Source Sans Pro, 14pt, midnight slate
- Axis labels: Source Sans Pro, 12pt, mid gray

Design:
- Semi-flat style with subtle depth (not 3D)
- Rounded corners on all shapes (8px radius)
- 2-3px line weight for graph lines
- Subtle horizontal grid lines at 25%, 50%, 75%, 100% (1px, light gray)
- Clean composition, generous white space
- High data-ink ratio (minimal decoration)

Festival Context:
- Include small simplified stage icons at each data point on major festival line
- Stages should increase in detail/complexity from 2025 → 2035 (suggesting evolution)
- Subtle RFID wristband symbols at phase transition points
- Crowd silhouette growing in background (left to right) suggesting increasing adoption

Layout:
- Title at top center
- Timeline occupies central 70% of canvas
- Phase labels above timeline
- Milestone callouts to right side of timeline (avoiding line overlap)
- Source citation bottom right: "Source: Industry surveys (2024), Market research, EU AI Act (2025), DICE (2025)"
- Legend bottom left: Line styles for Major/Small festivals

Professional yet energetic mood:
- Clean, evidence-based visualization
- Festival industry context (not generic business chart)
- Optimistic progression but grounded in data
- Appropriate for academic and professional audiences

AVOID:
- Generic business imagery (suits, offices, corporate charts)
- Clichéd AI imagery (robots, circuit brains)
- Overly complex 3D effects
- Clutter or unnecessary decorative elements
```

### Generate

1. Click **"Generate Infographic"**
2. Wait **1-2 minutes** (Nano Banana Pro processing)
3. Image will appear when ready

---

## Step 3: Review & Download (5 min)

### Quality Checklist

✅ **Data Accuracy**:
- [ ] All percentages match source (45%, 67.5%, 87.5%, 95% for major)
- [ ] Years labeled correctly (2025, 2028, 2032, 2035)
- [ ] Phase labels match three phases
- [ ] Milestone callouts present and accurate

✅ **EventAI Style**:
- [ ] Colors match palette (deep purple, electric coral, sky blue)
- [ ] Typography readable (Inter headings, Source Sans Pro body)
- [ ] 95% endpoint emphasized in electric coral
- [ ] Clean white background, minimal decoration

✅ **Festival Context**:
- [ ] Stage icons visible at data points
- [ ] Not generic business imagery
- [ ] Professional yet energetic mood

✅ **Accessibility**:
- [ ] Text legible at intended display size
- [ ] High contrast between text and background
- [ ] Legend clearly distinguishes major/small festivals

### If Unsatisfactory

**Option 1**: Regenerate with same prompt (may get variation)
**Option 2**: Adjust prompt to be more specific about problematic element
**Option 3**: Try different detail level (Brief or Comprehensive)

Generate **2-3 variations** and select best.

---

## Step 4: Download & Save (2 min)

### Download

1. Click download icon (down arrow)
2. File format: **PNG** (high resolution)
3. Save to your computer

### Rename and Move

1. **Rename file**: `transformation-infographic-adoption-timeline.png`
2. **Move to**: `docs/writing/1-transformation/visuals/` (this folder)

### Verify Quality

1. Open in image viewer
2. Check resolution (should be high-res, print-ready)
3. Zoom in to verify text is crisp
4. Check colors display correctly

---

## Step 5: Documentation (1 min)

### Update Status

Mark VIS-1.1 as complete in [VISUAL-CONTENT-PLAN.md](../../VISUAL-CONTENT-PLAN.md):
- Change status from 📋 to ✅
- Note any variations generated
- Record generation date

### Optional: Reference in Draft

Add to [transformation.draft.md](../drafts/transformation.draft.md) after "The Adoption Timeline: 2025-2035" section:

```markdown
![AI Adoption Timeline (2025-2035)](../visuals/transformation-infographic-adoption-timeline.png)
```

---

## Expected Outcome

### What You Should Have

**File**: `transformation-infographic-adoption-timeline.png`

**Content**:
- Horizontal timeline infographic (landscape orientation)
- Two ascending lines showing adoption progression
- Three phase sections clearly delineated
- Key milestones and statistics labeled
- EventAI visual style (purple, coral, blue on white)
- Festival context (stage icons, wristbands)
- Professional yet energetic presentation

**File size**: Likely 2-5 MB (high-resolution PNG)

**Resolution**: Print-ready (minimum 2400x1800px)

---

## Troubleshooting

### Problem: Infographic doesn't match EventAI style

**Solution**:
- Ensure entire customization prompt was copied (including style section)
- Regenerate with emphasis on "EventAI festival industry style"
- Reference exact hex codes in prompt

### Problem: Data points incorrect

**Solution**:
- Check source document has correct percentages
- Regenerate with more explicit data point listing in prompt
- Verify NotebookLM processed source correctly

### Problem: Timeline layout unclear

**Solution**:
- Try "Comprehensive" detail level for more elements
- Regenerate with more specific layout guidance in prompt
- Emphasize "horizontal timeline" and "ascending line graph"

### Problem: Text not legible

**Solution**:
- Regenerate requesting larger font sizes
- Specify minimum text size (14pt body, 24pt emphasis)
- Ensure high-resolution output

---

## Next Steps After Success

🎉 **Congratulations!** You've generated your first EventAI infographic!

### Continue with More Visuals

**Transformation topic** has 4 total infographics planned:
- ✅ VIS-1.1: AI Adoption Timeline (complete!)
- 📋 VIS-1.2: Before/After Comparison
- 📋 VIS-1.3: Adoption Barriers
- 📋 VIS-1.4: Key Capabilities Evolution

Follow same workflow for each:
1. Use existing or create source document
2. Apply EventAI style prompt
3. Generate in NotebookLM
4. Download and save

### Scale to Full Visual Content Plan

**20 total infographics** planned across 5 topics:
- See [VISUAL-CONTENT-PLAN.md](../../VISUAL-CONTENT-PLAN.md) for complete list

**Estimated total time**: ~5-6 hours for all 20 infographics (17 min each average)

---

## Related Documentation

- **NotebookLM Workflow**: [../../../lemmy/workflows/notebooklm-workflows.md](../../../lemmy/workflows/notebooklm-workflows.md)
- **Infographic Prompt Template**: [../../../lemmy/prompts/notebooklm/infographic.prompt.md](../../../lemmy/prompts/notebooklm/infographic.prompt.md)
- **EventAI Style Guide**: [../../../lemmy/style-guide/eventai-visual-identity.md](../../../lemmy/style-guide/eventai-visual-identity.md)
- **Visual Content Plan**: [../../VISUAL-CONTENT-PLAN.md](../../VISUAL-CONTENT-PLAN.md)

---

*Test Infographic Generation Package*
*Created: December 28, 2025*
*Part of: Lemmy Multi-AI Content Generation System*
*Ready to generate - follow steps above!*
