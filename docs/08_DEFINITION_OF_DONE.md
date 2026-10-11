# ApplyTrack — Definition of Done

A task can be marked `DONE` only when the applicable criteria are satisfied.

## Code

- implementation is complete
- code is readable
- no debug prints remain unless intentionally used for logging
- unused imports/code removed
- naming is consistent

## Behavior

- happy path works
- expected failure cases are handled
- validation is present where necessary
- UI communicates the result

## Testing

- relevant manual test performed
- automated test added when the phase requires it
- no known regression introduced

## Documentation

For meaningful features, document:

- what was built
- why it exists
- important implementation choices
- known limitations

## Git

Before marking a milestone complete:

- changes are committed
- commit message describes the change
- repository remains runnable

## Learning

The developer should be able to explain:

- what changed
- why it changed
- what data flows through the system
- at least one alternative design and why it was not chosen

A feature copied from a tutorial without being understood does not satisfy this definition of done.
