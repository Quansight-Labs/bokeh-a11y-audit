# Target Pointer Size

## Test Type Performed

Target pointer interaction size.

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Plotting interface's tooltip fails to have a large enough interaction target size. Tooltip is pixel-precise based on the size of the element rendered, meaning that rendered interactive visualization elements that are smaller than 24x24 will fail.

## Expected Behavior (Pass/Fail)

- _FAIL_ - We would expect interaction elements to have a minimum target size of 24 x 24px for mouse or touch modalities. We expect that elements with a visual space of less than 24 x 24px in size are still centered within a non-overlapping 24 x 24px interaction target area (even if invisible).

## Image or Video of Failure

```{figure} ./assets/plotting-interface_target-pointer-size.png
:width: 100%
:alt: A line chart is shown with a tooltip being provided by a mouse hover event. The line is only 1 or 2px thick and is being hovered over perfectly by the mouse pointer to accomplish the tooltip appearance.

A line chart is shown with a tooltip being provided by a mouse hover event. The line is only 1 or 2px thick and is being hovered over perfectly by the mouse pointer to accomplish the tooltip appearance.
```

## Steps to Reproduce

Interact with all elements using a mouse pointer to find which are interactive (try hovering, clicking, and dragging). If an element is interactive, then measure the width and height of that element. If the element is not a simple square, rectangle, or circle, then attempt to measure the thinnest and thickest straight line intersections of that shape instead of width and height. Both the thinnest _and_ thickest dimensions must pass 24x24 pixels in size.

## Guidelines and Standards Used

Target pointer interaction size is too small [https://chartability.github.io/POUR-CAF/#**targetpointerinteractionsizeistoosmall**](https://chartability.github.io/POUR-CAF/#__targetpointerinteractionsizeistoosmall__)

<!-- ## Related Evidence
N/A

## Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

## Technical Details

- Chrome Version 129.0.6668.59 (64-bit)
- Windows 11 Build 22631.3958

_Updated as of: September 18th, 2024_

## Notes

Note that Chartability uses the older AAA standard, requiring elements to have 44 x 44px for interaction target size. But AA standard was introduced (as a later amendment to WCAG 2.2) that allows 24x24px.

<!--
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels. -->
