# EventAI Academic Content Creation Pipeline - Work Breakdown Structure (WBS)

**Epic:** EventAI Academic Content Creation Pipeline - Complete Documentation
**Epic ID:** eventai-jwc
**Priority:** P2
**Status:** Open

---

## 📋 Executive Summary

This WBS provides an exhaustive examination and documentation of the EventAI academic content creation pipeline. The pipeline transforms a question into a publication-ready DOCX document through 6 major phases, integrating deep research, narrative refinement, visual content generation, and rigorous validation.

### Pipeline Overview

```
Question → Research → Draft → Validate → Visualize → Integrate → Publish
   ↓          ↓         ↓         ↓          ↓          ↓          ↓
  Specs    Sources   Narrative  Facts    Infographics  Media    DOCX RC
```

### Success Criteria

- ✅ Complete documentation of all 6 phases
- ✅ All CLI tools documented (gemini-generate, todd-image-convert, docutil)
- ✅ All Claude commands/skills documented
- ✅ Workflow diagrams and examples
- ✅ Current implementation fully described
- ✅ File structures and naming conventions documented
- ✅ Integration points between phases clear
- ✅ 90%+ data accuracy validation
- ✅ 90%+ visual quality scores
- ✅ Publication-ready DOCX output

---

## 🎯 Phase 1: Question & Requirements Definition

**Tasks:**

### eventai-r9z: Phase 1.1 - Document question formulation & output specifications
**Priority:** P2 | **Status:** Open

**Scope:**
- Question format and requirements
- Length specifications (2000 words target)
- Voice specifications (casual for university academic textbook)
- Structure requirements (overview, 3-5 major points, conclusion)
- Narrative requirements (central thesis, no sideramps)
- Visual requirements (3-5 concise infographics)

**Key Deliverables:**
- Question formulation guidelines
- Output specification templates
- Examples from existing sections

---

## 🔬 Phase 2: Deep Research & Knowledge Assembly

**Tasks:**

### eventai-d99: Phase 2.1 - Document deep research process & knowledge assembly
**Priority:** P2 | **Status:** Open

**Scope:**
- Multiple-pass research approach
- Source discovery and cataloging (*.sources.md format)
- Research note-taking (*.research.md format)
- Claim extraction and verification
- Source tier classification (Tier 1-4)
- Alternative approaches and impact/tradeoffs
- Knowledge synthesis methods

**Key Deliverables:**
- *.sources.md structure documentation
- *.research.md structure documentation
- Source tier classification criteria
- Research workflow examples

### eventai-yo9: Phase 2.2 - Document claim validation & source verification
**Priority:** P2 | **Status:** Open

**Scope:**
- Priority structure (Question Alignment PRIMARY, Data Accuracy SECONDARY)
- 3-step verification process (research.md → sources.md → verify accuracy)
- Consistency checks and formatting standards
- Validation report format
- /validate command usage
- /narrative-refine-validate integration

**Key Deliverables:**
- Validation process documentation
- Fact-check report format
- Source verification workflow
- 90%+ accuracy standards

---

## ✍️ Phase 3: Narrative Generation & Drafting

**Tasks:**

### eventai-64y: Phase 3.1 - Document narrative generation & drafting workflow
**Priority:** P2 | **Status:** Open

**Scope:**
- Draft progression (draft1 → draft2 → ... → draftN)
- Narrative transformation techniques (bullets → prose, conciseness)
- 30-40% conciseness vs academic style target
- Textbook best practices (/textbook-bestpractices)
- Learning objectives, bold headers, scanability
- Second-person address usage
- Question alignment (no sideramps)

**Key Deliverables:**
- Narrative transformation guidelines
- /section-create workflow documentation
- /narrative-refine-validate command documentation
- Draft progression examples

### eventai-hfg: Phase 3.2 - Document iterative refinement & fact-checking
**Priority:** P2 | **Status:** Open

**Scope:**
- Multiple draft iterations
- Fact-check report generation
- Correction application workflow
- 90%+ accuracy target
- Before/after examples
- Word count reduction tracking
- Manual edits and author feedback integration

**Key Deliverables:**
- Iterative refinement workflow
- Fact-check report format ({name}.draftN-FACT-CHECK-REPORT.md)
- Section revision examples ({name}.draftN-SECTION-REVISIONS.md)

### eventai-i7lh: Phase 3.3 - Document /narrative-revise command (revision workflow)
**Priority:** P2 | **Status:** Open

