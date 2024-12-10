# Design Consistent

## Test Type Performed

Design is consistent and familiar.

## Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, colorbar, span (i.e, line), text, and arrows.

## Results Summary

Annotations pass for design consistency and familiarity, even if not all charts share the same features. See "Notes" section below.

## Expected Behavior (Pass/Fail)

- _Pass_ - We expect that any tools used by multiple charts would implement the same design and interactivity from one to another.

<!-- ## Image or Video of Failure
...

## Steps to Reproduce
... -->

## Guidelines and Standards Used

Design is not consistent and familiar [https://chartability.github.io/POUR-CAF/#**designisnotconsistentandfamiliar**](https://chartability.github.io/POUR-CAF/#__designisnotconsistentandfamiliar__)

<!-- ## Related Evidence
...

## Known or Documented Issues
... -->

## Technical Details

- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

## Notes

This is a conditional pass due to the state the charts and tools are currently in, but in general the same design happens across different chart types, browsers, devices, software, and OS.
