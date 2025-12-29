# Nano Banana (Gemini) Image Generation Workflows

**Platform**: Google AI Studio / Gemini API
**Model**: Imagen 3 / Nano Banana Pro
**Capabilities**: Custom images, diagrams, illustrations, icons
**EventAI Integration**: Fully integrated with prompt templates and style guide

---

## Overview

Nano Banana (Gemini's Imagen 3/Nano Banana Pro) uses **autoregressive image generation** (1,290 tokens per image) rather than traditional diffusion models. This gives it:

✅ **Excellent text rendering** - Can reliably generate text within images
✅ **Precise composition control** - Responds well to detailed structural prompts
✅ **High resolution output** - Print-ready images (2400x1800px minimum)
✅ **Festival context understanding** - Can create industry-specific imagery

---

## Workflow 1: Technical Diagram Generation

### Use Cases

- System architecture diagrams
- Process flowcharts
- Decision trees
- Data flow diagrams
- DICE recommendation flow, AI processing pipelines, etc.

### Step-by-Step Process

#### Step 1: Select Template (2 min)

1. Open `docs/lemmy/prompts/images/nano-banana.prompt.md`
2. Locate "Template 1: Technical Diagram"
3. Review example (DICE Recommendation Flow)

#### Step 2: Define Diagram Structure (5 min)

**Answer these questions**:
- What is the diagram showing? (subject)
- How should it flow? (left-to-right, circular, hierarchical)
- What are the main elements? (boxes, nodes, stages)
- How do they connect? (arrows, lines, relationships)
- What should stand out? (emphasis, focal point)

**Example notes**:
```
Subject: AI-powered crowd flow management system
Layout: Left-to-right flow with 4 stages
Elements:
  1. Sensors (cameras, RFID readers) - sky blue
  2. AI Processing (real-time analysis) - deep purple
  3. Alerts (staff notifications) - electric coral
  4. Actions (crowd redirection) - sky blue
Connections: Sequential arrows, feedback loop from Actions to Processing
Emphasis: Processing stage (largest box, bold purple)
```

#### Step 3: Fill Template (8 min)

**Replace all {{PLACEHOLDERS}}**:

```
Generate a clean technical diagram showing {{AI-powered crowd flow management at festivals}}.

Visual structure:
{{Left-to-right flow with 4 main stages: Input → Processing → Output → Action, with feedback loop}}

Elements to include:
1. {{Input stage: "Sensor Network" with camera and RFID reader icons}}
2. {{Processing stage: "AI Analysis Engine" with neural network visual}}
3. {{Output stage: "Real-time Alerts" with notification symbols}}
4. {{Action stage: "Staff Response" with people icons}}

Connections:
{{Sequential arrows flowing left to right, dashed feedback arrow from Action back to Processing}}

Style: EventAI professional festival industry diagram
- Deep purple (#6B46C1) for AI processing elements
- Electric coral (#FF6B6B) for alert/critical elements
- Sky blue (#4299E1) for data/sensor elements
- Simple geometric shapes with rounded corners (8-12px radius)
- 2-3px outline stroke, clean lines
- Arrows with triangular heads showing clear directional flow
- Modern sans-serif labels, left-aligned text
- Clean white background, generous spacing between elements
- Semi-flat style with subtle shadows for depth (not 3D)
- Minimal decoration, every element serves a purpose

Festival context: Include small illustrative elements like {{simplified stage in background, crowd silhouettes, RFID wristband symbols}}.

Image specifications:
- Orientation: {{Landscape}}
- Emphasis: {{AI Processing stage should be visual anchor}}
- Size: High resolution, suitable for print (minimum 2400x1800px)
```

#### Step 4: Generate via Gemini (5 min)

1. **Go to Google AI Studio**
   - Navigate to [https://aistudio.google.com/](https://aistudio.google.com/)
   - Sign in with Google account

2. **Select Model**
   - Choose "Imagen 3" or "Nano Banana Pro" from model dropdown
   - Nano Banana Pro recommended for text rendering

3. **Paste Prompt**
   - Copy your filled template
   - Paste into prompt field
   - Review for any remaining placeholders

4. **Generate**
   - Click "Generate" or "Run"
   - Wait 30-60 seconds
   - Image will appear in output area

5. **Review Initial Result**
   - Check structure, layout, elements present
   - Verify text rendering quality
   - Check EventAI style compliance

#### Step 5: Iterate if Needed (5-15 min)

**If unsatisfactory, refine prompt**:

Common adjustments:
- **Layout issues**: Be more specific about spacing, positioning
- **Missing elements**: List more explicitly, add size guidance
- **Wrong colors**: Specify exact hex codes, repeat color assignments
- **Text errors**: Regenerate, check spelling in prompt
- **Style mismatch**: Add more EventAI style details, reference example images

**Generate 2-3 variations**:
- Try slight prompt variations
- Adjust emphasis or focal points
- Compare and select best version

#### Step 6: Download & Save (2 min)

1. **Download**
   - Click download icon or right-click → Save image
   - File format: PNG (high resolution)

2. **Verify Quality**
   - Open in image viewer
   - Check resolution (should be 2400x1800px or higher)
   - Zoom in to verify text is crisp
   - Check colors match EventAI palette

3. **Save to Project**
   - Location: `docs/writing/[N]-[topic]/visuals/`
   - Name: `[topic]-diagram-[descriptor].png`
   - Example: `privacy-diagram-surveillance-flow.png`

**Total Time**: ~20-25 minutes per diagram (including iteration)

---

## Workflow 2: Festival Scene Illustration

### Use Cases

- Conceptual imagery for section headers
- Before/After AI comparisons
- Visual metaphors
- Festival context establishment
- Hero images for topics

### Step-by-Step Process

#### Step 1: Conceptualize Scene (5 min)

**Define the concept**:
- What's the central metaphor? (e.g., "AI as festival conductor")
- What's happening in the scene?
- What mood should it convey?
- What festival elements are present?

**Example concept**:
```
Metaphor: AI personalizing attendee experiences
Scene: Festival-goer looking at personalized schedule on phone,
       with subtle AR-like highlights showing recommended stages/acts
Mood: Helpful technology, organic integration, not intrusive
Elements: Diverse crowd, multiple stages in background, phones/wristbands,
         AR-style UI overlays, sunset festival lighting
```

#### Step 2: Fill Template (10 min)

**Use Template 2: Festival Scene Illustration**

Replace placeholders with scene details:

```
Create a semi-flat illustration of {{AI-powered personalized festival experience}} in a festival context.

Scene composition:
{{Outdoor festival at sunset, main stage in background with lights. Foreground: diverse attendee looking at phone showing personalized schedule with AR-style highlights. Mid-ground: other attendees wearing RFID wristbands, some at food vendors, some heading to stages.}}

Key elements:
- {{Main stage: simplified geometric structure with purple and coral lighting}}
- {{Central attendee: young person (non-specific ethnicity) holding phone with glowing screen}}
- {{Phone UI: translucent AR overlay showing 3 recommended acts with paths highlighted}}
- {{Crowd: diverse silhouettes (varied skin tones, body types, some wheelchairs)}}
- {{Environment: outdoor festival setting, food vendors, sunset sky}}
- {{Technology: RFID wristbands visible, subtle connection lines from wristbands to phone}}

Mood: {{Helpful and organic - technology feels integrated, not intrusive. Optimistic but grounded.}}

Style: EventAI professional festival industry illustration
- Modern, simplified semi-flat style with clean 2-3px outlines and rounded corners
- Color palette: deep purple (#6B46C1) for tech elements, electric coral (#FF6B6B) for highlights, sky blue (#4299E1) for UI, warm sunlight (#F6AD55) for sunset
- {{Front-facing view with slight depth perspective}}
- Simplified crowd silhouettes showing diversity (varied skin tones, body types)
- Subtle single-source shading for depth, no heavy 3D effects
- Clean white background
- Distinctive but not cartoonish - appropriate for business/academic audience
- Professional yet energetic mood

Festival-specific details:
- {{RFID wristbands visible and glowing softly}}
- {{Mobile phone showing festival app with AR overlay}}
- {{Multiple stages visible in background at different distances}}
- {{Food vendor tents, outdoor setting with sky/grass}}

Avoid: Generic business imagery (suits, offices), clichéd AI imagery (robots, menacing tech), overly realistic detail

Image specifications:
- Orientation: {{Landscape}}
- Focal point: {{Central attendee with phone - eye drawn to glowing screen}}
- Size: High resolution, suitable for print (minimum 2400x1800px)
```

#### Step 3-6: Same as Technical Diagram

- Generate via Gemini (5 min)
- Iterate if needed (5-15 min)
- Download & save (2 min)

**Total Time**: ~30-40 minutes per illustration

---

## Workflow 3: Icon Set Generation

### Use Cases

- Consistent icons for infographics
- Section markers in documents
- Process step indicators
- Category symbols

### Step-by-Step Process

#### Step 1: Define Icon Set (5 min)

**Determine**:
- How many icons needed? (typically 4-8)
- What does each represent?
- What's the purpose? (navigation, categories, process steps)
- Should they be outlined or filled?

**Example set**:
```
Purpose: Festival operations categories for infographic
Count: 6 icons
Icons:
1. Crowd Management - group of people
2. Ticketing - ticket shape
3. Food Service - food vendor tent
4. Stage Operations - stage structure
5. Security - shield with camera
6. Analytics - bar chart
Style: Outlined (not filled), consistent detail level
```

#### Step 2: Fill Template (10 min)

**Use Template 3: Icon Set Generation**

```
Generate a set of {{6}} consistent icons for {{festival operations categories}}.

Icons needed:
1. {{Crowd Management}}: {{Simplified group of 3-5 people silhouettes arranged in formation}}
2. {{Ticketing}}: {{Simple ticket shape with perforated edge detail}}
3. {{Food Service}}: {{Minimalist food vendor tent or food/drink cup}}
4. {{Stage Operations}}: {{Geometric stage structure with simple truss outline}}
5. {{Security}}: {{Shield outline with small camera or eye symbol}}
6. {{Analytics}}: {{Simple bar chart or graph with 3-4 bars}}

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
- Orientation: {{Landscape}}
- Equal spacing between icons (48px horizontal, 64px vertical)
- Labels: 14pt sans-serif, midnight slate (#2D3748), centered below icon
- Size: High resolution (minimum 2400x1600px total, each icon exportable at 512x512px)
```

#### Step 3: Generate & Extract Icons (10 min)

1. **Generate full icon set** via Gemini
2. **Download complete grid image**
3. **Extract individual icons** (if needed):
   - Use image editor (Photoshop, GIMP, Figma)
   - Crop each icon from grid
   - Export as individual PNG files (512x512px)
   - Name: `icon-[name].png` (e.g., `icon-crowd-management.png`)

**Alternative**: Use full grid image in infographics/documents

**Total Time**: ~25-35 minutes per icon set (including extraction)

---

## Workflow 4: Data Visualization Enhancement

### Use Cases

- Custom charts not easily made in NotebookLM
- Creative data representations
- Timeline visualizations
- Comparative visualizations

### Step-by-Step Process

#### Step 1: Gather Data (3 min)

**Collect specific data points**:
```
Example: AI Adoption Growth 2025-2035
- 2025: 45% (current baseline)
- 2028: 70% (Phase 1 complete)
- 2032: 90% (Phase 2 complete)
- 2035: 95% (Phase 3 complete)
```

#### Step 2: Choose Visualization Type (2 min)

**Options**:
- **Line graph**: Showing trends over time
- **Bar chart**: Comparing categories
- **Comparison bars**: Side-by-side comparisons
- **Timeline**: Events/milestones along axis
- **Creative metaphor**: Data embedded in visual metaphor

**For EventAI**: Often line graphs or timelines with festival context

#### Step 3: Fill Template (10 min)

**Use Template 4: Data Visualization Enhancement**

```
Generate a data visualization showing {{AI adoption growth at festivals from 2025 to 2035}}.

Data to visualize:
{{- 2025: 45% (current baseline)
- 2028: 70% (Phase 1 complete)
- 2032: 90% (Phase 2 complete)
- 2035: 95% (Phase 3 complete)}}

Visualization type: {{Ascending line graph with milestone markers}}

Visual approach:
{{Smooth ascending line from bottom-left (2025, 45%) to top-right (2035, 95%). Each data point marked with a circle. Phase labels positioned above the line at transition points (2028, 2032). Subtle gradient fill below the line from transparent to light purple (10% opacity). Y-axis shows percentages 0-100%, X-axis shows years. Large "95%" label at final point in electric coral to emphasize destination.}}

Style: EventAI professional festival industry data visualization
- Color palette: deep purple (#6B46C1) for line/data points, electric coral (#FF6B6B) for final 95% emphasis, light purple gradient fill
- Clean axes (2px, mid gray #A0AEC0)
- Subtle horizontal grid lines at 25%, 50%, 75%, 100% (1px, light cloud #F7FAFC)
- Direct data labels at each point: percentage in bold 24pt purple, year below in 14pt slate
- Phase labels: "Phase 1: Foundation", "Phase 2: Mainstream", "Phase 3: Adaptive" in 16pt semibold purple
- Modern sans-serif typography (Inter or similar)
- Final data point "95%" in extra-large 56pt bold electric coral
- Source citation at bottom right: "Source: Market projections & EventAI analysis" (12pt, mid gray)
- Clean white background, 64px margins all sides
- High data-ink ratio (no unnecessary decorative elements)

Festival context: {{Use small simplified stage icons at each data point (increasing in detail/complexity from 2025 to 2035 to suggest evolution)}}

Image specifications:
- Orientation: {{Landscape}}
- Emphasis: {{The 95% endpoint in electric coral with largest visual weight}}
- Size: High resolution, suitable for print (minimum 2400x1800px)
```

#### Step 4-6: Same as Technical Diagram

**Total Time**: ~25-35 minutes per data visualization

---

## Tips & Best Practices

### Text Rendering Excellence

✅ **Nano Banana Pro's Strength**:
- Can reliably generate text within images
- Spell correctly in prompts → Nano Banana renders correctly
- Request specific text to appear:
  - "Include the text 'AI Adoption Timeline' at the top in bold purple"
  - "Label each box: Input, Processing, Output"
  - "Show percentage '42%' in large electric coral text"

⚠️ **Always Review**:
- Check spelling in generated images
- Verify numbers/percentages are correct
- Ensure text is legible at intended display size

### Consistency Across Multiple Images

**Maintain consistent style**:
1. Use same base prompt structure for related images
2. Reference EventAI style explicitly each time
3. Specify exact hex codes for colors
4. Request same outline width (2-3px), corner radius (8-12px), etc.
5. Generate related images in same session if possible

**Example**: If creating 5 diagrams for privacy topic, generate all 5 in one session with nearly identical style sections

### Iteration Strategy

**Efficient workflow**:
1. **First pass**: Generate with full detailed prompt
2. **Review**: Check style alignment, factual accuracy, text legibility
3. **Refine**: If needed, adjust specific aspects:
   - "Make the purple elements darker"
   - "Increase spacing between elements"
   - "Add more festival context (wristbands, stages)"
4. **Variations**: Generate 2-3 versions with slight variations, select best

**Don't**: Start completely over - make targeted adjustments

### Festival Context is Critical

**Always include**:
- Stages, tents, outdoor venues
- Crowds (diverse representation: varied skin tones, body types, accessibility devices)
- Wristbands, tickets, mobile devices
- Musical elements, lighting
- Outdoor settings (sky, grass, festival environment)

**Avoid**:
- Generic office/business imagery (suits, desks, briefcases)
- Clichéd AI imagery (menacing robots, circuit brains, blue glowy tech)
- Corporate tech visuals (server rooms, data centers)

### Accessibility Considerations

✅ **Build in from start**:
- Request high contrast (WCAG AA minimum)
- Don't rely on color alone - use icons + text + color
- Ensure text is large enough (14pt+ for body, 24pt+ for emphasis)
- Test for color-blind viewing (use tools like Color Oracle)

**In prompts**:
- "Ensure text labels are readable at 14pt minimum"
- "Use both color and icons to distinguish elements"
- "Maintain WCAG AA contrast ratios"

---

## Common Use Cases & Examples

### Use Case 1: System Architecture Diagram

**Scenario**: Showing how AI recommendation engine works

**Template**: Technical Diagram
**Orientation**: Landscape
**Time**: ~25 minutes

**Key elements**:
- Input sources (listening history, past attendance, social connections)
- AI processing box (central, deep purple)
- Output recommendations
- Success metric (40-41% of sales in coral)

### Use Case 2: Before/After AI Comparison

**Scenario**: Traditional festival planning vs AI-optimized

**Template**: Festival Scene Illustration (generate 2: before and after)
**Orientation**: Square (for side-by-side layout)
**Time**: ~60-80 minutes (both images)

**Key elements**:
- Before: Manual processes, paper, stressed staff, inefficiencies
- After: Digital interfaces, AI assistance, smooth operations, happy staff

### Use Case 3: Process Steps Icons

**Scenario**: 5-step AI implementation roadmap icons

**Template**: Icon Set Generation
**Orientation**: Landscape grid
**Time**: ~30 minutes

**Key elements**:
- Assessment, Planning, Implementation, Testing, Optimization icons
- Consistent outlined style, purple color
- Numbered or labeled below

### Use Case 4: Trend Visualization

**Scenario**: Growth of AI investment in festivals 2020-2025

**Template**: Data Visualization
**Orientation**: Landscape
**Time**: ~30 minutes

**Key elements**:
- Line graph showing exponential growth
- Key inflection points (COVID impact, recovery, acceleration)
- Festival context (stage icons at data points)

---

## Integration with NotebookLM Infographics

**When to use Nano Banana vs NotebookLM**:

### Nano Banana (this workflow)
- ✅ Custom diagrams with specific structure
- ✅ Illustrations and conceptual imagery
- ✅ Icon sets for reuse
- ✅ Visual elements to combine with other content
- ✅ When you need precise control over composition

### NotebookLM Infographics
- ✅ Data-heavy visualizations
- ✅ Multi-section comprehensive infographics
- ✅ Text-heavy content summaries
- ✅ When you have structured source documents
- ✅ Automated layout from source content

### Best Approach: Use Both Together

**Workflow**:
1. Generate custom icons/diagrams with Nano Banana
2. Reference those visual elements in NotebookLM infographic prompts:
   ```
   Use icon style similar to: [describe Nano Banana icons]
   Include diagram showing: [reference Nano Banana diagram concept]
   ```
3. Combine in final layout (e.g., NotebookLM infographic + Nano Banana hero illustration)

---

## EventAI Quick Prompt

**For any EventAI image generation, start with:**

```
EventAI festival industry style: Deep purple (#6B46C1), electric coral
(#FF6B6B), sky blue (#4299E1) on white. Modern sans-serif, rounded corners,
2-3px outlines. Semi-flat with subtle depth. Festival context (stages, crowds,
wristbands). Professional yet energetic. Minimal decoration, clean composition.
High resolution, print-ready.
```

**Then add your specific requirements** (diagram elements, scene composition, data visualization structure, etc.)

---

## Troubleshooting

### Problem: Generated image has spelling errors

**Solution**: Double-check spelling in prompt, regenerate. Nano Banana Pro is excellent but review carefully.

### Problem: Image doesn't match festival context

**Solution**: Be more specific about festival elements (stages, crowds, wristbands), add examples in prompt.

### Problem: Colors don't match EventAI palette

**Solution**: Include exact hex codes in prompt, reference EventAI style guide explicitly.

### Problem: Style inconsistent across multiple images

**Solution**: Use exact same EventAI style snippet, generate in same session, copy-paste color/typography specifications.

### Problem: Layout is cluttered

**Solution**: Request more white space, generous spacing between elements, minimal decoration. Emphasize "clean composition" and "high data-ink ratio".

### Problem: Text is illegible

**Solution**: Request larger font sizes, specify minimum sizes (14pt, 24pt), ensure high resolution output.

---

## Related Documentation

- **Nano Banana Prompt Template**: [../prompts/images/nano-banana.prompt.md](../prompts/images/nano-banana.prompt.md)
- **EventAI Style Guide**: [../style-guide/eventai-visual-identity.md](../style-guide/eventai-visual-identity.md)
- **Nano Banana Capabilities**: [../research/nano-banana/capabilities.md](../research/nano-banana/capabilities.md)
- **Visual Content Plan**: [../../writing/VISUAL-CONTENT-PLAN.md](../../writing/VISUAL-CONTENT-PLAN.md)
- **NotebookLM Workflows**: [notebooklm-workflows.md](notebooklm-workflows.md) (for comparison/integration)

---

*Workflow Version: 1.0*
*Last Updated: December 28, 2025*
*Platform: Google AI Studio / Gemini (Imagen 3 / Nano Banana Pro)*
