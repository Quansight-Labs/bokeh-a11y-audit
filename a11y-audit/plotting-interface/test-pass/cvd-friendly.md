### Test Type Performed
Color Vision Deficiency (CVD) friendly.

### Artifact Evaluated
[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

### Results Summary
Plotting interface pass for being CVD safe.

### Expected Behavior (Pass/Fail)
- *Pass* - We expect any colors used would pass standards for CVD.

<!-- ### Image or Video of Failure 
... -->

### Steps to Reproduce
Using a dropper tool to gather the RGB color codes, compare the background, icon, toggle button identifier, hover highlight, and button selected highlight colors using a CVD tester.

### Guidelines and Standards Used
Not CVD-friendly [https://chartability.github.io/POUR-CAF/#__notcvdfriendly__](https://chartability.github.io/POUR-CAF/#__notcvdfriendly__)

<!-- ### Related Evidence
...

### Known or Documented Issues
... -->

### Technical Details
- Chrome Version 128.0.6613.120 (64-bit)
- Chroma.js Color Palette Helper
- Windows 11 Build 22631.3958

*Updated as of: September 10th, 2024*

<!-- ### Notes
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.  -->
