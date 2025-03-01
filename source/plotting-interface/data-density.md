# Data Density

## Test Type Performed

Data density is inappropriate (critical).

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Plotting interface fails for the scatter plot density. When in the default view, the patterns and amount of data points creates confusing overlaps, hard to distinguish patterns, and high cognitive load.

## Expected Behavior (Pass/Fail)

- _FAIL_ - Data must be presented at an appropriate density. If more too many elements are competing for the same space (approximate limit is based on cognitive load): clustering or patterns (or lack of) must be explained, chart must be aggregated to a higher level with less elements, or chart must be divided into smaller charts with less data. Visual density should serve a purpose, such as retaining the data's signal (when appropriate).

## Image or Video of Failure

```{figure} ./assets/plotting-interface_meaningful-elements_2.png
:width: 100%
:alt: A scatter plot is shown. A red circle is highlighting an area with three data sets differentiated by squares, circles, and triangles. From this view, it is hard to tell the patterns apart - they all look similar (fails).

A scatter plot is shown. A red circle is highlighting an area with three data sets differentiated by squares, circles, and triangles. From this view, it is hard to tell the patterns apart - they all look similar (fails).
```

<!-- ## Steps to Reproduce
Use Inspect on the plot tool icon to open Console Command. Find the "style" section for the selected button then locate the font size. -->

## Guidelines and Standards Used

Data density is inappropriate (critical) [https://chartability.github.io/POUR-CAF/#**datadensityisinappropriate\_**critical\_](https://chartability.github.io/POUR-CAF/#__datadensityisinappropriate___critical_)

## Related Evidence

See "Meaningful elements can be distinguished from each other" evidence.

<!-- ## Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

## Technical Details

- Chrome Version 129.0.6668.59 (64-bit)
- Windows 11 Build 22631.3958

_Updated as of: September 18th, 2024_

<!-- ## Notes
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.  -->
