### Test Type Performed
Information complexity is appropriate.

### Artifact Evaluated
[Annotations](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html): which include titles, axes labels, legends and their labels, color bar, span (i.e, line), text, and arrows.

### Results Summary
Annotations pass for information complexity and understandability with their intended purposes. 

### Expected Behavior (Pass/Fail)
- *Pass* - Information complexity must be appropriate to the task or goal of the visual. Often, this is an issue when charts have too many different kinds of information encoded (note that this isn't the same as density). Chart must not have more than one Y or X axis without first presenting two charts separately. Chart must not encode along a third spatial dimension (z axis) unless the data itself is 3D (spatial, modeling, etc). Chart should not contain more than 5 data categories.

<!-- ### Image or Video of Failure 
Figure 1
<figure>
    <img width="803" alt="A scatter plot is shown. In the chart's upper tab, 'All Species' is selected. Three categories are shown, but are hard to differentiate from one another based on their color and patterns." src="./assets/plotting-interface_information-complexity_1.png">
    <figcaption>A scatter plot is shown. Three categories are shown, but are hard to differentiate from one another based on their color and patterns.</figcaption>
</figure> -->

<!-- ### Steps to Reproduce
For Scatter:
Using the scatter plot's tab setting, first view the chart in default view. Next, go to the "Selected Species" tab and choose a drop-down option.

Examine all charts:
- Check that each important piece of information can be easily and accurately discerned from one another
- check that groupings, categories, trends, and patterns can be discerned and interpreted easily
- Check whether any complexity can be reduced without loss of accessibility or understanding (think of this as "complexity-to-ink ratio" in a similar way as Tufte's data-to-ink ratio) -->

### Guidelines and Standards Used
Information complexity is inappropriate [https://chartability.github.io/POUR-CAF/#__informationcomplexityisinappropriate__](https://chartability.github.io/POUR-CAF/#__informationcomplexityisinappropriate__)

<!-- ### Related Evidence
See "Spacing is inapproriate" evidence.  -->

<!-- ### Known or Documented Issues
(If there is already a github issue created for this test or a related test, it will be listed here.) -->

### Technical Details
- Chrome Version 130.0.6723.59 (64-bit)
- Windows 11 Build 22631.4317

*Updated as of: October 22nd, 2024*

<!-- ### Notes
A seasoned SR (screen reader) user could have the knowledge to navigate and explore webpages and graphs with more nuance, whether through manual mode switching, certain key shortcuts, etc. These tests are done by a sighted user with the SR’s default options and performed as if a new or beginner user is interacting with these elements. We would expect that all users could be able to navigate smoothly, regardless of experience levels.  -->
