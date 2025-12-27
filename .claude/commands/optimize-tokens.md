# Token Optimization Command

## Purpose

Optimize markdown documents for minimal token consumption by AI agents while preserving all substantive points and information.

## Core Approach

You are an expert technical writer with a meticulous eye for detail. Analyze the provided source, understand ALL the points being made, and drastically reduce the content and detail while preserving ALL of the points being made.

## Optimization Strategies

### Text Reduction Techniques

**Rephrase for conciseness:**
- Convert verbose sentences to terse, information-dense alternatives
- Example: "The research indicates that there are several important factors that need to be taken into consideration when we are thinking about implementing this approach in production environments." → "Key factors for production implementation:"

**Reorganize structure:**
- Group related concepts
- Eliminate redundancy
- Use hierarchical bullets for clarity

**Reduce to fragments:**
- Use bullet points and sentence fragments over full narratives
- Strip unnecessary articles (a, an, the) when meaning is clear
- Remove transition phrases ("In conclusion," "As mentioned above," "It's important to note that")

**Extract URLs:**
- Provide unique URL lists at end of document
- Strip querystring parameters (e.g., `?utm_source=twitter&ref=123`)
- Deduplicate repeated URLs

**Remove fluff:**
- Eliminate filler words (very, really, quite, actually, basically)
- Cut redundant examples (keep only most illustrative)
- Remove excessive context (assume informed reader)
- Strip marketing language and superlatives

---

## What to Preserve

✅ **Preserve:**
- All unique facts, claims, arguments
- Technical details, numbers, dates, statistics
- Logical relationships between concepts
- Critical warnings or caveats
- Source attributions and citations
- Decision criteria and frameworks
- Recommendations and action items
- Comparison tables and data matrices

❌ **Remove:**
- Introductory/transitional phrases
- Redundant examples (keep best 1-2)
- Verbose explanations when bullet point suffices
- Marketing language ("revolutionary," "game-changing," "cutting-edge")
- Excessive context setting
- Filler paragraphs that restate earlier points
- Overly detailed background (assume reader has domain knowledge)

---

## Optimization Process

### Step 1: Analysis Phase

1. **Identify all distinct points/claims/facts**
   - Make mental inventory of every unique piece of information
   - Note relationships and dependencies

2. **Map document structure**
   - Identify logical sections
   - Note where redundancy occurs

3. **Extract all URLs**
   - Collect every unique URL
   - Strip querystring parameters

4. **Identify redundancies**
   - Flag repeated concepts
   - Note verbose sections that can be condensed

### Step 2: Optimization Phase

1. **Preserve all unique information points**
   - Ensure no facts are lost
   - Maintain decision criteria

2. **Reduce narrative prose to bullet fragments**
   - Convert paragraphs to bullets
   - Use sentence fragments where clear
   - Remove unnecessary verbs (is, are, has, have when context is clear)

3. **Eliminate redundancy, filler, verbose phrasing**
   - Cut repeated examples
   - Remove transition sentences
   - Consolidate related bullets

4. **Consolidate related concepts**
   - Group similar ideas under single bullets with sub-bullets
   - Use tables for comparative data

5. **Extract URL list**
   - Move to "Sources" or "Referenced URLs" section at end
   - Deduplicate, strip parameters, alphabetize

### Step 3: Verification Phase

Before finalizing, verify:

- [ ] All substantive points from source preserved
- [ ] No factual information lost
- [ ] URLs extracted and cleaned
- [ ] Redundancy eliminated
- [ ] Maximum conciseness achieved
- [ ] Logical flow maintained
- [ ] Markdown properly formatted

---

## Output Format

### Standard Structure

```markdown
# [Original Document Title] - Optimized

## Summary
[Ultra-concise 1-2 sentence overview]

## Key Points
- [Point 1]
- [Point 2]
- [Point 3]

## [Section 1 Name]
- [Optimized content]
  - [Sub-point if hierarchical]
  - [Sub-point if hierarchical]
- [Next point]

## [Section 2 Name]
- [Optimized content]

## Decision Criteria / Recommendations
- [Actionable items]
- [Decision frameworks]

## Sources
- [URL 1]
- [URL 2]

---
**Optimization Stats**
- Original: ~X tokens
- Optimized: ~Y tokens
- Reduction: Z%
```

---

## Token Estimation

**Rough estimates:**
- 1 token ≈ 4 characters
- Target reduction: 40-70% of original
- Acceptable range: 30-75% (depends on original verbosity)
- **Maximum acceptable reduction:** No information loss

**Before/After Example:**

