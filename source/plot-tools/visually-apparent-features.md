# Visually Apparent Features

## Test Type Performed
Visually apparent features and relationships are described.

## Artifact Evaluated
[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769).

## Results Summary
First to note, nothing is describing the features in the charts. The chart does not describe itself as having 3 clusters (first image). This creates an issue that if I use any tool such as zooming, nothing describes the changes for any of the charts visuals or relationships. When I zoom out, the chart now appears to only have a single cluster (second image). If I now zoom in, it can get to a point where there are no clusters at all (third image).

## Expected Behavior (Pass/Fail)
- *FAIL* - Plot tools need to provide feedback to users for the changes the tools create while interacting with the chart. See "Notes" section at the end.

## Image or Video of Failure 
First image:
```{figure} ./assets/plot-tools_visually-apparent-features_1.png
:width: 100%
:alt: A scatter plot is shown in it's default view. There are 3 relatively distinct clusters.

A scatter plot is shown in it's default view. There are 3 relatively distinct clusters.
```

Second image:
```{figure} ./assets/plot-tools_visually-apparent-features_2.png
:width: 100%
:alt: A scatter plot is shown. The user has zoomed out to the point where the data now appears to be only a single cluster, just off-center. No where on screen is there a description what what has happened (fails).

A scatter plot is shown. The user has zoomed out to the point where the data now appears to be only a single cluster, just off-center. No where on screen is there a description what what has happened (fails).
```

Third image:
```{figure} ./assets/plot-tools_visually-apparent-features_3.png
:width: 100%
:alt: A scatter plot is shown. The user has zoomed in to the point where the data appears to have no clusters at all, and the points are somewhat indistinguishable. No where on screen is there a description what what has happened (fails).

A scatter plot is shown. The user has zoomed in to the point where the data appears to have no clusters at all, and the points are somewhat indistinguishable. No where on screen is there a description what what has happened (fails).
```

## Steps to Reproduce
Use the "Wheel zoom" plot tool and interact with the chart to change it's view or state.

## Guidelines and Standards Used
Visually apparent features and relationships are not described [https://chartability.github.io/POUR-CAF/#__visuallyapparentfeaturesandrelationshipsarenotdescribed__](https://chartability.github.io/POUR-CAF/#__visuallyapparentfeaturesandrelationshipsarenotdescribed__)

## Related Evidence
No related evidence currently.

## Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.)

## Technical Details
- Chrome Version 128.0.6613.85 (64-bit)
- Windows 11 Build 22631.3958

*Updated as of: August 27th, 2024*

## Notes
Clearly this is failing because there is core functionality missing that would be able to describe things not only for the plot tools, but to the chart as a whole at any given moment.