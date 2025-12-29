# Lemmy Workflows

This directory contains process documentation for content generation workflows using the Lemmy multi-AI system. Workflows describe **when** to use which tools, **how** to orchestrate between platforms, and **what** outputs to expect.

## Workflow Categories

### Research Workflows
*When you need to gather information*

- **Deep Research**: Using NotebookLM Deep Research for comprehensive topic exploration
- **Quick Research**: Using Perplexity or Claude for focused questions
- **Literature Review**: Systematic academic and industry research
- **Source Validation**: Verifying quality and credibility of sources

### Content Generation Workflows
*When you need to create deliverables*

- **Audio/Video Content**: NotebookLM overview generation
- **Slide Decks**: NotebookLM presentation creation
- **Infographics**: NotebookLM visual data representation
- **Written Content**: Claude/ChatGPT/Gemini for text generation
- **Visual Assets**: Nano Banana for custom imagery

### Hybrid Workflows
*Combining multiple AI platforms*

- **Research → Content**: Deep Research → Audio Overview
- **Text → Visuals**: Written content → Infographics + images
- **Draft → Polish**: Claude draft → NotebookLM multimedia
- **Concept → Execution**: Outline → Full multi-format content

## Workflow Structure

Each workflow document should include:

```markdown
# [Workflow Name]

## Purpose
[What this workflow achieves]

## When to Use
[Specific scenarios and triggers]

## Tools Involved
[Which AI platforms and in what order]

## Prerequisites
[What you need before starting]

## Step-by-Step Process
[Detailed numbered steps with decision points]

## Expected Outputs
[What you'll have when done]

## Tips & Troubleshooting
[Common issues and solutions]

## Examples
[Real usage scenarios from EventAI]
```

## Automation Levels

Workflows are categorized by automation potential:

### 🤖 Fully Automated (Claude Code)
Claude Code can execute end-to-end:
- File operations
- Research using web search
- Content drafting
- Template filling

### ⚙️ Partially Automated (Playwright + Manual)
Some steps automated, some require manual intervention:
- NotebookLM content generation (if Playwright works)
- Download management
- Quality review
- Final adjustments

### 👤 Manual (Guided by Prompts)
Human-executed with prompt templates:
- NotebookLM customization options
- Nano Banana image refinement
- Creative decisions
- Final approval

## Key Workflows (To Be Created)

### 1. NotebookLM Audio Overview Generation
**Automation**: ⚙️ Partially Automated
- Upload sources to NotebookLM
- Configure Audio Overview settings
- Generate overview
- Download and integrate

### 2. Education Curriculum Visual Content
**Automation**: 🤖 Fully Automated (Claude Code) + 👤 Manual (NotebookLM)
- Claude Code generates curriculum outline
- Identify infographic opportunities
- Create NotebookLM sources
- Generate infographics
- Integrate into curriculum document

### 3. Research → Multi-Format Content
**Automation**: ⚙️ Partially Automated
- Deep Research in NotebookLM
- Export research findings
- Generate audio overview
- Create slide deck
- Generate infographic
- Synthesize into comprehensive package

### 4. Consistent Visual Asset Generation
**Automation**: 🤖 Fully Automated (if using API)
- Define visual requirements
- Apply style guide parameters
- Generate images via Nano Banana
- Batch process for consistency
- Quality review and selection

## Integration Points

### Claude Code ↔️ NotebookLM
- Claude Code prepares source documents
- Human uploads to NotebookLM
- Human generates content
- Claude Code (or Playwright) downloads results
- Claude Code integrates into documentation

### Claude Code ↔️ Nano Banana
- Claude Code generates image prompts
- API call to Nano Banana (if available)
- Claude Code processes results
- Integration into content

### Manual Handoff Points
Where human intervention is required:
- Creative decisions on visual style
- Quality assessment of generated content
- Final approval before publication
- Platform-specific customization

## Workflow Templates (To Be Created)

- `research-workflow.md` - Comprehensive research process
- `notebooklm-audio.md` - Audio overview generation
- `notebooklm-slides.md` - Slide deck creation
- `notebooklm-infographic.md` - Infographic generation
- `image-generation.md` - Nano Banana workflow
- `multi-format-content.md` - Combined content generation
- `eventai-integration.md` - EventAI-specific workflows

## Current Status

- ✅ Workflow structure established
- 📋 Individual workflows to be documented
- 🔄 Automation evaluation in progress (Playwright)

## Related Documentation

- **Main Lemmy Guide**: [../README.md](../README.md)
- **Prompt Templates**: [../prompts/](../prompts/)
- **Research**: [../research/](../research/)
- **Style Guide**: [../style-guide/README.md](../style-guide/README.md)
