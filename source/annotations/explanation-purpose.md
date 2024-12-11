### Test Type Performed

Explanation for purpose or for how to read.

### Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, color bar, span (i.e, line), text, and arrows.

### Results Summary

Annotations fail to provide explanations for their elements and how to read or interpret what they mean. (I am not counting the explanation provided before the charts since that is more for audit purposes.)

The line's legend is especially tricky, since it is interactive. The color bar's legend is also a bit tricky, since the height of the bars doesn't actually align with the encoded height of the bars in the chart. I think that particular readability problem might be more of a bug or poor design implementation, but still worth noting as a cognitively difficult thing.

In general, annotations should actually provide valuable explanations and context onto the chart. But it appears that annotations here are treated a bit more like "add text or additional non-dataset elements to the visualization space." That is relatively open and flexible, but the unopinionated nature of it makes it easy to produce elements that are cognitively difficuly, unclear, or incomplete in their communication design.

### Expected Behavior (Pass/Fail)

- _FAIL_ - Chart should explain its purpose and how to read, use, and interpret it.

### Image or Video of Failure

```{figure} ./assets/annotations_explanation-purpose.png
    :width: 100%
    :alt: A screenshot of a double line chart is shown. While there is a title and axes labels, there is no explanation for the chart, that the legend can actually be interacted with, and that it has tooltip capabilities which show you detailed information.

    A screenshot of a double line chart is shown. While there is a title and axes labels, there is no explanation that the legend can actually be interacted with and represents a filtering capability. It is also not entirely clear that a tooltip exists, although this problem is more closely related to Cues and Instructions (see Related Evidence below).
```

### Steps to Reproduce

Nothing in particular needs to be done to reproduce failures.

### Guidelines and Standards Used

No explanation for purpose or for how to read [https://chartability.github.io/POUR-CAF/#**noexplanationforpurposeorforhowtoread\_**critical\_](https://chartability.github.io/POUR-CAF/#__noexplanationforpurposeorforhowtoread___critical_)

### Related Evidence

See "Content is visual only (critical)," "Cues and Instructions," and "Interactive context."

Note that "No explanation for purpose or how to read" may appear identical at first to "interactive context is not clear" as well as "No interaction instructions" since these are all in relation to interactive elements. A short summary of these 3 failures:

Explanation and purpose: must explain what the thing is and what it is for.

Cues and instructures: must help the user locate interactive capabilities and understand how to operate it.

Interactive context: when interactions change things around the interaction location, the context and change must be communicated through feedback.

<!-- ### Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

### Technical Details

- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

<!-- ### Notes
This could be a failure not so much on the annotations and rather the plotting interface, but we'll fail it just to be consistent. -->
