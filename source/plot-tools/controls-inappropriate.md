# Controls Inappropriate

## Test Type Performed

Controls are appropriate.

## Artifact Evaluated

[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769).

## Results Summary

Plot tools fail for irrelevant functionality. For example, we chose the wheel zoom and panning. Users are able to zoom so far out that they can lose the data and not easily be able to return. This currently cannot be tested with SR because the tools cannot be accessed as buttons, but I would expect this to fail.

## Expected Behavior (Pass/Fail)

- _FAIL_ - We would expect the tools functionality to match the analitical goals of the particular environment they are being used in.

## Image or Video of Failure

```{video} ./assets/plot-tools_controls-inappropriate.mp4
:width: 100%
:playsinline:
```

A scatter plot is shown. The mouse cursor hovers over a plot tool called "Pan." Using the mouse, a user pans to the left of the chart (away from the visable data points) into an empty space. They pan to the right until the data points appear again. The user then uses the "Wheel zoom" tool to zoom out until the data points become a small cluster, indistinguishable from one another before zooming in to where the data points disappear once again.

## Steps to Reproduce

Try to understand what the overall purpose of the visualization is, and then try to determine if the interactivity of the tools helps or assits with that purpose in any way.

## Guidelines and Standards Used

Controls are inappropriate [https://chartability.github.io/POUR-CAF/#**controlsareinappropriate**](https://chartability.github.io/POUR-CAF/#__controlsareinappropriate__)

## Related Evidence

See "Interactions are not forgivable."

## Known or Documented Issues

(If there is already a github issue created for this test or a related test, it will be listed here.)

## Technical Details

- Chrome Version 128.0.6613.85 (64-bit)
- Windows 11 Build 22631.3958

_Updated as of: August 27th, 2024_

## Notes

This is something I'm not sure fits anywhere above, but I wanted to explore the question of the scope of the plot tools. Is infinite zoom or panning needed? What contexts are those useful and how can we find balance between those and visualizations (like the scatter plot test environment) where there are finite data sets?
