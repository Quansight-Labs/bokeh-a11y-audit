# Contrast Interactive Elements

## Test Type Performed

Low contrast on interactive elements.

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Plotting interface fails for minimum contrast on interactive elements for the data table. Results are 1.07:1.

## Expected Behavior (Pass/Fail)

- _FAIL_ - We would expect interactive elements to pass a contrast ratio of 3:1 for the new state change against its previous state.

## Image or Video of Failure

```{figure} ./assets/plotting-interface_contrast-interactive-elements.png
:width: 100%
:alt: A data table is shown. A row is selected and highlighted. The contrast checking score is shown on the bottom left corner at 1:07:1 (fails).

A data table is shown. A row is selected and highlighted. The contrast checking score is shown on the bottom left corner at 1:07:1 (fails).
```

## Steps to Reproduce

Using a dropper tool to gather the color, compare the foreground color against the background color to calculate the contrast score.

In this particular case, we tested the blue "selected" highlight of the data table against the full white background. Avoiding aliased/partial pixels.

## Guidelines and Standards Used

Low contrast on interactive elements [https://chartability.github.io/POUR-CAF/#**lowcontrastoninteractiveelements**](https://chartability.github.io/POUR-CAF/#__lowcontrastoninteractiveelements__)

## Related Evidence

See "Low contrast (critical)" evidence.

<!-- ## Known or Documented Issues
... -->

## Technical Details

- Chrome Version 129.0.6668.59 (64-bit)
- Windows 11 Build 22631.3958

_Updated as of: September 18th, 2024_

<!-- ## Notes
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.  -->
