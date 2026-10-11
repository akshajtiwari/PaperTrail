# ApplyTrack — Master Task Tracker

## Status legend

- `TODO` — not started
- `NEXT` — current focus
- `DOING` — actively implementing
- `BLOCKED` — cannot continue until dependency is resolved
- `DONE` — complete and tested
- `DEFERRED` — intentionally postponed

## Current rule

Only keep **one main task** in `DOING` at a time during the learning phases. This prevents jumping between frontend, backend, database, and infrastructure simultaneously.

## Phase 0 — Product understanding

| ID | Task | Status | Dependency | Notes |
|---|---|---|---|---|
| P0-01 | Read PRD completely | TODO | — | Understand scope |
| P0-02 | Draw application lifecycle on paper | TODO | P0-01 | Create → Apply → Interview → Outcome |
| P0-03 | Sketch first application page | TODO | P0-01 | No visual polish |
| P0-04 | Sketch database table | TODO | P0-01 | Only Release 1 fields |
| P0-05 | Write first 5 API endpoints by hand | TODO | P0-01 | Before implementation |

## Phase 1 — FastAPI foundation

| ID | Task | Status | Dependency | Notes |
|---|---|---|---|---|
| P1-01 | Create repository | Done | P0 complete | |
| P1-02 | Create Python virtual environment | Done | P1-01 | |
| P1-03 | Install FastAPI/server dependencies | Done | P1-02 | |
| P1-04 | Create `/health` | Done | P1-03 | |
| P1-05 | Test with browser/curl | Done | P1-04 | |
| P1-06 | Understand generated API docs | Done | P1-05 | |

## Phase 2 — CRUD API in memory

| ID | Task | Status | Dependency | Notes |
|---|---|---|---|---|
| P2-01 | Define Application input schema | Done | P1 complete | |
| P2-02 | Define Application response schema | TODO | P2-01 | |
| P2-03 | Implement create endpoint | TODO | P2-02 | |
| P2-04 | Implement list endpoint | TODO | P2-03 | |
| P2-05 | Implement get endpoint | TODO | P2-04 | |
| P2-06 | Implement update endpoint | TODO | P2-05 | |
| P2-07 | Implement delete endpoint | TODO | P2-06 | |
| P2-08 | Add validation errors | TODO | P2-07 | |
| P2-09 | Manually test every endpoint | TODO | P2-08 | |

## Phase 3 — SQLite + SQLAlchemy

| ID | Task | Status | Dependency | Notes |
|---|---|---|---|---|
| P3-01 | Configure SQLite | TODO | Phase 2 | |
| P3-02 | Create SQLAlchemy engine/session | TODO | P3-01 | |
| P3-03 | Create Application model | TODO | P3-02 | |
| P3-04 | Create database table | TODO | P3-03 | |
| P3-05 | Replace in-memory create | TODO | P3-04 | |
| P3-06 | Replace list/get | TODO | P3-05 | |
| P3-07 | Replace update/delete | TODO | P3-06 | |
| P3-08 | Restart and verify persistence | TODO | P3-07 | |

## Phase 4 — Backend architecture

| ID | Task | Status | Dependency | Notes |
|---|---|---|---|---|
| P4-01 | Introduce routers | TODO | Phase 3 | |
| P4-02 | Separate models and schemas | TODO | P4-01 | |
| P4-03 | Create DB dependency | TODO | P4-02 | |
| P4-04 | Create service layer where useful | TODO | P4-03 | Avoid unnecessary abstraction |
| P4-05 | Add configuration module | TODO | P4-04 | |
| P4-06 | Add backend README | TODO | P4-05 | |

## Phase 5 — React frontend

| ID | Task | Status | Dependency | Notes |
|---|---|---|---|---|
| P5-01 | Create React TypeScript app | TODO | Phase 4 | |
| P5-02 | Create application list page | TODO | P5-01 | |
| P5-03 | Create add form | TODO | P5-02 | |
| P5-04 | Connect create API | TODO | P5-03 | |
| P5-05 | Connect list API | TODO | P5-04 | |
| P5-06 | Add detail page | TODO | P5-05 | |
| P5-07 | Add edit | TODO | P5-06 | |
| P5-08 | Add delete | TODO | P5-07 | |
| P5-09 | Handle loading/errors | TODO | P5-08 | |
| P5-10 | Resolve CORS properly | TODO | P5-04 | |

## Phase 6 — Quality

