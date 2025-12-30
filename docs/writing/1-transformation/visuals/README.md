# Transformation Topic - Visual Assets

**Topic**: AI's Long-term Future Vision (2025-2035)
**Question**: What is the ultimate, long-term future of AI in festivals over the next decade?

This folder contains visual assets for the Transformation topic, including infographics, diagrams, and illustrations generated using the Lemmy multi-AI content generation system.

---

## Visual Content Plan

### VIS-1.1: AI Adoption Timeline (2025-2035) ✅ READY TO GENERATE

**Type**: Timeline Infographic
**Platform**: NotebookLM
**Status**: Test package prepared, ready for generation

**Files**:
- `VIS-1.1-source.md` - Focused source document for NotebookLM upload
- `VIS-1.1-GENERATE-INSTRUCTIONS.md` - Complete step-by-step generation guide
- `transformation-infographic-adoption-timeline.png` - Generated infographic (after creation)

**What it shows**:
- Three-phase AI adoption progression (2025-2035)
- Dual lines: Major festivals vs Small festivals
- Key milestones and statistics for each phase
- Percentage adoption rates over time

**Estimated generation time**: ~17 minutes

**To generate**: Follow instructions in `VIS-1.1-GENERATE-INSTRUCTIONS.md`

---

### VIS-1.2: Before/After Comparison ✅ READY TO GENERATE

**Type**: Comparative Infographic
**Platform**: NotebookLM
**Status**: Test package prepared, ready for generation

**Files**:
- `VIS-1.2-source.md` - Focused source document for NotebookLM upload
- `VIS-1.2-GENERATE-INSTRUCTIONS.md` - Complete step-by-step generation guide
- `transformation-infographic-before-after.png` - Generated infographic (after creation)

**What it shows**: Side-by-side comparison of traditional vs AI-optimized festival experiences across three key dimensions:
- **Discovery & Ticketing**: Manual browsing vs AI recommendations (40-41% of sales now algorithmic)
- **On-Site Experience**: Paper maps vs real-time apps (20% engagement with contextual notifications)
- **Post-Festival**: Manual photos vs AI-generated recaps (with privacy opt-in requirements)

**Key statistics**:
- 40-41% ticket sales via AI recommendations
- 20% engagement rate with contextual notifications
- 44-56% users decline notification permissions when asked explicitly

**Privacy focus**: Clearly shows which features require opt-in, balances benefits with privacy considerations

**Estimated generation time**: ~15 minutes

**To generate**: Follow instructions in `VIS-1.2-GENERATE-INSTRUCTIONS.md`

---

### VIS-1.3: Adoption Barriers

**Type**: Data Visualization
**Platform**: NotebookLM or Nano Banana
**Status**: 📋 Planned

**What it shows**: Key barriers preventing AI adoption (cost, complexity, privacy concerns, ROI uncertainty) with percentage breakdowns

---

### VIS-1.4: Key Capabilities Evolution

**Type**: Feature Comparison Matrix
**Platform**: NotebookLM
**Status**: 📋 Planned

**What it shows**: Evolution of AI capabilities across three phases (Foundation, Mainstream, Adaptive), showing what becomes standard in each era

---

## Generation Workflow

### For NotebookLM Infographics

1. **Prepare source**: Extract relevant content into focused markdown file
2. **Upload to NotebookLM**: Create notebook, add source
3. **Apply EventAI style**: Use customization prompt with style guide
4. **Generate**: Select detail level and orientation
5. **Download & Save**: Rename according to convention, save to this folder

**Detailed workflow**: [../../../lemmy/workflows/notebooklm-workflows.md](../../../lemmy/workflows/notebooklm-workflows.md)

### For Nano Banana Diagrams

1. **Select template**: Choose from nano-banana.prompt.md
2. **Fill template**: Replace placeholders with specific content
3. **Generate**: Use Google AI Studio (Imagen 3 or Nano Banana Pro)
4. **Download & Save**: High-res PNG to this folder

**Detailed workflow**: [../../../lemmy/workflows/nano-banana-workflows.md](../../../lemmy/workflows/nano-banana-workflows.md)

---

## File Naming Convention

### Image Files
**Format**: `{topic}-N.{ext}`

**Examples**:
- `timeline-1.png`, `timeline-2.png`, `timeline-3.png` (VIS-1.1)
- `before-after-1.png`, `before-after-2.png`, `before-after-3.png` (VIS-1.2)
- `barriers-1.png` through `barriers-6.png` (VIS-1.3)
- `capabilities-1.png`, `capabilities-2.png`, `capabilities-3.png` (VIS-1.4)

### Documentation Files
**Format**: `{topic}.{type}.md`

**Types**:
- `.content.md` - Source material/data for NotebookLM upload
- `.prompt.md` - Raw NotebookLM prompt (token-optimized, no framing)
- `.instructions.md` - Workflow guidance and generation steps
- `.eval.md` - Evaluation report from /ig-evaluate

