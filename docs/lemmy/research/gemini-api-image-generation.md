# Gemini API for Programmatic Image Generation

**Discovery Date:** December 29, 2025
**Discovery:** NotebookLM's "Infographic" button uses Gemini (Imagen/Nano Banana Core) under the hood

---

## Key Insight

**NotebookLM Infographic Generation = Gemini API Image Generation**

When we click "Infographic" in NotebookLM with our detailed prompts, it's essentially:
1. Taking our prompt.md + content.md as context
2. Feeding it to Gemini's image generation model (Imagen 3 or Nano Banana)
3. Generating the infographic

**This means we can automate the entire process from Claude Code!**

---

## Proposed Workflow

### Option 1: Gemini API Direct (Preferred if available)

```bash
# From Claude Code, programmatically:
1. Read prompt.md (style instructions)
2. Read content.md (data/content)
3. Call Gemini API with combined context
4. Generate N variants
5. Save as PNG/WebP
6. Auto-run /ig-evaluate on all variants
```

**Advantages:**
- Fully automated from Claude Code
- No manual NotebookLM clicking
- Can generate 10+ variants in one go
- Reproducible, version-controlled prompts
- Can iterate rapidly

**Requirements:**
- Gemini API access
- Check if there's a free tier
- API key setup
- Image generation endpoint knowledge

### Option 2: Playwright Automation (Fallback)

If no free API tier or API limits are too restrictive:

```bash
# Automate Gemini UI via Playwright:
1. Navigate to ai.google.dev or Gemini UI
2. Upload prompt.md + content.md
3. Click "Generate image" or equivalent
4. Download generated images
5. Auto-run /ig-evaluate
```

**Advantages:**
- Works without API access
- Can use existing Gemini account
- Fully automated still

**Disadvantages:**
- Slower than API
- Fragile to UI changes
- Rate limiting via UI throttling

---

## Implementation Plan

### Phase 1: Research (Immediate)

- [ ] **Check Gemini API documentation**
  - Does it support image generation?
  - What's the endpoint?
  - What's the pricing/free tier?
  - What's the rate limit?

- [ ] **Test Gemini API image generation**
  - Simple prompt test
  - Complex infographic test
  - Compare output to NotebookLM

- [ ] **Verify equivalence**
  - NotebookLM output == Gemini API output?
  - Same model/quality?
  - Any differences in capabilities?

### Phase 2: Integration (Short-term)

- [ ] **Create `/generate-infographic` skill**
  - Input: prompt.md + content.md
  - Output: N variant images
  - Auto-convert to WebP 1080p
  - Auto-run /ig-evaluate

- [ ] **Update Lemmy workflow**
  - Replace manual NotebookLM step
  - Automate end-to-end: content → images → evaluation → selection

- [ ] **Add to EventAI curriculum generation**
  - One command generates all visuals for a topic
  - Full automation of visual content pipeline

### Phase 3: Enhancement (Long-term)

- [ ] **Prompt optimization feedback loop**
  - /ig-evaluate finds issues
  - Auto-update prompt.md with improvements
  - Regenerate until quality threshold met

- [ ] **Variant diversity controls**
  - Generate multiple layout types (radial, list, comparison)
  - Different color schemes
  - Various icon styles

- [ ] **Integration with beads workflow**
  - `bd create --title="Generate VIS-1.3 infographics"` → auto-generates and evaluates

---

## API Research Notes

### Gemini Models with Image Generation

**Gemini 2.0 Flash Experimental:**
- Multimodal (text + image input/output)
- Image generation capabilities
- Free tier available? (TO VERIFY)

**Imagen 3:**
- Google's latest image generation model
- High quality, photorealistic
- Pricing? (TO VERIFY)

**Nano Banana (if separate):**
- NotebookLM's infographic engine
- Specialized for diagrams/infographics?
- Access method? (TO VERIFY)

### API Endpoints (To Research)

```python
# Hypothetical API call:
import google.generativeai as genai

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

# Generate image from prompt
response = model.generate_images(
    prompt=combined_prompt,
    context=content_markdown,
    num_images=5,
    aspect_ratio="16:9",
    style="infographic"
)

for i, image in enumerate(response.images):
    image.save(f"barriers-{i+1}.png")
```

**To verify:**
- Correct model name
- Image generation method
- Parameter options
- Output format

---

## Benefits of Automation

### Current Manual Workflow

```
1. Write content.md (manual)
2. Write prompt.md (manual)
3. Open NotebookLM (manual)
4. Upload files (manual)
5. Click "Infographic" (manual)
6. Wait for generation (manual)
7. Download PNG (manual)
8. Rename files (manual)
9. Convert to WebP (semi-automated)
10. Run /ig-evaluate (semi-automated)
11. Review evaluation (manual)
12. Select winner (manual)
```

