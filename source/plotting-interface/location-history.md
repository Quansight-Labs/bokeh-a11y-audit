# Location History

## Test Type Performed

Location and history is clear.

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Plotting interface fails to provide any information about what actions have been taken after navigating or interacting with the chart. For example, if a user uses the wheel zoom to where they can no longer see data points, there should be some sort of history for them to know how they got to that place or how to recreate it.

In addition, the interactive scatterplot can change glyph size and select species but provides no way to return to defaults or "work backwards" through an interactive process without refreshing the page and starting over.

## Expected Behavior (Pass/Fail)

- _FAIL_ - With interfaces that have altered views of charts, we would expect some way for the user to understand how they got to their current state.

- Current location in a system is not easy to understand. Similar to “more than one process” and “easy to share and reproduce,” current view and state of visualization (in a complex environment like a dashboard or app) must provide the user with breadcrumbs to guide their path as well as the ability to save, reload, and navigate history.

## Image or Video of Failure

<video controls src="./assets/plot-tools_complex-actions.mp4" title="Plot-tools_Complex-actions"></video>
A scatter plot is shown. The mouse cursor hovers over a plot tool called "Wheel Zoom." Using a mouse, a user zooms in and out on the chart space before clicking and panning away from the visible data points into an empty space. There is nothing on the screen that states any action history.

## Steps to Reproduce

Use any plot tools to interact with the chart to change it's view or state.

## Guidelines and Standards Used

Location and history is clear [https://chartability.github.io/POUR-CAF/#**locationandhistoryisclear**](https://chartability.github.io/POUR-CAF/#__locationandhistoryisclear__)

## Related Evidence

See "Changes are not easy to follow" and "Interactive context is not clear" evidence.

<!-- ## Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

## Technical Details

- Chrome Version 129.0.6668.59 (64-bit)
- JAWS 2023.2402.1
- Windows 11 Build 22631.3958

_Updated as of: September 18th, 2024_

## Notes

This has carry-over from the plot tool testing since they are necessary to interact with the chart.
