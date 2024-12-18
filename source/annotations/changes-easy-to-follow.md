# Changes Easy to Follow

## Test Type Performed

Changes are easy to follow.

## Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, color bar, span (i.e, line), text, and arrows.

## Results Summary

Technically, none of the annotations actually change in our examples, but this is a pre-emptive failure because I am confident that there is nothing in place to handle change (if it happened).

## Expected Behavior (Pass/Fail)

- _FAIL_ - Chart changes must be easy to follow. If a chart’s data change is meaningful, it must employ animations for object constancy (no faster than 250ms or longer than 2s). Changes to state must be announced to screen reader users.

## Image or Video of Failure

No evidence, however see "Interactive Context is Not Clear" for a good example of why I anticipate this will fail.

## Steps to Reproduce

If there was some data change for example that updated annotations or the legend, we would expect that some kind of announcement would be made (typically through `aria-live="polite"`). Visual changes, if to the data or otherwise, should provide object constancy for objects that persist but move.

Note that this announcement is (ideally) not made for every single element that changes as a result of one change. A simple "New data has been added to the chart" is good enough for most cases.

Toggling the lines in the legend on and off are an example of when constancy isn't really important (since the metaphor here is that the lines "exit" the chart).

## Guidelines and Standards Used

Changes are not easy to follow [https://chartability.github.io/POUR-CAF/#**changesarenoteasytofollow**](https://chartability.github.io/POUR-CAF/#__changesarenoteasytofollow__)

## Related Evidence

See "Interactive context is not clear" evidence.

## Known or Documented Issues

See "Plot tools: Changes are not easy to follow" evidence.

## Technical Details

- JAWS 2023.2402.1
- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

<!-- ## Notes
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels. -->
