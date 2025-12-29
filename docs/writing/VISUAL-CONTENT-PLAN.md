# EventAI Visual Content Plan (Lemmy Application)

Comprehensive plan for generating infographics, diagrams, and visual content to accompany the EventAI "AI in Festivals" curriculum using the Lemmy multi-AI content generation system.

**Status**: Planning Phase
**Last Updated**: December 28, 2025
**System**: Lemmy (NotebookLM + Nano Banana)

---

## Philosophy: Dense Visual Integration

Following Edward Tufte's principles and infographics best practices research, the EventAI curriculum will include:

- **High Visual Density**: Every 500-1,000 words accompanied by relevant visual
- **Information-Rich Design**: Visuals that add information, not just decoration
- **Minimal Cruft**: No unnecessary borders, gradients, or generic stock imagery
- **Professional + Whimsy**: Clean layouts with distinctive personality
- **Festival Context**: Visual metaphors and examples from actual events

**Target**: 15-20 infographics/diagrams across 5 topics (3-4 per topic)

---

## Topic 1: Transformation (Long-term AI Future Vision)

**Draft Length**: 3,400 words
**Visual Opportunities**: 4 infographics

### VIS-1.1: AI Adoption Timeline (2025-2035)
**Type**: Timeline Infographic
**Purpose**: Visualize the three phases of AI transformation at festivals

**Content**:
- Phase 1 (2025-2028): Foundation Building
  - Market size: $1.8B → $14.2B
  - Adoption: 45% current → 60-70% by 2028
  - Key developments: EU AI Act, 5G infrastructure, vendor consolidation
- Phase 2 (2028-2032): Mainstream Integration
  - Cross-festival identity, generative AI content, predictive operations
  - Adoption: 85-90% major festivals, 50-60% small festivals
- Phase 3 (2032-2035): Adaptive Ecosystems
  - Real-time program adjustments, environmental responsiveness
  - Adoption: 95%+ major, 70-75% small

**NotebookLM Prompt**: [../lemmy/prompts/notebooklm/infographic.prompt.md](../lemmy/prompts/notebooklm/infographic.prompt.md)
- Detail: Detailed
- Orientation: Landscape
- Style: Timeline with phase markers

**Placement**: After "The Adoption Timeline: 2025-2035" introduction

---

### VIS-1.2: Before AI vs. After AI Festival Experience
**Type**: Comparison Infographic
**Purpose**: Show attendee-facing changes across discovery, on-site, and post-festival

**Content**:
Three sections (Before AI | After AI):
1. **Discovery & Ticketing**
   - Before: Manual browsing, static pricing, hand-made schedules
   - After: AI recommendations (40% of sales), dynamic pricing, auto-schedules
2. **On-Site Experience**
   - Before: Paper maps, uniform experience, manual security
   - After: Real-time wayfinding, personalization, AI crowd monitoring
3. **Post-Festival**
   - Before: Manual photo sharing, generic surveys
   - After: AI-generated highlight reels, hyper-targeted feedback

**NotebookLM Prompt**: Use Comparison template
- Detail: Standard
- Orientation: Portrait (split-screen Before/After)

**Placement**: "What Changes for Attendees" section

---

### VIS-1.3: Barriers to AI Transformation
**Type**: Process/Problem Infographic
**Purpose**: Visualize the 5 major barriers preventing widespread adoption

**Content**:
Pentagon or radial diagram showing:
1. **Economic Constraints**: $566K initial investment, 42% zero ROI
2. **Data Quality**: Training data requirements, cold-start problem
3. **Regulatory Uncertainty**: EU AI Act fines (€35M or 7% revenue)
4. **Technical Complexity**: Integration debt, temporary infrastructure
5. **Ethical Tensions**: Serendipity vs. optimization, filter bubbles

**Nano Banana Prompt**: [../lemmy/prompts/images/diagrams.prompt.md](../lemmy/prompts/images/diagrams.prompt.md)
- Style: Clean conceptual diagram with icons for each barrier
- Festival context: Use festival-relevant metaphors

**Placement**: "The Barriers: Why Transformation Is Not Inevitable" section

---

