### Test Type Performed

Technology support.

### Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, color bar, span (i.e, line), text, and arrows.

### Results Summary

Annotations fail to give access across different technologies, most notably with screen reader software. Overall, the charts have the same issues with interactivity with annotation elements over various environments.

### Expected Behavior (Pass/Fail)

- _FAILS_ - Chart access must not be isolated to one browser, device, software, or operating system. There must be a diversity of technological means to access the chart and its information and functionality.

### Image or Video of Failure

Figure 1: Chrome with JAWS (Previous recording show similar/related evidence).

````
  ```{video} ./assets/annotations_visual-only.mp4
  :width: 100%
  :playsinline:
  ```
````

A video shows a web browser with multiple charts. A screen reader navigates through the page and through multiple charts, but very limited information is given as they do so. The user (a sighted tester, in this case) navigates to the "Hover" tool on the toolbar and presses enter to interact with it, but this opens a link to a new webpage (fails).

Figure 2: Firefox with JAWS

````
  ```{video} ./assets/annotations_fragile-support_firefox.mp4
  :width: 100%
  :playsinline:
  ```
````

A video shows multiple charts in a Firefox browser. A screen reader navigates through the page and through multiple charts, but very limited information is given as they do so. The only information that is relayed from the charts are "Bokeh.org link."

Figure 3: Mobile

````
  ```{video} ./assets/annotations_modality-input.mp4
  :width: 100%
  :playsinline:
  ```
````

From the default mobile browser view, the tester navigates the second line chart. They then touch select (shown with a green circle and blue border) the interactive legend to toggle the categories on and off. Next, they pinch to zoom in on the page to get a closer view of the chart. The tester runs their finger along the filled line to try and view the hover tool tip. While it does show at times, the user cannot consistently get it to show. They repeat the process with the dashed line on the chart.

### Steps to Reproduce

Open the Quansight Bokeh test environment web page in: Chrome and Firefox with PC/laptops and mobile phone. Interact with the charts with both mouse and keyboard-only.
Next, open the JAWS software in both web browsers and press TAB to navigate.

### Guidelines and Standards Used

Fragile technology support [https://chartability.github.io/POUR-CAF/#**fragiletechnologysupport**](https://chartability.github.io/POUR-CAF/#__fragiletechnologysupport__)

### Related Evidence

See "Content is visual only," "Semantically Invalid," "Narrative structure," and "Keyboard focus" evidence.

### Known or Documented Issues

See both "Plot tools" and "Plotting interface" tests.

### Technical Details

- Chrome Version 130.0.6723.59 (64-bit)
- Mozilla Firefox 133 (64-bit)
- JAWS 2023.2402.1
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

<!-- ### Notes
This is a conditional pass due to the state the tools are currently in, but in general the same functionality happens across different browsers, devices, software, and OS.  -->
