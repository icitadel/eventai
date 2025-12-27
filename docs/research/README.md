# AI in Festivals & Events Research Repository

**Purpose:** Research materials for authoring a chapter on "AI's Impact on Festivals and Events" for an accessible academic textbook on The Future of Festivals & Events.

---

## 🎯 Quick Start

**New to this project?** Read in this order:
1. [Research Operating Instructions](#research-operating-instructions) - How we work
2. [Best Practices Guidance](#best-practices-guidance) - Quality standards
3. [Initial Research](#initial-research) - Topic foundations

---

## 📋 Research Operating Instructions

**Primary document:** [researchai.instructions.md](researchai.instructions.md)

Defines the operating model for Claude Code as Research Lead working under human governance. Key principles:

- **Human = Final Authority:** AI executes, human approves
- **Gate-Based Workflow:** Review gates block progression until human approval
- **Work Breakdown Structure:** Tasks sized 4-8h with explicit acceptance criteria
- **Review Packet Format:** Standardized deliverables for human decision-making
- **Uncertainty Protocol:** Confidence levels, escalation triggers, verification requirements

**When to use:** Before starting any research task, at every review gate, when uncertain about scope or quality.

---

## 📚 Best Practices Guidance

Located in [guidance/](guidance/)

### Governing AI Research Teams
**File:** [researchai-bp.research.md](guidance/researchai-bp.research.md)
**Summary:** Evidence-based framework for human governance of AI research teams. Covers role definitions, decision authority matrices, review gate design, and multi-task coordination. Key finding: "Process quality matters more than individual capability."

**Key topics:**
- Role architecture (Human stakeholder, AI lead, specialist agents)
- Work breakdown structure methodology (100% rule, mutual exclusivity, task sizing)
- Review gate design (decision packets, uncertainty communication)
- Quality assurance (verification, hallucination prevention, cascading error prevention)

### Writing Accessible Academic Textbooks
**File:** [textboox-bp.research.md](guidance/textboox-bp.research.md)
**Summary:** Research synthesis on creating accessible academic content. Applies cognitive science, universal design principles, and pedagogical research to textbook writing.

**Key topics:**
- Cognitive load management (worked examples, faded scaffolding, signaling)
- Linguistic clarity (plain language, active voice, 15-20 word sentences)
- Disability/neurodiversity considerations (dyslexia, ADHD, autism spectrum)
- Text-image integration (dual coding theory, spatial contiguity)

### Technical Implementation Plans
**Files:**
- [researchai-techplan.research.md](guidance/researchai-techplan.research.md) - Original technical plan
- [researchai-techplan-bp.research.md](guidance/researchai-techplan-bp.research.md) - Best practices implementation

**Summary:** Detailed technical approaches for implementing the research workflow, including tool selection, automation strategies, and quality control mechanisms.

### Source Documents
- [researchai-bp.sources.md](guidance/researchai-bp.sources.md) - Citations for AI research governance
- [textboox-bp.sources.md](guidance/textboox-bp.sources.md) - Citations for textbook best practices
- [researchai-bp.prompt.md](guidance/researchai-bp.prompt.md) - Prompts that generated guidance documents
- [textbook-bp.prompt.md](guidance/textbook-bp.prompt.md)

---

## 🔬 Initial Research

Located in [initial/](initial/)

Early AI-generated explorations addressing the 5 core interview questions for the chapter. These materials provide foundation knowledge for content development.

### Interview Questions Framework
**File:** [eventai-questions.md](initial/eventai-questions.md)
Defines 5 core questions the chapter addresses:

1. **Long-term AI Future Vision** - Transformative changes in festivals over next decade
2. **Critical AI Literacy in Education** - Beyond functional skills to ethical/philosophical understanding
3. **Innovative On-Site Personalization** - AI enhancing individual fan experiences organically
4. **Surveillance Ethics & Privacy Risks** - Responsible use of crowd analysis, facial recognition, sentiment tracking
5. **Real-Time Predictive Analytics** - AI for forecasting demand, pricing, resource allocation

### Topic Research Files

Each topic has 2-3 associated files:

#### 1. Transformation (Q1: Long-term AI Vision)
- [eventai-transformation.md](initial/eventai-transformation.md) - Research synthesis
- [eventai-transformation.prompt.md](initial/eventai-transformation.prompt.md) - Generation prompt

#### 2. Education (Q2: Critical AI Literacy)
- [eventai-education.md](initial/eventai-education.md) - Research synthesis
- [eventai-education.prompt.md](initial/eventai-education.prompt.md) - Generation prompt

#### 3. Personalization (Q3: On-Site Experience)
- [eventai-personalization.md](initial/eventai-personalization.md) - Research synthesis
- [eventai-personalization.prompt.md](initial/eventai-personalization.prompt.md) - Generation prompt

#### 4. Privacy & Ethics (Q4: Surveillance)
- [eventai-privacy.md](initial/eventai-privacy.md) - Privacy research synthesis
- [eventai-privacy-misuse.md](initial/eventai-privacy-misuse.md) - Misuse/risk analysis
- [eventai-privacy.prompt.md](initial/eventai-privacy.prompt.md) - Generation prompts
- [eventai-privacy-misuse.prompt.md](initial/eventai-privacy-misuse.prompt.md)

#### 5. Analytics (Q5: Predictive Operations)
- [eventai-analytics.md](initial/eventai-analytics.md) - Research synthesis
- [eventai-analytics.notes.md](initial/eventai-analytics.notes.md) - Working notes
- [eventai-analytics.prompt.md](initial/eventai-analytics.prompt.md) - Generation prompt

**Status:** Initial research only. These materials require verification, gap analysis, and synthesis before use in final chapter content.

---

## 🌍 External Research

Located in [external/](external/)

Third-party sources acquired from authoritative organizations (NOT AI-generated).

### Current Sources
- **[unesco-ai-competency-fx.pdf](external/unesco-ai-competency-fx.pdf)** - UNESCO AI Competency Framework for educators and students. Provides authoritative foundation for educational literacy discussions (Q2).

**Citation guidelines:**
- External sources have higher verification confidence than AI-generated research
- Cite with full bibliographic information
- Cross-reference with AI research to identify gaps or contradictions

---

## 📁 Folder Organization

```
docs/research/
├── README.md                       # This file - navigation and guidance
├── researchai.instructions.md      # Operating guide for AI Research Lead
├── guidance/                       # Best practices and methodology
│   ├── researchai-bp.*            # AI research team governance
│   ├── textboox-bp.*              # Accessible textbook writing
│   └── researchai-techplan.*      # Technical implementation
├── initial/                        # Early topic explorations (AI-generated)
│   ├── eventai-questions.md       # 5 core interview questions
│   ├── eventai-transformation.*   # Q1: Long-term vision
│   ├── eventai-education.*        # Q2: Critical literacy
│   ├── eventai-personalization.*  # Q3: On-site personalization
│   ├── eventai-privacy.*          # Q4: Ethics & privacy
│   └── eventai-analytics.*        # Q5: Predictive operations
└── external/                       # Third-party authoritative sources
    └── unesco-ai-competency-fx.pdf
```

---

## 🎯 Content Development Workflow

Per [researchai.instructions.md](researchai.instructions.md), content development follows this pattern:

1. **Source Analysis** → Extract themes, assess quality, identify gaps
2. **Research Synthesis** → Integrate findings, assign confidence levels, flag uncertainties
3. **Draft Content** → Write to acceptance criteria, maintain source attribution
4. **Quality Self-Check** → Verify completeness, evidence, uncertainty communication
5. **Review Gate** → Human approval required to proceed

**Output standards:**
- Consumer-oriented textbook tone (accessible, engaging)
- Evidence-based claims with confidence levels
- Cognitive load management (chunking, scaffolding, signaling)
- Plain language (15-20 word sentences, active voice, defined jargon)
- Neurodiversity-inclusive (avoid unexplained idioms, maintain consistency)

---

## 🔍 Using This Repository

### For Research Tasks
1. Review [researchai.instructions.md](researchai.instructions.md) for operating procedures
2. Check [initial/](initial/) for existing topic research
3. Cross-reference [external/](external/) sources for authoritative grounding
4. Apply standards from [guidance/](guidance/) for quality

### For Content Writing
1. Follow accessibility principles in [textboox-bp.research.md](guidance/textboox-bp.research.md)
2. Use [eventai-questions.md](initial/eventai-questions.md) to ensure complete coverage
3. Reference initial research but verify claims independently
4. Maintain uncertainty protocol (confidence levels, verification status)

### For Quality Review
1. Check against acceptance criteria in task definitions
2. Verify source attribution and confidence levels
3. Assess cognitive load (chunking, scaffolding, clarity)
4. Confirm accessibility standards met (plain language, structure, contrast)

---

## ⚠️ Important Notes

**AI-Generated Content Status:**
- Files in [initial/](initial/) are early AI explorations
- Treat as research leads, NOT verified facts
- All claims require independent verification
- Cross-reference multiple sources before citing

**Version Control:**
- `.prompt.md` files preserve generation context for reproducibility
- `.notes.md` files contain working annotations
- `.sources.md` files list citations and references

**Human Approval Required:**
- Review gates block progression (see [researchai.instructions.md](researchai.instructions.md))
- No content advances to next phase without explicit human sign-off
- Escalate when confidence < 60% or conflicts detected

---

**Last Updated:** 2025-12-27
**Primary Author:** Joe Allan Muharsky
**Research Lead:** Claude Code (AI agent operating under human governance)