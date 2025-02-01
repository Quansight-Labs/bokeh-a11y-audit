### Test Type Performed
Navigation and interaction is not tedious (critical).

### Artifact Evaluated
[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769).

### Results Summary
Plot tools navigation passes for not being tedious.

### Expected Behavior (Pass/Fail)
- *Pass* - Plot tools should not create a overly repetitive, restrictive, or convoluted experience when interacting with charts. See "Notes" section at the end.

### Image or Video of Failure 
...

### Steps to Reproduce
Using a keyboard (for keyboard-only or a SR), press TAB to navigate into the plot toolbar area. Continue to press TAB to cycle through the tools. 

### Guidelines and Standards Used
Navigation and interaction is tedious [https://chartability.github.io/POUR-CAF/#__navigationandinteractionistedious___critical_](https://chartability.github.io/POUR-CAF/#__navigationandinteractionistedious___critical_)

### Related Evidence
*See Notes section below.

### Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.)

### Technical Details
- Chrome Version 128.0.6613.85 (64-bit)
- JAWS 2023.2402.1
- Windows 11 Build 22631.3958

*Updated as of: August 27th, 2024*

### Notes
This is a conditional pass. I want to note that this scatter plot chart isn't tedious, but a chart like the color scatter plot - with 17 plot tools - would become particularly tedious for keyboard-only and SR users. 

In the test environment's current state, we can't accurately test how the buttons will work while using a SR, and what that will do for navigation. If we look at the "Changes are not easy to follow" video evidence, we can see that interacting with chart elements resets the user's location to the top of the page. Having to renavigate back to the chart to then renavigate through all the tools becomes overwhelming.