**Scope:**
- Revision workflow vs refinement workflow
- Targeted changes vs complete rewrite
- Integration with /narrative-refine-validate
- Source preservation during revision
- Fact-checking requirements for revised content
- Draft version management during revisions

**Key Deliverables:**
- /narrative-revise command documentation
- Difference from /narrative-refine-validate
- Best practices for content revision
- Quality standards for revised drafts

---

## 🎨 Phase 4: Visual Content Creation

**Tasks:**

### eventai-0vj: Phase 4.1 - Document visual content planning & infographic identification
**Priority:** P2 | **Status:** Open

**Scope:**
- Infographic opportunity identification
- Target: 3-5 visuals per section
- Spacing: Every 500-1000 words
- Visual types (comparison, timeline, framework, chart)
- Context determination (embedded vs standalone)
- Density tier selection (concise, standard, detailed)

**Key Deliverables:**
- Visual planning guidelines
- Folder structure documentation (docs/writing/{topic}/visuals/{visual-name}/)
- VIS-X.X naming convention

### eventai-i2j: Phase 4.2 - Document infographic prompt generation (tier-aware)
**Priority:** P2 | **Status:** Open

**Scope:**
- Density tier framework (concise, standard, detailed)
- Text pattern enforcement (3-5 words for concise, 10-15 for standard)
- CLI validation integration (gemini-generate --validate-prompt)
- EventAI brand compliance
- Embedded vs standalone context adjustments

**Key Deliverables:**
- /ig-generate-prompt command documentation
- Tier-aware prompt templates
- Text pattern enforcement rules
- CLI validation workflow

### eventai-jt2o: Phase 4.2b - Document /test-visual-prompt-density command (tier validation)
**Priority:** P2 | **Status:** Open

**Scope:**
- Density tier validation (concise, standard, detailed)
- Structural metrics (concept count, depth, complexity)
- Text pattern analysis (word counts, drilldown detection)
- CLI validation integration (gemini-generate --validate-prompt)
- Tier inflation detection and correction
- Prompt revision recommendations

**Key Deliverables:**
- /test-visual-prompt-density command documentation
- Validation criteria by tier
- Integration with /ig-generate-prompt workflow
- Examples of passing and failing validations

### eventai-cdg: Phase 4.3 - Document gemini-generate CLI tool (browser automation)
**Priority:** P2 | **Status:** Open

**Scope:**
- Browser automation via Playwright (NOT API)
- Parallel tab generation (3 variants simultaneously)
- Usage patterns and parameters
- Batch parameter for iterative generation
- PNG → WebP automatic conversion (1080p)
- Free unlimited use (no quotas)

**Key Deliverables:**
- gemini-generate CLI documentation
- Installation and setup instructions
- Usage examples and best practices
- Integration with .content.md and .prompt.md

### eventai-yg2: Phase 4.4 - Document todd-image-convert CLI tool
**Priority:** P2 | **Status:** Open

**Scope:**
- Image format conversion (PNG → WebP)
- Resolution presets (1080p, 4k, 720p, original)
- Quality settings (lossless vs lossy)
- Batch processing with parallelization
- Environment setup (pyvips/libvips)

**Key Deliverables:**
- todd-image-convert CLI documentation
- Installation and environment setup
- Resolution and quality guidelines
- Best practices for web vs print

### eventai-usn: Phase 4.5 - Document /ig-evaluate command (quantitative analysis)
**Priority:** P2 | **Status:** Open

**Scope:**
- Context identification (embedded vs standalone) - CRITICAL
- EventAI style compliance scoring
- Best practices adherence (Tufte principles)
- Data accuracy verification
- Accessibility compliance (WCAG AA)
- Comparative evaluation (variant comparison matrix)
- 90%+ score target

**Key Deliverables:**
- /ig-evaluate command documentation
- Evaluation criteria and scorecards
- Context-aware evaluation guidelines
- Evaluation report format ({name}.eval.md)

---

## 🖼️ Phase 5: Media Integration & RC Preparation

**Tasks:**

### eventai-wxh: Phase 5.1 - Document media integration into narrative
**Priority:** P2 | **Status:** Open

**Scope:**
- Image reference format in markdown
- Figure captions and alt text requirements
- Placement spacing (every 500-1000 words)
- Winner selection from evaluated variants
- Source attribution at DOCUMENT END ONLY (NOT sectional)

**Key Deliverables:**
- /narrative-add-media workflow documentation
- Image reference syntax
- Caption and alt text guidelines
- PNG vs WebP usage rules

### eventai-o73: Phase 5.2 - Document RC markdown preparation
**Priority:** P2 | **Status:** Open

