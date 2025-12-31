# Narrative Commit Message Guide

**Purpose:** Best practices and examples for writing narrative-style commit messages that tell the story of code changes.

**Created:** December 30, 2025
**Project:** EventAI
**Context:** Developed while crafting commit for VIS-5.4 Use Cases Matrix generation and evaluation

---

## Research Foundation

### Key Principles from Industry Best Practices

**Storytelling Approach:**
- View code like a story - one you're telling to your future self or another developer
- Every commit is a chapter, every branch is a plot thread, every merge is where storylines converge
- Good commit messages tell a complete story: what was broken/needed, how it was fixed, why it matters, what the impact is

**Structure Elements:**
- **Problem/Need:** What requirement, bug, or improvement prompted this change?
- **Solution:** How was it addressed?
- **Context:** Why this approach? What alternatives were considered?
- **Impact:** What does this enable? Who benefits?

**Best Practices:**
- Imperative mood for subject line ("Add feature" not "Added feature")
- Subject under 50 characters (72 max for complex summaries)
- Body wrapped at 72 characters
- Blank line between subject and body
- Explain "why" not just "what"
- Use conventional commits format (`feat:`, `fix:`, `chore:`, etc.)

### Sources
- [Telling stories through your commits](https://blog.mocoso.co.uk/posts/talks/telling-stories-through-your-commits/)
- [The Beauty of Git: Writing Code Stories](https://dev.to/rafaeljohn9/the-beauty-of-git-writing-code-stories-3i99)
- [Git commit message best practices](https://graphite.com/guides/git-commit-message-best-practices)
- [How to Write a Good Git Commit Message](https://cbea.ms/git-commit/)
- [The Storyteller's Code: Crafting Compelling Narratives](https://algocademy.com/blog/the-storytellers-code-crafting-compelling-narratives-in-your-github-commits/)

---

## Example: VIS-5.4 Use Cases Matrix

### Context
Generated 3 infographic variants, evaluated them comprehensively, selected winner (Variant #3, 91%). Needed to communicate this journey in a narrative commit message rather than bullet points.

### Draft 1: Story Arc Approach

**Grade:** 85/100

```
feat(visuals): Add VIS-5.4 Use Cases Matrix - Variant #3 approved (91%)

The Predictive Analytics Use Cases Matrix went from concept to publication-ready design in under 90 seconds. Using gemini-generate browser automation, three variants were generated simultaneously, then evaluated comprehensively against EventAI visual identity standards and Tufte's information design principles.

Variant #3 emerged as the clear winner with a 91% score, outperforming its competitors through exceptional execution across five critical dimensions: EventAI style compliance (92/100), Tufte's data-ink ratio adherence (95/100), white space optimization (35-40% composition), perfect data accuracy (100/100 verified), and accessibility (90/100). Variant #1 scored 78% with its professional grid but suffered from asymmetric side panels and generic iconography, while Variant #2 achieved only 72% despite stronger festival personality due to dark backgrounds and compromised readability.

The matrix presents a comprehensive decision framework for festival professionals: 15 AI applications organized across four functional areas (Demand Forecasting, Resource Allocation, Risk Management, Revenue Optimization), with each cell revealing vendor examples, ROI metrics, implementation timelines, and complexity indicators. What separates the winning variant is its clean minimal aesthetic—generous spacing and pure white background create superior scanability, enabling both quick overview scanning and detailed investigation.

The evaluation revealed textbook adherence to both EventAI brand standards and Tufte's visualization principles. The result: a publication-ready visual with zero critical issues, ready to guide decision-makers through the landscape of predictive analytics applications in event management.

🤖 Generated with Claude Code (https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

**Strengths:**
- ✅ Strong narrative arc (concept → execution → evaluation → result)
- ✅ Explains why #3 won with specific comparisons
- ✅ Preserves all key facts and metrics
- ✅ Good flow and readability
- ✅ Professional tone

**Weaknesses:**
- ⚠️ Slightly long (could be more concise in places)
- ⚠️ Third paragraph could be tighter

---

### Draft 2: Problem-Solution Narrative

**Grade:** 88/100

```
feat(visuals): Add VIS-5.4 Use Cases Matrix - Variant #3 approved (91%)

Festival professionals need a comprehensive decision framework for evaluating predictive analytics applications across their operations. This commit delivers that framework through VIS-5.4, a matrix visualization displaying 15 AI applications organized by functional area (Demand, Resource, Risk, Revenue), complete with vendor examples, ROI metrics, implementation timelines, and complexity indicators.

Three design variants were generated via gemini-generate in 86.7 seconds. Comprehensive evaluation against EventAI visual identity guidelines and Tufte's data-ink ratio principles identified Variant #3 as the superior solution, scoring 91% versus alternatives at 78% and 72%. The winning design achieves excellence across all critical dimensions: EventAI style compliance (92/100), Tufte principles adherence (95/100), white space optimization (35-40%), perfect data accuracy (100/100 verified against source material), and accessibility (90/100).

What makes Variant #3 exceptional is its balance of information density and clarity. The clean minimal aesthetic with generous spacing enables both quick scanning for category overview and detailed investigation of specific applications. Variant #1's professional grid suffered from asymmetric side panels that reduced main content white space, while Variant #2's playful illustrated approach compromised readability through dark backgrounds and higher visual density despite stronger festival personality.

Publication-ready with zero critical issues. Optional enhancements: festival-specific iconography could strengthen brand personality; verify 300+ DPI for professional print applications.

🤖 Generated with Claude Code (https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

**Strengths:**
- ✅✅ Strong problem-solution structure (leads with user need)
- ✅ Comprehensive yet readable
- ✅ Good paragraph flow with clear transitions
- ✅ Balances technical detail with narrative accessibility
- ✅ Concise final paragraph with actionable items

**Weaknesses:**
- ⚠️ Could tighten first paragraph slightly (currently two sentences, could be one)

---

### Draft 3: Journey Narrative (RECOMMENDED)

**Grade:** 92/100 ⭐

```
feat(visuals): Add VIS-5.4 Use Cases Matrix - Variant #3 approved (91%)

This commit completes VIS-5.4, transforming a complex decision framework into a scannable matrix that festival professionals can use to evaluate 15 predictive analytics applications across their operations. The journey from concept to publication-ready design took 86.7 seconds through gemini-generate browser automation, producing three variants evaluated against EventAI visual identity standards and Tufte's information visualization principles.

Variant #3 achieved 91% overall, establishing itself as the clear winner through exceptional performance across five dimensions: EventAI style compliance (92/100), Tufte's data-ink ratio principles (95/100), white space optimization reaching 35-40% of composition, perfect data accuracy with all statistics verified (100/100), and strong accessibility (90/100). The matrix organizes applications by functional area—Demand Forecasting, Resource Allocation, Risk Management, Revenue Optimization—with each cell containing vendor examples, ROI metrics, timelines, and complexity indicators color-coded for quick assessment.

The evaluation revealed why Variant #3 outperformed alternatives scoring 78% and 72%. Its clean minimal aesthetic with generous spacing creates superior scanability, enabling viewers to extract value at multiple levels: quick category scan, overview of all applications, or detailed investigation of specific use cases. Variant #1's asymmetric side panels compromised main content white space despite professional grid structure, while Variant #2's darker, denser approach sacrificed readability for festival personality through illustrated icons and playful styling.

The result: textbook adherence to both EventAI brand guidelines and Tufte's multi-level revelation principle. Publication-ready with zero critical issues, though future iterations could enhance festival-specific iconography to strengthen brand personality while maintaining the current balance of information density and clarity.

🤖 Generated with Claude Code (https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

**Strengths:**
- ✅✅ Excellent narrative flow (transformation → execution → evaluation → insight)
- ✅✅ Leads with value ("transforming a complex decision framework"), maintains technical accuracy
- ✅ Comprehensive without being dense
- ✅✅ Strong transitions between paragraphs (each builds on previous)
- ✅ Explains not just what but why (design rationale, comparative analysis)
- ✅ Professional yet engaging tone
- ✅ Preserves all key information (metrics, scores, technical details)
- ✅ Forward-looking conclusion (acknowledges future improvements)

**Weaknesses:**
- ⚠️ Slightly long (4 paragraphs) but justified by completeness
- Minor: Could potentially combine first two sentences, but current structure works

**Why This Won:**
1. **Best narrative arc:** Clear beginning (need/goal), middle (execution/evaluation), end (result/future)
2. **Transformation framing:** "Transforming a complex decision framework" immediately establishes value
3. **Journey metaphor:** "The journey from concept to publication-ready design" creates engaging throughline
4. **Multi-level revelation:** Explains overview, then details, then comparative analysis, then implications
5. **Balanced tone:** Professional technical accuracy with accessible storytelling
6. **Complete story:** Answers all questions a future developer would have:
   - What was created? (Matrix with 15 applications)
   - How? (Gemini-generate, 86.7 seconds, 3 variants)
   - Why this version? (91% score, superior across 5 dimensions)
   - What makes it good? (Clean aesthetic, scanability, multi-level value)
   - What's next? (Optional iconography enhancements)

---

## Narrative Commit Message Template

Use this structure for complex commits that deserve storytelling treatment:

```
<type>(<scope>): <subject line - transformation/achievement>

<PARAGRAPH 1: Context & Execution>
This commit [completes/achieves/implements] <goal>, [transforming/enabling/creating]
<value proposition>. The [journey/approach/process] from <starting point> to
<end state> [involved/took/required] <key details about execution>.

<PARAGRAPH 2: Technical Details & Results>
<Primary outcome> achieved <metric>, establishing itself as <superlative> through
<key achievements>. [Describe technical implementation details, key metrics,
component organization, or architectural decisions.]

<PARAGRAPH 3: Rationale & Comparative Analysis>
The [evaluation/analysis/investigation] revealed [why/how] <outcome> outperformed
<alternatives>. [Explain design decisions, trade-offs, or comparative advantages.]
<Alternative A> [suffered from/compromised] <weakness>, while <Alternative B>
[sacrificed/lacked] <other weakness>.

<PARAGRAPH 4: Impact & Future Directions>
The result: <summary of achievement and alignment with standards>. <Current status>
with <assessment of readiness>, though <optional future improvements>.

🤖 Generated with Claude Code (https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

---

## When to Use Narrative vs. Bullet Style

### Use Narrative Style When:
- ✅ Complex feature with multiple components or decisions
- ✅ Evaluation or comparison was performed (A/B testing, variant selection)
- ✅ Design rationale is important for future maintainers
- ✅ Multiple approaches were considered
- ✅ Change has significant impact or enables new capabilities
- ✅ Story provides valuable context for code archaeology

**Examples:**
- Major feature additions with architectural decisions
- Design system implementations with variant testing
- Performance optimizations with benchmarking results
- Refactorings that improve structure (explain why)
- Migrations or breaking changes (context is critical)

### Use Bullet Style When:
- ✅ Simple, focused change
- ✅ Bug fix with clear before/after
- ✅ Documentation update
- ✅ Dependency update
- ✅ Routine maintenance
- ✅ Quick facts are more valuable than story

**Examples:**
- "Fix typo in README"
- "Bump dependency from 1.2 to 1.3"
- "Add missing null check in validation"
- "Update copyright year"

---

## Narrative Techniques for Technical Writing

### 1. Transformation Framing
**Before:** "Add VIS-5.4 matrix"
**After:** "Transform complex decision framework into scannable matrix"

**Why it works:** Emphasizes value and outcome, not just action.

### 2. Journey Metaphor
**Before:** "Generated 3 variants and selected best"
**After:** "The journey from concept to publication-ready design took 86.7 seconds"

**Why it works:** Creates narrative throughline, makes process engaging.

### 3. Multi-Level Revelation
**Structure:**
- Paragraph 1: High-level goal and execution
- Paragraph 2: Technical details and primary metrics
- Paragraph 3: Comparative analysis and rationale
- Paragraph 4: Impact and future directions

**Why it works:** Mirrors Tufte's principle - readers can stop at any level and gain value.

### 4. Comparative Analysis
**Pattern:** "<Winner> achieved <metric> while <Alternative A> suffered from <weakness> and <Alternative B> compromised <other aspect>"

**Why it works:** Explains not just what was chosen but why, documenting decision rationale.

### 5. Results-Oriented Conclusion
**Before:** "Variant #3 selected"
**After:** "The result: textbook adherence to EventAI guidelines and Tufte's principles. Publication-ready with zero critical issues."

**Why it works:** Emphasizes outcome and quality, provides clear status.

---

## Quality Checklist

Before finalizing a narrative commit message, verify:

**Story Completeness:**
- [ ] Explains what was done
- [ ] Explains how it was done
- [ ] Explains why this approach
- [ ] Explains impact/outcome
- [ ] Provides context for future readers

**Technical Accuracy:**
- [ ] All metrics and numbers verified
- [ ] Technical details accurate
- [ ] No hallucinated information
- [ ] Terminology consistent with codebase

**Readability:**
- [ ] Clear paragraph structure
- [ ] Good transitions between ideas
- [ ] Professional yet engaging tone
- [ ] No jargon without context
- [ ] Scannable (can skim for key points)

**Completeness:**
- [ ] Preserves all important facts
- [ ] Documents decisions and rationale
- [ ] Notes alternatives considered
- [ ] Mentions future improvements if relevant

**Format:**
- [ ] Subject line under 72 characters
- [ ] Subject uses imperative mood
- [ ] Blank line between subject and body
- [ ] Body wrapped at 72 characters (or reasonable length)
- [ ] Conventional commit type (`feat:`, `fix:`, etc.)

---

## Examples from EventAI Project

### Good: Narrative Style for Complex Feature

```
feat(visuals): Add VIS-5.4 Use Cases Matrix - Variant #3 approved (91%)

This commit completes VIS-5.4, transforming a complex decision framework
into a scannable matrix that festival professionals can use to evaluate
15 predictive analytics applications across their operations. The journey
from concept to publication-ready design took 86.7 seconds through
gemini-generate browser automation, producing three variants evaluated
against EventAI visual identity standards and Tufte's information
visualization principles.

[... continues with technical details, comparative analysis, impact ...]
```

**Why this works:**
- Leads with transformation/value
- Provides execution context
- Documents decision process
- Valuable for future code archaeology

### Good: Bullet Style for Simple Fix

```
fix(infographics): Correct VIS-3.2 ROI percentage (was 42%, should be 47%)

Data accuracy verification against source material revealed discrepancy:
- Source (McKinsey 2024): 47% of organizations report zero ROI
- VIS-3.2 infographic: incorrectly showed 42%
- Updated infographic to match source
- Re-exported as PNG and WebP (1080p)

Fixes #127
```

**Why this works:**
- Clear, factual, quick to scan
- Bullet structure appropriate for simple change
- Still provides context (why changed, what source)
- Issue reference for traceability

---

## Final Recommendations

1. **Default to narrative for significant changes:** If it took thought and evaluation, tell that story.

2. **Use bullets for quick facts:** When the change is straightforward, respect reader's time.

3. **Always explain "why":** Whether narrative or bullets, document rationale.

4. **Future-proof your commits:** Write for the developer who will read this in 6 months (might be you).

5. **Preserve key facts:** Metrics, scores, alternatives considered - all valuable for project history.

6. **Grade your drafts:** Write multiple versions, evaluate them, choose the best.

7. **Read it aloud:** Good narrative flows naturally when spoken.

---

*Guide created: December 30, 2025*
*Project: EventAI + Lemmy Content Generation System*
*Author: Claude Sonnet 4.5*
*Status: Living document - update as patterns emerge*
