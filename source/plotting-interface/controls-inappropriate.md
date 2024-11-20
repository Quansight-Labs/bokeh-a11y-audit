# Contrast Inappropriate

## Test Type Performed

Controls are appropriate.

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Plotting interface fails for irrelevant functionality in all charts (besides the data table). For example, we chose the wheel zoom and panning. Users are able to zoom so far out that they can lose the data and not easily be able to return. This currently cannot be tested with SR because the tools cannot be accessed as buttons, but I would expect this to fail.

## Expected Behavior (Pass/Fail)

- _FAIL_ - All controls provided must not be irrelevant to the message, question, or task of the chart. Chart's interactive scope and functionality must not be too broad. The chart should if it can have irrelevant functionality removed.

## Image or Video of Failure

<video controls src="./assets/plot-tools_controls-inappropriate.mp4" title="Plot-tools_controls-inappropriate"></video>
A scatter plot is shown. The mouse cursor hovers over a plot tool called "Pan." Using the mouse, a user pans to the left of the chart (away from the visible data points) into an empty space. They pan to the right until the data points appear again. The user then uses the "Wheel zoom" tool to zoom out until the data points become a small cluster, indistinguishable from one another before zooming in to where the data points disappear once again.

## Steps to Reproduce

Try to understand what the overall purpose of the visualization is, and then try to determine if the interactivity of the tools helps or assists with that purpose in any way.

## Guidelines and Standards Used

Controls are inappropriate [https://chartability.github.io/POUR-CAF/#**controlsareinappropriate**](https://chartability.github.io/POUR-CAF/#__controlsareinappropriate__)

## Related Evidence

See "Interactions are not unforgivable."

## Known or Documented Issues

See "Plot tools: Controls are inapproriate" as well.

## Technical Details

- Chrome Version 129.0.6668.59 (64-bit)
- Windows 11 Build 22631.3958

_Updated as of: September 18th, 2024_

## Notes

We noted these same issues in the plot tools testing, but I wanted to reiterate them here.
