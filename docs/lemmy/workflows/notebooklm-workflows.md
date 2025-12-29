# NotebookLM Detailed Workflows

**Platform**: Google NotebookLM (2025 version)
**Capabilities**: Audio/Video Overviews, Slide Decks, Infographics, Deep Research
**EventAI Integration**: Fully integrated with prompt templates and style guide

---

## Workflow 1: Audio Overview Generation

### Step-by-Step Process

#### Step 1: Create New Notebook (2 min)

1. Go to [NotebookLM](https://notebooklm.google.com/)
2. Click "New notebook" or "+ New"
3. Name notebook: `EventAI - [Topic Name]`
   - Example: `EventAI - AI Privacy & Surveillance`

#### Step 2: Upload Source Document (2 min)

**Prepare source document first**:
- Use draft from `docs/writing/[N]-[topic]/drafts/[topic].draft.md`
- OR extract focused section if draft is very long
- Include: question header, main content, key sources

**Upload process**:
1. Click "Add sources" or drag-and-drop area
2. Select "Upload file" (supports: PDF, TXT, MD, DOCX)
3. Upload your prepared markdown file
4. Wait for processing (usually 10-30 seconds)
5. Verify source appears in left sidebar

#### Step 3: Generate Audio Overview (5 min)

1. **Access Audio Feature**
   - Click "Audio Overview" button (speaker icon)
   - Or find in content generation options

2. **Select Format** (September 2025+ options)
   - **Deep Dive**: Comprehensive exploration (default, ~10 min)
   - **Brief**: Quick 5-minute summary
   - **Critique**: Critical analysis with counterarguments
   - **Debate**: Two hosts with opposing viewpoints
   - **Lecture**: Educational class session format (experimental)

3. **Choose Length**
   - **Shorter**: ~5 minutes
   - **Default**: ~10 minutes
   - **Longer**: ~20 minutes

4. **Add Customization Prompt** (optional but recommended)
   - Click "Customize" or "Instructions" field
   - Paste EventAI-specific prompt:

   ```
   Create an Audio Overview for university students studying event management.

   Focus areas:
   - Real-world festival industry applications
   - Practical implications for event organizers
   - Ethical considerations and critical thinking
   - Current examples from major festivals (2024-2025)

   Tone:
   - Professional yet accessible
   - Evidence-based with specific examples
   - Balanced perspective (opportunities and risks)
   - Engaging and conversational

   Structure:
   - Start with the core question being explored
   - Provide context and definitions
   - Present real-world case studies
   - Discuss implications and future directions
   - End with actionable insights

   Avoid:
   - Overly technical jargon without explanation
   - Generic AI hype or tech-solutionism
   - Speculation without evidence
   ```

5. **Generate**
   - Click "Generate" or "Create Audio Overview"
   - Wait 2-3 minutes (processing time varies)
   - NotebookLM will show progress indicator

#### Step 4: Review & Download (3 min)

1. **Play Audio**
   - Listen to first 2-3 minutes
   - Check: tone, pacing, content accuracy, festival context

2. **Iterate if Needed**
   - If unsatisfactory: regenerate with more specific customization
   - Try different format (e.g., Debate instead of Deep Dive)
   - Adjust length setting

3. **Download**
   - Click download icon (down arrow)
   - File format: MP3
   - Save to: `docs/writing/[N]-[topic]/audio/`
   - Name: `[topic]-audio-[format].mp3`
     - Example: `privacy-audio-deepdive.mp3`

#### Step 5: Documentation (1 min)

- Add entry to topic README
- Note: format used, length, customization applied
- Link from main draft if desired

**Total Time**: ~13 minutes per audio overview

---

## Workflow 2: Infographic Generation

### Step-by-Step Process

#### Step 1: Prepare Focused Source (5 min)

**Extract specific content for this infographic**:

From draft, identify:
- Title/topic of infographic
- 3-5 key points to visualize
- Specific data (statistics, percentages, timelines)
- 2-3 supporting examples or case studies

**Create focused source document**:
```markdown
# [Infographic Title]

## Key Question
[The question or topic this infographic addresses]

## Main Points

### Point 1: [Title]
[Brief explanation with data]
- Statistic 1: [value, source]
- Example: [specific case]

### Point 2: [Title]
[Brief explanation with data]
- Statistic 2: [value, source]

[Continue for 3-5 points]

## Visual Guidance
- Emphasis: [What should stand out visually]
- Comparison: [What should be compared/contrasted]
- Flow: [How information should be read]

## Sources
1. [Source 1]
2. [Source 2]
```

Save as: `[topic]-infographic-[descriptor]-source.md`

#### Step 2: Upload to NotebookLM (2 min)

1. Create new notebook OR use existing topic notebook
2. Upload focused source document
3. Wait for processing

#### Step 3: Generate Infographic (5 min)

1. **Access Infographic Feature**
   - Click "Infographic" option
   - Or find in content generation menu

2. **Select Detail Level**
   - **Brief**: High-level overview (minimal text)
   - **Detailed**: Comprehensive (recommended for EventAI)
   - **Comprehensive**: Maximum information density

3. **Choose Orientation**
   - **Landscape**: Most versatile (recommended default)
   - **Portrait**: Vertical displays, mobile viewing
   - **Square**: Social media, balanced composition

4. **Add EventAI Style Customization**
   - Use prompt template from `docs/lemmy/prompts/notebooklm/infographic.prompt.md`
   - Fill in placeholders
   - Include style guide snippet:

   ```
   EventAI Visual Style:

   Colors:
   - Deep purple (#6B46C1) for primary elements, headers
   - Electric coral (#FF6B6B) for emphasis, key statistics
   - Sky blue (#4299E1) for data visualization, comparisons
   - Midnight slate (#2D3748) for body text
   - Clean white background

   Typography:
   - Headings: Inter (bold, 24-36pt)
   - Body: Source Sans Pro (regular, 14-16pt)
   - Data: Inter (bold, 48-72pt for key numbers)

   Design:
   - Semi-flat style with subtle depth
   - Rounded corners on all shapes (8-12px radius)
   - 2-3px outlines for clarity
   - Generous white space, uncluttered layout
   - High data-ink ratio (minimal decoration)

   Festival Context:
   - Include festival-specific imagery: stages, crowds, wristbands, outdoor venues
   - Avoid generic business imagery (suits, offices, briefcases)
   - Professional yet energetic mood

   Layout Preferences:
   - [Specify: grid, timeline, flow diagram, comparison, etc.]
   - Emphasis on: [Key statistic or concept]
   - Visual hierarchy: [What should dominate]
   ```

5. **Generate**
   - Click "Generate Infographic"
   - Wait 1-2 minutes (Nano Banana Pro powered)
   - NotebookLM creates image

#### Step 4: Review & Iterate (3 min)

**Quality Checklist**:
- ✅ Data accuracy (all numbers, percentages correct)
- ✅ EventAI style compliance (colors, typography match)
- ✅ Text legibility (all text readable at intended size)
- ✅ Festival context present (not generic imagery)
- ✅ Information hierarchy clear (eye drawn to key points)
- ✅ Accessibility (WCAG AA contrast ratios)

**If unsatisfactory**:
- Regenerate with more specific style guidance
- Try different orientation
- Adjust detail level
- Create 2-3 variations, select best

#### Step 5: Download & Save (2 min)

1. **Download**
   - Click download icon
   - File format: PNG (high resolution)
   - Save to: `docs/writing/[N]-[topic]/visuals/`

2. **Name File**
   - Format: `[topic]-infographic-[descriptor].png`
   - Example: `privacy-infographic-surveillance-risks.png`

3. **Verify File Quality**
   - Open in image viewer
   - Check resolution (should be high-res, print-ready)
   - Verify colors display correctly

**Total Time**: ~17 minutes per infographic

---

## Workflow 3: Slide Deck Generation

### Step-by-Step Process

#### Step 1: Upload Comprehensive Source (3 min)

**Use full draft content**:
- Upload complete `[topic].draft.md` file
- Include question header, all sections, sources
- NotebookLM will automatically structure into slides

#### Step 2: Generate Slide Deck (5 min)

1. **Access Slide Deck Feature**
   - Click "Slide Deck" or "Presentation" option

2. **Customize Presentation**
   - Add EventAI style guidance:

   ```
   Create a slide deck for university event management students.

   Visual Style:
   - Use EventAI color palette: deep purple (#6B46C1), electric coral (#FF6B6B),
     sky blue (#4299E1) on white background
   - Modern, clean design with festival context imagery
   - Avoid generic business templates

   Content Structure:
   - Title slide with core question
   - 3-5 main section slides
   - Supporting slides with examples and data
   - Summary/implications slide
   - Sources slide

   Slide Content:
   - Concise bullet points (3-5 per slide)
   - Large, readable fonts
   - Specific examples from festival industry
   - Data visualizations where appropriate
   - One main idea per slide

   Tone:
   - Professional yet accessible
   - Evidence-based
   - Critical thinking emphasis
   ```

3. **Generate**
   - Click "Generate Slide Deck"
   - Wait 2-3 minutes

#### Step 3: Download PDF (2 min)

1. **Review Slides**
   - Preview generated deck
   - Check slide count, content distribution
   - Verify style alignment

2. **Download**
   - Click download
   - File format: PDF
   - Save to: `docs/writing/[N]-[topic]/visuals/`
   - Name: `[topic]-slides.pdf`

3. **Optional: Export to PowerPoint**
   - Some PDF tools can convert to PPTX for editing
   - Edit in PowerPoint/Keynote if needed
   - Re-save as PDF when finalized

**Total Time**: ~10 minutes per slide deck

---

## Workflow 4: Video Overview Generation

### Step-by-Step Process

#### Step 1: Upload Source (Same as Audio)

- Use full draft or focused section
- Upload to NotebookLM notebook

#### Step 2: Generate Video Overview (7 min)

1. **Access Video Feature**
   - Click "Video Overview" option
   - Available with Nano Banana Pro integration

2. **Select Visual Style** (8 options)
   - **Slides with Narration**: Presentation format
   - **Animated Diagrams**: Dynamic visualizations
   - **Whiteboard Style**: Educational drawing
   - **Documentary Style**: Professional narrative
   - **Split Screen**: Dual perspectives
   - **Picture-in-Picture**: Visual + narrator
   - **Kinetic Typography**: Text-focused animation
   - **Mixed Media**: Combination approach

   **Recommended for EventAI**: Slides with Narration or Animated Diagrams

3. **Customize**
   - Length: 5-20 minutes
   - Pacing: Moderate (educational)
   - Visual density: Balanced
   - Add EventAI style guidance similar to infographic prompt

4. **Generate**
   - Click "Generate Video Overview"
   - Wait 3-5 minutes (longer than audio)

#### Step 3: Download Video (2 min)

1. **Review**
   - Watch first 2-3 minutes
   - Check visual quality, narration accuracy

2. **Download**
   - File format: MP4 (high resolution)
   - Save to: `docs/writing/[N]-[topic]/audio/` (or create video/ folder)
   - Name: `[topic]-video-overview.mp4`

**Total Time**: ~14 minutes per video overview

---

## Workflow 5: Deep Research (Multi-Source Synthesis)

### Step-by-Step Process

#### Step 1: Upload Multiple Sources (10 min)

**NotebookLM supports up to 50 sources**:
- Upload all research documents
- PDFs, web pages (via URL), Google Docs, markdown files
- Organize by topic or theme

**For EventAI**:
- Research reports on festival AI implementations
- Academic papers on event technology
- Industry case studies
- Regulatory documents (GDPR, privacy laws)
- News articles and blog posts

#### Step 2: Ask Deep Research Questions (2 min)

**Use NotebookLM's Q&A feature**:

Example questions:
- "What are the documented privacy risks of facial recognition at festivals?"
- "Compare AI ticketing systems: DICE, Eventbrite, and Universe"
- "What ROI metrics exist for AI predictive analytics in live events?"

#### Step 3: Generate Deep Research Report (5 min)

1. **Select "Deep Research" or "Generate Report"**
2. **Specify research focus**:
   ```
   Synthesize findings on: [Specific topic]

   Focus areas:
   - [Area 1]
   - [Area 2]
   - [Area 3]

   Analyze:
   - Current implementations (2024-2025)
   - Documented outcomes and metrics
   - Ethical considerations
   - Industry best practices

   Format:
   - Executive summary
   - Detailed findings by focus area
   - Case study examples
   - Implications and recommendations
   - Full source citations
   ```

3. **Generate**
   - NotebookLM synthesizes across all sources
   - Creates comprehensive research report
   - Includes citations and cross-references

#### Step 4: Export Research (3 min)

1. **Download as document**
   - File format: PDF or DOCX
   - Save to: `docs/writing/[N]-[topic]/sources/`
   - Name: `[topic]-deep-research.pdf`

2. **Use as source for content**
   - Extract key findings for draft
   - Reference in infographics
   - Cite in audio overview customization

**Total Time**: ~20 minutes for multi-source research synthesis

---

## Tips & Best Practices

### Source Document Preparation

✅ **Do**:
- Keep focused (1,000-3,000 words optimal for single infographic/audio)
- Include clear section headers
- Add specific data points and statistics
- Cite sources within the document
- Use markdown formatting for clarity

❌ **Don't**:
- Upload massive documents without structure
- Mix unrelated topics in one source
- Include irrelevant metadata or formatting artifacts
- Forget to include context and definitions

### Customization Prompts

✅ **Do**:
- Be specific about visual style (colors, typography, layout)
- Reference EventAI style guide explicitly
- Specify audience (university students, event professionals)
- Include festival context requirements
- Mention desired tone and approach

❌ **Don't**:
- Use vague terms like "make it look good"
- Forget to specify orientation/format
- Assume NotebookLM knows EventAI style
- Omit festival industry context

### Quality Control

✅ **Always Check**:
- Factual accuracy (all statistics, dates, names correct)
- Source attribution (claims properly cited)
- Style compliance (EventAI colors, typography, design)
- Text legibility (readable at intended display size)
- Accessibility (contrast ratios, color-blind safe)
- Festival relevance (industry-specific, not generic)

### File Management

✅ **Consistent Naming**:
```
[topic]-[type]-[descriptor].[ext]

Examples:
privacy-infographic-surveillance-risks.png
education-audio-deepdive.mp3
analytics-slides.pdf
transformation-video-overview.mp4
```

✅ **Organized Folders**:
```
docs/writing/[N]-[topic]/
├── drafts/
├── visuals/    ← PNG, PDF (infographics, slides)
├── audio/      ← MP3, MP4 (audio/video overviews)
└── sources/    ← Research documents, citations
```

---

## Language & Translation Support

### Audio Overview Languages (80+ supported)

**Major languages**:
- English (multiple accents: US, UK, AU, IN)
- Spanish, French, German, Italian, Portuguese
- Mandarin, Japanese, Korean
- Hindi, Arabic, Russian
- And 70+ more

**To generate in different language**:
1. Provide source in target language, OR
2. Upload English source and specify in customization: "Generate audio in [language]"

### Localization for Global Events

**Use case**: Creating EventAI content for international festivals

1. Generate master content in English
2. Translate source document to target language
3. Regenerate audio/video in target language
4. Maintain consistent visual style across languages

---

## Troubleshooting

### Problem: Audio sounds too robotic

**Solution**: Use "Debate" or "Critique" format for more natural conversation

### Problem: Infographic doesn't match EventAI style

**Solution**: Be more explicit in customization prompt, include exact hex codes, regenerate

### Problem: Video quality is low

**Solution**: Check source content quality, ensure high-res images in source if applicable

### Problem: Generated content is too generic

**Solution**: Add more specific examples and case studies to source document, emphasize festival context in customization

### Problem: Source processing fails

**Solution**: Check file format (PDF, TXT, MD, DOCX supported), reduce file size if very large, simplify formatting

---

## Integration with Other Workflows

### With Nano Banana

1. Generate custom diagram with Nano Banana
2. Reference in NotebookLM infographic prompt:
   ```
   Include visual similar to: [describe Nano Banana diagram]
   Maintain consistent style with: [list key elements]
   ```

### With Claude Code

1. Use Claude to synthesize research and create draft
2. Upload draft to NotebookLM for multi-format generation
3. Use Claude to integrate all assets into final curriculum

### With Beads (bd) Tracking

```bash
# Create issue for each NotebookLM asset
bd create --title="Generate privacy infographic VIS-4.1" --type=task --priority=2
bd create --title="Generate privacy audio overview" --type=task --priority=2

# Mark in progress when starting
bd update [issue-id] --status=in_progress

# Close when downloaded and saved
bd close [issue-id] --reason="Generated and saved to visuals/"
```

---

## Related Documentation

- **NotebookLM Capabilities**: [../research/notebooklm/capabilities.md](../research/notebooklm/capabilities.md)
- **Infographic Prompt Template**: [../prompts/notebooklm/infographic.prompt.md](../prompts/notebooklm/infographic.prompt.md)
- **Audio Overview Prompt Template**: [../prompts/notebooklm/audio-overview.prompt.md](../prompts/notebooklm/audio-overview.prompt.md)
- **EventAI Style Guide**: [../style-guide/eventai-visual-identity.md](../style-guide/eventai-visual-identity.md)
- **Automation Assessment**: [../research/notebooklm/automation-assessment.md](../research/notebooklm/automation-assessment.md)

---

*Workflow Version: 1.0*
*Last Updated: December 28, 2025*
*Platform: Google NotebookLM (2025)*