**Examples**:
- `barriers.content.md`, `barriers.prompt.md`, `barriers.instructions.md`, `barriers.eval.md`
- `timeline.content.md`, `timeline.prompt.md`, `timeline.instructions.md`

---

## Token Optimization Requirements

**🚨 CRITICAL**: `.content.md` and `.prompt.md` files MUST be token-optimized before upload to AI agents (NotebookLM, Claude, etc.)

### Why This Matters
- AI models charge per token consumed
- NotebookLM has context limits that benefit from compact source material
- Verbose content increases costs and may hit limits unnecessarily
- Token-optimized content preserves ALL information while reducing waste

### Target Metrics
- ✅ **Token reduction**: 40-70% from verbose original
- ✅ **Information preservation**: 100% of substantive points
- ✅ **Readability**: High (scannable, clear structure)
- ✅ **Completeness**: All facts, stats, technical details intact

### Optimization Strategies

**Rephrase for conciseness**:
- Verbose → terse, information-dense phrasing
- Example: "You should ensure that the background color is exactly pure white" → "Background: Pure white #FFFFFF"

**Use fragments over sentences**:
- Bullet points and fragments instead of prose
- Strip unnecessary articles (a, an, the)
- Remove transitions ("In conclusion," "As mentioned," "It's important that")

**Consolidate and deduplicate**:
- Group related concepts together
- Eliminate redundancy across sections
- Use hierarchical bullets to show relationships

**Remove fluff, preserve substance**:
- ❌ Remove: Filler words (very, really, quite, actually, basically)
- ❌ Remove: Redundant examples (keep most illustrative only)
- ❌ Remove: Excessive context or marketing language
- ✅ Preserve: Unique facts, numbers, dates, statistics
- ✅ Preserve: Technical details (hex codes, point sizes, measurements)
- ✅ Preserve: Decision criteria, warnings, recommendations
- ✅ Preserve: Source attributions and citations

### File-Specific Guidelines

**`.content.md` files** (source material):
- Compress narrative sections by 50-60%
- Preserve all data points, statistics, examples
- Use tables/lists instead of prose where possible
- Keep section headers for structure

**`.prompt.md` files** (NotebookLM prompts):
- Compress by 40-55%
- Preserve ALL technical specifications (colors, sizes, layout details)
- Keep markdown headers (# ##) for implicit structure
- Remove all explanatory framing ("This prompt will...", "Make sure to...")
- Keep only the directive content AI needs to execute

### Quality Verification

Before committing optimized files, verify:
- [ ] No substantive information lost
- [ ] All numbers, stats, technical specs preserved
- [ ] Markdown structure clean and readable
- [ ] 40-70% token reduction achieved
- [ ] File scans quickly (test by reading it yourself)

### Token Estimation
- 1 token ≈ 4 characters in English text
- Use `/optimize-tokens` command to apply optimization principles
- Count approximate tokens: `wc -m file.md` divided by 4

---

## EventAI Style Standards

All visuals must comply with EventAI visual identity:

### Colors
- **Deep purple** (#6B46C1) - primary brand, AI elements
- **Electric coral** (#FF6B6B) - emphasis, key statistics
- **Sky blue** (#4299E1) - data, comparisons
- **Midnight slate** (#2D3748) - body text
- **Clean white background**

### Typography
- **Headings**: Inter (bold, 24-36pt)
- **Body**: Source Sans Pro (regular, 14-16pt)
- **Data**: Inter (bold, 48-72pt for key numbers)

### Design Principles
- Semi-flat style with subtle depth
- Rounded corners (8-12px radius)
- 2-3px outlines for clarity
- Minimal decoration (high data-ink ratio)
- Festival context (stages, crowds, wristbands)
- Professional yet energetic mood

**Full guide**: [../../../lemmy/style-guide/eventai-visual-identity.md](../../../lemmy/style-guide/eventai-visual-identity.md)

---

## Quality Checklist

Before marking visual complete:

✅ **Factual Accuracy**: All data verified against source documents
✅ **EventAI Style**: Colors, typography, design match style guide
✅ **Festival Context**: Industry-specific imagery, not generic
✅ **Accessibility**: WCAG AA contrast, readable text sizes
✅ **File Management**: Named correctly, saved to this folder
✅ **Documentation**: Status updated in VISUAL-CONTENT-PLAN.md

---

## Related Documentation

- **Main Draft**: [../drafts/transformation.draft.md](../drafts/transformation.draft.md)
- **Visual Content Plan**: [../../VISUAL-CONTENT-PLAN.md](../../VISUAL-CONTENT-PLAN.md)
- **Lemmy Workflows**: [../../../lemmy/workflows/](../../../lemmy/workflows/)
- **EventAI Style Guide**: [../../../lemmy/style-guide/eventai-visual-identity.md](../../../lemmy/style-guide/eventai-visual-identity.md)

---

*Visual Assets Folder for Transformation Topic*
*Last Updated: December 28, 2025*
*Part of: EventAI Curriculum + Lemmy Content Generation System*
