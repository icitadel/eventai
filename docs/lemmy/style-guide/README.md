# Lemmy Visual Style Guide

This directory defines the visual identity for all EventAI educational content generated through the Lemmy system. The goal is to create a distinctive, consistent look that balances **professional credibility** with **whimsical approachability**.

## Core Principles

### 1. Professional + Whimsy Balance
- **Professional**: Clean layouts, readable typography, proper data visualization
- **Whimsy**: Playful color accents, distinctive illustrations, memorable visual metaphors
- **NOT**: Corporate blandness OR childish unprofessionalism

### 2. Minimal Cruft
- Every visual element must serve a purpose
- Avoid decorative borders, unnecessary gradients, generic stock imagery
- White space is valuable - don't fill every gap
- Simplicity over complexity

### 3. Distinctive Identity
- Immediately recognizable as EventAI content
- Unique visual voice in the AI/event tech space
- Memorable without being gimmicky

### 4. Dense Visual Integration
- Text should be accompanied by relevant visuals
- Tables and data benefit from inline charts/graphs
- Diagrams and infographics break up long sections
- Balance: visuals enhance, not distract

## To Be Defined

This section will be populated with:

### Color Palette
- Primary colors (brand identity)
- Secondary colors (accents, highlights)
- Data visualization colors (charts, graphs)
- Accessibility considerations (contrast ratios)

### Typography
- Heading fonts (professional yet distinctive)
- Body fonts (readable, friendly)
- Code/technical fonts
- Size hierarchy and spacing

### Visual Elements
- Icon style and design language
- Illustration style (flat, semi-flat, isometric?)
- Diagram conventions (flowcharts, architecture diagrams)
- Infographic templates

### Layout Standards
- Grid systems for slides and infographics
- Margin and padding standards
- Alignment and spacing rules
- Responsive considerations for digital vs. print

### Content-Specific Styles
- **Slide Decks**: Title slide, content slide, section divider templates
- **Infographics**: Data visualization, process flows, comparison charts
- **Diagrams**: Technical architecture, concept maps, timelines
- **Illustrations**: Conceptual imagery, metaphors, character design?

## Research Needed

Before defining the style guide, we need:

1. **Infographics Best Practices Research** (eventai-6x7)
   - Print-ready design standards
   - Data visualization principles
   - Accessibility in visual design
   - Dense visual integration techniques

2. **Platform Capability Research**
   - What styles can NotebookLM generate?
   - What controls does Nano Banana offer?
   - Can we enforce consistency across platforms?

3. **Reference Analysis**
   - What works well in AI/tech education?
   - What makes content memorable yet professional?
   - How do others balance whimsy + credibility?

## File Structure (To Be Created)

```
style-guide/
├── README.md              # This file
├── color-palette.md       # Color definitions and usage
├── typography.md          # Font choices and hierarchy
├── visual-elements.md     # Icons, illustrations, diagrams
├── layout-standards.md    # Grid, spacing, alignment
├── slide-templates.md     # Slide deck design standards
├── infographic-templates.md  # Infographic design patterns
├── examples/              # Reference implementations
│   ├── good/              # What to do
│   └── avoid/             # What not to do
└── assets/                # Reusable design assets
    ├── colors/            # Color swatches
    ├── icons/             # Icon library
    └── templates/         # Template files
```

## Integration with Prompts

Once the style guide is defined, it will inform:

- **NotebookLM prompts**: Style specifications for infographics and slides
- **Nano Banana prompts**: Consistent image generation parameters
- **General templates**: Visual layout expectations
- **Quality criteria**: What "good" looks like for generated content

## Dependencies

This style guide depends on:
- ✅ Directory structure created
- 🔄 Infographics best practices research (eventai-6x7)
- 🔄 NotebookLM capability research (what styles are possible?)
- 🔄 Nano Banana research (what controls exist?)

## Related Documentation

- **Main Lemmy Guide**: [../README.md](../README.md)
- **Prompt Templates**: [../prompts/](../prompts/)
- **Research**: [../research/](../research/)
- **Workflows**: [../workflows/](../workflows/)
