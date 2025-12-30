# VIS-4.2: GDPR Biometric Data Requirements Flowchart - Generation Instructions

**Infographic**: GDPR Compliance Decision Flowchart
**Status**: ✅ Ready to generate
**Estimated time**: ~15-20 minutes total

---

## Quick Start: NotebookLM Workflow

### Step 1: Upload Source (2 min)

1. Go to [NotebookLM](https://notebooklm.google.com/)
2. Create notebook: `EventAI - Privacy & Regulation`
3. Upload: `gdpr-flowchart.content.md` (this folder)
4. Wait for processing (~30 sec)

### Step 2: Generate Infographic (10-15 min)

1. Click **"Infographic"** in generation menu
2. Settings:
   - **Detail Level**: Detailed
   - **Orientation**: Portrait (flowchart requires vertical space)
3. **Paste prompt** below
4. Click **"Generate"**
5. Wait ~2 min for Nano Banana processing
6. **Generate 3 variations** (click regenerate 2 more times)

---

## 🔥 FLOWCHART PROMPT (Token-optimized ~310 tokens)

```
Vertical decision flowchart: GDPR compliance pathway for festival biometric systems

🚨 CRITICAL: Pure white background #FFFFFF, clear top-to-bottom flow with YES/NO branches, green compliance path, red violation endpoints, exact regulatory requirements and fine amounts

STRUCTURE:
Top-to-bottom flowchart: START → Q1-Q5 decision diamonds → PROCEED or STOP
YES (green) branches lead forward or to PROCEED
NO (red) branches lead to STOP violation nodes
Final node: PROCEED with safeguards implementation box

FLOW (Top to Bottom):

START (Purple #6B46C1):
"Deploying biometric system at festival?"

Q1 (Blue #4299E1 diamond): [Article 5 Data Minimization]
"Biometric collection NECESSARY? (not just convenient/future use)"
YES → Q2 (green branch)
NO → STOP "VIOLATION: Data Minimization" (red branch)
  Fine: €20M or 4% turnover
  Reason: Cannot collect unnecessary biometric data

Q2 (Blue diamond): [Article 9 Special Category]
"EXPLICIT informed consent? (before event, clear, affirmative action, not pre-checked)"
YES → Q3 (green)
NO → STOP "VIOLATION: Article 9" (red)
  Fine: €20M or 4% turnover
  Reason: Biometric = special category (most restrictive)
  Real: ❌ Taylor Swift Rose Bowl (secret scanning)

Q3 (Blue diamond): [Consent Autonomy]
"Opt-out WITHOUT penalty? (alternative entry free/easy, no waiting line penalty)"
YES → Q4 (green)
NO → STOP "VIOLATION: Coercive Consent" (red)
  Fine: €20M or 4% turnover
  Reason: Consent cannot be forced or penalized

Q4 (Blue diamond): [Article 5 Storage Limitation]
"Data MINIMIZED + LIMITED retention? (auto-delete on schedule, not indefinite)"
YES → Q5 (green)
NO → STOP "VIOLATION: Retention" (red)
  Fine: €20M or 4% turnover
  Reason: Must delete unnecessary data on retention schedule

Q5 (Blue diamond): [Article 35 DPIA]
"DPIA completed? (formal impact assessment documented, risks identified)"
YES → PROCEED (green)
NO → ⚠️ ELEVATED RISK (amber) - Complete DPIA before processing

PROCEED NODE (Green #48BB78 rounded rect):
"✅ GDPR COMPLIANCE PATHWAY CLEAR"

SAFEGUARDS BOX (Green background, dark text 13-14pt):
"MANDATORY SAFEGUARDS (Non-Negotiable Implementation):"

1. ENCRYPTION
   In transit: TLS 1.3+
   At rest: AES-256
   Keys: Separate from data, secure storage

2. LIMITED RETENTION
   Max window: 30 days (example)
   Auto-delete: Scheduled purge system
   Verification: Monthly audit trail

3. ACCESS CONTROLS
   Need-to-know basis only
   Role-based access (security vs analytics)
   Logging: All access recorded
   Revocation: Immediate removal when staff leaves

4. BREACH RESPONSE PLAN
   Detection: Monitoring for unauthorized access
   Response: Incident response team (documented procedures)
   Notification: 72-hour attendee notification if breach
   Regulator: DPA notified if high-risk
   Correction: Improvements to prevent recurrence

STYLE:
- Background: Pure white #FFFFFF
- START/PROCEED: Purple #6B46C1 (rounded rect, white text)
- Questions: Blue #4299E1 diamonds/squares (white text)
- YES branches: Green #48BB78 (green lines, white YES label)
- NO branches: Red #FF6B6B (red lines, white NO label)
- STOP endpoints: Dark red background
- Safeguards box: Green #48BB78 background
- Text: Source Sans Pro 14-16pt questions, 13-14pt safeguards
- Regulation refs: Light gray 11-12pt (Article X citations)
- Layout: Semi-flat, clear top-to-bottom progression, clean arrows

REGULATORY ACCURACY (Embed exactly):
- Article 5 (Data Minimization): Cannot collect unnecessary data
- Article 9 (Special Category): Biometric requires explicit consent
- Article 35 (DPIA): High-risk processing requires impact assessment
- Fines: €20M or 4% (standard), €35M or 7% (serious violations)
- Enforcement: National Data Protection Authority

REAL EXAMPLES (Include if possible):
- ✅ Danish police football (DPA-approved, explicit consent, legitimate security purpose)
- ❌ Taylor Swift Rose Bowl (secret scanning, no consent obtained)
- ❌ Clearview AI (mass web scraping, indefinite retention, prohibited)

❌ AVOID: Cream/beige background, horizontal layout, unclear branches, missing regulations/fines, generic flowchart (not festival-specific), cluttered safeguards, text <12pt

✅ REFERENCE: Clear decision tree, color-coded paths (green=compliance, red=violation), STOP endpoints with consequences, festival biometric context, safeguards implementation details
```

---

## Step 3: Review Generated Variants (5 min)

### Quality Checklist

**✅ CRITICAL (Must Pass):**
- [ ] **Pure white background** (#FFFFFF, not cream/beige)
- [ ] **Clear flowchart structure**: START → Q1-Q5 → PROCEED/STOP
- [ ] **YES/NO branches obvious**: Green for YES, red for NO
- [ ] **All 5 questions present**: Necessity, consent, opt-out, data minimization, DPIA
- [ ] **STOP endpoints labeled**: With regulation citations and fine amounts
- [ ] **Safeguards box at end**: With 4 detailed requirements
- [ ] **Text legible**: Minimum 12pt for labels, 14-16pt for questions
- [ ] **Festival context**: References to real examples (Danish football, Taylor Swift Rose Bowl, Clearview)

**✅ STYLE (EventAI Compliance):**
- [ ] Colors accurate (purple #6B46C1, blue #4299E1, green #48BB78, red #FF6B6B)
- [ ] Typography clean (Source Sans Pro, no fancy fonts)
- [ ] Semi-flat design, rounded corners
- [ ] Professional + authoritative mood (regulatory content)

**✅ FLOWCHART-SPECIFIC:**
- [ ] Clear directional flow (top to bottom)
- [ ] Decision points marked with diamonds/squares
- [ ] Green path shows compliance route
- [ ] Red branches show violations
- [ ] PROCEED node distinct from STOP nodes
- [ ] Safeguards clearly listed at end

### If Any Variant Fails Checklist

**Background NOT pure white?**
→ Regenerate: "Background EXACTLY #FFFFFF pure white, NOT cream/beige. Verify with color picker."

**Flowchart unclear/messy?**
→ Regenerate: "Clear top-to-bottom flow. Each question is diamond. YES branches green (→PROCEED). NO branches red (→STOP). Simple visual hierarchy."

**Questions/regulations wrong?**
→ Regenerate: "Verify: Q1 Article 5 (necessity), Q2 Article 9 (explicit consent), Q3 (autonomy), Q4 Article 5 (retention), Q5 Article 35 (DPIA). Fines: €20M or 4% turnover."

**Missing real examples?**
→ Regenerate: "Include real cases: ✅ Danish police football (approved), ❌ Taylor Swift Rose Bowl (rejected, no consent), ❌ Clearview AI (prohibited, mass scraping)."

**Text too small?**
→ Regenerate: "Minimum 12pt for all text, 14-16pt for questions. Safeguards list 13-14pt. Print-ready sizes."

---

## Step 4: Download & Save (2 min)

### Download All Variants

1. Download each generated variant (PNG, high resolution)
2. Rename: `gdpr-flowchart-1.png`, `gdpr-flowchart-2.png`, `gdpr-flowchart-3.png`
3. Save to: `docs/writing/4-privacy/visuals/gdpr-flowchart/`

### Convert to WebP

```bash
cd docs/writing/4-privacy/visuals/gdpr-flowchart
todd-image-convert gdpr-flowchart-*.png --output-format webp --resolution 1080p
```

---

## Step 5: Evaluate & Select Winner (5 min)

### Run Comprehensive Evaluation

```bash
/ig-evaluate docs/writing/4-privacy/visuals/gdpr-flowchart/gdpr-flowchart-*.webp
```

### Expected Scores

**Flowchart variants**: 75-88/100 (if white background + clear flow + regulatory accuracy + festival context)

### Select Winner

Choose variant with:
- Highest scores for clarity + EventAI style
- Clear decision tree progression
- Readable branch labels and endpoints
- Accurate regulation citations and fines
- Pure white background
- Festival deployment context

---

## Quick Command

```bash
# After generating in NotebookLM and downloading PNGs:
todd-image-convert docs/writing/4-privacy/visuals/gdpr-flowchart/*.png --output-format webp --resolution 1080p && /ig-evaluate docs/writing/4-privacy/visuals/gdpr-flowchart/*.webp
```

---

## Expected Outcomes

### What Success Looks Like

**Flowchart Layout:**
- Vertical decision tree (top to bottom)
- Clear YES (green) and NO (red) branches
- Questions as decision points
- STOP endpoints for violations (red)
- PROCEED endpoint for compliance (green)
- Safeguards box with 4 implementation details
- Pure white background
- Festival context (real examples, biometric systems)

### File Deliverables

- ✅ `gdpr-flowchart-{N}.png` (3-5 MB, high-res PNG)
- ✅ `gdpr-flowchart-{N}.webp` (1-3 MB, web-optimized)
- ✅ `VIS-4.2-EVALUATION-REPORT.md` (comprehensive analysis)
- ✅ Winner selected and documented

---

## Troubleshooting

### Background NOT pure white
**Solution**: Regenerate with "🚨 Background EXACTLY #FFFFFF pure white, not cream/beige. Use color picker to verify."

### Flowchart unclear (hard to follow flow)
**Solution**: Regenerate with "Simple vertical flowchart: START → Q1 → Q2 → Q3 → Q4 → Q5 → PROCEED. YES branches green (forward). NO branches red (STOP). Diamond shapes for decisions."

### Regulations/fines wrong or missing
**Solution**: Regenerate with exact requirements: "Q1 Article 5 (necessity), Q2 Article 9 (explicit consent), Q3 (autonomy), Q4 Article 5 (retention), Q5 Article 35 (DPIA). All violations: €20M or 4% turnover."

### Missing real examples
**Solution**: Regenerate with "Real cases: ✅ Danish football (approved), ❌ Taylor Swift Rose Bowl (no consent rejected), ❌ Clearview AI (mass scraping prohibited). Festival context required."

### Questions/requirements unclear
**Solution**: Regenerate with clear, simple wording: "Q1: Is collection NECESSARY? Q2: EXPLICIT consent obtained? Q3: Opt-out penalty-free? Q4: Data minimized/limited retention? Q5: DPIA completed?"

---

## Related Documentation

- [VIS-4.2 Source Material](gdpr-flowchart.content.md)
- [EventAI Visual Identity](../../../lemmy/style-guide/eventai-visual-identity.md)
- [Privacy Visual Content Plan](../../VISUAL-CONTENT-PLAN.md)
- [/ig-evaluate Command](/.claude/commands/ig-evaluate.md)

---

*VIS-4.2 Generation Package - GDPR Biometric Compliance Flowchart*
*Updated: December 29, 2025*
*Ready for NotebookLM generation*
