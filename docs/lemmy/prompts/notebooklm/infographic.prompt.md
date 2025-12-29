# NotebookLM Infographic Prompt Template

**Platform**: NotebookLM (Nano Banana Pro)
**Output**: Single-page visual infographic (PNG/image file)
**Customization**: Medium
**Generation Time**: 30-60 seconds

## Purpose
Transform complex information into a single engaging visual summary. Perfect for creating quick-reference materials, visual abstracts, process diagrams, and data visualizations that accompany text-heavy content.

## Usage Instructions

### Step 1: Upload Sources
1. Go to your NotebookLM notebook
2. Add relevant sources containing the information to visualize
3. Ensure sources have clear structure and data

### Step 2: Configure Infographic
1. Click "Generate" in the Studio panel
2. Select "Infographic"
3. Click the pencil icon (Customize) before generating

### Step 3: Apply This Template
Copy the steering prompt below and paste into the customization panel.

### Step 4: Set Options
- **Language**: Select output language (80+ supported)
- **Detail Level**: Concise | Standard | Detailed (beta)
- **Orientation**: Square | Portrait | Landscape

### Step 5: Generate and Download
1. Click "Generate"
2. Wait ~30 seconds (generates in background)
3. Download image file when ready
4. **⚠️ Review for accuracy** - AI-generated visuals may contain errors

---

## Customization Template

### Template: Process Flow

```
Create an infographic showing the process of {{PROCESS_NAME}}.

Visualize these steps:
1. {{STEP_1}}
2. {{STEP_2}}
3. {{STEP_3}}
4. {{STEP_4}}

Highlight decision points and key transitions.
{{ADDITIONAL_VISUAL_ELEMENTS}}

Style: {{CLEAN|DETAILED|MODERN}}
Emphasis: {{WHAT_TO_HIGHLIGHT}}
```

### Template: Concept Overview

```
Visualize the key concepts of {{TOPIC}}.

Main components to show:
- {{COMPONENT_1}}: {{DESCRIPTION}}
- {{COMPONENT_2}}: {{DESCRIPTION}}
- {{COMPONENT_3}}: {{DESCRIPTION}}

Show relationships between: {{RELATIONSHIP_DESCRIPTION}}

Include: {{EXAMPLES|STATISTICS|QUOTES}}

Target audience: {{AUDIENCE}} - adjust complexity accordingly
```

### Template: Data Visualization

```
Create a data-driven infographic about {{DATA_TOPIC}}.

Key statistics to feature:
- {{STAT_1}}
- {{STAT_2}}
- {{STAT_3}}

Comparison points:
{{WHAT_TO_COMPARE}}

Visualize trends: {{TREND_DESCRIPTION}}

Use {{BAR_CHARTS|PIE_CHARTS|TIMELINES|COMPARISON_TABLES}} where appropriate.
```

### Template: EventAI Educational Infographic

```
Create an educational infographic for {{CURRICULUM_SECTION}} in the EventAI "AI in Festivals" curriculum.

Visual goals:
- Explain {{MAIN_CONCEPT}} clearly for festival professionals
- Show {{PRACTICAL_APPLICATION}}
- Highlight {{CRITICAL_CONSIDERATION}}

Include:
- Real-world festival examples
- Decision-making framework
- Key takeaways

Style: Professional with whimsical touches (EventAI brand)
Avoid: Generic corporate styling, excessive decoration
Balance: Information density with visual clarity

Target audience: Festival organizers (mixed technical backgrounds)
```

---

## Examples

### Example 1: Privacy Ethics Decision Framework

**Filled Template**:
```
Create an educational infographic for Privacy & Surveillance Ethics in the EventAI "AI in Festivals" curriculum.

Visual goals:
- Explain the decision framework for evaluating AI surveillance at festivals
- Show practical application: when to use facial recognition vs. alternative methods
- Highlight critical consideration: attendee consent and data protection laws

Include:
- Real-world festival examples (security vs. privacy trade-offs)
- Decision-making flowchart (evaluate need → assess privacy impact → choose approach)
- Key takeaways (legal requirements, ethical best practices)

Style: Professional with whimsical touches (EventAI brand)
Avoid: Generic corporate styling, excessive decoration
Balance: Information density with visual clarity

Target audience: Festival organizers (mixed technical backgrounds)
```

**Settings**:
- Language: English
- Detail: Detailed
- Orientation: Portrait

**Use Case**: Accompanies privacy curriculum section, provides quick-reference visual for decision-making process

---

### Example 2: AI Implementation Timeline

**Filled Template**:
```
Create an infographic showing the process of implementing AI personalization at festivals.

Visualize these steps:
1. Pre-Event: Data collection strategy and consent framework
2. Setup: System integration and testing
3. During Event: Real-time personalization delivery
4. Post-Event: Analysis and privacy compliance

Highlight decision points: attendee opt-in, data usage boundaries, system failure fallbacks
Show key transitions between planning, execution, and evaluation phases

Style: Clean and modern
Emphasis: Timeline flow and decision points at each stage
```

**Settings**:
- Language: English
- Detail: Standard
- Orientation: Landscape

**Use Case**: Visual timeline for personalization implementation chapter

---

### Example 3: Concept Comparison

