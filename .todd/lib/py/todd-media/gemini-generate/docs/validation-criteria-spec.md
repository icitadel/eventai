# Image Validation Criteria Specification

**Status**: Draft (eventai-bex)
**Date**: 2026-01-01
**Author**: Claude (AI Assistant)
**Approach**: A→C→B (Document → Test with Fixtures → Implement)

---

## Executive Summary

This document defines **unified validation criteria** for gemini-generate that work across both prompt validation (text analysis) and image validation (OCR analysis). It resolves the current tier specification mismatch and adds missing validation dimensions (whitespace, text density).

### Key Decisions

1. **Unified Tier Specs**: Align prompt and image validation to same ranges
2. **Whitespace Measurement**: Pixel-based approach with 240 threshold
3. **Text Density**: Per-hierarchy-level word count validation
4. **OCR Tolerance**: ±2 concept variance acceptable (soft warning zone)

### Status

- ⏸️ **DRAFT**: Specifications proposed but not validated with fixtures
- 🔄 **NEXT**: Generate image fixtures (eventai-0tl) to validate these criteria
- ✅ **THEN**: Adjust specs based on real OCR results and implement (eventai-5au, 9wf, 50c)

---

## Problem Statement

### Current State Issues

1. **Tier Spec Mismatch** ([docs/ocr-capabilities.md](./ocr-capabilities.md))
   - Prompt validation: Concise = 5-16 concepts
   - Image validation: Concise = 5-8 concepts
   - **Result**: Prompts pass but images fail

2. **Incomplete Validation**
   - Whitespace: Specified (40%/30%/25%) but not measured
   - Text density: Validated in prompts (3-5 words) but not images
   - Visual hierarchy: Partially measured (clustering) but not scored

3. **No Test Data**
   - No image fixtures to validate criteria
   - No empirical data on what Gemini actually generates
   - Specs are theoretical, not grounded in reality

---

## Approach: A→C→B (Document → Fixtures → Implement)

Per user's directive, we follow this sequence:

### Phase A: Documentation ✅ (This Document)
- Define proposed criteria
- Identify validation dimensions
- Document decision rationale

### Phase C: Fixture Validation 🔄 (Next - eventai-0tl)
- Generate 3 variants per tier using ig-generate
- Analyze with OCR to measure actual metrics
- Compare to proposed specs
- **ADJUST SPECS** based on reality

### Phase B: Implementation ⏸️ (After validation)
- Implement whitespace detection (eventai-5au)
- Implement text density analysis (eventai-9wf)
- Implement hierarchy scoring (eventai-50c)
- Write tests with validated fixtures (eventai-8tw, 2pv)

**Critical**: Specs below are **DRAFT** and may change after fixture analysis.

---

## Single Source of Truth: Tier Specifications

**Architecture**: This markdown file is the ONLY place tier specs are defined.
- **CLI**: Parses this file to extract tier ranges (no hardcoded dicts)
- **Agent**: Reads this file to understand validation criteria
- **Humans**: Single doc to maintain/update

**Format**: Machine-parseable markdown tables below

### Design Principles

1. **Single canonical spec** - One source of truth for prompts, images, and evaluation
2. **Empirically calibrated** - Based on real-world prompt usage and fixture validation
3. **OCR-friendly ranges** - Account for ±2 concept variance in OCR accuracy
4. **Human-centered** - Tied to comprehension time (15s / 60s / 2min)

### Tier Specifications (CANONICAL)

<!-- SPEC_START -->
| tier | variant | concepts_min | concepts_max | depth_min | depth_max | whitespace_min | whitespace_max | text_density_max_l1l2 | comprehension_seconds | use_case |
|------|---------|--------------|--------------|-----------|-----------|----------------|----------------|----------------------|----------------------|----------|
| concise | default | 8 | 16 | 3 | 4 | 40 | 60 | 5 | 15-30 | Social media, quick glance |
| standard | breadth | 16 | 28 | 3 | 4 | 30 | 40 | 15 | 30-90 | Presentations, blog posts |
| standard | depth | 10 | 20 | 3 | 4 | 30 | 40 | 15 | 30-90 | Educational charts |
| detailed | default | 28 | 999 | 4 | 6 | 25 | 35 | 999 | 120-180 | Textbooks, analyst reports |
<!-- SPEC_END -->

