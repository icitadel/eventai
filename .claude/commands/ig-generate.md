# /generate-infographic: Automated Infographic Generation

**Purpose:** Fully automated infographic generation using Gemini web automation (Playwright)

**Workflow:**
1. Reads prompt.md and content.md from directory
2. Opens Gemini in Chrome browser with parallel tabs
3. Generates 3 variants simultaneously
4. Downloads PNG files
5. Converts to WebP using todd-image-convert
6. Ready for /ig-evaluate

**Method:** Browser automation via Playwright (not API - uses gemini.google.com directly)

---

## Information Density Tiers

**CRITICAL: EventAI uses three density tiers. Default to Standard tier unless explicitly requested.**

### The Three-Tier Framework

**1. Concise Tier** (Minimal Detail)
- Headlines + 3-5 key stats
- 15-30 second comprehension
- 40%+ white space
- **Use:** Social media, quick pitches
- **Example:** Title + "13x ROI, 8-9 month payback, $6.87M net benefit" (no breakdowns)

**2. Standard Tier** (Balanced Detail) **← DEFAULT**
- Key breakdowns with 3-4 components each
- 30-60 second comprehension
- 30% white space
- **Use:** Conference slides, blog posts, reports (most common)
- **Example:** Title + Investment breakdown (4 components w/ values) + Benefits breakdown (4 components w/ values) + ROI summary

**3. Detailed Tier** (Comprehensive)
- Explanatory annotations, case studies, year-by-year detail
- 2-3 minute comprehension
- 25%+ white space
- **Use:** Textbooks, MBA cases, training materials
- **Example:** Everything in Standard + explanatory text for each component + year-by-year progression + case study callout

**Unless user specifies tier, ALWAYS generate Standard tier prompts.**

---

## Quick Start

```bash
# The /ig-generate skill uses the gemini-generate CLI
gemini-generate \
  --content docs/writing/1-transformation/visuals/barriers/barriers.content.md \
  --prompt docs/writing/1-transformation/visuals/barriers/barriers.prompt.md \
  --output-dir docs/writing/1-transformation/visuals/barriers \
  --name barriers

# Generates 3 variants (typically at Standard tier density):
# - barriers-1.png, barriers-2.png, barriers-3.png
# - barriers-1.webp, barriers-2.webp, barriers-3.webp
# - Ready for /ig-evaluate
```

---

## Setup (One-Time)

### 1. Install CLI Tool

```bash
cd .todd/lib/py/todd-media
pip install -e .
```

This installs:
- `gemini-generate` CLI command (installed to `~/.local/bin/`)
- Playwright dependency for browser automation

### 2. Install Playwright Browsers

```bash
playwright install chromium
```

### 3. Verify Setup

```bash
which gemini-generate  # Should show ~/.local/bin/gemini-generate
gemini-generate --help # Should show usage
```

**Requirements:**
- Chrome browser with signed-in Google account
- Gemini access at gemini.google.com

---

## Usage

### Basic Generation

```bash
gemini-generate \
  --content path/to/content.md \
  --prompt path/to/prompt.md \
  --output-dir path/to/output \
  --name base-name

# Example:
gemini-generate \
  --content docs/writing/1-transformation/visuals/barriers/barriers.content.md \
  --prompt docs/writing/1-transformation/visuals/barriers/barriers.prompt.md \
  --output-dir docs/writing/1-transformation/visuals/barriers \
  --name barriers
```

**Required arguments:**
- `--content`: Path to content markdown file
- `--prompt`: Path to prompt/style instructions file
- `--output-dir`: Directory for generated files
- `--name`: Base filename for outputs

**Generated files:**
- `barriers-1.png` through `barriers-3.png`
- `barriers-1.webp` through `barriers-3.webp`

### Iterative Generation (Multiple Batches)

