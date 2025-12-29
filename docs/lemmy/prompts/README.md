# Lemmy Prompt Templates

This directory contains reusable prompt templates for content generation across multiple AI platforms. All templates use the `.prompt.md` format for consistency and easy discovery.

## Directory Organization

### [notebooklm/](notebooklm/)
NotebookLM-specific prompts for rich media generation:
- `audio-overview.prompt.md` - Customizable audio overview generation
- `video-overview.prompt.md` - Video overview with visual customization
- `slide-deck.prompt.md` - Presentation slide generation
- `infographic.prompt.md` - Infographic creation with style controls
- `deep-research.prompt.md` - Deep research request configuration

### [images/](images/)
Image generation prompts for visual content:
- `nano-banana.prompt.md` - Gemini 3 Pro (Nano Banana) image generation
- `diagram.prompt.md` - Technical diagram generation
- `illustration.prompt.md` - Conceptual illustration prompts
- `icon-set.prompt.md` - Icon and symbol generation

### [research/](research/)
Research-focused prompts for content gathering:
- `deep-research.prompt.md` - Structured research requests
- `literature-review.prompt.md` - Academic and industry research
- `competitive-analysis.prompt.md` - Comparative research
- `source-validation.prompt.md` - Source quality assessment

### [general/](general/)
Cross-platform prompts that work across multiple AI tools:
- `summary.prompt.md` - Content summarization
- `outline.prompt.md` - Document outlining
- `expansion.prompt.md` - Content expansion and elaboration
- `simplification.prompt.md` - Complexity reduction

## Template Format

All `.prompt.md` files follow this structure:

```markdown
# [Template Name]

**Platform**: [NotebookLM | Nano Banana | Multi-platform]
**Output**: [Expected output type]
**Customization**: [Low | Medium | High]

## Purpose
[Brief description of what this template generates]

## Usage Instructions
[Step-by-step instructions for using this prompt]

## Customization Options
[All available parameters and settings]

## Template

[The actual prompt text with {{PLACEHOLDERS}}]

## Examples
[1-2 example use cases with filled-in placeholders]

## Tips & Best Practices
[Platform-specific guidance and limitations]
```

## Using Templates

1. **Find the right template**: Check [INDEX.md](INDEX.md) for categorized listing
2. **Read usage instructions**: Understand platform requirements and limitations
3. **Customize the template**: Fill in placeholders with your specific content
4. **Copy to AI platform**: Paste into NotebookLM, Claude, etc.
5. **Iterate**: Adjust based on results and platform feedback

## Creating New Templates

When adding new prompt templates:

1. Use the standard `.prompt.md` format above
2. Include comprehensive customization options
3. Document all platform-specific requirements
4. Provide at least one working example
5. Update the [INDEX.md](INDEX.md) file
6. Test the template on the target platform

## Related Documentation

- **Main Lemmy Guide**: [../README.md](../README.md)
- **Prompt Index**: [INDEX.md](INDEX.md)
- **Style Guide**: [../style-guide/README.md](../style-guide/README.md)
- **Workflows**: [../workflows/](../workflows/)
