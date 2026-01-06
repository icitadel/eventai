# VIS-4.1: EU AI Act Risk Classification

**Infographic Purpose**: Visualize the three-tier EU AI Act risk classification system for biometric systems deployed at festivals, showing prohibition zones, high-risk requirements, and limited-risk scenarios with real regulatory consequences.

---

## EU AI Act Risk Tiers

### Tier 1: PROHIBITED PRACTICES (Top - Red, #FF6B6B)

**Legal Status**: Completely banned as of February 2, 2025

**Real-Time Biometric ID in Public Spaces**
- Facial recognition deployed live at venue
- Flagging attendees during events in real-time
- Matching against watchlists (law enforcement databases)
- Real example: Clearview AI approach (used illegally at US festivals)

**Untargeted Web Scraping (Clearview AI-Style Databases)**
- Mass collection of facial images from internet
- Building biometric databases without consent
- Selling to private event organizers
- Financial penalty: €35M or 7% global turnover (whichever higher)

**Emotion Recognition Systems**
- Detecting emotional states from facial/physiological signals
- Used in workplace, educational, or security contexts
- Can identify sadness, anger, fear for behavioral prediction
- Enforcement: Applies to festival security systems detecting "suspicious" emotions

**Financial Penalty**
- Fine: **€35 million OR 7% of global annual turnover** (whichever is higher)
- Applies to: Both deployment organizations and AI providers
- Timeline: Enforcement began February 2, 2025
- Risk: Existential threat for festivals under threshold; significant financial impact for large organizers

---

### Tier 2: HIGH-RISK (Middle - Orange, #ED8936)

**Legal Status**: Permitted but heavily regulated, requires conformity assessments

**Post-Event Biometric Identification**
- Facial recognition used AFTER events conclude
- Example: Police matching crowd images against databases post-concert
- Used to identify individuals for law enforcement/security purposes
- NOT in real-time (key distinction from prohibited tier)

**Regulatory Requirements**
- Mandatory conformity assessment: Third-party evaluation before deployment
- Technical documentation: Detailed system architecture, training data, accuracy metrics
- Transparent disclosure: Attendees MUST know system exists before using venue
- Data minimization: Collect only necessary images, delete according to retention schedule
- Human oversight: Decisions flagged for human review before law enforcement action
- Impact assessment: Document potential discrimination risks (accuracy bias by demographics)

**Real-World Example**
- Danish police (DPA-approved): Real-time facial recognition at football matches
- Approval conditions: Explicit surveillance notices, law enforcement justification, independent audit
- Result: ✅ Approved because threat level + safeguards justified high-risk deployment

---

### Tier 3: LIMITED RISK (Bottom - Green, #48BB78)

**Legal Status**: Permitted with transparency disclosure (minimal regulatory burden)

**Chatbots with Disclosure**
- AI systems answering festival questions (ticketing, directions, FAQs)
- Must clearly state: "This is an AI chatbot, not human support"
- Applies to: Mobile app bots, website chat assistants, SMS responses
- Low-risk because: Limited autonomy, users aware of AI nature, human escalation available

**Recommendation Systems with Transparency**
- Algorithmic suggestions for artists, schedules, food vendors
- Must disclose: "Recommendations based on algorithm, not human curation"
- Shows alternative options (not just top recommendation)
- Allows user to opt out of algorithmic suggestions
- Example: "Similar artists" on lineup, "You might enjoy..." vendor suggestions

**Why Limited Risk**
- No biometric data collection
- No real-time individual identification
- User agency (can ignore recommendations)
- Clear boundaries (not deceptive marketing)

---

## Visual Structure Recommendation

**Layout**: Three-tier pyramid (top to bottom)

**Proportions**: Equal visual weight (same height per tier)

**Top Tier (Prohibited - Red)**
- Title: "PROHIBITED" (28-32pt bold, white text)
- Stat: "€35M or 7% Turnover Fine" (40-48pt bold, white)
- Practices: Bullet list, white text
  - Real-time biometric ID in public
  - Untargeted web scraping
  - Emotion recognition systems
