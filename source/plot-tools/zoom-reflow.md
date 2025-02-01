# Zoom Reflow

## Test Type Performed
Zoom and reflow are supported.

## Artifact Evaluated
[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769).

## Results Summary
Plot tools fail to reflow to fit different screen sizes, a mobile phone in this case. The font becomes too small to read without zooming, and the chart alignment shifts off center (compared to a desktop screen view). When zooming, no intelligent reflow takes place at all.

## Expected Behavior (Pass/Fail)
- *FAIL* - We expect that the plot tools (along with the chart) would stay on screen regardless of changes in device. In the case of zoom, ideally intelligent reflow would move the buttons to a better position.

## Image or Video of Failure 
```{figure} ./assets/plot-tools_zoom-reflow.png
:width: 100%
:alt: A mobile web browser is shown with five different charts. The font size of most text is too small to read. At the bottom, one of the charts is aligned far to the right, cutting off parts of the image from view (fails).

A mobile web browser is shown with five different charts. The font size of most text is too small to read. At the bottom, one of the charts is aligned far to the right, cutting off parts of the image from view (fails).
```

## Steps to Reproduce
Open the Bokeh test environment webpage on a mobile device. Zoom in and out to check for reflow capabilities.

## Guidelines and Standards Used
Zoom and reflow are not supported [https://chartability.github.io/POUR-CAF/#__zoomandreflowarenotsupported__](https://chartability.github.io/POUR-CAF/#__zoomandreflowarenotsupported__)

## Related Evidence
See "User style change not respected (critical)" evidence.


## Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.)

## Technical Details
- Chrome Version 128.0.6613.85 (64-bit)
- Samsung Galaxy S24
- Windows 11 Build 22631.3958

*Updated as of: August 27th, 2024*

## Notes
I want to note that while the test failed overall, zooming would condittionally pass because the chart and tools do respect those changes.