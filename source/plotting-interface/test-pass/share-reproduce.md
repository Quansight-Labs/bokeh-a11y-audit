# Share Reproduce

## Test Type Performed

State is not easy to share and reproduce.

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Plotting interface provides downloadable charts.

## Expected Behavior (Pass/Fail)

- _Pass_ - Chart state must be easy to share and reproduce. If an analysis or complex interaction can produce a customized view, this view must be easy to share (such as with a single link, file, or saved state).

<!-- ## Image or Video of Failure
<figure>
    <img width="803" alt="A browser Command Console window is open. A red line is highlighting the font size '12px' (passes)" src="./assets/plot-tools_text-size.png">
    <figcaption>A browser Command Console window is open. A red line is highlighting the font size '12px' (passes).</figcaption>
</figure> -->

<!-- ## Steps to Reproduce
Use Inspect on the plot tool icon to open Console Command. Find the "style" section for the selected button then locate the font size. -->

## Guidelines and Standards Used

State is not easy to share and reproduce [https://chartability.github.io/POUR-CAF/#**axislabelsareunclearormissing**](https://chartability.github.io/POUR-CAF/#__axislabelsareunclearormissing__)

<!-- ## Related Evidence
(Added if additional evidence has already been gathered for related elements. This will not be edited retroactively, however, due to scope creep. This means that the latest issues will have the most Related Evidence listed.)

## Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

## Technical Details

- Chrome Version 129.0.6668.59 (64-bit)
- JAWS 2023.2402.1
- Windows 11 Build 22631.3958

_Updated as of: September 18th, 2024_

## Notes

Downloading the current state of the chart is an awesome feature for accessibility, but I also recommend adding url queries to any online application/demo where people are able to manipulate the view of a chart or charts as well. For example, if plot tools are used to change the coordinates or view of a chart or (for the scatterplot) if dropdowns/tabs or other interface elements can be interacted with to change the application state, that exact state can be accessed by someone else simply by sharing the user's current URL. Google maps (accessed via browser) is incredible at this. They encode zoom, angle of view, coordinates, and current user selection in the URL for the sake of sharing interaction state.