**CALIBRATION NOTE** (2026-01-01): Specs updated based on fixture analysis (see [fixture-analysis.md](./fixture-analysis.md)).
- Concepts shifted up ~60% to match Gemini's OCR granularity (8-16 vs 5-12 for concise)
- Depth adjusted to 3-4 for all tiers (Gemini consistently generates 4-level hierarchies)
- Validated against 6 real infographics - see fixture analysis for details

**Field Definitions**:
- `concepts_min/max`: Number of distinct information chunks (level 1-2 text blocks)
- `depth_min/max`: Hierarchy levels (1=flat, 4+=deep)
- `whitespace_min/max`: Percentage of image area that is "empty" (threshold=240)
- `text_density_max_l1l2`: Maximum words per text block at levels 1-2 (999=unlimited)
- `comprehension_seconds`: Expected time to fully understand the infographic
- `use_case`: Typical application context

### Rationale for Changes

#### Concise: 5-12 (was 5-16 prompts / 5-8 images)
- **Why not 5-8?** Too strict - real concise prompts often have 10-12 key stats
- **Why not 5-16?** Too lenient - 16 concepts feels like "standard" tier
- **Compromise**: 5-12 captures "few to moderate" without feeling crowded
- **Human test**: Can you comprehend 12 key stats in 15-30 seconds? → Yes, if minimal labels

#### Standard Breadth: 12-20 (was 15-25 prompts / 10-15 images)
- **Why not 10-15?** Misses the "breadth" intent - only 5 more than concise
- **Why not 15-25?** Upper bound (25) overlaps with detailed tier (20+)
- **Compromise**: 12-20 provides clear separation from concise (12+) and detailed (20+)
- **Overlap**: 12 is upper bound of concise AND lower bound of standard
  - **Resolution**: Standard requires MORE than just concept count (see text density below)
  - Concise @ 12 concepts: 3-5 words per concept (36-60 words total)
  - Standard @ 12 concepts: 10-15 words per concept (120-180 words total)

#### Standard Depth: 8-15 (was 8-15 prompts / 5-8 images)
- **Why not 5-8?** Image spec was too strict, rejects valid depth-focused infographics
- **Keep 8-15**: Prompt spec is empirically validated
- **Rationale**: "Depth" variant has FEWER concepts but DEEPER explanations (3 levels)

#### Detailed: 20+ (was 25-999 prompts / 20-30 images)
- **Why 20+?** Provides clear separation from standard (12-20)
- **Why no upper bound?** Some analyst reports have 40+ concepts - shouldn't cap it
- **Practical limit**: Tesseract KMeans clustering caps at 4 levels
  - Could extend to 10 levels with better clustering algorithm
  - For now, accept 4-10 depth range (most infographics are 4-6 levels)

---

## Validation Dimensions

### 1. Structural Validation (Concept Count + Depth)

**What it measures**: Number of distinct information chunks and hierarchy levels

**Implementation**: EXISTING (`analyze_infographic_structure()`)

**Algorithm**:
1. OCR extracts text blocks with bounding boxes
2. K-Means clusters font sizes into 1-4 hierarchy levels
3. Count level 1-2 blocks as "concepts" (headlines + primary stats)
4. Depth = number of hierarchy levels

**Validation Rules**:

| Tier | Concepts | Depth | Logic |
|------|----------|-------|-------|
| Concise | 5-12 | 1-2 | Simple AND flat |
| Standard (Breadth) | 12-20 | 1-2 | More concepts, still flat |
| Standard (Depth) | 8-15 | 3 | Fewer concepts, deeper |
| Detailed | 20+ | 4-10 | Many concepts AND deep |

**Pass Criteria**:
- Concepts AND depth both within range → ✅ PASS
- Concepts OR depth outside range → Evaluate tolerance (see below)

