# Phase 1: Acceptance Criteria per Section
**Task:** P1.3 Define Acceptance Criteria per Section
**Created:** 2025-12-27
**Purpose:** Establish verifiable quality standards for all Phase 2 content development

---

## Global Quality Standards (Apply to All Sections)

### Accessibility & Readability
Per `guidance/textboox-bp.research.md` best practices:

- [ ] **Plain language:** Average sentence length 15-20 words; active voice preferred
- [ ] **Cognitive load:** Content chunked into digestible segments (paragraphs 3-5 sentences)
- [ ] **Technical jargon:** All specialized terms defined on first use
- [ ] **Headings:** Clear hierarchy (H1 → H2 → H3) with descriptive labels
- [ ] **Signposting:** Advance organizers at section start; summaries at section end
- [ ] **Avoid unexplained idioms:** Literal language for neurodiversity-inclusive design
- [ ] **Contrast:** If visual elements included, meet 4.5:1 minimum contrast ratio

### Evidence & Source Quality
Per `researchai.instructions.md` protocols:

- [ ] **Source attribution:** Every substantive claim has citation
- [ ] **Confidence levels:** Claims marked High (>80%), Medium (60-80%), Low (<60%)
- [ ] **Verification status:** Sources flagged as Verified, Partially Verified, or Unverified
- [ ] **Tier classification:** Sources categorized as Tier 1/2/3 per P1 inventory
- [ ] **No hallucinations:** All statistics, quotes, case studies verified against sources
- [ ] **Provenance:** Source-to-claim mapping traceable
- [ ] **Gaps acknowledged:** Limitations and uncertainties stated explicitly

### Textbook Pedagogy
Per cognitive science principles:

- [ ] **Worked examples:** Concrete illustrations precede abstract concepts
- [ ] **Scaffolding:** Progressive disclosure from simple to complex
- [ ] **Dual coding:** Text-image integration where applicable
- [ ] **Coherence:** Extraneous material excluded; focus maintained
- [ ] **Advance organizers:** Big picture before details

### Consumer-Oriented Tone

- [ ] **Accessible:** University student (not expert) assumed audience
- [ ] **Engaging:** Avoid dry academic prose; use active constructions
- [ ] **Relevant:** Clear "so what?" connections to festival industry
- [ ] **Balanced:** Present multiple perspectives; acknowledge tradeoffs
- [ ] **Practical:** Theory grounded in real-world application

---

## Topic-Specific Acceptance Criteria

### Topic 1: Transformation (Q1: Long-term AI Vision)

**GIVEN:** `initial/eventai-transformation.md` + P1 inventory analysis
**WHEN:** Draft section complete
**THEN output MUST include:**

#### Content Requirements
- [ ] **Forecast timeline:** Specific milestones 2025-2035 with adoption percentages/market sizes
- [ ] **Attendee-facing differences:** Clear before/after comparison (AI vs. non-AI event experience)
- [ ] **5+ documented case studies:** Real deployments with verifiable details (not hypotheticals)
  - [ ] At least 3 festival-specific (not general events/sports)
  - [ ] Geographic diversity (not all US/EU)
  - [ ] Scale diversity (major + mid-sized events)
- [ ] **Technology categories:** Personalization, safety, operations, content generation
- [ ] **Barrier analysis:** Technical, economic, ethical, regulatory obstacles
- [ ] **Market projections:** Industry-specific data (not generic AI market growth)

#### Evidence Standards
- [ ] **Quantified adoption:** Percentages from industry surveys (not speculation)
- [ ] **Regulatory framework:** EU AI Act, GDPR specifics with effective dates
- [ ] **ROI data:** Documented failure rates (42% zero ROI cited with source)
- [ ] **Case study verification:** Vendor names, dates, venues, outcomes verifiable
- [ ] **Confidence markers:** Mark vendor claims vs. independent validation

#### Quality Metrics
- [ ] Length: 2,500-3,500 words (textbook section-appropriate)
- [ ] Sources: Minimum 15 citations; mix of academic, industry, regulatory
- [ ] Case studies: 3 detailed (200+ words each); 2 brief (100 words)
- [ ] No speculation presented as fact
- [ ] Future predictions clearly labeled as forecasts (not certainties)

#### Prohibited Content
- [ ] NO: Vendor marketing language without critical analysis
- [ ] NO: Unverified statistics or invented examples
- [ ] NO: Technology hype without evidence
- [ ] NO: Ignoring documented failures or risks

---

### Topic 2: Education (Q2: Critical AI Literacy)

