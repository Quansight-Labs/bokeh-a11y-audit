### Test Type Performed

Visually apparent features and relationships are described.

### Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, color bar, span (i.e, line), text, and arrows.

### Results Summary

Annotations fail for providing minimum descriptions for visual features. The "Mean" span line on the bar chart is one such example. This annotation is great! But it isn't available to screen readers.

### Expected Behavior (Pass/Fail)

- _FAIL_ - Trends, clusters, patterns, outliers, or significant statistical semantics and findings that are considered “visually apparent” must be described through text at a minimum. Optionally, these features may also be exposed using sonification or tactile means or through other multi-sensory approaches.

<!-- ### Image or Video of Failure
First image:
<figure>
    <img width="803" alt="A scatter plot is shown in it's default view. There are 3 clusters in the shape of a downward pointing triangle." src="../assets/plot-tools_visually-apparent-features_1.png">
    <figcaption>A scatter plot is shown in it's default view. There are 3 clusters in the shape of a downward pointing triangle.</figcaption>
</figure> -->

### Steps to Reproduce

Using a screen reader, navigate to a chart and into chart areas (when available). Regions that have visual significance from an analytical perspective should be described in some text or alt text. Clusters, trends, and visual features produced as a result of the plotting techniques combined with the data in their visual-aggregate must be summarized and described.

In this case: annotations in the chart that refer to or call out visual or statistical features should be navigable to screen readers and announce their content.

### Guidelines and Standards Used

Visually apparent features and relationships are not described [https://chartability.github.io/POUR-CAF/#**visuallyapparentfeaturesandrelationshipsarenotdescribed**](https://chartability.github.io/POUR-CAF/#__visuallyapparentfeaturesandrelationshipsarenotdescribed__)

### Related Evidence

See "Visual only" evidence.

<!-- ### Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

### Technical Details
- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

*Updated as of: October 22nd, 2024*

### Notes

How this fits into the narrative structure (see "Narrative structure") will eventually be important to consider.