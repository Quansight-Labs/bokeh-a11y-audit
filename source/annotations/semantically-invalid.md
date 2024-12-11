### Test Type Performed
Semantically valid.

### Artifact Evaluated
[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, color bar, span (i.e, line), text, and arrows.

### Results Summary
Annotations fail to follow correct standards for not providing a heading for chart titles. It also fails to provide a button heading for the interactive legend. (Elements are generally categorized as divs.)

### Expected Behavior (Pass/Fail)
- *FAIL* - Semantically invalid use of document elements (if it functions like a button, but it is semantically other than a button, etc). Chart must be semantically valid according to modern standards. Initial testing (on the web) may be automated using any combination of: Axe-core, Wave, HTML Codesniffer, Accessibility Insights, or W3C Markup Validation but may only pass once a screen reader test has also verified the experience (see: Perceivable Failures for screen reader info).

The charts need to be given roles and put a system in place. Divs and canvas are meaningless for SRs. 

### Image or Video of Failure 
Figure 1: Chart title
```{figure} ./assets/annotations_semantically-invalid_1.png
    :width: 100%
    :alt: The element inspector pane of a web browser is opened. A yellow arrow is highlighting a section of code that reads 'div class= bk-Title'.

    The element inspector pane of a web browser is opened. A yellow arrow is highlighting a section of code that reads 'div class= bk-Title'.
```

Figure 2: Interactive legend
```{figure} ./assets/annotations_semantically-invalid_2.png
    :width: 100%
    :alt: The element inspector pane of a web browser is opened. A yellow arrow is highlighting a section of code that reads "div class= bk-Legend".

    The element inspector pane of a web browser is opened. A yellow arrow is highlighting a section of code that reads "div class= bk-Legend".
```

### Steps to Reproduce
1) Understand intended semantics.
1.a) are semantics functional? (buttons, toggle buttons, etc.)
2) Is there an HTML elements or aria that can correctly portray that semantic intention?
2a) If yes, did they use that element?
2b) If not, is there something that could have been used?
3) If there is no valid possible semantics that they could rely on, did they construct semantics themselves? (Typically done by adding to the end of an `aria-label` or `alt` description or by adding to `aria-roledescription`)


### Guidelines and Standards Used
Semantically invalid [https://chartability.github.io/POUR-CAF/#__semanticallyinvalid__](https://chartability.github.io/POUR-CAF/#__semanticallyinvalid__)

### Related Evidence
See "Content is only visual (critical)" and "Interaction modality has only one input type (critical)".

### Known or Documented Issues
See "Plot tools: Semantically invalid" evidence.

### Technical Details
- JAWS 2023.2402.1
- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

*Updated as of: October 22nd, 2024*

### Notes
As a note, if you test using WAVE or another equivalent tool, it won't won't be able to detect problems with divs and canvas elements because they are semanticless. Their assumed use is unknown.

Also note that *functional semantics* are less relevant for this test, since these are not interactive elements. But images should be `<img>` or `<figure>` or (if interactive) something like `<div role="application">`. No meaningful semantics are really used here. Passing this will require careful planning about *what* you intend and then matching that intention to the best semantic representations that exist.

<!-- A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels. -->