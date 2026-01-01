# Gemini Infographic Generator & Density Validation

Automated infographic generation using Gemini with density tier validation.

## Directory Structure

```
gemini-generate/
├── gemini_generate.py          # Main CLI tool (generation + validation)
├── tests/                      # Automated test suite (23 tests)
│   ├── run_all_tests.py       # Master test runner
│   ├── run_tests.sh           # Shell wrapper
│   ├── test_prompt_analysis.py      # Unit: structural analysis
│   ├── test_prompt_validation.py    # Unit: validation logic
│   ├── test_density_validation.py   # Integration: CLI
│   ├── fixtures/              # Test examples (prompts)
│   └── TESTING.md             # Testing guide
├── package.json               # npm scripts for tests
├── VALIDATION_USAGE.md        # CLI validation usage guide
└── README.md                  # This file
```

## Quick Start

### Generate Infographics

```bash
# Generate 3 variants (Concise tier)
python3 gemini_generate.py \
  --content source-content.md \
  --prompt infographic-prompt.md \
  --output-dir output/ \
  --name my-infographic \
  --density concise \
  --variants 3
```

### Validate Prompts/Images

```bash
# Validate prompt against tier
python3 gemini_generate.py \
  --validate-prompt my-prompt.md \
  --density concise

# Validate infographic image
python3 gemini_generate.py \
  --validate-image my-infographic.webp \
  --density concise
```

### Run Tests

```bash
# Using npm (recommended)
npm test

# Or directly with Python
python3 tests/run_all_tests.py

# Or with shell wrapper
./tests/run_tests.sh
```

## Features

### 1. Infographic Generation

- **Parallel generation:** Creates multiple variants simultaneously using browser tabs
- **Density tiers:** Concise (minimal) / Standard (balanced) / Detailed (comprehensive)
- **Auto WebP conversion:** Generates PNG and converts to optimized WebP
- **Complexity analysis:** Validates prompts against tier specifications

### 2. Density Validation

- **Prompt validation:** Structural analysis (concepts × hierarchy depth)
- **Image validation:** OCR-based analysis (requires Tesseract)
- **Three-tier system:**
  - **Concise:** 5-8 concepts, 1-2 levels deep
  - **Standard:** EITHER 10-15 concepts (breadth) OR 5-8 concepts at 3 levels (depth)
  - **Detailed:** 20-30+ concepts, 4+ levels deep
- **CLI + AI analysis:** Static structural metrics + semantic tier appropriateness

### 3. Automated Testing

- **23 automated tests:** Unit tests (analysis + validation) + integration tests (CLI)
- **Test fixtures:** Example prompts for all density tiers
- **Coverage:** Concept counting, depth detection, tier validation, CLI interface

## Usage Examples

### Example 1: Generate Concise Tier Infographic

```bash
python3 gemini_generate.py \
  --content docs/writing/4-privacy/visuals/consent-spectrum/consent-spectrum.content.md \
  --prompt docs/writing/4-privacy/visuals/consent-spectrum/consent-spectrum.prompt.md \
  --output-dir docs/writing/4-privacy/visuals/consent-spectrum/ \
  --name consent-spectrum \
  --density concise \
  --variants 3
```

### Example 2: Validate Prompt Before Generation

```bash
# Validate prompt is Concise tier
python3 gemini_generate.py \
  --validate-prompt consent-spectrum.prompt.md \
  --density concise

# If valid (exit code 0), proceed with generation
if [ $? -eq 0 ]; then
    python3 gemini_generate.py --content ... --prompt ... --density concise
fi
```

### Example 3: Batch Validation

```bash
# Validate all prompts in directory
for f in docs/writing/*/visuals/*/prompt.md; do
    echo "Validating: $f"
    python3 gemini_generate.py --validate-prompt "$f" --density concise
done
```

## Density Tier Framework

### Concept Count × Hierarchy Depth

**Complexity = Concepts × Depth**

