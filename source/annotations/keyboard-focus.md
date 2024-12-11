### Test Type Performed

Keyboard focus indicator.

### Artifact Evaluated

[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, color bar, span (i.e, line), text, and arrows.

### Results Summary

Annotations fail for providing focus indicators on interactable elements, which is related to other technical limitations. Since the interactive legend is a div and can be interacted with like a button there should be a keyboard indicator. However, in the chart's current state this can't happen. 

### Expected Behavior (Pass/Fail)

- _FAIL_ - Visual keyboard focus indication must be present and easy to see. Focus indicator must have 4.5:1 contrast against background, must not be fully obscured, and must have at least a 2px border.

### Image or Video of Failure
From 00:00-00:05s, a double line chart is shown. A user moves their cursor over an interactive legend and presses each label like a button. This toggles each line "on/off", respectively. 
From 00:05-00:18s
The user changes to keyboard-only interactions. They use TAB to navigate to the correct chart, then continue to press TAB to try and access the interactive. They cannot.

````
  ```{video} ./assets/annotations_keyboard-focus.mp4
  :width: 100%
  :playsinline:
  ```
````

### Steps to Reproduce

Navigate elements using a keyboard only (no screen reader or other assistive tech). A focus indicator should be visibly present based on the keyboard's current focus location.

### Guidelines and Standards Used

Keyboard focus indicator missing, obscured, or low contrast [https://chartability.github.io/POUR-CAF/#**keyboardfocusindicatormissingobscuredorlowcontrast**](https://chartability.github.io/POUR-CAF/#__keyboardfocusindicatormissingobscuredorlowcontrast__)

### Related Evidence

See "Fragile support," "Low interactive contrast," and "Cues and instructions."

### Known or Documented Issues

See "Plot tools: Keyboard focus indicator" evidence.

### Technical Details

- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

*Updated as of: October 22nd, 2024*

<!-- ### Notes

As of right now, Chartability requires 4.5:1 but we're using the more-lenient WCAG 2.2 3:1 requirements instead (Chartability will use this in the future anyway). -->

<!-- A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.  -->
