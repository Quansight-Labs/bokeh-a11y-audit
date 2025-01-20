# Audit Summary

```{note}
This page is being developed.
```

This summary document serves 2 purposes and is organized into 2 major subheadings, below.

The first section focuses on providing an overview of problems and themes present in the evidence gathered from our audit of Bokeh's [plotting interface](https://bokeh-a11y-audit.readthedocs.io/plotting-interface/index.html), [plot tools](https://bokeh-a11y-audit.readthedocs.io/plot-tools/index.html), and [annotations](https://bokeh-a11y-audit.readthedocs.io/annotations/index.html) artifacts. These are our _findings_.

The second section focuses on suggestions for remediation based on the connectedness of various issues, prioritization of critical failures, and (in some cases) the ease of the fix involved. The remediation process should be negotiated and discussed broadly, broken into an actionable plan, and then enacted. My suggestions should not serve as an end to this discussion, but just a way to get it started.

## <a id="findings" href="#findings" aria-label="Findings"><span aria-hidden="true">#</span></a> Overview of findings: problems and themes

This section will break down the major themes related to problems or meta-issues as a result of our auditing evaluation. It is important to note that audits, when performed true to their intent, are about focusing on gathering evidence of failures, issues, gaps, or problems. Then that evidence serves as a basis for an analysis of systemic and interconnected issues across a system.

What separates an audit from the typical atomic or incremental approach used in open source software (aka "opening an issue") is that audits are a chance to systematically evaluate and analyze an entire ecosystem and synthesize all possible related problems at once. As an example, it is common to see an issue on an open source repo that asks for "alt text capabilities." While this might be great to add on, sometimes a library or tool needs several larger refactors or overhauls to really reach ideals/goals and uphold principles of good design. In order to do this (and even know what the larger issues are), having a procedure for taking a step back, finding the biggest gaps, and setting goalposts is vital. Consider the following subheadings as those big gaps.

### <a id="finding-1" href="#finding-1" aria-label="Finding 1"><span aria-hidden="true">#</span></a> 1. Finding: Lacks _foundational_ accessibility

I don't think this will come as a surprise to the Bokeh team, but it is quite clear that Bokeh has substantial gaps for basic text and interaction accessibility.

Providing alternative text will not be enough for Bokeh to become accessible, either. Textual design overall is lacking, which includes much more than alt text. And due to the complexity of interaction that Bokeh is capable of, significantly more work will need to be done to lay the groundwork for assistive technology and interactivity access.

Many, many tests failed because of this. Our 2 focus areas:

#### <a id="finding-1A" href="#finding-1A" aria-label="Finding 1A"><span aria-hidden="true">#</span></a> A. Has little textual accessibility

Across our tests, this was the most consistent finding and also the type of failure that intersects with the most evidence.

Both screen reader accessibility and cognitive accessibility require good text design, which means this is fundamental to include in order to support assistive technologies. Text should be a deeply embedded part of any interface but especially one that relies heavily on visuals, data, and complex interactivity.

Note that _only_ alt text (and aria-labels) are hidden visually. But overall, the accessibility of a textual experience that accompanies an analytical dashboard, visualization, or interface, is the cornerstone contributor to the overall accessibility of that artifact. Text accessibility is paramount.

Not only should screen readers be provided descriptions so that screen reader users can perceive _what_ content is (at both a high level through alt but also a low level via tables and elements with aria labels), but descriptions should be provided for _how_ to interact, _why_ things are the way they are, and more. Making these additional textual descriptions and experiences visually available has a broad impact on who gets included, how much work an interface is asking its users to do, and ultimately how successful the usability of that interface is. Better text makes for a better experience for everyone.

Busy executives can look at an interface and make faster decisions. Scientists can share their work more clearly and succinctly with their peers. Novices can learn more quickly. And of course, people with disabilities can be included.

Text design must consider all possible text in an interface and includes: titles, subtitles, captions, alt text on a visualization, aria labels on navigation elements, aria labels on interactive elements, semantics and aria roles are provided, tables of data, descriptions and help menus, and more.

This finding is primarily about the fact that a significant amount of text that should be present in the interface (and under the hood) simply isn't.

##### Evidence of this finding

