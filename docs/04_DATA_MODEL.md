# ApplyTrack — Data Model

This document describes the intended data model, but implementation must be introduced phase by phase.

## Phase 3 model — only Application

```text
applications
────────────────────────────────
id                  PK
company_name       TEXT NOT NULL
role_title         TEXT NOT NULL
application_url    TEXT NULL
date_applied       DATE NULL
status             TEXT NOT NULL
notes              TEXT NULL
created_at         DATETIME NOT NULL
updated_at         DATETIME NOT NULL
```

## Phase 7 model — Resume

```text
resumes
────────────────────────────────
id                  PK
name               TEXT NOT NULL
version_label      TEXT NULL
original_filename  TEXT NOT NULL
storage_key        TEXT NOT NULL
mime_type          TEXT NOT NULL
file_size          INTEGER NOT NULL
description        TEXT NULL
created_at         DATETIME NOT NULL
```

Add to applications:

```text
resume_id          FK → resumes.id, nullable initially
```

### Why nullable initially?

Existing applications created before resume support must continue to work.

## Phase 9 model — Application Event

```text
application_events
────────────────────────────────
id                  PK
application_id     FK → applications.id
event_type         TEXT NOT NULL
timestamp          DATETIME NOT NULL
note               TEXT NULL
created_at         DATETIME NOT NULL
```

## Phase 11 model — User

```text
users
────────────────────────────────
id                  PK
email              TEXT UNIQUE NOT NULL
password_hash      TEXT NOT NULL
created_at         DATETIME NOT NULL
```

Later add `user_id` to owned records:

```text
applications.user_id
resumes.user_id
```

## Optional later entities

### Cover letters

```text
cover_letters
────────────────────────────────
id
user_id
name
version_label
storage_key
mime_type
file_size
created_at
```

### Reminders

```text
reminders
────────────────────────────────
id
application_id
scheduled_for
note
status
created_at
completed_at
```

### Contacts

```text
contacts
────────────────────────────────
id
user_id
name
company
email
linkedin_url
notes
created_at
```

## Relationship map

```text
User
 ├──────────────< Application
 │                   └──────────< ApplicationEvent
 │                   ├────────── Resume
 │                   └──────────< Reminder
 │
 └──────────────< Resume
```

## Database rules

1. Use real foreign keys for relationships.
2. Define deletion behavior explicitly.
3. Store timestamps consistently.
4. Do not store a file's complete binary contents in the database for the initial version.
5. Store a stable storage key/path reference instead.
6. Never depend on the user's original filename as a filesystem identifier.
7. Do not add tables merely because they might be useful someday.

## Example application record

```json
{
  "id": 17,
  "company_name": "Example Corp",
  "role_title": "Backend Engineering Intern",
  "application_url": "https://example.com/jobs/123",
  "date_applied": "2026-10-02",
  "status": "Applied",
  "notes": "Applied through campus portal"
}
```
