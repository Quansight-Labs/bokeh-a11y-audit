# Cues (or Instructions)

## Test Type Performed

Interaction cues or instructions.

If chart has any interactive capabilities at all, it must be explained somewhere for users to understand. All keyboard controls must also be explained as well.

## Artifact Evaluated

[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating both the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) as well as what those interactive capabilities do.

## Results Summary

Plot tools fail for no interaction cues or instructions. There are no explanations that there is a interactive toolbar or for what each tool is, what it does, how to access and what the different tool modes are, and how to use them once they are activated or engaged.

It is especially worse for screen readers as the toolbar icons are not even explained as interactive buttons (missing low level semantics). This will be mentioned again in future tests related to semantics/conforming to standard use of HTML materials.

## Expected Behavior (Pass/Fail)

- _FAIL_ - We would expect interactive controls to be clearly explained for each modal input type. This fails for mouse-click, keyboard-only, and a screen readers that we are testing.

## Image or Video of Failure

```{figure} ./assets/plot-tools_cues-instructions.png
:width: 100%
:alt: A scatter plot is shown. A toolbar for interactive plotting tools is on the right-hand side. No instructions are written in the chart space for how to use the tools (fails).

A scatter plot is shown. A toolbar for interactive plotting tools is on the right-hand side. No instructions are written in the chart space for how to use the tools (fails).
```

## Steps to Reproduce

Navigate using a keyboard, screen reader, and visually from the top of the page to the toolbar and then to the end of the group that the toolbar is part of. If no instructions are encountered before the toolbar, during the toolbar, or after the toolbar, this fails.

## Guidelines and Standards Used

No interaction cues or instructions (critical) [https://chartability.github.io/POUR-CAF/#**nointeractioncuesorinstructions\_**critical\_](https://chartability.github.io/POUR-CAF/#__nointeractioncuesorinstructions___critical_)

## Related Evidence

See "Content is only visual (critical)."

Note that "No explanation for purpose or how to read" may appear identical at first to "interactive context is not clear" as well as "No interaction instructions" since these are all in relation to interactive elements (the plot tools). I'll just clarify here the differences (and copy+paste this section into each of these three):

- **No explanation for purpose or how to read**: An explanation must be provided that helps someone interpret _what_ they see. For interactive tools, it is important that users know what a lasso does (before they use it) and how to interpret what they are looking at if they end up using it.
- **Cues and instructions are not provided**: Instructions must be provided that helps someone figure out _how_ to use things that are interactive. For interactive tools that require anything other than standard input (such as inputting text, clicking/pressing a button, visiting somewhere with a link, etc), users should have instructions available somewhere that help them actually perform the relevant actions.
- **Interactive context is not clear**: This is only relevant for communicating interactivity and change that happens _during_ interaction and when that change takes places somewhere other than the current interaction location. A common example of this is cross-filtering, where using a lasso or selection on one chart changes another chart elsewhere. This change will need to be communicated to users, especially screen reader users.

## Known or Documented Issues

(If there is already a github issue created for this test or a related test, it will be listed here.)

## Technical Details

- Chrome Version 127.0.6533.89 (64-bit)
- JAWS 2023.2402.1
- Windows 11 Build 22631.3958

_Updated as of: August 2nd, 2024_

## Notes

Instructions or cues must be made available visually if the controls perform a visual function. Instructions must always be made available non-visually for screen reader use. Instructions can be provided but then be dismissable on future visits, for cases where the interface is assumed to be used more than once by the same person. In some cases, a simple link (such as before, beneath, or within the tools or a menu) can be provided that will take the user to a "how to use" or instructional area for learning.

In this case, it might not be a bad idea (especially given the close relationship this issue has with "no explanation for purpose" failure) to consider making a "how to interpret and use our tools" page on Bokeh somewhere that is linked to from these tools (like with an informational `( i )` icon or something else).

<!-- A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.  -->
