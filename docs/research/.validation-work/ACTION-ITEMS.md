# Validation Action Items - Quick Reference
**Priority-Sorted Tasks for Research Draft Revision**

---

## 🔴 CRITICAL (Must Fix Before Publication)

### 1. Create Source Catalogs for All 5 Documents
**Estimated Time:** 20-30 hours total (4-6 hours per document)

**What's needed:**
- Add formal "Sources" or "References" section to end of each document
- Include full citations with URLs for all web sources
- Organize by tiers (Regulatory → Independent Research → Industry Reports → Media)
- Add access dates for all web content

**Template to use:**
```markdown
---

## Sources

### Tier 1: Regulatory & Legal Documents
1. **EU AI Act** - Regulation (EU) 2024/1689 (February 2, 2025)
   https://eur-lex.europa.eu/...
   Accessed: December 28, 2025

### Tier 2: Independent Research & Audits
[Continue...]

### Tier 3: Industry Reports & Vendor Case Studies
[Continue...]

### Tier 4: Media Coverage & Advocacy
[Continue...]
```

**Files affected:** ALL 5 draft documents

---

## 🟡 HIGH PRIORITY (Strongly Recommended)

### 2. Replace Vague Citations with Specific Sources
**Estimated Time:** 2-3 hours per document

**Citations to fix:**

#### Transformation Draft
- Line 16: "(Industry survey, 2024)" → Replace with specific organization/survey name OR remove
- Line 58: "(Market research report, 2024)" → Replace with specific firm/report title OR remove
- Line 58: "55% of AI adopters are small businesses" → Add source OR remove
- Line 164: "industry data shows 88% vs 54% retention" → Add specific app analytics study OR remove

#### Analytics Draft
- Line 14: "78% yield improvement" (Cover Genius) → Add specific citation
- Lines 115, 120, 124: Sports venue revenue claims (Real Madrid 29%, Warriors 92%/27%, Manchester United 22%) → Add vendor case study or sports business publication citations
- Line 150: "91% of UK fans oppose dynamic pricing" → Add specific survey source

#### Privacy Draft
- Lines 106, 321: "€20,000-80,000 DPIA costs" → Add source for estimate
- Lines 143, 392: "300+ artists, 35+ organizations" (Red Rocks) → Add Fight for the Future or media source
- Lines 360-368: Cleveland Browns Wicket metrics → Add Stadium Tech Report or Wicket case study citation

#### Personalization Draft
- Lines 17, 176: "77% disappear within 3 days" → Add app analytics firm study
- Lines 16, 172: "44-56% declined notifications" (iOS) → Add specific research source
- Lines 50, 213: "313% decline" (iBeacon) → Add research study
- Lines 219, 225: DoubleDutch/Hopin financials → Add TechCrunch or similar business press citation
- Line 192: "67% BCG inaccurate personalization" → Add full BCG study title

#### Education Draft
- Line 15: "12 major universities" → Either list all 12 OR clarify as "Research across major universities including..."
- Lines 41, 130, 138: Professional cert pricing → Add website citations with access dates
- Lines 127, 141, 142: MPI/PCMA enrollment/usage stats → Add source

---

### 3. Add Cross-Reference Transferability Notes
**Estimated Time:** 1 hour

**Transformation draft only:**

When citing sports venue data (Real Madrid, Warriors, Manchester United), add note:
```markdown
*Note: Sports venue data; festival transferability remains unverified.
See Analytics section for detailed transferability assessment.*
```

**Files affected:** [transformation/draft.md](docs/research/transformation/draft.md)

---

## 🟠 MEDIUM PRIORITY (Recommended)

### 4. Add Missing Citations for Remaining Orphan Claims
**Estimated Time:** 3-4 hours

**Track down and add citations for:**
- Small business AI adopters (55%)
- App retention rates (88% vs 54%)
- iOS notification opt-in decline (44-56%)
- iBeacon shopping app decline (313%)
- Cover Genius yield improvement (78%)
- DPIA cost estimates
- Red Rocks protest numbers
- Cleveland Browns detailed metrics
- University survey methodology
- Professional certification enrollment data

