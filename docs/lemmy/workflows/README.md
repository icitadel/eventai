# Lemmy Content Generation Workflows

**System**: Lemmy (LMy) - Multi-AI Content Generation Orchestration
**Purpose**: Step-by-step workflows for creating EventAI curriculum materials
**Last Updated**: December 28, 2025

---

## Quick Start

### New to Lemmy?

1. **Read**: [content-generation.md](content-generation.md) - Overview of all workflows
2. **Choose platform**: NotebookLM or Nano Banana based on content type
3. **Follow detailed workflow**: Platform-specific steps below
4. **Use templates**: Copy from `docs/lemmy/prompts/` and fill in

### Experienced with Lemmy?

**Quick reference**:
- 📊 Infographic needed? → [NotebookLM workflow](notebooklm-workflows.md#workflow-2-infographic-generation)
- 🎨 Custom diagram? → [Nano Banana workflow](nano-banana-workflows.md#workflow-1-technical-diagram-generation)
- 🎙️ Audio explainer? → [NotebookLM workflow](notebooklm-workflows.md#workflow-1-audio-overview-generation)
- 🎬 Video overview? → [NotebookLM workflow](notebooklm-workflows.md#workflow-4-video-overview-generation)
- 🖼️ Icon set? → [Nano Banana workflow](nano-banana-workflows.md#workflow-3-icon-set-generation)

---

## Workflow Documents

### 1. Content Generation Overview
**File**: [content-generation.md](content-generation.md)

**Contains**:
- Complete Topic Package Generation (Research → Text → Visuals → Audio)
- Platform Selection Decision Tree (when to use which AI)
- Quality Standards and File Naming Conventions
- Multi-Format Package Creation (Audio + Slides + Infographics)
- Integration workflows and troubleshooting

**Use when**: You need to understand the big picture or plan a complete topic package.

---

### 2. NotebookLM Detailed Workflows
**File**: [notebooklm-workflows.md](notebooklm-workflows.md)

**Contains**:
- Audio Overview Generation (5 formats, 80+ languages)
- Infographic Generation (3 detail levels)
- Slide Deck Creation (PDF export)
- Video Overview Generation (8 visual styles)
- Deep Research (multi-source synthesis)

**Use when**: Creating NotebookLM content (infographics, audio, video, slides, research).

**Time estimates**:
- Audio Overview: ~13 min
- Infographic: ~17 min
- Slide Deck: ~10 min
- Video Overview: ~14 min
- Deep Research: ~20 min

---

### 3. Nano Banana (Gemini) Image Workflows
**File**: [nano-banana-workflows.md](nano-banana-workflows.md)

**Contains**:
- Technical Diagram Generation (flowcharts, system diagrams)
- Festival Scene Illustration (conceptual imagery)
- Icon Set Generation (consistent visual language)
- Data Visualization Enhancement (custom charts)

**Use when**: Creating custom images, diagrams, illustrations, or icons with precise control.

**Time estimates**:
- Technical Diagram: ~20-25 min
- Festival Illustration: ~30-40 min
- Icon Set: ~25-35 min
- Data Visualization: ~25-35 min

---

## Decision Tree: Which Platform?

### Start Here: What do you need to create?

#### Audio/Video Content
→ **NotebookLM**
- Audio Overview (podcast-style explanation)
- Video Overview (narrated slides)
- Options: 5 audio formats, 8 video styles

#### Presentation/Slides
→ **NotebookLM**
- Slide Deck (PDF export)
- Automatically structured from source content

#### Data-Heavy Infographic
→ **NotebookLM**
- Multi-section infographic
- Text summaries with visualizations
- Automated layout from source

#### Custom Diagram/Illustration
→ **Nano Banana (Gemini)**
- Flowchart, system architecture
- Festival scene illustration
- Precise composition control

#### Icon Set
→ **Nano Banana (Gemini)**
- Consistent visual language
- Multiple icons with same style

#### Creative Data Visualization
→ **Nano Banana (Gemini)**
- Timeline with festival context
- Creative metaphor visualizations
- Custom chart designs

#### Comprehensive Package
→ **Both Platforms**
- NotebookLM for audio + infographics
- Nano Banana for custom diagrams + icons
- See [content-generation.md](content-generation.md) Workflow 5

---

## Common Workflows (Quick Reference)

### Generate Single Infographic (NotebookLM)

**Steps**: 5 steps, ~17 minutes total

1. Extract source content from draft (5 min)
2. Prepare NotebookLM prompt with EventAI style (3 min)
3. Generate in NotebookLM (2-5 min)
4. Download & save to visuals/ folder (1 min)
5. Quality check (2 min)

**Files needed**:
- Draft content: `docs/writing/[N]-[topic]/drafts/[topic].draft.md`
- Prompt template: `docs/lemmy/prompts/notebooklm/infographic.prompt.md`
- Style guide: `docs/lemmy/style-guide/eventai-visual-identity.md`

**Output**: `[topic]-infographic-[descriptor].png` in `docs/writing/[N]-[topic]/visuals/`

**Detailed steps**: [notebooklm-workflows.md#workflow-2-infographic-generation](notebooklm-workflows.md#workflow-2-infographic-generation)

---

### Generate Custom Diagram (Nano Banana)

**Steps**: 6 steps, ~20-25 minutes total

1. Select template from nano-banana.prompt.md (2 min)
2. Define diagram structure (5 min)
3. Fill template with specific content (8 min)
4. Generate via Google AI Studio (5 min)
5. Iterate if needed (5-15 min)
6. Download & save (2 min)

**Files needed**:
- Prompt template: `docs/lemmy/prompts/images/nano-banana.prompt.md`
- Style guide: `docs/lemmy/style-guide/eventai-visual-identity.md`

**Output**: `[topic]-diagram-[descriptor].png` in `docs/writing/[N]-[topic]/visuals/`

**Detailed steps**: [nano-banana-workflows.md#workflow-1-technical-diagram-generation](nano-banana-workflows.md#workflow-1-technical-diagram-generation)

---

### Generate Audio Overview (NotebookLM)

**Steps**: 5 steps, ~13 minutes total

1. Create/select notebook (2 min)
2. Upload source document (2 min)
3. Generate Audio Overview with customization (5 min)
4. Review & download (3 min)
5. Documentation (1 min)

**Files needed**:
- Draft content: `docs/writing/[N]-[topic]/drafts/[topic].draft.md`
- Prompt template: `docs/lemmy/prompts/notebooklm/audio-overview.prompt.md`

**Output**: `[topic]-audio-[format].mp3` in `docs/writing/[N]-[topic]/audio/`

**Detailed steps**: [notebooklm-workflows.md#workflow-1-audio-overview-generation](notebooklm-workflows.md#workflow-1-audio-overview-generation)

---

### Create Complete Topic Package

**Steps**: 4 phases, ~2-3 hours total

1. **Phase 1**: Research & Text Content (Claude + Perplexity)
2. **Phase 2**: Visual Content Planning
3. **Phase 3A**: NotebookLM Content (infographics, audio, slides)
4. **Phase 3B**: Nano Banana Images (diagrams, illustrations)
5. **Phase 4**: Integration & Review

**Files needed**:
- All templates from `docs/lemmy/prompts/`
- Style guide: `docs/lemmy/style-guide/eventai-visual-identity.md`
- Visual plan: `docs/writing/VISUAL-CONTENT-PLAN.md`

**Output**: Complete folder in `docs/writing/[N]-[topic]/` with drafts, visuals, audio, sources

**Detailed steps**: [content-generation.md#workflow-1-complete-topic-package-generation](content-generation.md#workflow-1-complete-topic-package-generation)

---

## EventAI Style Compliance

### Every Generated Asset Must Include

✅ **EventAI Color Palette**:
- Deep purple (#6B46C1) - primary brand, AI elements
- Electric coral (#FF6B6B) - emphasis, key statistics
- Sky blue (#4299E1) - data, comparisons
- Midnight slate (#2D3748) - body text

✅ **Typography**:
- Headings: Inter (bold, 24-36pt)
- Body: Source Sans Pro (regular, 14-16pt)
- Data: Inter (bold, 48-72pt for key numbers)

✅ **Design Principles**:
- Semi-flat style with subtle depth
- Rounded corners (8-12px radius)
- 2-3px outlines for clarity
- Minimal decoration (high data-ink ratio)
- Festival context (stages, crowds, wristbands)

✅ **Quick Copy-Paste Style Snippet**:
```
EventAI festival industry style: Deep purple (#6B46C1), electric coral
(#FF6B6B), sky blue (#4299E1) on white. Modern sans-serif, rounded corners,
2-3px outlines. Semi-flat with subtle depth. Festival context (stages, crowds,
wristbands). Professional yet energetic. Minimal decoration, clean composition.
High resolution, print-ready.
```

**Full guide**: [../style-guide/eventai-visual-identity.md](../style-guide/eventai-visual-identity.md)

---

## File Organization

### Standard Structure

```
docs/writing/[N]-[topic]/
├── drafts/
│   └── [topic].draft.md          # Main content with question header
├── visuals/
│   ├── [topic]-infographic-*.png # NotebookLM infographics
│   ├── [topic]-diagram-*.png     # Nano Banana diagrams
│   ├── [topic]-illustration-*.png # Nano Banana illustrations
│   └── [topic]-slides.pdf        # NotebookLM slide deck
├── audio/
│   ├── [topic]-audio-*.mp3       # NotebookLM audio overviews
│   └── [topic]-video-*.mp4       # NotebookLM video overviews
└── sources/
    ├── citations.md              # Source references
    └── research-notes.md         # Research synthesis
```

### File Naming Convention

**Format**: `[topic]-[type]-[descriptor].[ext]`

**Examples**:
- `privacy-infographic-surveillance-risks.png`
- `analytics-diagram-predictive-flow.png`
- `education-audio-deepdive.mp3`
- `transformation-slides.pdf`
- `personalization-illustration-ai-conductor.png`

---

## Quality Standards

### Before Marking Content Complete

✅ **Factual Accuracy**:
- All statistics verified and cited
- Claims supported by sources
- Examples are real and current (2024-2025)

✅ **EventAI Style**:
- Colors match palette (exact hex codes)
- Typography consistent (Inter/Source Sans Pro)
- Design language matches (rounded corners, outlines, semi-flat)

✅ **Festival Context**:
- Industry-specific imagery (stages, crowds, wristbands)
- NOT generic business imagery (suits, offices)
- Professional yet energetic mood

✅ **Accessibility**:
- WCAG AA contrast ratios met
- Text readable (14pt+ body, 24pt+ emphasis)
- Color-blind safe (not relying on color alone)

✅ **File Management**:
- Saved to correct folder
- Named according to convention
- Referenced in draft if applicable

---

## Tools & Resources

### Required Platforms

- **NotebookLM**: [https://notebooklm.google.com/](https://notebooklm.google.com/)
- **Google AI Studio**: [https://aistudio.google.com/](https://aistudio.google.com/)
- **Claude Code**: For research synthesis and content drafting
- **Perplexity**: For real-time research and fact-checking

### Prompt Templates

All templates in: `docs/lemmy/prompts/`

- **NotebookLM Infographic**: [../prompts/notebooklm/infographic.prompt.md](../prompts/notebooklm/infographic.prompt.md)
- **NotebookLM Audio**: [../prompts/notebooklm/audio-overview.prompt.md](../prompts/notebooklm/audio-overview.prompt.md)
- **Nano Banana Images**: [../prompts/images/nano-banana.prompt.md](../prompts/images/nano-banana.prompt.md)

**Template index**: [../prompts/INDEX.md](../prompts/INDEX.md)

### Style Guide

**EventAI Visual Identity**: [../style-guide/eventai-visual-identity.md](../style-guide/eventai-visual-identity.md)

Contains:
- Complete color palette with usage guidelines
- Typography specifications
- Professional + Whimsy balance definition
- Minimal Cruft principle
- Copy-paste prompt templates

### Research Documentation

- **NotebookLM Capabilities**: [../research/notebooklm/capabilities.md](../research/notebooklm/capabilities.md)
- **Nano Banana Capabilities**: [../research/nano-banana/capabilities.md](../research/nano-banana/capabilities.md)
- **Infographics Best Practices**: [../research/infographics-best-practices.md](../research/infographics-best-practices.md)
- **Automation Assessment**: [../research/notebooklm/automation-assessment.md](../research/notebooklm/automation-assessment.md)

---

## Troubleshooting

### Generated content doesn't match EventAI style

**Solution**: Include exact EventAI style snippet in prompt, reference specific hex codes, regenerate.

### NotebookLM infographic too generic

**Solution**: Add more specific customization prompt emphasizing festival context, professional+whimsy balance.

### Nano Banana image has text errors

**Solution**: Check spelling in prompt, regenerate. Nano Banana Pro has excellent text rendering but always review.

### File organization unclear

**Solution**: Follow standard structure above, use naming convention exactly, reference [content-generation.md](content-generation.md).

### Don't know which platform to use

**Solution**: Use decision tree above, or see [content-generation.md#platform-selection-decision-tree](content-generation.md#platform-selection-decision-tree).

---

## Next Steps

### First-Time User

1. **Read Overview**: [content-generation.md](content-generation.md)
2. **Review Style Guide**: [../style-guide/eventai-visual-identity.md](../style-guide/eventai-visual-identity.md)
3. **Try Simple Workflow**: Generate one infographic using [NotebookLM workflow](notebooklm-workflows.md#workflow-2-infographic-generation)
4. **Scale Up**: Create complete topic package

### Creating Specific Content

- **Need infographic?** → [notebooklm-workflows.md#workflow-2](notebooklm-workflows.md#workflow-2-infographic-generation)
- **Need diagram?** → [nano-banana-workflows.md#workflow-1](nano-banana-workflows.md#workflow-1-technical-diagram-generation)
- **Need audio?** → [notebooklm-workflows.md#workflow-1](notebooklm-workflows.md#workflow-1-audio-overview-generation)

### Creating Complete Package

Follow: [content-generation.md#workflow-1](content-generation.md#workflow-1-complete-topic-package-generation)

---

## Future Enhancements

### Automation Potential (Playwright)

**Status**: ✅ HIGHLY FEASIBLE

See [../research/notebooklm/automation-assessment.md](../research/notebooklm/automation-assessment.md)

**Possible**:
- Automated NotebookLM source upload
- Batch infographic generation
- Audio Overview automation
- Automated download and file management

**Existing projects**: DataNath, upamune, sshnaidm (GitHub)

---

*Workflow Documentation Version: 1.0*
*Last Updated: December 28, 2025*
*Part of: Lemmy Multi-AI Content Generation System*
*Maintained by: EventAI Curriculum Team*