**Tolerance Bands** (NEW):

```
Hard Pass: Exactly within range
Soft Pass (Warning): Within ±2 of range boundaries
  Example: Concise is 5-12, soft pass is 3-14
  Rationale: OCR may miscount by ±2 due to:
    - Logo text being counted as concept
    - Multi-word headline split into separate blocks
    - Footnotes/credits being included

Hard Fail: Outside ±2 tolerance
  Example: Concise with 15+ concepts → Different tier
```

### 2. Whitespace Validation (NEW)

**What it measures**: Percentage of image area that is "empty" (no content)

**Rationale**: Visual breathing room, tied to comprehension speed
- Concise: 40%+ whitespace → forces simplicity, enables quick glance
- Standard: 30%+ whitespace → balanced information density
- Detailed: 25%+ whitespace → information-rich but still readable

**Implementation**: NEW (`calculate_whitespace_percentage()` - eventai-5au)

**Algorithm (Pixel-Based)**:
```python
def calculate_whitespace_percentage(image_path, threshold=240):
    """
    Calculate percentage of "white" pixels in image.

    Args:
        image_path: Path to image file
        threshold: Grayscale value to consider "whitespace" (0-255)
                  Default 240 = light gray or white

    Returns:
        float: Percentage (0.0 to 100.0)
    """
    # Convert to grayscale
    image = Image.open(image_path).convert('L')
    pixels = np.array(image)

    # Count pixels >= threshold
    white_pixels = np.sum(pixels >= threshold)
    total_pixels = pixels.size

    return (white_pixels / total_pixels) * 100
```

**Design Decisions**:

**Q: Why threshold=240 instead of 255 (pure white)?**
A: Real infographics use light backgrounds (248, 245, etc.) that should count as whitespace

**Q: Why pixel-based instead of content-based (OCR bounding boxes)?**
A:
- Pixel-based is simpler, faster, more objective
- Content-based would miss charts, icons, graphics (only counts text)
- Can enhance later with OpenCV contour detection for non-text content

**Q: Should we measure global or per-region whitespace?**
A:
- **Phase 1 (MVP)**: Global only - simpler
- **Phase 2 (Enhancement)**: Per-quadrant analysis
  - Example: Concise should have white space in ALL quadrants, not just margins
  - Prevents "dense top, empty bottom" layout from passing

**Validation Rules**:

| Tier | Whitespace % | Tolerance | Logic |
|------|--------------|-----------|-------|
| Concise | 40-60% | ±5% soft warning | Too much white (65%+) = underutilized space |
| Standard | 30-40% | ±5% soft warning | Balanced density |
| Detailed | 25-35% | ±5% soft warning | Information-rich, not cluttered |

**Pass Criteria**:
```
Hard Pass: Within range
Soft Pass (Warning): Within ±5% of boundaries
Hard Fail: Outside ±5% tolerance

Example:
  Concise requires 40-60%
  Hard Pass: 40-60%
  Soft Pass: 35-65% (warning: "slightly too dense/sparse")
  Hard Fail: <35% or >65%
```

**Edge Cases**:

1. **Dark backgrounds**: Threshold=240 will count dark areas as content
   - **Solution**: Invert image if mean brightness < 128
   - **Detection**: `np.mean(pixels) < 128` → invert before measuring

2. **Colored backgrounds**: Convert to grayscale loses color info
   - **Solution**: Use HSV saturation to detect colored regions
   - **For MVP**: Accept limitation (most infographics use white/light gray)

3. **Gradients**: May partially count as whitespace
   - **Solution**: Use edge detection to find content boundaries
   - **For MVP**: Accept limitation (gradients are uncommon)

### 3. Text Density Validation (NEW)

**What it measures**: Words per text block at each hierarchy level

**Rationale**: Prevents verbose labels/annotations that slow comprehension
- Concise: 3-5 words per concept (headline + stat)
- Standard: 10-15 words per concept (brief description)
- Detailed: No limit (explanatory paragraphs expected)

**Implementation**: NEW (`validate_image_text_density()` - eventai-9wf)

