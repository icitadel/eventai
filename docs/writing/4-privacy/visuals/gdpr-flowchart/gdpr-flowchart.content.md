# VIS-4.2: GDPR Biometric Data Requirements Flowchart

**Infographic Purpose**: Decision-tree flowchart guiding festival organizers through GDPR compliance for biometric systems, showing mandatory checkpoints and exit points for non-compliance, with final safeguards framework.

---

## GDPR Compliance Decision Tree

### START NODE
**Question**: "Deploying biometric system at festival?"
- YES → Q1
- NO → End (No GDPR compliance needed)

---

### Q1: Is Biometric Collection NECESSARY?
**GDPR Article 5(1)(c): Data Minimization**

**Question**: "Is collection necessary (not just convenient)? Not collecting just for 'future use' or 'nice to have'?"

**YES Path**: → Q2
**NO Path**:
- ❌ STOP - VIOLATION
- Consequence: Fines up to €20M or 4% turnover
- Explanation: Data minimization principle requires proving necessity
- Alternative: Use non-biometric methods (security staff, behavioral monitoring, ticket validation)

---

### Q2: Explicit Informed Consent
**GDPR Article 9: Special Category Data**

**Question**: "Attendees gave EXPLICIT, informed consent BEFORE event? (Not just clickthrough, actual affirmative action)"

**Details of Valid Consent:**
- Clear, specific, informed statement (not bundled with terms)
- Freely given (no coercion, no service contingency)
- Easy to withdraw consent without penalty
- Granular (separate consent for each use: security, analytics, marketing)

**Real Examples:**
- ✅ Valid: "We will scan your face for festival security. Separate opt-in for marketing use."
- ✅ Valid: Explicit email confirmation + paper forms at entry
- ❌ Invalid: "Check this box to enter" (pre-checked or mandatory)
- ❌ Invalid: Hidden in 50-page terms of service
- ❌ Invalid: Used for purpose beyond consent (consent for security, used for marketing)

**YES Path**: → Q3
**NO Path**:
- ❌ STOP - VIOLATION (Article 9)
- Consequence: €20M or 4% turnover fine
- Explanation: Biometric data is "special category personal data" - most restrictive category
- Alternative: Don't process biometric data OR restructure consent process

---

### Q3: Right to Opt Out Without Penalty
**GDPR Core Principle: Autonomy**

**Question**: "Can attendees refuse consent without losing access to festival? (No paywall, no penalty)"

**Details:**
- No charging for non-biometric entry (paper ID, manual verification)
- No degraded experience for those who opt out
- Alternative methods must be equally effective
- Cannot pressure/shame people into biometric use

**Real Examples:**
- ✅ Valid: Facial recognition OR manual ID check, both free
- ✅ Valid: "You can opt out without penalty" actually honored in practice
- ❌ Invalid: "You can opt out but you'll wait in 2-hour line" (hidden penalty)
- ❌ Invalid: Manual entry available but "takes 20 minutes" (pseudo-option)
- ❌ Invalid: No alternative provided (effectively mandatory)

**YES Path**: → Q4
**NO Path**:
- ❌ STOP - VIOLATION (Consent/Autonomy)
- Consequence: €20M or 4% turnover fine
- Explanation: Consent cannot be coerced or penalized
- Alternative: Provide genuine, penalty-free alternatives

---

### Q4: Data Minimization & Retention
**GDPR Article 5(1)(e): Storage Limitation**

**Question**: "Only collecting necessary data? Deleting according to schedule? (Not mass collection, not indefinite retention)"

**Details:**
- Collect minimum required (faces only, not additional biometrics)
- Retention window defined (e.g., 30 days post-event max)
- Automatic deletion (not kept "just in case")
- No secondary use without new consent

**Real Examples:**
- ✅ Valid: Facial images collected, stored 30 days, deleted automatically
- ✅ Valid: Images used for real-time entry/security ONLY, not saved
- ❌ Invalid: Collecting full body images, gait analysis, emotional expressions
- ❌ Invalid: "We'll keep them indefinitely for future law enforcement"
- ❌ Invalid: Photos stored long-term for marketing/analytics without consent

**YES Path**: → Q5
**NO Path**:
- ❌ STOP - VIOLATION (Article 5)
- Consequence: €20M or 4% turnover fine
- Explanation: Data minimization requires deleting unnecessary information
- Alternative: Redesign system to collect minimum data, implement automatic deletion

---

### Q5: Data Protection Impact Assessment (DPIA) Completed?
**GDPR Article 35: Mandatory for High-Risk Processing**

**Question**: "Completed formal DPIA? Documented risks and mitigations?"

**DPIA Requirements:**
- Risk assessment: Identify discrimination potential (accuracy bias by demographics)
- Risk mitigation: Controls to address identified risks
- Residual risk evaluation: Remaining issues after mitigations
- Documentation: All findings recorded and retained
- Independent review: Potentially consulted with Data Protection Authority if high residual risk

**Real Examples:**
- ✅ Valid: DPIA shows facial recognition has 3-5% bias by ethnicity, mitigation = manual override for edge cases
- ✅ Valid: Assessment completed before festival, findings documented
- ❌ Invalid: "We assume it's accurate" (no actual assessment)
- ❌ Invalid: DPIA done but not retained or updated
- ❌ Invalid: Identified risks but no mitigations

**YES Path**: → PROCEED (Green box)
**NO Path**:
- ⚠️ ELEVATED RISK - May still proceed but with added scrutiny
- Must complete DPIA before processing
- Alternative: Don't process biometric data until DPIA complete

---

