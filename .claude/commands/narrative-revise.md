# Narrative Revision Command

## Purpose

Transform content into concise, flowing narrative using accessible prose principles while enforcing thematic consistency with the question posed. This command ensures every section directly answers the question, applies narrative best practices to reduce word count, and structures documents with explicit Question + Narrative + Points framework.

## When to Use

Use this command when you have content that needs:
- Concise narrative transformation (cut 30-50% word count)
- Better paragraph flow (merge choppy one-sentence paragraphs)
- More conversational voice (contractions, "you," direct language)
- Improved readability (varied sentence length, better transitions)

**DO use for:**
- Academic/verbose drafts that need tightening
- Bullet-point content that should become narrative prose
- Content with too many one-sentence paragraphs
- Formal writing that needs conversational tone

**DO NOT use for:**
- Content that's already concise and well-flowing
- Creative fiction (different style requirements)
- Technical specifications (precision over flow)
- Legal documents (formal language required)

## Use Cases & Target Word Counts

| Use Case | Target Range | Characteristics |
|----------|--------------|-----------------|
| **Concise Infographic** | 30-60 words | Visual-first, headline stats only, minimal labels (see gemini-generate, infographics-bestpractices) |
| **Standard Infographic** | 80-150 words | Balanced detail, category labels, brief explanations (30-60 sec comprehension) |
| **Detailed Infographic** | 200-400 words | Comprehensive annotations, educational context (2-3 min comprehension) |
| **Instagram Post** | 150-400 words | Punchy, scannable, mobile-friendly |
| **Blog Post** | 800-1,200 words | Conversational, SEO-friendly, subheaders |
| **Textbook Section** | 1,500-2,000 words | Educational, thorough, accessible |
| **Magazine Article** | 1,500-2,500 words | Engaging narrative, human interest |
| **White Paper** | 2,500-5,000 words | Authoritative, detailed, evidence-based |
| **Long-Form Feature** | 3,000-6,000 words | Deep dive, storytelling, comprehensive |

## Core Principles

This command applies five narrative best practices:

### 1. Conversational Voice
- **Use contractions**: don't, can't, won't, you'll, it's, they're
- **Use "you" relentlessly**: Transform third-person → second-person
- **Short sentences for emphasis**: 10-15 words average
- **Longer sentences for development**: 20-30 words for nuance
- **Ask rhetorical questions**: Engage readers in dialogue
- **Be blunt when appropriate**: Clear claims over hedging

### 2. Ruthless Conciseness
- **Cut filler words**: very, really, actually, basically, literally
- **Eliminate throat-clearing**: "It is interesting to note that..."
- **Active voice**: "John threw the ball" (not "was thrown by")
- **Target 30-40% reduction**: From academic/verbose style
- **Every word earns its place**: No redundancy

### 3. Narrative Structure
- **Topic sentences**: Clear controlling idea per paragraph
- **Transitions signal relationships**: however, therefore, building on this
- **Back-references**: "This approach," "These findings"
- **Concrete before abstract**: Examples first, principles second
- **Inverted pyramid**: Most important information first

### 4. Selective Formatting
- **Bold 1-3 key terms** per section for scanning anchors
- **Subheadings as signposts**: Informative, not vague
- **Short paragraphs**: 3-5 sentences typical, 1-sentence for punch
- **Reserve bullets** for truly list-like content (steps, features)
- **Prose for persuasion**: When ideas must connect and build

### 5. Strong Bookends
- **BLUF opening**: Bottom Line Up Front, state conclusion first
- **Hook readers immediately**: Surprising stat, provocative question, anecdote
- **Synthesize, don't summarize**: Draw meaning, point to implications
- **Echo opening in closing**: Return to opening image with evolved understanding

## Command Usage

```
/narrative-revise [file or content] [optional: target word count]
```

**Examples:**
```
/narrative-revise privacy.draft4.md 1500-2000
/narrative-revise analytics-research.md blog
/narrative-revise "Here's a verbose paragraph..." concise
```

## Workflow

### Step 0: Thematic Consistency Analysis (REQUIRED FIRST STEP)

**Before any narrative transformation, analyze whether each section actually answers the question posed.**

#### 0.1: Identify the Question

**Locate the question at the top of the document:**
- Should be explicitly stated in a "Question" or similar heading
- If missing, infer from title, learning objectives, or opening paragraphs
- Document the question clearly before proceeding

**Example:**
```markdown
# Question
> In your view, what is the ultimate, long-term future of AI in the festival
> and live events industry over the next decade? What will be the most
> significant, visible difference for the average attendee?
```

#### 0.2: Rate Each Section for Relevance

**For each major section, rate relevance to the question (1-10 scale):**

