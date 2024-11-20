# Fragile Support

## Test Type Performed

Technology support.

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Plotting interface fails to give access across different technologies, most notably with screen reader software. For example, there is varying support between browsers for SRs, but nothing consistent. Google Chrome can use heading navigation and announce heading names, but Firefox cannot.

## Expected Behavior (Pass/Fail)

- _FAILS_ - Chart access must not be isolated to one browser, device, software, or operating system. There must be a diversity of technological means to access the chart and its information and functionality.

## Image or Video of Failure

```{video} ./assets/plotting-interface_fragile_support.mp4
:width: 100%
:playsinline:
```

A line chart is shown. A screen reader attempts to navigate by headings using the "H" control, and can be heard stating "H". No heading navigation occurs. The user then presses TAB to navigate forward before attempting once again to use H to get to the headings. It fails once more.

## Steps to Reproduce

Open the Quansight Bokeh test environment web page in Firefox web browser. Then open the JAWS software and press "H" to attempt to navigate forward by headings.

## Guidelines and Standards Used

Fragile technology support [https://chartability.github.io/POUR-CAF/#**fragiletechnologysupport**](https://chartability.github.io/POUR-CAF/#__fragiletechnologysupport__)

## Related Evidence

See "Content is visual only" and "Semantically Invalid" evidence forms.

## Known or Documented Issues

...

## Technical Details

- Chrome Version 129.0.6668.59 (64-bit)
- Mozilla Firefox 129.0.2 (64-bit)
- JAWS 2023.2402.1
- Windows 11 Build 22631.3958
- Apple iPad Air Version 17.6

_Updated as of: September 18th, 2024_

<!-- ## Notes
This is a conditional pass due to the state the tools are currently in, but in general the same functionality happens across different browsers, devices, software, and OS.  -->
