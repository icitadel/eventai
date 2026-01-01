# Density Validation Test Fixtures

This directory contains example prompts and infographics representing each density tier, used for automated validation testing.

## Prompt Examples

### Concise Tier: `prompts/concise-example.md`

**Target Metrics:**
- Concepts: 6 (5 revenue categories + structure)
- Depth: 2 levels (headings → bullets, no sub-explanations)
- Complexity: 12 (6 × 2)
- Character count: ~800

**Philosophy:** Few concepts, shallow depth. Labels and values only, minimal explanatory text.

**Example characteristic:** "Tickets: $750,000" (label + value, 1 level)

---

### Standard Breadth Tier: `prompts/standard-breadth-example.md`

**Target Metrics:**
- Concepts: 13 (6 time points × 2-6 technologies each, organized as technology trends)
- Depth: 2 levels (year headings → technology bullets)
- Complexity: 26 (13 × 2)
- Character count: ~1,800

**Philosophy:** Many concepts, shallow depth. Wide coverage across years and technologies without deep explanations.

**Strategy:** Breadth (go wide, not deep)

---

### Standard Depth Tier: `prompts/standard-depth-example.md`

**Target Metrics:**
- Concepts: 6 (3 consent models × 2 aspects: implementation + legal status)
- Depth: 3 levels (model → aspect → details)
- Complexity: 18 (6 × 3)
- Character count: ~1,600

**Philosophy:** Few concepts, deeper detail. Each consent model explained with implementation details and legal status.

**Example characteristic:** "Consent Model 1" → "Implementation" → "Facial recognition required at all entry points" (3 levels)

**Strategy:** Depth (go deep, not wide)

---

### Detailed Tier: `prompts/detailed-example.md`

**Target Metrics:**
- Concepts: 29 (5 revenue streams × 4 aspects + technology stack + legal/ethical)
- Depth: 4-5 levels (revenue stream → aspect → sub-details → examples with data)
- Complexity: 116-145 (29 × 4-5)
- Character count: ~6,500

**Philosophy:** Many concepts AND deep detail. Comprehensive coverage with multi-level explanations, examples, and quantitative data.

**Example characteristic:** "Revenue Stream 1" → "Data Inputs" → "Historical sales velocity" → "2015-2024 data, hourly granularity" (4 levels)

**Strategy:** Both breadth AND depth

---

## Image Examples (TODO)

Image validation requires OCR-based analysis. Example infographics will be added for:
- Concise: Simple bar chart (5-8 data points, minimal text)
- Standard breadth: Timeline with many data points (10-15 concepts, shallow annotations)
- Standard depth: Comparison chart (5-8 concepts, detailed explanations)
- Detailed: Comprehensive system diagram (20-30+ concepts, multi-level annotations)

For now, test with existing consent-spectrum images:
- `consent-spectrum-1.webp` (estimated: Concise tier)
- `consent-spectrum-4.webp` (estimated: Concise tier, publication winner)

---

## Running Tests

```bash
# From todd-media directory
cd .todd/lib/py/todd-media
python3 tests/test_density_validation.py
```

Expected output: All tests pass, confirming that:
1. Concise prompts validate as Concise (and reject Standard/Detailed)
2. Standard prompts validate as Standard (and reject Concise/Detailed)
3. Detailed prompts validate as Detailed (and reject Concise/Standard)
4. Real-world consent-spectrum prompt validates as Concise

---

## Adding New Test Cases

When adding new test fixtures:

1. **Create the prompt/image file** in appropriate subdirectory
2. **Document metrics** in this README (concepts, depth, complexity)
3. **Add test case** to `test_density_validation.py`
4. **Verify manually** before committing:
   ```bash
   python3 gemini_generate.py --validate-prompt fixtures/prompts/your-file.md --density <tier>
   ```

---

*Created: January 1, 2026*
*Purpose: Automated validation testing for density tier compliance*