---

## 🟢 LOW PRIORITY (Optional Enhancements)

### 5. Add Access Dates to All Web Sources
**Estimated Time:** 30 minutes (during source catalog creation)

Format: `Accessed: December 28, 2025`

---

### 6. Create Abbreviation Index
**Estimated Time:** 1 hour per document

Add comprehensive abbreviation list to each document:
- GDPR, BIPA, CCPA, EU AI Act, DPIA, etc.
- First-mention definitions already exist, this just consolidates for reference

---

### 7. Consider Source Catalog Deduplication
**Estimated Time:** 2-3 hours

**Options:**
- Create master source catalog referenced by all 5 documents
- Ensure identical formatting for shared sources across separate catalogs
- Use endnote-style numbering

---

## Document-Specific Priority Breakdown

### Transformation Draft
1. 🔴 Create source catalog (4-6 hours)
2. 🟡 Replace vague citations: "Industry survey", "Market research report", retention data (1-2 hours)
3. 🟡 Add transferability notes for sports venue data (30 minutes)

### Analytics Draft
1. 🔴 Create source catalog (4-6 hours)
2. 🟡 Add sports venue revenue source citations (1-2 hours)
3. 🟡 Add UK fan survey source (30 minutes)

### Privacy Draft
1. 🔴 Create source catalog (4-6 hours)
2. 🟡 Add DPIA cost source (30 minutes)
3. 🟡 Add Red Rocks protest sources (30 minutes)
4. 🟡 Add Cleveland Browns metrics source (30 minutes)

### Personalization Draft
1. 🔴 Create source catalog (4-6 hours)
2. 🟡 Add app analytics sources: attrition, iOS opt-in, iBeacon decline (1-2 hours)
3. 🟡 Add BCG study full citation (15 minutes)
4. 🟡 Add DoubleDutch/Hopin financial sources (30 minutes)

### Education Draft
1. 🔴 Create source catalog (4-6 hours)
2. 🟡 Clarify university survey methodology (30 minutes)
3. 🟡 Add certification pricing/enrollment sources (1 hour)

---

## Validation Strengths to Preserve ✅

**DO NOT change these - they're excellent:**

1. ✅ **Cross-document consistency** - Perfect alignment on all shared claims (40-41% DICE, 20% Bonnaroo engagement, 42% zero ROI, etc.)
2. ✅ **Entity name standardization** - Zero inconsistencies (DICE, Bonnaroo, FC Copenhagen, Danish DPA, etc.)
3. ✅ **Numerical formatting** - Consistent percentages, currency, ranges
4. ✅ **Regulatory citations** - Specific GDPR articles, DPA decisions, EU AI Act references
5. ✅ **Confidence markers on projections** - Forecasts appropriately labeled
6. ✅ **Vendor vs. independent data distinction** - Critical for evidence assessment

---

## Quick Stats

**Overall Assessment:** ⚠️ PASS WITH WARNINGS
- **Consistency Score:** 100% (zero contradictions)
- **Citation Coverage:** ~70% (good but needs improvement)
- **Entity Consistency:** 100% (perfect)
- **Numerical Formatting:** 100% (perfect)

**Critical Issues:** 1 (no source catalogs)
**High Priority Issues:** ~15-20 (vague citations, orphan claims)
**Medium/Low Issues:** ~10 (enhancements)

**Estimated Total Revision Time:**
- Critical fixes: 20-30 hours
- High priority fixes: 8-12 hours
- Medium/low enhancements: 5-10 hours
- **Total: 33-52 hours**

---

## Validation Documents

**Full Report:** [.validation-work/VALIDATION-REPORT.md](.validation-work/VALIDATION-REPORT.md)
**Claims Database:** [.validation-work/claims-database.md](.validation-work/claims-database.md)
**This Action Items List:** [.validation-work/ACTION-ITEMS.md](.validation-work/ACTION-ITEMS.md)

**Validation Date:** December 28, 2025
**Validator:** Claude Sonnet 4.5
