# NotebookLM Audio Overview Prompt Template

**Platform**: NotebookLM
**Output**: Audio podcast-style conversation (MP3/audio file)
**Customization**: High
**Generation Time**: 3-10 minutes

## Purpose
Generate an AI podcast featuring two hosts discussing your source materials in a conversational, engaging format. Perfect for creating learning content that can be consumed while commuting, exercising, or multitasking.

## Usage Instructions

### Step 1: Upload Sources
1. Go to your NotebookLM notebook
2. Add relevant sources (PDFs, Google Docs, URLs, etc.)
3. Ensure sources contain the content you want covered

### Step 2: Configure Audio Overview
1. Click "Generate" in the Studio panel
2. Select "Audio Overview"
3. Click the pencil icon (Customize) before generating

### Step 3: Apply This Template
Copy the customization prompt below and paste into the customization panel.

### Step 4: Set Options
- **Format**: Choose Deep Dive, Brief, Critique, Debate, or Lecture
- **Length**: Shorter (~5min), Default (~10min), Longer (~20min)
- **Language**: Select from 80+ languages

### Step 5: Generate and Download
1. Click "Generate"
2. Wait for completion (runs in background)
3. Download audio file when ready

---

## Customization Template

### Template: General Overview

```
Create an engaging audio overview that covers {{MAIN_TOPIC}}.

Focus areas:
- {{FOCUS_AREA_1}}
- {{FOCUS_AREA_2}}
- {{FOCUS_AREA_3}}

Target audience: {{AUDIENCE_LEVEL}}
Expertise level: {{BEGINNER|INTERMEDIATE|ADVANCED}}

Special emphasis on:
{{SPECIAL_INSTRUCTIONS}}

Tone: {{CONVERSATIONAL|ANALYTICAL|CRITICAL|EDUCATIONAL}}
```

### Template: Educational Content (EventAI Style)

```
Create an educational audio overview explaining {{CURRICULUM_TOPIC}} for festival professionals.

This is part of the EventAI education curriculum on "AI in Festivals: A Critical Guide."

Focus on:
1. {{KEY_CONCEPT_1}} - Why this matters for festival organizers
2. {{KEY_CONCEPT_2}} - Practical implications
3. {{KEY_CONCEPT_3}} - Critical considerations

Balance professional credibility with approachable explanation.
Avoid jargon when possible, but explain technical terms when necessary.

Target audience: Festival organizers, event professionals (varying technical backgrounds)
Tone: Professional yet whimsical - serious about the topic but engaging in delivery
```

### Template: Research Synthesis

```
Synthesize the research on {{RESEARCH_TOPIC}} from the provided sources.

Research questions to address:
1. {{RESEARCH_QUESTION_1}}
2. {{RESEARCH_QUESTION_2}}
3. {{RESEARCH_QUESTION_3}}

Highlight:
- Key findings and consensus
- Areas of disagreement or debate
- Gaps in current research
- Practical implications

Target audience: {{RESEARCHERS|PRACTITIONERS|GENERAL_PUBLIC}}
Cite sources explicitly when discussing specific findings.
```

### Template: Critical Analysis

```
Provide a critical analysis of {{TOPIC}}, examining both benefits and concerns.

Debate points:
- Pro: {{POSITIVE_ANGLE}}
- Con: {{CONCERN_ANGLE}}

Specific focus:
{{DETAILED_INSTRUCTIONS}}

Ensure balanced coverage of multiple perspectives.
Address {{STAKEHOLDER_GROUP_1}} concerns and {{STAKEHOLDER_GROUP_2}} interests.

Format: Use Debate format for contrasting viewpoints
```

---

## Examples

### Example 1: EventAI Privacy Topic

**Filled Template**:
```
Create an educational audio overview explaining surveillance and privacy ethics in AI-powered festivals for festival professionals.

This is part of the EventAI education curriculum on "AI in Festivals: A Critical Guide."

Focus on:
1. Facial recognition and attendee tracking - Why this matters for festival organizers
2. Data collection and privacy implications - Practical legal and ethical considerations
3. Balancing security with attendee rights - Critical decision-making framework

Balance professional credibility with approachable explanation.
Avoid jargon when possible, but explain technical terms when necessary.

Target audience: Festival organizers, event professionals (varying technical backgrounds)
Tone: Professional yet whimsical - serious about the topic but engaging in delivery
```

**Settings**:
- Format: Deep Dive
- Length: Longer (~20 min)
- Language: English

### Example 2: Quick Research Summary

**Filled Template**:
```
Create an engaging audio overview that covers NotebookLM's new 2025 features.

Focus areas:
- Video Overviews with Nano Banana
- Infographic generation capabilities
- Deep Research integration

Target audience: Content creators and educators
Expertise level: Intermediate

Special emphasis on:
How these features compare to traditional content creation workflows and what time savings they offer.

Tone: Conversational
```

**Settings**:
- Format: Brief
- Length: Shorter (~5 min)
- Language: English

---

## Tips & Best Practices

### Source Preparation
✅ **Do**: Include diverse source types (research papers, articles, documentation)
✅ **Do**: Ensure sources are comprehensive on the topic
✅ **Do**: Include 5-15 sources for best results
❌ **Don't**: Upload 100+ sources (overwhelming, unfocused)
❌ **Don't**: Use sources that contradict your desired focus

### Customization Prompts
✅ **Do**: Be specific about focus areas
✅ **Do**: Specify target audience expertise level
✅ **Do**: Mention desired tone and style
❌ **Don't**: Write overly long customization prompts (keep under 200 words)
❌ **Don't**: Contradict the chosen format (e.g., asking for debate in Deep Dive)

### Format Selection Guide
- **Deep Dive**: Comprehensive exploration, multiple angles, 10-20min
- **Brief**: Quick summary, core concepts only, 5min
- **Critique**: Critical analysis, evaluate claims, 10-20min
- **Debate**: Contrasting viewpoints, pros/cons, 10-20min
- **Lecture**: Structured teaching, linear explanation, 10-30min

### Quality Optimization
1. **Focused Sources**: More targeted sources = better audio
2. **Clear Customization**: Specific prompts = more relevant content
3. **Appropriate Length**: Match length to content depth
4. **Audience Awareness**: Specify expertise level for better explanations

### Common Issues
- **Too Generic**: Add more specific customization instructions
- **Wrong Focus**: Review sources, ensure they cover desired topics
- **Too Technical**: Specify beginner audience, request simplified explanations
- **Too Shallow**: Choose longer length, add more detailed sources

### EventAI-Specific Considerations
- Always mention "EventAI education curriculum" context
- Specify "festival professional" as target audience
- Request balance of "professional + whimsy"
- Emphasize practical implications for festival organizers

---

## Integration with Lemmy Workflow

### Claude Code Preparation
1. Claude Code synthesizes research into source documents
2. Claude Code identifies key topics for audio focus
3. Claude Code generates customization prompt using this template

### Manual NotebookLM Step
4. User uploads sources to NotebookLM
5. User pastes customization prompt
6. User selects format, length, language
7. User generates and downloads audio

### Claude Code Integration
8. Claude Code documents audio file in content package
9. Audio file linked in curriculum documentation
10. Transcript generated if needed for accessibility

---

## Related Prompts
- [Video Overview](video-overview.prompt.md) - Visual version with illustrations
- [Slide Deck](slide-deck.prompt.md) - Presentation format
- [Deep Research](../research/deep-research.prompt.md) - Research question formulation

---

*Template Version: 1.0*
*Last Updated: December 28, 2025*
*Part of: Lemmy Prompt Library*
