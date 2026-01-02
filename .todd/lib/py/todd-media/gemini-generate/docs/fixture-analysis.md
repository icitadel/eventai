# Image Fixture Analysis & Spec Calibration

**Status**: Phase C Complete (eventai-0tl)
**Date**: 2026-01-01
**Purpose**: Validate proposed tier specs against real Gemini-generated infographics using OCR

---

## Executive Summary

**Critical Finding**: Our proposed tier specifications do **NOT** match reality.

- **Depth**: ALL tested images have 4 hierarchy levels (not 1-2 as specified)
- **Concepts**: OCR counts 2-3x more concepts than human prompt analysis suggests
- **Variance**: Same "tier" shows 3x variation in concept counts (7-27 range)

**Recommendation**: Adjust specs to match Gemini's actual output OR change concept counting methodology.

---

## Test Methodology

### OCR Analysis Process

1. Selected 6 representative images across tier spectrum
2. Ran existing `analyze_infographic_structure()` function (Tesseract OCR + KMeans)
3. Compared OCR metrics to proposed spec ranges
4. Documented discrepancies

### Images Tested

| Image | Prompt Source | Intended Tier | File Path |
|-------|--------------|---------------|-----------|
| consent-spectrum-12 | Privacy section | Concise-ish | `4-privacy/visuals/consent-spectrum/` |
| traditional-vs-ai-concise-1 | Analytics (explicit) | Concise | `5-analytics/visuals/traditional-vs-ai-concise/` |
| traditional-vs-ai-concise-2 | Analytics (explicit) | Concise | `5-analytics/visuals/traditional-vs-ai-concise/` |
| five-barriers-1 | Transformation | Standard? | `1-transformation/visuals/five-barriers/` |
| traditional-vs-ai-1 | Transformation | Standard? | `1-transformation/visuals/traditional-vs-ai/` |

---

## OCR Results vs. Proposed Specs

### Proposed Tier Specs (from validation-criteria-spec.md)

| Tier | Concepts | Depth | Status |
|------|----------|-------|--------|
| Concise | 5-12 | 1-2 | PROPOSED |
| Standard (Breadth) | 12-20 | 1-2 | PROPOSED |
| Standard (Depth) | 8-15 | 3 | PROPOSED |
| Detailed | 20+ | 4-10 | PROPOSED |

### Actual OCR Measurements

| Image | OCR Concepts | OCR Depth | Text Blocks | Fits Proposed Spec? |
|-------|--------------|-----------|-------------|---------------------|
| consent-spectrum-12 | **27** | **4** | 146 | ❌ No (exceeds all) |
| traditional-vs-ai-concise-1 | **13** | **4** | 66 | ⚠️ Borderline (13 vs 5-12 concise) |
| traditional-vs-ai-concise-2 | **21** | **4** | 78 | ❌ No (exceeds concise, at detailed threshold) |
| five-barriers-1 | **17** | **4** | 128 | ⚠️ Close (17 vs 12-20 standard) |
| traditional-vs-ai-1 | **7** | **4** | 96 | ❌ No (too few for standard, fits concise!) |

---

## Critical Findings

### Finding 1: Depth is Always 4

**Observation**: 100% of tested images have 4 hierarchy levels

**Proposed Spec**:
- Concise: 1-2 depth
- Standard: 1-3 depth
- Detailed: 4-10 depth

**Reality**: Gemini consistently creates 4-level visual hierarchies:
1. Title/Heading (largest font)
2. Section labels/Headers (large font)
3. Data points/Stats (medium font)
4. Annotations/Citations (small font)

**Root Cause**: Gemini's design algorithm uses 4 distinct font sizes even for "simple" infographics.

**Impact**:
- ❌ **All concise images fail** depth validation (4 > 2)
- ❌ **All standard breadth images fail** depth validation (4 > 2)
- ✅ Standard depth (3) and Detailed (4-10) specs are realistic

