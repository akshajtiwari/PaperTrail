# ApplyTrack — Gradual Phase Roadmap

The project should be built in very small increments. Do not skip ahead because a later feature looks exciting.

## Phase 0 — Understand the product

Goal: know exactly what is being built before writing code.

Learn:

- client/server model
- HTTP request/response
- REST endpoint concept
- JSON
- CRUD

Deliverables:

- project README
- requirements document
- initial wireframe
- initial database sketch

Exit condition:

You can explain what happens when a user presses “Save Application”.

## Phase 1 — Backend hello world

Goal: create a minimal FastAPI server.

Tasks:

1. Create Python virtual environment.
2. Install FastAPI and server dependency.
3. Create `main.py`.
4. Add `/health` endpoint.
5. Run server.
6. Open automatic API docs.
7. Test endpoint from browser or curl.

Concepts learned:

- ASGI
- routing
- HTTP methods
- status codes
- JSON responses

Exit condition:

You can create and test a new endpoint without looking at a tutorial.

## Phase 2 — First real API without database

Goal: understand CRUD before introducing SQL.

Use an in-memory Python list temporarily.

Tasks:

1. Define application request schema.
2. Define application response schema.
3. Implement create.
4. Implement list.
5. Implement get-by-id.
6. Implement update.
7. Implement delete.
8. Validate missing/invalid values.

Concepts:

- Pydantic models
- request bodies
- path parameters
- query parameters
- response models
- HTTP error responses

Exit condition:

You understand the entire API request/response cycle without the database hiding it.

## Phase 3 — Database fundamentals

Goal: replace the in-memory list with SQLite.

Tasks:

1. Install SQLAlchemy.
2. Create database connection.
3. Create application model.
4. Create table.
5. Create record.
6. Read records.
7. Update records.
8. Delete records.
9. Add basic transaction handling.

Concepts:

- relational tables
- primary keys
- rows/columns
- ORM vs SQL
- sessions
- transactions

Exit condition:

Restarting the backend does not lose applications.

## Phase 4 — Backend structure

Goal: stop treating the backend as one file.

Introduce:

```text
routes → services → database/models
          ↑
        schemas
```

Tasks:

- move routes into routers
- separate schemas from models
- create DB dependency
- create service functions
- introduce configuration

Concepts:

- separation of concerns
- dependencies
- application configuration
- reusable business logic

Exit condition:

You can locate where routing, validation, business rules, and persistence belong.

## Phase 5 — Connect React

Goal: make the browser use your API.

Tasks:

1. Create Vite React TypeScript app.
2. Create basic page.
3. Create application form.
4. Submit with `fetch`.
5. Load applications from API.
6. Render cards/table.
7. Edit application.
8. Delete application.

Concepts:

- component state
- controlled forms
- async requests
- loading/error states
- CORS
- frontend/backend separation

Exit condition:

Creating an application in the browser produces a persisted database record.

## Phase 6 — Quality pass

Goal: improve the small product before expanding it.

Tasks:

- server-side validation
- frontend validation
- consistent error responses
- loading indicators
- empty states
- pagination
- sorting
- filtering

Exit condition:

The app feels reliable even though it is still small.

## Phase 7 — Resume library

Goal: introduce file storage because it directly solves the user's real problem.

Start with local disk only.

Tasks:

1. Create resume metadata table.
2. Build upload endpoint.
3. Validate extension/MIME/size.
4. Store file outside source code.
5. Return metadata.
6. Build resume list UI.
7. Build download endpoint.
8. Link resume to application.

Concepts:

- multipart form data
- file storage
- filesystem paths
- binary responses
- DB/file consistency

Exit condition:

You can create an application and later retrieve the exact resume version attached to it.

## Phase 8 — Saved job description

Goal: preserve application context.

Tasks:

- add job description field
- save pasted JD
- display full saved JD
- add “snapshot saved on” metadata

Concepts:

- text storage
- long-form content
- UI content rendering

Exit condition:

A deleted/changed job page no longer causes you to lose the original job description because your copy is stored.

## Phase 9 — Timeline

Goal: model history rather than only current state.

Tasks:

- create application events table
- add event endpoint
- create automatic “Application created” event
- create automatic status-change event
- render timeline
- allow custom notes/events

Concepts:

- one-to-many relationships
- audit/history thinking
- ordering by time

Exit condition:

Opening an application shows a trustworthy history of what happened.

## Phase 10 — Search and dashboard

Goal: make the product useful at scale.

Tasks:

- search query
- status filter
- date filter
- pagination
- status counts
- recent activity

Concepts:

- SQL filtering
- aggregation
- indexes
- derived UI state

Exit condition:

You can find an application quickly even with hundreds of records.

## Phase 11 — Authentication

Goal: learn real user security after the core product works.

Tasks:

- user table
- registration
- password hashing
- login
- token/session handling
- current-user endpoint
- protect all user-owned resources

Concepts:

- authentication vs authorization
- hashing
- identity
- ownership

Exit condition:

Two users can use the same deployment without seeing each other's data.

## Phase 12 — Reminders/background work

Goal: learn asynchronous processing only when there is an actual use case.

Tasks:

- follow-up dates
- overdue calculations
- background worker
- reminder processing
- optional notifications

Concepts:

- background jobs
- queues
- retries
- idempotency

Exit condition:

A reminder can be generated without the user keeping the browser open.

## Phase 13 — Production infrastructure

Goal: make the project deployable.

Tasks:

- PostgreSQL
- Alembic
- Docker
- Docker Compose
- environment configuration
- health checks
- logs
- deployment

Exit condition:

A fresh machine can run the production-like stack from documented instructions.

## Phase 14 — Optional advanced features

Only choose one or two.

Possible directions:

- Gmail parsing
- browser extension
- calendar events
- job URL import
- automatic email-to-application matching
- resume usage analytics
- application export
- CSV import/export

The project should not become a feature graveyard.
