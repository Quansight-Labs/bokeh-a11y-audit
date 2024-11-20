# Narrative Structure

## Test Type Performed

Information cannot be navigated according to narrative or structure.

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Plotting interface does not provide a narrative structure that allows navigation or interaction into the chart and its elements (for keyboard-only and SR modalities). All "navigation" just takes users straight to the plot tools.

## Expected Behavior (Pass/Fail)

- _FAIL_ - Chart must provide a way to be navigated according to its data or narrative structure. The title, description, annotations, and then lower level data structures should be navigable and in that order. Chart data that contains sub-grouping (like a stacked bar chart) or nesting (like a treemap or hierarchy) must provide keyboard navigation that can navigate between levels and/or laterally across levels (in a non-linear fashion). Keyboard navigation must be comparable to the data structure (including cases where the data structure is novel) as well as provide linear or tabular navigation (like in a table or list).

## Image or Video of Failure

<video controls src="./assets/plotting-interface_visual-only.mp4" title="Plotting-interface_Visual-only"></video>
A web browser is shown with multiple charts. A screen reader navigates through the page and through multiple charts, but very limited information is given as they do so (fails).

## Steps to Reproduce

Using a SR or keyboard, press TAB to begin navigating to the chart.

## Guidelines and Standards Used

Information cannot be navigated according to narrative or structure [https://chartability.github.io/POUR-CAF/#**informationcannotbenavigatedaccordingtonarrativeorstructure**](https://chartability.github.io/POUR-CAF/#__informationcannotbenavigatedaccordingtonarrativeorstructure__)

## Related Evidence

See "Content is visual only" evidence.

<!-- ## Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

## Technical Details

- Chrome Version 129.0.6668.59 (64-bit)
- JAWS 2023.2402.1
- Windows 11 Build 22631.3958

_Updated as of: September 18th, 2024_

## Notes

A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.
