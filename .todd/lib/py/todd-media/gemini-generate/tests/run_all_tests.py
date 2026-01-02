#!/usr/bin/env python3
"""
Master test runner for density validation test suite.

Runs all tests:
1. Unit tests for structural analysis
2. Unit tests for validation logic
3. Integration tests for CLI validation

Usage:
    python3 tests/run_all_tests.py
    python3 tests/run_all_tests.py --verbose
"""

import sys
import subprocess
from pathlib import Path

def run_test_suite(script_name, description):
    """Run a test suite and return status."""
    print("\n" + "=" * 60)
    print(f"Running: {description}")
    print("=" * 60)
    
    script_path = Path(__file__).parent / script_name
    result = subprocess.run([sys.executable, str(script_path)], capture_output=False)
    
    return result.returncode == 0

def main():
    """Run all test suites."""
    verbose = '--verbose' in sys.argv
    
    print("\n" + "=" * 60)
    print("DENSITY VALIDATION - FULL TEST SUITE")
    print("=" * 60)
    print("\nRunning comprehensive tests for prompt/image validation...")
    
    suites = [
        ('test_prompt_analysis.py', 'Structural Analysis Unit Tests'),
        ('test_prompt_validation.py', 'Validation Logic Unit Tests'),
        ('test_image_validation.py', 'Image Validation Unit Tests (OCR)'),
        ('test_density_validation.py', 'CLI Integration Tests'),
    ]
    
    results = []
    
    for script, description in suites:
        passed = run_test_suite(script, description)
        results.append((description, passed))
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUITE SUMMARY")
    print("=" * 60)
    
    total = len(results)
    passed = sum(1 for _, p in results if p)
    
    for description, status in results:
        icon = "✅" if status else "❌"
        print(f"{icon} {description}")
    
    print("\n" + "=" * 60)
    
    if passed == total:
        print(f"✅ ALL TEST SUITES PASSED ({passed}/{total})")
        print("=" * 60)
        print("\n✨ Density validation system is working correctly!")
        sys.exit(0)
    else:
        print(f"❌ SOME TESTS FAILED ({passed}/{total} passed)")
        print("=" * 60)
        sys.exit(1)

if __name__ == '__main__':
    main()
