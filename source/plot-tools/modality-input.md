# Modality input

## Test Type Performed

Interaction modality only has one input type.

## Artifact Evaluated

[Plot tools](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/tools.html#ug-interaction-tools). Specifically, evaluating the interface icons that are used to access the tools that are in the [scatter plot](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769).

## Results Summary

Plot tools fail for keyboard and screen reader, and some mouse input types. The mouse cannot access the different modes of a selected tool without also using SPACE on a keyboard, but this is not made clear.

Some keyboard interactions work as intended, but the tools are not usable on the chart once selected. A keyboard-only user has to TAB through all the plot tools in order to switch between a specific tool's mode. Also, the plot widget can be TAB-bed to, but cannot be accessed. To return back to the desired tool afterwards, you would need re-navigate back. There is also no tooltips for the user to know what tool is currently selected, like you would see on a mouse hover.

The screen reader TAB focus moves forward to the buttons, but they are not interactable. When using JAWS and interacting with these buttons, JAWS reverts to the previously visited link. There are also no audio tooltips for the user to know what tool is currently selected, like you would see on a mouse hover.

## Expected Behavior (Pass/Fail)

- _FAIL_ - We would expect interactive elements to be comparably usable between mouse, keyboard, and screen reader devices. All tools and tool options should be easily accessed.

## Image or Video of Failure

First video: Mouse-click input. From 00:10-00:15s, a keyboard is used to show mouse incapability.
<video controls src="assets/plot-tools_modality-input-type_mouse.mp4" title="Title"></video>

Second video: Keyboard-only input. From 00:28-00:38s, the tester SHIFT+TABto move backwards back into the scatter plot testing area (continuing to TAB after selecting a specific tool mode brings the user to the top of the page versus staying in the chart space.)
From 00:43-00:47 the tester is trying to interact in the chart space with the tool, but cannot.
<video controls src="assets/plot-tools_modality-input-type_keyboard.mp4" title="Title"></video>

Third video: JAWS screen reader input.
<video controls src="assets/plot-tools_modality-input-type_SR.mp4" title="Title"></video>

## Steps to Reproduce

Mouse-click:

Keyboard: Using TAB, navigate to the scatter plot chart. Pressing TAB twice more should bring you to the plot tools bar.

JAWS screen reader:

## Guidelines and Standards Used

Interaction modality only has one input type (critical) [https://chartability.github.io/POUR-CAF/#**interactionmodalityonlyhasoneinputtype\_**critical\_](https://chartability.github.io/POUR-CAF/#__interactionmodalityonlyhasoneinputtype___critical_)

## Related Evidence

See "Content is only visual (critical)" evidence.

## Known or Documented Issues

(If there is already a github issue created for this test or a related test, it will be listed here.)

## Technical Details

- Chrome Version 127.0.6533.89 (64-bit)
- JAWS 2023.2402.1
- Windows 11 Build 22631.3958

_Updated as of: August 2nd, 2024_

## Notes

A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.
