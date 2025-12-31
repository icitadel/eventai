# Dynamic Pricing Mechanics: System Flow Diagram

Horizontal flow diagram showing dynamic pricing algorithm: real-time inputs → processing (with human review) → pricing outputs. Three vertical lanes: inputs, processing, outputs.

## LAYOUT
- Three vertical lanes: Input Layer (left) | Processing Layer (center) | Output Layer (right)
- Horizontal flow with arrows showing data movement left-to-right
- Processing layer highlights human review (95% reviewed, 85-95% approved)
- Case study callout for Tomorrowland (78% yield improvement)

## INPUT LAYER
- Current demand (sales velocity, inventory, conversion rates)
- Time factors (days to event, day of week, time of day)
- Competitor pricing (real-time price intel)
- Historical patterns (previous year demand, seasonality)
- External factors (weather, social sentiment, macro events)

## PROCESSING LAYER
- Demand forecasting (ML model predicts ticket demand)
- Price elasticity (analyzes demand curves by segment)
- Revenue optimization solver (maximizes price × quantity)
- Human review & approval (95% reviewed, 85-95% approved)
- Implementation & distribution (real-time updates to channels)

## OUTPUT LAYER
- New ticket price (up to 20-30% variance, e.g., $49 → $119 over weeks)
- Real-time updates (recalculates every 1-6 hours, urgency messaging)
- A/B testing (test variants, measure conversion, rollback if <5% lift)
- Results: Yield improvement, revenue per seat, conversion metrics

## KEY STATS
- Tomorrowland: 78% yield improvement
- Revenue per seat: $150 (static) → $265 (dynamic)
- Human review rate: 95% of changes reviewed
- Approval rate: 85-95% (15% rejected for ethical reasons)
- Price variance: 143% markup over weeks (e.g., $49 → $119)
- Weekly variance: ±15-20% common, intra-day: ±5-10% rare
- A/B test win rate: 65-75%
- Conversion lift: +18% with dynamic pricing + urgency messaging
- Customer opposition: 91% → 34% with transparency

## ETHICAL SAFEGUARDS
- Price floor: $35-50 minimum (protects artist economics)
- Price ceiling: $150-200 maximum (prevents price gouging)
- Variance cap: ±20% day-over-day, ±5% intra-hour
- Transparency: Show price history, explain drivers, allow alerts
- Fairness messaging: Price based on WHEN you buy, not WHO you are

## CASE STUDY CALLOUT: TOMORROWLAND
- 78% yield improvement
- Avg ticket: $150 → $265
- Customer opposition: 91% → 34% with pricing transparency
- Key lesson: Dynamic pricing optimal but requires trust/transparency

## MOOD
Clear, educational, showing algorithm + human interaction. Emphasizes accuracy, ethics, and customer trust. High-resolution for curriculum use.
