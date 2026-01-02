# OCR Capabilities and Image Validation - Technical Documentation

**Status**: Draft (eventai-tn5)
**Date**: 2026-01-01
**Author**: Claude (AI Assistant)

---

## Overview

This document provides a comprehensive technical analysis of the existing OCR-based image validation infrastructure in gemini-generate. The system is **implemented but dormant** - the code exists, but is not tested, integrated into workflows, or consistently aligned with prompt validation logic.

## Current Implementation

### 1. Core OCR Function: `analyze_infographic_structure()`

**Location**: `gemini_generate.py`, lines 814-906

**Purpose**: Extract text, positions, and hierarchy levels from infographic images using Tesseract OCR.

**Algorithm**:

```
1. Load image via PIL
2. Run Tesseract OCR with bounding box output
3. Filter text blocks (skip single characters, require len > 2)
4. Extract features: text, position (x,y), dimensions (width, height)
5. Cluster font sizes using K-Means (max 4 clusters)
6. Assign hierarchy levels (1 = largest fonts, 4 = smallest)
7. Count concepts (text blocks at levels 1-2)
8. Calculate depth (number of clusters = hierarchy levels)
```

**Dependencies**:
- `PIL` (Pillow) - Image loading
- `pytesseract` - OCR interface to Tesseract
- `scikit-learn` (KMeans) - Font size clustering
- `numpy` - Array operations
- System: `tesseract-ocr` binary (brew/apt-get)

**Return Value**:
```python
{
    'concepts': int,        # Count of level 1-2 text blocks
    'depth': int,           # Number of hierarchy levels (1-4)
    'complexity': int,      # concepts × depth
    'text_blocks': [...],   # List of text blocks with positions, sizes, levels
    'n_clusters': int,      # Number of font size clusters detected
    'error': str (optional) # Error message if OCR fails
}
```

**Strengths**:
- ✅ Objective, deterministic analysis (no AI inference needed)
- ✅ Fast execution (< 2 seconds for typical infographic)
- ✅ Extracts both content (text) and structure (hierarchy)
- ✅ Works with any image format supported by PIL (PNG, WebP, JPEG)
- ✅ Graceful error handling (missing dependencies, no text detected)

**Limitations**:
- ❌ **Font size clustering is simplistic** - Uses height of bounding box as proxy for font size
  - Doesn't account for actual font weight, boldness, or styling
  - May incorrectly group headlines with large body text
  - No handling of decorative fonts or logos

- ❌ **No whitespace detection** - Cannot measure the "40% whitespace" requirement for concise tier

- ❌ **No text density analysis** - Cannot validate "3-5 words max" per concept
  - Extracts individual words/phrases, not logical groupings
  - Cannot detect if a headline + stat are one "concept" vs separate

- ❌ **OCR accuracy issues** - Tesseract may fail on:
  - Stylized fonts, handwriting, logos
  - Text on complex backgrounds
  - Rotated or curved text
  - Very small or very large text

- ❌ **No semantic understanding** - Cannot distinguish:
  - Chart labels vs. explanatory annotations
  - Title vs. subtitle vs. data labels
  - Legend text vs. main content

### 2. Validation Function: `validate_image_against_tier()`

**Location**: `gemini_generate.py`, lines 908-988

**Purpose**: Analyze an image and determine if it matches the expected density tier.

**Algorithm**:

```
1. Call analyze_infographic_structure() to get metrics
2. Load tier specifications (concise, standard, detailed)
3. Compare metrics against tier ranges:
   - concepts: within (min, max) range
   - depth: within (min, max) range
4. For 'standard' tier: check BOTH breadth and depth variants
5. Return validation result with metrics and expected ranges
```

**Tier Specifications** (Image Validation):

| Tier | Concepts | Depth | Description |
|------|----------|-------|-------------|
| **Concise** | 5-8 | 1-2 | Few concepts, shallow hierarchy |
| **Standard (Breadth)** | 10-15 | 1-2 | Many concepts, shallow hierarchy |
| **Standard (Depth)** | 5-8 | 3 | Few concepts, medium hierarchy |
| **Detailed** | 20-30 | 4-10 | Many concepts, deep hierarchy |

**Return Value**:
```python
{
    'valid': bool,          # True if image matches tier
    'tier': str,            # Expected tier ('concise', 'standard', 'detailed')
    'variant': str,         # 'breadth', 'depth', or None
    'metrics': {...},       # OCR analysis results
    'expected': {...},      # Expected tier specification
    'image_path': str,      # Path to analyzed image
    'error': str (optional) # Error message if OCR fails
}
```

