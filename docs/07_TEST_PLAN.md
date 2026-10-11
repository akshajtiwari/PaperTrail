# ApplyTrack — Test Plan

Testing is introduced gradually rather than all at once.

## Phase 1–2: manual API testing

Use:

- FastAPI Swagger/OpenAPI docs
- curl
- browser for GET requests where practical

For every endpoint test:

- valid input
- missing required input
- malformed input
- unknown ID
- boundary values

## Phase 3: database behavior tests

Verify:

- create persists
- list retrieves persisted rows
- update persists
- delete removes row
- restart does not erase data

## Phase 5: API integration tests

Use pytest and FastAPI TestClient.

Minimum tests:

- health endpoint returns 200
- create application returns 201
- created application can be retrieved
- list returns created application
- update changes only requested fields
- delete returns 204
- unknown application returns 404
- invalid data returns validation error

## Phase 7: file tests

Test:

- allowed resume upload
- disallowed file type
- oversized file
- download works
- file metadata matches storage
- application correctly references resume
- deleting a resume follows defined behavior

## Phase 9: event tests

Test:

- events are attached to correct application
- events are sorted correctly
- deleting application handles events correctly

## Phase 11: authentication/security tests

Test:

- registration
- duplicate email handling
- password hashing
- successful login
- invalid credentials
- unauthenticated access
- user A cannot access user B data

## Frontend tests

Start testing the frontend only after the main workflow is stable.

Prioritize:

- form validation
- list rendering
- loading state
- error state
- successful creation
- successful deletion

## Definition of a bug fix

A bug is not considered fully fixed until:

1. root cause is understood
2. fix is implemented
3. reproduction steps no longer reproduce it
4. a regression test is added when reasonable
5. the tracker records the lesson if it taught an important concept
