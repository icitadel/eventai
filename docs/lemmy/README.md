# Lemmy (LMy): Multi-AI Learning Management System

**Lemmy** is EventAI's orchestration system for generating rich educational content across multiple AI platforms. It establishes workflows, templates, and visual standards for creating comprehensive learning materials with dense visual integration.

## Philosophy

- **Multi-AI Orchestration**: Leverage the unique strengths of each AI platform (NotebookLM for rich media, Nano Banana for directed imagery, etc.)
- **Visual Density**: Balance professional presentation with whimsical distinctiveness
- **Reusability**: Build once, use everywhere through comprehensive prompt templates
- **Integration**: Seamless handoffs between Claude Code automation and manual AI tool usage

## Directory Structure

```
lemmy/
├── prompts/           # Reusable prompt templates (.prompt.md files)
│   ├── notebooklm/    # NotebookLM-specific prompts (Audio, Video, Slides, Infographics)
│   ├── images/        # Image generation prompts (Nano Banana, etc.)
│   ├── research/      # Research-focused prompts (Deep Research, etc.)
│   └── general/       # Cross-platform prompts
├── research/          # Platform capability research and documentation
│   ├── notebooklm/    # NotebookLM capabilities, features, limitations
│   ├── nano-banana/   # Gemini 3 Pro image generation research
│   ├── gemini/        # Gemini content generation research
│   ├── claude/        # Claude content generation research
│   ├── chatgpt/       # ChatGPT content generation research
│   └── perplexity/    # Perplexity research capabilities
├── workflows/         # Process documentation and workflow guides
├── style-guide/       # Visual identity, design standards, consistency rules
└── examples/          # Reference implementations and sample outputs
```

## Key Components

### 1. NotebookLM Integration (Primary Focus)
- Audio/Video Overview generation
- Slide Deck creation
- Infographic generation
- Deep Research capabilities
- Potential Playwright automation

### 2. Visual Content Strategy
- **Style**: Professional + Whimsy balance, minimal cruft
- **Density**: Rich visual accompaniment to text and tables
- **Consistency**: Unified visual language across all content
- **Formats**: Infographics, diagrams, illustrations, slide decks

### 3. Prompt Template Library
- Comprehensive `.prompt.md` files with all customization options
- Indexed for easy discovery and use
- Platform-specific and cross-platform templates
- Usage instructions and examples

### 4. Workflow Documentation
- Research workflows (when to use which AI)
- Content generation workflows (step-by-step processes)
- Claude Code-assisted automation
- Manual processes for NotebookLM and other tools

## Getting Started

1. **For Research Tasks**: See [workflows/research-workflow.md](workflows/research-workflow.md)
2. **For Visual Content**: See [style-guide/README.md](style-guide/README.md)
3. **For Prompt Templates**: See [prompts/INDEX.md](prompts/INDEX.md)
4. **For Platform Capabilities**: See [research/](research/)

## EventAI Integration

Lemmy is specifically designed to support EventAI's educational content needs:
- Education curriculum visualizations
- Research documentation enhancement
- Multi-format content delivery (print, digital, audio/video)
- Consistent branding across all materials

## Contributing

When adding new prompts or workflows:
1. Use the `.prompt.md` format for all prompt templates
2. Update the appropriate INDEX.md file
3. Include examples and customization options
4. Document limitations and best practices

## Related Documentation

- Main research workflow: [docs/research/README.md](../research/README.md)
- EventAI project overview: [README.md](../../README.md)
- Beads issue tracker: `bd list --status=open | grep -i lemmy`