### PROCEED NODE (Green Box)
**✅ GDPR COMPLIANCE PATHWAY CLEAR**

**Conditions Met:**
- ✅ Necessity proven
- ✅ Explicit, informed consent obtained
- ✅ Opt-out available without penalty
- ✅ Data minimized
- ✅ Retention limited
- ✅ DPIA completed

**MANDATORY SAFEGUARDS (Implementation Non-Negotiable)**

1. **Encryption**
   - Data in transit: TLS 1.3+
   - Data at rest: AES-256
   - Keys: Separate from data, secure storage
   - Purpose: Prevent unauthorized access/breach exposure

2. **Limited Retention**
   - Window: Define maximum retention (e.g., 30 days post-event)
   - Automatic deletion: Set system to purge after window
   - Verification: Monthly audit confirming deletion
   - Documentation: Log all deletions for compliance audit

3. **Access Controls**
   - Need-to-know: Only security staff can access
   - Role-based: Different access for security vs. analytics
   - Logging: All access recorded (who, what, when)
   - Revocation: Immediate removal when staff leaves

4. **Breach Response Plan**
   - Detection: Monitoring for unauthorized access attempts
   - Response: Incident response team + procedures documented
   - Notification: Attendees notified within 72 hours if breach
   - Regulator: Data Protection Authority notified if high risk
   - Correction: Implement improvements to prevent recurrence

---

## Flowchart Visual Structure

**Layout**: Top-to-bottom decision tree with yes/no branches

**Color Scheme:**
- START node: Deep purple #6B46C1 (EventAI primary)
- Questions (Q1-Q5): Sky blue #4299E1 (decision points)
- YES paths: Forest green #48BB78 (compliant)
- NO paths: Electric coral #FF6B6B (violation)
- STOP nodes: Dark red (non-compliant endpoint)
- PROCEED node: Forest green with white background (success)

**Typography:**
- Question text: Source Sans Pro, 14-16pt, dark slate
- Yes/No labels: Bold, 12-14pt, white on colored background
- Consequences: Alert amber #ED8936, 12-14pt, bold
- Safeguards: Dark slate, 13-14pt, structured list

**Shapes:**
- START/PROCEED: Rounded rectangles
- Questions: Diamond or rounded squares
- Consequences: Red rectangles
- Arrows: Clear directional flow, labeled YES/NO

**Key Visual Elements:**
- Green path shows compliance route
- Red branches show violation endpoints
- Safeguards box at end (green background, detailed requirements)
- Visual progression: Q1 → Q2 → Q3 → Q4 → Q5 → PROCEED
- Alternative paths clearly marked with STOP/NO labels

---

## Key Regulatory References

**Article 5(1)(c) - Data Minimization**: "Personal data must be adequate, relevant and limited to what is necessary"

**Article 9 - Special Category Data**: "Biometric data can only be processed with explicit consent (Article 9(2)(a)) or for specific purposes (security, identification)"

**Article 9(2)(c) - Opt-Out Right**: "Processing must allow subject to object, and cannot make processing conditional on objection"

**Article 35 - DPIA**: "High-risk processing requires impact assessment"

**Enforcement**:
- Fines: €20M or 4% turnover (standard), €35M or 7% turnover (most serious violations)
- Supervisory Authority: National Data Protection Authority (enforces, investigates, fines)
- Private Right of Action: Attendees can sue for damages

---

## Festival Application Context

**Real Compliance Examples:**

✅ **Approved Approach (Danish Police Football)**
- Explicit signage: "Facial recognition active for security"
- Clear consent requirement: Attendees confirm before entry
- Legitimate purpose: Law enforcement, proven threat level
- Data protection: Limited retention, police DPIA completed
- Opt-out: Manual ID check available
- Result: DPA approval with conditions

❌ **Rejected Approach (Taylor Swift Rose Bowl)**
- No prior consent: Secret facial scanning
- Unclear purpose: "Analytics and marketing" undefined
- No alternatives: Mandatory biometric
- No DPIA: Risk assessment not completed
- Outcome: Public backlash, regulatory investigation

❌ **Rejected Approach (Clearview AI Festivals)**
- Mass scraping: Biometric database built from web photos
- No consent: Users didn't authorize facial data collection
- Indefinite retention: Database kept permanently
- Prohibited use: Real-time identification without legal authority
- Outcome: €35M+ fines, criminal investigation

---

## EventAI Color Palette

- **Primary (START)**: Deep purple #6B46C1
- **Questions**: Sky blue #4299E1
- **Compliance (YES)**: Forest green #48BB78
- **Violation (NO)**: Electric coral #FF6B6B
- **Warning**: Alert amber #ED8936
- **Text**: Midnight slate #2D3748
- **Background**: Pure white #FFFFFF

---

## Context for NotebookLM

**Purpose**: Interactive decision guide for festival compliance

**Tone**: Clear, practical, non-judgmental
- This is a complex regulatory landscape (multiple correct approaches)
- Guide provides framework for thinking through requirements
- Real examples show both compliant and non-compliant scenarios

**Audience**:
- Festival organizers evaluating biometric systems
- Legal teams designing consent processes
- Students learning about privacy regulation
- Privacy officers implementing safeguards

**Use Case**:
- Accompanies "Privacy & Regulation" section
- Provides step-by-step compliance roadmap
- Shows consequences of each violation
- Clarifies safeguards implementation

---

*Source document prepared for NotebookLM infographic generation*
*Target visual: VIS-4.2 in VISUAL-CONTENT-PLAN.md*
*Save as: gdpr-flowchart.png*
