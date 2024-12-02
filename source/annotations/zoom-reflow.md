### Test Type Performed

Zoom and reflow are supported.

### Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, colorbar, span (i.e, line), text, and arrows.

### Results Summary

Annotations fails to reflow to fit different screen sizes. Reflow does not happen and quality is lost at higher zoom levels. I specifically focused on the hover tooltip for this test (See Notes section below.)

On mobile: The hover tooltip is not usable and cannot be accessed at all.

### Expected Behavior (Pass/Fail)

- _FAIL_ - We expect that the charts would stay on screen regardless of changes in screen size or screen view, like zooming.
- Chart space must be able to be zoomed using assistive technology or equivalent. Text, geometries, and all elements must change size appropriate to the type of zoom used. When zooming, content should reflow and not be cut off from view in two directions. Responsive design may need to consider re-arranging the display to ensure that no meaningful information or functionality is lost during reflow.

### Image or Video of Failure

````
  ```{video} ./assets/annotations_zoom-reflow.mp4
  :width: 100%
  :playsinline:
  ```
````
<!-- <video controls src="./assets/annotations_zoom-reflow.mp4" title="Annotations: Zoom and Reflow test"></video> -->
A desktop web browser is shown with five different charts. The user clicks an option in the command console called "Toggle deivce toolbar". This changes the browser to a moblie view. A gray circle is shown on screen to simulate the "touch" of a finger on a mobile device. When the user hovers over the second line chart, nothing happens. They move to the tool bar and toggle the "Hover" tool off and on, then attempt to hover over the line in the chart again. As before, nothing happens: no tooltip pops up. 

### Steps to Reproduce

Content should reflow intelligently, especially when a columnar layout is used (columns should reduce as viewport reduces). Content should not just resize as the viewport shrinks. Content should also remain generally viewable and readable (other perceptual tests and standards should apply). In general, visual-spatial searching should take place primarily across only 1 dimension at a time. So if significant content is hidden in an X direction but content is scrollable across the Y, this is likely going to fail for cognitive/discoverability problems (people will get lost or lose content without smart reflow). Make sure that whitespace, contrast, text size, and other perceptual tests are also considered when testing for zoom and reflow scenarios (below).

Test the following scenarios:

- Open the Bokeh test environment webpage on a mobile device. Zoom in and out to check for reflow capabilities.
  - You may also open a desktop browser (such as Chrome) and use mobile options in the Device Toolbar of the developer tools, to view using a simulated mobile device.
- On a desktop browser, resize the viewport of the browser from widescreen (1920px wide) down to narrow (350px).
- On a desktop browser, zoom the viewport to 500% using native browser zoom (do not use zoom utilities).

### Guidelines and Standards Used

Zoom and reflow are not supported [https://chartability.github.io/POUR-CAF/#**zoomandreflowarenotsupported**](https://chartability.github.io/POUR-CAF/#__zoomandreflowarenotsupported__)

### Related Evidence

See "User style change not respected (critical)" evidence.

<!-- ### Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

### Technical Details

- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

### Notes
I only tested the hover tooltip for this test because the results are the same as the "Plotting Interface" evidence forms. The hover was the only thing not tested previously. 