**Scope:**
- Strip narrative guidance and statistics
- Update image references to PNG format (NOT webp)
- Add {width=7in} to all image references
- Clean source lists
- Create {name}.draftN-formatted.md

**Key Deliverables:**
- RC markdown preparation guidelines
- PNG format requirements for DOCX
- Source list format standards
- DOCUMENT END source placement enforcement

---

## 📄 Phase 6: Final Publishing

**Tasks:**

### eventai-1jg: Phase 6.1 - Document DOCX generation via Pandoc
**Priority:** P2 | **Status:** Open

**Scope:**
- Pandoc command and parameters
- PNG image embedding (7-inch wide)
- Resource path configuration
- File size validation (~18-20MB confirms embedding)

**Key Deliverables:**
- Pandoc DOCX generation documentation
- PNG embedding workflow
- Resource path configuration
- Quality validation checklist

### eventai-cda: Phase 6.2 - Document justified text alignment utility
**Priority:** P2 | **Status:** Open

**Scope:**
- justify_docx.py utility script
- Python-docx library usage
- Body paragraph justification
- Heading left-alignment preservation
- Reusability across sections

**Key Deliverables:**
- justify_docx.py script documentation
- Installation instructions (python-docx)
- Usage guidelines
- Reusability best practices

### eventai-tg0: Phase 6.3 - Document /section-publish end-to-end workflow
**Priority:** P2 | **Status:** Open

**Scope:**
- Step 1: Narrative refinement + validation
- Step 2: Visual content review
- Step 3: Visual regeneration (if needed)
- Step 4: Release candidate generation
- Quality standards for each step
- Integration between phases

**Key Deliverables:**
- /section-publish workflow documentation
- Integration with all sub-commands
- Error handling and iteration loops
- Success criteria and validation gates

### eventai-cau1: Phase 6.4 - Document /section-revise command (section revision workflow)
**Priority:** P2 | **Status:** Open

**Scope:**
- Complete section revision workflow
- When to use section-revise vs section-create
- Handling existing visuals (keep, regenerate, or remove)
- Source preservation and updating
- Draft version progression during revisions
- Quality validation for revised sections

**Key Deliverables:**
- /section-revise workflow steps
- Integration with narrative-revise and ig-* commands
- Revision checklist and quality gates
- Examples from actual section revisions

---

## 🛠️ Supporting Documentation Tasks

### eventai-bam: Document all Claude commands/skills and their integration
**Priority:** P2 | **Status:** Open

**Scope:**
- All 15+ custom Claude commands
- Purpose and usage for each
- Arguments and parameters
- Integration patterns
- Quality standards

**Key Deliverables:**
- Complete command reference
- Integration matrix
- Usage examples

### eventai-sn8h: Document file structures and naming conventions
**Priority:** P2 | **Status:** Open

**Scope:**
- Directory organization
- File naming conventions
- Draft progression (draft1 → draftN)
- RC naming (rc1 → rcN)
- Visual naming ({name}-1.png → {name}-N.png)
- Report naming conventions

**Key Deliverables:**
- Directory structure documentation
- Naming convention standards
- File format specifications

### eventai-voqi: Document quality standards and success criteria
**Priority:** P2 | **Status:** Open

**Scope:**
- Data accuracy: 90%+ claim verification
- Narrative quality: 30-40% conciseness
- Visual quality: 90%+ evaluation score
- Source attribution standards
- Question alignment requirements
- EventAI brand compliance
- Accessibility standards

**Key Deliverables:**
- Quality standards documentation
- Success criteria for each phase
- Evaluation scorecard templates

### eventai-g8dg: Document workflow integration points and dependencies
**Priority:** P2 | **Status:** Open

**Scope:**
- Integration between phases
- Dependencies and workflow gates
- Research → Drafting
- Validation → Visual Generation
- Visual Evaluation → Draft Integration
- Formatted MD → DOCX

**Key Deliverables:**
- Integration point documentation
- Dependency matrix
- Workflow gate definitions

### eventai-ubi0: Document best practices and anti-patterns
**Priority:** P2 | **Status:** Open

**Scope:**
- Best practices across all phases
- Common anti-patterns to avoid
- Efficiency tips
- Tool usage patterns
- Validation workflows

**Key Deliverables:**
- Best practices guide
- Anti-pattern reference
- Efficiency recommendations

---

## 📚 Final Deliverable

### eventai-opk5: Create comprehensive workflow documentation markdown file
**Priority:** P1 | **Status:** Open

**Dependencies:** ALL phase tasks + supporting tasks (10 dependencies)

