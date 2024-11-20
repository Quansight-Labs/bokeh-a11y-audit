# Interactive context

## Test Type Performed

Interactive context is not clear.

## Artifact Evaluated

[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769).

## Results Summary

I've decided to "fail" this test even though the demo we have available doesn't actually show a failure of this. The reason for this is because I know why something like a lasso or selection would exist in a chart (often used to cross-filter another or change something about a dataset or interface). For that reason, I'm **failing this without evidence** because I'm pretty sure there isn't anything in place for facilitating communication of whatever a lasso tool accomplishes.

## Expected Behavior (Pass/Fail)

- _FAIL_ - If chart can affect the logic or layout of the page or if receives data or parameters from other UI controls or logic, this must be clearly communicated in text. Alerts or notifications must be provided that can be monitored programmatically without requiring navigation (to notify screen reader users, for example).

## Image or Video of Failure

We don't have evidence of this.

## Steps to Reproduce

Since this was failed without evidence (a sort of pre-emptive failure), here are the steps I'd anticipate:

- Activate something like the lasso tool with a screen reader
- Use the lasso tool within the chart space to select elements
- (Due to the selection, something else on the page changes)
- If an aria-live notification (or equivalent) communicates the important details of the change (where the elements are that changed and what changed, at a high level), then this passes
- If elements that are changed only ever _succeed_ the current interactive context in the navigation order of the page (AKA elements never change something that comes before them), then this will also pass

## Guidelines and Standards Used

Interactive context is not clear [https://chartability.github.io/POUR-CAF/#**interactivecontextisnotclear**](https://chartability.github.io/POUR-CAF/#__interactivecontextisnotclear__)

## Related Evidence

See "Content is visual only (critical)."

Note that "No explanation for purpose or how to read" may appear identical at first to "interactive context is not clear" as well as "No interaction instructions" since these are all in relation to interactive elements (the plot tools). I'll just clarify here the differences (and copy+paste this section into each of these three):

- **No explanation for purpose or how to read**: An explanation must be provided that helps someone interpret _what_ they see. For interactive tools, it is important that users know what a lasso does (before they use it) and how to interpret what they are looking at if they end up using it.
- **Cues and instructions are not provided**: Instructions must be provided that helps someone figure out _how_ to use things that are interactive. For interactive tools that require anything other than standard input (such as inputting text, clicking/pressing a button, visiting somewhere with a link, etc), users should have instructions available somewhere that help them actually perform the relevant actions.
- **Interactive context is not clear**: This is only relevant for communicating interactivity and change that happens _during_ interaction and when that change takes places somewhere other than the current interaction location. A common example of this is cross-filtering, where using a lasso or selection on one chart changes another chart elsewhere. This change will need to be communicated to users, especially screen reader users.

## Known or Documented Issues

(If there is already a github issue created for this test or a related test, it will be listed here.)

## Technical Details

- Chrome Version 127.0.6533.120 (64-bit)
- JAWS 2023.2402.1
- Windows 11 Build 22631.4037

_Updated as of: August 16th, 2024_

## Notes

A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.
