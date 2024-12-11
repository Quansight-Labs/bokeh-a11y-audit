### Test Type Performed

Low contrast on interactive elements.

### Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, color bar, span (i.e, line), text, and arrows.

### Results Summary

Annotations fail for minimum contrast on interactive elements against active/inactive states.

Interactive legend "muted" against "unmuted": Fails. Results are 2.7:1.

Hover tooltip: Fails. Results are 2.54:1.

### Expected Behavior (Pass/Fail)

- _FAIL_ - We would expect interactive elements to pass a contrast ratio of 3:1 for the new state change against its previous state.

### Image or Video of Failure

Figure 1: Interactive legend "muted" against "unmuted" lines.

```{figure} ./assets/annotations_interactive-contrast-elements_1.png
    :width: 100%
    :alt: A line chart is shown. The legends blue color is highlighted. The contrast checking score is shown on the bottom left corner at 2.7:1 (fails).

    A line chart is shown. The legends blue color is highlighted. The contrast checking score is shown on the bottom left corner at 2.7:1 (fails).
```

Figure 2: Hover tooltip.

```{figure} ./assets/annotations_contrast-interactive-elements_2.png
    :width: 100%
    :alt: A line chart is shown. The hover tooltip's blue color is highlighted. The contrast checking score is shown on the bottom left corner at 2.54:1 (fails).

    A line chart is shown. The hover tooltip's blue color is highlighted. The contrast checking score is shown on the bottom left corner at 2.54:1 (fails).
```

### Steps to Reproduce

Using a dropper tool to gather the color, compare the foreground color against the background color to calculate the contrast score.

In this particular case, we tested the blue line in the legend against the full white background and the blue text in the tooltip against the white background. Avoiding aliased/partial pixels.

### Guidelines and Standards Used

Low contrast on interactive elements [https://chartability.github.io/POUR-CAF/#**lowcontrastoninteractiveelements**](https://chartability.github.io/POUR-CAF/#__lowcontrastoninteractiveelements__)

### Related Evidence

See "Low contrast (critical)" evidence as well as "Keyboard focus."

<!-- ### Known or Documented Issues
... -->

### Technical Details

- JAWS 2023.2402.1
- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

<!-- ### Notes
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.  -->