**Filled Template**:
```
Visualize the key concepts of AI-powered vs. Traditional Festival Operations.

Main components to show:
- AI-Powered: Predictive analytics, automated decision-making, real-time adaptation
- Traditional: Manual planning, fixed schedules, reactive problem-solving
- Hybrid Approach: Human oversight with AI assistance, selective automation

Show relationships between: How AI augments rather than replaces human decision-making

Include: Statistics on efficiency gains, examples of successful hybrid implementations

Target audience: Festival organizers new to AI - emphasize practical differences, not technical details
```

**Settings**:
- Language: English
- Detail: Standard
- Orientation: Square

**Use Case**: Visual comparison for transformation curriculum section

---

## Configuration Guide

### Detail Level Selection

| Level | Best For | Typical Content |
|-------|----------|----------------|
| **Concise** | Quick overviews, simple concepts | 3-5 key points, minimal text |
| **Standard** | General use, balanced approach | 5-8 key points, moderate text |
| **Detailed** | Complex topics, comprehensive summaries | 8+ key points, rich text (beta) |

### Orientation Selection

| Orientation | Best For | Aspect Ratio |
|-------------|----------|--------------|
| **Square** | Social media, embedded images | 1:1 |
| **Portrait** | Print documents, vertical scroll | 2:3 or 3:4 |
| **Landscape** | Presentations, wide displays | 16:9 or 4:3 |

### Language Considerations
- 80+ languages supported
- Visual elements adapt to language (text direction, cultural symbols)
- Test output for cultural appropriateness

---

## Tips & Best Practices

### Source Preparation
✅ **Do**: Include structured data (lists, tables, statistics)
✅ **Do**: Provide clear headings and sections in sources
✅ **Do**: Include specific examples and case studies
❌ **Don't**: Use overly dense academic papers without key points extraction
❌ **Don't**: Mix too many unrelated topics (one focused topic per infographic)

### Steering Prompts
✅ **Do**: Specify desired visual elements (flowcharts, timelines, comparisons)
✅ **Do**: Mention what to emphasize or highlight
✅ **Do**: Request specific style preferences
❌ **Don't**: Overly prescribe exact layout (AI determines best visual structure)
❌ **Don't**: Request impossible data visualization (AI will hallucinate)

### Visual Quality
- **Information Density**: More sources = richer infographic, but risk of clutter
- **Focused Topic**: Single clear topic = cleaner visual
- **Structural Sources**: Well-organized sources = better layout
- **Review Required**: Always check for visual/factual accuracy

### Common Issues and Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Too cluttered | Too many sources or concepts | Narrow focus, use Concise detail level |
| Too simple | Insufficient source detail | Add more comprehensive sources, use Detailed level |
| Wrong visual type | Unclear prompt about desired format | Specify: "Create a flowchart" or "Show as timeline" |
| Factual errors | AI hallucination | Always review, cross-check data against sources |
| Poor composition | Weak source structure | Reorganize sources with clear headings |

### EventAI Style Integration

**Professional + Whimsy Balance**:
- Request "clean, modern design" (professional)
- Add "with distinctive visual personality" (whimsy)
- Avoid "corporate" or "generic stock imagery"
- Emphasize "festival context" for appropriate metaphors

**Minimal Cruft Principle**:
- Request "essential information only"
- Avoid "decorative borders" or "unnecessary gradients"
- Emphasize "white space and visual breathing room"

**Distinctive Identity**:
- Mention "EventAI brand" in prompt
- Request "memorable visual metaphors"
- Specify "festival-relevant imagery"

---

## Integration with Lemmy Workflow

### Claude Code Preparation
1. Claude Code identifies infographic-worthy content in curriculum
2. Claude Code prepares structured source document (headings, lists, data)
3. Claude Code generates steering prompt using this template
4. Claude Code specifies orientation based on document placement

### Manual NotebookLM Step
5. User uploads structured source to NotebookLM
6. User pastes steering prompt
7. User selects detail level, orientation, language
8. User generates infographic
9. **User reviews for accuracy and brand alignment**
10. User downloads image file

### Claude Code Integration
11. Claude Code receives downloaded infographic file
12. Claude Code embeds in curriculum at designated location
13. Claude Code adds alt text for accessibility
14. Claude Code documents in image asset inventory

### Quality Control
- Manual review required (AI-generated visuals may have errors)
- Check data accuracy against sources
- Verify visual style aligns with EventAI brand
- Ensure accessibility (contrast, text legibility)

---

## Automation Considerations

### Playwright Automation Potential
✅ **Feasible**: Trigger generation
✅ **Feasible**: Set detail/orientation/language options
❓ **Unknown**: Download automation (needs testing)
❌ **Not Feasible**: Quality review (requires human judgment)

### Automation Workflow
```python
# Pseudocode for future automation
generate_infographic(
    sources=["structured-content.pdf"],
    prompt=filled_template,
    detail="Detailed",
    orientation="Portrait",
    language="English"
)
download_path = wait_and_download()
# Human review step here
integrate_into_docs(download_path)
```

---

## Related Prompts
- [Slide Deck](slide-deck.prompt.md) - Multi-slide presentation format
- [Video Overview](video-overview.prompt.md) - Animated visual explanation
- [Nano Banana](../images/nano-banana.prompt.md) - Custom image generation

---

## Accessibility Notes

When using infographics in EventAI curriculum:
1. Always provide text alternative (alt text)
2. Ensure sufficient color contrast
3. Don't rely solely on color to convey information
4. Consider providing transcript of information
5. Test readability at different sizes

---

*Template Version: 1.0*
*Last Updated: December 28, 2025*
*Part of: Lemmy Prompt Library*
