### Test Type Performed

Content is only visual.

### Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

### Results Summary

Plotting interface fails for visual only interactivity, particularly for screen reader and keyboard navigability and perceivability. (Some issues also exist for mouse users as well.) Elements cannot be accessed using typical SR navigation (directional keys), which is a failure. TAB focus moves forward to the buttons (because they have the attribute "`tabindex`" added), but they do not announce anything to a screen reader. TAB and `tabindex` should not be used or relied on as for making a divider element (`<div>`) into something that can simulate a richly semantic element (such as a `<button>` or equivalent).

The line, bar, and scatter plot charts cannot be accessed at all outside of mouse-and-click interactions. And even using a mouse, there is no way to explore the individual data elements of the charts to understand their relation to one another. For example, in the scatter plot, a user cannot navigate to any individual points to know their value using any input method. The only way to know the value is to visually look and find where they sit on the axes.

Overall, in our test environment, none of the charts can really be differentiated from one another except visually. No titles, axes labels, etc. are announced during navigation. While the user can get to the tool bar, there is no introduction as to what that is and they are forced to navigate there.

### Expected Behavior (Pass/Fail)

- _FAIL_ - We would expect the meaningful elements to be navigable and perceivable by a screen reader, state what each element is when navigated to (such as with a label) as well as any functional semantics (such as "button" or "link" or equivalent).

### Image or Video of Failure

<video controls src="./assets/plotting-interface_visual-only.mp4" title="Plotting-interface_Visual-only"></video>
A web browser is shown with multiple charts. A screen reader navigates through the page and through multiple charts, but very limited information is given as they do so (fails).

### Steps to Reproduce

Using JAWS, navigate using arrow keys into the color scatter plot toolbar. Since it cannot be reached, navigate again to the toolbar by pressing TAB. Once at the toolbar, continue to press TAB or Shift+TAB to switch between elements. Note that only a visual indication of focus is provided (no screen reader announcement is made). Also note that interacting with/selecting an element opens the previous link (which is where the SR's "cursor focus" last encountered a valid interactive element).

### Guidelines and Standards Used

Content is only visual [https://chartability.github.io/POUR-CAF/#**contentisonlyvisual\_**critical\_](https://chartability.github.io/POUR-CAF/#__contentisonlyvisual___critical_)

### Related Evidence

This issue will be highly related to failure to use correct semantics and screen reader operability.

### Known or Documented Issues

See "Plot tools: Content is onlly visual" for evidence.

### Technical Details

- Chrome Version 128.0.6613.120 (64-bit)
- JAWS 2023.2402.1
- Windows 11 Build 22631.3958

_Updated as of: September 10th, 2024_

### Notes

A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.
