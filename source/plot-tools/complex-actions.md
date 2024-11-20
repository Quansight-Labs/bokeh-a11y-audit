# Complex Actions

## Test Type Performed

Complex actions have alternatives.

## Artifact Evaluated

[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769).

## Results Summary

Plot tools fail for standard UI alternatives for custom/complex chart controls. Anything that isn't "standard" (uses a `<button>`, `<a>`, `<input>`, etc default interaction) must have a `<button>`, `<a>`, `<input>`, or other "simple" kind of interaction provided somewhere as an alternative. And if it is hard or impossible to accomplish providing a 1:1 replacement for the interaction type (like with a lasso-type selection), then at least an easy-to-use alternative should be provided that can still accomplish the same interaction goals (if a lasso can make complex, spatial selections of data, then some equivalent method of complex selection should be available). Sometimes this requires creativity, such as by adding a search function or by provided the option to filter or manipulate input data directly (with an interactive table or command line). Consider also sonification or interaction outside of the visual space.

## Expected Behavior (Pass/Fail)

- _FAIL_ - Special actions (brushing/zooming/filtering/gesturing) that use custom or complex chart controls must have a standard UI alternative available. These controls must be clear and easy to use with a keyboard, screen reader, and touch device.

## Image or Video of Failure

```{video} ./assets/plot-tools_complex-actions.mp4
:width: 100%
:playsinline:
```

## Steps to Reproduce

In this case, we cannot even activate the tools (such as the wheel zoom) with a screen reader. Using a keyboard-only approach (no screen reader), it is possible to activate the wheel zoom tool but then using the wheel zoom is impossible without a mouse pointer.

## Guidelines and Standards Used

Complex actions have no alternatives [https://chartability.github.io/POUR-CAF/#**complexactionshavenoalternatives**](https://chartability.github.io/POUR-CAF/#__complexactionshavenoalternatives__)

## Related Evidence

See "Low contrast interactive elements (critical)," "Low contrast (critical)," "Content is only visual (critical)," "Interaction modality has only one input type (critical)" and later tests we will perform based on using standard HTML.

## Known or Documented Issues

(If there is already a github issue created for this test or a related test, it will be listed here.)

## Technical Details

- Chrome Version 127.0.6533.89 (64-bit)
- Windows 11 Build 22631.3958

_Updated as of: August 2nd, 2024_

## Notes

A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.
