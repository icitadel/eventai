# Research Requests: Gap-Filling for AI in Festivals Chapter

**Purpose:** Catalog targeted research needed to address critical gaps identified during Phase 2 synthesis (P2.1.1 - P2.5.1)

**Status:** 5 requests created; awaiting execution

**Workflow:**
1. Research Lead (Claude Code) creates **.prompt.md files with specific research questions
2. Research Agent (Claude/GPT) executes research using prompts
3. Outputs: **.research.md (findings) + **.sources.md (bibliography) for each request
4. Research Lead integrates findings into section drafts

---

## Request Index

| ID | Title | Topic | Status | Prompt | Research | Sources |
|----|-------|-------|--------|--------|----------|---------|
| RR-01 | Attendee Experience Data | Transformation | 📝 READY | [transformation-attendee.prompt.md](transformation-attendee.prompt.md) | [transformation-attendee.research.md](transformation-attendee.research.md) | [transformation-attendee.sources.md](transformation-attendee.sources.md) |
| RR-02 | Event Management Curricula | Education | 📝 READY | [education-curriculum.prompt.md](education-curriculum.prompt.md) | [education-curriculum.research.md](education-curriculum.research.md) | [education-curriculum.sources.md](education-curriculum.sources.md) |
| RR-03 | Personalization Failures & ROI | Personalization | 📝 READY | [personalization-failures.prompt.md](personalization-failures.prompt.md) | [personalization-failures.research.md](personalization-failures.research.md) | [personalization-failures.sources.md](personalization-failures.sources.md) |
| RR-04 | Opt-In Privacy Systems | Privacy | 📝 READY | [privacy-optin.prompt.md](privacy-optin.prompt.md) | [privacy-optin.research.md](privacy-optin.research.md) | [privacy-optin.sources.md](privacy-optin.sources.md) |
| RR-05 | Festival-Specific Analytics | Analytics | 📝 READY | [analytics-festival.prompt.md](analytics-festival.prompt.md) | [analytics-festival.research.md](analytics-festival.research.md) | [analytics-festival.sources.md](analytics-festival.sources.md) |

---

## RR-01: Attendee Experience Data

**Topic:** Transformation (Q1 - Long-term AI Vision)

**Description:** Fill gap in attendee perspective on AI-enhanced festival experiences; need survey data, qualitative feedback, demographic breakdowns, and mid-sized festival examples beyond Tomorrowland/Coachella/DICE.

**Critical Gap:** Synthesis has strong organizer/vendor perspective but limited attendee voice; need to understand what attendees actually experience and prefer.

**Ideal GPT(s):**
- Claude Sonnet 4.5 (web research + synthesis)
- Perplexity Pro (real-time search for 2024-2025 data)

**Expected Output Length:** 800-1,200 words research + 15-20 sources

**Prompt File:** [transformation-attendee.prompt.md](transformation-attendee.prompt.md)

**Integration Target:** Transformation draft section "What Changes for Attendees: Before AI vs. After AI"

---

## RR-02: Event Management Curricula

**Topic:** Education (Q2 - Critical AI Literacy)

**Description:** Identify event management, hospitality, or tourism programs with AI literacy integration; need syllabi, learning outcomes, assessment methods, and empirical data on effectiveness.

**Critical Gap:** Have general AI literacy frameworks (UNESCO, U. Florida) but no event management-specific curriculum data; cannot make confident claims about industry preparedness without this.

**Ideal GPT(s):**
- Claude Sonnet 4.5 (academic search + synthesis)
- SearchGPT (university program discovery)

**Expected Output Length:** 1,000-1,500 words research + 20-25 sources

**Prompt File:** [education-curriculum.prompt.md](education-curriculum.prompt.md)

**Integration Target:** Education draft section on curriculum models and industry integration

---

## RR-03: Personalization Failures & ROI

**Topic:** Personalization (Q3 - On-Site Experience)

