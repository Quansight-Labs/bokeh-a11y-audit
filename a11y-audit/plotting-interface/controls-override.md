### Test Type Performed
Controls override AT controls (critical)

### Artifact Evaluated
[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

### Results Summary
Test is not applicable.

<!-- ### Expected Behavior (Pass/Fail)
- *Pass* - Special actions (brushing/zooming/filtering/gesturing) that use custom or complex chart controls must have a standard UI alternative available. These controls must be clear and easy to use with a keyboard, screen reader, and touch device. -->

<!-- ### Image or Video of Failure 
<video controls src="plot-tools_complex-actions.mp4" title="Title"></video> -->

<!-- ### Steps to Reproduce
In this case, we cannot even activate the tools (such as the wheel zoom) with a screen reader. Using a keyboard-only approach (no screen reader), it is possible to activate the wheel zoom tool but then using the wheel zoom is impossible without a mouse pointer. -->

### Guidelines and Standards Used
Controls override AT controls (critical) [https://chartability.github.io/POUR-CAF/#__controlsoverrideatcontrols___critical_](https://chartability.github.io/POUR-CAF/#__controlsoverrideatcontrols___critical_)

<!-- ### Related Evidence
See "Low contrast interactive elements (critical)," "Low contrast (critical)," "Content is only visual (critical)," "Interaction modality has only one input type (critical)" and later tests we will perform based on using standard HTML.

### Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

<!-- ### Technical Details
- Chrome Version 129.0.6668.59 (64-bit)
- Windows 11 Build 22631.3958

*Updated as of: September 18th, 2024* -->

### Notes
There are no controls to even interact with the chart so we cannot test this fully. Also to note, there is a keyboard trap at the end of the data table.