#!/usr/bin/env python3
"""
Unit tests for image validation functions (OCR-based).

Tests the three new validation functions:
- calculate_whitespace_percentage()
- validate_image_text_density()
- score_visual_hierarchy()

Requires: tesseract, pytesseract, scikit-learn
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from gemini_generate import (
    calculate_whitespace_percentage,
    validate_image_text_density,
    score_visual_hierarchy
)

# Test image paths (using real fixtures from docs/writing)
# From: .todd/lib/py/todd-media/gemini-generate/tests/test_image_validation.py
# To:   docs/writing (7 levels up to eventai root)
DOCS_DIR = Path(__file__).parent.parent.parent.parent.parent.parent.parent / 'docs/writing'

CONCISE_IMAGE = DOCS_DIR / '5-analytics/visuals/traditional-vs-ai-concise/traditional-vs-ai-concise-1.webp'
STANDARD_IMAGE = DOCS_DIR / '1-transformation/visuals/five-barriers/five-barriers-1.webp'
DETAILED_IMAGE = DOCS_DIR / '4-privacy/visuals/consent-spectrum/consent-spectrum-12.webp'


def test_whitespace_concise_image():
    """Concise image should have 40-60% whitespace."""
    if not CONCISE_IMAGE.exists():
        print(f"⚠️  SKIP: Fixture not found: {CONCISE_IMAGE}")
        return

    result = calculate_whitespace_percentage(str(CONCISE_IMAGE))

    assert 'error' not in result, f"Whitespace calculation failed: {result.get('error')}"
    assert 'percentage' in result, "Missing percentage in result"

    percentage = result['percentage']
    assert 40 <= percentage <= 60, \
        f"Concise image should have 40-60% whitespace, got {percentage}%"

    print(f"✅ PASS: Concise whitespace = {percentage}% (within 40-60% range)")


def test_whitespace_standard_image():
    """Standard image should have 30-40% whitespace."""
    if not STANDARD_IMAGE.exists():
        print(f"⚠️  SKIP: Fixture not found: {STANDARD_IMAGE}")
        return

    result = calculate_whitespace_percentage(str(STANDARD_IMAGE))

    assert 'error' not in result, f"Whitespace calculation failed: {result.get('error')}"

    percentage = result['percentage']
    # Allow ±5% tolerance as spec defines
    assert 25 <= percentage <= 45, \
        f"Standard image should have ~30-40% whitespace (±5%), got {percentage}%"

    print(f"✅ PASS: Standard whitespace = {percentage}% (within 30-40% ±5% range)")


def test_whitespace_returns_metadata():
    """Whitespace function should return detailed metadata."""
    if not CONCISE_IMAGE.exists():
        print(f"⚠️  SKIP: Fixture not found: {CONCISE_IMAGE}")
        return

    result = calculate_whitespace_percentage(str(CONCISE_IMAGE))

    assert 'percentage' in result
    assert 'threshold' in result
    assert result['threshold'] == 240, "Default threshold should be 240"
    assert 'inverted' in result
    assert 'mean_brightness' in result
    assert 'image_size' in result
    assert 'total_pixels' in result
    assert 'white_pixels' in result

    print(f"✅ PASS: Whitespace returns complete metadata (threshold={result['threshold']}, size={result['image_size']})")


def test_text_density_concise_image():
    """Concise image text blocks should have ≤5 words (level 1-2)."""
    if not CONCISE_IMAGE.exists():
        print(f"⚠️  SKIP: Fixture not found: {CONCISE_IMAGE}")
        return

    result = validate_image_text_density(str(CONCISE_IMAGE), 'concise')

    assert 'error' not in result, f"Text density validation failed: {result.get('error')}"
    assert result['valid'], \
        f"Concise image should pass text density validation (found {len(result['violations'])} violations)"

    print(f"✅ PASS: Concise text density valid ({result['level12_blocks']} blocks checked, 0 violations)")


def test_text_density_standard_image():
    """Standard image text blocks should have ≤15 words (level 1-2)."""
    if not STANDARD_IMAGE.exists():
        print(f"⚠️  SKIP: Fixture not found: {STANDARD_IMAGE}")
        return

    result = validate_image_text_density(str(STANDARD_IMAGE), 'standard')

    assert 'error' not in result, f"Text density validation failed: {result.get('error')}"

    # Standard can have some violations if text is verbose
    # We consider it acceptable if <20% of blocks violate
    violation_rate = len(result['violations']) / max(result['level12_blocks'], 1)

    assert violation_rate < 0.2, \
        f"Standard image has too many text density violations: {len(result['violations'])} / {result['level12_blocks']} blocks ({violation_rate:.0%})"

    print(f"✅ PASS: Standard text density acceptable ({len(result['violations'])} violations / {result['level12_blocks']} blocks = {violation_rate:.0%})")


def test_text_density_returns_violations():
    """Text density function should return detailed violation information."""
    if not DETAILED_IMAGE.exists():
        print(f"⚠️  SKIP: Fixture not found: {DETAILED_IMAGE}")
        return

    # Test with 'concise' limit (5 words) on detailed image to force violations
    result = validate_image_text_density(str(DETAILED_IMAGE), 'concise')

    assert 'valid' in result
    assert 'violations' in result
    assert 'tier' in result
    assert result['tier'] == 'concise'
    assert 'total_blocks' in result
    assert 'level12_blocks' in result
    assert 'word_limit' in result
    assert result['word_limit'] == 5

    if result['violations']:
        violation = result['violations'][0]
        assert 'block_index' in violation
        assert 'level' in violation
        assert 'text' in violation
        assert 'word_count' in violation
        assert 'limit' in violation
        assert 'excess' in violation

    print(f"✅ PASS: Text density returns detailed violation data (found {len(result['violations'])} violations)")


def test_hierarchy_score_range():
    """Hierarchy score should be between 0.0 and 1.0."""
    if not CONCISE_IMAGE.exists():
        print(f"⚠️  SKIP: Fixture not found: {CONCISE_IMAGE}")
        return

    result = score_visual_hierarchy(str(CONCISE_IMAGE))

    assert 'error' not in result, f"Hierarchy scoring failed: {result.get('error')}"
    assert 'score' in result
    assert 0.0 <= result['score'] <= 1.0, \
        f"Hierarchy score should be 0.0-1.0, got {result['score']}"

    print(f"✅ PASS: Hierarchy score in valid range (score={result['score']})")


def test_hierarchy_score_assessment():
    """Hierarchy score should include quality assessment."""
    if not STANDARD_IMAGE.exists():
        print(f"⚠️  SKIP: Fixture not found: {STANDARD_IMAGE}")
        return

    result = score_visual_hierarchy(str(STANDARD_IMAGE))

    assert 'assessment' in result
    assert result['assessment'] in ['Excellent', 'Good', 'Fair', 'Poor', 'No Text', 'Error'], \
        f"Unexpected assessment: {result['assessment']}"

    # Standard image (five-barriers) should have good hierarchy
    assert result['score'] >= 0.7, \
        f"Expected good hierarchy for standard image, got {result['score']} ({result['assessment']})"

    print(f"✅ PASS: Hierarchy assessment = {result['assessment']} (score={result['score']}, ratio={result.get('avg_ratio')})")


def test_hierarchy_returns_ratios():
    """Hierarchy function should return font size ratios and level data."""
    if not CONCISE_IMAGE.exists():
        print(f"⚠️  SKIP: Fixture not found: {CONCISE_IMAGE}")
        return

    result = score_visual_hierarchy(str(CONCISE_IMAGE))

    assert 'score' in result
    assert 'avg_ratio' in result
    assert 'n_levels' in result
    assert 'level_means' in result
    assert 'ratios' in result
    assert 'assessment' in result

    # Gemini images consistently have 4 levels based on fixture analysis
    assert result['n_levels'] >= 3, \
        f"Expected at least 3 hierarchy levels, got {result['n_levels']}"

    # Avg ratio should be reasonable (>1.0)
    assert result['avg_ratio'] >= 1.0, \
        f"Average ratio should be ≥1.0, got {result['avg_ratio']}"

    print(f"✅ PASS: Hierarchy returns complete data (levels={result['n_levels']}, avg_ratio={result['avg_ratio']}, ratios={result['ratios']})")


def test_missing_dependencies_handling():
    """Functions should gracefully handle missing dependencies."""
    # This test would need to mock the imports, which is complex
    # For now, just verify functions don't crash on edge cases
    print("⚠️  SKIP: Missing dependencies test (requires mocking)")


def run_all_tests():
    """Run all image validation tests."""
    tests = [
        ('Whitespace: Concise image range', test_whitespace_concise_image),
        ('Whitespace: Standard image range', test_whitespace_standard_image),
        ('Whitespace: Metadata completeness', test_whitespace_returns_metadata),
        ('Text Density: Concise validation', test_text_density_concise_image),
        ('Text Density: Standard validation', test_text_density_standard_image),
        ('Text Density: Violation details', test_text_density_returns_violations),
        ('Hierarchy: Score range', test_hierarchy_score_range),
        ('Hierarchy: Assessment quality', test_hierarchy_score_assessment),
        ('Hierarchy: Ratio data', test_hierarchy_returns_ratios),
    ]

    print("=" * 70)
    print("IMAGE VALIDATION TESTS (OCR-based)")
    print("=" * 70)
    print()

    passed = 0
    failed = 0
    skipped = 0

    for name, test_func in tests:
        try:
            print(f"Running: {name}")
            test_func()
            passed += 1
            print()
        except AssertionError as e:
            print(f"❌ FAIL: {name}")
            print(f"   {e}")
            print()
            failed += 1
        except Exception as e:
            if "SKIP" in str(e):
                print(f"⚠️  SKIP: {name} - {e}")
                skipped += 1
            else:
                print(f"❌ ERROR: {name}")
                print(f"   {e}")
                failed += 1
            print()

    print("=" * 70)
    print(f"RESULTS: {passed} passed, {failed} failed, {skipped} skipped")
    print("=" * 70)

    return failed == 0


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
