### Test Type Performed

User style changes respected (critical).

### Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, colorbar, span (i.e, line), text, and arrows.

### Results Summary

Annotations do not respect a user's custom styling changes when trying to use a high contrast setting, except the hover tooltip. See "Notes" section at the end.

### Expected Behavior (Pass/Fail)

- _FAIL_ - Styling changed by the user must be respected. Chart must not interfere with or override styling changes made by the user (such as importing a custom style sheet for use in an HTML application or web site).

### Image or Video of Failure

<figure>
    <img width="803" alt="A line chart is shown. A high contrast filter has been implemented, and the web browser background is black with yellow font. However, the chart space retains it's default color scheme - the contrast change was not applied (fails). Only the hover tooltip has respected the contrast change." src="./assets/annotations_contrast-texture-adjustments.png">
    <figcaption>A line chart is shown. A high contrast filter has been implemented, and the web browser background is black with yellow font. However, the chart space retains it's default color scheme - the contrast change was not applied (fails). Only the hover tooltip has respected the contrast change.</figcaption>
</figure>

### Steps to Reproduce

Using Windows contrast themes, choose Night Sky (high contrast) option and apply.

### Guidelines and Standards Used

User style change not respected (critical) [https://chartability.github.io/POUR-CAF/#**userstylechangenotrespected\_**critical\_](https://chartability.github.io/POUR-CAF/#__userstylechangenotrespected___critical_)

### Related Evidence

See "User's text adjustments are not respected", "Contrast and textures cannot be adjusted", and "Zoom and reflow are not supported" evidence.

### Known or Documented Issues

See "Plot tools: User style change not respected (critical)" evidence forms.

### Technical Details

- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

*Updated as of: October 22nd, 2024*

### Notes

This test is somewhat of an umbrella of all the tests that come after. First, we test: text styling, zoom assistive tech, and contrast options. If any of those separate tests fail, then this test fails.
