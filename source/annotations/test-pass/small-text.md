### Test Type Performed

Small text size.

### Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/basic/annotations.html#): which include titles, axes labels, labels, legends, colorbar, arrows, and spans (i.e, line).

### Results Summary

Annotations text have 12px text size.

### Expected Behavior (Pass/Fail)

- _Pass_ - Annotations text meets minimum requirement of 9pt/12px.

Titles: Pass at 12pt.

Axes labels: Pass at 9pt.

Legends: Pass at 11pt.

Span text: Pass at 16pt.

Hover tooltip text: Pass at 10pt.

<!-- ### Image or Video of Failure
...

### Steps to Reproduce
... -->

### Guidelines and Standards Used

Small text size [https://chartability.github.io/POUR-CAF/#**smalltextsize\_**critical\_](https://chartability.github.io/POUR-CAF/#__smalltextsize___critical_)

<!-- ### Related Evidence
...

### Known or Documented Issues
... -->

### Technical Details

- Figma
- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

### Notes

I wasn't sure what all was part of the plotting interface when I began that previous testing, so some of these Annotation tests may be redudant. I'm still adding them to this audit branch for the sake of being thorough and consolidating information.
