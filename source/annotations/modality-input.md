### Test Type Performed
Interaction modality only has one input type.

### Artifact Evaluated
[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, color bar, span (i.e, line), text, and arrows.

### Results Summary
Annotations (that have applicable interactions) fail for comparable access in multiple modalities. Currently, most of the annotations are interactive either visually or with a mouse. Elements with touch capabilities have limiting factors.

Titles: Visual only.

Axes labels: Visual only.

Labels: Visual only.

Legends: Visual, mouse-click, and touch.

Color bar: Visual only.

Span: Visual only.

Arrow: Visual only.

Hover tooltip: Visual and touch. (See Notes section below).

### Expected Behavior (Pass/Fail)
- *FAIL* - We would expect interactive or important elements to be comparably usable between mouse, keyboard, touch screen, and screen reader devices. 

### Image or Video of Failure 
First video: Mouse-only input. 
A user tester navigates the second line chart and then selects the interactive legend to toggle the categories on and off. They then hover over the filled and dashed chart lines to show the hover tool tip.
````
  ```{video} ./assets/annotations_modality-input_mouse.mp4
  :width: 100%
  :playsinline:
  ```
````  

Second video: Keyboard-only input.
The tester uses TAB to navigate to the second line chart. Once there, they continue to press TAB to try and navigate to the interactive legend with no success. They also cannot navigate to the chart to use the "hover" tool. Eventually they TAB too far and must SHIFT+TAB to move backwards to return to the correct chart area.
````
  ```{video} ./assets/annotations_modality-input_keyboard.mp4
  :width: 100%
  :playsinline:
  ```
````

Third video: JAWS screen reader input. 
A sighted tester navigates to the chart area using TAB, but there is no audible information given on where the user is at. All JAWS says is, "Visited link." The title, which visually is the first signifier of the chart space, is not read. The tester continues to press TAB to navigate with "visited link" continually being repeated, and them not being able to interact with the chart space. 
````
  ```{video} ./assets/annotations_visual-only.mp4
  :width: 100%
  :playsinline:
  ```
````

Fourth video: Mobile phone (touch screen).
From the default mobile browser view, the tester navigates the second line chart. They then touch select (shown with a green circle and blue border) the interactive legend to toggle the categories on and off. Next, they pinch to zoom in on the page to get a closer view of the chart. The tester runs their finger along the filled line to try and view the hover tool tip. While it does show at times, the user cannot consistently get it to show. They repeat the process with the dashed line on the chart. 
````
  ```{video} ./assets/annotations_modality-input.mp4
  :width: 100%
  :playsinline:
  ```
````

### Steps to Reproduce
Keyboard: Using TAB, navigate to the double line chart. Continue to press TAB to explore the chart, and SPACE or ENTER to attempt to interact.

JAWS screen reader: Using TAB, navigate to the double line chart. Press SPACE or ENTER to attempt to interact.

Touch screen device: Using your finger on a touch screen or using a touch screen simulator, interact with the double line chart. Select and deselect legend options and place your finger along the chart lines to use the hover tooltip.

### Guidelines and Standards Used
Interaction modality only has one input type (critical) [https://chartability.github.io/POUR-CAF/#__interactionmodalityonlyhasoneinputtype___critical_](https://chartability.github.io/POUR-CAF/#__interactionmodalityonlyhasoneinputtype___critical_)

### Related Evidence
See "Fragile support," "Target pointer interaction size is too small," "Semantically invalid," and "Zoom and reflow are not supported" evidence forms for more information for touch screens, specifically.

### Known or Documented Issues
See "Plot tools: Interaction modality only has one input type" evidence. 

### Technical Details
- Mobile phone
- JAWS 2023.2402.1
- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

*Updated as of: October 22nd, 2024*

### Notes
The double line chart technically does work with touch screens, but the target sizes to touch the points on each line is incredibly hard to do and to replicate. This is something that relies heavily on the target pointer interaction sizing and reflow working correctly. 