<ul>
    <li>Elements are visual only [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visual-only.html" aria-label="Visual only evidence in plot tools" title="Visual only evidence in plot tools">1</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">2</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/visual-only.html" aria-label="Visual only evidence in annotations" title="Visual only evidence in annotations">3</a>].</li>
    <li>Only one modality/input is provided [].</li>
    <li>Metrics and variables are not defined [].</li>
    <li>Cannot be navigated according to narrative/structure [].</li>
    <li>Semantically invalid [].</li>
    <li>No title, summary, or caption provided [].</li>
    <li>Axis labels are not clear or present [].</li>
    <li>No table [].</li>
    <li>Visually apparent features are not described [].</li>
</ul>

##### Example

<p><i>Example taken from plotting interface [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">2</a>].</i> Below demonstrates that the lack of textual information excludes screen reader users from participation.</p>

```{video} ./plot-tools/assets/plotting-interface_visual-only.mp4
:width: 100%
:playsinline:
```

<p>A web browser is shown with multiple charts. A screen reader navigates through the page and through multiple charts, but very limited information is given as they do so (fails).</p>

#### <a id="finding-1B" href="#finding-1B" aria-label="Finding 1B"><span aria-hidden="true">#</span></a> B. Foundational navigation design and interactivity is poor

This particular issue tends to be the most difficult part of remediating a data visualization system like Bokeh, but also any interactive interface that has been built without using the correct building materials.

Most major assistive technologies _navigate_ content and in order to make this possible, the correct substrate must be in place. We generally divide navigational assistive technologies into two types: screen readers and "keyboard-only" types. Navigation must be possible with _both_ methods.

Screen readers that are used on desktop devices use a keyboard, so you might think that testing with a keyboard alone should be sufficient. But testing mobile screen reader access is necessary.

In addition, screen readers read _all_ content on a screen, one element at a time as well as have a plethora of navigational shortcuts available (navigation via headings, regions, tabbing, etc). An interface should first be tested with a screen reader: can everything be accessed? Check _literally everything_.

The basic navigation pattern of a screen reader _must_ be supported and includes: On a desktop, NVDA and JAWS navigate forward using <kbd aria-label="down arrow">↓</kbd> and backward <kbd aria-label="up arrow">↑</kbd>. VoiceOver and Narrator use a key shortcut plus <kbd aria-label="right arrow">→</kbd> to navigate forward <kbd aria-label="left arrow">←</kbd> to navigate backward (see [Deque's survival guide for more](https://dequeuniversity.com/screenreaders/survival-guide)).

But keyboard-only based assistive technologies (sip-and-puffs, single button switches, foot boards/switches, tongue switches, and of course _keyboards_ themselves) all rely on the "keyboard api" to get around. What matters for this type of navigation is primarily that interactive elements can be navigated to using <kbd aria-label="tab key">TAB</kbd>. This means that only elements that are meaningfully interactive should be tab-navigable, otherwise these technologies don't need to navigate to them.

However, in order for sighted users of screen readers and keyboard navigation technologies to know where they are at, a focus indicator must always be visible when `:focus` is detected on an element.

And of course: elements that are interactive with a mouse need more than just _navigation_ to be possible for assistive technologies, but assistive technologies need to be able to _interact_ with them as well. Buttons should be clickable, toggles toggleable, etc. And when an HTML `<div>` element is used in place of something like a `<button>`, then downstream navigation and interaction problems exacerbate quickly.

When elements are interactive and they can do something to some other part of a page or application (such as filtering a chart using the legend), then feedback needs to be provided to the user. We check for this in 2 ways: first, feedback must be programmatically provided for screen reader users (such as a valid state change using `aria-pressed` or equivalent on a semantically rich `<button>` element or via a console area that emits `aria-live` events). Secondly, sighted users need to be able to see the change with enough contrast difference between states. If something is highlighted or emphasized, that emphasis needs to be strong enough. If something is hidden, it needs to have already started with decent contrast before disappearing.

Lastly, providing basic navigational access can actually cause unintended accessibility barriers when not designed intentionally. An example of this is the too-common approach to make every element navigable in a visualization for screen reader users (see [Vega-Lite](https://github.com/vega/vega-lite/pull/6185) and Observable's [Plot](https://observablehq.com/plot/features/accessibility)). What ends up happening is that a scatterplot with 1000 elements would require a user to navigate forward 1000 times just to get through the chart. It is an immensely painful navigation experience for most users. It isn't just useless, but possibly a worse user experience than providing navigation in the first place. And, if `tabindex` is added to elements (for example, if they are interactive), then this tedious navigation problem also applies to keyboard-only assistive technology users too.

Smart navigational design then becomes much more complex: how do you prepare a visualization, especially an interactive one, to progressively show or hide sets and subsets of elements at a time? How do you allow users to search, filter, and sort elements for faster navigation?

Testing for _intelligent_ navigation wasn't even possible, since even basic navigation wasn't provided.

##### Evidence of this finding

<ul>
    <li>Only one modality/input is provided [].</li>
    <li>Cannot be navigated according to narrative/structure [].</li>
    <li>Semantically invalid [].</li>
    <li>Focus indicator not perceivable [].</li>
    <li>Single process [].</li>
    <li>Fragile support [].</li>
    <li>Controls inappropriate [].</li>
    <li>Tab stops inappropriate [].</li>
    <li>Navigation is tedious [].</li>
    <li>Interactive context is not clear [].</li>
    <li>Complex actions have alternatives [].</li>
    <li>Low contrast for interactive elements [].</li>
</ul>

##### Example

<p><i>Example taken from plot tools [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">1</a>].</i> Below demonstrates a screen reader user's frustrating and confusing interaction experience.</p>

```{video} ./plot-tools/assets/plot-tools_visual-only.mp4
:width: 100%
:playsinline:
```

<p>A color scatter plot is shown. A screen reader focus indicator moves across the plot tool icons, but when a tool is selected it opens a previously visited link instead of toggling the tool that corresponds to the visual focus indication (fails).</p>

### <a id="finding-2" href="#finding-2" aria-label="Finding 2"><span aria-hidden="true">#</span></a> 2. Finding: Perceivability and understandability have barriers

Understandability (and cognitive support) can be a difficult thing to ask a visualization library/tool to provide. It is _always_ ultimately the responsibility of the implementer of a tool to provide end users with cognitive access. The application and use of a library (E.g. the contexts where Bokeh is used) should explain, describe, make outcomes easy, and provide robust alternative ways to reach those outcomes.

However, there are some cognitive support areas that a visualization library _should_ be responsible for. And of course, there are many things that a visualization library can assist developer-users and designer-users with. Below we are focusing on issues that either fall under the purview of Bokeh or are things that Bokeh can do to assist their users with.

As for perceivability (perceptual accessibility), ultimately being able to find things intersects strongly with cognitive issues. If users can't perceive elements (whether they are buried/hidden, left out, or hard to perceive), then they will have to mentally fill gaps, perform additional labor, or might even be excluded from using the interface altogether.

#### <a id="finding-2A" href="#finding-2A" aria-label="Finding 2A"><span aria-hidden="true">#</span></a> A. Findability and perceivability has problems

Users need to be able to find things. _Perception_ and _discovery_ should be easy tasks. And unfortunately, there are some elements that are essentially invisible or hidden in our testing environment. Hard-to-see and hard-to-find elements can add difficulty or even make certain things impossible about Bokeh's usage.

For screen reader users, semantic labels need to exist for interactive elements so that they know what a particular button or input does and its current state. And without proper labels on elements, they are virtually invisible to screen reader users.

For low vision users, high contrast is paramount. Contrast is the difference or "discriminability" between two things. High contrast means that things can easily be distinguished or discriminated from one another. In accessibility, we test the color of foreground elements against the color of adjacent elements and background elements. Color contrast must be high enough on anything that is meaningful, provide information, helps the user understand what something is, and is capable of performing some sort of interaction. In particular, contrast must be especially strong and well-designed on interactive elements. Elements that display a change of state (from off to on) need to be perceivable in the "off" state if it is still interactive. And elements with a change of state need to have a minimum contrast between the previous state and new state after interaction.

For sighted mouse users with motor and dexterity impairents, tooltips can be helpful on chart elements but the target size of elements (such as in the line chart) are far too small. Discovering that tooltips exist on an element using pixel-perfect strategies actually creates accessibility barriers for all kinds of folks (but especially those with dexterity disabilities such as tremors or upper-body motor impairments). Being honest, I didn't even notice the line chart had tooltips enabled until I found them by accident testing for contrast

##### Evidence of this finding

<ul>
    <li>Visual only [].</li>
    <li>Semantically invalid [].</li>
    <li>Color contrast [].</li>
    <li>Contrast of interactive elements [].</li>
    <li>Target pointer size is too small [].</li>
    <li>Interaction is tedious [].</li>
    <li>Data density [].</li>
    <li>Spacing [].</li>
    <li>Keyboard focus indicator is missing, obscured, or low contrast [].</li>
</ul>

##### Example

<p><i>Example taken from annotations [<a href="" aria-label="Contrast evidence in annotation" title="Contrast evidence in annotation">23</a>].</i> Below demonstrates the near-invisibility of the interactive annotation element used to toggle a line chart on and off.</p>

```{figure} ./annotations/assets/annotations_contrast_1.png
:width: 100%
:alt: A double line chart is shown. A color selection dropper is highlighting a selected 'muted', grayed out line. The contrast checking score of 1.27 is shown on the bottom left corner (fails).

A double line chart is shown. A color selection dropper is highlighting a selected 'muted', grayed out line. The contrast checking score of 1.27 is shown on the bottom left corner (fails).
```

#### <a id="finding-2B" href="#finding-2B" aria-label="Finding 2B"><span aria-hidden="true">#</span></a> B. Understanding is not easy

In general, everything should be easy to understand for folks who have never before encountered a Bokeh chart, its interactive capabilities, and its annotations.

_What_ a chart shows should be described. _Why_ some information has been visualized should be explained. _How_ a user can interact should be clearly explained, including with instructions provided for more complex interactions (like lasso, etc). All text and labels should be made legible and presented at a reasonable reading level.

Bokeh's cognitive support overall seems to be geared toward supporting software developers who are using the library while generally leaving end-user understandability up to the user's own ability to poke around with interactivity, grok context/use, and self-interpret.

In general, Bokeh doesn't appear to provide _any_ assistance to developers in authoring textual descriptions, providing end-user oriented instructions/explanations, and also appears to have minimal support for automatically simplifying/formatting data-oriented numerical values (such as using too many decimal points of precision in a label).

Also, Bokeh is a library grounded on _interaction_ with data and data visualizations. One important area of cognitive accessibility to consider is that there are many valid ways to interact with data. But by providing only one narrow path to reach a particular piece of information or outcome is a cognitive accessibility barrier as it assumes that users will always understand, remember, and correctly execute that given path of interaction.

##### Evidence of this finding

<ul>
    <li>No title, summary, or caption provided [].</li>
    <li>Explanation or purpose [].</li>
    <li>No table [].</li>
    <li>Visually apparent features are not described [].</li>
    <li>No interaction cues or instructions [].</li>
    <li>Not human-readable [].</li>
    <li>Narrative or structure [].</li>
    <li>Only one modality/input is provided [].</li>
    <li>Single process [].</li>
    <li>Complex actions have no alternatives [].</li>
    <li>Information complexity [].</li>
</ul>

##### Example

<p><i>Example taken from plot tools [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">1</a>].</i> Below demonstrates a screen reader user's frustrating and confusing interaction experience.</p>

```{figure} ./assets/plotting-interface_information-complexity_1.png
:width: 100%
:alt: A scatter plot is shown. In the chart's upper tab, 'All Species' is selected. Three categories are shown, but are hard to differentiate from one another based on their color and patterns.

A scatter plot is shown. Three categories are shown, but are hard to differentiate from one another based on their color and patterns.
```

#### <a id="finding-2C" href="#finding-2C" aria-label="Finding 2C"><span aria-hidden="true">#</span></a> C. Interactive capabilities and system state are not clear

Interactive data visualization comes with an additional layer of cognitive accessibility issues: keeping track of what could happen, is happening, and has happened in a system.

Initially, users will need to know what interactions are possible. Without cues that invite/demonstrate interaction or easily discoverable instructions, users will likely not even use the interactive features of a visualization.

Additionally, when change takes place in a system, it should be easy to both anticipate or know the context of what will change as well as follow the change as it happens. During interaction, users should have a clear sense of where change takes place if it isn't in the same location where their focus currently is (this applies to sighted as well as blind users). In addition, once change takes place, it should be clear that the action has taken place and completed. Systems must provide rich, multimodal channels of feedback in response to user input.

Lastly, after change has taken place, users should be able to easily undo their actions, know their current location within an interaction process, have a sense of their interaction history, and be able to share and reproduce the current state of their interactive work. Presently, the general design pattern assumes that users will come to a visualization, interact, and then if they leave the page or wish to share their work with someone else, the work must be completely reconstructed from scratch.

Again, as mentioned previously in this audit summary: it is difficult to expect a visualization library to handle _everything_ that would make an interactive application experience more accessible. The burden of higher-level system accessibility (such as history, sharing, reproducibility, saving, loading, etc) often falls to systems that implement interactive charts. However, the fact that Bokeh fails should be noted as an area of potential improvement. Systems and utilities could be in place to facilitate these functionalities more easily.

##### Evidence of this finding

<ul>
    <li>No explanation or purpose for how to read [].</li>
    <li>No interaction cues or instructions [].</li>
    <li>Changes are easy to follow [].</li>
    <li>Interactive context is not clear [].</li>
    <li>Interactions are not forgivable [].</li>
    <li>State is not easy to share or reproduce [].</li>
    <li>Location and history is not clear [].</li>
</ul>

##### Example

<p><i>Example taken from plot tools [<a href="https://bokeh-a11y-audit.readthedocs.io/annotations/share-reproduce.html" aria-label="Share and reproduce evidence in plot tools" title="Share and reproduce evidence in plot tools">1</a>].</i> Below demonstrates how a screen reader user interacts with an input and then loses their location and focus, in addition to receiving no system feedback about their original input.</p>

```{video} ./plot-tools/assets/plot-tools_changes-easy-to-follow.mp4
:width: 100%
:playsinline:
```

<p>A scatter plot is shown. A screen reader is navigating through the chart's dropdown menu, but when an option is selected, the user is forced back to the top of the webpage.</p>

### <a id="finding-3" href="#finding-3" aria-label="Finding 3"><span aria-hidden="true">#</span></a> 3. Finding: System is fragile

This part in an audit can be difficult because it can feel like asking a distinct tool like a hammer to be transformed into a rocket ship. This part of an audit is when the shortcomings of older, smaller, or just-emerging technologies come to light. Systems, especially ones that are tools, can often be built as a response to the needs of a specific community. Bokeh, in that sense, emerged to provide a better way to visualize data in Python for a web context. But the community that uses and consumes Bokeh is broader than the underlying system was originally designed for.

Tools and systems should not be fragile. They should be able to withstand different environments, used by different people in different ways, and allow for end-user personalization, customization, and adaptation.

Systems engineering is always held in tension: good engineering is built to do specific tasks very effectively for years and years. But at the same time, user needs and behaviors, contexts of use, and surrounding technologies all change over time. So good systems engineering does at times require revisiting, updating, and maintenance.

That being said, Bokeh has catching up to do.

#### <a id="finding-3A" href="#finding-3A" aria-label="Finding 3A"><span aria-hidden="true">#</span></a> A. System's capabilities are not robust

Sometimes a system is built using the wrong materials or with the wrong substrate, which ultimately limits how robust that system is. In this case, Bokeh uses non-standard interactive elements, such as `<div>`s and also does not provide adequate descriptions and attributes on elements that enable assistive technologies. This limits which devices are capable of interaction and input, as well as which ways a user is able to perceive the contents of that system.

But more than using the correct materials, sometimes systems should also be encouraged to grow in order to handle new devices, interaction patterns, and uses. And in this sense, Bokeh does not handle zoom/reflow well, which is difficult especially for mobile users. Many users who have disabilities actually use mobile or tablet devices _more_ than desktop devices. Some screen reader users, for example, love VoiceOver on iOS much more than a desktop experience.

Bokeh should be built in a way that enables a myriad of current technologies to interact with it. In particular, what makes Bokeh awesome are the interactive capabilities that it offers end users. But care should be taken to design how different users with different assistive technologies and input devices and interaction patterns will want to accomplish similar goals. Pairity in the quality of experience should be provided for all users. Sighted, mouse users shouldn't not have an easier and better time than everyone else.

##### Evidence of this finding

<ul>
    <li>Content is visual only [].</li>
    <li>Semantically invalid [].</li>
    <li>Fragile support [].</li>
    <li>Only one modality/input is provided [].</li>
    <li>Zoom and reflow are not supported [].</li>
    <li>Scrolling experiences cannot be altered [].</li>
    <li>Complex interactions have no alternatives [].</li>
    <li>Interactive context is not clear [].</li>
    <li>Interactions are not forgivable [].</li>
    <li>State is not easy to share or reproduce [].</li>
    <li>Location and history is not clear [].</li>
    <li>Keyboard focus indicator is missing, obscured, or low contrast [].</li>
</ul>

##### Example
<p><i>Example taken from plotting interface [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/zoom-reflow.html" aria-label="Zoom and reflow evidence in plotting interface" title="Zoom and reflow evidence in plotting interface">1</a>].</i> Below demonstrates how a high-zoom user will have a worse experience reading Bokeh's text than someone who uses Bokeh at 100% zoom. Because Bokeh renders with canvas, text becomes rasterized and does not scale well compared to HTML or SVG elements when zoomed.</p>

```{figure} ./assets/plotting-interface_zoom-reflow_6.png
:width: 100%
:alt: Viewport is zoomed in to 400% showing the canvas-based text from the bar chart labels being highly aliased and fuzzy, compared to the text for the Scatter plot beneath (circled in red) which is high fidelity and readable (fails).

Viewport is zoomed in to 400% showing the canvas-based text from the bar chart labels being highly aliased and fuzzy, compared to the text for the Scatter plot beneath (circled in red) which is high fidelity and readable (fails).
```

#### <a id="finding-3B" href="#finding-3B" aria-label="Finding 3B"><span aria-hidden="true">#</span></a> B. System's presentation is not flexible
Many users, especially those with disabilities, customize their technology experiences. This is called "fitting" in some spaces, but generally is part of "personalization" and "customization." In order for an end user to be able to make these changes to an interface, it must be built on a relatively flexible system. Rigid systems will try to enforce their own rules for syling, animation and more. But flexible systems are built with an assumption that end users may override things.

There is a massive array of different things that end users might want to be able to do and building a system that could allow them to do whatever they wanted might be impossible. However, there are a few things that should *always* work as-expected out of the box, which we check for: detecting and adapting to changes in system-set high contrast mode, if textures/patterns are on can they be turned off, whether animations can be disabled, zoom/reflow support, ability to adjust scrolling experiences, whether obscure chart types have alternatives for viewing the same data, and whether text can be manipulated using css.

Foundationally, many users leverage browser extensions that automatically try to update every webpage they visit to suit their preferred minimum font size, text spacing, color choices, and more. A library's inability to respond to simple CSS-based changes can produce pretty harsh barriers for some end users (and also can look clunky too). Responding to an end-user's personal CSS as-expected is easily the most important first thing we check. Then we test different devices and assistive tech (mobile devices, magnifiers). After that, we work through system settings (contrast, animations, textures, etc) and lastly we check certain visualization-specific things.

Ideally, all content on the web is flexible enough to handle these variations that facilitate an end-user's "fit."

##### Evidence of this finding

<ul>
    <li>User's style changes are not respected [].</li>
    <li>Contrast and texture cannot be adjusted [].</li>
    <li>User's text adjustments are not respected [].</li>
    <li>Zoom and reflow are not supported [].</li>
    <li>Scrolling experiences cannot be altered [].</li>
    <li>Complex interactions have no alternatives [].</li>
</ul>

##### Example
<p><i>Example taken from plotting interface [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/contrast-texture-adjustments.html" aria-label="Contrast and texture evidence in plotting interface" title="Contrast and texture evidence in plotting interface">1</a>].</i> Below demonstrates how an inflexible visualization is incapable of correctly responding to an operating system's *High Contrast* mode.</p>

```{figure} ./assets/plotting-interface_style-change-respected.png
:width: 100%
:alt: A scatter plot is shown. A high contrast filter has been implemented, and the web browser background is black with white font. However, the chart space retains it's default color scheme - the contrast change was not applied (fails).

A scatter plot is shown. A high contrast filter has been implemented, and the web browser background is black with white font. However, the chart space retains it's default color scheme - the contrast change was not applied (fails).
```

## <a id="suggestions" href="#suggestions" aria-label="Suggestions"><span aria-hidden="true">#</span></a> Suggested directions for remediation

```{note}
Explanation pending.
```

### Focus on text experiences: explanations, descriptions, and labels

```{note}
Explanation pending.
```

### Use better building materials

```{note}
Explanation pending.
```

### Support assistive technology interaction

```{note}
Explanation pending.
```

### Build a flexible system

In [my latest research on what I call "softerware,"]() I actually explored what the future of accessibility customization could look like for data visualizations.

```{note}
Explanation pending.
```

### Help developers succeed

Whenever possible, the library should be designed to assume that software-users are not the end users, but rather building interfaces for users who are not necessarily skilled at visualizing and interacting with data.

utilities, validation, smart defaults, and guardrails

```{note}
Explanation pending.
```

### Add end-user documentation and guides

```{note}
Explanation pending.
```
