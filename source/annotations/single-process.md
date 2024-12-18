### Test Type Performed

Information can only be reached through single process.

### Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, color bar, span (i.e, line), text, and arrows.

### Results Summary

Annotations preemptively fail for not providing alternative means to reach information. A concrete example is with the hover tooltip. There is only precision information available with the tooltip and no other way to find this same information without it.

Another example is the legend's filtering capability: there is not a dropdown or alternative UI provided that can be used to accomplish this same activity.

Note that while not every chart needs to become a business-y sort of dashboard with 50 dropdowns and levers to pull, this still is a technical failure on principle. It would be good for bokeh to consider how to build more robust multi-path data interactions for visualizations than only ever presenting the end user with legend filters or point data on hover.

### Expected Behavior (Pass/Fail)

- _FAIL_ - There must be more than one process available to reach the same information. If chart is contained within or participates in complex user interface flows, such as transitions between views or states, interacting with filters, or moving between pages, there must be alternative paths to reach that same state (such as with search features, table of contents, parallel UI controls, etc).

### Image or Video of Failure

````
  ```{video} ./assets/annotations_single-process.mp4
  :width: 100%
  :playsinline:
  ```
````

A page with multiple line charts is shown. The user moves their cursor over a filled line on the chart, revealing a hover tooltip pop-up. It reads "No. of degrees: 14.224". They then turn off the hover function on the toolbar and try to return to the same point on the line. Next, the user tracks their cursor left across the chart to the "Number of degrees" y-axes label. There is no exact number match but they appear to be in the 14 range bracket.

### Steps to Reproduce

Using the Hover tool, find a number on the double line chart and try to find that information again without the hover tool.

Try to filter the chart without using the legend's toggle functionality.

### Guidelines and Standards Used

Information can only be reached through single process [https://chartability.github.io/POUR-CAF/#**informationcanonlybereachedthroughsingleprocess**](https://chartability.github.io/POUR-CAF/#__informationcanonlybereachedthroughsingleprocess__)

### Related Evidence

See "Content is only visual" evidence.

<!-- ### Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

### Technical Details

- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

<!-- ### Notes
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels. -->