**Primary Metrics:**
- **Concept count:** How many distinct ideas/requirements?
- **Hierarchy depth:** How many levels deep per concept?

**Tier Specifications:**

| Tier | Concepts | Depth | Strategy |
|------|----------|-------|----------|
| **Concise** | 5-8 | 1-2 levels | Few concepts, shallow depth |
| **Standard (Breadth)** | 10-15 | 1-2 levels | Many concepts, shallow depth |
| **Standard (Depth)** | 5-8 | 3 levels | Few concepts, deeper explanations |
| **Detailed** | 20-30+ | 4+ levels | Many concepts AND deep detail |

**Example (Concise):**
- ✅ "DEFAULT OPT-IN" (label only) = 1 level
- ⚠️ "DEFAULT OPT-IN - biometric on unless disabled" = 2 levels (pushing Standard)

## CLI Arguments

### Generation Mode

```
--content <file>          Source content file
--prompt <file>           Infographic prompt file
--output-dir <dir>        Output directory (default: current)
--name <name>             Base filename (default: infographic)
--variants <1-5>          Number of variants (default: 1)
--aspect-ratio <ratio>    landscape|portrait|square (default: landscape)
--density <tier>          concise|standard|detailed (default: standard)
--batch <num>             Batch number (for sequential numbering)
--skip-webp               Skip WebP conversion
--resolution <res>        WebP resolution (default: 1080p)
--chrome-profile <name>   Chrome profile (default: Default)
```

### Validation Mode

```
--validate-prompt <file>  Validate prompt against tier
--validate-image <file>   Validate infographic against tier
--density <tier>          Tier to validate against (required)
```

## Dependencies

### Python (Required)

```bash
pip3 install playwright
playwright install chromium
```

### OCR (Optional - for image validation)

```bash
# macOS
brew install tesseract
pip3 install pytesseract pillow scikit-learn

# Ubuntu/Debian
sudo apt-get install tesseract-ocr
pip3 install pytesseract pillow scikit-learn
```

## Exit Codes

- **0:** Success (generation complete, or validation passed)
- **1:** Failure (generation failed, or validation failed)

## Testing

See [tests/TESTING.md](tests/TESTING.md) for comprehensive testing guide.

**Quick test:**
```bash
npm test
```

## Documentation

- [VALIDATION_USAGE.md](VALIDATION_USAGE.md) - CLI validation usage guide
- [tests/TESTING.md](tests/TESTING.md) - Testing guide
- [tests/fixtures/README.md](tests/fixtures/README.md) - Test fixture documentation
- [/.claude/commands/test-visual-prompt-density.md](/.claude/commands/test-visual-prompt-density.md) - AI + CLI validation workflow

## Integration with EventAI Workflow

### Typical Workflow

1. **Create prompt** following tier guidelines
2. **Validate prompt** against tier
3. **Generate variants** (3 recommended)
4. **Convert to WebP** (automatic)
5. **Evaluate variants** using `/ig-evaluate`
6. **Select winner** and publish

### Beads Integration

```bash
# Create task
bd create --title="Generate VIS-X.X infographics" --type=task --priority=2

# Generate and validate
python3 gemini_generate.py --content ... --prompt ... --density concise

# Mark complete
bd close <beads-id>
```

## Troubleshooting

### Playwright/Chrome Issues

```bash
# Reinstall browser
playwright install chromium --force

# Specify different profile
python3 gemini_generate.py ... --chrome-profile "Profile 1"
```

### Validation Fails

```
❌ INVALID: CONCISE TIER
⚠️  Issues:
  - Too many concepts: 15 > 8
```

**Fix:** Reduce number of ## sections or top-level bullets in prompt.

### Test Failures

```bash
# Run individual test suite to isolate issue
npm run test:analysis
npm run test:validation
npm run test:integration
```

---

*Last updated: January 1, 2026*
*Part of: EventAI Lemmy Content Generation System*
