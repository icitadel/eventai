# Commit Message Generation

**CRITICAL: Output MARKDOWN SOURCE, not formatted text.**

## Format

```
# [What changed + quantified impact]

## Summary
[1-2 sentences: what, why]

## Impact

**[Category]:**
- [Metric: X → Y or ±N%]
- [Metric: X → Y or ±N%]

**[Category]:**
- [Metric: X → Y or ±N%]
```

## Categories

**Bugs** | **Features** | **Performance** | **Developer Experience** | **Data Quality** | **Automation** | **Security**

## Examples

```
# Fix payment timeouts (27% → 0%)

## Summary
Async pagination eliminates timeouts, 82% faster processing.

## Impact

**Reliability:**
- Timeout errors: 12/week → 0
- Success rate: 73% → 100%

**Performance:**
- Processing: 45s → 8s (82% faster)
```

```
# Add real-time revenue dashboard

## Summary
Live sales metrics during event operations.

## Impact

**Efficiency:**
- Eliminated 2hr post-event reconciliation
- Prevented 3 stockouts via real-time inventory

**Revenue:**
- Identified 4pm-6pm peak (staffing optimization)
- Floats outsell scoops 2:1 after 5pm
```

## Rules

❌ No file lists, test output, next steps
✅ Quantify (X → Y, ±N%), 2-3 categories, markdown source