| Rating | Meaning | Action |
|--------|---------|--------|
| **9-10** | Directly answers the question | Keep, potentially strengthen |
| **7-8** | Provides essential context | Keep, ensure clear connection |
| **5-6** | Useful background, tangential | Condense or reframe |
| **3-4** | Weakly related, optional | Consider removing/moving |
| **1-2** | Off-topic, answers different question | Remove or move to appendix |

**Rating criteria:**
- Does this section directly answer the question posed?
- Is this information necessary to understand the answer?
- Could the question be answered fully without this section?
- Does this section answer a *different* question than the one posed?

**Example analysis:**
```
Section: "What Attendees Will Experience" - 10/10
  → Directly answers "What will be the most significant, visible difference?"

Section: "Three-Phase Transformation" - 10/10
  → Directly answers "What is the long-term future over the next decade?"

Section: "Why AI Fails Most of the Time" - 6/10
  → Provides context for realistic expectations but doesn't answer what the future IS
  → Answers "Why might it not happen?" not "What will happen?"
  → DECISION: Condense by 50% or integrate into timeline as barriers

Section: "What Actually Works" - 5/10
  → Answers "How to implement successfully" not "What is the future?"
  → Implementation tactics, not outcome predictions
  → DECISION: Remove or move to appendix/different document
```

#### 0.3: Handle Tangential Sections

**For sections rated below 7/10, choose one approach:**

**Option 1: Delete entirely**
- Use when: Section answers a completely different question
- Example: Implementation best practices in a document about future predictions

**Option 2: Condense significantly (50-70% reduction)**
- Use when: Section provides useful context but is over-developed
- Keep core insight in 1-2 paragraphs
- Example: "Why AI Fails" condensed to acknowledge barriers without full analysis

**Option 3: Reframe within high-relevance sections**
- Use when: Information supports the answer but is misplaced
- Example: Move barrier discussion into timeline phases ("Phase 1 faces these challenges...")

**Option 4: Move to appendix**
- Use when: Information is valuable but tangential
- Create "Context: [Topic]" or "Appendix: [Topic]" section
- Example: "Appendix: Implementation Best Practices for Festival AI"

**Document your decisions:**
```markdown
## Thematic Consistency Decisions

Sections removed:
- "What Actually Works" (5/10 relevance) → Answers implementation question, not future prediction
- Moved to: appendix-implementation-patterns.md

Sections condensed:
- "Why AI Fails" (6/10 relevance) → 500 words → 150 words
- Reason: Provides context for realistic predictions but over-developed
- Action: Keep 80% failure stat, remove detailed five-barrier analysis

Sections strengthened:
- "Bottom Line" (9/10) → Add explicit return to attendee experience to bookend answer
```

#### 0.4: Verify Document Structure

**Required structure for question-answer documents:**

```markdown
# Question
> [The question being answered, verbatim]

---

# Narrative

**Target:** [word count range, e.g., "1,500-2,000 words"]

[2-3 sentence summary that directly answers the question]

**This narrative covers [3-5] points:**

- **Point 1: [Title]** — [1 sentence describing what this section argues]
- **Point 2: [Title]** — [1 sentence describing what this section argues]
- **Point 3: [Title]** — [1 sentence describing what this section argues]
- **Point 4: [Title]** — [1 sentence describing what this section argues] (optional)
- **Point 5: [Title]** — [1 sentence describing what this section argues] (optional)

---

# [Title for Article/Section]

**Learning Objectives:** (if educational content)
- [Objective 1]
- [Objective 2]
- [Objective 3]

---

## [Section matching Point 1]
[Content that develops Point 1...]

## [Section matching Point 2]
[Content that develops Point 2...]

## [Section matching Point 3]
[Content that develops Point 3...]

## [Conclusion/Bottom Line]
[Synthesis and implications...]

---

**Sources:**
[Bibliography...]
```

**Structural requirements:**
1. **Question section**: Explicit statement of question being answered
2. **Narrative section**:
   - Word count target (e.g., "1,500-2,000 words" for textbook sections)
   - 2-3 sentence direct answer to the question
   - 3-5 point preview of the argument
3. **Body sections**: Each point has corresponding section(s) in body
4. **No orphaned sections**: Every major section maps to a point or is removed
5. **Proper bookends**: Opening narrative + closing synthesis that echoes it
6. **Learning objectives**: Immediately after title (for educational content)

**Word count targets by use case:**
- Textbook section: 1,500-2,000 words
- Blog post: 800-1,200 words
- White paper: 2,500-5,000 words
- Instagram post: 150-400 words

**If structure is missing:**
- Create it before proceeding with narrative transformation
- Extract the core argument from existing content
- Map existing sections to points or mark for removal/condensing

### Step 1: Analyze Current State

**Use docutil CLI for baseline metrics:**