**Strengths**:
- ✅ Same validation logic as prompts (structure-based)
- ✅ Handles 'standard' tier variants (breadth vs. depth)
- ✅ Returns detailed metrics for debugging
- ✅ Clear pass/fail determination

**Limitations**:
- ❌ **Not aligned with prompt validation** - Different tier ranges (see Critical Issue below)
- ❌ **No text pattern validation** - Image validation doesn't check word counts like prompt validation does
- ❌ **No whitespace validation** - Specs mention 40%/30%/25% but not measured
- ❌ **Not tested** - No unit tests or integration tests
- ❌ **Not integrated** - Not called from ig-evaluate or ig-generate commands

---

## Critical Issue: Tier Specification Mismatch

### The Problem

The codebase has **TWO DIFFERENT** tier specifications that are not aligned:

#### Prompt Validation Specs (lines 754-775)

| Tier | Concepts | Depth | Rationale |
|------|----------|-------|-----------|
| **Concise** | 5-16 | 1-2 | "Few to moderate concepts" - lenient upper bound |
| **Standard (Breadth)** | 15-25 | 1-2 | "Many concepts at shallow depth" |
| **Standard (Depth)** | 8-15 | 3 | "Moderate concepts at medium depth" |
| **Detailed** | 25-999 | 4-10 | "Many concepts AND deep detail" - no upper limit |

#### Image Validation Specs (lines 932-953)

| Tier | Concepts | Depth | Rationale |
|------|----------|-------|-----------|
| **Concise** | 5-8 | 1-2 | "Few concepts" - strict upper bound |
| **Standard (Breadth)** | 10-15 | 1-2 | "Many concepts at shallow depth" |
| **Standard (Depth)** | 5-8 | 3 | "Few concepts at medium depth" |
| **Detailed** | 20-30 | 4-10 | "Many concepts AND deep detail" - capped at 30 |

### The Impact

**Scenario 1: Concise tier mismatch**
- Prompt with 12 concepts → ✅ **PASSES** prompt validation (5-16 range)
- Generated image with 12 concepts → ❌ **FAILS** image validation (5-8 range)
- **Result**: User generates valid prompt, but Gemini produces "invalid" image

**Scenario 2: Detailed tier mismatch**
- Prompt with 35 concepts → ✅ **PASSES** prompt validation (25-999 range)
- Generated image with 35 concepts → ❌ **FAILS** image validation (20-30 range)
- **Result**: Unnecessarily strict image validation rejects valid infographics

### Root Cause Analysis

Looking at the commit history and comments:

1. **Prompt specs were calibrated** (lines 753-775) - "adjusted based on real-world prompts"
   - Comment states: "Tier expectations (adjusted based on real-world prompts)"
   - Suggests empirical tuning based on actual usage

2. **Image specs were NOT calibrated** (lines 932-953) - "Use same tier specs as prompts" (line 931)
   - Comment claims alignment but specs are different
   - Likely copied from an earlier version before prompt calibration
   - Never updated to match the refined prompt specs

### Recommendation

**Option A**: Align image specs to match prompt specs (more lenient)
- Allows more variety in generated images
- Risk: May accept images that feel "too dense" for their tier

**Option B**: Align prompt specs to match image specs (stricter)
- Ensures prompts don't promise more than images deliver
- Risk: May reject valid prompts that could produce good infographics

**Option C**: Calibrate both based on real image fixtures (data-driven)
- Generate representative images for each tier
- Measure actual concept counts via OCR
- Adjust both specs to match reality
- **RECOMMENDED**: This is the A→C→B approach the user requested

---

## Text Pattern Validation (Prompt-Only)

**Location**: `gemini_generate.py`, lines 655-731

**Purpose**: Validate that prompt text follows tier-specific density rules.

**Key Rules**:

| Tier | Word Limit | Multi-Sentence | Notes |
|------|------------|----------------|-------|
| **Concise** | 3-5 words max | ❌ Forbidden | Single labels only, no drilldowns |
| **Standard** | 10-15 words max | ⚠️ Max 1 sentence | Brief descriptions allowed |
| **Detailed** | No limit | ✅ Expected | Multi-level nested bullets required |

**Algorithm**:

```
1. Extract content bullets from prompt (ignore Style/Structure sections)
2. Remove bold markers (**text**) for word counting
3. For each bullet:
   - Count words (split on whitespace)
   - Check for multi-sentence patterns (". " in middle)
   - Check for drilldown patterns ("topic - detail")
4. Return list of validation issues (empty = valid)
```

**Strengths**:
- ✅ Enforces text density at prompt creation time
- ✅ Catches over-verbose prompts before generation
- ✅ Tier-specific rules (concise is strictest)

