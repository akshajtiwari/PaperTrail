# ApplyTrack — Start Here

This is the execution guide for the first few sessions.

## Session 1 — Design, no serious coding

1. Read `01_PROJECT_REQUIREMENTS.md`.
2. Read Phase 0 and Phase 1 of `02_PHASED_ROADMAP.md`.
3. Draw the first application screen on paper.
4. Write the Application fields.
5. Write the first API endpoints yourself.
6. Mark `P0-01` through `P0-05` as you complete them.

## Session 2 — Backend foundation

1. Create repository.
2. Create Python virtual environment.
3. Install FastAPI and server.
4. Build `/health`.
5. Verify `/docs` works.
6. Commit.

Stop here if you are still unsure what FastAPI is doing.

## Session 3 — First CRUD endpoint

Implement only:

```text
POST /applications
```

Use an in-memory list.

Do not add:

- database
- React
- authentication
- file uploads

Test it from Swagger.

## Session 4 — Finish in-memory CRUD

Add:

```text
GET /applications
GET /applications/{id}
PATCH /applications/{id}
DELETE /applications/{id}
```

Test failure cases too.

## Session 5 — SQLite

Replace the in-memory list with SQLite + SQLAlchemy.

Your milestone is:

> Stop the server, start it again, and the application is still there.

## The first real product milestone

Only after Phases 1–3 are complete should you touch React.

The first visible product milestone should be:

> A browser form creates a real application and the backend persists it in SQLite.

That is the moment the project becomes a full-stack application.
