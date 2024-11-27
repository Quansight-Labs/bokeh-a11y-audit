# Tedious

## Test Type Performed

Navigation and interaction is not tedious (critical).

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Plotting interface navigation passes for not being tedious. See Notes section below.

## Expected Behavior (Pass/Fail)

- _Pass_ - Large blocks of repeated content must be skippable and interactions where the user is required to perform significant labor must not be considered essential (in content or function). The number of interactions or time required to perform a single task should be measured and compared across modalities (mouse pointer versus sequential keyboard versus search versus voice, etc).

<!-- ## Image or Video of Failure
... -->

<!-- ## Steps to Reproduce
Using a keyboard (for keyboard-only or a SR), press TAB to navigate into the plot toolbar area. Continue to press TAB to cycle through the tools.  -->

## Guidelines and Standards Used

Navigation and interaction is tedious [https://chartability.github.io/POUR-CAF/#**navigationandinteractionistedious\_**critical\_](https://chartability.github.io/POUR-CAF/#__navigationandinteractionistedious___critical_)

## Related Evidence

See "Plot tools: Navigation and interaction is tedious" evidence.

<!-- ## Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

## Technical Details

- Chrome Version 129.0.6668.59 (64-bit)
- Windows 11 Build 22631.3958

_Updated as of: September 18th, 2024_

## Notes

This is a conditional pass. There currently isn't any way to directly interact with any of the chart elements besides the plot tools. So we cannot actively test if interactions would be tedious or not.
