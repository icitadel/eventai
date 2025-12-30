# Education Topic - Visual Assets

**Topic**: Critical AI Literacy
**Question**: How should event professionals be educated about AI—functionally and critically?

This folder contains visual assets for the Education topic, including infographics, diagrams, and illustrations generated using the Lemmy multi-AI content generation system.

---

## Visual Content Plan

### VIS-2.1: Functional vs. Critical AI Literacy ✅ READY TO GENERATE

**Type**: Comparison Infographic
**Platform**: NotebookLM
**Status**: Placeholder files prepared, ready for generation

**Files**:
- `literacy-comparison/literacy-comparison.content.md` - Source material for NotebookLM
- `literacy-comparison/literacy-comparison.prompt.md` - Token-optimized prompt
- `literacy-comparison/literacy-comparison.instructions.md` - Generation workflow
- `literacy-comparison/literacy-comparison-1.png` - Generated infographic (after creation)

**What it shows**: Side-by-side comparison distinguishing functional literacy (tool usage) from critical literacy (system evaluation):
- **Functional**: MPI/PCMA certificates (7.5 hrs, $300-700), vendor training, prompt engineering
- **Critical**: Proposed 15-week course, GDPR/EU AI Act, algorithmic bias, ethical frameworks
- **The Gap**: 71% skills gap, 42% zero ROI, vendor-only training creates evaluation blindness

**Key statistics**: 7.5 hrs vs 15 weeks, $300-700, 71% skills gap, 42% zero ROI, 3% academic coverage

**Estimated generation time**: ~15-20 minutes

**To generate**: Follow instructions in `literacy-comparison/literacy-comparison.instructions.md`

---

### VIS-2.2: Academic AI Integration Map ✅ READY TO GENERATE

**Type**: Conceptual Disparity Diagram
**Platform**: NotebookLM or Nano Banana
**Status**: Placeholder files prepared, ready for generation

**Files**:
- `academic-integration/academic-integration.content.md` - Source material
- `academic-integration/academic-integration.prompt.md` - Token-optimized prompt
- `academic-integration/academic-integration.instructions.md` - Generation workflow
- `academic-integration/academic-integration-1.png` - Generated infographic (after creation)

**What it shows**: Visual representation of 3% academic AI coverage:
- **3 universities WITH AI**: Surrey (UK), Southern Cross (Australia), Penn State (US) - lit up/prominent
- **100+ programs WITHOUT AI**: Leeds Beckett UKCEM, UCF Rosen, hundreds more - faded/darkened
- **The vicious cycle**: University/industry blame loop resulting in graduates lacking both literacies

**Key statistics**: 3/100+ = 3%, 97% teach ZERO AI, 71% skills gap

**Estimated generation time**: ~15-20 minutes

**To generate**: Follow instructions in `academic-integration/academic-integration.instructions.md`

---

### VIS-2.3: The 71% Skills Gap Cycle ✅ READY TO GENERATE

**Type**: Circular/Cyclical Diagram
**Platform**: NotebookLM
**Status**: Placeholder files prepared, ready for generation

**Files**:
- `skills-gap-cycle/skills-gap-cycle.content.md` - Source material
- `skills-gap-cycle/skills-gap-cycle.prompt.md` - Token-optimized prompt
- `skills-gap-cycle/skills-gap-cycle.instructions.md` - Generation workflow
- `skills-gap-cycle/skills-gap-cycle-1.png` - Generated infographic (after creation)

**What it shows**: Circular flow diagram showing the vicious cycle:
1. **Industry**: "Universities don't teach AI, we train in-house"
2. **University**: "Industry changes too fast, we can't keep up"
3. **Graduates**: Lack functional AND critical AI literacy
4. **On-the-Job Learning**: From vendors (incentivized to oversell)
5. **Failures**: 42% zero ROI, GDPR fines, wrongful arrests (back to 1)

**Key statistics**: 71% skills gap, 42% zero ROI, 0% event-specific AI programs

**Estimated generation time**: ~15-20 minutes

**To generate**: Follow instructions in `skills-gap-cycle/skills-gap-cycle.instructions.md`

---

### VIS-2.4: Proposed AI Literacy Curriculum ✅ READY TO GENERATE

**Type**: Course Structure Diagram
**Platform**: NotebookLM
**Status**: Placeholder files prepared, ready for generation

**Files**:
- `curriculum-structure/curriculum-structure.content.md` - Source material
- `curriculum-structure/curriculum-structure.prompt.md` - Token-optimized prompt
- `curriculum-structure/curriculum-structure.instructions.md` - Generation workflow
- `curriculum-structure/curriculum-structure-1.png` - Generated infographic (after creation)

**What it shows**: 15-week semester course structure with 4 modules:
- **Weeks 1-4**: AI Fundamentals (What is AI/ML, Festival use cases, Deploy chatbot)
- **Weeks 5-8**: Critical Evaluation (Evidence assessment, GDPR/EU AI Act, Paris 2024 case)
- **Weeks 9-12**: Ethical Dilemmas (Algorithmic bias, Dynamic pricing backlash, Ethics project)
- **Weeks 13-15**: Industry Perspectives (Guest lectures, Facial recognition debate, Policy paper)

