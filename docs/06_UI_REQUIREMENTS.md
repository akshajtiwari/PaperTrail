# ApplyTrack — UI Requirements

The interface should be simple, functional, and information-dense without looking like a generic AI-generated SaaS dashboard.

## Design principles

- prioritize readability
- keep actions obvious
- avoid excessive cards and gradients
- use consistent spacing
- use tables where tabular information is appropriate
- use timelines where chronology matters
- don't over-design before functionality works

## Phase 5 screens

### 1. Applications page

Must show:

- company
- role
- status
- date applied
- last updated
- action to open details

Primary action:

`Add Application`

### 2. Add application form

Fields:

- Company name — required
- Role title — required
- Application URL — optional
- Date applied — optional during initial implementation
- Status — required
- Notes — optional

Actions:

- Save
- Cancel

Validation should appear near the relevant field.

### 3. Application detail page

Must show:

- company and role
- current status
- application date
- original URL
- notes
- edit action
- delete action

Later it will include:

- resume used
- saved JD
- timeline
- reminders
- attachments

## Phase 7 resume UI

### Resume library

Display:

- resume name
- version
- file type
- size
- created date
- download action

### Resume picker in application form

Show versions clearly, for example:

```text
Backend Resume — v3
ML Resume — v2
General Resume — v5
```

Avoid showing ambiguous labels such as just `resume.pdf`.

## Phase 9 timeline UI

Example:

```text
● Interview completed
  Oct 5, 3:30 PM
  Technical round completed

● OA submitted
  Sep 28, 6:10 PM

● Applied
  Sep 24, 11:40 AM
```

## Interaction states

Every network-driven view needs:

- loading state
- success state where meaningful
- empty state
- error state

Example empty state:

> No applications yet. Add the first one to start tracking your search.

## Mobile behavior

The application should remain usable on a phone, but mobile-specific optimization is secondary to getting desktop behavior correct.