- Icon: Prohibition symbol, enforcement badge, scales of justice

**Middle Tier (High-Risk - Orange)**
- Title: "HIGH-RISK" (28-32pt bold, dark text)
- Stat: "Requires Conformity Assessment" (32-36pt bold, orange)
- Practices: Bullet list
  - Post-event biometric ID
  - Requirements: Documentation, human oversight, transparency
- Icon: Warning symbol, checklist, audit badge

**Bottom Tier (Limited Risk - Green)**
- Title: "LIMITED RISK" (28-32pt bold, dark text)
- Stat: "Disclosure Only" (32-36pt bold, green)
- Practices: Bullet list
  - Chatbots with AI disclosure
  - Recommendation systems (transparent, user choice)
- Icon: Checkmark, information symbol, disclosure badge

**Context Box (below pyramid)**
- Enforcement Date: February 2, 2025
- Jurisdiction: EU member states
- Applies to: AI providers AND deployment organizations
- Scope: Any AI system deployed at EU festivals

---

## Key Statistics for Visual

**Prohibited Tier:**
- €35 million fine (minimum)
- 7% global turnover (if company larger)
- February 2, 2025 (enforcement date)
- Applies to private organizers (not just law enforcement)

**High-Risk Tier:**
- Requires conformity assessment (independent third-party)
- Documentation requirements (technical specs, training data)
- Real-world example: Danish DPA football match approval (with safeguards)
- NOT approved: Taylor Swift Rose Bowl (no consent, no safeguards)

**Limited-Risk Tier:**
- Disclosure requirement (transparent AI disclosure)
- User choice (algorithms with alternatives)
- No biometric data collection
- Low regulatory burden

---

## EventAI Color Palette

**Prohibited (Top)**
- Background: Electric Coral #FF6B6B
- Text: Pure white #FFFFFF
- Accent: Darker red for emphasis

**High-Risk (Middle)**
- Background: Alert Amber #ED8936
- Text: Midnight Slate #2D3748 (dark for contrast)
- Accent: Orange highlights

**Limited-Risk (Bottom)**
- Background: Forest Green #48BB78 (EventAI green alternative)
- Text: Midnight Slate #2D3748
- Accent: Light green highlights

**Overall**
- Border/outline: Midnight Slate #2D3748 (2-3px)
- White space: 25-30% breathing room
- Background: Pure white #FFFFFF

---

## Typography

- **Tier Titles**: Inter/Roboto, bold, 28-32pt
- **Statistics**: Inter/Roboto, bold, 40-48pt (prohibited), 32-36pt (others)
- **Body text**: Source Sans Pro/Lato, 14-16pt
- **Minimum text size**: 14pt (accessibility requirement)
- **Contrast**: High (dark on light, light on dark)

---

## Design Principles

- Semi-flat style with subtle depth
- Rounded corners (8-12px) on tier boxes
- 2-3px outlines for visual clarity
- Minimal decoration (high data-ink ratio)
- Festival context (not generic legal infographic)
- Professional + authoritative mood (regulatory topic)
- Clear visual hierarchy (prohibition > high-risk > limited-risk)

---

## Context for NotebookLM

**Purpose**: Educational infographic for festival professionals, students, legal teams

**Tone**: Authoritative but accessible
- This is serious regulatory content (enforcement is real)
- Clear explanation of compliance levels
- Real consequences matter for business operations

**Audience**:
- Festival organizers evaluating AI technology
- Legal teams assessing EU compliance
- Students learning about regulation
- Investors evaluating AI company risk

**Use Case**:
- Accompanies "Privacy & Regulation" section
- Explains why certain AI use cases are banned
- Clarifies compliance requirements for each tier
- Provides visual reference for legal obligations

---

*Source document prepared for NotebookLM infographic generation*
*Target visual: VIS-4.1 in VISUAL-CONTENT-PLAN.md*
*Save as: eu-ai-act.png*
