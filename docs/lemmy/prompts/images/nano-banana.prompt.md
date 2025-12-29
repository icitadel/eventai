# Nano Banana (Gemini) Image Generation - General Template

**Platform**: Gemini API / Google AI Studio (Nano Banana / Nano Banana Pro)
**Output**: Custom images (PNG)
**Customization**: High
**EventAI Style**: Applied

## Purpose
Generate custom images, diagrams, and illustrations for EventAI curriculum using Gemini's Nano Banana image generation with EventAI visual identity standards.

## Usage Instructions

### Step 1: Choose Image Type
Determine what you need:
- **Diagram**: Technical/conceptual diagrams (flowcharts, system diagrams)
- **Illustration**: Festival scenes, conceptual imagery
- **Icon Set**: Consistent icons for infographics
- **Data Visualization**: Custom charts that can't be done in NotebookLM

### Step 2: Use Appropriate Template Below
Select the template matching your need and fill in placeholders.

### Step 3: Generate via Gemini
- Go to [Google AI Studio](https://aistudio.google.com/)
- Select Imagen 3 or Nano Banana Pro model
- Paste your filled prompt
- Generate (may take 30-60 seconds)
- Download PNG file

### Step 4: Quality Check
- Verify factual accuracy
- Check EventAI style compliance (colors, typography feel)
- Ensure text rendering is legible (if any)
- Review for accessibility

---

## Template 1: Technical Diagram

### Use For
- System architecture diagrams
- Process flowcharts
- Decision trees
- Data flow diagrams

### Template

```
Generate a clean technical diagram showing {{DIAGRAM_SUBJECT}}.

Visual structure:
{{DESCRIBE_LAYOUT - e.g., "left-to-right flow with 4 main stages" or "circular process with 5 steps"}}

Elements to include:
1. {{ELEMENT_1 - e.g., "Input box labeled 'Attendee Data'"}}
2. {{ELEMENT_2}}
3. {{ELEMENT_3}}
{{ADD MORE AS NEEDED}}

Connections:
{{DESCRIBE_RELATIONSHIPS - e.g., "Arrows from Input → Processing → Output, with feedback loop from Output back to Processing"}}

Style: EventAI professional festival industry diagram
- Deep purple (#6B46C1) for AI-related elements
- Electric coral (#FF6B6B) for human elements
- Sky blue (#4299E1) for data flow
- Simple geometric shapes with rounded corners (8-12px radius)
- 2-3px outline stroke, clean lines
- Arrows with triangular heads showing clear directional flow
- Modern sans-serif labels, left-aligned text
- Clean white background, generous spacing between elements
- Semi-flat style with subtle shadows for depth (not 3D)
- Minimal decoration, every element serves a purpose

Festival context: Include small illustrative elements like {{FESTIVAL_ELEMENTS - e.g., "simplified stage icons, tiny crowd silhouettes, wristband symbols"}}.

Image specifications:
- Orientation: {{LANDSCAPE|PORTRAIT|SQUARE}}
- Emphasis: {{WHAT_SHOULD_STAND_OUT}}
- Size: High resolution, suitable for print (minimum 2400x1800px)
```

### Example: DICE Recommendation Flow

**Filled Template**:
```
Generate a clean technical diagram showing how DICE's AI recommendation engine drives 40% of ticket sales.

Visual structure:
Left-to-right flow with 3 main stages: Input → AI Processing → Output, plus a results indicator below.

Elements to include:
1. Input box (left): "Listening History" with musical note icon
2. Input box (left): "Past Attendance" with ticket icon
3. Input box (left): "Social Connections" with people icon
4. Input box (left): "Real-time Availability" with calendar icon
5. Center processing box: "AI Recommendation Algorithm" with sparkle/AI icon
6. Output box (right): "Personalized Festival Suggestions" with list icon
7. Bottom stat box: "40-41% of Sales" in large text

Connections:
Four arrows from input boxes converging into AI processing box, one arrow from processing to output, dashed line from output down to stat box.

Style: EventAI professional festival industry diagram
- Deep purple (#6B46C1) for AI processing box
- Electric coral (#FF6B6B) for stat box with "40-41%"
- Sky blue (#4299E1) for input boxes
- Simple geometric shapes with rounded corners (8-12px radius)
- 2-3px outline stroke, clean lines
- Arrows with triangular heads showing clear directional flow
- Modern sans-serif labels, left-aligned text
- Clean white background, generous spacing between elements
- Semi-flat style with subtle shadows for depth (not 3D)
- Minimal decoration, every element serves a purpose

Festival context: Include small illustrative elements like musical notes near listening history, ticket shape for attendance, wristband icon near availability.

Image specifications:
- Orientation: Landscape
- Emphasis: The 40-41% statistic in electric coral should be the visual anchor
- Size: High resolution, suitable for print (minimum 2400x1800px)
```

---

## Template 2: Festival Scene Illustration

### Use For
- Conceptual imagery for section headers
- Before/After AI comparisons
- Visual metaphors
- Festival context establishment

### Template

```
Create a semi-flat illustration of {{SCENE_DESCRIPTION}} in a festival context.

Scene composition:
{{DESCRIBE_WHAT'S_HAPPENING - e.g., "Outdoor festival with main stage in background, crowd of diverse attendees in foreground, some using mobile devices"}}

Key elements:
- {{ELEMENT_1 - e.g., "Main stage with simplified geometric structure, purple and coral lighting"}}
- {{ELEMENT_2 - e.g., "Diverse crowd silhouettes (varied skin tones, body types, some with accessibility devices)"}}
- {{ELEMENT_3}}
{{ADD MORE AS NEEDED}}

Mood: {{MOOD - e.g., "Energetic but professional, optimistic but not overly cheerful"}}

Style: EventAI professional festival industry illustration
- Modern, simplified semi-flat style with clean 2-3px outlines and rounded corners
- Color palette: deep purple (#6B46C1), electric coral (#FF6B6B), sky blue (#4299E1), warm sunlight (#F6AD55) as accents
- {{PERSPECTIVE - e.g., "Slight isometric perspective" or "Front-facing view" or "Aerial view"}}
- Simplified crowd silhouettes showing diversity (varied skin tones, body types)
- Subtle single-source shading for depth, no heavy 3D effects
- Clean white background
- Distinctive but not cartoonish - appropriate for business/academic audience
- Professional yet energetic mood

Festival-specific details:
- {{FESTIVAL_TECH - e.g., "RFID wristbands visible on some attendees, mobile phones showing festival apps"}}
- {{FESTIVAL_ENV - e.g., "Tents and food vendor structures in background, outdoor setting with sky visible"}}

Avoid: Generic business imagery (suits, offices), clichéd AI imagery (robots, circuit brains), overly realistic detail

Image specifications:
- Orientation: {{LANDSCAPE|PORTRAIT|SQUARE}}
- Focal point: {{WHAT_DRAWS_EYE}}
- Size: High resolution, suitable for print (minimum 2400x1800px)
```

### Example: AI as Festival Conductor

**Filled Template**:
```
Create a semi-flat illustration of AI as a festival conductor orchestrating different festival operations in a festival context.

Scene composition:
Central conductor figure (abstract, not human) made of glowing purple geometric shapes with circuit-like patterns, conducting with a baton. Around the conductor in a semi-circle: 5 "sections" representing different festival operations (crowd management, ticketing, food service, stage operations, security), each shown as simplified icons or mini-scenes.

Key elements:
- Central AI conductor: abstract geometric form in deep purple (#6B46C1) with subtle glow
- Crowd management section: simplified crowd silhouettes with flow arrows (sky blue)
- Ticketing section: ticket icons and phone screens (warm sunlight)
- Food service: vendor tent and food icons (coral)
- Stage operations: stage structure with sound/light elements (purple and coral)
- Security: shield icon with camera (sky blue)
- Musical staff lines connecting all elements to conductor (thin, light gray)

Mood: Professional yet whimsical - serious orchestration concept delivered with creative energy

Style: EventAI professional festival industry illustration
- Modern, simplified semi-flat style with clean 2-3px outlines and rounded corners
- Color palette: deep purple (#6B46C1) for AI conductor, electric coral (#FF6B6B) for human-focused elements, sky blue (#4299E1) for data/monitoring, warm sunlight (#F6AD55) for services
- Front-facing view with slight depth perspective
- Simplified crowd silhouettes showing diversity (varied skin tones, body types)
- Subtle single-source shading for depth, no heavy 3D effects
- Clean white background
- Distinctive but not cartoonish - appropriate for business/academic audience
- Professional yet energetic mood

Festival-specific details:
- RFID wristbands visible on crowd silhouettes
- Mobile screens showing festival app interfaces
- Outdoor festival environment (sky, grass/ground visible)
- Stage lighting and sound equipment simplified but recognizable

Avoid: Generic business imagery (suits, offices), clichéd AI imagery (menacing robots, human-brain hybrids), overly realistic detail

Image specifications:
- Orientation: Square
- Focal point: Central AI conductor figure, with eye drawn outward to surrounding operations
- Size: High resolution, suitable for print (minimum 2400x1800px)
```

---

## Template 3: Icon Set Generation

### Use For
- Consistent icons for infographics
- Section markers
- Process step indicators
- Category symbols

### Template

```
Generate a set of {{NUMBER}} consistent icons for {{ICON_SET_PURPOSE}}.

Icons needed:
1. {{ICON_1_NAME}}: {{DESCRIPTION - e.g., "Stage with simple geometric structure"}}
2. {{ICON_2_NAME}}: {{DESCRIPTION}}
3. {{ICON_3_NAME}}: {{DESCRIPTION}}
{{ADD MORE AS NEEDED}}

Style: EventAI professional festival industry icons
- Outlined style (not filled), 2-3px stroke weight
- Rounded corners (2-4px radius)
- Modern, minimal, geometric approach
- Single color per icon: deep purple (#6B46C1) or midnight slate (#2D3748)
- Consistent size (each icon fits in 64x64px grid with padding)
- Similar level of detail across all icons
- Festival-relevant subjects (avoid generic business icons)
- Distinctive but professional

Layout: Display all icons in a grid on white background with labels below each icon

Image specifications:
- Orientation: Square or Landscape (depending on number of icons)
- Equal spacing between icons (minimum 32px)
- Labels: 12-14pt sans-serif, midnight slate, centered below icon
- Size: High resolution (each icon exportable at 512x512px minimum)
```

### Example: Festival Operations Icon Set

**Filled Template**:
```
Generate a set of 6 consistent icons for festival operations categories.

Icons needed:
1. Crowd Management: Simplified group of 3-5 people silhouettes arranged in formation
2. Ticketing: Simple ticket shape with perforated edge detail
3. Food Service: Minimalist food vendor tent or food/drink cup
4. Stage Operations: Geometric stage structure with simple truss outline
5. Security: Shield outline with small camera or eye symbol
6. Analytics: Simple bar chart or graph with 3-4 bars

Style: EventAI professional festival industry icons
- Outlined style (not filled), 2-3px stroke weight
- Rounded corners (2-4px radius)
- Modern, minimal, geometric approach
- Single color per icon: deep purple (#6B46C1)
- Consistent size (each icon fits in 64x64px grid with padding)
- Similar level of detail across all icons (not overly complex, essential forms only)
- Festival-relevant subjects (stages, crowds, tents - not briefcases or generic buildings)
- Distinctive but professional

Layout: Display all 6 icons in a 2x3 grid on white background with labels below each icon

Image specifications:
- Orientation: Landscape
- Equal spacing between icons (48px horizontal, 64px vertical)
- Labels: 14pt sans-serif, midnight slate (#2D3748), centered below icon
- Size: High resolution (minimum 2400x1600px total, each icon exportable at 512x512px)
```

---

## Template 4: Data Visualization Enhancement

### Use For
- Custom charts not easily made in NotebookLM
- Complex comparative visualizations
- Creative data representations

### Template

```
Generate a data visualization showing {{DATA_SUBJECT}}.

Data to visualize:
{{LIST_THE_DATA - e.g., "2025: 45%, 2028: 70%, 2032: 90%, 2035: 95%"}}

Visualization type: {{TYPE - e.g., "Line graph" or "Bar chart" or "Comparison bars" or "Creative metaphor"}}

Visual approach:
{{DESCRIBE_HOW_TO_SHOW_DATA - e.g., "Ascending line graph with data points marked, gradient fill below line showing growth"}}

Style: EventAI professional festival industry data visualization
- Color palette: deep purple (#6B46C1) for primary data, electric coral (#FF6B6B) for key points, sky blue (#4299E1) for comparisons
- Clean axes (1-2px, mid gray #A0AEC0)
- Subtle grid lines if needed (1px, light cloud #F7FAFC)
- Direct data labels on/near points (not separate legend)
- Modern sans-serif typography
- Large, bold numbers for key statistics (48-56pt in electric coral)
- Source citation at bottom (10-12pt, mid gray)
- Clean white background, generous margins
- High data-ink ratio (minimal decoration)

Festival context: {{HOW_TO_INTEGRATE_FESTIVAL_IMAGERY - e.g., "Use small wristband icons at each data point" or "Stage silhouette shapes for bars"}}

Image specifications:
- Orientation: {{LANDSCAPE|PORTRAIT|SQUARE}}
- Emphasis: {{MOST_IMPORTANT_DATA_POINT}}
- Size: High resolution, suitable for print (minimum 2400x1800px)
```

### Example: AI Adoption Growth (2025-2035)

**Filled Template**:
```
Generate a data visualization showing AI adoption growth at festivals from 2025 to 2035.

Data to visualize:
- 2025: 45% (current baseline)
- 2028: 70% (Phase 1 complete)
- 2032: 90% (Phase 2 complete)
- 2035: 95% (Phase 3 complete)

Visualization type: Ascending line graph with milestone markers

Visual approach:
Smooth ascending line from bottom-left (2025, 45%) to top-right (2035, 95%). Each data point marked with a circle. Phase labels positioned above the line at transition points (2028, 2032). Subtle gradient fill below the line from transparent to light purple (10% opacity). Y-axis shows percentages 0-100%, X-axis shows years. Large "95%" label at final point in electric coral to emphasize destination.

Style: EventAI professional festival industry data visualization
- Color palette: deep purple (#6B46C1) for line and data points, electric coral (#FF6B6B) for final 95% emphasis, light purple gradient fill below line
- Clean axes (2px, mid gray #A0AEC0)
- Subtle horizontal grid lines at 25%, 50%, 75%, 100% (1px, light cloud #F7FAFC)
- Direct data labels at each point: percentage in bold 24pt purple, year below in 14pt slate
- Phase labels: "Phase 1: Foundation", "Phase 2: Mainstream", "Phase 3: Adaptive" in 16pt semibold purple
- Modern sans-serif typography (Inter or similar)
- Final data point "95%" in extra-large 56pt bold electric coral
- Source citation at bottom right: "Source: Market projections & EventAI analysis" (12pt, mid gray)
- Clean white background, 64px margins all sides
- High data-ink ratio (no unnecessary decorative elements)

Festival context: Use small simplified stage icons at each data point (increasing in detail/complexity from 2025 to 2035 to suggest evolution)

Image specifications:
- Orientation: Landscape
- Emphasis: The 95% endpoint in electric coral with largest visual weight
- Size: High resolution, suitable for print (minimum 2400x1800px)
```

---

## Tips & Best Practices

### Text Rendering (Nano Banana Pro Strength)
✅ **Do**: Request specific text to appear in image
- "Include the text 'AI Adoption Timeline' at the top in bold purple"
- "Label each box with its name: Input, Processing, Output"
- "Show percentage '42%' in large electric coral text"

⚠️ **Caveat**: Always review generated text for spelling/accuracy

### Consistency Across Multiple Images
- Use the same base prompt structure
- Reference EventAI style explicitly each time
- Specify exact hex codes for colors
- Request same outline width, corner radius, etc.
- Generate related images in same session if possible

### Iteration Strategy
1. **First pass**: Generate with full detailed prompt
2. **Review**: Check style alignment, factual accuracy, text legibility
3. **Refine**: If needed, regenerate with more specific guidance about what to change
4. **Variations**: Generate 2-3 versions, select best

### Festival Context is Critical
Always include festival-specific elements:
- Stages, tents, outdoor venues
- Crowds (diverse representation)
- Wristbands, tickets, mobile devices
- Musical elements, lighting
- NOT: Generic office/business/tech imagery

### Accessibility Considerations
- Request high contrast (verify WCAG AA)
- Don't rely on color alone (icons + text + color)
- Ensure text is large enough to read
- Test generated image for color-blind viewing

---

## Integration with NotebookLM Infographics

**When to use Nano Banana vs. NotebookLM**:

**Nano Banana** (this template):
- Custom diagrams with specific structure
- Illustrations and conceptual imagery
- Icon sets
- Visual elements to combine with other content

**NotebookLM Infographics**:
- Data-heavy visualizations
- Multi-section comprehensive infographics
- Text-heavy content summaries
- When you have structured source documents

**Best Approach**: Use both together
1. Generate custom icons/diagrams with Nano Banana
2. Reference those visual elements in NotebookLM infographic prompts
3. Combine in final layout

---

## EventAI Quick Prompt (Copy This!)

For any EventAI image generation, start with:

```
EventAI festival industry style: Deep purple (#6B46C1), electric coral
(#FF6B6B), sky blue (#4299E1) on white. Modern sans-serif, rounded corners,
2-3px outlines. Semi-flat with subtle depth. Festival context (stages, crowds,
wristbands). Professional yet energetic. Minimal decoration, clean composition.
High resolution, print-ready.
```

Then add your specific requirements.

---

## Related Templates

- [NotebookLM Infographic](../notebooklm/infographic.prompt.md) - For data-heavy infographics
- [Diagrams](diagrams.prompt.md) - Specialized diagram prompts
- [Festival Context](festival-context.prompt.md) - Festival-specific imagery
- [Icon Sets](icons.prompt.md) - Detailed icon generation guidance

---

*Template Version: 1.0*
*Last Updated: December 28, 2025*
*Part of: Lemmy Prompt Library*
*Style Guide: [eventai-visual-identity.md](../../style-guide/eventai-visual-identity.md)*
