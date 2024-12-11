### Test Type Performed
Appropriate tab stops.

### Artifact Evaluated
[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, color bar, span (i.e, line), text, and arrows.

### Results Summary
Annotations fail for tab stops on interactive elements for the interactive legend.

### Expected Behavior (Pass/Fail)
- *FAIL* - Interactive elements (that represent buttons, links, or selectable features) must have a tab stop, while non-interactive elements must not have a tab stop. Every interactive chart element must NOT have its own tab stop unless the chart is small or the tabs are programmatically revealed (such as having a single tab stop at the root of a chart and then a way to enter further layers or sections of the chart using keyboard controls). At least one tab stop should be 

### Image or Video of Failure 
````
  ```{video} ./assets/annotations_modality-input_keyboard.mp4
  :width: 100%
  :playsinline:
  ```
````  
A video of a webpage with multiple charts is shown. The user navigates to a double line chart using TAB. Once there, they continue to press TAB to try and navigate to the interactive legend with no success.

### Steps to Reproduce
Using the keyboard, press TAB to navigate to the double line chart area. Continue to press TAB to try and navigate to the interactive legend.

### Guidelines and Standards Used
Inappropriate tab stops [https://chartability.github.io/POUR-CAF/#__inappropriatetabstops__](https://chartability.github.io/POUR-CAF/#__inappropriatetabstops__)

### Related Evidence
See "Interaction modality has only one input type (critical)," "Tedious," "Narrative structure."

### Known or Documented Issues
See "Plotting interface: Inappropriate tab stops" and "Content is only visual" evidence.

### Technical Details
- JAWS 2023.2402.1
- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

*Updated as of: October 22nd, 2024*

<!-- ### Notes
This test also depends heavily on more interactivity being made available to SR users in general. The ability to navigate to the legend doesn't make sense in that it is a visual-only tool and a SR cannot interact with any of the "points" of the line charts like the mouse hover can (currently). -->