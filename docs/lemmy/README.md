# Lemmy, Taley, Tooly: Knowledge-to-Output Creation System

A three-phase system for transforming ideas and questions into high-quality outputs through systematic knowledge corpus building, narrative extraction, and format-specific creation.

## The Three Phases

### 🔍 Lemmy: Knowledge Corpus Building

**Purpose**: Build a well-sourced, reliable corpus of knowledge about any topic through collaborative research.

**The Distinguishing Characteristic**: Agent and user work together to assemble a wide body of reliable, well-sourced knowledge that becomes the foundation for everything else. This collaborative corpus building sets Lemmy apart - it's not just research, it's systematic knowledge assembly.

**Process**:
- Start with an idea, question, or topic to explore
- Use prompt chains including Deep Research, Analysis, and Verification
- Users can provide knowledge (links, uploads), discover it, or synthesize it
- Guide research with questions and observations
- Build a corpus that's comprehensive, verified, and ready to work with

**Knowledge Type**: **Topic Knowledge** - Deep understanding of the subject being researched

---

### 📖 Taley: Narrative Extraction

**Purpose**: Extract and craft narratives from your knowledge corpus.

**Process**:
- Whether your information is fact or fiction, this phase helps you find the stories
- Extract any number of narratives that can be told with your topic knowledge
- Shape information into compelling storylines
- Multiple narratives can emerge from the same corpus

**Knowledge Type**: **Voice Knowledge** - Tone, phrasing, and narrative style for telling your stories

---

### 🎨 Tooly: Output Creation

**Purpose**: Create outputs beyond the narrative using format-specific best practices.

**Process**:
- Build or leverage a corpus of knowledge about the output format you want
- Apply best practices for specific content types
- Create diverse outputs from your narratives

**Possible Outputs**:
- Research papers and academic articles
- Summaries and executive briefs
- Social media content (posts, threads, stories)
- Cover art and visual branding
- Infographics and data visualizations
- Detailed analyses and reports
- Video overviews and presentations
- Slide decks and keynotes
- Interactive applications
- ...and more

**Knowledge Type**: **Content Knowledge** - Best practices, conventions, and standards for specific output formats (infographics, debates, social posts, etc.)

---

## The Three Knowledge Types

The system works with three distinct types of knowledge:

1. **Topic Knowledge**: Understanding of the subject being researched
   - Built in Lemmy phase
   - Forms the foundation for all outputs
   - Verified, sourced, comprehensive

2. **Voice Knowledge**: Tone, style, and phrasing for communication
   - Applied in Taley phase
   - Defines how stories are told
   - Can be formal, casual, academic, conversational, etc.

3. **Content Knowledge**: Best practices for specific output formats
   - Applied in Tooly phase
   - Format-specific conventions and standards
   - Ensures quality matches professional expectations

---

## The Vision

By separating **knowledge building** (Lemmy), **narrative extraction** (Taley), and **output creation** (Tooly), the system enables:

- **Reusability**: One corpus → many narratives → many outputs
- **Quality**: Each phase has focused expertise and standards
- **Collaboration**: User and agent build knowledge together
- **Flexibility**: Adapt narratives and outputs without rebuilding research
- **Reliability**: Well-sourced foundation prevents hallucination and drift

The key insight: **Start with great knowledge, and everything else follows.**

---

## Current Implementation

The current prototype focuses on academic textbook content creation for EventAI, demonstrating all three phases:

- **Lemmy**: Deep research with tier-classified sources and claim verification
- **Taley**: Casual-academic narrative style with conciseness standards
- **Tooly**: DOCX documents, tier-aware infographics, and visual content

For implementation details, see [PROTOTYPE-DESIGN.md](PROTOTYPE-DESIGN.md).

---

**Created**: January 6, 2026
**Purpose**: Vision document for knowledge-to-output creation system
**Status**: Active development - prototype demonstrates academic content pipeline
