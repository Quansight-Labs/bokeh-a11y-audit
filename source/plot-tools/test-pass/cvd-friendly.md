# CVD Friendly

## Test Type Performed

Color Vision Deficiency (CVD) friendly.

## Artifact Evaluated

[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769).

## Results Summary

Plot tool icons pass multiple CVD tests.

## Expected Behavior (Pass/Fail)

- _Pass_ - We expect any colors used would pass standards for CVD.

## Image or Video of Failure

...

## Steps to Reproduce

Using a dropper tool to gather the RGB color codes, compare the background, icon, toggle button identifier, hover highlight, and button selected highlight colors using a CVD tester.

## Guidelines and Standards Used

Not CVD-friendly [https://chartability.github.io/POUR-CAF/#**notcvdfriendly**](https://chartability.github.io/POUR-CAF/#__notcvdfriendly__)

## Related Evidence

...

## Known or Documented Issues

...

## Technical Details

- Viz4.net/palettes
- Chrome Version 127.0.6533.89 (64-bit)
- Windows 11 Build 22631.3958

_Updated as of: August 2nd, 2024_

## Notes

<!-- A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.  -->
