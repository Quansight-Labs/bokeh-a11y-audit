### Test Type Performed
Color Contrast.

### Artifact Evaluated
[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/basic/annotations.html#): which include titles, axes labels, labels, legends, color bars, arrows, and spans (i.e, line).

### Results Summary
Annotations has failures for minimum contrast. 

Interactive legend "muted" against background: Fails at 1.27:1.

Color bar legend: The first 4/10 colors fail contrast against a white backdrop (starting at the top and working down). Fails are as follows: 1.26, 1.58, 2, and 2.56. 

All colors fail for ordered pairs. See both "Problems.." sections below.

Title text: Passes.

Axes label texts: Passes.

Label ("Mean"): Passes. Note: This does not have the white box around the label as expected, so depending on what the text overlaps it would fail.

Legend text: Passes.

Legend shapes: Passes for geometries. Scatter plot legend passes. 

Color bar text: Passes.

Span line: Passes. 

Arrow: Passes for geometries.

#### Problems unique to lines
(Copied text from Plotting Interface contrast test) Lines are hard to perceive already because they are often thin. And we don't include element size in our contrast calculations, so it is very important to still hit minimum contrast colors for lines used. For plotted marks, like lines in a line chart, follow this strictly. For grid or axis lines, you can consider alternative ways to lower contrast that still technically pass contrast scores, such as making them dotted lines.

#### Problems unique to adjacent, ordered colors
(Copied text from Plotting Interface contrast test) In situations where colors are ordered and adjacent, they need to pass "pair contrast" as well as contrast against their background. The legend in the bar chart is a good example of this. This is a sequential scheme where each step will fail contrast against sibling steps. (See examples [here](https://observablehq.com/@frankelavsky/contrast-and-no-use-of-color-alone-in-adjacent-charts).)

Consider either removing the pixel between these categories, so that each color only needs to pass against the background, or consider having much fewer color steps with much larger steps in contrast (although this significantly limits the scheme's options overall).

#### Problems unique to adjacent, unordered colors
(Copied text from Plotting Interface contrast test) So in the bar chart as well as the scatter plot, colors of elements overlap and intersect with one another and fail contrast. Consider adding 1 pixel of white between everything, especially if it is important to be able to discern individual elements from one another. (See examples [here](https://observablehq.com/@frankelavsky/experimental-color-scale-textures).)

The bar should do this. But sometimes scatter plots are meant to be perceived "as a whole" - so it is less important for every individual element to be distinguishable from one another visually. All elements should still pass contrast against their background, however.

### Expected Behavior (Pass/Fail)
- *FAIL* - We would expect annotation elements to pass a contrast ratio of either 4.5:1 for text or 3:1 for graphics.

### Image or Video of Failure 
Figure 1: Double line chart: Muted line
```{figure} ./assets/annotations_contrast_1.png
    :width: 100%
    :alt: A double line chart is shown. A color selection dropper is highlighting a selected 'muted', grayed out line. The contrast checking score of 1.27 is shown on the bottom left corner (fails).

    A double line chart is shown. A color selection dropper is highlighting a selected 'muted', grayed out line. The contrast checking score of 1.27 is shown on the bottom left corner (fails).
```

Figure 2 and 3: Bar Chart: Color bar
```{figure} ./assets/annotations_contrast_3.png
    :width: 100%
    :alt: A color bar chart is shown. A color selection dropper is highlighting the first bar color on the legend. The contrast checking score of 1.26 is shown on the bottom left corner (fails).

    A color bar chart is shown. A color selection dropper is highlighting the first bar color on the legend. The contrast checking score of 1.26 is shown on the bottom left corner (fails).
```
```{figure} ./assets/annotations_contrast_4.png
    :width: 100%
    :alt: A color bar chart is shown. The contrast checking score of 1.25 is shown on the bottom left, comparing two colors right next to one another (fails pair contrast).

    A color bar chart is shown. The contrast checking score of 1.25 is shown on the bottom left, comparing two colors right next to one another (fails pair contrast).
```

### Steps to Reproduce
Using a dropper tool to gather the color, compare the foreground color against the background color to calculate the contrast score. For the bar chart, also test ordered colors against one another.

For each respective chart, we tested the full interior pixels of interface elements (lines, bars, plots, table) against the full white background (avoiding aliased/partial pixels).

### Guidelines and Standards Used
Low contrast minimums [https://chartability.github.io/POUR-CAF/#__lowcontrast___critical_](https://chartability.github.io/POUR-CAF/#__lowcontrast___critical_)

### Related Evidence
See "Plotting interface: Contrast" evidence.

<!-- ### Known or Documented Issues
See "Plot tools" contrast evidence. -->

### Technical Details
- Chrome Version 130.0.6723.59 (64-bit)
- WCAG Color Contrast checker extension
- Windows 11 Build 22631.4317

*Updated as of: October 22nd, 2024*

### Notes
I wasn't sure what all was part of the plotting interface when I began that previous testing, so some of these Annotation tests may be redundant. I'm still adding them to this audit branch for the sake of being thorough and consolidating information.