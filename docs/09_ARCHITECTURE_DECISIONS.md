# ApplyTrack — Architecture Decision Record

Keep this file updated whenever an important technical choice is made.

## ADR-001 — Start with a monolith

**Decision:** Build one FastAPI backend and one React frontend.

**Reason:** The goal is to learn full-stack fundamentals and request/data flow. Splitting services would create operational complexity without providing learning value at the beginning.

**Status:** Accepted

## ADR-002 — Start with SQLite

**Decision:** Use SQLite for the first database release.

**Reason:** It removes local database setup friction while still teaching relational data, SQLAlchemy, queries, and persistence.

**Later:** Move to PostgreSQL when authentication, deployment, concurrency, or production-like infrastructure becomes relevant.

**Status:** Accepted

## ADR-003 — Store resume files outside the database

**Decision:** Store resume binaries in local filesystem/object storage and metadata in SQL.

**Reason:** This keeps the learning model clear: database stores structured information; storage handles files.

**Status:** Accepted

## ADR-004 — No authentication initially

**Decision:** Build the useful single-user version before introducing users/auth.

**Reason:** Authentication can obscure the first lessons about CRUD, HTTP, database persistence, and frontend/API integration.

**Status:** Accepted

## ADR-005 — Use native fetch initially

**Decision:** Use the browser's `fetch` rather than immediately adding a data-fetching abstraction.

**Reason:** It makes HTTP behavior visible while learning.

**Later:** Introduce a dedicated client/query library only when complexity justifies it.

**Status:** Accepted

## Decision template

Copy this section for future decisions:

```text
## ADR-XXX — Title

Decision:

Reason:

Alternatives considered:

Trade-offs:

Status:

Date:
```
