# Spacing

## Test Type Performed

Spacing is appropriate.

## Artifact Evaluated

[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769).

## Results Summary

These are fine

## Expected Behavior (Pass/Fail)

- _Pass_ - Use of white space and other forms of padded, structured spacing should be appropriate. Too much or too little white space on charts with intervals (like a bar chart with thin bars and large gaps or vice a versa) can cause perceivable and understandable issues.

## Image or Video of Failure

```{figure} ../assets/plot-tools_color-contrast.png
:width: 100%
:alt: A color scatter plot is shown. A plotting tool button is highlighted on the right, while the contrast checking score is shown on the bottom left corner (fails).

A color scatter plot is shown. A plotting tool button is highlighted on the right, while the contrast checking score is shown on the bottom left corner (fails).
```

## Steps to Reproduce

Measure gap size and element size for repeating, aligned elements. Gaps should not be wider than 50% of element size in cases where elements are laid out in a regular pattern or fashion. At least 1 pixel visual and interactive gap should be provided between interactive elements that are categorically different. For clustering and encodings where non-interactive elements overlap, this test is not relevant.

## Guidelines and Standards Used

Spacing is inappropriate [https://chartability.github.io/POUR-CAF/#**spacingisinappropriate**](https://chartability.github.io/POUR-CAF/#__spacingisinappropriate__)

## Related Evidence

See "Meaningful elements can be distinguished from each other" evidence about borders.

## Known or Documented Issues

(If there is already a github issue created for this test or a related test, it will be listed here.)

## Technical Details

- Chrome Version 127.0.6533.89 (64-bit)
- Windows 11 Build 22631.3958

_Updated as of: August 2nd, 2024_

## Notes

<!-- A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.  -->
