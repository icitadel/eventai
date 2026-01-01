#!/usr/bin/env python3
"""
Unit tests for prompt structural analysis functions.

Tests the core logic of analyze_prompt_structure() to ensure accurate
concept counting and hierarchy depth measurement.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from gemini_generate import analyze_prompt_structure

def test_simple_prompt():
    """Test analysis of simple prompt with minimal structure."""
    prompt = """# Title

## Section 1
- Item 1
- Item 2

## Section 2
- Item 3
"""
    
    result = analyze_prompt_structure(prompt)
    
    assert result['headings'] == 2, f"Expected 2 sections, got {result['headings']}"
    assert result['bullets'] == 3, f"Expected 3 top-level bullets, got {result['bullets']}"
    assert result['concepts'] == 5, f"Expected 5 concepts (2 sections + 3 bullets), got {result['concepts']}"
    assert result['max_heading_depth'] == 2, f"Expected max heading depth 2, got {result['max_heading_depth']}"
    assert result['max_list_depth'] == 1, f"Expected max list depth 1, got {result['max_list_depth']}"
    assert result['depth'] == 2, f"Expected depth 2, got {result['depth']}"
    assert result['complexity'] == 10, f"Expected complexity 10 (5×2), got {result['complexity']}"
    
    print("✅ PASS: test_simple_prompt")

def test_nested_lists():
    """Test detection of nested list depth."""
    prompt = """# Title

## Section 1
- Level 1 item
  - Level 2 item
    - Level 3 item
- Another level 1 item
"""
    
    result = analyze_prompt_structure(prompt)
    
    assert result['max_list_depth'] == 3, f"Expected max list depth 3, got {result['max_list_depth']}"
    assert result['bullets'] == 2, f"Expected 2 top-level bullets, got {result['bullets']}"
    assert result['depth'] == 3, f"Expected depth 3 (max of heading=2, list=3), got {result['depth']}"
    
    print("✅ PASS: test_nested_lists")

def test_concise_tier_prompt():
    """Test Concise tier example prompt."""
    prompt_path = Path(__file__).parent / 'fixtures/prompts/concise-example.md'
    
    with open(prompt_path, 'r') as f:
        prompt = f.read()
    
    result = analyze_prompt_structure(prompt)
    
    # Concise tier: 5-8 concepts, 1-2 depth
    assert 5 <= result['concepts'] <= 8, \
        f"Concise tier should have 5-8 concepts, got {result['concepts']}"
    assert 1 <= result['depth'] <= 2, \
        f"Concise tier should have 1-2 depth, got {result['depth']}"
    
    print(f"✅ PASS: test_concise_tier_prompt (concepts={result['concepts']}, depth={result['depth']})")

def test_standard_breadth_prompt():
    """Test Standard breadth tier example prompt."""
    prompt_path = Path(__file__).parent / 'fixtures/prompts/standard-breadth-example.md'
    
    with open(prompt_path, 'r') as f:
        prompt = f.read()
    
    result = analyze_prompt_structure(prompt)
    
    # Standard breadth: 10-15 concepts, 1-2 depth
    assert 10 <= result['concepts'] <= 15, \
        f"Standard breadth should have 10-15 concepts, got {result['concepts']}"
    assert 1 <= result['depth'] <= 2, \
        f"Standard breadth should have 1-2 depth, got {result['depth']}"
    
    print(f"✅ PASS: test_standard_breadth_prompt (concepts={result['concepts']}, depth={result['depth']})")

def test_standard_depth_prompt():
    """Test Standard depth tier example prompt."""
    prompt_path = Path(__file__).parent / 'fixtures/prompts/standard-depth-example.md'
    
    with open(prompt_path, 'r') as f:
        prompt = f.read()
    
    result = analyze_prompt_structure(prompt)
    
    # Standard depth: 5-8 concepts, 3 depth
    assert 5 <= result['concepts'] <= 8, \
        f"Standard depth should have 5-8 concepts, got {result['concepts']}"
    assert result['depth'] == 3, \
        f"Standard depth should have 3 depth, got {result['depth']}"
    
    print(f"✅ PASS: test_standard_depth_prompt (concepts={result['concepts']}, depth={result['depth']})")

def test_detailed_tier_prompt():
    """Test Detailed tier example prompt."""
    prompt_path = Path(__file__).parent / 'fixtures/prompts/detailed-example.md'
    
    with open(prompt_path, 'r') as f:
        prompt = f.read()
    
    result = analyze_prompt_structure(prompt)
    
    # Detailed tier: 20-30+ concepts, 4+ depth
    assert result['concepts'] >= 20, \
        f"Detailed tier should have 20+ concepts, got {result['concepts']}"
    assert result['depth'] >= 4, \
        f"Detailed tier should have 4+ depth, got {result['depth']}"
    
    print(f"✅ PASS: test_detailed_tier_prompt (concepts={result['concepts']}, depth={result['depth']})")

def test_edge_case_empty_prompt():
    """Test handling of empty prompt."""
    prompt = ""
    
    result = analyze_prompt_structure(prompt)
    
    assert result['concepts'] == 0, f"Empty prompt should have 0 concepts, got {result['concepts']}"
    assert result['depth'] == 0, f"Empty prompt should have 0 depth, got {result['depth']}"
    
    print("✅ PASS: test_edge_case_empty_prompt")

def test_edge_case_no_structure():
    """Test prompt with text but no markdown structure."""
    prompt = "Just plain text with no headings or bullets."
    
    result = analyze_prompt_structure(prompt)
    
    assert result['concepts'] == 0, f"Unstructured prompt should have 0 concepts, got {result['concepts']}"
    assert result['depth'] == 0, f"Unstructured prompt should have 0 depth, got {result['depth']}"
    
    print("✅ PASS: test_edge_case_no_structure")

def test_different_bullet_styles():
    """Test detection of different bullet point markers."""
    prompt = """# Title

## Section 1
- Dash bullet
* Asterisk bullet
• Unicode bullet
"""
    
    result = analyze_prompt_structure(prompt)
    
    assert result['bullets'] == 3, f"Expected 3 bullets (-, *, •), got {result['bullets']}"
    assert result['concepts'] == 4, f"Expected 4 concepts (1 section + 3 bullets), got {result['concepts']}"
    
    print("✅ PASS: test_different_bullet_styles")

def test_deeply_nested_headings():
    """Test detection of deep heading hierarchy."""
    prompt = """# H1
## H2
### H3
#### H4
##### H5
###### H6
"""
    
    result = analyze_prompt_structure(prompt)
    
    assert result['max_heading_depth'] == 6, f"Expected max heading depth 6, got {result['max_heading_depth']}"
    
    print("✅ PASS: test_deeply_nested_headings")

def main():
    """Run all unit tests."""
    print("\n" + "=" * 60)
    print("PROMPT ANALYSIS UNIT TESTS")
    print("=" * 60)
    
    try:
        # Basic functionality tests
        test_simple_prompt()
        test_nested_lists()
        test_different_bullet_styles()
        test_deeply_nested_headings()
        
        # Edge case tests
        test_edge_case_empty_prompt()
        test_edge_case_no_structure()
        
        # Tier example tests
        test_concise_tier_prompt()
        test_standard_breadth_prompt()
        test_standard_depth_prompt()
        test_detailed_tier_prompt()
        
        print("\n" + "=" * 60)
        print("✅ ALL UNIT TESTS PASSED (10/10)")
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