For .docx files:
```bash
docutil analyze-density privacy.draft4.docx
docutil count-words privacy.draft4.docx
```

Expected output:
```
Document Structure:
  Total words: 3,324
  Total sentences: 296
  Total paragraphs: 121

Density Metrics:
  Words per sentence: 11.2
  Sentences per paragraph: 2.4
```

**Quality indicators from metrics:**
- **Words per sentence < 15**: Good readability
- **Words per sentence 15-20**: Moderate complexity
- **Words per sentence > 20**: Too complex, needs simplification
- **Sentences per paragraph < 2**: Too choppy (one-sentence paragraphs)
- **Sentences per paragraph 2-5**: Good flow
- **Sentences per paragraph > 5**: Too dense, needs breaking up

**Manual analysis:**
- **Read the content** to understand structure and voice
- **Identify problems**: choppy paragraphs, verbose explanations, formal tone
- **Note key facts** that must be preserved

### Step 2: Apply Narrative Transformation

**Merge one-sentence paragraphs:**
```markdown
❌ BEFORE (choppy):
The GSMA deployed facial recognition.

Spain fined them €200,000.

The violation was inadequate DPIA.

✅ AFTER (flowing):
The GSMA deployed facial recognition for conference entry. Spain fined them €200,000 anyway. The violation: inadequate DPIA documentation failed to examine necessity and proportionality.
```

**Add contractions:**
```markdown
❌ BEFORE: Festivals cannot claim "general security."
✅ AFTER: Festivals can't claim "general security."

❌ BEFORE: You will encounter pressure to deploy surveillance AI.
✅ AFTER: You'll encounter pressure to deploy surveillance AI.
```

**Vary sentence length:**
```markdown
✅ GOOD RHYTHM:
No signage. No opt-in. No way to decline. [3 short punches]

When Rolling Stone broke the story, the ACLU condemned it as "unacceptable surveillance." [Longer development]

Regulators still cite the incident today. [Medium transition]
```

**Cut redundancy:**
```markdown
❌ BEFORE (84 words):
The festival industry has actively rejected dynamic pricing despite the technology's proven success in other live entertainment venues. DICE CEO Phil Hutcheon clarified the company's actual deployment...

✅ AFTER (52 words):
The festival industry has rejected dynamic pricing. DICE CEO Phil Hutcheon: "We've never had an artist approach us for dynamic pricing." DICE processes 40-41% of sales through AI recommendations—not pricing optimization.
```

### Step 3: Verify Quality

**Use docutil to compare before/after metrics:**

```bash
# Analyze revised version
docutil analyze-density privacy.draft5.docx
docutil count-words privacy.draft5.docx
```

**Compare metrics:**
```
BEFORE (draft4):
  Words per sentence: 18.5
  Sentences per paragraph: 1.8
  Total words: 3,324

AFTER (draft5):
  Words per sentence: 14.2  ✅ Improved readability
  Sentences per paragraph: 2.9  ✅ Better flow
  Total words: 1,822  ✅ 45% reduction
```

**Quality targets:**
- **Word count reduction**: 30-50% fewer words
- **Words per sentence**: Reduced to 12-16 (from 18-24)
- **Sentences per paragraph**: Increased to 2-4 (from 1-2)
- **No information loss**: 100% of facts preserved

**Manual verification:**
- No excessive one-sentence paragraphs
- Clear topic sentences throughout
- Smooth transitions between ideas
- Contractions used throughout
- "You" address where appropriate
- Mix of short punchy and longer flowing sentences
- Bold headers scannable
- 1-3 key terms bolded per section

### Step 4: Output Results

Create revised file with narrative improvements applied.

**File naming:**
- If input is `draft4.md` → output `draft5.md`
- If input is `research.md` → output `research-revised.md`

**Include summary with docutil metrics:**
```markdown
## Narrative Revision Summary

### Docutil Metrics Comparison

**BEFORE (draft4.docx):**
- Total words: 3,500
- Words per sentence: 18.5
- Sentences per paragraph: 1.8

**AFTER (draft5.docx):**
- Total words: 1,822
- Words per sentence: 14.2
- Sentences per paragraph: 2.9

**Improvement:**
- 48% word reduction
- 23% more concise sentences
- 61% better paragraph flow

### Changes Applied:
✅ Merged 15 one-sentence paragraphs into flowing narrative
✅ Added contractions throughout (formal → conversational)
✅ Varied sentence length (short punches + longer development)
✅ Cut redundant explanations and throat-clearing
✅ Preserved 100% of factual claims

### Quality Checks:
✅ Words per sentence: 14.2 (was 18.5) - improved readability
✅ Sentences per paragraph: 2.9 (was 1.8) - better flow
✅ Conversational voice: contractions, "you," direct language
✅ Formatting: selective bolding, scannable headers
```

