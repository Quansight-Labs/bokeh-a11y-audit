### Test Type Performed
Interaction modality only has one input type.

### Artifact Evaluated
[Plotting interface](https://docs.bokeh.org/en/latest/docs/user_guide/basic.html#ug-basic). Specifically, evaluating the interfaces for all [charts](https://quansight-labs.github.io/bokeh-a11y-audit/#_ts1723552414769) in our test environment: line, bar, table and scatter plot.

### Results Summary
Plotting interface does not directly interact with the chart unless plot tools are used, and even then users cannot actively navigate any "data points" or bars in some charts. The line plot with two lines has mouse-over tooltips for data points, but they are not accessible in any other way. The scatter plot tab categories are interactable, but not consistently. For now we'll talk about this. 

The tabs can be navigated to in multiple modalities, but interaction is limited or does not work as expected. Keyboard-only users cannot select the tab categories. SR users can select the tabs but are then redirected to the top of the webpage versus being able to navigate further into the chart.

### Expected Behavior (Pass/Fail)
- *FAIL* - We would expect interactive elements to be comparably usable between mouse, keyboard, and screen reader devices. All tools and tool options should be easily accessed.

### Image or Video of Failure 
First video: Mouse then Keyboard-only input. From 00:09-00:08s, the user the mouse to hover over data points in the second line chart. 
From 00:12-00:28s, the tester TABs to navigate to the chart. Once there, they continue to press TAB to try and navigate into the chart with no success. Eventually they must SHIFT+TAB to move backwards to return to the correct chart testing area.
<video controls src="plotting-interface_modality_1.mp4" title="Modality-input-type_Keyboard"></video>

Second video: JAWS screen reader input. From 00:09-00:19s, the SR navigates to the line chart with two lines by using TAB, then continues to try and access the data points. When they press SPACE or ENTER, they are taken to a visited link rather than being able to interact with the chart.  
<video controls src="../assets/plotting-interface_modality_2.mp4" title="Modalit-input-type_SR-1"></video>

Third video: JAWS screen reader input. From 00:04-00:19s, the SR navigates to the scatter plot by using TAB, then continues to try and access the "Selected Species" chart tab. When they press ENTER, the UI changes to show the updated species selected dropdown, but the SR cannot access this by pressing TAB or down arrow. They are instead taken to the website's toolbar. 
<video controls src="../assets/plotting-interface_modality_3.mp4" title="Modality-input-type_SR-2"></video>

### Steps to Reproduce
Keyboard: Using TAB, navigate to the line chart. Continue to press TAB to explore the chart, and SPACE or ENTER to attempt to interact.

JAWS screen reader: Using TAB, navigate to the line chart and then the scatter plot. Continue to press TAB to bring you to the "Selected Species" tabs.

### Guidelines and Standards Used
Interaction modality only has one input type (critical) [https://chartability.github.io/POUR-CAF/#__interactionmodalityonlyhasoneinputtype___critical_](https://chartability.github.io/POUR-CAF/#__interactionmodalityonlyhasoneinputtype___critical_)

### Related Evidence
See "Plot tools: Interaction modality only has one input type" evidence. 

### Known or Documented Issues
See "Plot tools: Interaction modality only has one input type" evidence. 

### Technical Details
- Chrome Version 129.0.6668.59 (64-bit)
- JAWS 2023.2402.1
- Windows 11 Build 22631.3958

*Updated as of: September 18th, 2024*

<!-- ### Notes
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.  -->
