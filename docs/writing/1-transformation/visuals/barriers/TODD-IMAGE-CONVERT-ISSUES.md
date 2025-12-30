# todd-image-convert: Issues & Fixes Required

**Date:** December 29, 2025
**Context:** /ig-evaluate workflow requires todd-image-convert, discovered multiple issues

---

## Critical Issues Found

### 1. Environment Variables Not Set ❌

**Problem:** todd-image-convert requires PYTHONPATH and DYLD_LIBRARY_PATH but these aren't set globally

**Error:**
```
ModuleNotFoundError: No module named 'todd_media.image_converter'
```

**Current Workaround:**
```bash
export PYTHONPATH="/Users/ja/Documents/CodeProjects/todd-lab/.todd/lib/py/todd-media/image-converter:$PYTHONPATH"
export DYLD_LIBRARY_PATH="/opt/homebrew/opt/vips/lib:$DYLD_LIBRARY_PATH"
todd-image-convert [args]
```

**Permanent Fix Needed:**
- Add these exports to shell profile (.zshrc or .bashrc)
- OR create wrapper script that sets vars automatically
- OR fix Python package installation to include proper paths

---

### 2. Argument Syntax - RESOLVED ✅

**Correct Syntax (Confirmed):**
- `--replace` = overwrite existing files (for updating/replacing visuals)
- `--no-replace` = skip existing files silently (for new visuals)

**Implementation:**
```python
# In cli.py line 58-63:
parser.add_argument(
    "--replace",
    action=argparse.BooleanOptionalAction,
    default=None,
    help="Replace existing outputs...",
)
```

**Usage:**
```bash
# For NEW visuals (skip existing files silently):
todd-image-convert *.png --resolution 1080p --output-format webp --no-replace

# For UPDATING/REPLACING visuals (overwrite existing):
todd-image-convert *.png --resolution 1080p --output-format webp --replace
```

**Status:** ✅ Working as designed - no changes needed

---

### 3. Package Reinstallation Required After Changes ⚠️

**Problem:** Local changes to todd-image-converter code don't take effect until package is reinstalled

**Current State:**
- Modified files exist in `/Users/ja/Documents/CodeProjects/todd-lab/.todd/lib/py/todd-media/image-converter/`
- Changes not staged for commit
- Package needs `python3 -m pip install -e .` to reload

**Required Fix:**
- Either: Commit changes and install from repo
- Or: Document that dev mode requires reinstall after changes
- Or: Set up auto-reload/watch mode for development

**Priority:** 🟡 MEDIUM - Development workflow issue

---

## Confirmed Working Features ✅

1. **--parallel default is 8** ✅
   - Correctly implemented
   - Help text confirms: "Concurrent workers (default: 8, clamped to CPU count)"

2. **Resolution presets work** ✅
   - 1080p, 4k, 720p, original
   - Default: 4k

3. **Output format works** ✅
   - webp, png, jpg, etc.
   - Default: webp

4. **Core conversion functionality** ✅
   - Successful conversion of barriers-7 through barriers-10
   - Output: "total=4 converted=4 skipped=0 errors=0"

---

## Documentation Updates Needed

### Update ig-evaluate skill documentation

**Current issue:** Assumes todd-image-convert "just works"

**Required additions:**

1. **Environment Setup:**
```bash
# Add to ~/.zshrc or ~/.bashrc:
export PYTHONPATH="/Users/ja/Documents/CodeProjects/todd-lab/.todd/lib/py/todd-media/image-converter:$PYTHONPATH"
export DYLD_LIBRARY_PATH="/opt/homebrew/opt/vips/lib:$DYLD_LIBRARY_PATH"
```

2. **Correct Syntax:**
```bash
# For NEW visuals (skip existing):
todd-image-convert *.png --resolution 1080p --output-format webp --no-replace

# For UPDATING/REPLACING visuals:
todd-image-convert *.png --resolution 1080p --output-format webp --replace
```

---

## Action Items

### Immediate (Required for /ig-evaluate to work reliably)

- [ ] **Fix environment variables** (CRITICAL)
  - Option A: Add to shell profile (.zshrc or .bashrc)
  - Option B: Create wrapper script `todd-image-convert-wrapped` that sets vars
  - Option C: Fix Python installation paths
  - **Recommended:** Option A (shell profile) for simplicity

### Short-term (Workflow improvements)

- [ ] **Document dev workflow**
  - Add note about reinstalling after local changes
  - Consider adding to project README

- [ ] **Test suite**
  - Add tests for argument parsing
  - Add tests for environment variable handling

### Long-term (Future enhancements)

- [ ] **Auto-detection of environment**
  - Detect vips location automatically
  - Set DYLD_LIBRARY_PATH internally if needed

- [ ] **Better error messages**
  - When PYTHONPATH not set: "Run: export PYTHONPATH=..."
  - When libvips not found: "Install vips: brew install vips"

---

## Decisions Made

1. **Argument syntax:** ✅ Use current `--replace` / `--no-replace` (no colon syntax needed)

2. **Environment variables:** Pending decision
   - Recommended: Add to shell profile for permanent fix
   - Alternative: Wrapper script for portability

3. **Development mode:** Pending decision
   - Current: Editable install (`pip install -e .`) with manual reinstall
   - Consider: Auto-reload or better documentation

---

## Summary

**Blocking /ig-evaluate:**
- ❌ Environment variables not set (workaround exists, permanent fix needed)

**Resolved:**
- ✅ Argument syntax confirmed: `--replace` / `--no-replace` is correct

**Recommended immediate action:**
1. Add environment variables to shell profile (.zshrc or .bashrc)
2. Update /ig-evaluate documentation with environment setup instructions
3. Test that /ig-evaluate works without manual export commands

**Working correctly:**
- ✅ Core conversion functionality
- ✅ --parallel default of 8
- ✅ Resolution and format options
- ✅ Argument syntax (`--replace` / `--no-replace`)

---

*Documented during VIS-1.3 barriers evaluation*
*Next: Fix environment setup and clarify syntax requirements*