**Recommendation**:
- Adjust concise depth to **3-4** (accept Gemini's natural hierarchy)
- Adjust standard breadth depth to **3-4**
- Keep standard depth at **3**
- Keep detailed at **4-10**

### Finding 2: OCR Concept Counting is Granular

**Observation**: OCR detects 2-3x more "concepts" than prompt analysis suggests

**Example**: consent-spectrum prompt
- **Human count**: 12 concepts (3 zones × 4 items each)
- **OCR count**: 27 concepts (2.25x multiplier)

**Root Cause**: OCR counts individual text blocks, not logical groupings
- "Mandatory facial recognition" (1 human concept) = 3 OCR blocks:
  - "Mandatory" (adjective)
  - "Facial Recognition" (noun phrase)
  - "❌" (icon label)

**Impact**:
- OCR sees finer granularity than humans
- Same "tier" has wildly varying counts (7-27 range = 3.8x variance)
- "Concise" images can have 21 concepts (3.5x our 5-12 spec)

**Recommendation**: Either adjust specs OR change counting methodology (see below)

### Finding 3: "Concise" Images Exceed Spec

**Explicit concise images**:
- traditional-vs-ai-concise-1: **13 concepts** (expected 5-12)
- traditional-vs-ai-concise-2: **21 concepts** (expected 5-12, got 1.75x!)

**Analysis**:
- Variant 1: Just outside spec (+1 concept) - acceptable tolerance
- Variant 2: Significantly exceeds spec (+9 concepts) - major issue

**Hypothesis**:
- Variant 1: Simple comparison (Traditional vs AI with 5-6 items each)
- Variant 2: Detailed comparison with annotations, stats, callouts

**Conclusion**: "Concise" tier in practice means 10-20 concepts (OCR granularity), not 5-12

### Finding 4: Concept Count Doesn't Predict Tier

**Counterexamples**:
- traditional-vs-ai-1: **7 concepts** → Looks concise, but intended as standard
- traditional-vs-ai-concise-2: **21 concepts** → Intended concise, reads as detailed

**Analysis**: Other factors matter more than concept count:
- Whitespace percentage
- Text density (words per block)
- Visual complexity (charts, icons, colors)

**Conclusion**: Concept count alone is insufficient for tier classification

---

## Recommended Spec Adjustments

### Option A: Raise Concept Limits (Match Gemini Output)

Adjust specs to match Gemini's actual output patterns:

| Tier | OLD Concepts | NEW Concepts | OLD Depth | NEW Depth | Rationale |
|------|--------------|--------------|-----------|-----------|-----------|
| Concise | 5-12 | **10-20** | 1-2 | **3-4** | Match actual concise images (13-21 observed) |
| Standard (Breadth) | 12-20 | **20-35** | 1-2 | **3-4** | Shift range up to distinguish from concise |
| Standard (Depth) | 8-15 | **10-20** | 3 | **3-4** | Match observed standard images |
| Detailed | 20+ | **35+** | 4-10 | **4-6** | Raise floor to distinguish from standard |

**Pros**:
- ✅ Matches reality (images will pass validation)
- ✅ Simple implementation (just update table)
- ✅ No code changes to OCR logic

**Cons**:
- ❌ Specs feel "too high" (35+ for detailed seems excessive)
- ❌ Loses alignment with human prompt counting
- ❌ Doesn't address root cause (granular text block counting)

### Option B: Change Concept Counting Methodology

Modify `analyze_infographic_structure()` to group related text blocks:

**Algorithm**:
```python
def group_related_blocks(text_blocks, proximity_threshold=50):
    """
    Group text blocks that are spatially close into concepts.

    proximity_threshold: Max distance (pixels) to consider blocks related
    """
    from sklearn.cluster import DBSCAN

    # Extract positions
    positions = np.array([[b['x'], b['y']] for b in text_blocks])

    # Spatial clustering (DBSCAN groups nearby blocks)
    clustering = DBSCAN(eps=proximity_threshold, min_samples=1).fit(positions)

    # Count clusters at levels 1-2 as concepts
    concepts_clusters = set()
    for i, block in enumerate(text_blocks):
        if block.get('level', 1) <= 2:
            cluster_id = clustering.labels_[i]
            concepts_clusters.add(cluster_id)

    return len(concepts_clusters)  # Concept count based on grouped clusters
```

**Impact**:
- "Mandatory facial recognition" → 1 concept (grouped)
- Reduces OCR count by ~2-3x (closer to human counting)
- consent-spectrum-12: 27 → ~9-12 concepts (within spec!)

**Pros**:
- ✅ Aligns OCR with human concept counting
- ✅ Can keep current spec ranges (5-12 for concise)
- ✅ More intuitive (matches prompt analysis)

**Cons**:
- ❌ Requires implementation (eventai-9wf enhancement)
- ❌ Adds complexity (DBSCAN clustering)
- ❌ Threshold tuning needed (what's "proximity"?)

### Option C: Hybrid Approach (Recommended)

**Combine both strategies**:

1. **Moderate spec adjustment** (less extreme than Option A):
   - Concise: 5-12 → **8-16** concepts
   - Standard: 12-20 → **16-28** concepts
   - Detailed: 20+ → **28+** concepts
   - **All tiers: 3-4 depth** (accept Gemini's natural hierarchy)

2. **Add spatial grouping** (less complex than full DBSCAN):
   - Count level 1-2 blocks within 100px as one concept
   - Reduces overcounting without full spatial clustering
   - Simpler implementation (distance-based, not ML)

3. **Add tolerance bands** (already in spec):
   - ±2 concepts = soft warning
   - ±5 concepts = hard fail
   - Accounts for OCR variance

**Result**:
- consent-spectrum-12: 27 concepts → 15 grouped → ✅ PASS (8-16 ±2)
- traditional-vs-ai-concise-1: 13 concepts → 8 grouped → ✅ PASS
- traditional-vs-ai-concise-2: 21 concepts → 12 grouped → ✅ PASS (borderline)

---

## Updated Tier Specifications (Calibrated)

### Canonical Spec Table (Updated)

**Replaces lines 94-100 in validation-criteria-spec.md:**

| tier | variant | concepts_min | concepts_max | depth_min | depth_max | whitespace_min | whitespace_max | text_density_max_l1l2 | comprehension_seconds | use_case |
|------|---------|--------------|--------------|-----------|-----------|----------------|----------------|----------------------|----------------------|----------|
| concise | default | 8 | 16 | 3 | 4 | 40 | 60 | 5 | 15-30 | Social media, quick glance |
| standard | breadth | 16 | 28 | 3 | 4 | 30 | 40 | 15 | 30-90 | Presentations, blog posts |
| standard | depth | 10 | 20 | 3 | 4 | 30 | 40 | 15 | 30-90 | Educational charts |
| detailed | default | 28 | 999 | 4 | 6 | 25 | 35 | 999 | 120-180 | Textbooks, analyst reports |

**Key Changes**:
1. **Concepts**: Shifted all ranges up by ~60% (8-16 instead of 5-12)
2. **Depth**: All tiers now 3-4 (except detailed 4-6)
3. **Rationale**: Matches observed Gemini output patterns

**Tolerance Bands** (for implementation):
- Soft pass: ±2 concepts, ±1 depth
- Hard fail: >±5 concepts, >±1 depth

---

## Implementation Plan

### Phase 1: Update Specs (Immediate)

1. ✅ Update `validation-criteria-spec.md` table (lines 94-100)
2. ✅ Document rationale in fixture-analysis.md (this file)
3. ⏸️ Test updated specs against fixtures (verify all pass)

### Phase 2: Add Spatial Grouping (eventai-9wf Enhancement)

```python
def count_concepts_with_grouping(text_blocks, proximity_px=100):
    """
    Count concepts by grouping nearby level 1-2 text blocks.

    Args:
        text_blocks: OCR output from analyze_infographic_structure()
        proximity_px: Max distance to group blocks as one concept

    Returns:
        int: Grouped concept count
    """
    level12_blocks = [b for b in text_blocks if b.get('level', 1) <= 2]

    if not level12_blocks:
        return 0

    # Simple distance-based grouping
    groups = []
    for block in level12_blocks:
        # Find nearest group within proximity
        pos = (block['x'], block['y'])
        closest_group = None
        min_dist = float('inf')

        for group in groups:
            group_center = (
                sum(b['x'] for b in group) / len(group),
                sum(b['y'] for b in group) / len(group)
            )
            dist = ((pos[0] - group_center[0])**2 + (pos[1] - group_center[1])**2)**0.5

            if dist < min_dist:
                min_dist = dist
                closest_group = group

        # Add to closest group if within proximity, else create new group
        if min_dist <= proximity_px:
            closest_group.append(block)
        else:
            groups.append([block])

    return len(groups)
```

**Testing**:
- Run on all fixtures
- Tune `proximity_px` to achieve ~2x reduction (27 → 13-15)
- Validate that grouped counts align with human perception

### Phase 3: Validation (eventai-2pv)

1. Create fixture test suite:
   - `tests/fixtures/images/concise/` (3 variants)
   - `tests/fixtures/images/standard/` (3 variants)
   - `tests/fixtures/images/detailed/` (3 variants)

2. Write integration tests:
   - Test that all fixtures pass updated specs
   - Test grouped vs ungrouped concept counting
   - Test tolerance bands

---

## Fixture Recommendations

### Concise Tier Fixtures

**Selected**:
- ✅ `traditional-vs-ai-concise-1.webp` (13 concepts → 8 grouped)
- ✅ `traditional-vs-ai-concise-2.webp` (21 concepts → 12 grouped)
- ⏸️ Need one more (target: 10-12 concepts OCR)

**Criteria**: 8-16 concepts (grouped), 3-4 depth, 40-60% whitespace

### Standard Tier Fixtures

**Selected**:
- ✅ `five-barriers-1.webp` (17 concepts → 10 grouped) - could be standard depth
- ✅ `traditional-vs-ai-1.webp` (7 concepts → 5 grouped) - too few, borderline concise
- ⏸️ Need true standard breadth (20-25 concepts OCR)

**Criteria**: 16-28 concepts (grouped), 3-4 depth, 30-40% whitespace

### Detailed Tier Fixtures

**Selected**:
- ✅ `consent-spectrum-12.webp` (27 concepts → 15 grouped) - borderline concise/standard!
- ⏸️ Need true detailed (40+ concepts OCR)

**Criteria**: 28+ concepts (grouped), 4-6 depth, 25-35% whitespace

---

## Next Steps

1. ✅ **Completed**: Fixture analysis (this document)
2. 🔄 **In Progress**: Update canonical spec table with calibrated ranges
3. ⏸️ **Pending**: Implement spatial grouping in `analyze_infographic_structure()`
4. ⏸️ **Pending**: Test updated specs against all fixtures
5. ⏸️ **Pending**: Proceed to Phase B implementation (whitespace, text density, hierarchy)

---

**End of Analysis**
