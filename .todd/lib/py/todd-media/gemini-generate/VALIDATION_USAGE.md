# Density Validation CLI Usage Guide

Quick reference for validating prompts and infographics against density tiers.

## Basic Usage

### Validate a Prompt File

```bash
python3 gemini_generate.py \
  --validate-prompt <path-to-prompt.md> \
  --density <tier>
```

**Example:**
```bash
python3 gemini_generate.py \
  --validate-prompt docs/writing/4-privacy/visuals/consent-spectrum/consent-spectrum.prompt.md \
  --density concise
```

**Output:**
```
📊 Validating prompt: consent-spectrum.prompt.md
🎯 Target tier: concise

============================================================
✅ VALID: CONCISE TIER
============================================================

📈 Structural Metrics:
  Concepts: 6 (expected: 5-8)
    - Sections (## headings): 3
    - Top-level bullets: 3
  Depth: 2 levels (expected: 1-2)
    - Max heading depth: 2
    - Max list nesting: 2
  Complexity: 12 (concepts × depth)
```

### Validate an Infographic Image

```bash
python3 gemini_generate.py \
  --validate-image <path-to-image.webp> \
  --density <tier>
```

**Example:**
```bash
python3 gemini_generate.py \
  --validate-image docs/writing/4-privacy/visuals/consent-spectrum/consent-spectrum-4.webp \
  --density concise
```

**Output:**
```
🖼️  Validating infographic: consent-spectrum-4.webp
🎯 Target tier: concise

============================================================
✅ VALID: CONCISE TIER
============================================================

📈 OCR-Based Metrics:
  Concepts: 7 (expected: 5-8)
  Depth: 2 hierarchy levels (expected: 1-2)
  Complexity: 14 (concepts × depth)
  Text blocks extracted: 23
```

## Tier Options

### Concise Tier

**Target:** 5-8 concepts, 1-2 levels deep
```bash
--density concise
```

**Example prompts:**
- Simple bar charts (5 categories)
- Basic comparisons (3-4 items)
- Quick reference (labels + values only)

### Standard Tier (Default)

**Target:** EITHER breadth (10-15 concepts, 1-2 levels) OR depth (5-8 concepts, 3 levels)
```bash
--density standard
```

**Example prompts:**
- Timelines with many data points (breadth)
- Detailed comparison charts (depth)
- Multi-category breakdowns

### Detailed Tier

**Target:** 20-30+ concepts, 4+ levels deep
```bash
--density detailed
```

**Example prompts:**
- Comprehensive system diagrams
- Multi-layered explanations with examples
- Educational annotations with case studies

## Exit Codes

- **0** = Valid (prompt/image matches tier)
- **1** = Invalid (prompt/image does NOT match tier)

Use in scripts:
```bash
if python3 gemini_generate.py --validate-prompt my-prompt.md --density concise; then
    echo "Prompt is valid!"
    # Proceed with generation
else
    echo "Prompt doesn't match Concise tier, revise and try again"
    exit 1
fi
```

## Understanding Output

### Success Output (✅ VALID)

```
============================================================
✅ VALID: CONCISE TIER
============================================================

📈 Structural Metrics:
  Concepts: 6 (expected: 5-8)    ← Within range ✅
    - Sections (## headings): 3
    - Top-level bullets: 3
  Depth: 2 levels (expected: 1-2) ← Within range ✅
    - Max heading depth: 2
    - Max list nesting: 2
  Complexity: 12 (concepts × depth)
```

**Means:** All metrics are within expected ranges for the tier.

### Failure Output (❌ INVALID)

```
============================================================
❌ INVALID: CONCISE TIER
============================================================

📈 Structural Metrics:
  Concepts: 15 (expected: 5-8)    ← TOO MANY ❌
    - Sections (## headings): 8
    - Top-level bullets: 7
  Depth: 3 levels (expected: 1-2) ← TOO DEEP ❌
    - Max heading depth: 3
    - Max list nesting: 2
  Complexity: 45 (concepts × depth)

⚠️  Issues:
  - Too many concepts: 15 > 8
  - Too deep: 3 > 2 levels
```

