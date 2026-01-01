#!/usr/bin/env python3
"""
Unit tests for variant number auto-detection.

Tests that get_next_variant_number() correctly scans output directories
and determines the next available variant number.
"""

import sys
import tempfile
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from gemini_generate import get_next_variant_number

def test_empty_directory():
    """Test that empty directory returns 1."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = get_next_variant_number(Path(tmpdir), 'consent-spectrum')
        assert result == 1, f"Empty directory should return 1, got {result}"

    print("✅ PASS: test_empty_directory")

def test_nonexistent_directory():
    """Test that nonexistent directory returns 1."""
    result = get_next_variant_number(Path('/nonexistent/path/xyz'), 'consent-spectrum')
    assert result == 1, f"Nonexistent directory should return 1, got {result}"

    print("✅ PASS: test_nonexistent_directory")

def test_sequential_variants():
    """Test with sequential variants 1-7."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = Path(tmpdir)

        # Create files: consent-spectrum-1.png through consent-spectrum-7.webp
        for i in range(1, 8):
            ext = 'png' if i % 2 == 1 else 'webp'
            (tmppath / f'consent-spectrum-{i}.{ext}').touch()

        result = get_next_variant_number(tmppath, 'consent-spectrum')
        assert result == 8, f"With variants 1-7, should return 8, got {result}"

    print("✅ PASS: test_sequential_variants")

def test_gaps_in_numbering():
    """Test with gaps in variant numbers."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = Path(tmpdir)

        # Create files with gaps: 1, 3, 7, 12
        for i in [1, 3, 7, 12]:
            (tmppath / f'consent-spectrum-{i}.png').touch()

        result = get_next_variant_number(tmppath, 'consent-spectrum')
        assert result == 13, f"With max variant 12, should return 13, got {result}"

    print("✅ PASS: test_gaps_in_numbering")

def test_mixed_png_and_webp():
    """Test with both PNG and WebP files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = Path(tmpdir)

        # Create mixed files
        (tmppath / 'consent-spectrum-5.png').touch()
        (tmppath / 'consent-spectrum-8.webp').touch()
        (tmppath / 'consent-spectrum-3.png').touch()
        (tmppath / 'consent-spectrum-10.webp').touch()

        result = get_next_variant_number(tmppath, 'consent-spectrum')
        assert result == 11, f"With max variant 10, should return 11, got {result}"

    print("✅ PASS: test_mixed_png_and_webp")

def test_different_base_names():
    """Test that only files with matching base name are counted."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = Path(tmpdir)

        # Create files with different base names
        (tmppath / 'consent-spectrum-1.png').touch()
        (tmppath / 'consent-spectrum-2.png').touch()
        (tmppath / 'privacy-matrix-5.png').touch()  # Different base name
        (tmppath / 'consent-spectrum-3.png').touch()
        (tmppath / 'other-file-10.webp').touch()  # Different base name

        result = get_next_variant_number(tmppath, 'consent-spectrum')
        assert result == 4, f"With consent-spectrum 1-3, should return 4, got {result}"

        # Test with different base name
        result2 = get_next_variant_number(tmppath, 'privacy-matrix')
        assert result2 == 6, f"With privacy-matrix max 5, should return 6, got {result2}"

    print("✅ PASS: test_different_base_names")

def test_ignores_non_matching_files():
    """Test that non-matching files are ignored."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = Path(tmpdir)

        # Create matching files
        (tmppath / 'consent-spectrum-1.png').touch()
        (tmppath / 'consent-spectrum-2.png').touch()

        # Create non-matching files (should be ignored)
        (tmppath / 'consent-spectrum.png').touch()  # No number
        (tmppath / 'consent-spectrum-draft.png').touch()  # Text suffix
        (tmppath / 'consent-spectrum-3.jpg').touch()  # Wrong extension
        (tmppath / 'consent-spectrum-4-final.png').touch()  # Extra suffix
        (tmppath / 'README.md').touch()  # Unrelated file

        result = get_next_variant_number(tmppath, 'consent-spectrum')
        assert result == 3, f"Should only count exact matches, expected 3, got {result}"

    print("✅ PASS: test_ignores_non_matching_files")

def test_large_numbers():
    """Test with large variant numbers."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = Path(tmpdir)

        # Create files with large numbers
        (tmppath / 'consent-spectrum-100.png').touch()
        (tmppath / 'consent-spectrum-250.webp').touch()
        (tmppath / 'consent-spectrum-1000.png').touch()

        result = get_next_variant_number(tmppath, 'consent-spectrum')
        assert result == 1001, f"With max variant 1000, should return 1001, got {result}"

    print("✅ PASS: test_large_numbers")

def test_special_characters_in_base_name():
    """Test with special characters in base name."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = Path(tmpdir)

        # Create files with special characters in base name
        base_name = 'consent-spectrum-v2.0'
        (tmppath / f'{base_name}-1.png').touch()
        (tmppath / f'{base_name}-2.png').touch()
        (tmppath / f'{base_name}-5.webp').touch()

        result = get_next_variant_number(tmppath, base_name)
        assert result == 6, f"With max variant 5, should return 6, got {result}"

    print("✅ PASS: test_special_characters_in_base_name")

def main():
    """Run all unit tests."""
    print("\n" + "=" * 60)
    print("VARIANT NUMBER AUTO-DETECTION TESTS")
    print("=" * 60)

    try:
        test_empty_directory()
        test_nonexistent_directory()
        test_sequential_variants()
        test_gaps_in_numbering()
        test_mixed_png_and_webp()
        test_different_base_names()
        test_ignores_non_matching_files()
        test_large_numbers()
        test_special_characters_in_base_name()

        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED (9/9)")
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