## Examples

### Example 1: Textbook Section (1,500-2,000 words)

**Input:**
```
privacy.draft4.md (3,500 words, academic tone, verbose)
```

**Command:**
```
/narrative-revise privacy.draft4.md 1500-2000
```

**Output:**
```
privacy.draft5.md (1,822 words, conversational, concise)
- Merged choppy paragraphs
- Added contractions
- Cut 48% word count
- Preserved all facts
```

### Example 2: Blog Post (800-1,200 words)

**Input:**
```
analytics-research.md (2,800 words, bullet points)
```

**Command:**
```
/narrative-revise analytics-research.md blog
```

**Output:**
```
analytics-blog.md (1,050 words, narrative prose)
- Converted bullets to flowing paragraphs
- Added conversational hooks
- Created scannable subheaders
```

### Example 3: Instagram Post (150-400 words)

**Input:**
```
festival-ai-summary.md (800 words, formal)
```

**Command:**
```
/narrative-revise festival-ai-summary.md instagram
```

**Output:**
```
festival-ai-instagram.md (280 words, punchy)
- Ultra-concise
- Mobile-friendly short paragraphs
- Direct, conversational voice
```

## Quality Standards

### ✅ Good Narrative Revision

**Before (Academic, Verbose):**
> The landscape is stark. Across 12 major universities offering event management degrees in the United Kingdom, zero programs provide systematic AI education specific to the discipline. This does not mean that students cannot use AI tools effectively, but rather that there is a fundamental gap between the education they receive and the AI-saturated industry they will encounter upon graduation.

**After (Conversational, Concise):**
> Here's where it gets bleak. Across 12 major UK universities offering event management degrees, zero provide systematic AI education for the discipline. You're graduating with zero AI frameworks specific to your field. This doesn't mean you can't use AI tools—but there's a fundamental gap between your education and the AI-saturated industry you're entering.

**What Changed:**
- "Here's where it gets bleak" (conversational hook)
- UK (concise abbreviation)
- "You're graduating" (second-person address)
- Contractions: doesn't, can't, you're
- Shorter sentences: 15-word average
- 89 words → 62 words (30% reduction)

### ❌ Poor Narrative Revision

**Bad Example 1: Lost Information**
```
❌ Before: "Roskilde achieved a 74% opt-in rate for wristband tracking"
❌ After: "Roskilde had high opt-in" (lost the 74% figure!)
```

**Bad Example 2: Too Choppy**
```
❌ Every paragraph is one sentence.
❌ This creates staccato rhythm.
❌ It's exhausting to read.
❌ Sentences don't connect.
❌ Ideas feel fragmented.
```

**Bad Example 3: Still Verbose**
```
❌ "It is important to note that when considering the implementation of facial recognition systems at festival venues, one must take into account the various regulatory frameworks..."
✅ "When deploying facial recognition at festivals, consider GDPR, BIPA, and EU AI Act requirements."
```

## Troubleshooting

**Problem: Word count didn't reduce enough**
- Check for redundant explanations (cut scaffolding)
- Look for throat-clearing phrases ("It is interesting to note that...")
- Verify active voice throughout (not passive)
- Cut unnecessary adjectives and adverbs

**Problem: Paragraphs still choppy**
- Merge related one-sentence paragraphs
- Add transitions between ideas
- Ensure each paragraph develops a single idea

**Problem: Voice still too formal**
- Search and replace: cannot → can't, do not → don't, etc.
- Change third-person → second-person ("students" → "you")
- Add conversational signposts ("Here's the catch...")

**Problem: Information was lost**
- Cross-reference all numerical claims (preserve exact figures)
- Verify all examples still present
- Check that condensation didn't change meaning

## Integration with Other Commands

**Before narrative-revise:**
- `/section-create` - Generate initial draft content
- Research and fact-gathering

**After narrative-revise:**
- `/validate` - Verify factual accuracy
- `/narrative-refine-validate` - Full fact-checking + sourcing
- `/optimize-tokens` - Further reduce if still too long

**Complementary commands:**
- `/textbook-bestpractices` - Educational content principles
- `/infographics-bestpractices` - Visual communication

## Notes

- This command focuses on **narrative transformation**, not fact-checking
- If content needs both narrative revision AND fact-checking, use `/narrative-refine-validate` instead
- Preserve all numerical claims, statistics, and factual assertions
- When in doubt, prioritize readability over brevity
- Different audiences need different tones (adjust accordingly)

---

**Command Created:** January 2, 2026
**Version:** 2.0 (Updated January 4, 2026 - Added thematic consistency analysis and structural requirements)
**Based On:** .claude/skills/narrative-bp.md
**Related Commands:** /narrative-refine-validate, /validate, /optimize-tokens