### VIS-1.4: Confidence Matrix for 2030-2035 Predictions
**Type**: Data Visualization
**Purpose**: Show confidence levels for different AI adoption predictions

**Content**:
Three-tier matrix:

**High Confidence (>80%)**:
- Ticketing/marketing AI: 90%+ adoption by 2030
- Crowd monitoring: Standard at major festivals by 2028
- Dynamic pricing: 70%+ festivals by 2032

**Medium Confidence (60-80%)**:
- Personalized itineraries expected by 2030
- Predictive operations: 10-15% margin improvements
- Regulatory frameworks stabilize by 2027

**Low Confidence (<60%)**:
- Generative AI content mainstream
- Small festival adoption >75% by 2035
- Full real-time program orchestration

**NotebookLM Prompt**: Data visualization template
- Detail: Concise (focus on clarity)
- Orientation: Square

**Placement**: "Conclusion: Realistic Expectations" section

---

## Topic 2: Education (Critical AI Literacy)

**Draft Length**: 3,100 words
**Visual Opportunities**: 4 infographics

### VIS-2.1: Functional vs. Critical AI Literacy
**Type**: Comparison Table/Diagram
**Purpose**: Clearly distinguish the two types of literacy

**Content**:
Two-column comparison:

**Functional AI Literacy** | **Critical AI Literacy**
- Definition: Using tools | Definition: Questioning systems
- Questions: How does it work? | Questions: Whose interests does it serve?
- Festival Example: Use ChatGPT for event descriptions | Festival Example: Evaluate if AI recommendations prioritize sponsors
- Training: MPI/PCMA certificates (7.5 hrs, $300-700) | Training: Proposed semester course (15 weeks)

**NotebookLM Prompt**: Conceptual comparison
- Detail: Standard
- Orientation: Landscape (side-by-side)

**Placement**: "Two Types of AI Literacy" section

---

### VIS-2.2: Academic AI Integration Map
**Type**: Geographic/Institution Map
**Purpose**: Show the 3 universities with AI integration vs. hundreds without

**Content**:
Visual representation:
- **3 programs WITH AI** (highlighted):
  - University of Surrey (UK): VR/AR/AI in Visitor Attraction Management
  - Southern Cross (Australia): Automation/Robotics in Hotel Management
  - Penn State (US): Data Analytics in Hospitality
- **Event Management Programs** (called out separately):
  - Leeds Beckett (UKCEM): ZERO AI modules
  - UCF Rosen: ZERO documented AI content
- **Stat**: 3 out of 100+ hospitality programs = 3% coverage

**Nano Banana Prompt**: Conceptual diagram (not literal map)
- Show disparity: 3 lit-up institutions vs. many darkened
- Festival professional + whimsy style

**Placement**: "The State of Academic AI Integration" section

---

### VIS-2.3: The 71% Skills Gap Cycle
**Type**: Circular/Cyclical Diagram
**Purpose**: Show the vicious cycle between industry and academia

**Content**:
Circular flow diagram:
1. **Industry**: "Universities don't teach AI, we train in-house"
   ↓
2. **University**: "Industry changes too fast, we can't keep up"
   ↓
3. **Graduates**: Lack functional AND critical AI literacy
   ↓
4. **On-the-Job Learning**: From vendors (incentivized to oversell)
   ↓
5. **Failures**: 42% zero ROI, GDPR fines, wrongful arrests
   ↓ (back to 1)

**NotebookLM Prompt**: Process flow/cycle
- Detail: Standard
- Orientation: Square (circular flow)

**Placement**: "The 71% Skills Gap and Who Bears the Cost" section

---

### VIS-2.4: Proposed AI Literacy Curriculum
**Type**: Course Structure Diagram
**Purpose**: Visualize the ideal semester-long course

**Content**:
15-week course breakdown:

**Weeks 1-4: AI Fundamentals**
- What is AI/ML?
- Festival use cases
- Hands-on: Deploy chatbot

**Weeks 5-8: Critical Evaluation**
- Evidence assessment
- Regulatory landscape (GDPR, EU AI Act)
- Case study: Paris 2024

**Weeks 9-12: Ethical Dilemmas**
- Algorithmic bias (NIST study)
- Power and values (dynamic pricing backlash)
- Student project: Ethical assessment

