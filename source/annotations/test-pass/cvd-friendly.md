### Test Type Performed

Color Vision Deficiency (CVD) friendly.

### Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, colorbar, span (i.e, line), text, and arrows.

### Results Summary

Annotations pass for being CVD safe.

### Expected Behavior (Pass/Fail)

- _Pass_ - We expect any colors used would pass standards for CVD.

<!-- ### Image or Video of Failure
... -->

### Steps to Reproduce

Using a dropper tool to gather the RGB color codes, compare the background, icon, toggle button identifier, hover highlight, and button selected highlight colors using a CVD tester.

### Guidelines and Standards Used

Not CVD-friendly [https://chartability.github.io/POUR-CAF/#**notcvdfriendly**](https://chartability.github.io/POUR-CAF/#__notcvdfriendly__)

### Related Evidence

See "CVD Friendly" for plotting interface.

<!-- ### Known or Documented Issues
... -->

### Technical Details

- Chroma.js Color Palette Helper
- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

<!-- ### Notes
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.  -->
