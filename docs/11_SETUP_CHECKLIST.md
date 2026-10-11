# ApplyTrack — Pre-Implementation Setup Checklist

## Repository

- [x] Create GitHub repository
- [x] Clone locally
- [x] Create `README.md`
- [x] Create `.gitignore`
- [x] Add `docs/` directory and copy project documents
- [x] Create initial commit

## Backend

- [x] Check Python version
- [x] Create virtual environment
- [x] Activate environment
- [x] Install FastAPI
- [x] Install ASGI server
- [x] Install Pydantic-compatible dependencies as needed
- [x] Create `backend/`
- [x] Create `backend/app/`
- [x] Add `main.py`
- [x] Create `/health`

## Frontend

- [ ] Check Node.js version
- [ ] Create React + TypeScript + Vite app
- [ ] Create `frontend/`
- [ ] Run starter app successfully

## Git workflow

Recommended branches:

```text
main
└── feature/<short-description>
```

Commit example:

```text
feat: add application creation endpoint
```

Avoid giant commits such as:

```text
finished backend frontend auth database
```

## Local environment

Document your actual commands in the README after verifying them.

Expected local architecture:

```text
Browser
   │
   ├── http://localhost:<frontend-port>
   │
   ▼
React
   │
   │ HTTP/JSON
   ▼
FastAPI
   │
   ▼
SQLite
```

## First milestone checklist

Do not start React or PostgreSQL before this is complete:

- [ ] `/health` works
- [ ] Swagger docs open
- [ ] one application can be created through API docs
- [ ] application can be listed
- [ ] application can be fetched by ID
- [ ] application can be updated
- [ ] application can be deleted
- [ ] validation errors are understandable
