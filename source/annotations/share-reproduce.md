# Share Reproduce

### Test Type Performed

State is not easy to share and reproduce.

### Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, color bar, span (i.e, line), text, and arrows.

### Results Summary

Annotations fail for being able to share and reproduce custom edits to the charts. Complete fail if the user attempts to share via URL (charts retain their default settings).

Legend: Limited - able to mute and unmute labels and have those edits remain ONLY if the chart's own share button is used.

Hover tooltip: Fails - cannot be saved or "selected" to stay on screen.

### Expected Behavior (Pass/Fail)

- _FAIL_ - Chart state must be easy to share and reproduce. If an analysis or complex interaction can produce a customized view, this view must be easy to share (such as with a single link, file, or saved state).

### Image or Video of Failure

Figure 1: Using the chart's filtering function

```{figure} ./assets/annotations_share-reproduce_1.png
:width: 100%
:alt: A line chart is shown. A blue dashed line labeled 'Business' is the main focus, while the 'Engineering' line has been toggled off (it is faded and grayed).

A line chart is shown. A blue dashed line labeled 'Business' is the main focus, while the 'Engineering' line has been toggled off (it is faded and grayed).
```

Figure 2: Video sharing URL

```{video} ./assets/annotations_share-reproduce_2.mp4
:width: 100%
:playsinline:
```

The user makes custom edits to a line chart (deselecting a filled line in the interactive legend and zooming in). They then copy and paste the URL into a new window. None of their changes to the chart transfer over to the new window. Refreshing the page, the changes are also lost.

### Steps to Reproduce

1. Interact and change the state of the chart (toggle the legend labels on or off.)
2. Locate any way that enables sharing this state (such as via a URL, button, state export file, etc).
3. Locate how to import or load this changed state upon page or application refresh.
4. Test fails if 1 is possible and either 2 and 3 are not easily possible.

### Guidelines and Standards Used

State is not easy to share and reproduce [https://chartability.github.io/POUR-CAF/#**axislabelsareunclearormissing**](https://chartability.github.io/POUR-CAF/#__axislabelsareunclearormissing__)

<!-- ### Related Evidence
See "Plotting interface: State is not easy to share and reproduce" evidence.  -->

### Known or Documented Issues

See "Plotting interface: State is not easy to share and reproduce" evidence.

### Technical Details

- JAWS 2023.2402.1
- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

<!-- ### Notes

Downloading the current state of the chart is an awesome feature for accessibility, but I also recommend adding url queries to any online application/demo where people are able to manipulate the view of a chart or charts as well. For example, if plot tools are used to change the coordinates or view of a chart or (for the scatter plot) if dropdowns/tabs or other interface elements can be interacted with to change the application state, that exact state can be accessed by someone else simply by sharing the user's current URL. Google maps (accessed via browser) is incredible at this. They encode zoom, angle of view, coordinates, and current user selection in the URL for the sake of sharing interaction state. -->