**Description:** Document failed AI personalization deployments, attendee backlash, opt-out rates, discontinued programs, and total cost of ownership data to balance survivorship bias in current sources.

**Critical Gap:** Have 9 success case studies but no failure examples beyond Red Rocks palm-scan; need to understand what doesn't work and why to provide balanced guidance.

**Ideal GPT(s):**
- Claude Sonnet 4.5 (nuanced analysis of failures)
- Perplexity Pro (news coverage of controversies/cancellations)

**Expected Output Length:** 800-1,000 words research + 12-15 sources

**Prompt File:** [personalization-failures.prompt.md](personalization-failures.prompt.md)

**Integration Target:** Personalization draft section on design patterns and "what not to do"

---

## RR-04: Opt-In Privacy Systems

**Topic:** Privacy (Q4 - Surveillance Ethics)

**Description:** Find successful opt-in biometric/surveillance systems at festivals with adoption rates, consent architecture details, GDPR compliance examples, and organizer decision-making rationale.

**Critical Gap:** Heavy focus on failures (Taylor Swift, MSG, wrongful arrests); need responsible implementation examples to show viable path forward beyond "don't do surveillance."

**Ideal GPT(s):**
- Claude Sonnet 4.5 (regulatory compliance analysis)
- Legal research tools if available

**Expected Output Length:** 1,000-1,200 words research + 15-20 sources

**Prompt File:** [privacy-optin.prompt.md](privacy-optin.prompt.md)

**Integration Target:** Privacy draft section "Responsible vs. Irresponsible Implementations"

---

## RR-05: Festival-Specific Analytics

**Topic:** Analytics (Q5 - Predictive Operations)

**Description:** Validate AI analytics deployments at multi-day outdoor festivals (not sports venues) for waste reduction, dynamic pricing, staffing, and crowd flow; analyze sports-to-festival transferability; assess small festival applicability.

**Critical Gap:** Strong sports venue data (Real Madrid, Golden State Warriors) but festival-specific validation limited; food waste data from IKEA/universities, not outdoor festivals with unique challenges.

**Ideal GPT(s):**
- Claude Sonnet 4.5 (technical analysis + transferability assessment)
- Industry-specific search tools

**Expected Output Length:** 1,200-1,500 words research + 20-25 sources

**Prompt File:** [analytics-festival.prompt.md](analytics-festival.prompt.md)

**Integration Target:** Analytics draft section on operational domains + transferability argument

---

## Research Execution Protocol

### For Each Request:

1. **Read prompt file** (**.prompt.md)
2. **Execute research** using specified GPT(s)
3. **Output TWO files:**
   - **.research.md: Findings organized by research questions with confidence levels
   - **.sources.md: Full bibliography with verification status (Tier 1/2/3)
4. **Update this tracker** with completion status
5. **Flag for integration** if findings contradict existing synthesis

### Quality Standards:

- **Source verification:** All claims must be traceable to specific sources
- **Confidence levels:** Mark HIGH/MEDIUM/LOW based on source quality
- **Gaps acknowledged:** State clearly if research question cannot be answered
- **No hallucination:** If data doesn't exist, say so (don't invent)

### Escalation Triggers:

- [ ] Research reveals contradictions with existing synthesis (requires reconciliation)
- [ ] Critical data unavailable despite extensive search (may need to revise claims)
- [ ] New regulatory/legal developments that change framework (2024-2025 updates)

---

## Status Tracking

**Created:** 2025-12-27
**Requests ready:** 5/5
**Research complete:** 0/5
**Integrated into drafts:** 0/5

**Next Action:** Execute research requests (can be parallelized across multiple Claude instances)

**Estimated Time:** 2.5-4 hours total (30-45 min per request)

---

**Research Lead:** Claude Code
**Approval Required:** No (pre-approved research protocol from Phase 1)
**Deliverable:** Integrate findings into drafts before QC phase (P2.1.3 - P2.5.3)