**Total time:** ~20-30 minutes per visual

### Proposed Automated Workflow

```
1. Write content.md (manual)
2. Write prompt.md (manual)
3. Run: /generate-infographic barriers/*.md (automated)
   - Generates 10 variants
   - Converts to WebP
   - Runs /ig-evaluate
   - Produces evaluation report
4. Review evaluation (manual)
5. Select winner (manual)
```

**Total time:** ~5 minutes per visual (75% reduction!)

### At Scale

**Current:** 10 visuals = 200-300 minutes (3-5 hours)
**Automated:** 10 visuals = 50 minutes (< 1 hour)

**Compound benefits:**
- Faster iteration (can regenerate easily)
- More variants (10+ instead of 3-5)
- Better quality (more options to choose from)
- Reproducible (version-controlled prompts)
- Learnings captured (prompt improvements automated)

---

## Integration Points

### 1. /ig-evaluate Enhancement

Current: Manual conversion + manual evaluation
Future: Auto-detect PNGs → auto-convert → auto-evaluate

```bash
# Instead of:
todd-image-convert *.png --resolution 1080p --output-format webp --no-replace
/ig-evaluate *.webp

# Just:
/ig-evaluate *.png  # Handles conversion internally
```

### 2. /generate-infographic Skill (New)

```bash
/generate-infographic docs/writing/1-transformation/visuals/barriers/

# Reads:
# - barriers.content.md
# - barriers.prompt.md

# Generates:
# - barriers-1.png through barriers-10.png
# - Auto-converts to webp
# - Auto-runs /ig-evaluate
# - Outputs: barriers.eval.md

# One command, full pipeline!
```

### 3. Lemmy Workflow Update

**Before:**
```markdown
## VIS-1.3: Generate Infographics

1. Open NotebookLM
2. Upload barriers.content.md
3. Click "Infographic"
4. Download and rename
5. Convert to WebP
6. Evaluate
7. Select winner
```

**After:**
```markdown
## VIS-1.3: Generate Infographics

1. Run: /generate-infographic barriers/
2. Review: barriers.eval.md
3. Select winner
```

---

## Questions to Answer

### API Access

- [ ] Does Gemini API support image generation?
- [ ] Is there a free tier? What are the limits?
- [ ] What's the pricing for paid tier?
- [ ] Can we use existing Google account?
- [ ] Are there academic/research discounts?

### Technical Feasibility

- [ ] Can we pass markdown context like NotebookLM?
- [ ] Can we control style/format like "infographic"?
- [ ] Can we generate multiple variants in one call?
- [ ] What's the generation time per image?
- [ ] Are there size/resolution controls?

### Quality Parity

- [ ] NotebookLM output == Gemini API output?
- [ ] Same model (Imagen 3 vs Nano Banana)?
- [ ] Any quality differences?
- [ ] Can we get better results with API fine-tuning?

### Workflow Integration

- [ ] How to structure prompts for API vs NotebookLM?
- [ ] Can we use same prompt.md files?
- [ ] How to handle multi-page context?
- [ ] Error handling for failed generations?

---

## Next Steps

**Immediate (This Week):**
1. Research Gemini API documentation
2. Test basic image generation
3. Compare to NotebookLM output
4. Document findings

**Short-term (Next Sprint):**
1. Build /generate-infographic prototype
2. Test on barriers regeneration
3. Validate quality parity
4. Measure time savings

**Long-term (Next Month):**
1. Integrate into Lemmy workflow
2. Auto-generate all EventAI visuals
3. Build feedback loop (evaluation → prompt improvement)
4. Scale to entire curriculum

---

## Success Criteria

**Phase 1 (Research) Success:**
- ✅ Confirmed API supports image generation
- ✅ Quality parity with NotebookLM verified
- ✅ Pricing acceptable (free tier or reasonable cost)

**Phase 2 (Prototype) Success:**
- ✅ /generate-infographic generates 10 variants
- ✅ Auto-conversion to WebP works
- ✅ Auto-evaluation produces accurate reports
- ✅ Time savings: 50%+ vs manual workflow

**Phase 3 (Production) Success:**
- ✅ All EventAI visuals generated via automation
- ✅ Quality meets or exceeds manual workflow
- ✅ Time savings: 75%+ vs manual workflow
- ✅ Reproducible, version-controlled process

---

## References

**Gemini API:**
- https://ai.google.dev/
- https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api

**NotebookLM:**
- https://notebooklm.google.com/

**Related Workflows:**
- `/ig-evaluate` - Infographic evaluation
- `todd-image-convert` - Image conversion
- Lemmy content generation system

---

*Discovery documented: December 29, 2025*
*Impact: HIGH - Potential 75% time savings on visual generation*
*Next: Research Gemini API capabilities and pricing*
