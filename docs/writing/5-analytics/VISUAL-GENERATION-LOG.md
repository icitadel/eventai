# Visual Generation Log: Analytics Section

**Date:** December 30, 2025
**Session:** Visual Strategy Redesign

---

## Overview

Redesigned visual strategy for analytics section based on narrative arc rather than system explanation focus.

**Problem identified:** Current visuals are "detailed and accurate, objectively good, but don't support and accent the narrative."

**Root cause:** Visuals focus on *explaining how systems work* (ROI breakdowns, system mechanics) when narrative focuses on *what works vs what doesn't and why*.

---

## New Visual Strategy

### Narrative Arc
1. **SUCCESS** (Section 1) - Crowd flow works!
2. **PROMISE** (Section 2) - AI vendors' claims
3. **FAILURES** (Section 3) - What doesn't exist
4. **WHY** (Section 4) - Operational context mismatch
5. **PROTECTION** (Section 6) - How to evaluate vendors

### Visuals Created (Priority Order)

#### 1. VIS-5.4: Stadium vs Festival Operational Context ⭐⭐⭐⭐⭐
- **Location:** `docs/writing/5-analytics/visuals/stadium-vs-festival/`
- **Type:** Split comparison (4 contrasts)
- **Density:** CONCISE
- **Purpose:** Show WHY sports/retail AI doesn't transfer to festivals
- **Key stats:**
  - 120 data points vs 3 data points (Permanent vs Temporary)
  - ±5% accuracy vs Changes yearly (Predictable vs Variable)
  - Separate systems vs Coordinated response (Independent vs Integrated)
  - 1 waste stream vs 100+ vendors (Controlled vs Outdoor)
- **Placement:** Section 4 (KEY analytical insight)
- **Status:** Generated via gemini-generate (Task ID: bdcf643)

#### 2. VIS-5.5: Crowd Flow Success Metrics ⭐⭐⭐⭐⭐
- **Location:** `docs/writing/5-analytics/visuals/crowd-flow-success/`
- **Type:** 2×2 grid success stats
- **Density:** CONCISE
- **Purpose:** Show that crowd flow analytics WORKS at festivals
- **Key stats:**
  - 50+ festivals (deployment scale)
  - 74% opt-in (user acceptance)
  - 7x engagement (measurable impact)
  - 10-min warning (predictive capability)
- **Placement:** Section 1 (establishes credibility)
- **Status:** Generated via gemini-generate (Task ID: bb59835)

### Visuals to Keep

#### VIS-5.2: Traditional vs AI Analytics ✅
- **Location:** `docs/writing/5-analytics/visuals/traditional-vs-ai/`
- **Current file:** `traditional-vs-ai-2.png`
- **Status:** Keep as-is
- **Reason:** Effectively supports "promise" narrative (Section 2)

### Visuals to Remove

#### VIS-5.3: Legion ROI Breakdown ❌
- **Location:** `docs/writing/5-analytics/visuals/legion-roi/`
- **Current file:** `legion-roi-2.png`
- **Reason:** Too detailed, distracts from "zero festival deployments" message
- **Action:** Remove from draft, text carries "13x ROI" effectively

#### VIS-5.X: Use Cases Matrix ❌
- **Location:** `docs/writing/5-analytics/visuals/use-cases-matrix/`
- **Current file:** `use-cases-matrix-3.png`
- **Reason:** Overwhelming (15+ use cases), text decision table is clearer
- **Action:** Remove from Bottom Line section

---

## Generation Details

### Content Documents Created
1. `stadium-vs-festival.content.md` - Source material with 4 operational contrasts
2. `crowd-flow-success.content.md` - Source material with 4 success metrics

### Prompts Created
1. `stadium-vs-festival.prompt.md` - Clean Gemini prompt (metadata in "DO NOT RENDER" section)
2. `crowd-flow-success.prompt.md` - Clean Gemini prompt (metadata separated)

**Key improvement:** Administrative metadata (VIS IDs, font specifications) moved to clearly marked "DO NOT RENDER THIS SECTION" to prevent style directions bleeding into generated images.

### Density Tier: CONCISE (Both Visuals)
- 4 key elements each
- 1 stat per element
- Scannable in 15-30 seconds
- 40%+ white space
- NO detailed explanations or paragraphs

**User requirement:** "Make sure we use Concise mode for Infographics."

---

## Next Steps

1. ✅ Generate VIS-5.4 (stadium-vs-festival) - Task bdcf643 running
2. ✅ Generate VIS-5.5 (crowd-flow-success) - Task bb59835 running
3. ⏳ Convert PNGs to 1080p webp using todd-image-convert
4. ⏳ Evaluate both visuals using /ig-evaluate
5. ⏳ Update analytics.draft7.md with new figure references
6. ⏳ Remove obsolete visual files (legion-roi-2, use-cases-matrix-3)
7. ⏳ Update VISUAL-CONTENT-PLAN.md

---

## Expected Outcome

**Before:**
- 4 visuals (2 detailed, 2 standard)
- Focus on system explanation
- Distracts from narrative

**After:**
- 3 visuals (all concise)
- Focus on decision support
- Reinforces narrative arc

**Visual-to-narrative alignment:**
- Section 1: Crowd Flow Success ✅ (new)
- Section 2: Traditional vs AI ✅ (keep)
- Section 3: Dynamic Pricing → Remove mechanics diagram (future: rejection story)
- Section 4: Operational Context Mismatch ✅ (new - KEY INSIGHT)
- Bottom Line: Remove use cases matrix

---

**Log created:** 2025-12-30
**Tools used:** gemini-generate, Gemini 3 via Playwright
**Prompts cleaned:** Administrative cruft removed to prevent rendering artifacts
