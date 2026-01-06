# Privacy Topic - Visual Assets

**Topic**: Privacy, Regulation & Consent (Section 4)
**Question**: How do we balance legitimate security needs with fundamental privacy rights at festivals?

This folder contains visual assets for the Privacy section, including infographics, decision frameworks, and regulatory visualizations generated using NotebookLM.

---

## Visual Content Plan

### VIS-4.1: EU AI Act Risk Classification (Pyramid/Tier Diagram)

**Type**: Regulatory Risk Visualization
**Platform**: NotebookLM
**Status**: ✅ Ready to generate

**Files**:
- `eu-ai-act/eu-ai-act.content.md` - Detailed source material for NotebookLM upload
- `eu-ai-act/eu-ai-act.prompt.md` - Token-optimized generation prompt
- `eu-ai-act/eu-ai-act.instructions.md` - Step-by-step generation workflow

**What it shows**:
- Three-tier pyramid classification (Prohibited/High-Risk/Limited-Risk)
- EU AI Act regulatory framework for biometric systems at festivals
- Real-world examples: Clearview AI (prohibited), post-event biometrics (high-risk), chatbots (limited-risk)
- Financial penalties: €35M or 7% global turnover for violations
- Enforcement date: February 2, 2025

**Key statistics**:
- PROHIBITED: €35M or 7% turnover fine, real-time biometric ID banned
- HIGH-RISK: Conformity assessment required, post-event ID permitted with safeguards
- LIMITED-RISK: Disclosure only, AI chatbots and recommendation systems

**Estimated generation time**: ~15-20 minutes

**To generate**: Follow instructions in `eu-ai-act/eu-ai-act.instructions.md`

---

### VIS-4.2: GDPR Biometric Data Requirements Flowchart

**Type**: Compliance Decision Tree
**Platform**: NotebookLM
**Status**: ✅ Ready to generate

**Files**:
- `gdpr-flowchart/gdpr-flowchart.content.md` - Complete regulatory framework
- `gdpr-flowchart/gdpr-flowchart.prompt.md` - Token-optimized flowchart prompt
- `gdpr-flowchart/gdpr-flowchart.instructions.md` - Generation workflow

**What it shows**:
- Five-question decision tree for GDPR compliance
- YES/NO branches showing compliant (green) and non-compliant (red) paths
- Clear STOP endpoints with violation consequences
- Final PROCEED node with four mandatory safeguards
- Real examples: Danish football (approved), Taylor Swift Rose Bowl (rejected)

**Five compliance checkpoints**:
1. Necessity: Is collection necessary (not just convenient)?
2. Explicit consent: Did attendees affirmatively consent before event?
3. Opt-out: Can they refuse without penalty?
4. Data minimization: Only necessary data, limited retention?
5. DPIA: Impact assessment completed?

**Mandatory safeguards** (if passing all 5):
- Encryption (TLS 1.3, AES-256)
- Limited retention (scheduled auto-delete)
- Access controls (need-to-know, logged)
- Breach response plan (72-hour notification)

**Estimated generation time**: ~15-20 minutes

**To generate**: Follow instructions in `gdpr-flowchart/gdpr-flowchart.instructions.md`

---

### VIS-4.3: Consent Architecture Spectrum

**Type**: Design Pattern Evaluation Spectrum
**Platform**: NotebookLM
**Status**: ✅ Ready to generate

**Files**:
- `consent-spectrum/consent-spectrum.content.md` - Consent design patterns across spectrum
- `consent-spectrum/consent-spectrum.prompt.md` - Token-optimized spectrum prompt
- `consent-spectrum/consent-spectrum.instructions.md` - Generation instructions

**What it shows**:
- Horizontal spectrum from Coercive (red) to Voluntary (green)
- Three zones: Coercive (illegal), Problematic (gray area), Voluntary (compliant)
- Real consent design patterns and their legal status
- GDPR Article 7 and Article 9 principles embedded

**Spectrum sections**:

**Coercive (Red - ❌ PROHIBITED)**:
- Mandatory facial recognition (no alternatives)
- Bundled consent (all-or-nothing)
- Pre-checked checkboxes (silence = consent)
- Hidden in terms of service (buried in 50-page document)

**Problematic (Orange - ⚠️ GRAY AREA)**:
- Default opt-in (yes by default, disable in settings)
- Soft wall penalties (one option vastly superior, other appears "available")
- Confusing interfaces (users consent without understanding)

**Voluntary (Green - ✅ COMPLIANT)**:
- Clear opt-in (explicit YES/NO, equal prominence)
- Genuine alternatives (multiple entry methods, all equal)
- Granular controls (separate consent per purpose)
- Plain language (understandable without jargon)
- Easy withdrawal (can change mind without friction)

**GDPR principles shown**:
- Article 7: Freely given, specific, informed, unambiguous
- Article 9: Special category requires explicit, clear, separate, alternative

**Estimated generation time**: ~15-20 minutes

**To generate**: Follow instructions in `consent-spectrum/consent-spectrum.instructions.md`