```bash
# First batch (generates #1-3)
gemini-generate --content barriers.content.md --prompt barriers.prompt.md \
  --output-dir ./barriers --name barriers --batch 1

# Second batch (generates #4-6)
gemini-generate --content barriers.content.md --prompt barriers.prompt.md \
  --output-dir ./barriers --name barriers --batch 2

# Each batch generates 3 new variants
```

### Optional Arguments

```bash
--variants 5          # Generate 5 instead of 3 (default: 3, max: 5)
--aspect-ratio portrait  # portrait, landscape (default), or square
--batch 2             # Batch number for iterative generation
--skip-webp           # Skip WebP conversion, keep PNGs only
--resolution 1080p    # WebP resolution (default: 1080p)
--chrome-profile ProfileName  # Use specific Chrome profile (default: Default)
```

---

## How It Works

### Step 1: Read Files

```
barriers/
  ├── barriers.prompt.md   ← Style instructions
  ├── barriers.content.md  ← Data/content
  └── (output files will be created here)
```

### Step 2: Browser Automation

```
1. Launches Chrome browser with user profile (already logged in)
2. Opens 3 parallel tabs to gemini.google.com
3. Enables "Create images" mode in each tab
4. Fills combined prompt + content into each tab
5. Submits all prompts simultaneously
6. Waits for image generation (typically 40-50s per variant)
7. Downloads generated PNGs sequentially
```

**Advantages over API:**
- No API key needed (uses your Google account)
- No rate limits or quotas (free unlimited use)
- Same quality as NotebookLM (uses Gemini Imagen)
- Parallel generation speeds up workflow

### Step 3: Convert to WebP

```bash
todd-image-convert barriers-*.png \
  --resolution 1080p \
  --output-format webp \
  --no-replace
```

### Step 4: Ready for Evaluation

```bash
# Run evaluation manually
/ig-evaluate

# Or use the CLI directly
# Generates: barriers.eval.md with scores
```

---

## Iterative Improvement Loop

**Goal:** Achieve 90%+ score through iteration

### Round 1: Initial Generation

```bash
/generate-infographic barriers/

# Output:
# - barriers-1.png (Score: 75%)
# - barriers-2.png (Score: 82%)  ← Best
# - barriers-3.png (Score: 78%)
#
# Best score: 82% < 90% → Continue
```

### Round 2: Learn and Regenerate

```bash
# Script updates prompt.md with learnings from barriers.eval.md
# Generates barriers-4, 5, 6

/generate-infographic barriers/ --batch 2

# Output:
# - barriers-4.png (Score: 85%)
# - barriers-5.png (Score: 91%)  ← Best ✅
# - barriers-6.png (Score: 87%)
#
# Best score: 91% >= 90% → DONE!
```

**Result:** barriers-5.webp is the winner (91%)

---

## No Limits - Free Unlimited Use

**Browser Automation Benefits:**
- ✅ No daily quotas or rate limits
- ✅ No API key required
- ✅ Free unlimited use (via your Google account)
- ✅ No watermarks
- ✅ Same quality as NotebookLM/Gemini web interface

**Realistic Usage:**
- 3 variants per batch (~95 seconds total)
- ~5 batches max to reach 90% (15 images, ~8 minutes)
- Can generate unlimited infographics per day
- Perfect for EventAI curriculum (10-15 topics total)

**Cost:** $0 (completely free via browser automation)

---

## File Naming Convention

**Generated files follow EventAI standard:**

```
barriers/
  ├── barriers.prompt.md
  ├── barriers.content.md
  ├── barriers.instructions.md
  ├── barriers.eval.md              ← Auto-generated
  ├── barriers-1.png                ← Generated (batch 1)
  ├── barriers-2.png
  ├── barriers-3.png
  ├── barriers-1.webp               ← Converted
  ├── barriers-2.webp
  ├── barriers-3.webp
  └── [If needed: barriers-4.png...] ← Batch 2
```

---

## Integration with Workflow

### Current Manual Workflow

