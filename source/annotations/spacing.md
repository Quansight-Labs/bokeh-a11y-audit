### Test Type Performed
Spacing is appropriate.

### Artifact Evaluated
[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, colorbar, span (i.e, line), text, and arrows.

### Results Summary
Annotations in the bar chart fail for spacing with the colorbar, span, and arrow.

### Expected Behavior (Pass/Fail)
- *FAIL* - At least 1 pixel visual and interactive gap should be provided between interactive elements that are categorically different. For clustering and encodings where non-interactive elements overlap, this test is not relevant.

- Use of white space and other forms of padded, structured spacing should be appropriate. Too much or too little white space on charts with intervals (like a bar chart with thin bars and large gaps or vice a versa) can cause perceivable and understandable issues.

### Image or Video of Failure 
Figure 1: Bar chart - Colorbar
```{figure} ./assets/annotations_meaningful-elements_1.png
    :width: 100%
    :alt: A color gradient for values of a bar chart is shown. A red circle is highlighting a pair of lemon-yellow and a lime-green squares. There is no border or space between the two colored squares (fails).

    A color gradient for values of a bar chart is shown. A red circle is highlighting a pair of lemon-yellow and a lime-green squares. There is no border or space between the two colored squares (fails).
```

Figure 2: Bar chart - Span
```{figure} ./assets/annotations_meaningful-elements_2.png
    :width: 100%
    :alt: A bar chart is shown. A red box is highlighting a black line that is overlapping a green colored bar. There is no border around the line to separate it from the bars (fails).

    A bar chart is shown. A red box is highlighting a black line that is overlapping a green colored bar. There is no border around the line to separate it from the bars (fails).
```

Figure 3: Bar chart - Arrow
```{figure} ./assets/annotations_meaningful-elements_3.png
    :width: 100%
    :alt: A bar chart is shown. A red box is highlighting a black arrow that is pointing to a black line, both overlapping a green colored bar. There is no border around the arrow to separate it from the bars (fails).

    A bar chart is shown. A red box is highlighting a black arrow that is pointing to a black line, both overlapping a green colored bar. There is no border around the arrow to separate it from the bars (fails).
```

### Steps to Reproduce
Measure gap size and element size for repeating, aligned elements. Gaps should not be wider than 50% of element size in cases where elements are laid out in a regular pattern or fashion. 

### Guidelines and Standards Used
Spacing is inappropriate [https://chartability.github.io/POUR-CAF/#__spacingisinappropriate__](https://chartability.github.io/POUR-CAF/#__spacingisinappropriate__)

### Related Evidence
See "Meaningful elements can be distinguished from each other" evidence about borders.

### Known or Documented Issues
...

### Technical Details
- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

*Updated as of: October 22nd, 2024*

<!-- ### Notes
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.  -->
