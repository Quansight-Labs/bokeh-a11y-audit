### Test Type Performed
Axis labels are clear or present. 

### Artifact Evaluated
[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

### Results Summary
Plotting interface fails for providing axis titles for screen reader users.

### Expected Behavior (Pass/Fail)
- *FAIL* - Axis labels should be present and clear. Axis must not be truncated without a clear label. In rare cases axes may be removed (if adequate text explanation or annotation is provided). Otherwise, axis should be present and clearly labeled. Axis labels may be abbreviated but with a clear and consistent convention.

### Image or Video of Failure 
<video controls src="./assets/plotting-interface_metrics-variables.mp4" title="Title"></video>
A line chart is shown. A screen reader begins to navigate down through a webpage to get to the chart. Once the user navigates to the chart, they taken to the tools of the chart. No title, metrics, axes labels, etc are given to the user (fails).

### Steps to Reproduce
Using a SR, navigate to the chart space. Explore the chart space as needed. 

### Guidelines and Standards Used
Axis labels are unclear or missing [https://chartability.github.io/POUR-CAF/#__axislabelsareunclearormissing__](https://chartability.github.io/POUR-CAF/#__axislabelsareunclearormissing__)

### Related Evidence
See "Content is only visual" evidence.

### Known or Documented Issues
See "Plot Tools: Content is only visual" evidence forms. 

### Technical Details
- Chrome Version 129.0.6668.59 (64-bit)
- JAWS 2023.2402.1 
- Windows 11 Build 22631.3958

*Updated as of: September 18th, 2024*

### Notes
We fail this overall if it fails for a single modality. 
