# Lemmy Prototype Implementation Design

This document contains the detailed implementation specifications for the current Lemmy prototype, including the complete pipeline, commands, tools, and workflows.

## The Pipeline (6 Phases)

```
Question → Research → Draft → Validate → Visualize → Integrate → Publish
   ↓          ↓         ↓         ↓          ↓          ↓          ↓
  Specs    Sources   Narrative  Facts    Infographics  Media    DOCX RC
```

### Phase 1: Question & Requirements Definition
- **Input**: Question to answer
- **Output**: Specifications (2000 words, casual-academic voice, 3-5 major points, 3-5 infographics)
- **Key Point**: No sideramps - content must answer the question cleanly

### Phase 2: Deep Research & Knowledge Assembly
- **Tools**: Web search, academic databases, industry reports
- **Outputs**:
  - `{topic}.sources.md` - Tier-classified source catalog (Tier 1-4)
  - `{topic}.research.md` - Claim extraction and context notes
- **Quality Standard**: 90%+ claim verification rate

### Phase 3: Narrative Generation & Drafting
- **Process**: Research → Draft → Validate → Refine → Repeat
- **Target**: 30-40% conciseness vs academic style, 15-word avg sentence length
- **Commands**: `/section-create`, `/narrative-refine-validate`, `/narrative-revise`, `/validate`
- **Outputs**: `{topic}.draft1.md` → `{topic}.draftN.md` + fact-check reports

### Phase 4: Visual Content Creation (Most Complex)
- **Target**: 3-5 infographics per section (every 500-1000 words)
- **Workflow**:
  1. **Prompt Generation**: `/ig-generate-prompt` (tier-aware templates)
  2. **Tier Validation**: `/test-visual-prompt-density` (CLI validation)
  3. **Generation**: `gemini-generate` CLI (3 variants via browser automation)
  4. **Conversion**: `todd-image-convert` (PNG → WebP @ 1080p)
  5. **Evaluation**: `/ig-evaluate` (quantitative scoring, 90%+ target)
- **Outputs**: `{visual}-1.png` → `{visual}-N.png`, evaluation reports

### Phase 5: Media Integration & RC Preparation
- **Process**: Embed winning variants, strip metadata, prepare for DOCX
- **Commands**: `/narrative-add-media`, `/section-rc`
- **Critical**: PNG format (NOT webp), 7-inch width, sources at DOCUMENT END ONLY
- **Output**: `{topic}.draftN-formatted.md`

### Phase 6: Final Publishing
- **Tools**: Pandoc (markdown → DOCX), `justify_docx.py` (text alignment)
- **Commands**: `/section-publish` (end-to-end orchestration)
- **Quality Checks**: Images embedded (~20MB file size), justified text, 7" images
- **Output**: `{topic}.rc1.docx` → `{topic}.rcN.docx`

## Complete Command/Skill Inventory

### Section Orchestration (4 commands)
- `/section-create` - Complete authoring from scratch to RC
- `/section-revise` - Revising existing sections
- `/section-rc` - RC preparation from finalized draft
- `/section-publish` - End-to-end publishing workflow

### Narrative Generation (3 commands)
- `/narrative-refine-validate` - Refinement + validation + source attribution
- `/narrative-revise` - Targeted content revision
- `/narrative-add-media` - Media integration into narrative

### Validation & Quality (2 commands)
- `/validate` - Content validation (question alignment + data accuracy)
- `/textbook-bestpractices` - Academic writing standards

### Visual Content (6 commands)
- `/ig-generate-prompt` - Tier-aware prompt generation
- `/test-visual-prompt-density` - Tier validation (structural metrics + text patterns)
- `/ig-generate` - Automated infographic generation (browser automation)
- `/ig-evaluate` - Comprehensive evaluation (style + data + accessibility)
- `/infographics-bestpractices` - Tufte principles + EventAI brand
- `/todd-image-convert` - Image format conversion

### Utility Commands (2 commands)
- `/optimize-tokens` - Token optimization for long documents
- `/commit` - Commit message generation

## CLI Tools

### gemini-generate
**Purpose**: Browser automation for infographic generation via NotebookLM
- **Usage**: `gemini-generate --content X.content.md --prompt Y.prompt.md --variants 3`
- **Method**: Playwright automation (NOT API), parallel tab generation
- **Speed**: ~95 seconds for 3 variants
- **Output**: PNG files auto-converted to WebP @ 1080p
- **Cost**: Free unlimited use (no API quotas)

