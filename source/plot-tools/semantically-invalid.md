# Semantically Invalid

## Test Type Performed

Semantically valid.

## Artifact Evaluated

[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769).

## Results Summary

Plot tools buttons are div elements, not buttons, which is semantically invalid. "div" elements are not functionally semantic, which means that they do not offer user agents and assistive technologies any programmatic functionality out of the box.

## Expected Behavior (Pass/Fail)

- _FAIL_ - We expect each plot tool and each chart selection tab to be classified as a button and not a div.

## Image or Video of Failure

```{figure} ./assets/plot-tools_semantically-invalid.png
:width: 100%
:alt: The Developer Tools of a web browser is opened. Visually, a button of a scatter plot for the 'pan' tool is highlighted. In HTML, it is a div element (fails).

The Developer Tools of a web browser is opened. Visually, a button of a scatter plot for the 'pan' tool is highlighted. In HTML, it is a div element (fails).
```

## Steps to Reproduce

Right click on a selected element to open the browser's Developer tools console.

## Guidelines and Standards Used

Semantically invalid [https://chartability.github.io/POUR-CAF/#**semanticallyinvalid**](https://chartability.github.io/POUR-CAF/#__semanticallyinvalid__)

## Related Evidence

See "Content is only visual (critical)," "Interaction modality has only one input type (critical)" and later tests we will perform based on using standard HTML.

## Known or Documented Issues

(If there is already a github issue created for this test or a related test, it will be listed here.)

## Technical Details

- Chrome Version 128.0.6613.85 (64-bit)
- JAWS 2023.2402.1
- Windows 11 Build 22631.3958

_Updated as of: August 27th, 2024_

## Notes

A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.
