# Changes Easy to Follow

## Test Type Performed

Changes are easy to follow.

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Pre-emptive failure: I assume this fails, but in order to test we need to change the data and render the chart with new data (updating it).

## Expected Behavior (Pass/Fail)

- _FAIL_ - The plot tools only offer visual feedback for any changes occurring in the chart. Although the tools currently cannot be accessed with a SR, I expect they would fail to announce the meaningful changes to the chart area.
  For example, when interacting with the scatterplot's tabs, there is so clear indication to SR users if their input worked or if changes occurred. The tabs also do not note what is currently selected when you renavigate to the "Selected Species" tab. The SR is simply announcing what the user has done, like pressing ENTER. (See video evidence below for example.)

<!-- ## Image or Video of Failure
<video controls src="plot-tools_changes-easy-to-follow.mp4" title=""></video>
A scatter plot is shown. A screen reader is navigating through the chart's dropdown menu, but when an option is selected, the user is forced back to the top of the webpage.  (fails). -->

<!-- ## Steps to Reproduce
In this case, we cannot even activate the tools (such as the pan) with a screen reader. For the video example above, navigate to the scatter plot header. Use TAB to navigate to the chart. TAB until you get to the "Selected Species" tab. Press ENTER to open the menu, then select desired option and press ENTER again. -->

## Guidelines and Standards Used

Changes are not easy to follow [https://chartability.github.io/POUR-CAF/#**changesarenoteasytofollow**](https://chartability.github.io/POUR-CAF/#__changesarenoteasytofollow__)

<!-- ## Related Evidence
See "Low contrast (critical)," "Content is only visual (critical)," "Interaction modality has only one input type (critical)" and later tests we will perform based on using standard HTML. -->

<!-- ## Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.)

## Technical Details
- Chrome Version 129.0.6668.59 (64-bit)
- Hemingway Editor browser app
- Windows 11 Build 22631.3958

*Updated as of: September 18th, 2024* -->

<!-- ## Notes
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels. -->