**Weeks 13-15: Industry Perspectives**
- Guest lectures
- Debate: Facial recognition at festivals?
- Final paper: AI deployment policy

**NotebookLM Prompt**: Educational structure
- Detail: Detailed
- Orientation: Portrait

**Placement**: "Ideal State: Functional + Critical Literacy" section

---

## Topic 3: Personalization (On-Site Experience)

**Draft Length**: TBD (estimated 3,000-3,500 words)
**Visual Opportunities**: 3-4 infographics

### VIS-3.1: DICE Recommendation Engine Flow
**Type**: System Diagram
**Purpose**: Show how AI personalization drives 40-41% of ticket sales

**Content**:
Data flow diagram:
- **Input**: Listening history + Past attendance + Social connections + Real-time availability
- **Processing**: AI recommendation algorithm
- **Output**: Personalized festival suggestions (events user didn't search for)
- **Result**: 40-41% of sales (vs. 59% direct search)

**Discovery shift**: Search-based → Algorithmic curation

**Nano Banana Prompt**: Technical diagram with festival context
- Clean data flow with arrows
- Festival imagery (tickets, attendees, music notes)

**Placement**: Personalization deployment section

---

### VIS-3.2: Bonnaroo iBeacon Engagement Metrics
**Type**: Data Visualization (Stats)
**Purpose**: Show the adoption gap: 86% download vs. 20% engagement

**Content**:
Visual statistics:
- **86%** of attendees downloaded app
- **20%** engaged with personalization features
- **66 percentage points** gap (adoption vs. usage)
- **97,000+** notifications sent over 4 days
- **12.6** notifications per user average
- **0** promotional messages in year 1 (trust-building)

**NotebookLM Prompt**: Data-driven infographic
- Detail: Concise (focus on key stats)
- Orientation: Square

**Placement**: Real-world deployment examples

---

### VIS-3.3: Helpful vs. Intrusive Features
**Type**: Comparison/User Feedback Visualization
**Purpose**: Show what attendees actually want vs. what they reject

**Content**:
Two-column visual:

**✅ Helpful (Consistently Praised)**:
- Schedule management (lock screen widgets)
- Artist discovery (Spotify/Apple Music integration)
- Emergency alerts (90% reach for Lollapalooza evacuation)
- Interactive maps (walking time estimates)
- Wayfinding to services

**❌ Intrusive (Consistent Complaints)**:
- Persistent location tracking (battery drain)
- Auto-reset privacy settings
- Over-notification (5/day = 54% retention vs. 1/day = 88%)
- Sponsor spam
- Mandatory app downloads

**Threshold**: User control + Transparency + Frequency limits

**NotebookLM Prompt**: User feedback comparison
- Detail: Standard
- Orientation: Landscape

**Placement**: Attendee experience analysis section

---

### VIS-3.4: Personalization ROI vs. Implementation Barriers
**Type**: Matrix/Quadrant Diagram
**Purpose**: Plot different personalization systems by value and difficulty

**Content**:
Quadrant matrix (Value vs. Ease of Implementation):

**High Value, Easy**:
- AI schedule recommendations
- Artist discovery integrations

**High Value, Hard**:
- Real-time crowd-responsive programming
- Cross-festival portable profiles

**Low Value, Easy**:
- Generic push notifications
- Basic wayfinding

**Low Value, Hard**:
- Facial recognition entry (+ regulatory issues)
- Full surveillance-based personalization

**Nano Banana Prompt**: Business decision matrix
- Professional style with festival context
- Clear quadrant boundaries

**Placement**: Implementation strategy section

---

## Topic 4: Privacy (Surveillance Ethics)

**Draft Length**: TBD (estimated 3,500-4,000 words)
**Visual Opportunities**: 4 infographics

### VIS-4.1: EU AI Act Risk Classification
**Type**: Pyramid/Tier Diagram
**Purpose**: Show the risk-based regulatory framework

**Content**:
Three-tier pyramid:

**🚫 PROHIBITED (Top - Red)**:
- Real-time biometric ID in public spaces (private organizers)
- Clearview AI-style web scraping databases
- Emotion recognition in workplace/education
- **Penalty**: €35M or 7% global turnover

**⚠️ HIGH-RISK (Middle - Orange)**:
- Post-event biometric identification
- **Requirements**: Conformity assessments, documentation, transparency

**✅ LIMITED RISK (Bottom - Green)**:
- Chatbots with disclosure
- Recommendation systems with transparency

**NotebookLM Prompt**: Hierarchical risk framework
- Detail: Standard
- Orientation: Portrait (pyramid)

**Placement**: Regulatory landscape section

---

### VIS-4.2: GDPR Biometric Data Requirements Flowchart
**Type**: Decision Tree/Flowchart
**Purpose**: Guide festival organizers through compliance requirements

**Content**:
Decision flowchart:

START: Deploying biometric system (facial recognition, fingerprint)?
↓
Q1: Is data collection **necessary** (not just convenient)?
- No → STOP (violates necessity principle)
- Yes → Continue
↓
Q2: Do you have **explicit, informed consent**?
- No → STOP (Article 9 violation)
- Yes → Continue
↓
Q3: Can attendees **opt out without penalty**?
- No → STOP (consent not voluntary)
- Yes → Continue
↓
Q4: Is data **minimized** (collect only what's needed)?
- No → STOP (Article 5 violation)
- Yes → Continue
↓
Q5: Have you completed a **DPIA** (Data Protection Impact Assessment)?
- No → STOP (required for high-risk processing)
- Yes → Continue
↓
✅ PROCEED with safeguards: Encryption, limited retention, access controls, breach notification plan

**Nano Banana Prompt**: Technical flowchart for festival context
- Clear yes/no paths
- Festival professional style

**Placement**: Compliance requirements section

---

### VIS-4.3: Consent Architecture Spectrum
**Type**: Spectrum/Scale Diagram
**Purpose**: Show the range from coercive to genuinely voluntary consent

**Content**:
Horizontal spectrum (Coercive ← → Voluntary):

**❌ Coercive** (Left - Red):
- Mandatory facial recognition for entry (no alternative)
- Bundled consent (accept all or get no service)
- Pre-checked boxes
- Hidden in ToS (legal but not informed)

**⚠️ Problematic** (Middle - Orange):
- Default opt-in (requires opt-out action)
- "Soft wall" (penalties for declining, e.g., slower lines)
- Confusing consent interfaces

**✅ Voluntary** (Right - Green):
- Clear opt-in (explicit action required)
- Genuine alternatives (paper tickets, manual entry)
- Granular controls (choose specific data sharing)
- Plain language explanations

**NotebookLM Prompt**: Conceptual spectrum
- Detail: Standard
- Orientation: Landscape

**Placement**: Consent design principles section

---

### VIS-4.4: Privacy vs. Safety Trade-Off Matrix
**Type**: Balancing Scales/Decision Framework
**Purpose**: Help organizers evaluate proportionality

**Content**:
Two-axis evaluation:

**Y-Axis: Safety Threat Level**
- High: Documented violence, terrorism risk (e.g., football hooliganism)
- Medium: Crowd density issues, theft
- Low: General security, convenience

**X-Axis: Privacy Intrusion Level**
- High: Real-time facial recognition, continuous tracking
- Medium: Post-event biometric analysis, anonymous crowd monitoring
- Low: Visible CCTV, manual security

**Guidance**:
- **High Threat + Low Intrusion**: Justified (e.g., visible cameras at documented violent events)
- **Low Threat + High Intrusion**: Not justified (e.g., facial recognition at music festival for convenience)
- **High Threat + High Intrusion**: Requires strict safeguards, regulatory approval (e.g., Paris 2024)

**Example Cases Plotted**:
- Danish DPA: Approved facial recognition for football (High/High with safeguards) ✅
- Danish DPA: Denied facial recognition for concerts (Low/High) ❌
- Taylor Swift Rose Bowl: Secret scanning (Low/High + No consent) ❌

**Nano Banana Prompt**: Decision matrix with case examples
- Professional framework diagram
- Festival context for examples

**Placement**: Proportionality assessment section

---

## Topic 5: Analytics (Predictive Operations)

**Draft Length**: TBD (estimated 3,000-3,500 words)
**Visual Opportunities**: 3-4 infographics

### VIS-5.1: Traditional vs. AI-Powered Analytics
**Type**: Before/After Comparison
**Purpose**: Show the shift from historical to real-time predictive

**Content**:
Side-by-side comparison:

**Traditional Analytics** (Before):
- **Data**: Historical only (last year's sales, weather, attendance)
- **Process**: Manual spreadsheets, static forecasts
- **Timing**: Weeks/months before event
- **Decisions**: Pre-planned, fixed
- **Example**: Order 10,000 beers based on last year

**AI-Powered Analytics** (After):
- **Data**: Real-time + Historical + External (weather, social media, traffic)
- **Process**: Automated ML models, continuous updating
- **Timing**: Real-time during event
- **Decisions**: Dynamic, adaptive
- **Example**: Adjust beer order mid-festival based on sales velocity + weather forecast

**ROI**: 10-15% margin improvement (documented)

**NotebookLM Prompt**: Process comparison
- Detail: Standard
- Orientation: Landscape

**Placement**: Introduction to predictive analytics

---

### VIS-5.2: Dynamic Pricing Mechanics
**Type**: System/Algorithm Diagram
**Purpose**: Show how AI dynamic pricing actually works

**Content**:
Flow diagram:

**Inputs** →
- Current demand (tickets sold/hour)
- Time to event
- Competitor pricing
- Historical patterns
- External factors (artist news, weather)

**AI Processing** →
- Demand forecasting model
- Price elasticity calculation
- Revenue optimization algorithm
- **Human review**: 95% of Qcue price changes reviewed

**Outputs** →
- New ticket price (up to 20-30% variance)
- Real-time updates
- A/B testing for optimization

**Results**:
- Tomorrowland: 78% yield improvement
- Revenue increase vs. static pricing
- BUT: 91% of UK fans oppose (public backlash)

**Nano Banana Prompt**: Technical system diagram
- Clean data flow
- Include human-in-the-loop element

**Placement**: Dynamic pricing section

---

### VIS-5.3: Legion WFM ROI Breakdown
**Type**: Financial/ROI Visualization
**Purpose**: Show costs vs. benefits of AI workforce optimization

**Content**:
Cost-Benefit breakdown (Forrester TEI study):

**Investment (3 years): $566,000**
- Software licenses: $280K
- Implementation: $150K
- Training: $86K
- Maintenance: $50K

**Benefits (3 years): $7.44 million**
- Labor cost optimization: $4.2M
- Reduced overtime: $1.8M
- Improved productivity: $1.1M
- Lower turnover: $340K

**Net ROI: 13x return**
**Payback period: 8 months**

**Caveat**: Only at enterprise scale (millions of transactions)
- Small festivals may not have data volume to achieve ROI

**NotebookLM Prompt**: Financial data visualization
- Detail: Detailed (show breakdown)
- Orientation: Square

**Placement**: Workforce optimization economics

---

### VIS-5.4: Predictive Analytics Use Cases Matrix
**Type**: Grid/Matrix of Applications
**Purpose**: Show the range of predictive analytics applications

**Content**:
Grid showing applications:

**Demand Forecasting**:
- Ticket sales prediction
- Merchandise demand
- Food/beverage consumption
- Parking capacity

**Resource Allocation**:
- Staff scheduling (Legion WFM)
- Vendor placement optimization
- Inventory management
- Security deployment

**Risk Management**:
- Crowd density prediction (10-min advance warning)
- Weather impact forecasting
- Equipment failure prediction
- Financial risk assessment

**Revenue Optimization**:
- Dynamic pricing (Qcue, TickPick)
- Upsell targeting
- Sponsor value optimization
- VIP package pricing

Each cell includes:
- Real vendor/case study example
- Documented ROI (if available)
- Implementation complexity (Low/Med/High)

**NotebookLM Prompt**: Multi-cell infographic
- Detail: Detailed
- Orientation: Landscape (wide grid)

**Placement**: Applications overview section

---

## Production Workflow

### Phase 1: Planning (Current)
- ✅ Identify visual opportunities in each draft
- ✅ Map to infographic types
- ✅ Create prompt specifications
- 📋 Prioritize by pedagogical value

### Phase 2: Source Preparation
- 📋 Extract relevant statistics, quotes, examples from drafts
- 📋 Create structured source documents for NotebookLM upload
- 📋 Organize visual requirements by complexity

### Phase 3: Generation
1. **NotebookLM Infographics** (using [infographic.prompt.md](../lemmy/prompts/notebooklm/infographic.prompt.md))
   - Upload draft sections as sources
   - Apply customization prompts
   - Generate at Detailed level, appropriate orientation
   - Download high-res PNG files

2. **Nano Banana Diagrams** (using [diagrams.prompt.md](../lemmy/prompts/images/diagrams.prompt.md))
   - Create detailed diagram descriptions
   - Apply EventAI style guide (professional + whimsy)
   - Generate via Gemini API (if automated) or manual prompt
   - Review for factual accuracy

### Phase 4: Quality Control
For each visual:
- ✅ **Factual Accuracy**: Data matches sources
- ✅ **Visual Clarity**: Information hierarchy effective
- ✅ **Style Alignment**: Professional + whimsy balance
- ✅ **Accessibility**: Sufficient contrast, non-color-dependent info
- ✅ **Print-Ready**: 300-600 DPI if for print

### Phase 5: Integration
- 📋 Place visuals in appropriate topic/visuals/ folders
- 📋 Reference in drafts with markdown image syntax
- 📋 Add alt text for accessibility
- 📋 Document in visual asset inventory

---

## Style Guide Application

All visuals follow EventAI style principles:

### Professional Elements
- Clean, structured layouts
- Readable typography (max 2 fonts)
- Evidence-based data representation
- Proper attribution and sources

### Whimsical Elements
- Festival-relevant visual metaphors
- Distinctive color palette (to be defined)
- Playful icons where appropriate
- Personality without sacrificing clarity

### Minimal Cruft
- No decorative borders
- No unnecessary gradients
- Functional design only
- High data-ink ratio (Tufte principle)

### Information Density
- Every 500-1,000 words = 1 visual
- Visuals add information, not just decoration
- Dense data presentations with clarity
- Multiple levels of detail (quick scan → deep read)

---

## Estimated Timeline

**Phase 1 (Planning)**: ✅ Complete (this document)
**Phase 2 (Source Prep)**: 2-4 hours
**Phase 3 (Generation)**: 8-12 hours (20 visuals × ~30 min each)
**Phase 4 (QC)**: 3-5 hours
**Phase 5 (Integration)**: 2-3 hours

**Total**: 15-24 hours for complete visual content package

---

## Priority Sequence

Generate in this order for maximum pedagogical impact:

1. **High Priority** (Core Concepts):
   - VIS-1.1: AI Adoption Timeline
   - VIS-2.1: Functional vs. Critical Literacy
   - VIS-4.1: EU AI Act Risk Classification
   - VIS-5.1: Traditional vs. AI-Powered Analytics

2. **Medium Priority** (Supporting Evidence):
   - VIS-1.2: Before/After Festival Experience
   - VIS-3.3: Helpful vs. Intrusive Features
   - VIS-4.2: GDPR Compliance Flowchart
   - VIS-5.2: Dynamic Pricing Mechanics

3. **Lower Priority** (Supplementary):
   - Remaining 12 visuals
   - Additional diagrams as needed

---

## Next Actions

**Immediate** (Next Session):
1. Extract statistics and key points from each draft
2. Create structured source documents for NotebookLM
3. Begin generating high-priority infographics (4 core concepts)
4. Test NotebookLM prompt templates with EventAI content

**Short-Term** (This Week):
5. Complete all 20 planned infographics
6. Review and refine based on quality control
7. Integrate into drafts with proper alt text
8. Document visual asset inventory

**Long-Term** (Next Week):
9. Generate Audio Overviews for each topic
10. Create Video Overviews with visual integration
11. Produce Slide Decks for presentation format
12. Compile complete multi-format content package

---

*Visual Content Plan Status: Planning Complete*
*Next Step: Source preparation for NotebookLM generation*
*System: Lemmy Multi-AI Content Generation*