**Gaps in Image Validation**:
- ❌ **No equivalent for images** - OCR extracts text but doesn't validate word counts
- ❌ **Cannot detect drilldown patterns** - OCR sees individual text blocks, not logical groupings
- ❌ **Cannot validate sentence structure** - OCR may split sentences incorrectly

**Extension Opportunity**:
Could add `validate_image_text_patterns()` function to:
1. Extract text from text_blocks
2. Count words per concept (group level 1-2 blocks)
3. Validate word counts against tier limits
4. Check for paragraph-length text (multi-line blocks at same level)

---

## Whitespace Requirements (Not Implemented)

### Specified in Density Instructions

**Location**: `gemini_generate.py`, lines 84-130

| Tier | Whitespace Requirement |
|------|------------------------|
| **Concise** | 40%+ mandatory (line 89) |
| **Standard** | 30% target (line 113) |
| **Detailed** | 25%+ acceptable (line 124) |

### Current Status

- ✅ **Documented in prompts** - Gemini receives whitespace instructions
- ❌ **Not measured** - No code to calculate whitespace percentage
- ❌ **Not validated** - Cannot verify if generated image meets requirement

### Implementation Strategy

Two approaches:

**Approach 1: Pixel-Based (Simple)**
```python
def calculate_whitespace_percentage(image_path, white_threshold=240):
    """
    Calculate percentage of image that is "white" (light-colored).

    Args:
        image_path: Path to image file
        white_threshold: Grayscale value to consider "white" (0-255)

    Returns:
        float: Percentage of white pixels (0.0 to 100.0)
    """
    image = Image.open(image_path).convert('L')  # Grayscale
    pixels = np.array(image)
    white_pixels = np.sum(pixels >= white_threshold)
    total_pixels = pixels.size
    return (white_pixels / total_pixels) * 100
```

**Pros**: Fast, simple, objective
**Cons**:
- May count light backgrounds as "whitespace"
- Doesn't distinguish margins from interior spacing
- Sensitive to threshold value

**Approach 2: Content-Based (Advanced)**
```python
def calculate_whitespace_percentage_advanced(image_path):
    """
    Calculate whitespace as percentage NOT occupied by text/graphics.

    Uses OCR bounding boxes to define content regions.
    Everything else is whitespace.
    """
    # Get text bounding boxes from OCR
    metrics = analyze_infographic_structure(image_path)

    # Calculate total area occupied by text
    content_area = sum(b['width'] * b['height'] for b in metrics['text_blocks'])

    # Get image dimensions
    image = Image.open(image_path)
    total_area = image.width * image.height

    # Whitespace = total - content
    whitespace_percentage = ((total_area - content_area) / total_area) * 100
    return whitespace_percentage
```

**Pros**:
- More accurate - only counts actual content
- Can detect margins, gutters, breathing room
- Could extend to detect charts/graphics (not just text)

**Cons**:
- More complex
- Misses non-text content (charts, icons, images)
- Requires accurate OCR bounding boxes

**Recommendation**: Start with Approach 1 for MVP, enhance with Approach 2 later.

---

## Integration Status

### Command Integration

| Command | Current Status | Integration Needed |
|---------|----------------|-------------------|
| **ig-generate** | ❌ Not integrated | Run `validate_image_against_tier()` after download/conversion |
| **ig-evaluate** | ❌ Not integrated | Include OCR metrics in evaluation report |
| **gemini-generate CLI** | ⚠️ Partial | Has `--validate-image` flag but not used in workflows |

### Test Coverage

**From TESTING.md** (lines 195-210):

```
✅ Covered (23 tests):
- Structural Analysis (concept counting, depth detection)
- Validation Logic (tier acceptance/rejection)
- CLI Interface (argument parsing, output)
- Edge cases and real-world prompts

⏸️ NOT Yet Covered (0 tests):
- Image Validation: OCR-based analysis
  - Requires: Tesseract, pytesseract, sklearn
  - Missing: Test fixtures (images for each tier)
  - Missing: Unit tests for analyze_infographic_structure()
  - Missing: Integration tests for validate_image_against_tier()
```

**Gap Analysis**:
- No tests for OCR functions → Cannot refactor safely
- No image fixtures → Cannot validate tier specs
- No integration tests → Cannot ensure end-to-end workflow works

---

## Extension Points

### 1. Enhanced Text Extraction

**Current**: Extracts individual words/phrases
**Needed**: Group related text into "concepts"

**Strategy**:
- Use spatial clustering (DBSCAN) to group nearby text blocks
- Combine level 1 (headline) + level 2 (stat) if close together
- More accurate concept counting

