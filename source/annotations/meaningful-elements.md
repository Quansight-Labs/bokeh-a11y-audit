### Test Type Performed

Meaningful elements can be distinguished from each other.

### Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, colorbar, span (i.e, line), text, and arrows.

### Results Summary

Annotations fail for the colorbar, span, and arrow in the bar chart. Each of these elements has the potential to become compromised depending on the contrast of other elements interacting with them.

The black span line and arrow overlap colored bars on the bar chart. In this specific example the contrast passes, but without any border around these elements it could create issues in other charts.

### Expected Behavior (Pass/Fail)

- _FAIL_ - Adjacent elements must have at least 1px white space between them (like stacked bars or pie charts where elements “touch”). Text (any) must not be obscured or overlapped by any other elements.

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

- Determine which elements are meaningful.
- Test whether these elements can be distinguished from other meaningful elements (typically at least whether they have at least 1px separation).

### Guidelines and Standards Used

Meaningful elements can be distinguished from each other
[https://chartability.github.io/POUR-CAF/#**meaningfulelementscanbedistinguishedfromeachother**](https://chartability.github.io/POUR-CAF/#__meaningfulelementscanbedistinguishedfromeachother__)

### Related Evidence

See "Low contrast" and "Information Complexity."

### Known or Documented Issues

...

### Technical Details

- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

<!-- ### Notes
We lean towards a failing if anything is questionable. -->
