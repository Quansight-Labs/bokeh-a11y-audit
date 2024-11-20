### Test Type Performed

Visually apparent features and relationships are described.

### Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

### Results Summary

First to note, nothing is describing the features in the charts. The line charts, for example, provide no text that the line trends up. The scatter plot does not describe itself as having 3 clusters or 3 different data sets. These details can only be visually seen or known. This makes it paricularly a failure for SR users.

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

### Guidelines and Standards Used

Visually apparent features and relationships are not described [https://chartability.github.io/POUR-CAF/#**visuallyapparentfeaturesandrelationshipsarenotdescribed**](https://chartability.github.io/POUR-CAF/#__visuallyapparentfeaturesandrelationshipsarenotdescribed__)

### Related Evidence

See "No explanation for purpose or for how to read (critical)" and "No title, summary, or caption (critical)" evidence forms.

<!-- ### Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

### Technical Details

- Chrome Version 129.0.6668.59 (64-bit)
- JAWS 2023.2402.1
- Windows 11 Build 22631.3958

_Updated as of: September 18th, 2024_

### Notes

Clearly this is failing because there is core functionality missing to describe things not specific to only the plot tools, but to the chart as a whole.
