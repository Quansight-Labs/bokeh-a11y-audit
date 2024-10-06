### Test Type Performed
Color is used alone to communicate meaning.

### Artifact Evaluated
[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

### Results Summary
Plotting interface passes for all charts. 

### Expected Behavior (Pass/Fail)
- *Pass* - We expect charts to apply more than color alone to their elements, especially if those elements overlap or have close proximity.

<!-- ### Image or Video of Failure 
...

### Steps to Reproduce
... -->

### Guidelines and Standards Used
Color is used alone to communicate meaning [https://chartability.github.io/POUR-CAF/#__colorisusedalonetocommunicatemeaning__](https://chartability.github.io/POUR-CAF/#__colorisusedalonetocommunicatemeaning__)

<!-- ### Related Evidence
...

### Known or Documented Issues
... -->

### Technical Details
- Chrome Version 128.0.6613.120 (64-bit)
- Windows 11 Build 22631.3958

*Updated as of: September 10th, 2024*

<!-- ### Notes
See these examples for adjacent ordered colors [here](https://observablehq.com/@frankelavsky/contrast-and-no-use-of-color-alone-in-adjacent-charts) and unordered colors [here](https://observablehq.com/@frankelavsky/experimental-color-scale-textures). -->
