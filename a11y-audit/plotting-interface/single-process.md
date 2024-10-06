### Test Type Performed
Information can only be reached through single process. 

### Artifact Evaluated
[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

### Results Summary
Plotting interface does not provide alternative means to change states outside of utilizing the plot tools or the content being visual.

### Expected Behavior (Pass/Fail)
- *FAIL* - There must be more than one process available to reach the same information. If chart is contained within or participates in complex user interface flows, such as transitions between views or states, interacting with filters, or moving between pages, there must be alternative paths to reach that same state (such as with search features, table of contents, parallel UI controls, etc).

<!-- ### Image or Video of Failure 
<figure>
    <img width="803" alt="A browser Command Console window is open. A red line is highlighting the font size '12px' (passes)" src="../assets/plotting-interface_color-contrast_1.png">
    <figcaption>A browser Command Console window is open. A red line is highlighting the font size '12px' (passes).</figcaption>
</figure>

### Steps to Reproduce
Use Inspect on the plot tool icon to open Console Command. Find the "style" section for the selected button then locate the font size. -->

### Guidelines and Standards Used
Information can only be reached through single process [https://chartability.github.io/POUR-CAF/#__informationcanonlybereachedthroughsingleprocess__](https://chartability.github.io/POUR-CAF/#__informationcanonlybereachedthroughsingleprocess__)

### Related Evidence
See "Content is only visual" evidence. 

<!-- ### Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

### Technical Details
- Chrome Version 129.0.6668.59 (64-bit)
- JAWS 2023.2402.1 
- Windows 11 Build 22631.3958

*Updated as of: September 18th, 2024*

<!-- ### Notes
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels. -->
