# Density Validation Testing Guide

This directory contains comprehensive automated tests for the density validation system.

## Test Structure

### 1. Unit Tests: Structural Analysis (`test_prompt_analysis.py`)

Tests the core `analyze_prompt_structure()` function:
- ✅ Concept counting (sections + top-level bullets)
- ✅ Hierarchy depth detection (headings + list nesting)
- ✅ Complexity calculation (concepts × depth)
- ✅ Edge cases (empty prompts, unstructured text)
- ✅ Tier example prompts match specifications

**10 test cases covering:**
- Basic functionality (simple prompts, nested lists)
- Different bullet styles (-, *, •)
- Deep heading hierarchies (H1-H6)
- Edge cases (empty, no structure)
- All four tier examples (Concise, Standard breadth/depth, Detailed)

### 2. Unit Tests: Validation Logic (`test_prompt_validation.py`)

Tests the `validate_prompt_against_tier()` function:
- ✅ Correct tier acceptance (Concise as Concise, etc.)
- ✅ Correct tier rejection (Concise NOT as Standard/Detailed)
- ✅ Standard tier variant detection (breadth vs. depth)
- ✅ Complexity formula validation
- ✅ Real-world prompt validation (consent-spectrum)

**12 test cases covering:**
- Concise tier validation (3 tests: accept Concise, reject Standard/Detailed)
- Standard tier validation (4 tests: accept Standard breadth/depth, reject Concise/Detailed)
- Detailed tier validation (3 tests: accept Detailed, reject Concise/Standard)
- Utility tests (complexity calculation)
- Real-world examples (consent-spectrum.prompt.md)

### 3. Integration Tests: CLI Validation (`test_density_validation.py`)

Tests the CLI validation interface end-to-end:
- ✅ CLI argument parsing and validation mode activation
- ✅ Output formatting and user-facing messages
- ✅ Exit codes (0 for valid, 1 for invalid)
- ✅ Error handling (missing files, malformed inputs)

