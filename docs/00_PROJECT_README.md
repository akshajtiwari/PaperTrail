# ApplyTrack — Project Documentation

ApplyTrack is a personal application-management system for tracking internships, jobs, scholarships, hackathons, programs, and other applications.

The core problem it solves is simple:

> After applying, you should still know what you applied for, when you applied, which resume/CV you used, what the original job description said, what happened afterward, and what you need to do next.

This project is intentionally designed as a learning project. The product should become useful while forcing the developer to learn full-stack fundamentals from first principles.

## Primary learning objective

Build the application yourself from an empty repository while learning:

- HTTP and REST APIs
- FastAPI backend development
- Request validation with Pydantic
- SQL and relational database design
- SQLAlchemy ORM
- Database migrations
- React and TypeScript
- Frontend state and API integration
- Authentication and authorization
- File storage and download flows
- Background jobs
- Testing
- Docker
- Deployment
- Basic application security
- Logging and debugging

## Recommended stack

### Initial stack

- Backend: Python + FastAPI
- Database: SQLite
- ORM: SQLAlchemy
- Validation: Pydantic
- Frontend: React + TypeScript + Vite
- Styling: Tailwind CSS
- API client: native `fetch` initially
- Testing: pytest + FastAPI TestClient
- Version control: Git + GitHub

### Later stack

- Production database: PostgreSQL
- Migrations: Alembic
- Background jobs: Redis + Celery or an equivalent queue
- Storage: local filesystem first, object storage later
- Containers: Docker / Docker Compose
- Deployment: a frontend host + backend host + managed PostgreSQL

## Product principles

1. Build the smallest working version first.
2. Do not add infrastructure before the application needs it.
3. Prefer explicit code over abstractions that hide the fundamentals.
4. Every phase should leave the application runnable.
5. Do not add AI until the core product is reliable.
6. Record architectural decisions instead of changing direction silently.
7. A feature is not complete until it is tested and usable through the UI where applicable.

## Non-goals for the first version

Do not build these early:

- AI resume generation
- automatic job scraping
- Gmail integration
- browser extensions
- recommendation engines
- microservices
- Kubernetes
- complex event-driven architecture
- multi-tenant enterprise features

These can become future extensions after the fundamentals are solid.

## Source of truth

When implementation begins, use these documents together:

- `01_PROJECT_REQUIREMENTS.md` — what the product must do
- `02_PHASED_ROADMAP.md` — the learning/build order
- `03_TASK_TRACKER.md` — current work
- `04_DATA_MODEL.md` — database design
- `05_API_CONTRACT.md` — API behavior
- `06_UI_REQUIREMENTS.md` — frontend behavior
- `07_TEST_PLAN.md` — quality requirements
- `08_DEFINITION_OF_DONE.md` — what completion means
- `09_ARCHITECTURE_DECISIONS.md` — decisions and reasons
- `10_LEARNING_LOG.md` — what was learned and what remains unclear
- `11_SETUP_CHECKLIST.md` — environment/repository setup
- `12_BACKLOG.md` — ideas that are deliberately postponed
