# Explanation Purpose

## Test Type Performed

Explanation for purpose or for how to read.

## Artifact Evaluated

[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769).

## Results Summary

Plot tools fail for providing no explanation of what they are and how to interpret what they do.

## Expected Behavior (Pass/Fail)

- _FAIL_ - We would expect the chart to explain the plot toolbar's purpose, what each interactive tool is, and how to interpret the results of their use.

In this particular case, we focused on keyboard-only and SR interactions and explanations. For the mouse, we did not consider the hover tooltips as explanations.

## Image or Video of Failure

```{figure} ./assets/plot-tools_explanation-purpose.png
:width: 100%
:alt: A screenshot a scatterplot is shown. On the right, there is a column of a toolbar for interactive buttons.

A screenshot a scatterplot is shown. On the right, there is a column of a toolbar for interactive buttons.
```

## Steps to Reproduce

Navigate to the "Scatterplot" chart heading.

## Guidelines and Standards Used

No explanation for purpose or for how to read [https://chartability.github.io/POUR-CAF/#**noexplanationforpurposeorforhowtoread\_**critical\_](https://chartability.github.io/POUR-CAF/#__noexplanationforpurposeorforhowtoread___critical_)

## Related Evidence

See "Content is visual only (critical)" evidence.

Note that "No explanation for purpose or how to read" may appear identical at first to "interactive context is not clear" as well as "No interaction instructions" since these are all in relation to interactive elements (the plot tools). I'll just clarify here the differences (and copy+paste this section into each of these three):

- **No explanation for purpose or how to read**: An explanation must be provided that helps someone interpret _what_ they see. For interactive tools, it is important that users know what a lasso does (before they use it) and how to interpret what they are looking at if they end up using it.
- **Cues and instructions are not provided**: Instructions must be provided that helps someone figure out _how_ to use things that are interactive. For interactive tools that require anything other than standard input (such as inputting text, clicking/pressing a button, visiting somewhere with a link, etc), users should have instructions available somewhere that help them actually perform the relevant actions.
- **Interactive context is not clear**: This is only relevant for communicating interactivity and change that happens _during_ interaction and when that change takes places somewhere other than the current interaction location. A common example of this is cross-filtering, where using a lasso or selection on one chart changes another chart elsewhere. This change will need to be communicated to users, especially screen reader users.

## Known or Documented Issues

(If there is already a github issue created for this test or a related test, it will be listed here.)

## Technical Details

- Chrome Version 127.0.6533.120 (64-bit)
- Windows 11 Build 22631.4037

_Updated as of: August 16th, 2024_

## Notes

In this case, it might not be a bad idea (especially given the close relationship this issue has with "cues and instructions" failure) to consider making a "how to interpret and use our tools" page on Bokeh somewhere that is linked to from these tools (like with an informational `( i )` icon or something else).

 <!--
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels. -->