**Tests validate:**
- All tier examples through full CLI pipeline
- Cross-tier rejection (ensure prompts don't validate as wrong tier)
- Real-world prompts (consent-spectrum)

## Running Tests

### Quick Run (All Tests)

```bash
# From todd-media directory
cd .todd/lib/py/todd-media
./tests/run_tests.sh
```

Or:

```bash
python3 tests/run_all_tests.py
```

### Individual Test Suites

```bash
# Unit tests: Structural analysis
python3 tests/test_prompt_analysis.py

# Unit tests: Validation logic
python3 tests/test_prompt_validation.py

# Integration tests: CLI validation
python3 tests/test_density_validation.py
```

### Expected Output

```
════════════════════════════════════════════════════════════
  DENSITY VALIDATION TEST SUITE
════════════════════════════════════════════════════════════

Running: Structural Analysis Unit Tests
============================================================
PROMPT ANALYSIS UNIT TESTS
============================================================
✅ PASS: test_simple_prompt
✅ PASS: test_nested_lists
✅ PASS: test_different_bullet_styles
✅ PASS: test_deeply_nested_headings
✅ PASS: test_edge_case_empty_prompt
✅ PASS: test_edge_case_no_structure
✅ PASS: test_concise_tier_prompt (concepts=6, depth=2)
✅ PASS: test_standard_breadth_prompt (concepts=13, depth=2)
✅ PASS: test_standard_depth_prompt (concepts=6, depth=3)
✅ PASS: test_detailed_tier_prompt (concepts=29, depth=4)

============================================================
✅ ALL UNIT TESTS PASSED (10/10)
============================================================

Running: Validation Logic Unit Tests
============================================================
[... similar output for 12 validation tests ...]

Running: CLI Integration Tests
============================================================
[... integration test output ...]

════════════════════════════════════════════════════════════
TEST SUITE SUMMARY
════════════════════════════════════════════════════════════
✅ Structural Analysis Unit Tests
✅ Validation Logic Unit Tests
✅ CLI Integration Tests

════════════════════════════════════════════════════════════
✅ ALL TEST SUITES PASSED (3/3)
════════════════════════════════════════════════════════════

✨ Density validation system is working correctly!
```

## Test Fixtures

### Prompt Examples (`fixtures/prompts/`)

**Concise tier** (`concise-example.md`):
- Concepts: 6 (5 revenue categories + structure section)
- Depth: 2 levels (headings → bullets)
- Complexity: 12
- Philosophy: Few concepts, shallow depth

**Standard breadth** (`standard-breadth-example.md`):
- Concepts: 13 (6 time points × multiple technologies)
- Depth: 2 levels (year → technology percentages)
- Complexity: 26
- Philosophy: Many concepts, shallow depth

**Standard depth** (`standard-depth-example.md`):
- Concepts: 6 (3 consent models × 2 aspects)
- Depth: 3 levels (model → aspect → details)
- Complexity: 18
- Philosophy: Few concepts, deeper explanations

**Detailed tier** (`detailed-example.md`):
- Concepts: 29 (5 revenue streams + tech stack + legal)
- Depth: 4-5 levels (stream → aspect → details → examples)
- Complexity: 116-145
- Philosophy: Many concepts AND deep detail

See [fixtures/README.md](fixtures/README.md) for detailed documentation.

## Adding New Tests

### 1. Add Unit Test

```python
# In test_prompt_analysis.py or test_prompt_validation.py
def test_your_new_test():
    """Description of what this tests."""
    # Your test logic
    assert condition, "Failure message"
    print("✅ PASS: test_your_new_test")
```

### 2. Add Integration Test

```python
# In test_density_validation.py
def test_your_integration_test():
    """Description of integration test."""
    result = run_validation('prompt', path, tier)
    assert result['valid'], "Should validate"
    print("✅ PASS: test_your_integration_test")
```

### 3. Run Test Suite

```bash
./tests/run_tests.sh
```

## Test Coverage

### Current Coverage

- ✅ **Structural Analysis:** Concept counting, depth detection, complexity calculation
- ✅ **Validation Logic:** Tier acceptance/rejection, variant detection
- ✅ **CLI Interface:** Argument parsing, output formatting, exit codes
- ✅ **Edge Cases:** Empty prompts, malformed markdown, no structure
- ✅ **Real-World Examples:** consent-spectrum.prompt.md validation

### Not Yet Covered

- ⏸️ **Image Validation:** OCR-based analysis (requires Tesseract, pytesseract, sklearn)
- ⏸️ **Performance:** Large prompt handling, timeout behavior
- ⏸️ **Error Recovery:** Malformed files, encoding issues, permission errors

## Continuous Integration

To integrate with CI/CD:

```yaml
# .github/workflows/test-density-validation.yml
name: Density Validation Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Run tests
        run: |
          cd .todd/lib/py/todd-media
          ./tests/run_tests.sh
```

## Debugging Failed Tests

### Test Fails: Concepts Count Mismatch

```
AssertionError: Concise tier should have 5-8 concepts, got 12
```

**Diagnosis:**
- Check if prompt has more sections (##) or top-level bullets than expected
- Verify nested bullets aren't counted (only top-level count as concepts)

**Fix:**
- Reduce number of ## sections or top-level bullets in example prompt
- Or adjust tier specification if example is correct

### Test Fails: Depth Detection Wrong

```
AssertionError: Expected depth 2, got 3
```

**Diagnosis:**
- Check for nested lists (indented bullets)
- Verify heading depth (###, ####)

**Fix:**
- Flatten list structure (remove indentation)
- Or reduce heading depth

### Test Fails: Tier Validation Rejects Valid Prompt

```
AssertionError: Concise prompt should validate as Concise tier
Metrics: {'concepts': 8, 'depth': 2, 'complexity': 16}
Expected: {'concepts': (5, 8), 'depth': (1, 2)}
```

**Diagnosis:**
- Prompt is at edge of valid range (8 concepts is max for Concise)
- Validation logic may be too strict (using < instead of <=)

**Fix:**
- Verify validation range is inclusive: `5 <= concepts <= 8`
- Not exclusive: `5 < concepts < 8`

## Performance Benchmarks

Expected execution times (on typical developer machine):

- Unit tests (analysis): ~0.1s
- Unit tests (validation): ~0.2s
- Integration tests (CLI): ~1-2s (subprocess overhead)
- **Total:** ~2-3s for full test suite

If tests take significantly longer:
- Check for infinite loops in regex parsing
- Verify file I/O isn't blocking
- Ensure no network requests in tests

## Exit Codes

All test scripts use standard exit codes:
- **0** = All tests passed
- **1** = One or more tests failed

This allows easy integration with CI/CD pipelines:

```bash
./tests/run_tests.sh && echo "Deploy!" || echo "Fix tests first"
```

---

*Last updated: January 1, 2026*
*Maintained by: Lemmy Content Generation System*
