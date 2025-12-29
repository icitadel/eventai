# Lemmy Content Generation Workflows

**System**: Lemmy (LMy) - Multi-AI Content Generation Orchestration
**Purpose**: Production workflows for creating EventAI curriculum materials
**Last Updated**: December 28, 2025

## Overview

Lemmy orchestrates multiple AI platforms to create comprehensive, multi-format learning content:

- **NotebookLM**: Rich media (Audio/Video Overviews, Slide Decks, Infographics, Deep Research)
- **Nano Banana (Gemini)**: Custom images, diagrams, illustrations, icons
- **Claude (Sonnet)**: Research synthesis, content drafting, technical writing
- **ChatGPT**: Alternative content generation, conversational formats
- **Perplexity**: Real-time research, fact-checking, citation gathering

---

## Workflow 1: Complete Topic Package Generation

**Use Case**: Creating all content for a single topic (e.g., "AI Privacy & Surveillance")

### Phase 1: Research & Text Content (Claude + Perplexity)

**Tools**: Claude Code, Perplexity

1. **Research Synthesis** (Claude)
   - Gather sources from research folders
   - Synthesize findings into coherent narrative
   - Create draft content in `docs/writing/[N]-[topic]/drafts/`
   - Ensure question is quoted at top of draft

2. **Fact-Checking** (Perplexity)
   - Verify statistics and claims
   - Gather current citations (2025)
   - Document sources in `docs/writing/[N]-[topic]/sources/`

**Output**: `[topic].draft.md` with question header and full content

### Phase 2: Visual Content Planning

**Tools**: Visual Content Plan, EventAI Style Guide

1. **Identify Visual Needs**
   - Review `docs/writing/VISUAL-CONTENT-PLAN.md` for topic
   - Determine infographics vs custom diagrams
   - Map visuals to content sections

2. **Select Generation Method**
   - **NotebookLM Infographics**: Data-heavy, multi-section, text summaries
   - **Nano Banana**: Custom diagrams, illustrations, icons, creative visualizations

**Output**: List of visuals to generate with assigned platform

### Phase 3A: NotebookLM Content Generation

**Tools**: NotebookLM, Prompt Templates

**Workflow**: See [notebooklm-workflows.md](notebooklm-workflows.md) for detailed steps

1. **Source Preparation**
   - Create focused source document (extract from draft)
   - Include only relevant content for this visual
   - Add EventAI style guide snippet

2. **Generation Process**
   - Upload source to NotebookLM
   - Select content type (Audio/Video/Slide/Infographic)
   - Apply prompt template from `docs/lemmy/prompts/notebooklm/`
   - Generate and download

3. **File Management**
   - Save to `docs/writing/[N]-[topic]/[visuals|audio]/`
   - Name: `[topic]-[type]-[descriptor].[ext]`
   - Example: `privacy-infographic-surveillance-risk.png`

**Output**: Downloaded files in appropriate folders

### Phase 3B: Nano Banana Image Generation

**Tools**: Google AI Studio (Gemini), Prompt Templates

**Workflow**: See [nano-banana-workflows.md](nano-banana-workflows.md) for detailed steps

1. **Prompt Construction**
   - Use template from `docs/lemmy/prompts/images/nano-banana.prompt.md`
   - Fill in placeholders with specific content
   - Include EventAI style snippet (copy from style guide)

