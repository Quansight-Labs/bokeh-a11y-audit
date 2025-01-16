# Target Pointer Size

## Test Type Performed

Target pointer interaction size.

## Artifact Evaluated

[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769).

## Results Summary

Plot tools pass for interactive elements button size. Results are 30 x 30px.

## Expected Behavior (Pass/Fail)

- _PASS_ - We would expect interaction elements to have a minimum target size of 24 x 24px for mouse or touch modalities. We expect that elements with a visual space of less than 24 x 24px in size are still centered within a non-overlapping 24 x 24px interaction target area (even if invisible).

## Image or Video of Failure

```{figure} ./assets/plot-tools_target-pointer-size.png
:width: 100%
:alt: A screenshot of a interaction plot tool button. The button is highlighted via the command console, and says '30x30' pixels size (passes).

A screenshot of a interaction plot tool button. The button is highlighted via the command console, and says '30x30' pixels size (passes)
```

## Steps to Reproduce

Left click on a desired plot tool button and choose "Inspect." In the Command Console, hover over the element to see how many rendered pixels it is given. You can also take a screenshot and count the pixels in Figma or equivalent.

## Guidelines and Standards Used

Target pointer interaction size is too small [https://chartability.github.io/POUR-CAF/#**targetpointerinteractionsizeistoosmall**](https://chartability.github.io/POUR-CAF/#__targetpointerinteractionsizeistoosmall__)

## Related Evidence

N/A

## Known or Documented Issues

(If there is already a github issue created for this test or a related test, it will be listed here.)

## Technical Details

- Chrome Version 127.0.6533.89 (64-bit)
- Windows 11 Build 22631.3958

_Updated as of: August 2nd, 2024_

## Notes

Note that Chartability uses the older AAA standard, requiring elements to have 44 x 44px for interaction target size. But AA standard was introduced (as a later amendment to WCAG 2.2) that allows 24x24px.

<!--
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels. -->
