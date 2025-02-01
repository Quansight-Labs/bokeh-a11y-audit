# Location History

## Test Type Performed

Location and history is clear.

## Artifact Evaluated

[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769).

## Results Summary

Plot tools fail to provide any information about what actions have been taken after interacting with the chart.

## Expected Behavior (Pass/Fail)

- _FAIL_ - With plot tools that alter the view of the chart, we would expect some way for the user to understand how they got to their current state. For example, if a user uses the wheel zoom to where they can no longer see data points, there should so some sort of history for them to know how they got to that place or how to recreate it.

## Image or Video of Failure

```{video} ./assets/plot-tools_complex-actions.mp4
:width: 100%
:playsinline:
```
A scatter plot is shown. The mouse cursor hovers over a plot tool called "Wheel Zoom." Using a mouse, a user zooms in and out on the chart space before clicking and panning away from the visible data points into an empty space. There is nothing on the screen that states any action history.

## Steps to Reproduce

Use any plot tools to interact with the chart to change it's view or state.

## Guidelines and Standards Used

Location and history is clear [https://chartability.github.io/POUR-CAF/#**locationandhistoryisclear**](https://chartability.github.io/POUR-CAF/#__locationandhistoryisclear__)

## Related Evidence

See "Changes are not easy to follow" and "Interactive context is not clear" evidence.

## Known or Documented Issues

(If there is already a github issue created for this test or a related test, it will be listed here.)

## Technical Details

- Chrome Version 128.0.6613.85 (64-bit)
- Windows 11 Build 22631.3958

_Updated as of: August 27th, 2024_

<!-- ## Notes
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels. -->
