# Task: Generate API contract from a text description

**Objective**  
Turn a plain-English requirement into a valid **OpenAPI (JSON) spec**, then view it in **Swagger UI**.

---

## Input

> “Build an API for managing to-do tasks with title, description, due date.”

---

## Instructions

### 1) Prompt

Use this exact prompt with your LLM (OpenAI/Bedrock/etc.):

> **“Generate an OpenAPI 3.1 spec in JSON only for: Build an API for managing to-do tasks with title, description, due date.  
> Include CRUD endpoints (/tasks, /tasks/{id}), pagination for listing, request/response schemas, and error examples (400/404/500).  
> Output strictly valid JSON; no markdown or commentary.”**

### 2) Run (choose one runtime)

- **Python** or **Node.js** script that:
  - Sends the **Input** and **Prompt** to the model.
  - Prints the **raw JSON** OpenAPI spec to the console/stdout.
  - (Optional) Validates the output with `JSON.parse` / `json.loads`.

### 3) Preview (Swagger UI)

- Copy the printed JSON.
- Open **editor.swagger.io** → **File** → **Paste JSON** → verify interactive docs **(Try it out)**.
  - **Alternative:** Save as `openapi.json` and run Swagger UI Docker:
    - `docker run -p 8080:8080 -e SWAGGER_JSON=/spec/openapi.json -v ${PWD}/openapi.json:/spec/openapi.json swaggerapi/swagger-ui`
    - Open `http://localhost:8080`.

---

## Deliverables

- `openapi.json` containing the generated spec (valid JSON).
- Screenshot or confirmation of Swagger UI rendering (endpoints visible and testable).

---

## Acceptance Criteria

- OpenAPI version is **3.1.x** with `info`, `paths`, and `components`.
- Endpoints:
  - `GET /tasks` (supports pagination),
  - `POST /tasks`,
  - `GET /tasks/{id}`,
  - `PATCH /tasks/{id}`,
  - `DELETE /tasks/{id}`.
- Schemas include at least:
  - `Task` (id, title, description, dueDate, createdAt, updatedAt),
  - `TaskInput` (title, description, dueDate),
  - `Error` (code, message).
- Common responses implemented: **200/201/204/400/404/500** with example payloads.
- JSON is **strictly valid** (parses without errors) and renders in Swagger UI.

---

## Tips

- Set **temperature = 0** for deterministic output.
- If the model returns text around JSON, re-prompt or extract just the JSON.
- If anything is missing (e.g., pagination parameters), re-run with a refinement prompt.
