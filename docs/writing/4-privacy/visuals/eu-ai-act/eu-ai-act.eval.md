# EU AI Act Pyramid - Variant Evaluation

**Date:** 2026-01-02
**Prompt Tier:** Concise
**Total Variants:** 12 (3 portrait, 9 landscape)

## Executive Summary

Generated 12 variants across two orientations. Only **5 of 12 variants** achieve concept counts within the valid 8-16 range for concise tier compliance. Portrait variants #1 and #2 demonstrate the preferred visual style with rounded-corner boxes, two-tone design, and icon-heavy layouts. Landscape variant #10 successfully adapts this style to horizontal format.

## Concise Tier Compliance Results

| # | Orientation | Concepts | Valid? | Depth | Complexity | Text Blocks | Status |
|---|-------------|----------|--------|-------|------------|-------------|---------|
| **1** | Portrait | 11 | ✅ 8-16 | 4 | 44 | 35 | ⚠️ Minor issues |
| **2** | Portrait | 11 | ✅ 8-16 | 4 | 44 | 52 | ⚠️ Minor issues |
| 3 | Portrait | 2 | ❌ Too few | 4 | 8 | 13 | ❌ Invalid |
| **4** | Landscape | 8 | ✅ 8-16 | 4 | 32 | 45 | ⚠️ Minor issues |
| 5 | Landscape | 7 | ❌ Too few | 4 | 28 | 48 | ❌ Invalid |
| **6** | Landscape | 16 | ✅ 8-16 | 4 | 64 | 47 | ⚠️ Minor issues |
| 7 | Landscape | 7 | ❌ Too few | 4 | 28 | 44 | ❌ Invalid |
| 8 | Landscape | 7 | ❌ Too few | 4 | 28 | 49 | ❌ Invalid |
| 9 | Landscape | 6 | ❌ Too few | 4 | 24 | 45 | ❌ Invalid |
| **10** | Landscape | 11 | ✅ 8-16 | 4 | 44 | 40 | ⚠️ Minor issues |
| 11 | Landscape | 24 | ❌ Too many | 4 | 96 | 50 | ❌ Invalid |
| 12 | Landscape | 6 | ❌ Too few | 4 | 24 | 41 | ❌ Invalid |

### Concise Tier Requirements

- **Concepts:** 8-16 (expected)
- **Depth:** 3-4 hierarchy levels (expected)
- **Complexity:** concepts × depth (lower is better)

## Top Candidates

### Portrait Variants (Preferred Visual Style)

**Variant #1** - 11 concepts, 35 text blocks
- Clean icon grid layout (3 columns per tier)
- Rounded-corner boxes with two-tone design
- Simple line-art icons with color fills
- Equal-height tiers stacked vertically
- White background with excellent spacing

**Variant #2** - 11 concepts, 52 text blocks
- Tab-style colored headers
- Large single icon on left per tier
- Bulleted list layout on right
- Light-tinted content areas (pink/orange/green)
- Similar rounded-corner aesthetic to #1

### Landscape Variants (Adapted Style)

**Variant #4** - 8 concepts (minimum), 45 text blocks
- Minimal concept density
- At lower boundary of valid range

**Variant #6** - 16 concepts (maximum), 47 text blocks
- Maximum concept density
- At upper boundary of valid range

**Variant #10** - 11 concepts, 40 text blocks ⭐ **RECOMMENDED**
- Side-by-side three-column layout
- Successfully adapts portrait style (#1, #2) to landscape
- Rounded-corner boxes maintained
- Two-tone design (colored header + light-tinted content)
- Icon grid layout (2×2 icons per tier)
- Equal-width tiers for direct comparison
- Matches concept count of portrait variants (11)

## Visual Style Analysis

### Shared Characteristics (Variants #1, #2, #10)

1. **Rounded-corner boxes** (12-16px radius)
2. **Two-tone tier design** (colored header + light-tinted content area)
3. **Icon-heavy layouts** with simple line-art icons
4. **Color-coded tiers:**
   - Red #FF6B6B (Prohibited)
   - Orange #ED8936 (High-Risk)
   - Green #48BB78 (Limited-Risk)
5. **White background** #FFFFFF
6. **Equal tier proportions**
7. **Consistent iconography style** (outline/line art)
8. **Clear visual hierarchy** through color and spacing

### Layout Variants

- **Portrait (#1, #2):** Vertical stacking, 3 tiers top-to-bottom
- **Landscape (#10):** Horizontal arrangement, 3 tiers side-by-side

## Concept Density Patterns

### Portrait Variants (1-3)
- Average valid concepts: 11
- Range: 2-11
- Success rate: 66% (2/3)

### Landscape Variants (4-12)
- Average valid concepts: 10.1
- Range: 6-24
- Success rate: 33% (3/9)
- High variance suggests inconsistent Gemini interpretation

## Key Insights

1. **Concept sweet spot:** 8-11 concepts for reliable concise tier compliance
2. **Style consistency:** Portrait variants show more consistent results
3. **Landscape adaptation:** Variant #10 successfully translates portrait aesthetic to horizontal format
4. **Orientation trade-off:** Landscape improves scanability (side-by-side comparison) but shows higher generation variance
5. **Depth uniformity:** All variants maintain 4 hierarchy levels (at upper limit of 3-4 expected)

## Recommendations

### Primary Recommendation: Variant #10
- ✅ Landscape orientation (better for side-by-side tier comparison)
- ✅ 11 concepts (matches preferred portrait variants)
- ✅ Successfully adapts visual style from #1 and #2
- ✅ Lowest complexity among landscape candidates (44)
- ✅ Clean execution of rounded-corner, two-tone design

### Alternative Candidates

**For maximum simplicity:** Variant #4 (8 concepts, minimal density)
**For maximum detail:** Variant #6 (16 concepts, upper boundary)
**For portrait format:** Variants #1 or #2 (11 concepts, original preferred style)

## Prompt Evolution

### Initial Prompt (Portrait-Optimized)
- 34 concepts → Failed concise tier
- 3 depth levels → Too deep for concise/standard, too shallow for detailed

### Revised Prompt (Concise-Compliant)
- 16 concepts → Passes concise tier validation
- 2 depth levels → Within 1-2 expected
- Added visual style enforcement from #1 and #2:
  - Rounded-corner boxes
  - Two-tone tier design
  - Line-art icons
  - Equal tier heights

## Files Generated

### Portrait (Variants 1-3)
- `eu-ai-act-1.webp` ⭐ Valid
- `eu-ai-act-2.webp` ⭐ Valid
- `eu-ai-act-3.webp` ❌ Invalid

### Landscape - Batch 1 (Variants 4-6)
- `eu-ai-act-4.webp` ⭐ Valid
- `eu-ai-act-5.webp` ❌ Invalid
- `eu-ai-act-6.webp` ⭐ Valid

### Landscape - Batch 2 (Variants 7-9)
- `eu-ai-act-7.webp` ❌ Invalid
- `eu-ai-act-8.webp` ❌ Invalid
- `eu-ai-act-9.webp` ❌ Invalid

### Landscape - Batch 3 (Variants 10-12)
- `eu-ai-act-10.webp` ⭐ Valid (RECOMMENDED)
- `eu-ai-act-11.webp` ❌ Invalid
- `eu-ai-act-12.webp` ❌ Invalid

## Next Steps

1. **Select variant #10** for primary use (landscape format, style-compliant)
2. **Optional:** Keep variants #1 or #2 for portrait applications
3. **Archive invalid variants** (3, 5, 7-9, 11-12) or delete to clean directory
4. **Document selection** in project assets or style guide
