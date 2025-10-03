## Steps (12–15 minutes)

1. **Import data** (5 rows minimum): category, budget, actual.
2. **Compute variance** per category:
   - `variance = actual - budget`
   - `variance_pct = variance / budget` (show “—” if budget = 0)
3. **Rank by impact**: sort by absolute variance **descending**.
4. **Identify top drivers (Pareto)**:
   - Compute each category’s **share of total variance** (use absolute values).
   - Calculate **cumulative share** and highlight items until you reach ~80%.
5. **Forecast next month** under 3 scenarios (choose one set):
   - **Flat** (0% growth), **Conservative** (−5%), **Growth** (+10%)  
     _(Apply rate to each category’s actuals or to the total—pick one and state it clearly.)_
6. **Summarize**: write 3–5 recommendations (e.g., “cap Marketing by 10% for Q2”, “negotiate Cloud commit discount”, “tighten SaaS seat audits”).
7. **Deliver** a Markdown report with:
   - Assumptions (which scenario method you used)
   - A variance table (category, budget, actual, variance, variance %)
   - Top drivers (Pareto)
   - Forecast table (scenario → projected next-month total)
   - Recommendations (bullet list)

## Timebox

- 10–12 minutes build, 2–3 minutes polish

## Deliverable format

```markdown
### Assumptions

...

### Variance Table (ranked by |variance|)

| Category | Budget | Actual | Variance | Variance % |

### Top Variance Drivers (Pareto 80/20)

1. ...
2. ...

### Next-Month Forecast

| Scenario | Growth Rate | Projected Total |

### Recommendations

- ...
- ...
```