1. Write content.md ✍️
2. Write prompt.md ✍️
3. Open NotebookLM 🖱️
4. Upload files 🖱️
5. Click "Infographic" 🖱️
6. Download PNGs 🖱️
7. Rename files ✍️
8. Convert to WebP ⚙️
9. Run /ig-evaluate ⚙️
10. Review and select 👀

**Total time:** ~20-30 minutes

### New Automated Workflow

1. Write content.md ✍️
2. Write prompt.md ✍️
3. Run: `/generate-infographic barriers/` ⚙️ (automated!)
4. Review evaluation, select winner 👀

**Total time:** ~5 minutes (75% faster!)

---

## Error Handling

### "GEMINI_API_KEY not set"

```bash
export GEMINI_API_KEY='your-key-here'
# Or add to ~/.zshrc permanently
```

### "google-generativeai not installed"

```bash
pip install google-generativeai
```

### "File not found: prompt.md"

**Expected names:**
- `{directory-name}.prompt.md` (e.g., `barriers.prompt.md`)
- OR `prompt.md` (fallback)

### "todd-image-convert failed"

**Check environment variables:**
```bash
export PYTHONPATH="/Users/ja/Documents/CodeProjects/todd-lab/.todd/lib/py/todd-media/image-converter:$PYTHONPATH"
export DYLD_LIBRARY_PATH="/opt/homebrew/opt/vips/lib:$DYLD_LIBRARY_PATH"
```

### "Rate limit exceeded"

**Free tier limits:**
- 500/day
- ~10/minute

**Wait and retry:**
- Script auto-pauses 6 seconds between generations
- If hit daily limit, try next day

---

## Advanced Usage

### Generate More Variants

```bash
# Default: 3 variants
/generate-infographic barriers/

# Custom: 5 variants (uses more quota)
/generate-infographic barriers/ --variants 5
```

### Custom Output Name

```bash
/generate-infographic barriers/ --name custom-barriers
# Generates: custom-barriers-1.png, custom-barriers-2.png, etc.
```

### Skip Conversion

```bash
# Generate PNGs only, skip WebP conversion
python3 .claude/scripts/generate-infographic.py barriers/ --skip-convert
```

---

## Quality Targets

**Evaluation Scores:**
- **< 70%:** Poor - major issues
- **70-79%:** Fair - significant improvements needed
- **80-89%:** Good - minor refinements recommended
- **90-94%:** Excellent - publication-ready
- **95-100%:** Outstanding - exceptional quality

**Target:** 90%+ (Excellent)

**Iterative approach ensures we hit target without over-generating**

---

## Browser Automation Benefits

### Why gemini-generate vs Manual NotebookLM/Gemini?

✅ **Fully automated** - zero manual clicking
✅ **Parallel generation** - 3 variants simultaneously (~95s total)
✅ **Iterative** - generate batches until quality target met
✅ **Reproducible** - version-controlled prompts
✅ **Unlimited** - no API quotas or rate limits
✅ **Free** - no API costs, uses your Google account
✅ **Programmatic** - integrate with other tools
✅ **Direct filesystem writes** - no manual downloads

### Gemini Web Interface Equivalence

**Same underlying model:**
- gemini.google.com "Create images" = Gemini Imagen
- Same quality as NotebookLM infographic generation
- Browser automation gives programmatic access
- No watermarks (unlike API free tier)

**Proof:** Identical output quality to manual generation

---

## Troubleshooting

### Browser Doesn't Launch

**Check installation:**
```bash
which gemini-generate  # Should show ~/.local/bin/gemini-generate
playwright install chromium  # Install browsers if missing
```

### Chrome Profile Not Found

**Common issue:** Profile name mismatch

```bash
# Find your Chrome profile names
ls ~/Library/Application\ Support/Google/Chrome/

# Use correct profile name
gemini-generate --chrome-profile "Profile 1" ...
```

### Image Mode Activation Warning

**Message:** `⚠️ Image mode activation failed`

**This is OK!** The warning appears but generation continues. The script attempts to enable image mode but will work even if already enabled.

