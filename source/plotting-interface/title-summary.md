# Title Summary

## Test Type Performed

Has a title, summary, or caption (critical)

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Plotting tools fails for providing titles, summaries, or captions for screen reader users. All these components are visual only.

## Expected Behavior (Pass/Fail)

- _FAIL_ - We expect a title, summary, context, or caption must be provided in any modality used.

## Image or Video of Failure

```{video} ./assets/plotting-interface_metrics-variables.mp4
:width: 100%
:playsinline:
```

A line chart is shown. A screen reader begins to navigate down through a webpage to get to the chart. Once the user navigates to the chart, they taken to the tools of the chart. No title, metrics, axes labels, etc are given to the user (fails).

## Steps to Reproduce

Using a SR, navigate to the chart space. Explore the chart space as needed.

## Guidelines and Standards Used

No title, summary, or caption (critical) [https://chartability.github.io/POUR-CAF/#**notitlesummaryorcaption\_**critical\_](https://chartability.github.io/POUR-CAF/#__notitlesummaryorcaption___critical_)

## Related Evidence

See "Content is only visual" evidence.

## Known or Documented Issues

"Plot tools: Content is only visual" evidence forms.

## Technical Details

- Chrome Version 129.0.6668.59 (64-bit)
- JAWS 2023.2402.1
- Windows 11 Build 22631.3958

_Updated as of: September 18th, 2024_

## Notes

We fail this overall if it fails for a single modality. In general, I'd also recommend that you provide a summary of the data in the title whenever known beforehand (and appropriate for the intended audience) as opposed to simply describing what the data is, such as "Bachelor's Degrees earned by women in 2010 across fields."
