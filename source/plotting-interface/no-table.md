# No Table

## Test Type Performed

No table (critical).

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Only one table was provided in our interface. A table was not available for every dataset that was visualized. Each chart that uses different data should have a corresponding downloadable dataset or table available.

Lines: fail.

Bar: passes.

Scatter: fails.


## Expected Behavior (Pass/Fail)
- *Fail* - A table must be provided that contains a human-readable version of the data the chart is based on. This may be excluded if the chart title, summary, context, or annotations are sufficient at conveying all relevant information contained in the chart.

## Image or Video of Failure
Figure 1: Line Charts
```{figure} ./assets/plotting-interface_no-table_1.png
:width: 100%
:alt: Two line charts are shown, no tables are present (fails).

Two line charts are shown, no tables are present (fails).
```

Figure 2: Scatter
```{figure} ./assets/plotting-interface_no-table_2.png
:width: 100%
:alt: A scatterplot is shown, no table is present (fails).

A scatterplot is shown, no table is present (fails).
```

## Steps to Reproduce
For each data visualization, first determine if it has a title, subtitle, caption, or explanation provided that *fully* explains the relevant data in the chart and what it is communicating. If not, next determine if the chart uses a unique dataset. If the dataset has not already been represented elsewhere in a table or through a downloadable link with simple data (such as a csv format or equivalent), check if the chart has a corresponding table or downloadable dataset provided. One must be true in order for each chart to pass: there is a complete and thorough textual description provided for the chart within close proximity to the chart or a data table is provided for viewing.

## Guidelines and Standards Used

No table https://chartability.github.io/POUR-CAF/#__notable___critical_

<!-- ## Related Evidence
(Added if additional evidence has already been gathered for related elements. This will not be edited retroactively, however, due to scope creep. This means that the latest issues will have the most Related Evidence listed.)

## Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

## Technical Details
- Chrome Version 127.0.6533.89 (64-bit)
- Windows 11 Build 22631.3958

*Updated as of: Jan 20th, 2025*