**Scope:**
Synthesize all documented phases into a single comprehensive workflow documentation file covering:
- Complete workflow overview
- All 6 phases in detail
- All CLI tools and utilities
- All Claude commands/skills
- File structures and conventions
- Integration points and dependencies
- Quality standards
- Best practices and anti-patterns
- Complete examples and case studies

**Output Location:** `docs/workflows/ACADEMIC-CONTENT-CREATION-PIPELINE.md`

**Structure:**
1. Overview and philosophy
2. Phase 1: Question & Requirements
3. Phase 2: Deep Research
4. Phase 3: Narrative Generation
5. Phase 4: Visual Content Creation
6. Phase 5: Media Integration & RC Prep
7. Phase 6: Final Publishing
8. Tools & Utilities Reference
9. File Structures & Conventions
10. Integration & Dependencies
11. Quality Standards
12. Best Practices & Anti-Patterns
13. Complete Workflow Examples

---

## 📊 WBS Statistics

**Total Tasks:** 23 (1 epic + 22 tasks)

**Phase Breakdown:**
- Phase 1: 1 task
- Phase 2: 2 tasks
- Phase 3: 3 tasks (added narrative-revise)
- Phase 4: 6 tasks (most complex phase - added test-visual-prompt-density)
- Phase 5: 2 tasks
- Phase 6: 4 tasks (added section-revise)
- Supporting: 5 tasks

**Priority Distribution:**
- P1: 1 task (final comprehensive documentation)
- P2: 22 tasks (all phase and supporting tasks)

**Dependencies:**
- eventai-opk5 (final doc) depends on 13 key tasks
- Ensures systematic completion from phases → comprehensive doc

---

## �� Current Implementation Status

### Tools Already Built
✅ **gemini-generate** - Browser automation for infographic generation
✅ **todd-image-convert** - PNG → WebP conversion with pyvips
✅ **docutil** - Document utilities
✅ **justify_docx.py** - Text justification utility

### Claude Commands Already Built
✅ **/section-create** - Complete authoring workflow
✅ **/section-revise** - Revision workflow
✅ **/section-rc** - RC preparation
✅ **/section-publish** - End-to-end publishing
✅ **/narrative-refine-validate** - Refinement + validation + sources
✅ **/narrative-revise** - Revision command
✅ **/narrative-add-media** - Media integration
✅ **/validate** - Content validation
✅ **/ig-generate-prompt** - Tier-aware prompt generation
✅ **/ig-generate** - Automated infographic generation
✅ **/ig-evaluate** - Comprehensive evaluation
✅ **/test-visual-prompt-density** - Tier validation command
✅ **/infographics-bestpractices** - Tufte + EventAI brand
✅ **/textbook-bestpractices** - Academic writing standards
✅ **/todd-image-convert** - Image conversion skill
✅ **/optimize-tokens** - Token optimization
✅ **/commit** - Commit message generation

### Workflow Evidence
✅ **Personalization section** - Complete progression visible
  - Draft 1-9 visible in [docs/writing/3-personalization/drafts/](../../docs/writing/3-personalization/drafts/)
  - RC1-3 generated
  - Multiple visuals created and evaluated
  - Sources cataloged and verified

---

## 🚀 Next Steps

1. **Phase Tasks** (eventai-r9z through eventai-tg0)
   - Document each phase systematically
   - Include examples from personalization section
   - Capture current implementation details

2. **Supporting Tasks** (eventai-bam through eventai-ubi0)
   - Document all commands/skills
   - Define file structures
   - Establish quality standards
   - Map integration points
   - Define best practices

3. **Final Documentation** (eventai-opk5)
   - Synthesize all phase documentation
   - Create comprehensive workflow guide
   - Include complete examples
   - Publish to docs/workflows/

4. **Review & Iteration**
   - Validate against actual workflow usage
   - Gather feedback from users
   - Refine documentation
   - Update as pipeline evolves

---

## 📝 Notes

**Focus:** This WBS documents the **current implementation** and **derived structure** of the existing pipeline. Future milestones will further abstract and generalize the workflow.

**Philosophy:** The pipeline prioritizes **data accuracy** (90%+ claim verification), **visual quality** (90%+ evaluation scores), and **narrative excellence** (30-40% conciseness vs academic) to produce publication-ready academic content.

**Evidence-Based:** All documentation will be grounded in actual implementation visible in [.claude/commands/](../../.claude/commands/) and workflow artifacts in [docs/writing/](../../docs/writing/).

---

**Created:** January 5, 2026
**Epic ID:** eventai-jwc
**Status:** Documentation in Progress