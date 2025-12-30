# GDPR Biometric Data Requirements Flowchart

Vertical decision flowchart: GDPR compliance pathway for festival biometric systems

🚨 CRITICAL: Pure white background #FFFFFF, clear top-to-bottom flow, YES/NO branches, STOP endpoints, green compliance route, exact regulatory requirements

## STRUCTURE

Top-to-bottom flowchart: START → Q1-Q5 decision questions → STOP or PROCEED node
Each question: Diamond/square + condition text + YES (green) and NO (red) branches
NO branches: Lead to STOP node with fine/violation consequence
YES branches: Continue to next question
Final Q5 YES: Leads to PROCEED node with safeguards box

## FLOW (Top to Bottom)

START (Purple #6B46C1 rounded rect):
"Deploying biometric system at festival?"
YES → Q1, NO → End

Q1 (Blue #4299E1 diamond):
"Biometric collection NECESSARY? (Not just convenient)" [Article 5 Data Minimization]
YES → Q2
NO → STOP "VIOLATION: Data Minimization" (Red #FF6B6B)
  Consequence: €20M or 4% turnover fine
  Explanation: Cannot collect 'just in case'

Q2 (Blue diamond):
"EXPLICIT informed consent? (Before event, clear, affirmative)" [Article 9 Special Category]
YES → Q3
NO → STOP "VIOLATION: Article 9" (Red)
  Consequence: €20M or 4% turnover fine
  Explanation: Biometric = special category (most restrictive)

Q3 (Blue diamond):
"Opt-out WITHOUT penalty? (Alternative entry free/easy)" [Consent Autonomy]
YES → Q4
NO → STOP "VIOLATION: Coercive Consent" (Red)
  Consequence: €20M or 4% turnover fine
  Explanation: Consent cannot be forced/penalized

Q4 (Blue diamond):
"Data MINIMIZED + LIMITED retention? (Auto-delete, not indefinite)" [Article 5 Storage Limitation]
YES → Q5
NO → STOP "VIOLATION: Retention" (Red)
  Consequence: €20M or 4% turnover fine
  Explanation: Must delete unnecessary data on schedule

Q5 (Blue diamond):
"DPIA completed? (Impact assessment documented)" [Article 35 High-Risk]
YES → PROCEED (Green #48BB78)
NO → ⚠️ ELEVATED RISK (Amber #ED8936)
  Complete DPIA before processing

PROCEED NODE (Green rounded rect, white text):
"✅ GDPR COMPLIANCE PATHWAY CLEAR"
"MANDATORY SAFEGUARDS (Non-Negotiable Implementation):"

SAFEGUARDS BOX (Green #48BB78 background, dark text):
1. ENCRYPTION
   - In transit: TLS 1.3+
   - At rest: AES-256
   - Keys: Separate, secure

2. LIMITED RETENTION
   - Max window: 30 days (example)
   - Auto-delete: Scheduled purge
   - Verification: Monthly audit

3. ACCESS CONTROLS
   - Need-to-know basis
   - Role-based access
   - Logging: All access recorded
   - Revocation: Immediate removal

4. BREACH RESPONSE PLAN
   - Detection: Monitoring active
   - Response: 72-hour notification
   - Regulator: DPA notification if high-risk
   - Correction: Improvements implemented

## STYLE

Background: Pure white #FFFFFF
Flow colors:
  - START/PROCEED: Purple #6B46C1 (rounded rect, white text)
  - Questions: Blue #4299E1 diamond (white text)
  - YES branches: Green #48BB78 (green line, white YES label)
  - NO branches: Red #FF6B6B (red line, white NO label)
  - STOP: Dark red with white text
  - Safeguards: Green #48BB78 background
  - Warnings: Amber #ED8936 background

Typography:
  - Questions: Source Sans Pro, 14-16pt, white on blue
  - YES/NO labels: Bold, 12-14pt, white on colored background
  - Consequences: Alert amber, 12-14pt, bold
  - Safeguards: Dark slate #2D3748, 13-14pt, structured list
  - Regulations: Light gray, 11-12pt, small text (Article references)

Shapes:
  - START/PROCEED: Rounded rectangles
  - Questions: Diamonds or rounded squares
  - Consequences: Red rectangles
  - Arrows: Thick, directional, YES=green, NO=red

Diagram Elements:
  - Clear top-to-bottom progression
  - Green path shows compliance route
  - Red branches show violation endpoints
  - Safeguards at end in green box with detailed list
  - Festival context NOT generic flowchart

## ❌ AVOID

Cream/beige backgrounds, horizontal layouts, unclear YES/NO paths, missing regulations/fines, generic flowchart (not festival-specific), unequal node sizes, cluttered safeguards box, text <12pt

## ✅ REFERENCE

Decision tree structure, color-coded branches (green=comply, red=violation), clear endpoint consequences, festival biometric context, safeguards implementation details

---

## REGULATORY ACCURACY (Verify in visual)

**Q1 (Article 5)**: Data minimization - cannot collect unnecessary data
**Q2 (Article 9)**: Special category data - biometric requires explicit consent
**Q3 (Autonomy)**: Cannot coerce consent or penalize refusal
**Q4 (Article 5)**: Storage limitation - must delete on schedule
**Q5 (Article 35)**: DPIA mandatory for high-risk processing

**Fine Amounts** (Verify exact):
- Standard violation: €20M or 4% turnover
- Serious violations: €35M or 7% turnover
- Enforcement: By national Data Protection Authority

**Real Examples** (Include if possible):
- ✅ Danish football (DPA-approved, explicit signage, clear consent)
- ❌ Taylor Swift Rose Bowl (secret scanning, no consent)
- ❌ Clearview AI (mass scraping, indefinite retention, prohibited)
