#!/bin/bash
# Quick test runner for density validation tests

set -e

cd "$(dirname "$0")/.."

echo ""
echo "════════════════════════════════════════════════════════════"
echo "  DENSITY VALIDATION TEST SUITE"
echo "════════════════════════════════════════════════════════════"
echo ""

python3 tests/run_all_tests.py "$@"
