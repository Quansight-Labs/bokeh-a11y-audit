# Scrolling

## Test Type Performed

Scrolling experiences can be altered.

## Artifact Evaluated

[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

## Results Summary

Plotting interface fails for allowing infinite scrolling in the charts. While there is the option to turn on/off the scrolling, it can be over used to the point of confusion and complexity.

## Expected Behavior (Pass/Fail)

- _FAIL_ - Scrolling experiences must provide a way to be adjusted or opted out of. Infinite scrolling, parallax scrolling, and “scrollytelling” experiences must come with the ability to be turned off or used optionally, with an option like “load more” or “next” in its place for keyboard only users.

## Image or Video of Failure

```{figure} ./assets/plotting-interface_scrolling.png
:width: 100%
:alt: Two line charts are shown side by side. The chart on the left has been scrolled out so far that you barely see it in the center, and cannot gain any information from it. The chart on the right is scrolled in the point where the lines are not visible at all.

Two line charts are shown side by side. The chart on the left has been scrolled out so far that you barely see it in the center, and cannot gain any information from it. The chart on the right is scrolled in the point where the lines are not visible at all.
```

## Steps to Reproduce

Using the line chart's scrolling tool, scroll forward or backward continually to change the chart's view.

## Guidelines and Standards Used

Scrolling experiences cannot be altered [https://chartability.github.io/POUR-CAF/#**scrollingexperiencescannotbealtered**](https://chartability.github.io/POUR-CAF/#__scrollingexperiencescannotbealtered__)

<!-- ## Related Evidence
(Added if additional evidence has already been gathered for related elements. This will not be edited retroactively, however, due to scope creep. This means that the latest issues will have the most Related Evidence listed.) -->

<!-- ## Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

## Technical Details

- Chrome Version 129.0.6668.59 (64-bit)
- Windows 11 Build 22631.3958

_Updated as of: September 18th, 2024_

<!-- ## Notes
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels. -->