---

### VIS-4.4: Privacy vs. Safety Trade-Off Matrix

**Type**: Decision Framework Matrix
**Platform**: NotebookLM
**Status**: ✅ Ready to generate

**Files**:
- `privacy-safety-matrix/privacy-safety-matrix.content.md` - Complete framework and examples
- `privacy-safety-matrix/privacy-safety-matrix.prompt.md` - Token-optimized matrix prompt
- `privacy-safety-matrix/privacy-safety-matrix.instructions.md` - Generation workflow

**What it shows**:
- Two-axis matrix: Safety Threat (Y) vs. Privacy Intrusion (X)
- Four quadrants with decision labels and color coding
- Real festival case studies positioned within quadrants
- Decision framework showing when surveillance is/isn't justified

**Four quadrants**:

**Q1 (Bottom-Left, Green - ✅ APPROPRIATE)**:
- Low safety threat + Low privacy intrusion
- Example: Standard CCTV, security staff, manual observation
- Decision: COMPLIANT & STANDARD

**Q2 (Bottom-Right, Red - ❌ INAPPROPRIATE)**:
- Low safety threat + High privacy intrusion
- Examples: Taylor Swift Rose Bowl 2018, secret facial recognition, mass surveillance
- Decision: ILLEGAL & UNETHICAL

**Q3 (Top-Left, Yellow - ⚠️ CONSTRAINED)**:
- High safety threat + Low privacy intrusion
- Scenario: Credible threat but limited to low-intrusion measures
- Decision: May require escalation to medium-intrusion if threat genuine

**Q4 (Top-Right, Orange - ⚠️ POTENTIALLY JUSTIFIED)**:
- High safety threat + High privacy intrusion
- Example: Danish police football with gang violence threat
- Decision: Legal IF all safeguards present (transparency, DPIA, limited retention, etc.)

**Real case studies** (positioned within matrix):
- ✅ Danish police football (Q4, approved with safeguards)
- ❌ Taylor Swift Rose Bowl (Q2, rejected, secret scanning)
- ❌ Concert facial recognition denied (Q2, low threat, high intrusion)
- ✅ Standard festival security (Q1, standard approach)

**Eight safeguards** (required for Q4 deployments):
1. Threat documented (credible, specific, justified)
2. Proportionality (least intrusive option)
3. Transparency (attendees informed)
4. DPIA completed (risk assessment)
5. Retention limited (delete after threat)
6. Access control (law enforcement only, logged)
7. Independent audit (third-party review)
8. Accountability (defensible to regulator)

**Estimated generation time**: ~15-20 minutes

**To generate**: Follow instructions in `privacy-safety-matrix/privacy-safety-matrix.instructions.md`

---

## Generation Workflow

### For NotebookLM Infographics

1. **Prepare source**: Use provided `.content.md` file (already completed)
2. **Upload to NotebookLM**: Create notebook, add source document
3. **Apply prompt**: Use provided `.prompt.md` (token-optimized)
4. **Generate**: Select detail level and orientation
5. **Download & Save**: Save as PNG, rename according to convention
6. **Convert**: Use `todd-image-convert` to create WebP versions
7. **Evaluate**: Use `/ig-evaluate` command for quality assessment
8. **Select winner**: Choose highest-scoring variant

### All Four Visuals Share Same Workflow

Each visual folder contains:
- `.content.md` - Source material (detailed regulatory/design content)
- `.prompt.md` - Token-optimized generation prompt
- `.instructions.md` - Complete step-by-step workflow

**Total generation time**: ~60-80 minutes for all four visuals (15-20 min per visual)

---

## File Naming Convention

### Image Files
**Format**: `{visual-name}-{variant}.{ext}`

**Examples**:
- `eu-ai-act-1.png`, `eu-ai-act-2.png`, `eu-ai-act-3.png` (VIS-4.1)
- `gdpr-flowchart-1.png`, `gdpr-flowchart-2.png`, `gdpr-flowchart-3.png` (VIS-4.2)
- `consent-spectrum-1.png`, `consent-spectrum-2.png`, `consent-spectrum-3.png` (VIS-4.3)
- `privacy-safety-matrix-1.png`, `privacy-safety-matrix-2.png`, `privacy-safety-matrix-3.png` (VIS-4.4)

### WebP Conversions
- `eu-ai-act-1.webp`, `eu-ai-act-2.webp`, etc. (optimized for web)

### Documentation Files
- `.content.md` - Source material for NotebookLM
- `.prompt.md` - Token-optimized generation prompt
- `.instructions.md` - Workflow guidance
- `.eval.md` - Evaluation report (generated after /ig-evaluate)

---

## EventAI Visual Identity Compliance

All visuals must comply with EventAI brand standards:

### Color Palette
- **Deep purple** (#6B46C1) - Primary brand, AI elements
- **Electric coral** (#FF6B6B) - Emphasis, prohibition, critical
- **Alert amber** (#ED8936) - Warnings, risk, attention
- **Sky blue** (#4299E1) - Data, questions, decisions
- **Forest green** (#48BB78) - Compliance, approval, success
- **Warm sunlight** (#F6AD55) - Secondary emphasis
- **Midnight slate** (#2D3748) - Body text, outlines
- **Pure white** (#FFFFFF) - Background, breathing room

### Typography
- **Headings**: Inter (bold, 24-36pt)
- **Body**: Source Sans Pro (regular, 14-16pt)
- **Data**: Inter (bold, 48-72pt for key numbers)
- **Minimum**: 11-12pt for smallest readable text

### Design Principles
- Semi-flat style with subtle depth
- Rounded corners (8-12px radius)
- 2-3px outlines for clarity
- High data-ink ratio (minimal decoration)
- Festival context (not generic diagrams)
- Professional yet accessible mood
- 25-30% white space minimum

### Festival Context Requirements
- Real examples from festival operations
- Regulatory/compliance focus (not generic)
- Biometric/privacy/security scenarios
- References to actual case studies
- Recognition of festival-specific challenges

---

## Token Optimization Requirements

**🚨 CRITICAL**: `.content.md` and `.prompt.md` files MUST be token-optimized before upload

### Target Metrics
- ✅ **Token reduction**: 40-70% from verbose original
- ✅ **Information preservation**: 100% of substantive points
- ✅ **Readability**: High (scannable, clear structure)
- ✅ **Completeness**: All facts, stats, technical details intact

### What's Preserved
- ✅ All regulatory details (fines, dates, requirements)
- ✅ Real case examples (Danish football, Taylor Swift Rose Bowl)
- ✅ Technical specifications (hex codes, point sizes, safeguards)
- ✅ Decision criteria and warnings

### What's Removed
- ❌ Filler words (very, really, quite, actually)
- ❌ Explanatory framing ("This prompt will...")
- ❌ Redundant examples (keep most illustrative only)
- ❌ Excessive context or marketing language

---

## Quality Checklist

Before marking visual complete:

✅ **Factual Accuracy**: All data verified against source documents
- Regulatory details (fines, enforcement dates, articles)
- Real examples (case outcomes, specific details)
- Technical specifications (hex codes, retention periods)

✅ **EventAI Style**: Colors, typography, design match style guide
- Pure white background (#FFFFFF, not cream/beige)
- Correct color palette (no substitutes)
- Appropriate typography (minimum 11pt, clear hierarchy)
- Semi-flat design, rounded corners

✅ **Festival Context**: Industry-specific imagery, not generic
- Real festival scenarios (not generic business diagrams)
- Biometric/privacy/security focus
- Recognizable examples (famous cases, known challenges)

✅ **Accessibility**: WCAG AA contrast, readable text sizes
- All text ≥11pt (12pt preferred)
- High contrast (dark on light, light on dark)
- Clear hierarchy and structure
- No color-dependent meaning

✅ **File Management**: Named correctly, saved to appropriate folder
- Correct naming convention applied
- Saved to corresponding visual folder
- PNG and WebP versions created
- Evaluation report generated

✅ **Documentation**: Status updated in VISUAL-CONTENT-PLAN.md
- Visual completion documented
- Score and selection noted
- Lesson learned recorded

---

## Related Documentation

- **Main Draft**: [../drafts/privacy.draft.md](../drafts/privacy.draft.md)
- **Visual Content Plan**: [../../VISUAL-CONTENT-PLAN.md](../../VISUAL-CONTENT-PLAN.md)
- **EventAI Style Guide**: [../../../lemmy/style-guide/eventai-visual-identity.md](../../../lemmy/style-guide/eventai-visual-identity.md)
- **Infographic Best Practices**: [../../../lemmy/research/infographics-best-practices.md](../../../lemmy/research/infographics-best-practices.md)
- **NotebookLM Workflows**: [../../../lemmy/workflows/notebooklm-workflows.md](../../../lemmy/workflows/notebooklm-workflows.md)

---

## Next Steps

1. **VIS-4.1**: Generate EU AI Act pyramid
   - Follow: `eu-ai-act/eu-ai-act.instructions.md`
   - Expected: 15-20 minutes

2. **VIS-4.2**: Generate GDPR flowchart
   - Follow: `gdpr-flowchart/gdpr-flowchart.instructions.md`
   - Expected: 15-20 minutes

3. **VIS-4.3**: Generate consent spectrum
   - Follow: `consent-spectrum/consent-spectrum.instructions.md`
   - Expected: 15-20 minutes

4. **VIS-4.4**: Generate privacy-safety matrix
   - Follow: `privacy-safety-matrix/privacy-safety-matrix.instructions.md`
   - Expected: 15-20 minutes

5. **Update VISUAL-CONTENT-PLAN.md** with completion status and scores

---

*Visual Assets Folder for Privacy Topic*
*Last Updated: December 29, 2025*
*All four visuals ready for NotebookLM generation*
*Part of: EventAI Curriculum + Lemmy Content Generation System*
