# Activity: Turn a Feature Request into a Sprint Plan (Scrum Master)

## Objective

Convert one plain-English feature request into a **2-week sprint plan** with:

- Sprint Goal
- Sprint Backlog (5–8 stories with point estimates)
- Ceremony Schedule (planning, daily stand-up, refinement, review, retro)
- Definition of Ready (DoR) & Definition of Done (DoD) tailored to AI work
- Risks & impediments with owners and due dates
- Burndown expectation (simple forecast)

## Input

> “We need dark mode in our app so users can read at night without straining their eyes.”

## Steps

1. **Set a Sprint Goal**
   - One sentence that ties the feature to user value and a measurable outcome.
2. **Draft a Sprint Backlog (5–8 items)**
   - Break the feature into thin vertical slices (incl. design, impl, QA).
   - Add **story points** (1–8 scale is fine).
   - Call out any spikes (e.g., accessibility audit).
3. **Plan the Ceremonies**
   - Create a 2-week calendar for: **Planning, Daily Stand-up, Refinement, Review, Retro**.
   - Add owners, timeboxes, and intended outcomes for each.
4. **Define DoR & DoD (AI-aware)**
   - DoR should include: acceptance criteria, data/privacy check, dependencies, test approach.
   - DoD should include: unit/e2e tests, **accessibility checks**, **LLM eval gate (≥ threshold)**, observability, docs.
5. **List Risks & Impediments**
   - 3–5 items with **owner** and **due date**; include at least one **accessibility** and one **theming consistency** risk.
6. **Burndown Expectation**
   - Note assumed team capacity (points) and a one-line forecast of completion risk.

## Timebox

- 10 minutes to draft, 2–5 minutes to polish.

## Deliverable Format

Create `dark_mode_sprint_plan_<team>.md` containing:

```markdown
### Sprint Goal

...

### Sprint Backlog (with points)

| ID  | Title | Points | Notes |
| --- | ----- | ------ | ----- |

...

### Ceremony Schedule (timeboxes, owners, outcomes)

...

### Definition of Ready (DoR)

...

### Definition of Done (DoD)

...

### Risks & Impediments

| Risk | Impact | Owner | Due |
| ---- | ------ | ----- | --- |

...

### Burndown Expectation

- Capacity: ...
- Forecast: ...
```