**GIVEN:** `initial/eventai-education.md` + `external/unesco-ai-competency-fx.pdf`
**WHEN:** Draft section complete
**THEN output MUST include:**

#### Content Requirements
- [ ] **Clear distinction:** Functional vs. Critical literacy definitions with examples
- [ ] **Five reasons framework:** Why critical literacy is essential for event students
  - [ ] Each reason with event-specific justification (not generic education)
  - [ ] Real-world examples (Taylor Swift surveillance, algorithmic bias cases)
- [ ] **Theoretical grounding:** Freire, Mezirow, UNESCO frameworks explained accessibly
- [ ] **3+ curriculum models:** U. Florida, Harvard Embedded EthiCS, EthAI Tour
  - [ ] Implementation specifics (not just "they have a program")
  - [ ] Assessment methods (how critical literacy is evaluated)
- [ ] **Risks of omission:** Documented harms from functional-only training
- [ ] **Practical integration:** How to embed in existing event management curricula

#### Evidence Standards
- [ ] **UNESCO framework:** Direct citation from 2024 AI Competency Framework
- [ ] **Peer-reviewed frameworks:** Long & Magerko (2020), Ng et al. (2021)
- [ ] **Documented programs:** U. Florida QEP, Harvard course syllabi
- [ ] **Gap acknowledgment:** Limited event management-specific empirical data flagged
- [ ] **Extrapolation clearly marked:** When generalizing from CS/education to hospitality

#### Quality Metrics
- [ ] Length: 2,000-3,000 words
- [ ] Sources: Minimum 12 citations; balance theory + practice
- [ ] Case examples: 5+ brief illustrations of functional vs. critical approaches
- [ ] Frameworks: 3 visual/table summaries (competency models, assessment rubrics)
- [ ] Actionable guidance: Clear steps for curriculum developers

#### Prohibited Content
- [ ] NO: Assuming event management programs have adopted AI literacy (data shows gap)
- [ ] NO: Pure theory without practical application
- [ ] NO: Vendor training programs presented as "education" without critical analysis

#### Special Handling
- [ ] **ESCALATION FLAG:** If synthesis reveals critical data gaps preventing confident claims, escalate before finalizing draft
- [ ] **Limitations section:** Explicitly state where evidence is thin (event management specifics)
- [ ] **Call for research:** Note areas needing further investigation

---

### Topic 3: Personalization (Q3: On-Site Experience)

**GIVEN:** `initial/eventai-personalization.md` (9 case studies)
**WHEN:** Draft section complete
**THEN output MUST include:**

#### Content Requirements
- [ ] **6+ detailed case studies:** Real on-site AI personalization deployments
  - [ ] At least 4 festival-specific (Bonnaroo, SXSW, Coachella, teamLab acceptable)
  - [ ] Mix of technologies (beacons, RFID, mobile apps, environmental sensors)
  - [ ] Scale range (50K-250K+ attendees)
- [ ] **"Organic vs. intrusive" analysis:** What makes personalization feel natural
  - [ ] Explicit design patterns: utility-first, consent architecture, ambient intelligence
  - [ ] Counterexamples: What crosses the line into surveillance
- [ ] **Privacy models:** Anonymous (teamLab), Opt-in (Meow Wolf), Profile-based (Disney)
- [ ] **Outcomes documented:** Engagement rates, visitor counts, behavioral changes
- [ ] **Serendipity preservation:** How AI enhances vs. constrains discovery

#### Evidence Standards
- [ ] **Case study verification:** Cross-reference vendor claims with press/awards
- [ ] **Metrics qualified:** Mark vendor-reported vs. independently validated
- [ ] **Technical specifics:** AWS infrastructure, beacon counts, RFID specs cited
- [ ] **Attendee perspective:** Include documented satisfaction/discomfort data
- [ ] **Failure examples:** At least 1 case of personalization rejection (Red Rocks palm-scan)

#### Quality Metrics
- [ ] Length: 2,500-3,500 words
- [ ] Sources: Minimum 15 citations (case study documentation, press, technical)
- [ ] Case depth: 6 detailed (200-300 words); 3+ brief mentions
- [ ] Comparative analysis: Table or framework comparing privacy/consent models
- [ ] Design principles: 3-5 actionable patterns for "organic" personalization

#### Prohibited Content
- [ ] NO: Vendor success stories without critical analysis
- [ ] NO: Ignoring privacy concerns or surveillance risks
- [ ] NO: Presenting all personalization as positive
- [ ] NO: Hypothetical/speculative implementations as real deployments