**Means:** One or more metrics are outside expected ranges. Fix by:
- Reducing number of ## sections or top-level bullets (too many concepts)
- Flattening nested lists or reducing heading depth (too deep)

### Standard Tier Variant Detection

```
============================================================
✅ VALID: STANDARD TIER
============================================================

📈 Structural Metrics:
  Concepts: 13 (expected: 10-15 OR 5-8)
  Depth: 2 levels (expected: 1-2 OR 3)
  Complexity: 26 (concepts × depth)

💡 Standard tier variant: breadth
   Strategy: Wide (many concepts, shallow depth)
```

**Means:** Standard tier can be achieved via breadth OR depth. This prompt uses breadth strategy (many concepts, shallow depth).

## Common Use Cases

### 1. Validate Before Generation

```bash
# Validate prompt is Concise tier
python3 gemini_generate.py \
  --validate-prompt my-prompt.md \
  --density concise

# If valid, generate infographic
python3 gemini_generate.py \
  --content content.md \
  --prompt my-prompt.md \
  --density concise \
  --output-dir output/
```

### 2. Test Tier Compliance After Editing

```bash
# After editing consent-spectrum.prompt.md
python3 gemini_generate.py \
  --validate-prompt docs/writing/4-privacy/visuals/consent-spectrum/consent-spectrum.prompt.md \
  --density concise
```

### 3. Verify Generated Infographic Matches Tier

```bash
# After generating infographic
python3 gemini_generate.py \
  --validate-image output/my-infographic-1.webp \
  --density concise
```

### 4. Batch Validation

```bash
# Validate all prompts in a directory
for f in docs/writing/*/visuals/*/prompt.md; do
    echo "Testing: $f"
    python3 gemini_generate.py --validate-prompt "$f" --density concise
done
```

## Integration with /test-visual-prompt-density Command

The CLI validation is designed to work with the `/test-visual-prompt-density` command:

**Step 1: CLI Static Analysis**
```bash
python3 gemini_generate.py \
  --validate-prompt consent-spectrum.prompt.md \
  --density concise
```

**Step 2: AI Agentic Analysis**
```
/test-visual-prompt-density consent-spectrum.prompt.md concise
```

Combined, these provide:
- **CLI:** Fast structural analysis (concepts, depth, complexity)
- **AI:** Semantic analysis (philosophy, detail level appropriateness)

## Troubleshooting

### Error: File Not Found

```
❌ Error during validation: [Errno 2] No such file or directory: 'my-prompt.md'
```

**Fix:** Use absolute path or ensure you're in correct directory:
```bash
python3 gemini_generate.py \
  --validate-prompt "$(pwd)/docs/writing/.../my-prompt.md" \
  --density concise
```

### Error: Too Few Concepts

```
⚠️  Issues:
  - Too few concepts: 3 < 5
```

**Fix:** Add more ## sections or top-level bullets to reach minimum concept count.

### Error: Too Many Concepts

```
⚠️  Issues:
  - Too many concepts: 18 > 8
```

**Fix:** Either:
- Reduce number of ## sections or top-level bullets
- Or use a higher tier (Standard or Detailed)

### Error: Too Deep

```
⚠️  Issues:
  - Too deep: 4 > 2 levels
```

**Fix:** Flatten nested lists or reduce heading depth (#### → ##).

## Running Automated Tests

```bash
# From todd-media directory
cd .todd/lib/py/todd-media

# Run all tests
./tests/run_tests.sh

# Or run individual test suites
python3 tests/test_prompt_analysis.py
python3 tests/test_prompt_validation.py
python3 tests/test_density_validation.py
```

See [tests/TESTING.md](tests/TESTING.md) for comprehensive testing guide.

---

*Last updated: January 1, 2026*
*See also: .claude/commands/test-visual-prompt-density.md*
