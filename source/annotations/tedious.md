### Test Type Performed

Navigation and interaction is not tedious (critical).

### Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, color bar, span (i.e, line), text, and arrows.

### Results Summary

Annotations fail for tedious behavior when using the hover tooltip. There are no obvious "points" on the lines in the line chart. This makes using the hover confusing and tedious when trying to find the information you want.

Note that this interaction is not accessible at all to keyboard or screen reader users, but if it were, it would need to be nested into skippable sections in case these users wanted to skip the many data points in a given visualization (see "Tab stops" and "Narrative structure" for more info once this becomes available).

### Expected Behavior (Pass/Fail)

- _FAIL_ - Large blocks of repeated content must be skippable and interactions where the user is required to perform significant labor must not be considered essential (in content or function). The number of interactions or time required to perform a single task should be measured and compared across modalities (mouse pointer versus sequential keyboard versus search versus voice, etc).

### Image or Video of Failure

````
  ```{video} ./assets/annotations_tedious.mp4
  :width: 100%
  :playsinline:
  ```
````

A user is placing their cursor over a filled line on a chart. As they hover over the line, a tool tip pops up and continually changes number values as they move across the line. They move forward and backward along the line to try and find the information they're looking for.

### Steps to Reproduce

Using a mouse on charts with hover tool enabled, drag the cursor over either of the line to see the hover tooltip. Continue to move the cursor and hover alone the line.

### Guidelines and Standards Used

Navigation and interaction is tedious [https://chartability.github.io/POUR-CAF/#**navigationandinteractionistedious\_**critical\_](https://chartability.github.io/POUR-CAF/#__navigationandinteractionistedious___critical_)

### Related Evidence

See "Plot tools: Navigation and interaction is tedious," "Visual only," "Tab stops," and "Narrative structure," evidence as well as the highly-related "Pointer size is too small."

<!-- ### Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

### Technical Details

- JAWS 2023.2402.1
- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

<!-- ### Notes
This is a conditional pass. There currently isn't any way to directly interact with any of the chart elements besides the plot tools. So we cannot actively test if interactions would be tedious or not. -->
