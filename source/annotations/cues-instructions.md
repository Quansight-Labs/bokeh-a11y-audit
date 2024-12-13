### Test Type Performed

Interaction cues or instructions.

If chart has any interactive capabilities at all, it instructions must be provided somewhere for users to understand. All keyboard controls must also be explained as well.

### Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, color bar, span (i.e, line), text, and arrows.

### Results Summary

Annotations fail for explanations of the interactive legend and hover tooltip, as well as the keyboard controls for these elements.

If sighted users were just looking at the charts they would not be able to tell the double line chart's legend is interactive and that the scatter plot's legend is not.

Although the hover tooltip is on by default, a user may not understand that it is a tool on the tool bar and it may not exist on the other charts. Also, there is no explanation provided for how hovering works, like what (if anything) a user can do with it.

In general, hovering to receive tooltips is a ubiquitous practice in data visualization, so you may not need to provide instructions for how to do this. However, it might be nice to have a link provided in the menu for all visualizations that points to the same article about how to interact with different Bokeh charts.

### Expected Behavior (Pass/Fail)

- _Pre-emptive fail_ - We would expect interactive controls to be clearly explained for each modal input type. (Explanations were provided for the sake of auditing, but not for end users. And these explanations were not _instructions_ either. See Related Evidence note below about disambiguating related cognitive + operability tests.)

### Image or Video of Failure

````
  ```{video} ./assets/annotations_cues-instructions.mp4
  :width: 100%
  :playsinline:
  ```
````

A video of a web browser is shown with multiple chart types. The user interacts with the right chart on the page, using their mouse to hover over a dashed line. A tooltip window pops up as they move alone each data point. Next, they click the labels in the legend to mute and unmute each line. They then move their cursor over to the left chart. No tooltips appear as they hover over the line. Finally, they scroll down to the final chart, a scatter plot. They attempt to click the labels in the legend, but nothing happens.

### Steps to Reproduce

No specific requirements to reproduce.

### Guidelines and Standards Used

No interaction cues or instructions (critical) [https://chartability.github.io/POUR-CAF/#**nointeractioncuesorinstructions\_**critical\_](https://chartability.github.io/POUR-CAF/#__nointeractioncuesorinstructions___critical_)

### Related Evidence

See "Keyboard focus," "Content is visual only (critical)," "Explanation for purpose," and "Interactive context."

Note that "No explanation for purpose or how to read" may appear identical at first to "interactive context is not clear" as well as "No interaction instructions" since these are all in relation to interactive elements. A short summary of these 3 failures:

Explanation and purpose: must explain what the thing is and what it is for.

Cues and instructures: must help the user locate interactive capabilities and understand how to operate it.

Interactive context: when interactions change things around the interaction location, the context and change must be communicated through feedback.

<!-- ### Known or Documented Issues
... -->

### Technical Details

- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

### Notes

I was thinking about this from a new user perspective and it may be important to think about how to help users understand that different developers and designers might implement tooltips and legends (and other interactive pieces) in different ways. A hard problem!
