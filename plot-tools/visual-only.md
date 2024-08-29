### Test Type Performed
Content is only visual.

### Artifact Evaluated
[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769).

### Results Summary
Plot tool icons fail screen reader navigability and perceivability. Elements cannot be accessed using typical SR navigation (directional keys), which is a failure. TAB focus moves forward to the buttons (because they have the attribute "`tabindex`" added), but they do not announce anything to a screen reader. TAB and `tabindex` should not be used or relied on as for making a divider element (`<div>`) into something that can simulate a richly semantic element (such as a `<button>` or equivalent).

### Expected Behavior (Pass/Fail)
- *FAIL* - We would expect the meaningful elements to be navigable and perceivable by a screen reader, state what each element is when navigated to (such as with a label) as well as any functional semantics (such as "button" or "link" or equivalent). 

### Image or Video of Failure 
<figure>
    <video controls src="./assets/plot-tools_visual-only.mp4" title="Plot-tools_visual-only"></video>
    <figcaption>A color scatter plot is shown. A screen reader highlighter box is on a plot tool icon, but when the tool is selected it opens a previous link instead of toggling (fails).</figcaption>
</figure>


### Steps to Reproduce
Using JAWS, navigate using arrow keys into the color scatter plot toolbar. Since it cannot be reached, navigate again to the toolbar by pressing TAB. Once at the toolbar, continue to press TAB or Shift+TAB to switch between elements. Note that only a visual indication of focus is provided (no screen reader announcement is made). Also note that interacting with/selecting an element opens the previous link (which is where the SR's "cursor focus" last encountered a valid interactive element).

In this particular case, the first toolbar element works as intended. (It is a link and links to Bokeh's website.)

### Guidelines and Standards Used
Content is only visual [https://chartability.github.io/POUR-CAF/#__contentisonlyvisual___critical_](https://chartability.github.io/POUR-CAF/#__contentisonlyvisual___critical_)

### Related Evidence
This issue will be highly related to failure to use correct semantics and screen reader operability (we haven't done these yet, but they will be incoming failures for sure). Since a button is not used (but instead these are `<div>` elements styled into buttons), not only are there no _functional semantics_ provided (aka "button" being announced to communicate this is interactive), but there is also no label provided for a screen reader user to be able to perceive.

An the automatic input handling provided to a `<button>` is far more robust than a `<div>`, which is why when using JAWS and interacting with these buttons, JAWS reverts to the previously visited link (the `<a>` element that leads to bokeh.com).

### Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.)

### Technical Details
- Chrome Version 127.0.6533.89 (64-bit)
- JAWS 2023.2402.1
- Windows 11 Build 22631.3958

*Updated as of: August 2nd, 2024*

### Notes
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels. 
