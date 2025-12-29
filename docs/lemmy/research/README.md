# Lemmy Platform Research

This directory contains research documentation on AI platform capabilities for content generation. Each platform is evaluated for its strengths, limitations, optimal use cases, and integration patterns.

## Research Goals

1. **Capability Mapping**: What can each platform do best?
2. **Workflow Integration**: How do platforms complement each other?
3. **Output Quality**: Strengths and weaknesses of generated content
4. **Automation Potential**: Can we automate with Playwright or APIs?
5. **Customization Options**: What controls are available?

## Platform Directories

### [notebooklm/](notebooklm/) 🎯 PRIMARY FOCUS
**Priority**: P1 (Highest)

NotebookLM research focuses on downloadable rich content:
- Audio Overview generation (customization, quality, length)
- Video Overview generation (visual styles, customization)
- Slide Deck creation (themes, formats, export options)
- Infographic generation (styles, complexity, data visualization)
- Deep Research capabilities (scope, depth, source handling)
- Playwright automation feasibility
- Download automation for generated content

**Key Questions**:
- What customization options exist for each content type?
- Can we automate generation and download via Playwright?
- What are the quality/format limitations?
- How do we optimize for EventAI's visual style?

### [nano-banana/](nano-banana/)
**Priority**: P1

Gemini 3 Pro (Nano Banana) image generation research:
- Prompt patterns and effectiveness
- Style controls and consistency
- Quality settings and output formats
- Integration with text content
- Alignment with Lemmy visual style guide
- Batch generation capabilities

### [gemini/](gemini/)
**Priority**: P2

Gemini content generation research:
- Multimodal capabilities (text + image + video)
- Long-form content generation
- Research and summarization strengths
- Integration patterns with other platforms

### [claude/](claude/)
**Priority**: P2

Claude content generation research:
- Extended context usage (200K tokens)
- Research and analysis capabilities
- Code generation for automation
- Integration with Claude Code workflows

### [chatgpt/](chatgpt/)
**Priority**: P2

ChatGPT content generation research:
- Plugin ecosystem for content creation
- DALL-E integration for images
- Canvas feature for iterative editing
- Custom GPT creation for specialized tasks

### [perplexity/](perplexity/)
**Priority**: P2

Perplexity research capabilities:
- Research quality and depth
- Citation handling and source quality
- Integration with content workflow
- When to use vs. other research tools

## Research Template

Each platform research directory should contain:

```
[platform]/
├── README.md              # Overview and key findings
├── capabilities.md        # Detailed capability documentation
├── customization.md       # All customization options
├── limitations.md         # Known limitations and workarounds
├── examples/              # Screenshots and sample outputs
├── automation.md          # Automation possibilities (Playwright, API)
└── integration.md         # How this platform fits in the workflow
```

## Research Process

1. **Manual Exploration**: Hands-on testing of all features
2. **Documentation Review**: Official docs, community resources
3. **Capability Testing**: Generate sample content, test limits
4. **Automation Evaluation**: Feasibility of Playwright/API usage
5. **Integration Design**: How to incorporate into Lemmy workflow

## Priority Matrix

| Platform | Priority | Focus Area | Automation? |
|----------|----------|------------|-------------|
| NotebookLM | P1 | Rich media (audio, video, slides, infographics) | Evaluate |
| Nano Banana | P1 | Image generation, visual consistency | Likely |
| Gemini | P2 | Multimodal content | Medium |
| Claude | P2 | Extended context research | High (Claude Code) |
| ChatGPT | P2 | Plugin ecosystem | Medium |
| Perplexity | P2 | Research quality | Low |

## Current Status

- ✅ Research structure established
- 🔄 NotebookLM research in progress
- 📋 Other platforms queued (P2)

## Related Documentation

- **Main Lemmy Guide**: [../README.md](../README.md)
- **Prompt Templates**: [../prompts/](../prompts/)
- **Workflows**: [../workflows/](../workflows/)
- **Style Guide**: [../style-guide/README.md](../style-guide/README.md)
