# Style Change Respected

## Test Type Performed
User style changes respected (critical).

## Artifact Evaluated
[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769).

## Results Summary
Plot tools fail to respect a user's custom styling changes when trying to use a high contrast setting. See "Notes" section at the end.

## Expected Behavior (Pass/Fail)
- *FAIL* - We expect that any styling changes a user makes (contrast, text strokes, etc) are not blocked from taking effect, and the charts do no override these styling changes.

## Image or Video of Failure 
```{figure} ./assets/plot-tools_style-change-respected.png
:width: 100%
:alt: A scatter plot is shown. A high contrast filter has been implemented, and the web browser background is black with yellow font. However, the plot tool buttons retain their default color scheme - the contrast change was not applied (fails).

A scatter plot is shown. A high contrast filter has been implemented, and the web browser background is black with yellow font. However, the plot tool buttons retain their default color scheme - the contrast change was not applied (fails).
```

## Steps to Reproduce
Using Windows contrast themes, choose Night Sky (high contrast) option and apply.

## Guidelines and Standards Used
User style change not respected (critical) [https://chartability.github.io/POUR-CAF/#__userstylechangenotrespected___critical_](https://chartability.github.io/POUR-CAF/#__userstylechangenotrespected___critical_)

## Related Evidence
See "User's text adjustments are not respected", "Contrast and textures cannot be adjusted", and "Zoom and reflow are not supported" evidence.

## Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.)

## Technical Details
- Chrome Version 128.0.6613.85 (64-bit)
- Windows high contrast theme
- Windows 11 Build 22631.3958

*Updated as of: August 27th, 2024*

## Notes
This test is somewhat of an umbrella of all the tests that come after. First, we test: text styling, zoom assistive tech, and contrast options. If any of those separate tests fail, then this test fails.