### Test Type Performed

Target pointer interaction size.

### Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, color bar, span (i.e, line), text, and arrows.

### Results Summary

Annotations fail for both the interactive legend and hover cursor target pointer sizes. The tooltip is pixel-precise based on the size of the element rendered, meaning that rendered interactive visualization elements that are smaller than 24x24 will fail. (The lines on the line chart were difficult to find their exact measurements.)

Legend labels: Fails at 98 x 19.

Hover tooltip: Fails to meet minimum.

### Expected Behavior (Pass/Fail)

- _FAIL_ - We would expect interaction elements to have a minimum target size of 24 x 24px for mouse or touch modalities. We expect that elements with a visual space of less than 24 x 24px in size are still centered within a non-overlapping 24 x 24px interaction target area (even if invisible).

### Image or Video of Failure

```{figure} ./assets/annotations_target-pointer-size.png
    :width: 100%
    :alt: A chart's legend is shown with two labels: Engineering and Business. A black border outlines the approximate dimensions for each toggleable button, reading 98x19 pixels. To the left of them is a pixel block that is 24 x 24 for comparison.

    A chart's legend is shown with two labels: Engineering and Business. A black border outlines the approximate dimensions for each toggleable button, reading 98x19 pixels. To the left of them is a pixel block that is 24 x 24 for comparison.
```

### Steps to Reproduce

Interact with all elements using a mouse pointer to find which are interactive (try hovering, clicking, and dragging). If an element is interactive, then measure the width and height of that element. If the element is not a simple square, rectangle, or circle, then attempt to measure the thinnest and thickest straight line intersections of that shape instead of width and height. Both the thinnest _and_ thickest dimensions must pass 24x24 pixels in size.

### Guidelines and Standards Used

Target pointer interaction size is too small [https://chartability.github.io/POUR-CAF/#**targetpointerinteractionsizeistoosmall**](https://chartability.github.io/POUR-CAF/#__targetpointerinteractionsizeistoosmall__)

<!-- ### Related Evidence
N/A

### Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

### Technical Details

- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

### Notes

Note that Chartability uses the older AAA standard, requiring elements to have 44 x 44px for interaction target size. But AA standard was introduced (as a later amendment to WCAG 2.2) that allows 24x24px.
