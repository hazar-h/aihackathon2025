# Activity: Turn a Feature Request into Backlog Items (12–15 min)

## Objective

Convert one plain-English feature request into **3 user stories with acceptance criteria**, **2 UX design guidelines**, and **1 QA test case**.

## Input

> “We need dark mode in our app so users can read at night without straining their eyes.”

## What you’ll do (simple steps)

1. **Read** the feature request once. Underline the key outcomes (comfort at night, readability).
2. **Draft 3 user stories** (1 sentence each) from different angles, e.g.:
   - manual control (toggle), preference persistence, system auto-theme.
3. **Write acceptance criteria** for each story:
   - Use **trigger → action → expected result** bullets (3–4 bullets/story).
4. **Add 2 UX guidelines** focused on:
   - accessibility/contrast, visual consistency across screens/components.
5. **Create 1 QA test case**:
   - Include **ID**, **Title**, **Preconditions**, **Steps**, **Expected Result** (concise and testable).
6. **Self-check** with the acceptance checklist below.
7. **Submit** your team’s markdown file in the provided folder.

## Timebox

- 10 minutes drafting, 2–5 minutes polish.

## Acceptance checklist (quick self-review)

- [ ] 3 user stories are clear and user-centric (“As a user, I want…”).
- [ ] Each story has 3–4 precise AC bullets with observable outcomes.
- [ ] 2 UX guidelines mention **WCAG/contrast** and **consistency**.
- [ ] 1 QA test case includes **steps** and a concrete **expected result**.
- [ ] Language is implementation-agnostic (no framework/library specifics).

## Deliverable format (submit one file)

Create a single markdown file named: `dark_mode_backlog_<team>.md` containing:

- `### User Stories with Acceptance Criteria`
- `### UX Design Guidelines`
- `### QA Test Case`

> Tip: If you finish early, add **one risk** (e.g., inconsistent theming in third-party views) and **one mitigation** (theme token audit + snapshot tests).
