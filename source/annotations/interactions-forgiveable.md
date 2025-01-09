# Interactions Forgivable

## Test Type Performed

Interactions are forgivable.

## Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, colorbar, span (i.e, line), text, and arrows.

## Results Summary

Annotations fail for the hover tooltips. There is no easy way to renavigate to a previously hovered point on the line chart.

The interactive legend does pass. It can be easily toggled in a single process and doesn't create hard to replicate actions.

## Expected Behavior (Pass/Fail)

- _FAILS_ - When the visualization is interactive or has the ability to perform a task, the user must be able to both undo or redo their actions in a single process.

## Image or Video of Failure

(similar test provided by plot tools, see below:)

```{video} ./assets/annotations_interactions-forgivable.mp4
:width: 100%
:playsinline:
```

A line chart is shown. A mouse cursor hovers over a plot tool called "Hover." Using the mouse, a user moves to a dashed line in the chart space. The user then hovers over a line (showing a number 47.218) then moves away. They try to hover over the same point again an cannot easily find the same data value.

## Steps to Reproduce

Using a mouse, hover over the line or dashed line on the double line chart. Move your mouse away and try to find the same data point again.

## Guidelines and Standards Used

Interactions are not forgivable [https://chartability.github.io/POUR-CAF/#**interactionsarenotforgiveable**](https://chartability.github.io/POUR-CAF/#__interactionsarenotforgiveable__)

## Related Evidence

See "Plot tools: Interactions are unforgivable" evidence.

<!-- ## Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

## Technical Details

- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

## Notes

The interactive legend works well so when it comes to making it interactable with a SR it will be important to keep the same semantics and mechanics.
