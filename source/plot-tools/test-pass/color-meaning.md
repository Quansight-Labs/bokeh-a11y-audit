# Color Meaning

## Test Type Performed

Color is used alone to communicate meaning.

## Artifact Evaluated

[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769).

## Results Summary

Plot tool icons pass. When a tool is selected there is a dashed, blue line bordering the icon. When the icon is toggled "On", there is a thicker, blue line on the left border of the box.

## Expected Behavior (Pass/Fail)

- _Pass_ - We expect any interactions on a chart space to notify the user with more than color alone.

## Image or Video of Failure

...

## Steps to Reproduce

Using a mouse or keyboard, click on or TAB then ENTER to the desired plot tool. Icons can be selected again to toggle "on/off" settings.

## Guidelines and Standards Used

Color is used alone to communicate meaning [https://chartability.github.io/POUR-CAF/#**colorisusedalonetocommunicatemeaning**](https://chartability.github.io/POUR-CAF/#__colorisusedalonetocommunicatemeaning__)

## Related Evidence

...

## Known or Documented Issues

...

## Technical Details

- Chrome Version 127.0.6533.89 (64-bit)
- Windows 11 Build 22631.3958

_Updated as of: August 2nd, 2024_

## Notes

<!-- A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.  -->
