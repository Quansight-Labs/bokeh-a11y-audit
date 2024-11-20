# Color Contrast

## Test Type Performed

Color Contrast.

## Artifact Evaluated

[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769).

## Results Summary

Plot tool icons fail minimum contrast. Results are 2.46:1.

## Expected Behavior (Pass/Fail)

- _FAIL_ - We would expect interactive elements to pass a contrast ratio of either 4.5:1 for text or 3:1 for graphics.

## Image or Video of Failure

```{figure} ./assets/plot-tools_color-contrast.png
:width: 100%
:alt: A color scatter plot is shown. A plotting tool button is highlighted on the right, while the contrast checking score is shown on the bottom left corner (fails).

A color scatter plot is shown. A plotting tool button is highlighted on the right, while the contrast checking score is shown on the bottom left corner (fails).
```

## Steps to Reproduce

Using a dropper tool to gather the color, compare the foreground color against the background color to calculate the contrast score.

In this particular case, we tested the full grey interior pixels of the icon against the full white background (avoiding aliased/partial pixels).

## Guidelines and Standards Used

Low contrast minimums [https://chartability.github.io/POUR-CAF/#**lowcontrast\_**critical\_](https://chartability.github.io/POUR-CAF/#__lowcontrast___critical_)

## Related Evidence

(Added if additional evidence has already been gathered for related elements. This will not be edited retroactively, however, due to scope creep. This means that the latest issues will have the most Related Evidence listed.)

## Known or Documented Issues

(If there is already a github issue created for this test or a related test, it will be listed here.)

## Technical Details

- Chrome Version 127.0.6533.89 (64-bit)
- WCAG Color Contrast checker extension
- Windows 11 Build 22631.3958

_Updated as of: August 2nd, 2024_

## Notes

<!-- A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.  -->
