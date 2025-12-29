# Commit Message Generation

Generate concise, impact-focused commit messages. No file lists, no testing steps - just observable impact.

## Format

```markdown
# [Brief title: what changed and why it matters]

## Summary
[1-2 sentences: what you did, why it matters]

## Impact

**[Category 1]:**
- [Observable change with quantification]
- [Observable change with quantification]

**[Category 2]:**
- [Observable change with quantification]

**[Category 3]:** (if applicable)
- [Observable change with quantification]
```

## Impact Categories

Choose 2-3 categories that describe observable changes:

**Data Quality** - Fixed calculations, corrected inconsistencies, improved accuracy
**Features** - New capabilities, enhanced functionality, improved UX
**Bugs** - Eliminated errors, fixed broken behavior
**Performance** - Reduced time/memory/resources (with numbers)
**Automation** - Reduced manual work, prevented future errors
**Security** - Fixed vulnerabilities, strengthened protection
**Developer Experience** - Better debugging, clearer code, improved tooling
**Process** - Streamlined workflows, better collaboration

## Examples

### Example 1: Bug Fix
```markdown
# Fix payment timeout errors (27% failure rate → 0%)

## Summary
Implemented async pagination for batch payment processing. Eliminates all timeout failures, reduces processing time 82%.

## Impact

**Reliability:**
- Timeout errors: 12/week → 0
- Batch success rate: 73% → 100%
- Support tickets: Eliminated "missing payment" reports

**Performance:**
- Processing time: 45s → 8s (82% faster)
- Memory usage: 250MB → 100MB peak (60% reduction)
```

### Example 2: Feature
```markdown
# Add real-time revenue dashboard for event staff

## Summary
Live revenue tracking dashboard provides event staff real-time sales metrics during operations.

## Impact

**Operational Efficiency:**
- Eliminated 2-hour post-event reconciliation
- Prevented 3 stockouts in first weekend via real-time inventory awareness

**Revenue Optimization:**
- Identified 4pm-6pm peak hours (optimized staffing)
- Discovered floats outsell scoops 2:1 after 5pm (informed product mix)
```

### Example 3: Refactoring
```markdown
# Refactor business plan validation into JSON rule engine

## Summary
Restructured bizzy-test from monolithic script to pluggable rule engine. Non-developers can now add validation via JSON.

## Impact

**Maintainability:**
- Code complexity: 450 lines → 270 lines (40% reduction)
- Adding validation: 30 lines Python → 5 lines JSON

**Extensibility:**
- Non-technical stakeholders can propose rules via JSON PR
- Targeted validation: run only financial checks, etc.
```

## Key Principles

- ❌ NO file lists (git diff shows this)
- ❌ NO testing commands/output (noise)
- ❌ NO "next steps" sections
- ✅ YES observable impact with numbers
- ✅ YES 2-3 focused impact categories
- ✅ YES concise summaries

## Usage

Say: "Give me a commit message" or "/commit"

I will:
1. Analyze changes
2. Identify 2-3 observable impact categories
3. Quantify improvements
4. Keep it concise
