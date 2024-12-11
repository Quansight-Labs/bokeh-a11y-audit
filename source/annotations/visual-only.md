### Test Type Performed

Content is only visual.

### Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/basic/annotations.html#): which include titles, axes labels, labels, legends, color bar, arrows, and spans (i.e, line).

### Results Summary

Annotations fail for visual only interactivity, particularly for screen reader and keyboard navigability and perceivability. (Some issues also exist for mouse users as well.) Elements cannot be accessed using typical SR navigation (directional keys and enter), which is a failure.

Overall, in our test environment, none of the charts can really be differentiated from one another except visually. No titles, axes labels, legends, etc. are announced during navigation.

For specific examples, the second line chart hover tooltips are only visual and mouse available. The color bar, span, and arrow of the bar chart are not explained or navigable at all in any input method besides visual.

### Expected Behavior (Pass/Fail)

- _FAIL_ - We would expect the meaningful elements to be navigable and perceivable by a screen reader, state what each element is when navigated to (such as with titles or labels) as well as any functional semantics (such as "button" or "link" or equivalent).

### Image or Video of Failure

````
  ```{video} ./assets/annotations_visual-only.mp4
  :width: 100%
  :playsinline:
  ```
````

A video shows a web browser with multiple charts. A screen reader navigates through the page and through multiple charts, but very limited information is given as they do so. The user (a sighted tester, in this case) navigates to the "Hover" tool on the toolbar and presses enter to interact with it, but this opens a link to a new webpage (fails).

### Steps to Reproduce

Using JAWS, navigate using arrow keys into the color scatter plot toolbar. Since it cannot be reached, navigate again to the toolbar by pressing TAB. Once at the toolbar, continue to press TAB or Shift+TAB to switch between elements. Note that only a visual indication of focus is provided (no screen reader announcement is made). Also note that interacting with/selecting an element opens the previous link (which is where the SR's "cursor focus" last encountered a valid interactive element).

### Guidelines and Standards Used

Content is only visual [https://chartability.github.io/POUR-CAF/#**contentisonlyvisual\_**critical\_](https://chartability.github.io/POUR-CAF/#__contentisonlyvisual___critical_)

### Related Evidence

This issue will be highly related many other tests: "Semantics," "Single process," "Narrative structure," "Fragile support," "Invalid semantics," "Interactive context is not clear," "Cues and instructions," "Explanation for purpose," "Visually apparent features," and "Tedious." (Possibly more I may have forgotten.)

### Known or Documented Issues

See "Plot tools: Content is only visual" for evidence.

### Technical Details

- JAWS 2023.2402.1
- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

### Notes

I wasn't sure what all was part of the plotting interface when I began that previous testing, so some of these Annotation tests may be redundant. I'm still adding them to this audit branch for the sake of being thorough and consolidating information.
