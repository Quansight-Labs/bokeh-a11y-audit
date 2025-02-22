# Seizure Risk

## Test Type Performed

Visual presents seizure risk.

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Passes.

## Expected Behavior (Pass/Fail)

- _PASS_ - Plotting interface does not pose a seizure risk.

## Image or Video of Failure

```{video} ../assets/plotting-interface_PEAT-seisure.mp4
:width: 100%
:playsinline:
```

A line chart, bar chart, and scatter plot are shown on a web browser. The user is selecting and deselecting tools rapidly to make the highlight color "flash". They then zoom in and out on each chart rapidly to check for any seizure risks (passes).

## Steps to Reproduce

Record screen while using interactive features and elements and then run that through PEAT software. In addition, check against common heuristics from WCAG (number of flashes present on the screen per second, etc).

## Guidelines and Standards Used

Visual presents seizure risk [https://chartability.github.io/POUR-CAF/#**visualpresentsseizurerisk\_**critical\_](https://chartability.github.io/POUR-CAF/#__visualpresentsseizurerisk___critical_)

## Related Evidence

...

## Known or Documented Issues

...

## Technical Details

- Chrome Version 128.0.6613.120 (64-bit)
- PEAT 1.6 (Photosensitive Epilepsy Analysis Tool)
- Windows 11 Build 22631.3958

_Updated as of: September 10th, 2024_

<!-- ## Notes
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.  -->
