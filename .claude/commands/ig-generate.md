# /generate-infographic: Automated Infographic Generation

**Purpose:** Fully automated infographic generation using Gemini API (Imagen)

**Workflow:**
1. Reads prompt.md and content.md
2. Generates 3 variants using Gemini API
3. Converts to WebP using todd-image-convert
4. Runs /ig-evaluate
5. If best score < 90%, generates next batch of 3
6. Repeats until 90%+ score achieved

**Free Tier:** 500 images/day (plenty for iterative generation)

---

## Quick Start

```bash
# Generate infographics for barriers
/generate-infographic docs/writing/1-transformation/visuals/barriers

# Generates:
# - barriers-1.png, barriers-2.png, barriers-3.png
# - Auto-converts to webp
# - Auto-evaluates
# - If score < 90%, prompts for next batch
```

---

## Setup (One-Time)

### 1. Install Gemini SDK

```bash
pip install google-generativeai
```

### 2. Get API Key

1. Go to https://aistudio.google.com/apikey
2. Create API key (free tier)
3. Copy key

### 3. Set Environment Variable

```bash
# Add to ~/.zshrc:
export GEMINI_API_KEY='your-api-key-here'

# Reload:
source ~/.zshrc
```

### 4. Verify Setup

```bash
python3 -c "import google.generativeai as genai; print('✅ Gemini SDK installed')"
echo $GEMINI_API_KEY  # Should show your key
```

---

## Usage

### Basic Generation

```bash
/generate-infographic <directory>

# Example:
/generate-infographic docs/writing/1-transformation/visuals/barriers
```

**Expected files in directory:**
- `barriers.prompt.md` (or `prompt.md`)
- `barriers.content.md` (or `content.md`)

**Generated files:**
- `barriers-1.png` through `barriers-3.png`
- `barriers-1.webp` through `barriers-3.webp`
- `barriers.eval.md` (evaluation report)

### With Custom Name

```bash
/generate-infographic docs/writing/.../timeline --name timeline

# Generates: timeline-1.png, timeline-2.png, timeline-3.png
```

### Iterative Generation (Until 90%+)

```bash
# First batch
/generate-infographic barriers/

# Review evaluation report
# If best score < 90%, run again for next batch:
/generate-infographic barriers/ --batch 2

# Repeat until 90%+ achieved
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

### Step 2: Generate with Gemini API

```python
# Combines prompt + content
combined = prompt.md + "\n\n" + content.md

# Calls Gemini 2.5 Flash Image API
model = genai.GenerativeModel('gemini-2.5-flash-image')
response = model.generate_content([combined])

# Saves: barriers-1.png, barriers-2.png, barriers-3.png
```

### Step 3: Convert to WebP

```bash
todd-image-convert barriers-*.png \
  --resolution 1080p \
  --output-format webp \
  --no-replace
```

### Step 4: Evaluate

```bash
# Calls /ig-evaluate skill
/ig-evaluate barriers/*.webp

# Generates: barriers.eval.md
```

### Step 5: Check Score

```
If best_score >= 90%:
  ✅ Done! Use winner
Else:
  🔄 Generate next batch of 3
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

## Free Tier Limits

**Daily Quota:** 500 images/day

**Realistic Usage:**
- 3 variants per batch
- ~5 batches max to reach 90% (15 images)
- Can generate ~30 infographic topics per day
- Perfect for EventAI curriculum (10-15 topics total)

**Cost:** $0 (free tier with small watermark)

**Paid Tier:** $0.039/image if free tier exhausted

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

## Gemini API Benefits

### Why Gemini vs Manual NotebookLM?

✅ **Fully automated** - zero manual clicking
✅ **Iterative** - generate batches until quality target met
✅ **Reproducible** - version-controlled prompts
✅ **Fast** - ~6 seconds per image
✅ **Free tier** - 500/day (plenty for EventAI)
✅ **Programmatic** - integrate with other tools
✅ **No UI** - direct filesystem writes

### NotebookLM Equivalence

**Same underlying model:**
- NotebookLM "Infographic" = Gemini 2.5 Flash Image
- Same quality, same capabilities
- API gives programmatic access

**Proof:** Generate side-by-side comparison shows identical results

---

## Troubleshooting

### Images Look Different Than NotebookLM

**Check model:**
- Use `gemini-2.5-flash-image` (not older models)
- Verify API key is active
- Check generation parameters

### Watermark on Images

**Free tier adds small Gemini sparkle watermark**

**Options:**
1. Accept watermark (barely visible)
2. Use paid tier ($0.039/image) - no watermark
3. Credit Gemini in acknowledgments (good practice anyway!)

### Generation Fails

**Common issues:**
1. API key expired → regenerate at aistudio.google.com
2. Rate limit hit → wait 60 seconds, retry
3. Daily quota exhausted → wait until midnight PT
4. Prompt too long → shorten prompt.md or content.md

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
- **`todd-image-convert`** - Image conversion
- **EventAI Visual Identity Guide** - Brand color palette and typography
- **Gemini API Documentation:** https://ai.google.dev/

---

*Skill created: December 29, 2025*
*Powered by: Gemini 2.5 Flash Image API (free tier)*
*Integration: EventAI + Lemmy Content Generation System*
