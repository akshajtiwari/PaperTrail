# ApplyTrack — Detailed Project Requirements Document

## 1. Project identity

**Project name:** ApplyTrack

**Project type:** Personal full-stack web application

**Primary user:** A student/job seeker managing multiple applications

**Primary goal:** Maintain a reliable record of every application and its exact submission context.

## 2. Problem statement

When a person applies to many opportunities, application information becomes fragmented across bookmarks, browser history, email, local files, notes, and memory.

Typical problems:

- Forgetting where and when an application was submitted
- Forgetting which resume/CV version was used
- Losing the exact job description
- Losing cover-letter or portfolio context
- Forgetting deadlines or follow-ups
- Not remembering interview stages
- Not knowing the current status of an application
- Having no useful history of previous applications

ApplyTrack centralizes this information into one application record and a timeline of events.

## 3. Product vision

A user should be able to record an application in under two minutes and later reconstruct exactly what they submitted and what happened.

The ideal application page answers five questions immediately:

1. What did I apply for?
2. When did I apply?
3. What did I submit?
4. What happened after I applied?
5. What should I do next?

## 4. Core entities

Initial entities:

- Application
- Resume
- Application Event

Later entities:

- User
- Cover Letter
- Company
- Contact
- Reminder
- Job Description Snapshot
- Application Attachment
- Tag

## 5. Functional requirements by release

### Release 0 — Foundation

The repository and development environment must exist.

Requirements:

- Backend starts locally
- Frontend starts locally
- Git repository initialized
- README explains how to run the project
- Environment variables are separated from source code

Acceptance criteria:

- A new developer can clone the repository and start both applications using the documented steps.

### Release 1 — Application CRUD

The user can create, view, edit, and delete an application.

Required application fields:

- company name
- role title
- application URL
- date applied
- status
- notes
- created timestamp
- updated timestamp

Initial statuses:

- Saved
- Applied
- Assessment
- Interview
- Offer
- Rejected
- Withdrawn

Backend requirements:

- `POST /applications`
- `GET /applications`
- `GET /applications/{id}`
- `PATCH /applications/{id}`
- `DELETE /applications/{id}`

Frontend requirements:

- Application list
- Add application form
- Application detail view
- Edit form
- Delete flow

Important constraints:

- Do not add authentication yet.
- Do not use PostgreSQL yet.
- Do not build a dashboard yet.

### Release 2 — Application quality

Improve the first release before adding more features.

Add:

- field validation
- useful API error messages
- pagination on list endpoint
- sorting by application date
- status filtering
- empty states
- loading states
- confirmation before deletion

Acceptance criteria:

- Invalid requests are rejected with predictable errors.
- The UI communicates loading, success, failure, and empty states.

### Release 3 — Resume library

The user can maintain resume/CV versions and attach the exact version used to an application.

Resume fields:

- id
- name
- version label
- file name
- file path/storage key
- mime type
- file size
- created timestamp
- optional description

Backend capabilities:

- upload resume
- list resumes
- view resume metadata
- download resume
- delete resume

Application capability:

- select a resume when creating/editing an application
- display the resume used on the application detail page

Critical product behavior:

The relationship must be historical. If Resume v3 is later edited or replaced, old applications must still point to the original version record.

### Release 4 — Saved job description

The user can preserve the original job description.

Initial implementation:

- paste job description text into the application
- store it in the database
- display it later in a readable format

Optional later implementation:

- save a raw HTML snapshot or uploaded source document

Requirements:

- The saved description remains available even if the original job posting disappears.
- The UI makes it obvious that the description is a saved snapshot.

### Release 5 — Application timeline

An application gets an event history.

Example:

- Application created
- Applied
- Assessment received
- Assessment submitted
- Interview scheduled
- Interview completed
- Offer received
- Rejected

Each event stores:

- id
- application_id
- event type
- event timestamp
- optional note
- created timestamp

Requirements:

- events appear in chronological order
- users can add custom events
- system-generated events can be created by application actions
- deleting an application must clean up its events according to the database relationship rules

### Release 6 — Dashboard and search

Dashboard requirements:

- total applications
- applications by status
- applications this month
- upcoming follow-ups once reminders exist
- recent applications

Search/filter requirements:

- search company
- search role
- filter status
- filter date range
- sort newest/oldest

Do not overbuild analytics. The dashboard should help the user answer practical questions rather than become a generic analytics screen.

### Release 7 — Authentication and authorization

Authentication should be introduced only after the single-user application works well.

Requirements:

- registration
- login
- logout
- authenticated current-user endpoint
- password hashing
- protected application routes
- user ownership checks

Security requirement:

A user must never be able to retrieve or mutate another user's applications or resumes.

### Release 8 — Reminders and follow-ups

The user can record a follow-up date.

Requirements:

- reminder date/time
- reminder note
- reminder state
- overdue state
- completed state

Later:

- background worker
- email or in-app notifications

### Release 9 — Production readiness

Move from learning-only local infrastructure toward deployable infrastructure.

Requirements:

- PostgreSQL support
- Alembic migrations
- Dockerfiles
- Docker Compose for local services
- production environment configuration
- structured logging
- health endpoint
- error handling
- basic security hardening
- deployment documentation

### Release 10 — Optional integrations

Only after the core system is stable:

- Gmail integration
- automatic application-email matching
- browser extension
- job import from a copied URL
- calendar integration
- portfolio version tracking

These are extensions, not requirements for the initial project.

## 6. Non-functional requirements

### Performance

For the personal deployment, normal CRUD requests should feel immediate and should not require unnecessary round trips.

### Reliability

Data should survive application restarts.

### Security

- never store plaintext passwords
- validate uploaded file types
- limit upload sizes
- prevent path traversal
- never trust user-provided filenames for filesystem paths
- keep secrets in environment variables
- enforce authorization server-side

### Maintainability

Backend code must be separated into logical modules. Avoid putting all routes, models, schemas, and business logic in one file.

Suggested backend structure later:

```text
backend/
  app/
    main.py
    api/
    models/
    schemas/
    services/
    db/
    core/
    tests/
```

## 7. First release data boundary

Release 1 only needs:

```text
Application
  id
  company_name
  role_title
  application_url
  date_applied
  status
  notes
  created_at
  updated_at
```

Do not create the complete future database schema on day one.

## 8. Product success criteria

The project is successful when the developer can:

- create a full-stack feature from database to UI
- explain every request path between browser, backend, and database
- debug common API/database errors independently
- add a new feature without copying a tutorial structure blindly
- run tests before merging changes
- deploy the finished core product

The learning outcome matters as much as the application itself.
