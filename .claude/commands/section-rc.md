# Section Release Candidate (RC) Preparation

## Purpose

Prepare a draft section for publishing by removing the narrative outline/summary section while preserving the question, main content (with images), and sources.

## Input Format

Draft files typically have this structure:
```markdown
# Question

> The question being answered

---

# Narrative

**Target:** word count

Summary paragraph...

**This narrative covers three points:**
- Point 1
- Point 2
- Point 3

---

# Main Title

[Main content with images, sections, etc.]

---

**Sources:**
- Source 1
- Source 2
```

## Output Format

RC (Release Candidate) files should have:
```markdown
# Question

> The question being answered

---

# Main Title

[Main content with images, sections, etc.]

---

**Sources:**
- Source 1
- Source 2
```

## Processing Rules

1. **Keep:** Question section (from start to first `---`)
2. **Remove:** Narrative section (from first `---` to second `---`, including both markers)
3. **Keep:** Main content (from after second `---` to final `---` before Sources)
4. **Keep:** Sources section (final `---` and everything after)

## Output File Naming

- Input: `transformation.draft9.md`
- Output: `transformation.rc9.md` (replace `.draft` with `.rc`)

Or:
- Input: `transformation.draft9.md`
- Output: `transformation.rc1.md` (if starting fresh RC numbering)

## Usage

```bash
/section-rc @docs/writing/1-transformation/drafts/transformation.draft9.md
```

Optional: Specify output RC number
```bash
/section-rc @docs/writing/1-transformation/drafts/transformation.draft9.md --rc=1
```

## Validation Before Publishing

The command should:
1. Verify all image references exist
2. Confirm all sources are accessible
3. Check word count matches target range
4. Report any orphan claims without sources

## Success Criteria

- Narrative section completely removed
- Question preserved exactly
- Main content preserved exactly (including images, formatting, line breaks)
- Sources preserved exactly
- File saved with `.rc` naming convention
- Confirmation message showing what was removed and what remains