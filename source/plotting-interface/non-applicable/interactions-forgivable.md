# Interactions forgivable

## Test Type Performed

Interactions are forgivable.

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Test is not applicable, this is redundant (plot tools fail to allow the user to undo or redo any actions taken but plotting interface tests are not additionally affected).

## Expected Behavior (Pass/Fail)

- _Not Applicable_ - When the visualization is interactive or has the ability to perform a task, the user must be able to both undo or redo their actions in a single process.

## Image or Video of Failure

(similar test provided by plot tools, see below:)

```{video} ../../plot-tools/assets/plot-tools_interactions-forgivable.mp4
:width: 100%
:playsinline:
```

A scatter plot is shown. A mouse cursor hovers over a plot tool called "Wheel Zoom." Using the mouse, a user zooms in on the chart space. The user then hovers over each chart plot tool until it comes to "Reset." They press it and the chart returns to it's default display.

## Steps to Reproduce

N/A

## Guidelines and Standards Used

Interactions are not forgivable [https://chartability.github.io/POUR-CAF/#**interactionsarenotforgivable**](https://chartability.github.io/POUR-CAF/#__interactionsarenotforgivable__)

## Related Evidence

See "Plot tools: Interactions are unforgivable" evidence.

<!-- ## Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

## Technical Details

- Chrome Version 129.0.6668.59 (64-bit)
- JAWS 2023.2402.1
- Windows 11 Build 22631.3958

_Updated as of: September 18th, 2024_

## Notes

This has carry-over from the plot tool testing since they are necessary to interact with the chart.
