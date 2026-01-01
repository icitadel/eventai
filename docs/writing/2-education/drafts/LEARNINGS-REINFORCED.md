# Learnings Reinforced in Skills/Commands (December 31, 2025)

## Critical Updates Made

Based on education.draft7→draft8→rc1 workflow corrections, the following learnings have been enforced in our skills and commands:

### 1. 🚨 Sources at Document END Only

**Updated Files:**
- `.claude/commands/narrative-refine-validate.md`
- `.claude/commands/section-publish.md`

**Changes:**
- ✅ **ENFORCED**: Single consolidated source list at END of document (after all content)
- ❌ **FORBIDDEN**: Sectional source placement (multiple source blocks throughout)
- ❌ **FORBIDDEN**: Source lists interspersed in narrative

**Rationale:**
- Professional academic publication standard
- Cleaner reading flow (no interruptions)
- Easier source management (single authoritative list)
- Consistent with textbook/research article format

**Example Structure:**
```markdown
# Question Title

[All narrative content...]

[Figure 1, Figure 2, Figure 3...]

## The Bottom Line

[Conclusion...]

---

**Sources:**

- [Long, D., & Magerko, B. (2020)...](URL)
- [UNESCO AI Competency Framework...](URL)
- [15 total sources listed]
```

---

### 2. 🚨 PNG Images for Final DOCX (NOT webp)

**Updated Files:**
- `.claude/commands/section-publish.md`

**Changes:**
- ✅ **REQUIRED**: PNG format for DOCX generation
- ❌ **WRONG**: Using webp in final DOCX (unsupported format)
- Updated error handling to check PNG format first

**Rationale:**
- DOCX requires PNG for high-quality image embedding
- WebP is for web/evaluation only (smaller file size for browser viewing)
- PNG ensures maximum quality in printed/distributed documents

**Correct Workflow:**
```bash
# 1. Generate with gemini-generate (creates PNG + webp)
gemini-generate --content barriers.content.md --prompt barriers.prompt.md

# 2. Evaluate using webp (faster loading)
/ig-evaluate barriers/*.webp

# 3. Update draft to reference PNG (for DOCX)
![Figure 1](../visuals/barriers/barriers-3.png)  # ✅ Correct
![Figure 1](../visuals/barriers/barriers-3.webp) # ❌ Wrong for DOCX
```

**File Size Indicators:**
- DOCX with 4 PNG images: ~18-20MB (confirms PNG embedding)
- DOCX with webp would fail or embed poorly: ~7-8MB

---

### 3. ⚠️ Keep Utility Scripts (DO NOT DELETE)

**Updated Files:**
- `.claude/commands/section-publish.md`

**Changes:**
- Added explicit warning to keep justify_docx.py
- Documented script location and reuse across sections
- Included full script code in section-publish skill

**Rationale:**
- Utility scripts are reusable across all sections
- Deleting after use forces recreation for next section
- Wastes time and introduces inconsistency risk

**Scripts to Keep:**
- `justify_docx.py` - DOCX justified text alignment
- Future utilities for common document processing tasks

**Location:**
```
docs/writing/{topic}/drafts/justify_docx.py  # Keep for all sections
```

---

### 4. 🚨 Question-Focused Narrative (No Sideramps)

**Updated Files:**
- `.claude/commands/section-create.md`
- `.claude/commands/narrative-refine-validate.md` (already had Priority 1: Question Alignment)

**Changes:**
- Added explicit "QUESTION-FOCUSED" requirement to narrative quality standards
- Emphasized "No sideramps" principle
- Reinforced that all content must serve answering the core question

**Rationale:**
- Each section addresses a specific research question
- Content must directly answer that question without tangents
- Mechanics explanations should only exist if they support answering the question
- Prevents scope creep and maintains tight focus

**Validation Checklist:**
- [ ] Does the content cleanly and thoroughly answer the question being asked?
- [ ] Is the narrative scope appropriate to the question's scope?
- [ ] Are there sideramps (tangents) that divert from answering the core question?
- [ ] Does every section support answering the question, or explain mechanics unrelated to it?

---

### 5. ❌ No Metadata Summary Sections

**Updated Files:**
- `.claude/commands/section-publish.md`

**Changes:**
- Added explicit requirement: "NO metadata summary section after sources"
- Publication-ready drafts should end with sources only

**Rationale:**
- Metadata summaries (Word Count, Status, Infographics list) are for internal tracking
- Publication-ready documents should not include process metadata
- Cleaner, more professional final output

**Wrong:**
```markdown
**Sources:**
- [Source 1](URL)
- [Source 2](URL)

---

**Word Count:** ~2,050 words
**Status:** DRAFT 8
**Infographics:**
- Figure 1: ...
```

**Correct:**
```markdown
**Sources:**
- [Source 1](URL)
- [Source 2](URL)

[End of document]
```

---

## Files Updated

1. `.claude/commands/narrative-refine-validate.md`
   - Lines 10, 100-148, 240-281: Source placement enforcement

2. `.claude/commands/section-publish.md`
   - Line 108: Source attribution at document end
   - Line 118-120: Quality standards (sources + no metadata)
   - Lines 230-234: PNG image requirement for DOCX
   - Lines 256-260: Image embedding PNG emphasis
   - Lines 262-320: justify_docx.py script preservation
   - Lines 374-381: Error handling for PNG format

3. `.claude/commands/section-create.md`
   - Lines 40-45: Question-focused narrative requirement

---

## Impact

These updates ensure that:
- ✅ All future sections use document-end source placement (not sectional)
- ✅ All final DOCX files use PNG images (not webp)
- ✅ Utility scripts are preserved for reuse
- ✅ All narratives stay focused on answering their core question
- ✅ Publication-ready documents exclude metadata summaries

**Result:** Consistent, professional, publication-ready curriculum sections following academic standards.

---

**Date:** December 31, 2025
**Context:** education.draft7→draft8→rc1 workflow corrections
**Updated By:** Claude Sonnet 4.5
