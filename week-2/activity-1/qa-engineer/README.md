# Activity: Turn a Feature Request into QA Test Assets

## Objective

Take a plain-English feature request and transform it into:

- A mini **test plan** (types of tests + priorities)
- A **boundary table** (edge conditions for key fields)
- 1 detailed **API test case** in JSON format

## Input

> “We need dark mode in our app so users can read at night without straining their eyes.”

## Steps

1. **Read** the feature request and identify what needs to be tested.
   - Think in terms of functional, edge, and error cases.
2. **Draft a mini test plan**:
   - 3–5 test cases (happy, edge, error) with IDs, Titles, Type, Priority, Preconditions, Steps, Expected.
3. **Create a boundary table** for key inputs (e.g., theme preference, toggle state, system setting).
   - Columns: Field | Min | Max | Null/Empty | Invalid.
4. **Write 1 API test case in JSON format** for the Dark Mode toggle API (assume endpoint `/settings/theme`).
   - Include: id, method, path, payload, expectedStatus, assertKeys.
5. **Save** your work as a Markdown file:  
   `dark_mode_tests_<team>.md`

## Timebox

- 10 minutes drafting
- 2–5 minutes polish

## Deliverable Format

````markdown
### Mini Test Plan

...

### Boundary Table

...

### API Test JSON

```json
[
  { "id": "...", "method": "...", "path": "...", "payload": {...}, "expectedStatus": 200, "assertKeys": ["..."] }
]
```
````