2. **Generation Process**
   - Go to [Google AI Studio](https://aistudio.google.com/)
   - Select Imagen 3 or Nano Banana Pro model
   - Paste filled prompt
   - Generate (30-60 seconds)
   - Download PNG file

3. **Quality Check**
   - Verify factual accuracy
   - Check EventAI style compliance
   - Ensure text legibility
   - Review accessibility (contrast, color-blind safe)

4. **File Management**
   - Save to `docs/writing/[N]-[topic]/visuals/`
   - Name: `[topic]-[type]-[descriptor].png`
   - Example: `privacy-diagram-surveillance-flow.png`

**Output**: High-resolution PNG files (2400x1800px minimum)

### Phase 4: Integration & Review

**Tools**: Markdown editor, Image viewer

1. **Reference Visuals in Draft**
   - Add image references in markdown: `![Alt text](path/to/image.png)`
   - Link to audio files: `[Listen: Audio Overview](path/to/audio.mp3)`
   - Embed slide decks or link to PDFs

2. **Content Review**
   - Verify visual-text alignment
   - Check all sources cited
   - Ensure EventAI style consistency
   - Accessibility review

3. **Finalization**
   - Mark topic complete in tracking system
   - Update README files
   - Commit to git with descriptive message

**Output**: Complete topic package ready for curriculum integration

---

## Workflow 2: Infographic-Only Generation (NotebookLM)

**Use Case**: Quickly creating a single infographic from existing content

### Prerequisites

- Draft content exists in `docs/writing/[N]-[topic]/drafts/`
- Visual identified in `VISUAL-CONTENT-PLAN.md`
- EventAI style guide reviewed

### Steps

1. **Extract Source Content** (5 min)
   ```bash
   # Create focused source document
   # Include: title, relevant section, key data points, citations
   ```

2. **Prepare NotebookLM Prompt** (3 min)
   - Copy template from `docs/lemmy/prompts/notebooklm/infographic.prompt.md`
   - Fill in: topic, key points, data to visualize, orientation
   - Add EventAI style snippet:
     ```
     Style Guide: Use deep purple (#6B46C1), electric coral (#FF6B6B),
     sky blue (#4299E1) on white background. Modern sans-serif typography
     (Inter for headings). Semi-flat design with rounded corners.
     Festival context (stages, crowds, wristbands). Professional yet
     energetic mood. Minimal decoration, high data-ink ratio.
     ```

3. **Generate in NotebookLM** (2-5 min)
   - Upload source document
   - Select "Infographic" content type
   - Choose detail level (Brief/Detailed/Comprehensive)
   - Select orientation (Landscape/Portrait/Square)
   - Paste customization prompt
   - Generate (may take 1-2 minutes)

4. **Download & Save** (1 min)
   - Download PNG file
   - Save to `docs/writing/[N]-[topic]/visuals/`
   - Name: `[topic]-infographic-[descriptor].png`

5. **Quality Check** (2 min)
   - Verify data accuracy
   - Check style compliance
   - Ensure readability
   - Review accessibility

**Total Time**: ~15 minutes per infographic

---

## Workflow 3: Audio Overview Generation (NotebookLM)

**Use Case**: Creating podcast-style explanation of a topic

### Prerequisites

- Draft content exists
- Audio format selected (Deep Dive, Brief, Critique, Debate, Lecture)

### Steps

1. **Prepare Source Document**
   - Use full draft content OR extract focused section
   - Include: question at top, main content, key sources

2. **Select Audio Format**
   - **Deep Dive**: Comprehensive exploration (10-20 min)
   - **Brief**: Quick summary (5 min)
   - **Critique**: Critical analysis with counterarguments
   - **Debate**: Two-host opposing viewpoints
   - **Lecture**: Educational session format

3. **Customize in NotebookLM**
   - Upload source document
   - Select "Audio Overview"
   - Choose format and length (Shorter/Default/Longer)
   - Add customization prompt:
     ```
     Focus on: [specific aspects]
     Audience: University students in event management
     Tone: Professional yet accessible, evidence-based
     Include: Real-world examples from festival industry
     ```

4. **Generate & Download**
   - Generate (may take 2-3 minutes)
   - Download MP3 file
   - Save to `docs/writing/[N]-[topic]/audio/`
   - Name: `[topic]-audio-[format].mp3`

**Output**: MP3 file (5-20 minutes)

---

## Workflow 4: Custom Diagram Creation (Nano Banana)

**Use Case**: Creating specific technical diagrams or illustrations

### Prerequisites

- Diagram concept defined (flowchart, system architecture, process flow)
- EventAI style guide reviewed

### Steps

1. **Select Template**
   - Open `docs/lemmy/prompts/images/nano-banana.prompt.md`
   - Choose:
     - Template 1: Technical Diagram (flowcharts, system diagrams)
     - Template 2: Festival Scene Illustration (conceptual imagery)
     - Template 3: Icon Set Generation (consistent icons)
     - Template 4: Data Visualization (custom charts)

2. **Fill Template**
   - Replace all `{{PLACEHOLDERS}}` with specific content
   - Be specific about layout, elements, connections
   - Include EventAI style specifications (already in template)
   - Add festival context elements

3. **Generate via Gemini**
   - Go to [Google AI Studio](https://aistudio.google.com/)
   - Select Imagen 3 or Nano Banana Pro model
   - Paste filled prompt
   - Generate (30-60 seconds)

4. **Review & Iterate**
   - Download PNG
   - Check factual accuracy, style compliance, text rendering
   - If needed: refine prompt and regenerate
   - Generate 2-3 variations, select best

5. **Save Final Version**
   - Save to `docs/writing/[N]-[topic]/visuals/`
   - Name: `[topic]-diagram-[descriptor].png`
   - High resolution (minimum 2400x1800px)

**Output**: Custom PNG diagram

---

## Workflow 5: Multi-Format Package (Audio + Slides + Infographics)

**Use Case**: Creating comprehensive learning package for a topic

### Timeline

**Total Time**: ~2-3 hours per topic

### Sequence

1. **Audio Overview** (15 min)
   - Generate Deep Dive format (10-15 min audio)
   - Save to `audio/` folder

2. **Slide Deck** (20 min)
   - Generate NotebookLM Slide Deck (PDF)
   - Customize for EventAI style
   - Save to `visuals/` folder

3. **Infographics** (60-90 min)
   - Generate 3-5 infographics per topic (per VISUAL-CONTENT-PLAN.md)
   - Mix NotebookLM and Nano Banana as appropriate
   - 15-20 min per infographic

4. **Custom Diagrams** (30-45 min)
   - Generate 1-2 custom Nano Banana diagrams
   - Technical flows, conceptual illustrations
   - 20-25 min per diagram

5. **Integration** (15 min)
   - Reference all media in draft markdown
   - Create comprehensive README for topic folder
   - Verify all files named consistently

**Output**: Complete learning package with 5-7 visual assets and 1-2 audio files

---

## Platform Selection Decision Tree

### When to Use NotebookLM

✅ **Use NotebookLM for**:
- Audio Overviews (podcast-style explanations)
- Video Overviews (narrated slides with visuals)
- Slide Decks (presentation format, PDF export)
- Infographics (data-heavy, multi-section, text summaries)
- Deep Research (comprehensive source synthesis)

✅ **Advantages**:
- Handles complex source documents
- Excellent text rendering in infographics
- Multi-format output from same source
- Built-in citation handling
- 80+ language support for audio

### When to Use Nano Banana (Gemini)

✅ **Use Nano Banana for**:
- Custom diagrams (flowcharts, system architecture)
- Illustrations (festival scenes, conceptual imagery)
- Icon sets (consistent visual language)
- Creative data visualizations (beyond standard charts)
- Visual elements to combine with other content

✅ **Advantages**:
- Precise control over composition
- Excellent text rendering (autoregressive model)
- High-resolution output (print-ready)
- Custom brand styling
- Creative freedom

### When to Use Both Together

✅ **Best Approach**:
1. Generate custom icons/diagrams with Nano Banana
2. Create infographics with NotebookLM (can reference Nano Banana visuals in prompt)
3. Generate Audio Overview with NotebookLM for comprehensive explanation
4. Combine in final layout

---

## Quality Standards

### All Content Must Meet

- ✅ **Factual Accuracy**: All statistics, claims, examples verified
- ✅ **EventAI Style**: Colors, typography, design language consistent
- ✅ **Accessibility**: WCAG AA contrast, readable text, color-blind safe
- ✅ **Festival Context**: Industry-specific imagery, not generic business
- ✅ **Professional + Whimsy**: Clean foundation with strategic playful accents
- ✅ **Minimal Cruft**: Every element serves information or clarity
- ✅ **Source Attribution**: All claims cited, sources documented

### File Naming Conventions

```
[topic]-[type]-[descriptor].[ext]

Examples:
- privacy-infographic-surveillance-risks.png
- analytics-diagram-predictive-flow.png
- education-audio-deepdive.mp3
- transformation-slides-2025-2035.pdf
```

### Folder Structure

```
docs/writing/[N]-[topic]/
├── drafts/[topic].draft.md          # Main content with question header
├── visuals/                          # All PNG/PDF visual content
├── audio/                            # All MP3/audio content
└── sources/                          # Citations, research notes
```

---

## Automation Potential

### Currently Manual

- NotebookLM source upload
- NotebookLM content generation
- Nano Banana prompt input
- Download and file management

### Future Automation (Playwright)

**Feasibility**: ✅ HIGHLY FEASIBLE

See [../research/notebooklm/automation-assessment.md](../research/notebooklm/automation-assessment.md)

**Possible Automations**:
- Source document upload to NotebookLM
- Audio Overview generation
- Batch infographic generation
- Automated download to correct folders

**Existing GitHub Projects**:
- [DataNath/notebooklm-voice-generator](https://github.com/DataNath/notebooklm-voice-generator)
- [upamune/notebooklm-audio-generator](https://github.com/upamune/notebooklm-audio-generator)
- [sshnaidm/notebooklm](https://github.com/sshnaidm/notebooklm)

---

## Troubleshooting

### NotebookLM Issues

**Problem**: Infographic doesn't match EventAI style
**Solution**: Be more explicit in style prompt, reference exact hex codes, regenerate

**Problem**: Audio Overview too generic
**Solution**: Add more specific customization prompt, use "Critique" or "Debate" format for deeper analysis

**Problem**: Source document too large
**Solution**: Extract focused section, NotebookLM handles up to 50 sources but performance varies

### Nano Banana Issues

**Problem**: Generated image has spelling errors in text
**Solution**: Regenerate, Nano Banana Pro has excellent text rendering but review carefully

**Problem**: Image doesn't match festival context
**Solution**: Be more specific about festival elements (stages, crowds, wristbands), add examples

**Problem**: Style inconsistent across multiple images
**Solution**: Use exact same EventAI style snippet, generate in same session

---

## Related Documentation

- **Prompt Templates**: [../prompts/INDEX.md](../prompts/INDEX.md)
- **EventAI Style Guide**: [../style-guide/eventai-visual-identity.md](../style-guide/eventai-visual-identity.md)
- **Visual Content Plan**: [../../writing/VISUAL-CONTENT-PLAN.md](../../writing/VISUAL-CONTENT-PLAN.md)
- **NotebookLM Capabilities**: [../research/notebooklm/capabilities.md](../research/notebooklm/capabilities.md)
- **Nano Banana Capabilities**: [../research/nano-banana/capabilities.md](../research/nano-banana/capabilities.md)

---

*Workflow Version: 1.0*
*Last Updated: December 28, 2025*
*Part of: Lemmy Multi-AI Content Generation System*