| ID | Task | Status | Dependency | Notes |
|---|---|---|---|---|
| P6-01 | Add pagination | TODO | Phase 5 | |
| P6-02 | Add status filter | TODO | P6-01 | |
| P6-03 | Add sorting | TODO | P6-02 | |
| P6-04 | Add empty states | TODO | P6-03 | |
| P6-05 | Add consistent errors | TODO | P6-04 | |
| P6-06 | Add API tests | TODO | P6-05 | |

## Phase 7 — Resume library

| ID | Task | Status | Dependency | Notes |
|---|---|---|---|---|
| P7-01 | Design resume table | TODO | Phase 6 | |
| P7-02 | Create upload endpoint | TODO | P7-01 | |
| P7-03 | Validate file size/type | TODO | P7-02 | |
| P7-04 | Store files outside source tree | TODO | P7-03 | |
| P7-05 | Build resume list UI | TODO | P7-04 | |
| P7-06 | Build download | TODO | P7-05 | |
| P7-07 | Link resume to application | TODO | P7-06 | |
| P7-08 | Verify historical version behavior | TODO | P7-07 | Important |

## Phase 8 — Saved JD

| ID | Task | Status | Dependency | Notes |
|---|---|---|---|---|
| P8-01 | Add JD field | TODO | Phase 7 | |
| P8-02 | Add create/edit UI | TODO | P8-01 | |
| P8-03 | Add full JD view | TODO | P8-02 | |
| P8-04 | Label as snapshot | TODO | P8-03 | |

## Phase 9 — Timeline

| ID | Task | Status | Dependency | Notes |
|---|---|---|---|---|
| P9-01 | Design event model | TODO | Phase 8 | |
| P9-02 | Create event table | TODO | P9-01 | |
| P9-03 | Add event endpoint | TODO | P9-02 | |
| P9-04 | Auto-create key events | TODO | P9-03 | |
| P9-05 | Build timeline UI | TODO | P9-04 | |
| P9-06 | Add custom events | TODO | P9-05 | |

## Phase 10 — Search/dashboard

| ID | Task | Status | Dependency | Notes |
|---|---|---|---|---|
| P10-01 | Search company/role | TODO | Phase 9 | |
| P10-02 | Date filters | TODO | P10-01 | |
| P10-03 | Status filters | TODO | P10-02 | |
| P10-04 | Status counts query | TODO | P10-03 | |
| P10-05 | Dashboard UI | TODO | P10-04 | |

## Phase 11 — Authentication

| ID | Task | Status | Dependency | Notes |
|---|---|---|---|---|
| P11-01 | Design user model | TODO | Phase 10 | |
| P11-02 | Registration | TODO | P11-01 | |
| P11-03 | Password hashing | TODO | P11-02 | |
| P11-04 | Login | TODO | P11-03 | |
| P11-05 | Authenticated current-user | TODO | P11-04 | |
| P11-06 | Protect application routes | TODO | P11-05 | |
| P11-07 | Protect resume routes | TODO | P11-06 | |
| P11-08 | Test cross-user isolation | TODO | P11-07 | |

## Phase 12 — Reminders

| ID | Task | Status | Dependency | Notes |
|---|---|---|---|---|
| P12-01 | Add follow-up date | TODO | Phase 11 | |
| P12-02 | Show upcoming reminders | TODO | P12-01 | |
| P12-03 | Show overdue reminders | TODO | P12-02 | |
| P12-04 | Add background worker | TODO | P12-03 | |
| P12-05 | Add notification mechanism | TODO | P12-04 | Optional initially |

## Phase 13 — Production

| ID | Task | Status | Dependency | Notes |
|---|---|---|---|---|
| P13-01 | Add PostgreSQL configuration | TODO | Phase 12 | |
| P13-02 | Add Alembic | TODO | P13-01 | |
| P13-03 | Write migrations | TODO | P13-02 | |
| P13-04 | Create backend Dockerfile | TODO | P13-03 | |
| P13-05 | Create frontend Dockerfile if needed | TODO | P13-04 | |
| P13-06 | Docker Compose local stack | TODO | P13-05 | |
| P13-07 | Add health checks | TODO | P13-06 | |
| P13-08 | Add structured logging | TODO | P13-07 | |
| P13-09 | Deploy | TODO | P13-08 | |

## Weekly review template

At the end of each work session/week, record:

```text
Week/date:
Current phase:
Tasks completed:
What I learned:
What confused me:
Biggest bug:
Why the bug happened:
How I fixed it:
What I can now explain without help:
Next single task:
```