**Before (Verbose - ~150 tokens):**
```
When evaluating potential Third Space locations in the Seattle metropolitan area,
there are a number of important factors that business owners and entrepreneurs need
to carefully consider. First and foremost, the demographic composition of the
neighborhood is absolutely critical, as you want to ensure that there is a
sufficient population of young professionals in the 25-44 age range who have
disposable income to spend on premium dessert experiences. Additionally, the
competitive landscape needs to be thoroughly analyzed to determine whether there
are already too many similar dessert venues operating late-night hours in the
immediate vicinity.
```

**After (Optimized - ~45 tokens):**
```
## Location Evaluation Criteria
- **Demographics:** Target 25-44 age range, disposable income for premium desserts
- **Competition:** Analyze existing late-night dessert venues in immediate area
```

**Reduction: 70%**

---

## Special Cases

### Tables and Data

**Preserve tables** but optimize content:

**Before:**
| Factor | Description | Why It Matters |
|--------|-------------|----------------|
| Demographics | The age, income, and lifestyle characteristics of residents | Understanding demographics helps determine if there's a market |

**After:**
| Factor | Key Metrics | Importance |
|--------|-------------|------------|
| Demographics | Age 25-44, income $50K+, renter % | Market validation |

### Decision Frameworks

**Preserve decision logic** but compress examples:

**Before:**
```
If the location has 6 or more green flags, you should pursue detailed research.
For example, if a location has good demographics, low competition, strong foot
traffic, excellent parking, good transit access, and moderate rent, that would
be 6 green flags and you should definitely investigate further.
```

**After:**
```
**Decision Rule:**
- 6+ green flags → Pursue detailed research
- 4-5 green flags, 0-1 red → Consider if strategic advantage
- 3+ red flags → Pass
```

### Citations and Sources

**Always preserve but consolidate:**

**Before:**
```
According to data from Point2Homes (https://www.point2homes.com/US/Neighborhood/WA/Seattle/Fremont-Demographics.html),
the median household income is $132,560. AreaVibes (https://www.areavibes.com/seattle-wa/fremont/demographics/)
reports similar figures, while Zumper (https://www.zumper.com/rent-research/seattle-wa/fremont)
shows rental data.
```

**After:**
```
Median household income: $132,560

**Sources:** Point2Homes, AreaVibes, Zumper (see URLs section)
```

---

## Usage Instructions

### For Single Document

```bash
# Read document and optimize
optimize-tokens [path-to-document.md]

# Output will be created as [document]-optimized.md
```

### For Research Documents

```bash
# Optimize a research file
optimize-tokens docs/business-plan-2026/03-market-analysis/research/R-015-fremont-third-space-evaluation.md

# Creates: R-015-fremont-third-space-evaluation-optimized.md
```

### Quality Check

After optimization, verify against original:
1. Scan optimized version - can you understand all key points?
2. Compare bullet points count - did we preserve all unique claims?
3. Check decision criteria - are frameworks intact?
4. Verify numbers - all statistics/metrics present?
5. Review recommendations - actionable items clear?

---

## Common Optimization Patterns

### Pattern 1: Verbose Background → Concise Context

**Before (8 lines):**
```
Capitol Hill is one of Seattle's most vibrant and diverse neighborhoods, known for
its thriving arts scene, LGBTQ+ community, and late-night culture. The Pike-Pine
corridor in particular has emerged as a major entertainment district with numerous
bars, restaurants, and music venues that stay open until 2 AM or later. This
creates a unique opportunity for a late-night dessert venue that can capture
customers after they finish dinner or drinks but before they head home for the night.
```

**After (3 lines):**
```
## Capitol Hill Market
- Pike-Pine corridor: bars/restaurants open to 2 AM
- Opportunity: Late-night dessert between drinks and home
```

---

### Pattern 2: Redundant Examples → Single Best Example

**Before (12 lines):**
```
There are many examples of successful brewery district partnerships. For instance,
Fremont Brewing could host popup events. Similarly, breweries in Ballard might
be interested in collaboration. Additionally, Georgetown has several breweries
that could work well. The key is finding a brewery with good foot traffic.
```

**After (3 lines):**
```
## Brewery Partnership Potential
- **Example:** Fremont Brewing popup at Urban Beer Garden
- **Criteria:** High foot traffic, community-focused brand
```

---

### Pattern 3: Long Methodology → Checklist

**Before (20 lines of paragraph text explaining process):**