**Algorithm**:
```python
def validate_image_text_density(image_path, tier):
    """
    Validate word counts per hierarchy level.

    Args:
        image_path: Path to image
        tier: 'concise', 'standard', or 'detailed'

    Returns:
        dict with validation results and violations
    """
    # Get OCR results with text blocks
    metrics = analyze_infographic_structure(image_path)

    violations = []

    # Per-level word count validation
    for block in metrics['text_blocks']:
        text = block['text']
        level = block.get('level', 1)
        word_count = len(text.split())

        # Apply tier-specific rules
        if tier == 'concise':
            # Level 1-2: 1-5 words each (headlines/stats)
            if level <= 2 and word_count > 5:
                violations.append({
                    'level': level,
                    'text': text[:50],
                    'word_count': word_count,
                    'limit': 5,
                    'message': f'Level {level} text too long: {word_count} words (max 5)'
                })

        elif tier == 'standard':
            # Level 1-2: 1-15 words (can have brief descriptions)
            if level <= 2 and word_count > 15:
                violations.append({
                    'level': level,
                    'text': text[:50],
                    'word_count': word_count,
                    'limit': 15,
                    'message': f'Level {level} text too long: {word_count} words (max 15)'
                })

        # Detailed: No limits

    return {
        'valid': len(violations) == 0,
        'tier': tier,
        'violations': violations,
        'metrics': metrics
    }
```

**Design Decisions**:

**Q: Why per-block instead of per-concept?**
A: OCR doesn't reliably group related blocks into concepts
- **Phase 1 (MVP)**: Validate per-block (simpler)
- **Phase 2**: Spatial clustering to group related blocks

**Q: What about multi-line text blocks?**
A: OCR may return entire paragraph as one block
- **Handling**: Count total words, flag if >15 for standard, >5 for concise
- **Assumption**: Multi-line = multi-sentence = too verbose for concise/standard

**Validation Rules**:

| Tier | Level 1-2 Word Limit | Level 3-4 Word Limit | Rationale |
|------|---------------------|---------------------|-----------|
| Concise | 1-5 words | N/A (1-2 levels only) | Headlines + stats only |
| Standard | 1-15 words | 5-30 words | Brief labels + descriptions |
| Detailed | No limit | No limit | Explanatory text expected |

**Pass Criteria**:
```
Concise:
  ✅ All level 1-2 blocks have ≤5 words
  ⚠️ 1-2 blocks have 6-8 words (soft warning)
  ❌ 3+ blocks have >8 words (hard fail)

Standard:
  ✅ All level 1-2 blocks have ≤15 words
  ⚠️ 1-2 blocks have 16-20 words (soft warning)
  ❌ 3+ blocks have >20 words (hard fail)

Detailed:
  ✅ Always passes (no word limits)
  ⚠️ Warn if NO blocks have >20 words (may be too sparse for "detailed")
```

### 4. Visual Hierarchy Scoring (NEW)

**What it measures**: Quality of visual hierarchy (font size separation)

**Rationale**: Clear hierarchy aids comprehension
- Good hierarchy: Distinct font sizes (title >> subtitle >> body)
- Poor hierarchy: All same size or too many levels

**Implementation**: NEW (`score_visual_hierarchy()` - eventai-50c)