### todd-image-convert
**Purpose**: Batch image format conversion with consistent resolution
- **Usage**: `todd-image-convert *.png --resolution 1080p --output-format webp`
- **Technology**: pyvips/libvips (fast, memory-efficient)
- **Presets**: 1080p (web/eval), 4k (print), 720p (thumbnails)
- **Critical**: Always convert PNG → WebP before `/ig-evaluate`

### docutil
**Purpose**: Document utilities for final publishing
- **Location**: `client-cli/py/docutil/`
- **Integration**: Pandoc workflow support

### justify_docx.py
**Purpose**: Post-process DOCX for justified text alignment
- **Usage**: `python3 justify_docx.py {topic}.rc1.docx`
- **Method**: python-docx library, body paragraph justification
- **Critical**: Keep in drafts/ directory for reuse across sections

## File Structures & Naming Conventions

### Draft Progression
```
docs/writing/{topic}/drafts/
  {topic}.draft1.md          # Initial draft
  {topic}.draft2.md          # After refinement
  {topic}.draftN.md          # Final validated draft
  {topic}.draftN-formatted.md  # RC-ready markdown
  {topic}.draftN-FACT-CHECK-REPORT.md  # Validation report
  {topic}.rc1.docx           # Release candidate
  {topic}.rcN.docx           # Final publication version
```

### Visual Content
```
docs/writing/{topic}/visuals/{visual-name}/
  {visual-name}.content.md   # Source data
  {visual-name}.prompt.md    # Generation instructions
  {visual-name}-1.png        # Variant 1
  {visual-name}-N.png        # Variant N
  {visual-name}-1.webp       # Converted for evaluation
  {visual-name}.eval.md      # Evaluation report
```

### Research Files
```
docs/research/{topic}/
  {topic}.sources.md         # Tier-classified source catalog
  {topic}.research.md        # Claim extraction and notes
```

## Quality Standards

### Data Accuracy
- ✅ **90%+ claim verification** against primary sources
- ✅ **Identical claims use identical data** across all occurrences
- ✅ **All sources at DOCUMENT END** (NOT sectional placement)
- ✅ **No orphan claims** (statistics without attribution)

### Narrative Quality
- ✅ **30-40% conciseness** vs academic style
- ✅ **15-word avg sentence length** (vs 24+ academic)
- ✅ **Bold headers** for scanability
- ✅ **Question alignment** (no sideramps)
- ✅ **100% information preservation** (conciseness without loss)

### Visual Quality
- ✅ **90%+ evaluation score** (EventAI style + best practices + data accuracy)
- ✅ **EventAI brand compliance** (color palette, typography, festival context)
- ✅ **Tufte principles** (data-ink ratio, graphical integrity, minimal cruft)
- ✅ **Accessibility** (WCAG AA, 4.5:1 contrast, non-color-dependent)
- ✅ **Context-aware** (embedded vs standalone evaluation)

### Publication Standards
- ✅ **PNG format for DOCX** (NOT webp - unsupported)
- ✅ **7-inch image width** via `{width=7in}` markdown syntax
- ✅ **Justified body text** (headings left-aligned)
- ✅ **~20MB file size** confirms images embedded (not linked)

## Tier-Aware Visual Framework

### Concise Tier (Minimal Detail)
- **Text Pattern**: 3-5 words per bullet (labels only, NO drilldown)
- **Structural Metrics**: 8-12 concepts, 1-2 depth, complexity ≤50
- **White Space**: 40%+ required
- **Comprehension**: 15-30 seconds
- **Use Case**: Social media, quick reference, high-level overview

### Standard Tier (Balanced Detail) ← DEFAULT
- **Text Pattern**: 10-15 words per bullet (brief descriptors, one level of detail)
- **Structural Metrics**: 12-20 concepts, 2-3 depth, complexity 50-100
- **White Space**: 30% target
- **Comprehension**: 30-60 seconds
- **Use Case**: Embedded textbook visuals, presentations, most infographics

### Detailed Tier (Comprehensive)
- **Text Pattern**: 15-30 words per bullet (multi-level explanations, case studies)
- **Structural Metrics**: 20-30+ concepts, 3-4+ depth, complexity 100-200+
- **White Space**: 25%+ acceptable
- **Comprehension**: 2-3 minutes close reading
- **Use Case**: Educational annotations, technical deep-dives, reference materials

## Workflow Evidence