#### Special Handling
- [ ] **Survivorship bias note:** Acknowledge focus on successful deployments; failures under-documented
- [ ] **ROI transparency:** State where cost/benefit data is unavailable
- [ ] **Temporal caveat:** Note novelty effects may not sustain long-term

---

### Topic 4: Privacy (Q4: Surveillance Ethics)

**GIVEN:** `initial/eventai-privacy.md` + `eventai-privacy-misuse.md`
**WHEN:** Draft section complete
**THEN output MUST include:**

#### Content Requirements
- [ ] **Seven risk categories:** As documented in source material
  - [ ] Each with real incident examples (Taylor Swift, Robert Williams, MSG)
  - [ ] Quantified harm data (NIST bias rates, wrongful arrest counts)
- [ ] **Regulatory frameworks:** GDPR Art. 9, EU AI Act, BIPA, UNESCO
  - [ ] Specific requirements (explicit consent, storage limits, DPIAs)
  - [ ] Enforcement examples (€20M fines, $650M settlements)
  - [ ] Compliance guidance for organizers
- [ ] **5+ documented incidents:** Wrongful arrests, retaliatory use, discriminatory deployment
- [ ] **Stakeholder perspectives:** Attendees, organizers, civil rights orgs, regulators
- [ ] **Responsible vs. irresponsible:** Clear contrast with design principles
- [ ] **Opt-in success cases:** Internet Economy Summit, KW MAPS (49% opt-in)

#### Evidence Standards
- [ ] **Legal sources:** Direct citation of GDPR articles, EU AI Act text, court cases
- [ ] **Government reports:** NIST FRVT, ACLU studies, Attorney General statements
- [ ] **Documented incidents:** News coverage + legal filings for wrongful arrests
- [ ] **Bias data:** MIT Gender Shades (34.4pp), NIST (10-100x), Big Brother Watch (89%)
- [ ] **No speculation:** Only deployed/documented surveillance systems

#### Quality Metrics
- [ ] Length: 3,000-4,000 words (most evidence-rich topic)
- [ ] Sources: Minimum 25 citations; emphasis on legal/regulatory
- [ ] Incidents: 7+ documented cases with verifiable details
- [ ] Frameworks: GDPR requirements table, EU AI Act prohibitions list
- [ ] Actionable guidance: Checklist for responsible deployment

#### Prohibited Content
- [ ] NO: Surveillance apologia without acknowledging documented harms
- [ ] NO: Vendor privacy claims without independent verification
- [ ] NO: Ignoring racial bias in facial recognition
- [ ] NO: Presenting "implied consent" as adequate under GDPR

#### Special Handling
- [ ] **Balance note:** While sources focus on failures, include opt-in successes to show responsible path
- [ ] **Regulatory currency:** Verify EU AI Act effective dates (Feb 2, 2025)
- [ ] **Intersectionality:** Highlight disproportionate impact on marginalized communities

---

### Topic 5: Analytics (Q5: Predictive Operations)

**GIVEN:** `initial/eventai-analytics.md` + notes
**WHEN:** Draft section complete
**THEN output MUST include:**

#### Content Requirements
- [ ] **Four operational domains:** Dynamic pricing, staffing, inventory, crowd flow
  - [ ] Each with quantified outcomes (78% yield, 66% time reduction, 50% waste, 10-min prediction)
  - [ ] Each with documented deployment example
- [ ] **Festival-specific cases:** At least 3 (Tomorrowland, DICE, Crowd Connected)
  - [ ] If using sports venues (Real Madrid, Golden State Warriors), explicitly discuss transferability
- [ ] **Predictive vs. BI distinction:** Technical architecture differences (real-time, ML training, feedback loops)
- [ ] **ROI documentation:** Forrester TEI (13x ROI), peer-reviewed waste study, independent audits
- [ ] **Implementation complexity:** TCO, integration challenges, failure modes
- [ ] **Vendor evaluation criteria:** How to assess claims vs. reality

