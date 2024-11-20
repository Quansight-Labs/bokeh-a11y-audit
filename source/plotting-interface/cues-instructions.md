# Cues (or Instructions)

## Test Type Performed

Interaction cues or instructions.

If chart has any interactive capabilities at all, it must be explained somewhere for users to understand. All keyboard controls must also be explained as well.

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Plotting interface passes for explanations of any interactive elements. There is a description before the chart that states what is part of each chart and some idea of any interactive elements, like the scatter plot's dropdown widgets.

That being said, it is assumed that this was added specifically to add context for me (as the auditor) and is not something generally part of the plotting interface. For that reason, I'm giving this a pre-emptive failure because there doesn't seem to be guardrails

## Expected Behavior (Pass/Fail)

- _Pre-emptive fail_ - We would expect interactive controls to be clearly explained for each modal input type. (Explanations were provided for the sake of auditing, but not for end users.)

<!-- ## Image or Video of Failure
<figure>
    <img width="803" alt="A scatter plot is shown. A toolbar for interactive plotting tools is on the right-hand side. No instructions are written in the chart space for how to use the tools (fails)." src="./assets/plot-tools_cues-instructions.png">
    <figcaption>A scatter plot is shown. A toolbar for interactive plotting tools is on the right-hand side. No instructions are written in the chart space for how to use the tools (fails).</figcaption>
</figure>

## Steps to Reproduce
Navigate using a keyboard, screen reader, and visually from the top of the page to the toolbar and then to the end of the group that the toolbar is part of. If no instructions are encountered before the toolbar, during the toolbar, or after the toolbar, this fails.  -->

## Guidelines and Standards Used

No interaction cues or instructions (critical) [https://chartability.github.io/POUR-CAF/#**nointeractioncuesorinstructions\_**critical\_](https://chartability.github.io/POUR-CAF/#__nointeractioncuesorinstructions___critical_)

<!-- ## Related Evidence
...

## Known or Documented Issues
... -->

## Technical Details

- Chrome Version 129.0.6668.59 (64-bit)
- Windows 11 Build 22631.3958

_Updated as of: September 18th, 2024_

<!-- ## Notes
Instructions or cues must be made available visually if the controls perform a visual function. Instructions must always be made available non-visually for screen reader use. Instructions can be provided but then be dismissable on future visits, for cases where the interface is assumed to be used more than once by the same person. In some cases, a simple link (such as before, beneath, or within the tools or a menu) can be provided that will take the user to a "how to use" or instructional area for learning.

In this case, it might not be a bad idea (especially given the close relationship this issue has with "no explanation for purpose" failure) to consider making a "how to interpret and use our tools" page on Bokeh somewhere that is linked to from these tools (like with an informational `( i )` icon or something else). -->

<!-- A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.  -->
