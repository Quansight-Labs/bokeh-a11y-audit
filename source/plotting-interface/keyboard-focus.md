# Keyboard Focus

## Test Type Performed

Keyboard focus indicator.

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Plotting interface fails for minimum contrast and border size for focus indicators, specifically for the data table and scatter plot's widgets. Results for contrast are 1.07:1 and 1.25:1 (respectively to image evidence below.) Result for focused border size is 1px.

## Expected Behavior (Pass/Fail)

- _FAIL_ - We would expect focus indicators to pass a minimum contrast ratio of 3:1 when focused or unfocused, and a border size of at least 2px.

## Image or Video of Failure

Figure 1

```{figure} ./assets/plotting-interface_contrast-interactive-elements.png
:width: 100%
:alt: A data table is shown. A row is selected and highlighted. The contrast checking score is shown on the bottom left corner at 1:07:1 (fails).

A data table is shown. A row is selected and highlighted. The contrast checking score is shown on the bottom left corner at 1:07:1 (fails).
```

Figure 2

```{figure} ./assets/plotting-interface_keyboard-focus.png
:width: 100%
:alt: A scatter plot is shown. A category tab widget is selected and highlighted. The contrast checking score is shown on the bottom left corner at 1:25:1 (fails).

A scatter plot is shown. A category tab widget is selected and highlighted. The contrast checking score is shown on the bottom left corner at 1:25:1 (fails).
```

## Steps to Reproduce

Navigate elements using a keyboard only (no screen reader or other assistive tech). A focus indicator should be visibly present based on the keyboard's current focus location.

For focus border size: Take a screenshot of the plot tool when the focused border is active, then paste into Figma. Using a rectangle figure too, create a 1x1 pixel box and compare to screenshot border.

For color contrast: Using a dropper tool to gather the color, compare the foreground color against the background color to calculate the contrast score.

In this particular case, we tested the blue "selected" highlight of the data table against the full white background and light-gray hover highlight against the full white background. Avoiding aliased/partial pixels.

## Guidelines and Standards Used

Keyboard focus indicator missing, obscured, or low contrast [https://chartability.github.io/POUR-CAF/#**keyboardfocusindicatormissingobscuredorlowcontrast**](https://chartability.github.io/POUR-CAF/#__keyboardfocusindicatormissingobscuredorlowcontrast__)

## Related Evidence

See "Low contrast interactive elements (critical)" and "Low contrast (critical)" evidence.

## Known or Documented Issues

See "Plot tools: Keyboard focus indicator" evidence.

## Technical Details

- Chrome Version 129.0.6668.59 (64-bit)
- Windows 11 Build 22631.3958

_Updated as of: September 18th, 2024_

## Notes

As of right now, Chartability requires 4.5:1 but we're using the more-lenient WCAG 2.2 3:1 requirements instead (Chartability will use this in the future anyway).

<!-- A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.  -->
