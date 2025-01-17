# Metrics Variables

## Test Type Performed

Metrics and variables are defined.

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Plotting interface fails for defining metrics and variables when using a SR. SR users are not able to access any information about the chart - titles, axes names, axes metrics or variables, etc.

## Expected Behavior (Pass/Fail)

- _FAIL_ - Metrics or variables must not be misleading or undefined. Chart must not lie and data (and source) must be defined. Metadata, metrics, calculations, and variables must be defined.

## Image or Video of Failure

```{video} ./assets/plotting-interface_metrics-variables.mp4
:width: 100%
:playsinline:
```

A line chart is shown. A screen reader begins to navigate down through a webpage to get to the chart. Once the user navigates to the chart, they are taken to the tools of the chart. No title, metrics, axes labels, etc are given to the user (fails).

## Steps to Reproduce

Using a SR, navigate to the chart space. Explore the chart space as needed.

## Guidelines and Standards Used

Metrics and variables are undefined [https://chartability.github.io/POUR-CAF/#**metricsandvariablesareundefined**](https://chartability.github.io/POUR-CAF/#__metricsandvariablesareundefined__)

## Related Evidence

See "Content is only visual" evidence.

<!-- ## Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

## Technical Details

- Chrome Version 129.0.6668.59 (64-bit)
- JAWS 2023.2402.1
- Windows 11 Build 22631.3958

_Updated as of: September 18th, 2024_

## Notes

We fail this overall if it fails for a single modality.