**Algorithm**:
```python
def score_visual_hierarchy(image_path):
    """
    Score visual hierarchy quality based on font size distribution.

    Returns:
        dict with hierarchy score (0.0 to 1.0) and analysis
    """
    metrics = analyze_infographic_structure(image_path)

    if metrics.get('error'):
        return {'score': 0.0, 'error': metrics['error']}

    text_blocks = metrics['text_blocks']
    n_clusters = metrics['n_clusters']

    # Extract font sizes
    sizes = [b['size'] for b in text_blocks]

    # Calculate size ratios between levels
    # Good hierarchy: Level 1 >> Level 2 >> Level 3
    # Poor hierarchy: All levels similar size

    level_sizes = {}
    for block in text_blocks:
        level = block.get('level', 1)
        if level not in level_sizes:
            level_sizes[level] = []
        level_sizes[level].append(block['size'])

    # Calculate mean size per level
    level_means = {
        level: np.mean(sizes)
        for level, sizes in level_sizes.items()
    }

    # Calculate separation ratios
    ratios = []
    sorted_levels = sorted(level_means.keys())
    for i in range(len(sorted_levels) - 1):
        level_a = sorted_levels[i]
        level_b = sorted_levels[i + 1]
        ratio = level_means[level_a] / level_means[level_b]
        ratios.append(ratio)

    # Score based on separation
    # Good: Ratios ~1.5-2.5 (clear separation)
    # Poor: Ratios ~1.0-1.2 (barely distinguishable)
    # Excessive: Ratios >3.0 (level 1 dominates)

    avg_ratio = np.mean(ratios) if ratios else 1.0

    if avg_ratio >= 1.5 and avg_ratio <= 2.5:
        score = 1.0  # Excellent
    elif avg_ratio >= 1.3 and avg_ratio <= 3.0:
        score = 0.7  # Good
    elif avg_ratio >= 1.1:
        score = 0.4  # Fair
    else:
        score = 0.1  # Poor (flat hierarchy)

    return {
        'score': score,
        'avg_ratio': avg_ratio,
        'n_levels': n_clusters,
        'level_means': level_means,
        'ratios': ratios,
        'assessment': (
            'Excellent' if score >= 0.9 else
            'Good' if score >= 0.7 else
            'Fair' if score >= 0.4 else
            'Poor'
        )
    }
```

**Design Decisions**:

**Q: Why ratio-based instead of absolute size differences?**
A: Ratios are resolution-independent
- 48px vs 24px (ratio 2.0) on 1080p image
- 96px vs 48px (ratio 2.0) on 4K image
- Same hierarchy quality, different absolute sizes

**Q: What's the ideal ratio?**
A: Typography best practices suggest 1.5-2.0 (golden ratio ~1.618)
- Too small (<1.3): Levels not distinguishable
- Too large (>3.0): Top level dominates, others invisible

**Validation Rules**:

| Score Range | Assessment | Tier Requirement |
|-------------|------------|------------------|
| 0.9-1.0 | Excellent | ✅ All tiers |
| 0.7-0.8 | Good | ✅ All tiers |
| 0.4-0.6 | Fair | ⚠️ Warning for concise (needs clarity) |
| 0.0-0.3 | Poor | ❌ Fail all tiers (unreadable) |

**Pass Criteria**:
```
All tiers:
  ✅ Score ≥ 0.7 (good hierarchy)
  ⚠️ Score 0.4-0.6 (fair, usable but suboptimal)
  ❌ Score < 0.4 (poor, difficult to read)

Concise tier (strict):
  ✅ Score ≥ 0.7 (needs crystal-clear hierarchy for quick glance)
  ❌ Score < 0.7 (fail)
```

---

## Composite Validation Logic

### How Dimensions Combine

Each infographic is evaluated on **4 dimensions**:
1. Structural (concepts + depth) - REQUIRED
2. Whitespace - REQUIRED
3. Text Density - REQUIRED
4. Visual Hierarchy - ADVISORY (warning only)

**Overall Pass Criteria**:

```python
def validate_image_comprehensive(image_path, tier):
    """
    Comprehensive validation across all dimensions.

    Returns:
        {
            'valid': bool,  # True if ALL required dimensions pass
            'tier': str,
            'dimensions': {
                'structural': {...},
                'whitespace': {...},
                'text_density': {...},
                'hierarchy': {...}
            },
            'warnings': [...],  # Soft failures
            'failures': [...]   # Hard failures
        }
    """
    results = {
        'tier': tier,
        'warnings': [],
        'failures': []
    }

    # 1. Structural validation
    structural = validate_image_against_tier(image_path, tier)
    results['dimensions']['structural'] = structural
    if not structural['valid']:
        results['failures'].append('Structural: Concepts or depth out of range')

    # 2. Whitespace validation
    whitespace = calculate_whitespace_percentage(image_path)
    whitespace_valid, whitespace_msg = check_whitespace_tier(whitespace, tier)
    results['dimensions']['whitespace'] = {
        'percentage': whitespace,
        'valid': whitespace_valid,
        'message': whitespace_msg
    }
    if not whitespace_valid:
        if 'warning' in whitespace_msg.lower():
            results['warnings'].append(f'Whitespace: {whitespace_msg}')
        else:
            results['failures'].append(f'Whitespace: {whitespace_msg}')

    # 3. Text density validation
    text_density = validate_image_text_density(image_path, tier)
    results['dimensions']['text_density'] = text_density
    if not text_density['valid']:
        if len(text_density['violations']) <= 2:
            results['warnings'].append(f'Text Density: {len(text_density["violations"])} blocks too verbose')
        else:
            results['failures'].append(f'Text Density: {len(text_density["violations"])} blocks too verbose')

    # 4. Visual hierarchy scoring (advisory only)
    hierarchy = score_visual_hierarchy(image_path)
    results['dimensions']['hierarchy'] = hierarchy
    if hierarchy['score'] < 0.4:
        results['warnings'].append(f'Hierarchy: Poor visual separation (score {hierarchy["score"]:.2f})')
    elif tier == 'concise' and hierarchy['score'] < 0.7:
        results['warnings'].append(f'Hierarchy: Fair separation (score {hierarchy["score"]:.2f}), prefer ≥0.7 for concise tier')

    # Overall validation
    results['valid'] = len(results['failures']) == 0

    return results
```

**Example Results**:

```json
{
  "valid": true,
  "tier": "concise",
  "dimensions": {
    "structural": {
      "concepts": 8,
      "depth": 2,
      "valid": true
    },
    "whitespace": {
      "percentage": 42.3,
      "valid": true,
      "message": "✅ Within range (40-60%)"
    },
    "text_density": {
      "valid": true,
      "violations": []
    },
    "hierarchy": {
      "score": 0.85,
      "assessment": "Good",
      "avg_ratio": 1.92
    }
  },
  "warnings": [],
  "failures": []
}
```

---

## Implementation Plan

### Phase 1: MVP (Required Validation)

**Implement (eventai-5au, 9wf, 50c)**:
1. ✅ `calculate_whitespace_percentage()` - Pixel-based, threshold=240
2. ✅ `validate_image_text_density()` - Per-block word counting
3. ✅ `score_visual_hierarchy()` - Font size ratio analysis
4. ✅ `validate_image_comprehensive()` - Composite validation

**Test (eventai-8tw, 2pv)**:
1. Unit tests for each function
2. Integration tests with image fixtures

**Integrate (eventai-ddb, g61)**:
1. Call from ig-evaluate command
2. Call from ig-generate workflow

### Phase 2: Enhancements (Optional - P3)

**Advanced Whitespace (eventai-r09)**:
- Per-quadrant analysis (detect unbalanced layouts)
- Content-based (OCR bounding boxes + OpenCV contours)
- Background color detection (HSV analysis)

**Advanced Text Density**:
- Spatial clustering to group related blocks into concepts
- Per-concept word counting (more accurate)
- Sentence structure detection (multi-sentence paragraphs)

**Advanced Hierarchy**:
- Typography analysis (bold, italic, font family)
- Color-based hierarchy (size + color combined)
- Spatial hierarchy (top-to-bottom, left-to-right flow)

**Accessibility (eventai-7jz)**:
- Contrast ratio calculation (WCAG compliance)
- Color-blind simulation
- Font size legibility (minimum 12pt equivalent at 1080p)

---

## Validation Workflow

### ig-generate Integration

```bash
# Current workflow
ig-generate --density=concise --output-dir=./output

# After integration
ig-generate --density=concise --output-dir=./output --validate

# Output:
# ✅ Generated variant #1 - VALID (all dimensions pass)
# ⚠️  Generated variant #2 - VALID with warnings (whitespace: 38%, expected 40%+)
# ❌ Generated variant #3 - INVALID (concepts: 15, expected 5-12 for concise)
```

