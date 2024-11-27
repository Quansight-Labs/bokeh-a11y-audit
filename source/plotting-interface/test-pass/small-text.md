# Small Text

## Test Type Performed

Small text size.

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Plotting interface texts have 12px text size.

## Expected Behavior (Pass/Fail)

- _Pass_ - Plotting interface text meets minimum requirement of 9pt/12px.

## Image or Video of Failure

...

## Steps to Reproduce

...

## Guidelines and Standards Used

Small text size [https://chartability.github.io/POUR-CAF/#**smalltextsize\_**critical\_](https://chartability.github.io/POUR-CAF/#__smalltextsize___critical_)

## Related Evidence

...

## Known or Documented Issues

...

## Technical Details

- Chrome Version 128.0.6613.120 (64-bit)
- Windows 11 Build 22631.3958

_Updated as of: September 10th, 2024_

## Notes

While the text does pass for desktops, from previous tests with the plot tools, we know that mobile devices do not scale correctly and the font size becomes smaller. (See Zoom and reflow are not supported" evidence.)