### 2. Whitespace Detection

**Current**: Not implemented
**Needed**: Measure 40%/30%/25% requirements

**Strategy**: Implement pixel-based approach (see section above)

### 3. Text Density Validation

**Current**: Word counts validated in prompts only
**Needed**: Validate in images too

**Strategy**:
- Extract full text from each concept cluster
- Count words per concept
- Validate against tier limits (3-5 for concise, etc.)

### 4. Visual Element Detection

**Current**: Text-only
**Needed**: Detect charts, icons, graphics

**Strategy**:
- Use image segmentation (OpenCV contours)
- Detect non-text regions (charts, arrows, icons)
- Include in complexity calculation

### 5. Cloud Vision APIs

**Current**: Tesseract OCR (local)
**Alternative**: Google Cloud Vision, AWS Textract, Azure Vision

**Pros**:
- Better accuracy on stylized fonts
- Can detect tables, charts, diagrams
- Built-in text grouping/structure detection

**Cons**:
- Requires API key (cost, quota limits)
- Slower (network latency)
- Privacy concerns (upload to cloud)

---

## Recommendations for eventai-bex (Criteria Definition)

Based on this analysis, the criteria definition task should:

### 1. Resolve Tier Spec Mismatch

**Action**: Run A→C→B approach
1. Generate representative images for each tier (using ig-generate)
2. Analyze with OCR to measure actual concept counts
3. Define unified tier specs that work for BOTH prompts and images

**Suggested Process**:
```bash
# Generate 3 variants per tier
bd update eventai-0tl --status=in_progress
ig-generate --density=concise --batch=3
ig-generate --density=standard --batch=3
ig-generate --density=detailed --batch=3

# Analyze each variant
for file in output/*.webp; do
    gemini-generate --validate-image "$file" --density=<tier>
done

# Document actual concept counts → update tier specs
```

### 2. Define Whitespace Requirements Precisely

**Current**: "40%+ mandatory" is vague
**Needed**: Measurable criteria

**Questions to answer**:
- What counts as "whitespace"? (threshold value?)
- Margins only, or interior spacing too?
- Does background color matter? (light blue vs white?)
- Should we measure global whitespace or per-region?

**Suggested Spec**:
```
Concise:
- Global whitespace: 40-60% (pixel-based, threshold=240)
- No region should be <20% whitespace (breathing room everywhere)

Standard:
- Global whitespace: 30-40%
- Acceptable to have dense regions if balanced by white margins

Detailed:
- Global whitespace: 25-35%
- Information-dense, but still readable
```

### 3. Define Text Density Validation for Images

**Current**: Word limits for prompts (3-5, 10-15 words)
**Needed**: Equivalent for images

**Challenge**: OCR may split concepts incorrectly

**Suggested Approach**:
- Measure words per **text block**, not per concept
- Define acceptable ranges per hierarchy level:
  - Level 1 (headlines): 1-5 words
  - Level 2 (stats): 1-8 words
  - Level 3 (labels): 3-15 words
  - Level 4 (annotations): 10+ words

### 4. Define Acceptable OCR Variance

**Current**: Exact ranges (5-8 concepts)
**Reality**: OCR may miscount by ±1-2

**Suggested**:
- Add tolerance bands (e.g., 5-8 ±1 = 4-9 acceptable)
- Or use "soft" vs "hard" failures:
  - Soft: Within ±1 → Warning but still valid
  - Hard: Outside ±2 → Invalid

---

## Summary

### Current State
- ✅ **OCR infrastructure exists** - Tesseract-based analysis implemented
- ✅ **Validation logic exists** - Tier comparison implemented
- ❌ **Not tested** - No test suite
- ❌ **Not integrated** - Not called from workflows
- ❌ **Not aligned** - Prompt and image specs differ
- ❌ **Incomplete** - Missing whitespace, text density validation

### Next Steps (Per User's A→C→B Plan)
1. ✅ **Document OCR capabilities** (this document - eventai-tn5)
2. 🔄 **Define validation criteria** (eventai-bex - resolve spec mismatches)
3. 🔄 **Create image fixtures** (eventai-0tl - generate and analyze)
4. 🔄 **Implement enhancements** (eventai-5au, 9wf, 50c - whitespace, density, hierarchy)

### Key Decisions Needed (eventai-bex)
- [ ] Unify tier specs: Which ranges to use?
- [ ] Whitespace measurement: Pixel-based or content-based?
- [ ] Text density: Per-block or per-concept validation?
- [ ] OCR tolerance: How much variance is acceptable?

---

**End of Document**