### ig-evaluate Integration

```bash
# Current workflow
ig-evaluate variant-1.webp variant-2.webp variant-3.webp

# After integration (automatic validation included)
ig-evaluate variant-1.webp variant-2.webp variant-3.webp --density=concise

# Output:
# Variant 1:
#   Structural: ✅ 8 concepts, 2 depth
#   Whitespace: ✅ 42.3%
#   Text Density: ✅ All blocks ≤5 words
#   Hierarchy: ✅ Score 0.85 (Good)
#   Overall: ✅ VALID
#
# Variant 2:
#   Structural: ✅ 7 concepts, 2 depth
#   Whitespace: ⚠️ 38% (expected 40%+, within tolerance)
#   Text Density: ✅ All blocks ≤5 words
#   Hierarchy: ✅ Score 0.78 (Good)
#   Overall: ✅ VALID with warnings
#
# Variant 3:
#   Structural: ❌ 15 concepts (expected 5-12)
#   Whitespace: ✅ 45%
#   Text Density: ❌ 4 blocks with >5 words
#   Hierarchy: ⚠️ Score 0.62 (Fair)
#   Overall: ❌ INVALID
#
# Recommendation: Use Variant 1
```

---

## Open Questions / Decisions Needed

### 1. Tier Spec Validation via Fixtures (Phase C)

**CRITICAL**: These specs are PROPOSED and must be validated with real fixtures.

**Process** (eventai-0tl):
1. Generate 3 variants per tier using ig-generate
2. Run OCR analysis on each
3. Document actual concept counts, whitespace %, text density
4. Compare to proposed specs
5. **Adjust specs** if reality differs from theory

**Questions to answer**:
- Do Gemini-generated concise infographics actually have 5-12 concepts?
- Or do they tend toward 8-15 (more than we expect)?
- What about whitespace - does Gemini achieve 40%+ for concise?
- Are the word counts realistic (3-5 for concise)?

**Adjustment Triggers**:
- If 80%+ of concise variants have 12-15 concepts → Raise upper bound to 15
- If whitespace is consistently 35-40% (not 40-60%) → Lower requirement to 35%+
- If text density violations are common → Relax word limits

### 2. OCR Tolerance Bands

**Current Proposal**: ±2 concept variance acceptable

**Questions**:
- Is ±2 too lenient? (Concise 5-12 becomes 3-14)
- Should tolerance be percentage-based? (±20% of range)
- Should tolerance differ by tier? (Concise strict, detailed lenient)

**Testing via Fixtures**:
- Generate same prompt 5 times
- Measure OCR variance across identical images
- Calculate standard deviation → inform tolerance

### 3. Whitespace Threshold

**Current Proposal**: threshold=240 (light gray or white)

**Questions**:
- Should we lower to 230 to catch slightly darker backgrounds?
- Should we auto-detect threshold based on image histogram?
- Should we invert dark-background images?

**Testing via Fixtures**:
- Analyze fixture backgrounds (what colors do they use?)
- Test threshold values 230, 240, 250
- Measure impact on whitespace percentage

### 4. Hierarchy Score Passing Threshold

**Current Proposal**:
- ≥0.7 = Pass for all tiers
- ≥0.4 = Soft warning
- <0.4 = Fail

**Questions**:
- Should concise tier require higher score (≥0.8) for clarity?
- Should detailed tier accept lower score (≥0.6) due to complexity?
- Should this be advisory-only (warning) or hard requirement?

**Testing via Fixtures**:
- Calculate hierarchy scores for all fixtures
- Correlate with human perception (does 0.7 feel "clear"?)
- Adjust thresholds based on real data

---

## CLI Parser Implementation

The Python CLI should parse the canonical spec table (lines 94-100) using this approach:

