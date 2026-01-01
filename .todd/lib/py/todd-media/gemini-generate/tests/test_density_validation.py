#!/usr/bin/env python3
"""
Test density validation for prompts and infographics.

Tests validate that:
1. Example prompts correctly match their intended density tiers
2. Example infographics correctly match their intended density tiers
3. Validation correctly rejects mismatched tiers
"""

import sys
import subprocess
from pathlib import Path

# Test data directory
TEST_DIR = Path(__file__).parent / 'fixtures'

def run_validation(file_type, file_path, tier):
    """Run validation CLI and return result."""
    cmd = [
        'python3',
        str(Path(__file__).parent.parent / 'gemini_generate.py'),
        f'--validate-{file_type}', str(file_path),
        '--density', tier
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {
        'valid': result.returncode == 0,
        'stdout': result.stdout,
        'stderr': result.stderr
    }

def test_concise_prompts():
    """Test that Concise tier prompts validate correctly."""
    print("\n" + "=" * 60)
    print("TEST: Concise Tier Prompts")
    print("=" * 60)
    
    # Should PASS: Concise prompt against Concise tier
    result = run_validation('prompt', TEST_DIR / 'prompts/concise-example.md', 'concise')
    assert result['valid'], f"Concise prompt should validate as Concise\n{result['stdout']}"
    
    # Verify CLI output contains expected elements
    assert '✅ VALID' in result['stdout'], "Output should contain validation success"
    assert 'CONCISE TIER' in result['stdout'], "Output should mention tier"
    assert 'Concepts:' in result['stdout'], "Output should show concepts metric"
    assert 'Depth:' in result['stdout'], "Output should show depth metric"
    assert 'Complexity:' in result['stdout'], "Output should show complexity metric"
    
    print("✅ PASS: concise-example.md validates as Concise")
    print(f"   Verified CLI output format")
    
    # Should FAIL: Concise prompt against Standard tier
    result = run_validation('prompt', TEST_DIR / 'prompts/concise-example.md', 'standard')
    assert not result['valid'], f"Concise prompt should NOT validate as Standard\n{result['stdout']}"
    assert '❌ INVALID' in result['stdout'], "Output should contain validation failure"
    print("✅ PASS: concise-example.md correctly rejects Standard tier")
    
    # Should FAIL: Concise prompt against Detailed tier
    result = run_validation('prompt', TEST_DIR / 'prompts/concise-example.md', 'detailed')
    assert not result['valid'], f"Concise prompt should NOT validate as Detailed\n{result['stdout']}"
    assert '❌ INVALID' in result['stdout'], "Output should contain validation failure"
    print("✅ PASS: concise-example.md correctly rejects Detailed tier")

def test_standard_prompts():
    """Test that Standard tier prompts validate correctly."""
    print("\n" + "=" * 60)
    print("TEST: Standard Tier Prompts")
    print("=" * 60)
    
    # Should PASS: Standard breadth prompt against Standard tier
    result = run_validation('prompt', TEST_DIR / 'prompts/standard-breadth-example.md', 'standard')
    assert result['valid'], f"Standard breadth prompt should validate as Standard\n{result['stdout']}"
    assert '✅ VALID' in result['stdout'], "Output should contain validation success"
    assert 'STANDARD TIER' in result['stdout'], "Output should mention tier"
    assert 'breadth' in result['stdout'].lower(), "Output should identify breadth variant"
    print("✅ PASS: standard-breadth-example.md validates as Standard (breadth)")
    
    # Should PASS: Standard depth prompt against Standard tier
    result = run_validation('prompt', TEST_DIR / 'prompts/standard-depth-example.md', 'standard')
    assert result['valid'], f"Standard depth prompt should validate as Standard\n{result['stdout']}"
    assert 'depth' in result['stdout'].lower(), "Output should identify depth variant"
    print("✅ PASS: standard-depth-example.md validates as Standard (depth)")
    
    # Should FAIL: Standard prompt against Concise tier
    result = run_validation('prompt', TEST_DIR / 'prompts/standard-breadth-example.md', 'concise')
    assert not result['valid'], f"Standard prompt should NOT validate as Concise\n{result['stdout']}"
    assert '❌ INVALID' in result['stdout'], "Output should contain validation failure"
    assert '⚠️  Issues:' in result['stdout'], "Output should explain why validation failed"
    print("✅ PASS: standard-breadth-example.md correctly rejects Concise tier")

def test_detailed_prompts():
    """Test that Detailed tier prompts validate correctly."""
    print("\n" + "=" * 60)
    print("TEST: Detailed Tier Prompts")
    print("=" * 60)
    
    # Should PASS: Detailed prompt against Detailed tier
    result = run_validation('prompt', TEST_DIR / 'prompts/detailed-example.md', 'detailed')
    assert result['valid'], f"Detailed prompt should validate as Detailed\n{result['stdout']}"
    print("✅ PASS: detailed-example.md validates as Detailed")
    
    # Should FAIL: Detailed prompt against Standard tier
    result = run_validation('prompt', TEST_DIR / 'prompts/detailed-example.md', 'standard')
    assert not result['valid'], f"Detailed prompt should NOT validate as Standard\n{result['stdout']}"
    print("✅ PASS: detailed-example.md correctly rejects Standard tier")
    
    # Should FAIL: Detailed prompt against Concise tier
    result = run_validation('prompt', TEST_DIR / 'prompts/detailed-example.md', 'concise')
    assert not result['valid'], f"Detailed prompt should NOT validate as Concise\n{result['stdout']}"
    print("✅ PASS: detailed-example.md correctly rejects Concise tier")

def test_real_world_prompt():
    """Test consent-spectrum prompt (Concise tier)."""
    print("\n" + "=" * 60)
    print("TEST: Real-World Prompt (consent-spectrum)")
    print("=" * 60)
    
    consent_prompt = Path(__file__).parent.parent.parent.parent.parent.parent / \
                     'docs/writing/4-privacy/visuals/consent-spectrum/consent-spectrum.prompt.md'
    
    if consent_prompt.exists():
        result = run_validation('prompt', consent_prompt, 'concise')
        assert result['valid'], f"consent-spectrum.prompt.md should validate as Concise\n{result['stdout']}"
        print("✅ PASS: consent-spectrum.prompt.md validates as Concise")
    else:
        print("⏭️  SKIP: consent-spectrum.prompt.md not found")

def test_cli_output_metrics():
    """Test that CLI outputs correct metric values."""
    print("\n" + "=" * 60)
    print("TEST: CLI Output Metrics Verification")
    print("=" * 60)
    
    # Test Concise example metrics
    result = run_validation('prompt', TEST_DIR / 'prompts/concise-example.md', 'concise')
    assert result['valid'], "Concise example should validate"
    
    # Parse output to verify metrics are in expected ranges
    output = result['stdout']
    
    # Verify concepts are displayed and in range 5-8
    import re
    concepts_match = re.search(r'Concepts:\s+(\d+)\s+\(expected:\s+(\d+)-(\d+)\)', output)
    assert concepts_match, "CLI output should display concepts metric"
    concepts = int(concepts_match.group(1))
    assert 5 <= concepts <= 8, f"Concise should have 5-8 concepts, got {concepts}"
    
    # Verify depth is displayed and in range 1-2
    depth_match = re.search(r'Depth:\s+(\d+)\s+levels?\s+\(expected:\s+(\d+)-(\d+)\)', output)
    assert depth_match, "CLI output should display depth metric"
    depth = int(depth_match.group(1))
    assert 1 <= depth <= 2, f"Concise should have 1-2 depth, got {depth}"
    
    # Verify complexity is displayed and equals concepts × depth
    complexity_match = re.search(r'Complexity:\s+(\d+)', output)
    assert complexity_match, "CLI output should display complexity metric"
    complexity = int(complexity_match.group(1))
    assert complexity == concepts * depth, f"Complexity should be {concepts}×{depth}={concepts*depth}, got {complexity}"
    
    print(f"✅ PASS: CLI metrics verified (concepts={concepts}, depth={depth}, complexity={complexity})")

def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("DENSITY VALIDATION TEST SUITE")
    print("=" * 60)
    
    # Check test fixtures exist
    if not TEST_DIR.exists():
        print(f"\n❌ ERROR: Test fixtures directory not found: {TEST_DIR}")
        print("   Run this script from the todd-media directory")
        sys.exit(1)
    
    try:
        test_concise_prompts()
        test_standard_prompts()
        test_detailed_prompts()
        test_real_world_prompt()
        test_cli_output_metrics()
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED")
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