#### Evidence Standards
- [ ] **Independent validation:** Forrester study, peer-reviewed Waste Management journal article
- [ ] **Cross-verified metrics:** Multiple vendors showing similar outcomes (waste reduction 23-51%)
- [ ] **Technical specifics:** 1.6B data points, 300K models, API capabilities
- [ ] **Sports-to-festival transfer:** Explicitly argue applicability (don't assume)
- [ ] **Vendor claims qualified:** Mark self-reported vs. third-party validated

#### Quality Metrics
- [ ] Length: 2,500-3,000 words
- [ ] Sources: Minimum 12 citations; balance vendor + independent
- [ ] Case studies: 4 detailed deployments (1 per domain)
- [ ] Metrics table: Comparison across dynamic pricing vendors
- [ ] Evaluation framework: How organizers should assess AI vendors

#### Prohibited Content
- [ ] NO: Vendor marketing metrics without verification discussion
- [ ] NO: Assuming sports venue success = festival success (argue transferability)
- [ ] NO: Ignoring implementation costs and complexity
- [ ] NO: Presenting predictions as perfect (include failure modes)

#### Special Handling
- [ ] **Sports venue caveat:** Clearly mark when extrapolating from stadium to festival context
- [ ] **Forrester study:** Note it's vendor-commissioned (though independent) - provide context
- [ ] **Market projection:** AI in events to $14.2B by 2033 - verify source and methodology
- [ ] **Small festival applicability:** Address whether small/mid-sized can afford/benefit

---

## Cross-Section Quality Assurance

### Consistency Checks (Apply After All Drafts Complete)
- [ ] **Terminology:** Consistent use of "AI" vs. "machine learning" vs. "algorithms"
- [ ] **Citation format:** Uniform style (APA, Chicago, or custom)
- [ ] **Case study overlap:** If same event appears in multiple sections, ensure consistent facts
- [ ] **Tone alignment:** Similar accessibility level across all sections
- [ ] **Evidence hierarchy:** Tier 1/2/3 classification applied uniformly

### Integration Readiness
- [ ] **Cross-references:** Sections acknowledge connections (e.g., Education mentions Privacy risks)
- [ ] **Narrative flow:** Each section could stand alone but also connects to whole
- [ ] **No contradictions:** Check for conflicting claims across sections
- [ ] **Gap documentation:** Consistent acknowledgment of limitations

### Textbook-Specific Requirements
- [ ] **Learning objectives:** Each section has implicit "what students should understand"
- [ ] **Reflection prompts:** Opportunities for critical thinking embedded
- [ ] **Contemporary relevance:** 2024-2025 examples (not outdated cases)
- [ ] **Diverse perspectives:** Not solely Western/US-centric examples

---

## Deliverable Checklist for Each Topic

When presenting draft for human review, package must include:

### 1. Draft Content File (`draft.md`)
- [ ] Complete section draft meeting word count target
- [ ] All inline citations present
- [ ] Confidence levels marked for claims
- [ ] Headings formatted for hierarchy

### 2. Quality Check Report (`qc-report.md`)
- [ ] All acceptance criteria checkboxes with status
- [ ] Gaps identified with rationale
- [ ] Evidence quality assessment
- [ ] Recommended revisions (if any)

### 3. Sources Bibliography (`sources.md`)
- [ ] Complete bibliography with full citations
- [ ] Verification status per source (Verified/Partial/Unverified)
- [ ] Tier classification (1/2/3)
- [ ] Access links where available

### 4. Synthesis Workbook (`synthesis.md`)
- [ ] Raw extracted themes and evidence
- [ ] Source-to-claim mapping
- [ ] Initial gap analysis
- [ ] Note on excluded material (and why)

---

## Review Gate Standards (GATE P2.1 - P2.5)

Each topic gate requires:

### Human Approval Criteria
- [ ] **Content completeness:** All required elements present
- [ ] **Evidence quality:** Appropriate source mix and verification
- [ ] **Accessibility:** Readable by target audience (university students)
- [ ] **Accuracy:** No hallucinations or unverified claims
- [ ] **Balance:** Multiple perspectives; tradeoffs acknowledged
- [ ] **Pedagogy:** Scaffolding, examples, clear explanations

### Risk Assessment
- [ ] **Low risk:** Proceed to next topic
- [ ] **Medium risk:** Minor revisions needed, re-present
- [ ] **High risk:** Substantial rework required or escalate scope questions

### Decision Options
1. **Approve:** Advance to next phase (or next topic if in Phase 2)
2. **Approve with minor edits:** Note specific changes needed
3. **Revise:** Return with detailed feedback
4. **Escalate:** Fundamental scope or quality concerns

---

## Special Escalation Triggers

Automatically escalate to human if:

- [ ] Confidence level < 60% on core claims
- [ ] Unable to verify critical statistics or case studies
- [ ] Contradictory evidence from Tier 1 sources
- [ ] Topic requires out-of-scope primary research
- [ ] Word count >50% over/under target without clear justification
- [ ] Accessibility standards cannot be met without major source limitations

---

**Sign-Off:**
**Task:** P1.3 Complete
**Created by:** Claude Code (Research Lead)
**Date:** 2025-12-27
**Status:** Ready for human review at GATE P1
