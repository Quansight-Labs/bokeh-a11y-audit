# Interactive Context

## Test Type Performed

Interactive context is not clear.

## Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, color bar, span (i.e, line), text, and arrows.

## Results Summary

Annotations fail to communicate that the legend on the double line chart is interactive. There is no communication with a screen reader about these interactive capabilities. Note that this test does pass visually, since the interactive context provides a visual change to the chart. That being said, it _does_ fails in the related "Contrast of interactive elements."

At the very least, 1 change needs to take place, which is to use button elements with toggle ARIA provided (`aria-pressed`). That way, when a screen reader user toggles the button, they get feedback about the state of the button itself. If instructions are provided (see Cues and Instructions) that make it clear the legend manipulates the chart's filtering, then we are good to go. For cases when interaction manipulates content already seen (previous in the navigation order) or content that is not explained, then `aria-live="polite"` with a short description of the state change is a good solution too.

## Expected Behavior (Pass/Fail)

- _FAIL_ - If chart can affect the logic or layout of the page or if receives data or parameters from other UI controls or logic, this must be clearly communicated in text. Alerts or notifications must be provided that can be monitored programmatically without requiring navigation (to notify screen reader users, for example).

## Image or Video of Failure

NOTE: The interactive legend element cannot currently be accessed with a screen reader so we cannot get evidence to show that notifications are or are not being given using this assistive tool.

Figure 1: Interactive context in text

```{figure} ./assets/annotations_interactive-context.png
:width: 100%
:alt: A double line chart is shown. A red box is highlighting the legend on the chart. There is no explanation in the chart space that lets the user now this legend works like a button; each label can be muted on or off (fails).

A double line chart is shown. A red box is highlighting the legend on the chart. There is no explanation in the chart space that lets the user now this legend works like a button; each label can be muted on or off (fails).
```

## Steps to Reproduce

Since we don't have evidence for this test because it is not screen reader accessible, I would assume the button function of the interactive labels would work similarly to the buttons on the toolbar. With this in mind, I expect the legend to preemptively fail because the tool bar is not correctly announcing each tool or allowing the SR to use those buttons.

## Guidelines and Standards Used

Interactive context is not clear [https://chartability.github.io/POUR-CAF/#**interactivecontextisnotclear**](https://chartability.github.io/POUR-CAF/#__interactivecontextisnotclear__)

## Related Evidence

See "Contrast of interactive elements," "Content is visual only (critical)." "Cues and Instructions," and "Explanation for purpose."

Note that "No explanation for purpose or how to read" may appear identical at first to "interactive context is not clear" as well as "No interaction instructions" since these are all in relation to interactive elements. A short summary of these 3 failures:

Explanation and purpose: must explain what the thing is and what it is for.

Cues and instructures: must help the user locate interactive capabilities and understand how to operate it.

Interactive context: when interactions change things around the interaction location, the context and change must be communicated through feedback.

<!-- ## Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

## Technical Details

- JAWS 2023.2402.1
- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

<!-- ## Notes -->