**Key deliverables**: Chatbot deployment, case study analysis, ethical assessment, policy debate, final paper

**Estimated generation time**: ~15-20 minutes

**To generate**: Follow instructions in `curriculum-structure/curriculum-structure.instructions.md`

---

## Generation Workflow

### For NotebookLM Infographics

1. **Prepare source**: Extract relevant content into focused markdown file ✅ (already done)
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
- `literacy-comparison-1.png`, `literacy-comparison-2.png`, `literacy-comparison-3.png` (VIS-2.1)
- `academic-integration-1.png`, `academic-integration-2.png` (VIS-2.2)
- `skills-gap-cycle-1.png` through `skills-gap-cycle-3.png` (VIS-2.3)
- `curriculum-structure-1.png`, `curriculum-structure-2.png` (VIS-2.4)

### Documentation Files
**Format**: `{topic}.{type}.md`

**Types**:
- `.content.md` - Source material/data for NotebookLM upload ✅
- `.prompt.md` - Raw NotebookLM prompt (token-optimized, no framing) ✅
- `.instructions.md` - Workflow guidance and generation steps ✅
- `.eval.md` - Evaluation report from /ig-evaluate (after generation)

**Examples**:
- `literacy-comparison.content.md`, `literacy-comparison.prompt.md`, etc. ✅
- `skills-gap-cycle.content.md`, `skills-gap-cycle.prompt.md`, etc. ✅

---

## Token Optimization Requirements

**🚨 CRITICAL**: `.content.md` and `.prompt.md` files MUST be token-optimized before upload to AI agents.

### Target Metrics
- ✅ **Token reduction**: 40-70% from verbose original
- ✅ **Information preservation**: 100% of substantive points
- ✅ **Readability**: High (scannable, clear structure)
- ✅ **Completeness**: All facts, stats, technical details intact

All files in this folder have been pre-optimized following these principles.

---

## EventAI Style Standards

All visuals must comply with EventAI visual identity:

### Colors
- **Deep purple** (#6B46C1) - primary brand, critical thinking
- **Electric coral** (#FF6B6B) - emphasis, key problems/urgency
- **Sky blue** (#4299E1) - functional elements, data
- **Midnight slate** (#2D3748) - body text
- **Clean white background** (#FFFFFF)

### Typography
- **Headings**: Inter (bold, 24-36pt)
- **Body**: Source Sans Pro (regular, 14-16pt)
- **Data**: Inter (bold, 48-72pt for key numbers)

### Design Principles
- Semi-flat style with subtle depth
- Rounded corners (8-12px radius)
- 2-3px outlines for clarity
- Minimal decoration (high data-ink ratio)
- Festival/event context (NOT generic academic or business imagery)
- Professional yet energetic mood
- White space ≥30%

**Full guide**: [../../../lemmy/style-guide/eventai-visual-identity.md](../../../lemmy/style-guide/eventai-visual-identity.md)

---

## Quality Checklist

Before marking visual complete:

✅ **Factual Accuracy**: All data verified against source documents
✅ **EventAI Style**: Colors, typography, design match style guide
✅ **Festival Context**: Industry-specific imagery, not generic
✅ **Accessibility**: WCAG AA contrast, readable text sizes
✅ **File Management**: Named correctly, saved to appropriate folder
✅ **Documentation**: Status updated in VISUAL-CONTENT-PLAN.md

---

## Education-Specific Quality Checks

### VIS-2.1 (Literacy Comparison):
- ✅ Clear distinction between functional (blue) and critical (purple) literacy
- ✅ Gap section prominently displayed in coral
- ✅ All training programs correctly described (MPI/PCMA vs proposed course)

### VIS-2.2 (Academic Integration):
- ✅ 3 universities WITH AI clearly prominent (Surrey, Southern Cross, Penn State)
- ✅ Visual disparity evident (3 vs 100+)
- ✅ NOT a literal geographic map (conceptual diagram)

### VIS-2.3 (Skills Gap Cycle):
- ✅ Circular flow clearly shows cycle returning to start
- ✅ All 5 stages present with accurate content
- ✅ 71% stat prominently displayed

### VIS-2.4 (Curriculum Structure):
- ✅ All 4 modules with correct week ranges
- ✅ Key deliverables clearly marked
- ✅ Progressive learning path evident
- ✅ Portrait orientation

---

## Related Documentation

- **Main Draft**: [../drafts/education.draft.md](../drafts/education.draft.md) (when created)
- **Visual Content Plan**: [../../VISUAL-CONTENT-PLAN.md](../../VISUAL-CONTENT-PLAN.md)
- **Lemmy Workflows**: [../../../lemmy/workflows/](../../../lemmy/workflows/)
- **EventAI Style Guide**: [../../../lemmy/style-guide/eventai-visual-identity.md](../../../lemmy/style-guide/eventai-visual-identity.md)

---

*Visual Assets Folder for Education Topic*
*Last Updated: December 29, 2025*
*Part of: EventAI Curriculum + Lemmy Content Generation System*
