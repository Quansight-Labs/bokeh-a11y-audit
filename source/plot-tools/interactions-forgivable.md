# Interactions Forgivable

## Test Type Performed

Interactions are forgivable.

## Artifact Evaluated

[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769).

## Results Summary

Plot tools fail to allow the user to undo or redo any actions taken.

## Expected Behavior (Pass/Fail)

- _FAIL_ - We would expect the plot tools to allow for the ability to undo or redo single actions at a time while interacting with the chart space. Although there is a "Reset" tool, this returns the chart to it's default state and erases all actions a user had previously taken.

## Image or Video of Failure

```{video} ./assets/plot-tools_interactions-forgivable.mp4
:width: 100%
:playsinline:
```

A scatter plot is shown. A mouse cursor hovers over a plot tool called "Wheel Zoom." Using the mouse, a user zooms in on the chart space. The user then hovers over each chart plot tool until it comes to "Reset." They press it and the chart returns to it's default display.

## Steps to Reproduce

Use any plot tool to interact with the chart to change it's view or state.

## Guidelines and Standards Used

Interactions are not forgivable [https://chartability.github.io/POUR-CAF/#**interactionsarenotforgivable**](https://chartability.github.io/POUR-CAF/#__interactionsarenotforgivable__)

## Related Evidence

No related evidence currently.

## Known or Documented Issues

(If there is already a github issue created for this test or a related test, it will be listed here.)

## Technical Details

- Chrome Version 128.0.6613.85 (64-bit)
- Windows 11 Build 22631.3958

_Updated as of: August 27th, 2024_

<!-- ## Notes
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels. -->