**After (8 lines):**
```
## Research Process
**Phase 1: Desk Research (2-3 hrs)**
1. Demographics - Seattle.gov, Point2Homes
2. Competition - Google Maps, Yelp, hours analysis
3. Foot traffic - Popular Times, transit data
4. Real estate - LoopNet, PropertyShark comps
5. Grants - King County equity maps, OED programs
```

---

## Target Reduction by Document Type

**Research Reports (R-0XX):** 40-60% reduction
- Original: 500-900 lines → Optimized: 200-450 lines
- Preserve all data points, compress narratives

**Framework Documents (R-013):** 30-40% reduction
- Original: 460 lines → Optimized: 275-320 lines
- Preserve methodology intact, reduce examples

**Meeting Notes / Documentation:** 50-70% reduction
- Strip all "As mentioned," "It's important," etc.
- Bullet points only, fragment sentences

**Email / Communication:** 60-80% reduction
- Ultra-concise
- Action items, dates, decisions only

---

## Anti-Patterns (What NOT to Do)

❌ **Don't sacrifice clarity for brevity:**
```
Bad: "CH: 6+ GF, pursue"
Good: "Capitol Hill: 6+ green flags → Pursue detailed research"
```

❌ **Don't remove context that enables decision-making:**
```
Bad: "Rent too high"
Good: "Rent: $42/SF exceeds $38/SF threshold → Pass"
```

❌ **Don't over-abbreviate domain terms:**
```
Bad: "TS loc eval"
Good: "Third Space location evaluation"
```

❌ **Don't eliminate comparisons that inform decisions:**
```
Bad: "Good demographics"
Good: "Demographics: 48% age 25-44 vs 35% Seattle avg → Exceeds target"
```

---

## Success Metrics

**Optimization is successful when:**
- ✅ Information preservation: 100%
- ✅ Token reduction: 40-70%
- ✅ Readability: High (scannable, clear structure)
- ✅ Actionability: Decisions and recommendations clear
- ✅ Verifiability: Sources cited, numbers traceable

**Optimization failed if:**
- ❌ Key facts missing
- ❌ Decision criteria unclear
- ❌ Relationships between concepts lost
- ❌ Recommendations not actionable
- ❌ Sources not traceable

---

## Example: Before/After Full Document

### Before: R-015 Fremont (919 lines, ~45,000 tokens)

**Executive Summary (verbose):**
```
Recommendation: DEFER TO YEAR 2 POPUP VALIDATION with strong potential for
Year 3-4 permanent location.

Quick Assessment Score: 6-7 Green Flags (exceeds threshold for detailed research)

Key Strengths:
Fremont presents exceptional demographics with 48.2% of the population aged
25-44 years old and a median household income of $132,560, which positions
it well above our target market requirements. The neighborhood also features
a walkability score of 90, placing it in the top 10 most walkable neighborhoods
in Seattle. Additionally, Fremont has developed a strong brewery district
identity with establishments like Fremont Brewing, Urban Family, Outlander,
and Odin Brewing creating a unique cultural ecosystem. The late-night dessert
competition is notably low, with only Marmalade Desserts operating in the area,
and they close early rather than serving the late-night crowd.
```

### After: R-015 Fremont Optimized (~400 lines, ~18,000 tokens)

**Executive Summary (concise):**
```
## Recommendation
**DEFER TO YEAR 2 POPUP VALIDATION** - strong Year 3-4 potential

**Quick Assessment:** 6-7 Green Flags (exceeds 6+ threshold)

**Strengths:**
- Demographics: 48% age 25-44, $132K median income (exceeds targets)
- Walkability: Score 90 (top 10 Seattle)
- Brewery district: Fremont Brewing, Urban Family, Outlander, Odin
- Competition: Low (Marmalade closes early, no late-night dessert)
- Rent: Est. $28-35/SF (below Capitol Hill $30-40)

**Weaknesses:**
- Late-night culture: Moderate (bars close 10-11 PM vs Capitol Hill 2 AM)
- Transit: No light rail (bus-dependent)
- Grants: Low potential $10-25K (affluent area)
```

**Token reduction: ~60% (45K → 18K tokens)**

---

## Final Notes

**Philosophy:** Ruthlessly eliminate words, religiously preserve meaning.

**Quality over compression:** If forced to choose between 70% reduction with information loss vs 50% reduction with perfect preservation, always choose perfect preservation.

**Iterative improvement:** First pass may achieve 40% reduction. Second pass can often find another 10-20% without loss.

**Context matters:** Business-critical documents (investor pitches, grant applications) may warrant more conservative optimization (30-40%) than internal research notes (60-70%).

---

**Command maintained by:** Strategic Planning Team
**Last updated:** December 25, 2025
**Version:** 1.0
