# Zoom Reflow

## Test Type Performed

Zoom and reflow are supported.

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Plotting interface fails to reflow to fit different screen sizes. Reflow does not happen and quality is lost at higher zoom levels.

On mobile: The font becomes too small to read without zooming, and the chart alignment shifts off center (compared to a desktop screen view). When zoomed in, the charts get cut off from view and do not resize to stay on screen.

At high zoom: Reflow does not take place while font quality becomes poor. Some significant whitespace traps are created due to lack of reflow (in the scatter area).

## Expected Behavior (Pass/Fail)

- _FAIL_ - We expect that the charts would stay on screen regardless of changes in screen size or screen view, like zooming.
- Chart space must be able to be zoomed using assistive technology or equivalent. Text, geometries, and all elements must change size appropriate to the type of zoom used. When zooming, content should reflow and not be cut off from view in two directions. Responsive design may need to consider re-arranging the display to ensure that no meaningful information or functionality is lost during reflow.

## Image or Video of Failure

Figure 1: Mobile view

```{figure} ./assets/plotting-interface_zoom-reflow_1.jpg
:width: 100%
:alt: A mobile web browser is shown with five different charts. The font size of most text is too small to read. At the bottom, one of the charts is aligned far to the right, cutting off parts of the image from view (fails).

A mobile web browser is shown with five different charts. The font size of most text is too small to read. At the bottom, one of the charts is aligned far to the right, cutting off parts of the image from view (fails).
```

Figure 2: Responsive + reflow check

```{figure} ./assets/plotting-interface_zoom-reflow_2.png
:width: 100%
:alt: Chrome developer tools are open and the page is being resized to 350px wide. Elements in the first column of the first two rows of charts are squished (responsive sizing), while the second column is shown off-screen (fails to reflow the second column into single-column view). Charts in the grid seem to be semi-responsive but not reflow (this is a fail).

Chrome developer tools are open and the page is being resized to 350px wide. Elements in the first column of the first two rows of charts are squished (responsive sizing), while the second column is shown off-screen (fails to reflow the second column into single-column view). Charts in the grid seem to be semi-responsive but not reflow (this is a fail).
```

Figure 3: Scatter reflow check

```{figure} ./assets/plotting-interface_zoom-reflow_3.png
:width: 100%
:alt: Chrome developer tools are open and the page is being resized to 350px wide. The scatter plot's view shows a large amount of empty space with a chart just out of view to the right of the screen (fails, does not reflow).

Chrome developer tools are open and the page is being resized to 350px wide. The scatter plot's view shows a large amount of empty space with a chart just out of view to the right of the screen (fails, does not reflow).
```

Figure 4: Text not reflowing with canvas chart

```{figure} ./assets/plotting-interface_zoom-reflow_4.png
:width: 100%
:alt: Viewport is resized to 350px wide and the title text within a chart (marked with red underline) is truncated and unreadable compared to the HTML-based text above it, which is reflowing properly by default (fails).

Viewport is resized to 350px wide and the title text within a chart (marked with red underline) is truncated and unreadable compared to the HTML-based text above it, which is reflowing properly by default (fails).
```

Figure 5: Massive whitespace from lack of reflow

```{figure} ./assets/plotting-interface_zoom-reflow_5.png
:width: 100%
:alt: Viewport is zoomed in to 500% and the scatterplot area (when first scrolling to it) is primarily whitespace (fails).

Viewport is zoomed in to 500% and the scatterplot area (when first scrolling to it) is primarily whitespace (fails).
```

Figure 6: Font readability suffers at high zoom levels

```{figure} ./assets/plotting-interface_zoom-reflow_6.png
:width: 100%
:alt: Viewport is zoomed in to 400% showing the canvas-based text from the bar chart labels being highly aliased and fuzzy, compared to the text for the Scatter plot beneath (circled in red) which is high fidelity and readable (fails).

Viewport is zoomed in to 400% showing the canvas-based text from the bar chart labels being highly aliased and fuzzy, compared to the text for the Scatter plot beneath (circled in red) which is high fidelity and readable (fails).
```

## Steps to Reproduce

Content should reflow intelligently, especially when a columnar layout is used (columns should reduce as viewport reduces). Content should not just resize as the viewport shrinks. Content should also remain generally viewable and readable (other perceptual tests and standards should apply). In general, visual-spatial searching should take place primarily across only 1 dimension at a time. So if significant content is hidden in an X direction but content is scrollable across the Y, this is likely going to fail for cognitive/discoverability problems (people will get lost or lose content without smart reflow). Make sure that whitespace, contrast, text size, and other perceptual tests are also considered when testing for zoom and reflow scenarios (below).

Test the following scenarios:

- Open the Bokeh test environment webpage on a mobile device. Zoom in and out to check for reflow capabilities.
  - You may also open a desktop browser (such as Chrome) and use mobile options in the Device Toolbar of the developer tools, to view using a simulated mobile device.
- On a desktop browser, resize the viewport of the browser from widescreen (1920px wide) down to narrow (350px).
- On a desktop browser, zoom the viewport to 500% using native browser zoom (do not use zoom utilities).

## Guidelines and Standards Used

Zoom and reflow are not supported [https://chartability.github.io/POUR-CAF/#**zoomandreflowarenotsupported**](https://chartability.github.io/POUR-CAF/#__zoomandreflowarenotsupported__)

## Related Evidence

See "User style change not respected (critical)" evidence.

<!-- ## Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

## Technical Details

- Chrome Version 129.0.6668.59 (64-bit)
- JAWS 2023.2402.1
- Windows 11 Build 22631.3958

_Updated as of: September 18th, 2024_

<!-- ## Notes
I want to note that while the test failed overall, zooming would conditionally pass because the chart and tools do respect those changes. -->
