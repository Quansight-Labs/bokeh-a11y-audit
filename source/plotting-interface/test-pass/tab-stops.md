# Tab stops

## Test Type Performed

Appropriate tab stops.

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Plotting interface passes for tab stops.

## Expected Behavior (Pass/Fail)

- _Pass_ - Interactive elements (that represent buttons, links, or selectable features) must have a tab stop, while non-interactive elements must not have a tab stop. Every interactive chart element must NOT have its own tab stop unless the chart is small or the tabs are programmatically revealed (such as having a single tab stop at the root of a chart and then a way to enter further layers or sections of the chart using keyboard controls). At least one tab stop should be

<!-- ## Image or Video of Failure
<video controls src="plot-tools_complex-actions.mp4" title="Title"></video>

## Steps to Reproduce
In this case, we cannot even activate the tools (such as the wheel zoom) with a screen reader. Using a keyboard-only approach (no screen reader), it is possible to activate the wheel zoom tool but then using the wheel zoom is impossible without a mouse pointer. -->

## Guidelines and Standards Used

Inappropriate tab stops [https://chartability.github.io/POUR-CAF/#**inappropriatetabstops**](https://chartability.github.io/POUR-CAF/#__inappropriatetabstops__)

<!-- ## Related Evidence
See "Low contrast interactive elements (critical)," "Low contrast (critical)," "Content is only visual (critical)," "Interaction modality has only one input type (critical)" and later tests we will perform based on using standard HTML.

## Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

## Technical Details

- Chrome Version 129.0.6668.59 (64-bit)
- Windows 11 Build 22631.3958

_Updated as of: September 18th, 2024_

## Notes

While this does pass, the data table does have a keyboard trap. After you tab into the table and navigate to the end, you cannot get out of it to continue "forward" to the next location.
