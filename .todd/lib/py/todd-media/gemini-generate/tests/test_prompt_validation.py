#!/usr/bin/env python3
"""
Unit tests for prompt validation logic.

Tests validate_prompt_against_tier() to ensure correct acceptance/rejection
of prompts based on tier specifications.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from gemini_generate import validate_prompt_against_tier

TEST_DIR = Path(__file__).parent / 'fixtures/prompts'

def test_concise_validates_as_concise():
    """Concise prompt should validate as Concise tier."""
    result = validate_prompt_against_tier(TEST_DIR / 'concise-example.md', 'concise')

    assert result['valid'], \
        f"Concise prompt should validate as Concise tier\nMetrics: {result['metrics']}\nExpected: {result['expected']}"
    assert result['tier'] == 'concise'

    print(f"✅ PASS: Concise validates as Concise (concepts={result['metrics']['concepts']}, depth={result['metrics']['depth']})")

def test_concise_breadth_validates_as_concise():
    """Concise breadth prompt (upper bound) should validate as Concise tier."""
    result = validate_prompt_against_tier(TEST_DIR / 'concise-breadth-example.md', 'concise')

    assert result['valid'], \
        f"Concise breadth should validate as Concise tier\nMetrics: {result['metrics']}\nExpected: {result['expected']}"
    assert result['tier'] == 'concise'

    print(f"✅ PASS: Concise breadth validates as Concise (concepts={result['metrics']['concepts']}, depth={result['metrics']['depth']}, complexity={result['metrics']['complexity']})")

def test_concise_rejects_standard():
    """Concise prompt should NOT validate as Standard tier."""
    result = validate_prompt_against_tier(TEST_DIR / 'concise-example.md', 'standard')
    
    assert not result['valid'], \
        f"Concise prompt should NOT validate as Standard tier\nMetrics: {result['metrics']}"
    
    print("✅ PASS: Concise correctly rejects Standard tier")

def test_concise_rejects_detailed():
    """Concise prompt should NOT validate as Detailed tier."""
    result = validate_prompt_against_tier(TEST_DIR / 'concise-example.md', 'detailed')
    
    assert not result['valid'], \
        f"Concise prompt should NOT validate as Detailed tier\nMetrics: {result['metrics']}"
    
    print("✅ PASS: Concise correctly rejects Detailed tier")

def test_standard_breadth_validates_as_standard():
    """Standard breadth prompt should validate as Standard tier."""
    result = validate_prompt_against_tier(TEST_DIR / 'standard-breadth-example.md', 'standard')
    
    assert result['valid'], \
        f"Standard breadth should validate as Standard tier\nMetrics: {result['metrics']}\nExpected: {result['expected']}"
    assert result['tier'] == 'standard'
    assert result['variant'] == 'breadth', \
        f"Expected 'breadth' variant, got '{result['variant']}'"
    
    print(f"✅ PASS: Standard breadth validates as Standard (variant={result['variant']}, concepts={result['metrics']['concepts']}, depth={result['metrics']['depth']})")

def test_standard_depth_validates_as_standard():
    """Standard depth prompt should validate as Standard tier."""
    result = validate_prompt_against_tier(TEST_DIR / 'standard-depth-example.md', 'standard')
    
    assert result['valid'], \
        f"Standard depth should validate as Standard tier\nMetrics: {result['metrics']}\nExpected: {result['expected']}"
    assert result['tier'] == 'standard'
    assert result['variant'] == 'depth', \
        f"Expected 'depth' variant, got '{result['variant']}'"
    
    print(f"✅ PASS: Standard depth validates as Standard (variant={result['variant']}, concepts={result['metrics']['concepts']}, depth={result['metrics']['depth']})")

def test_standard_rejects_concise():
    """Standard prompt should NOT validate as Concise tier."""
    result = validate_prompt_against_tier(TEST_DIR / 'standard-breadth-example.md', 'concise')
    
    assert not result['valid'], \
        f"Standard prompt should NOT validate as Concise tier\nMetrics: {result['metrics']}"
    
    print("✅ PASS: Standard correctly rejects Concise tier")

def test_standard_rejects_detailed():
    """Standard prompt should NOT validate as Detailed tier."""
    result = validate_prompt_against_tier(TEST_DIR / 'standard-breadth-example.md', 'detailed')
    
    assert not result['valid'], \
        f"Standard prompt should NOT validate as Detailed tier\nMetrics: {result['metrics']}"
    
    print("✅ PASS: Standard correctly rejects Detailed tier")

def test_detailed_validates_as_detailed():
    """Detailed prompt should validate as Detailed tier."""
    result = validate_prompt_against_tier(TEST_DIR / 'detailed-example.md', 'detailed')
    
    assert result['valid'], \
        f"Detailed prompt should validate as Detailed tier\nMetrics: {result['metrics']}\nExpected: {result['expected']}"
    assert result['tier'] == 'detailed'
    
    print(f"✅ PASS: Detailed validates as Detailed (concepts={result['metrics']['concepts']}, depth={result['metrics']['depth']})")

def test_detailed_rejects_concise():
    """Detailed prompt should NOT validate as Concise tier."""
    result = validate_prompt_against_tier(TEST_DIR / 'detailed-example.md', 'concise')
    
    assert not result['valid'], \
        f"Detailed prompt should NOT validate as Concise tier\nMetrics: {result['metrics']}"
    
    print("✅ PASS: Detailed correctly rejects Concise tier")

def test_detailed_rejects_standard():
    """Detailed prompt should NOT validate as Standard tier."""
    result = validate_prompt_against_tier(TEST_DIR / 'detailed-example.md', 'standard')
    
    assert not result['valid'], \
        f"Detailed prompt should NOT validate as Standard tier\nMetrics: {result['metrics']}"
    
    print("✅ PASS: Detailed correctly rejects Standard tier")

def test_complexity_calculation():
    """Verify complexity = concepts × depth."""
    result = validate_prompt_against_tier(TEST_DIR / 'concise-example.md', 'concise')

    metrics = result['metrics']
    expected_complexity = metrics['concepts'] * metrics['depth']

    assert metrics['complexity'] == expected_complexity, \
        f"Complexity should be concepts × depth: {metrics['concepts']} × {metrics['depth']} = {expected_complexity}, got {metrics['complexity']}"

    print(f"✅ PASS: Complexity correctly calculated ({metrics['concepts']} × {metrics['depth']} = {metrics['complexity']})")

def main():
    """Run all validation tests."""
    print("\n" + "=" * 60)
    print("PROMPT VALIDATION UNIT TESTS")
    print("=" * 60)
    
    if not TEST_DIR.exists():
        print(f"\n❌ ERROR: Test fixtures not found at {TEST_DIR}")
        sys.exit(1)
    
    try:
        # Concise tier tests
        test_concise_validates_as_concise()
        test_concise_breadth_validates_as_concise()
        test_concise_rejects_standard()
        test_concise_rejects_detailed()

        # Standard tier tests
        test_standard_breadth_validates_as_standard()
        test_standard_depth_validates_as_standard()
        test_standard_rejects_concise()
        test_standard_rejects_detailed()

        # Detailed tier tests
        test_detailed_validates_as_detailed()
        test_detailed_rejects_concise()
        test_detailed_rejects_standard()

        # Utility tests
        test_complexity_calculation()

        print("\n" + "=" * 60)
        print("✅ ALL VALIDATION TESTS PASSED (12/12)")
        print("=" * 60)
        sys.exit(0)
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