**Current Implementation Visible In:**
- **Personalization Section**: [docs/writing/3-personalization/](../writing/3-personalization/)
  - Drafts 1-9: Complete narrative progression
  - RC1-3: Publication-ready DOCX files
  - 5 visual directories: decision-framework, engagement-metrics, failure-patterns, helpful-intrusive, three-paths
  - Evaluation reports: Quantitative visual quality assessment

## Directory Structure

```
lemmy/
├── prompts/           # Reusable prompt templates (.prompt.md files)
│   └── notebooklm/    # NotebookLM-specific prompts for infographics
├── research/          # Platform capability research
│   ├── infographics-best-practices.md  # Tufte principles + professional standards
│   └── visual-prompt-density-tiers.md  # Tier framework documentation
├── workflows/         # Process documentation
│   └── CONTENT-PIPELINE-WBS-SUMMARY.md  # Complete WBS (23 tasks, 6 phases)
└── style-guide/       # Visual identity and design standards
    └── eventai-visual-identity.md  # Brand colors, typography, festival context
```

## Getting Started

### For Content Creation
1. **Read**: [style-guide/eventai-visual-identity.md](style-guide/eventai-visual-identity.md) - Brand standards
2. **Read**: [research/infographics-best-practices.md](research/infographics-best-practices.md) - Design principles
3. **Execute**: `/section-create` - Complete authoring workflow
4. **Review**: [workflows/CONTENT-PIPELINE-WBS-SUMMARY.md](workflows/CONTENT-PIPELINE-WBS-SUMMARY.md) - Detailed WBS

### For Visual Content
1. **Plan**: Identify 3-5 infographic opportunities (comparisons, timelines, frameworks)
2. **Generate Prompt**: `/ig-generate-prompt` (select tier: concise/standard/detailed)
3. **Validate**: `/test-visual-prompt-density` (CLI validation)
4. **Generate**: `gemini-generate --content X --prompt Y --variants 3`
5. **Convert**: `todd-image-convert *.png --resolution 1080p --output-format webp`
6. **Evaluate**: `/ig-evaluate *.webp` (quantitative scoring)
7. **Integrate**: `/narrative-add-media` (embed winner into draft)

### For Publishing
1. **Validate**: `/validate` (ensure 90%+ accuracy)
2. **Format**: Update image refs to PNG, add `{width=7in}`, sources at END
3. **Generate**: `pandoc X.md -o Y.docx --resource-path=../visuals`
4. **Justify**: `python3 justify_docx.py Y.docx`
5. **Verify**: File size ~20MB (confirms images embedded)

## Best Practices

### Do ✅
- **Always validate BEFORE generating visuals** (correct data first)
- **Load `/infographics-bestpractices` BEFORE creating prompts**
- **Use tier-appropriate text patterns** (concise: 3-5 words, standard: 10-15)
- **Convert PNG → WebP before evaluation** (consistency)
- **Sources at DOCUMENT END ONLY** (NOT sectional placement)
- **Keep utility scripts for reuse** (justify_docx.py in drafts/)

### Don't ❌
- **Don't generate visuals before validation** (regenerate after errors)
- **Don't skip evaluation** (pick variant without scoring)
- **Don't create RC from unvalidated draft** (data errors in published doc)
- **Don't use sectional source placement** (violates document-end standard)
- **Don't use WebP in DOCX** (format not supported, use PNG)
- **Don't over-specify concise prompts** (causes tier inflation)

## WBS Summary

**Epic**: EventAI Academic Content Creation Pipeline - Complete Documentation (eventai-jwc)

**Statistics**:
- **Total Tasks**: 23 (1 epic + 22 tasks)
- **Phase 1**: 1 task (Question & Requirements)
- **Phase 2**: 2 tasks (Deep Research)
- **Phase 3**: 3 tasks (Narrative Generation)
- **Phase 4**: 6 tasks (Visual Content - most complex)
- **Phase 5**: 2 tasks (Media Integration)
- **Phase 6**: 4 tasks (Final Publishing)
- **Supporting**: 5 tasks (Commands, file structures, quality standards, integration, best practices)

**Status**: Documentation in Progress
**Priority**: P2 (all tasks), P1 (final comprehensive doc)
**Dependencies**: Final doc (eventai-opk5) depends on 13 key tasks

---

**Created**: January 6, 2026
**Purpose**: Detailed implementation specifications for current Lemmy prototype
**Note**: This is implementation-specific and will evolve as the system matures