```python
def load_tier_specs_from_markdown(spec_file='docs/validation-criteria-spec.md'):
    """
    Parse tier specs from canonical markdown file.

    Returns: dict with tier specs
    """
    import re

    with open(spec_file, 'r') as f:
        content = f.read()

    # Extract table between SPEC_START and SPEC_END markers
    match = re.search(r'<!-- SPEC_START -->(.+?)<!-- SPEC_END -->', content, re.DOTALL)
    if not match:
        raise ValueError("Spec table not found in markdown")

    table_text = match.group(1)

    # Parse markdown table (skip header and separator rows)
    rows = [line.strip() for line in table_text.split('\n') if line.strip() and '|' in line]
    rows = [r for r in rows if not r.startswith('|---')]  # Skip separator
    header = [cell.strip() for cell in rows[0].split('|')[1:-1]]  # Remove first/last empty cells

    specs = {}
    for row in rows[1:]:  # Skip header
        cells = [cell.strip() for cell in row.split('|')[1:-1]]
        row_dict = dict(zip(header, cells))

        tier = row_dict['tier']
        variant = row_dict['variant']

        # Build spec dict
        spec_key = tier if variant == 'default' else f"{tier}_{variant}"
        specs[spec_key] = {
            'concepts': (int(row_dict['concepts_min']), int(row_dict['concepts_max'])),
            'depth': (int(row_dict['depth_min']), int(row_dict['depth_max'])),
            'whitespace': (int(row_dict['whitespace_min']), int(row_dict['whitespace_max'])),
            'text_density_max': int(row_dict['text_density_max_l1l2']),
            'comprehension_seconds': row_dict['comprehension_seconds'],
            'use_case': row_dict['use_case']
        }

    return specs

# Usage in gemini_generate.py - REPLACE all hardcoded tier_specs dicts
tier_specs = load_tier_specs_from_markdown()

# Result:
# {
#     'concise': {
#         'concepts': (5, 12),
#         'depth': (1, 2),
#         'whitespace': (40, 60),
#         'text_density_max': 5,
#         ...
#     },
#     'standard_breadth': {...},
#     'standard_depth': {...},
#     'detailed': {...}
# }
```

**Benefits**:
- ✅ No hardcoded tier specs in Python (lines 754-775, 932-953 will be removed)
- ✅ Single source of truth (this markdown file)
- ✅ Agent can read same spec during evaluation
- ✅ Easy to update (just edit markdown table)
- ✅ Version controlled (git tracks changes to specs)

---

## Summary

### Canonical Tier Specs

**See lines 94-100 for the machine-parseable canonical table.**

Quick reference (CALIBRATED 2026-01-01):
- **Concise**: 8-16 concepts, 3-4 depth, 40-60% whitespace, ≤5 words/block
- **Standard (Breadth)**: 16-28 concepts, 3-4 depth, 30-40% whitespace, ≤15 words/block
- **Standard (Depth)**: 10-20 concepts, 3-4 depth, 30-40% whitespace, ≤15 words/block
- **Detailed**: 28+ concepts, 4-6 depth, 25-35% whitespace, unlimited words

**Additional Validation**:
- Visual Hierarchy: Score ≥0.7 (all tiers)
- Tolerance Bands: ±2 concepts, ±5% whitespace (soft warnings)

### Key Changes from Current Implementation

1. **Single Source of Truth**: One markdown spec (this file) replaces hardcoded Python dicts
2. **Unified Ranges**: Same specs for prompts, images, and agent evaluation
3. **Added Whitespace**: Measurable requirement (was specified but not measured)
4. **Added Text Density**: Per-block word counting (was only validated in prompts)
5. **Added Hierarchy**: Quality score for visual separation (font size ratios)
6. **Added Tolerance**: ±2 concepts, ±5% whitespace (soft warnings vs hard failures)

### Next Steps (Per A→C→B Plan)

1. ✅ **Phase A: Document** (this document - eventai-bex)
2. 🔄 **Phase C: Validate** (eventai-0tl - generate fixtures, measure actual metrics)
3. ⏸️ **Phase B: Implement** (eventai-5au, 9wf, 50c - code the validation functions)

**CRITICAL**: Do NOT implement Phase B until Phase C validates these specs!

---

**End of Specification**
