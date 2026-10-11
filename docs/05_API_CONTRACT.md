# ApplyTrack — API Contract

This contract is intentionally small for the first implementation. Expand it only when a phase requires it.

Base URL during local development:

```text
http://localhost:8000
```

## Health

### GET `/health`

Response:

```json
{
  "status": "ok"
}
```

## Applications

### POST `/applications`

Purpose: create an application.

Example request:

```json
{
  "company_name": "Example Corp",
  "role_title": "Backend Engineering Intern",
  "application_url": "https://example.com/job/123",
  "date_applied": "2026-10-02",
  "status": "Applied",
  "notes": "Applied through campus portal"
}
```

Expected response: created resource with generated `id` and timestamps.

### GET `/applications`

Initial behavior:

- return all applications
- newest first once date sorting is implemented

Later query parameters:

```text
?page=1&page_size=20
?status=Interview
?search=google
?sort=date_applied_desc
```

### GET `/applications/{id}`

Purpose: fetch one application.

404 behavior:

```json
{
  "detail": "Application not found"
}
```

### PATCH `/applications/{id}`

Purpose: partially update mutable fields.

Example:

```json
{
  "status": "Interview",
  "notes": "Interview scheduled for Friday"
}
```

### DELETE `/applications/{id}`

Purpose: delete an application.

Expected status: `204 No Content` after successful deletion.

## Resume API — Phase 7

### POST `/resumes`

Content type: multipart form data.

Responsibilities:

- validate upload
- create metadata record
- store file

### GET `/resumes`

Return resume metadata only.

### GET `/resumes/{id}`

Return metadata.

### GET `/resumes/{id}/download`

Return the file as a binary response with safe download headers.

### DELETE `/resumes/{id}`

Delete according to the defined file/record consistency policy.

## Event API — Phase 9

### GET `/applications/{id}/events`

Return events chronologically.

### POST `/applications/{id}/events`

Example:

```json
{
  "event_type": "Interview completed",
  "timestamp": "2026-10-05T15:30:00",
  "note": "Technical round completed"
}
```

## API conventions

### HTTP status codes

Use status codes intentionally:

- `200` successful read/update
- `201` successful creation
- `204` successful deletion with no response body
- `400` malformed/general client request where appropriate
- `401` unauthenticated once auth exists
- `403` authenticated but not authorized
- `404` resource not found
- `409` conflict where relevant
- `413` payload too large for oversized upload
- `422` validation failure when using FastAPI/Pydantic validation
- `500` unexpected server failure

### Error shape

For custom errors, prefer a predictable structure:

```json
{
  "detail": "Human-readable message"
}
```

Do not expose stack traces to users.

## API design rule

Before implementing an endpoint, write down:

1. method
2. URL
3. input
4. validation
5. success status
6. response body
7. failure cases

This is part of the learning process.