### Generation Timeout

**If variants timeout after 60s:**
1. Check Gemini is accessible at gemini.google.com
2. Ensure you're logged into Google account
3. Try with fewer variants (--variants 1)
4. Check prompt length (very long prompts may slow generation)

### Download Fails

**If downloads fail:**
- Ensure Downloads folder is accessible
- Close other Chrome windows/tabs that might conflict
- Try again with --batch parameter to resume

---

## Best Practices Integration

### Recommended Pre-Generation Workflow

**For optimal results, load infographic best practices BEFORE creating prompts:**

```bash
# 1. Load Tufte principles and EventAI design standards
/infographics-bestpractices

# 2. Create prompt.md with loaded guidance
"Generate a NotebookLM-style prompt for VIS-X.X following Tufte's principles"

# Claude will automatically include:
# - Data-ink ratio optimization (minimal cruft)
# - EventAI color palette (purple, coral, blue, white)
# - Professional + whimsy balance (80% credible, 20% playful)
# - White space targets (30%+ composition)
# - Typography rules (two-font maximum)
# - Festival context (stages, crowds, wristbands)
# - Accessibility requirements (4.5:1 contrast)

# 3. Write content.md with source data
"Create content.md from VIS-X.X-source.md"

# 4. Run automated generation
/generate-infographic docs/writing/.../visuals/name/

# 5. Evaluation automatically uses loaded best practices
# → Tufte principles applied to scoring
# → EventAI brand compliance checked
# → Accessibility verified
```

### Why Load Best Practices First?

**Without `/infographics-bestpractices`:**
- Generic prompt creation (no Tufte principles)
- Missing EventAI color palette specifications
- No white space or cruft guidance
- Evaluation uses basic criteria only

**With `/infographics-bestpractices`:**
- ✅ Prompts include data-ink ratio requirements
- ✅ EventAI palette hex codes specified
- ✅ Professional + whimsy balance articulated
- ✅ Minimal cruft explicitly stated
- ✅ Evaluation scores against Tufte standards
- ✅ Higher quality output on first generation

### Quality Improvement Example

**Before (without best practices loaded):**
```markdown
# barriers.prompt.md
Create an infographic showing barriers to AI adoption.
Use EventAI colors. Make it professional but fun.
```
→ **Result:** 72% score (vague guidance, generic design)

**After (with /infographics-bestpractices loaded):**
```markdown
# barriers.prompt.md
Create an information-dense infographic showing barriers to AI adoption.

CRITICAL REQUIREMENTS:
- Deep purple (#6B46C1), electric coral (#FF6B6B), sky blue (#4299E1)
- Data-ink ratio: minimal decoration, every element serves information
- 30%+ white space for breathing room
- Festival context (academic setting with event-relevant metaphors)
- Professional foundation (clean structure) + whimsy accents (unexpected colors)
- No decorative borders, gradients, or ornamental shapes
- 4.5:1 minimum contrast ratio, non-color-dependent information
- Maximum 2 font families: clean sans-serif for body
```
→ **Result:** 89% score (first generation near target!)

---

## See Also

- **`/infographics-bestpractices`** - Load Tufte principles and EventAI design standards (USE BEFORE /ig-generate!)
- **`/ig-evaluate`** - Evaluation workflow (automatically uses loaded best practices)
- **`gemini-generate`** - The CLI tool (installed from `.todd/lib/py/todd-media/setup.py`)
- **`todd-image-convert`** - Image conversion to WebP
- **EventAI Visual Identity Guide** - Brand color palette and typography
- **Gemini Web Interface:** https://gemini.google.com

---

*Skill created: December 29, 2025*
*Powered by: Gemini Imagen via browser automation (Playwright)*
*Method: Parallel tab generation at gemini.google.com*
*CLI: gemini-generate (installed from .todd/lib/py/todd-media)*
*Integration: EventAI + Lemmy Content Generation System*
