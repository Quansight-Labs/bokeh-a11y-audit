### Test Type Performed

Data in text is not human-readable.

### Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, color bar, span (i.e, line), text, and arrows.

### Results Summary

Annotations fail for human-readability with the hover tooltips. The numbers are too granular for their context. While this is a bit nit-picky, it is technically a failure. "14.311 degrees" is far too many decimal points for this data. 14 would have been fine and 14.3 would have been the sweet spot. But 14.31 is a bit granular (probably still fine). I think 3 decimal points is too far.

This test is _highly_ dependent on the data in context! Dominik Moritz and I have actually had chats about how we think this should be treated. He argues that "5 total digits" is a good approach for precision, which means 14.311 is okay. But here it is too much and becomes tedious for SR users as well as too granular for people with cognitive disabilities.

I actually think that 4-digits-max for precision is a great approach as a default most of the time.

Examples:
.4311
1.431
14.31
143.1
1431

I even think that 3 is _even more_ ideal for visualizations for business/public readership, but understand that it might not satisfy many computational/analytical/scientific contexts:
.431
1.43
14.3
143
1431
...

When making data labels for bars in a bar chart? I follow the 3-digit approach.

Again, in all of these scenarios, problems can arise when the data itself requires precision at a more granular level. And in those cases, I think that there should be ways for developers to override the defaults.

### Expected Behavior (Pass/Fail)

- _FAIL_ - Data must be formatted to be human-readable. All textual information displayed (in data labels, annotations, axes, tables, legends, etc) must be formatted to an understandable level of content (ie “human readable”). These formats must also be made into versions that can be read and parsed comfortably by screen readers. (For example: 6500000000 should be formatted to 6.5b visually and to “six point five billion” when used in screen reader labels and alt text.)

### Image or Video of Failure

```{figure} ./assets/annotations_human-readable.png
    :width: 100%
    :alt: A double line chart is shown. The cursor is hovering over a filled line in the bottom of the chart. There is a tooltip that reads 'Year: 1992.' and 'No. of degrees: 14.311' (fails).

    A double line chart is shown. The cursor is hovering over a filled line in the bottom of the chart. There is a tooltip that reads 'Year: 1992.' and 'No. of degrees: 14.311' (fails).
```

### Steps to Reproduce

Use the Hover tool on the double line chart to hover over either line with the cursor. Continue along the line to observe other values.

### Guidelines and Standards Used

Data in text is not human-readable [https://chartability.github.io/POUR-CAF/#**dataintextisnothumanredable**](https://chartability.github.io/POUR-CAF/#__dataintextisnothumanreadable__)

### Related Evidence

See "Plotting interface: Data is not human-readable" and "Information complexity" evidence.

### Known or Documented Issues

"Plotting interface: Data is not human-readable" evidence.

### Technical Details

- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

### Notes

This evidence could also help with fine-tuning how much information is present/needed on the chart and how much the user needs to look through.
