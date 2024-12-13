### Test Type Performed

Information cannot be navigated according to narrative or structure.

### Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, color bar, span (i.e, line), text, and arrows.

### Results Summary

Annotations do not follow a narrative structure that allows navigation or interaction into annotation elements for keyboard and SR modalities. All "navigation" takes users straight to the plot tools.

Ideally, keyboard-only users are "guided" through the important interactive pieces of annotations using just the TAB key. I would expect that TAB goes to the tools, then to interactive legend elements, and then into the chart space. From there, a keyboard-only user could experience the narrative at a granular level (across chart elements) via the tooltips, continuing to use TAB or (more ideally) now using arrow keys. Currently, there is no intelligent flow (largely due to lack of access overall, see Related Evidence.)

### Expected Behavior (Pass/Fail)

- _FAIL_ - Chart must provide a way to be navigated according to its data or narrative structure. The title, description, annotations, and then lower level data structures should be navigable and in that order.
  Chart data that contains sub-grouping (like a stacked bar chart) or nesting (like a tree map or hierarchy) must provide keyboard navigation that can navigate between levels and/or laterally across levels (in a non-linear fashion). Keyboard navigation must be comparable to the data structure (including cases where the data structure is novel) as well as provide linear or tabular navigation (like in a table or list).

### Image or Video of Failure

(Previous recordings show similar/related evidence)

````
  ```{video} ./assets/annotations_visual-only.mp4
  :width: 100%
  :playsinline:
  ```
````

A video shows a web browser with multiple charts. A screen reader navigates through the page and through multiple charts, but very limited information is given as they do so. The user (a sighted tester, in this case) navigates to the "Hover" tool on the toolbar and presses enter to interact with it, but this opens a link to a new webpage (fails).

### Steps to Reproduce

Using a screen reader, navigate as normal. Pass through all content related to the visualization and data: is there a meaningful story constructed? Is the data+information flowing from high-level to lower level? Are important interactive elements presented in order of their importance (IE filtering/searching/arranging first, then subfiltering/selecting/etc later)?

Using a keyboard-only, press TAB to begin navigating to the chart. Continue using TAB to experience the high-level interactive element order. TAB should only reveal interactive elements, but visually, there should be exposure to titles, subtitles, axes, legends, annotations, and more as TAB progresses. Note: these elements should simply be in sight but only receive keyboard focus if they are interactive.

Using a screen reader _or_ a keyboard: if granular chart elements provide additional context or information (to a sighted user, such as via a tooltip), then this should also be tested as part of the flow. This is usually one of the last things that should be exposed to users (after title, subtitle, axes, legends, annotations). Within chart navigation, higher level groupings in the data should be navigable before lower level children elements (if groupings exist in the data). Examples of this are lines -> line data points, stacks in a stacked bar -> stacked bars, clusters in a scatter -> individual points, color-encoded groups in chart -> elements within that encoding, etc. Sometimes these groupings can be nested under the axes or legends provided, when appropriate.

After or before chart-element navigation, it may be appropriate to also experience a data table.

### Guidelines and Standards Used

Information cannot be navigated according to narrative or structure [https://chartability.github.io/POUR-CAF/#**informationcannotbenavigatedaccordingtonarrativeorstructure**](https://chartability.github.io/POUR-CAF/#__informationcannotbenavigatedaccordingtonarrativeorstructure__)

### Related Evidence

See "Content is visual only," "Fragile support," "Tedious," and "Tab stops" evidence.

### Known or Documented Issues

See "Information cannot be navigated according to narrative or structure" from other test environments.

### Technical Details

- JAWS 2023.2402.1
- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

_Updated as of: October 22nd, 2024_

<!-- ### Notes
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels. -->
