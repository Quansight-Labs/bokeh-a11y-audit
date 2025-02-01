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
    <li>Elements are visual only [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visual-only.html" aria-label="Visual only evidence in plot tools" title="Visual only evidence in plot tools">PT-18</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">PI-28</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/visual-only.html" aria-label="Visual only evidence in annotations" title="Visual only evidence in annotations">A-24</a>].</li>
    <li>Only one modality/input is provided [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/modality-input.html" aria-label="Modality Input evidence in plot tools" title="Modality Input evidence in plot tools">PT-13</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/modality-input.html" aria-label="Modality Input evidence in plotting interface" title="Modality Input evidence in plotting interface">PI-17</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/modality-input.html" aria-label="Modality Input evidence in annotations" title="Modality Input evidence in annotations">A-13</a>].</li>
    <li>Metrics and variables are not defined [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/metrics-variables.html" aria-label="Metrics Variables evidence in plotting interface" title="Metrics Variables evidence in plotting interface">PI-16</a>].</li>
    <li>Cannot be navigated according to narrative/structure [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/narrative-structure.html" aria-label="Narrative Structure evidence in plotting interface" title="Narrative Structure evidence in plotting interface">PI-18</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/narrative-structure.html" aria-label="Narrative Structure evidence in annotations" title="Narrative Structure evidence in annotations">A-14</a>].</li>
    <li>Semantically invalid [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/semantically-invalid.html" aria-label="Semantically Invalid evidence in plot tools" title="Semantically Invalid evidence in plot tools">PT-14</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/semantically-invalid.html" aria-label="Semantically Invalid evidence in plotting interface" title="Semantically Invalid evidence in plotting interface">PI-20</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/semantically-invalid.html" aria-label="Semantically Invalid evidence in annotations" title="Semantically Invalid evidence in annotations">A-15</a>].</li>
    <li>No title, summary, or caption provided [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/title-summary.html" aria-label="Title Summary evidence in plotting interface" title="Title Summary evidence in plotting interface">PI-27</a>].</li>
    <li>Axis labels are not clear or present [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/axis-labels.html" aria-label="Axis Labels evidence in plotting interface" title="Axis Labels evidence in plotting interface">PI-1</a>].</li>
    <li>No table [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/no-table.html" aria-label="No Table evidence in plotting interface" title="No Table evidence in plotting interface">PI-23</a>].</li>
    <li>Visually apparent features are not described [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visually-apparent-features.html" aria-label="Visually Apparent Features evidence in plot tools" title="Visually Apparent Features evidence in plot tools">PT-19</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/visually-apparent-features.html" aria-label="Visually Apparent Features evidence in plotting interface" title="Visually Apparent Features evidence in plotting interface">PI-29</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/visually-apparent-features.html" aria-label="Visually Apparent Features evidence in annotations" title="Visually Apparent Features evidence in annotations">A-25</a>].</li>
</ul>

##### Example

<p><i>Example taken from plotting interface [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">2</a>].</i> Below demonstrates that the lack of textual information excludes screen reader users from participation.</p>

```{video} ./plotting-interface/assets/plotting-interface_visual-only.mp4
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
    <li>Only one modality/input is provided [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/modality-input.html" aria-label="Modality Input evidence in plot tools" title="Modality Input evidence in plot tools">PT-13</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/modality-input.html" aria-label="Modality Input evidence in plotting interface" title="Modality Input evidence in plotting interface">PI-17</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/modality-input.html" aria-label="Modality Input evidence in annotations" title="Modality Input evidence in annotations">A-13</a>].</li>
    <li>Cannot be navigated according to narrative/structure [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/narrative-structure.html" aria-label="Narrative Structure evidence in plotting interface" title="Narrative Structure evidence in plotting interface">PI-18</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/narrative-structure.html" aria-label="Narrative Structure evidence in annotations" title="Narrative Structure evidence in annotations">A-14</a>].</li>
    <li>Semantically invalid [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/semantically-invalid.html" aria-label="Semantically Invalid evidence in plot tools" title="Semantically Invalid evidence in plot tools">PT-14</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/semantically-invalid.html" aria-label="Semantically Invalid evidence in plotting interface" title="Semantically Invalid evidence in plotting interface">PI-20</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/semantically-invalid.html" aria-label="Semantically Invalid evidence in annotations" title="Semantically Invalid evidence in annotations">A-15</a>].</li>
    <li>Focus indicator not perceivable [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/keyboard-focus.html" aria-label="Keyboard Focus evidence in plot tools" title="Keyboard Focus evidence in plot tools">PT-11</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/keyboard-focus.html" aria-label="Keyboard Focus evidence in plotting interface" title="Keyboard Focus evidence in plotting interface">PI-13</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/keyboard-focus.html" aria-label="Keyboard Focus evidence in annotations" title="Keyboard Focus evidence in annotations">A-11</a>].</li>
    <li>Single process [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/single-process.html" aria-label="Single Process evidence in plotting interface" title="Single Process evidence in plotting interface">PI-21</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/single-process.html" aria-label="Single Process evidence in annotations" title="Single Process evidence in annotations">A-17</a>].</li>
    <li>Fragile support [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/fragile-support.html" aria-label="Fragile Support evidence in plotting interface" title="Fragile Support evidence in plotting interface">PI-10</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/fragile-support.html" aria-label="Fragile Support evidence in annotations" title="Fragile Support evidence in annotations">A-7</a>].</li>
    <li>Controls inappropriate [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/controls-inappropriate.html" aria-label="Controls Inappropriate evidence in plot tools" title="Controls Inappropriate evidence in plot tools">PT-6</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/controls-inappropriate.html" aria-label="Controls Inappropriate evidence in plotting interface" title="Controls Inappropriate evidence in plotting interface">PI-6</a>].</li>
    <li>Tab stops inappropriate [<a href="https://bokeh-a11y-audit.readthedocs.io/annotations/tab-stops.html" aria-label="Tab Stops evidence in annotations" title="Tab Stops evidence in annotations">A-20</a>].</li>
    <li>Interaction is tedious [<a href="https://bokeh-a11y-audit.readthedocs.io/annotations/tedious.html" aria-label="Tedious evidence in annotations" title="Tedious evidence in annotations">A-22</a>].</li>
    <li>Interactive context is not clear [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/interactive-context.html" aria-label="Interactive Context evidence in plot tools" title="Interactive Context evidence in plot tools">PT-10</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/interactive-context.html" aria-label="Interactive Context evidence in annotations" title="Interactive Context evidence in annotations">A-10</a>].</li>
    <li>Complex actions have alternatives [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/complex-actions.html" aria-label="Complex Actions evidence in plot tools" title="Complex Actions evidence in plot tools">PT-2</a>].</li>
    <li>Low contrast for interactive elements [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/contrast-interactive-elements.html" aria-label="Contrast Interactive Elements evidence in plot tools" title="Contrast Interactive Elements evidence in plot tools">PT-4</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/contrast-interactive-elements.html" aria-label="Contrast Interactive Elements evidence in plotting interface" title="Contrast Interactive Elements evidence in plotting interface">PI-4</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/contrast-interactive-elements.html" aria-label="Contrast Interactive Elements evidence in annotations" title="Contrast Interactive Elements evidence in annotations">A-3</a>].</li>
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
    <li>Elements are visual only [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visual-only.html" aria-label="Visual only evidence in plot tools" title="Visual only evidence in plot tools">PT-18</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">PI-28</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/visual-only.html" aria-label="Visual only evidence in annotations" title="Visual only evidence in annotations">A-24</a>].</li>
    <li>Semantically invalid [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/semantically-invalid.html" aria-label="Semantically Invalid evidence in plot tools" title="Semantically Invalid evidence in plot tools">PT-14</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/semantically-invalid.html" aria-label="Semantically Invalid evidence in plotting interface" title="Semantically Invalid evidence in plotting interface">PI-20</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/semantically-invalid.html" aria-label="Semantically Invalid evidence in annotations" title="Semantically Invalid evidence in annotations">A-15</a>].</li>
    <li>Color contrast [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/contrast.html" aria-label="Color Contrast evidence in plot tools" title="Color Contrast evidence in plot tools">PT-3</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/contrast.html" aria-label="Color Contrast evidence in plotting interface" title="Color Contrast evidence in plotting interface">PI-3</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/contrast.html" aria-label="Color Contrast evidence in annotations" title="Color Contrast evidence in annotations">A-2</a>].</li>
    <li>Low contrast for interactive elements [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/contrast-interactive-elements.html" aria-label="Contrast Interactive Elements evidence in plot tools" title="Contrast Interactive Elements evidence in plot tools">PT-4</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/contrast-interactive-elements.html" aria-label="Contrast Interactive Elements evidence in plotting interface" title="Contrast Interactive Elements evidence in plotting interface">PI-4</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/contrast-interactive-elements.html" aria-label="Contrast Interactive Elements evidence in annotations" title="Contrast Interactive Elements evidence in annotations">A-3</a>].</li>
    <li>Target pointer size is too small [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/target-pointer-size.html" aria-label="Target Pointer Size evidence in plot tools" title="Target Pointer Size evidence in plot tools">PT-17</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/target-pointer-size.html" aria-label="Target Pointer Size evidence in plotting interface" title="Target Pointer Size evidence in plotting interface">PI-25</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/target-pointer-size.html" aria-label="Target Pointer Size evidence in annotations" title="Target Pointer Size evidence in annotations">A-21</a>].</li>
    <li>Interaction is tedious [<a href="https://bokeh-a11y-audit.readthedocs.io/annotations/tedious.html" aria-label="Tedious evidence in annotations" title="Tedious evidence in annotations">A-22</a>].</li>
    <li>Data density [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/data-density.html" aria-label="Data Density evidence in plotting interface" title="Data Density evidence in plotting interface">PI-25</a>].</li>
    <li>Spacing [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/spacing.html" aria-label="Spacing evidence in plot tools" title="Spacing evidence in plot tools">PT-15</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/spacing.html" aria-label="Spacing evidence in plotting interface" title="Spacing evidence in plotting interface">PI-22</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/spacing.html" aria-label="Spacing evidence in annotations" title="Spacing evidence in annotations">A-18</a>].</li>
    <li>Focus indicator not perceivable [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/keyboard-focus.html" aria-label="Keyboard Focus evidence in plot tools" title="Keyboard Focus evidence in plot tools">PT-11</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/keyboard-focus.html" aria-label="Keyboard Focus evidence in plotting interface" title="Keyboard Focus evidence in plotting interface">PI-13</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/keyboard-focus.html" aria-label="Keyboard Focus evidence in annotations" title="Keyboard Focus evidence in annotations">A-11</a>].</li>
    <li>Meaningful elements can be distinguished [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/meaningful-elements.html" aria-label="Meaningful Elements evidence in plotting interface" title="Meaningful Elements evidence in plotting interface">PI-15</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/meaningful-elements.html" aria-label="Meaningful Elements evidence in annotations" title="Meaningful Elements evidence in annotations">A-12</a>].</li>
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
    <li>No title, summary, or caption provided [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/title-summary.html" aria-label="Title Summary evidence in plotting interface" title="Title Summary evidence in plotting interface">PI-27</a>].</li>
    <li>Axis labels are not clear or present [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/axis-labels.html" aria-label="Axis Labels evidence in plotting interface" title="Axis Labels evidence in plotting interface">PI-1</a>].</li>
    <li>No table [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/no-table.html" aria-label="No Table evidence in plotting interface" title="No Table evidence in plotting interface">PI-23</a>].</li>
    <li>Visually apparent features are not described [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visually-apparent-features.html" aria-label="Visually Apparent Features evidence in plot tools" title="Visually Apparent Features evidence in plot tools">PT-19</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/visually-apparent-features.html" aria-label="Visually Apparent Features evidence in plotting interface" title="Visually Apparent Features evidence in plotting interface">PI-29</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/visually-apparent-features.html" aria-label="Visually Apparent Features evidence in annotations" title="Visually Apparent Features evidence in annotations">A-25</a>].</li>
    <li>Explanation or purpose [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/explanation-purpose.html" aria-label="Explanation Purpose evidence in plot tools" title="Explanation Purpose evidence in plot tools">PT-8</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/explanation-purpose.html" aria-label="Explanation Purpose evidence in plotting interface" title="Explanation Purpose evidence in plotting interface">PI-9</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/explanation-purpose.html" aria-label="Explanation Purpose evidence in annotations" title="Explanation Purpose evidence in annotations">A-6</a>].</li>
    <li>No interaction cues or instructions [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/cues-instructions.html" aria-label="Cues Instructions evidence in plot tools" title="Cues Instructions evidence in plot tools">PT-7</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/cues-instructions.html" aria-label="Cues Instructions evidence in plotting interface" title="Cues Instructions evidence in plotting interface">PI-7</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/cues-instructions.html" aria-label="Cues Instructions evidence in annotations" title="Cues Instructions evidence in annotations">A-5</a>].</li>
    <li>Not human-readable [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/human-readable.html" aria-label="Human Readable evidence in plotting interface" title="Human Readable evidence in plotting interface">PI-11</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/human-readable.html" aria-label="Human Readable evidence in annotations" title="Human Readable evidence in annotations">A-8</a>].</li>
    <li>Only one modality/input is provided [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/modality-input.html" aria-label="Modality Input evidence in plot tools" title="Modality Input evidence in plot tools">PT-13</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/modality-input.html" aria-label="Modality Input evidence in plotting interface" title="Modality Input evidence in plotting interface">PI-17</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/modality-input.html" aria-label="Modality Input evidence in annotations" title="Modality Input evidence in annotations">A-13</a>].</li>
    <li>Metrics and variables are not defined [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/metrics-variables.html" aria-label="Metrics Variables evidence in plotting interface" title="Metrics Variables evidence in plotting interface">PI-16</a>].</li>
    <li>Cannot be navigated according to narrative/structure [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/narrative-structure.html" aria-label="Narrative Structure evidence in plotting interface" title="Narrative Structure evidence in plotting interface">PI-18</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/narrative-structure.html" aria-label="Narrative Structure evidence in annotations" title="Narrative Structure evidence in annotations">A-14</a>].</li>
    <li>Single process [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/single-process.html" aria-label="Single Process evidence in plotting interface" title="Single Process evidence in plotting interface">PI-21</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/single-process.html" aria-label="Single Process evidence in annotations" title="Single Process evidence in annotations">A-17</a>].</li>
    <li>Interactive context is not clear [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/interactive-contrast.html" aria-label="Interactive Context evidence in plot tools" title="Interactive Context evidence in plot tools">PT-10</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/interactive-contrast.html" aria-label="Interactive Context evidence in annotations" title="Interactive Context evidence in annotations">A-10</a>].</li>
    <li>Complex actions have alternatives [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/complex-actions.html" aria-label="Complex Actions evidence in plot tools" title="Complex Actions evidence in plot tools">PT-2</a>].</li>
    <li>Information complexity [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/information-complexity.html" aria-label="Information Complexity evidence in plotting interface" title="Information Complexity evidence in plotting interface">PI-12</a>].</li>
</ul>
    

##### Example

<p><i>Example taken from plot tools [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">1</a>].</i> Below demonstrates a screen reader user's frustrating and confusing interaction experience.</p>

```{figure} ./plotting-interface/assets/plotting-interface_information-complexity_1.png
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
    <li>Explanation or purpose [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/explanation-purpose.html" aria-label="Explanation Purpose evidence in plot tools" title="Explanation Purpose evidence in plot tools">PT-8</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/explanation-purpose.html" aria-label="Explanation Purpose evidence in plotting interface" title="Explanation Purpose evidence in plotting interface">PI-9</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/explanation-purpose.html" aria-label="Explanation Purpose evidence in annotations" title="Explanation Purpose evidence in annotations">A-6</a>].</li>
    <li>No interaction cues or instructions [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/cues-instructions.html" aria-label="Cues Instructions evidence in plot tools" title="Cues Instructions evidence in plot tools">PT-7</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/cues-instructions.html" aria-label="Cues Instructions evidence in plotting interface" title="Cues Instructions evidence in plotting interface">PI-7</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/cues-instructions.html" aria-label="Cues Instructions evidence in annotations" title="Cues Instructions evidence in annotations">A-5</a>].</li>
    <li>Interactive context is not clear [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/interactive-context.html" aria-label="Interactive Context evidence in plot tools" title="Interactive Context evidence in plot tools">PT-10</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/interactive-context.html" aria-label="Interactive Context evidence in annotations" title="Interactive Context evidence in annotations">A-10</a>].</li>
    <li>Changes are not easy to follow [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/changes-easy-to-follow.html" aria-label="Changes Easy to Follow evidence in plot tools" title="Changes Easy to Follow evidence in plot tools">PT-1</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/changes-easy-to-follow.html" aria-label="Changes Easy to Follow evidence in plotting interface" title="Changes Easy to Follow evidence in plotting interface">PI-2</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/changes-easy-to-follow.html" aria-label="Changes Easy to Follow evidence in annotations" title="Changes Easy to Follow evidence in annotations">A-1</a>].</li>
    <li>Interactions are not forgivable [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/interactions-forgivable.html" aria-label="Interactions Forgivable evidence in plot tools" title="Interactions Forgivable evidence in plot tools">PT-9</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/interactions-forgivable.html" aria-label="Interactions forgivable evidence in annotations" title="Interactions forgivable evidence in annotations">A-9</a>].</li>
    <li>State is not easy to share or reproduce [<a href="https://bokeh-a11y-audit.readthedocs.io/annotations/share-reproduce.html" aria-label="Share Reproduce evidence in annotations" title="Share Reproduce evidence in annotations">A-16</a>].</li>
    <li>Location and history is not clear [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/location-history.html" aria-label="Location History evidence in plot tools" title="Location History evidence in plot tools">PT-12</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/location-history.html" aria-label="Location History evidence in plotting interface" title="Location History evidence in plotting interface">PI-14</a>].</li>
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
    <li>Elements are visual only [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visual-only.html" aria-label="Visual only evidence in plot tools" title="Visual only evidence in plot tools">PT-18</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">PI-28</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/visual-only.html" aria-label="Visual only evidence in annotations" title="Visual only evidence in annotations">A-24</a>].</li>
    <li>Only one modality/input is provided [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/modality-input.html" aria-label="Modality Input evidence in plot tools" title="Modality Input evidence in plot tools">PT-13</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/modality-input.html" aria-label="Modality Input evidence in plotting interface" title="Modality Input evidence in plotting interface">PI-17</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/modality-input.html" aria-label="Modality Input evidence in annotations" title="Modality Input evidence in annotations">A-13</a>].</li>
    <li>Semantically invalid [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/semantically-invalid.html" aria-label="Semantically Invalid evidence in plot tools" title="Semantically Invalid evidence in plot tools">PT-14</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/semantically-invalid.html" aria-label="Semantically Invalid evidence in plotting interface" title="Semantically Invalid evidence in plotting interface">PI-20</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/semantically-invalid.html" aria-label="Semantically Invalid evidence in annotations" title="Semantically Invalid evidence in annotations">A-15</a>].</li>
    <li>Fragile support [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/fragile-support.html" aria-label="Fragile Support evidence in plotting interface" title="Fragile Support evidence in plotting interface">PI-10</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/fragile-support.html" aria-label="Fragile Support evidence in annotations" title="Fragile Support evidence in annotations">A-7</a>].</li>
    <li>Interactive context is not clear [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/interactive-context.html" aria-label="Interactive Context evidence in plot tools" title="Interactive Context evidence in plot tools">PT-10</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/interactive-context.html" aria-label="Interactive Context evidence in annotations" title="Interactive Context evidence in annotations">A-10</a>].</li>
    <li>Complex actions have alternatives [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/complex-actions.html" aria-label="Complex Actions evidence in plot tools" title="Complex Actions evidence in plot tools">PT-2</a>].</li>
    <li>Interactions are not forgivable [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/interactions-forgivable.html" aria-label="Interactions Forgivable evidence in plot tools" title="Interactions Forgivable evidence in plot tools">PT-9</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/interactions-forgivable.html" aria-label="Interactions forgivable evidence in annotations" title="Interactions forgivable evidence in annotations">A-9</a>].</li>
    <li>State is not easy to share or reproduce [<a href="https://bokeh-a11y-audit.readthedocs.io/annotations/share-reproduce.html" aria-label="Share Reproduce evidence in annotations" title="Share Reproduce evidence in annotations">A-16</a>].</li>
    <li>Location and history is not clear [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/location-history.html" aria-label="Location History evidence in plot tools" title="Location History evidence in plot tools">PT-12</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/location-history.html" aria-label="Location History evidence in plotting interface" title="Location History evidence in plotting interface">PI-14</a>].</li>
    <li>Focus indicator not perceivable [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/keyboard-focus.html" aria-label="Keyboard Focus evidence in plot tools" title="Keyboard Focus evidence in plot tools">PT-11</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/keyboard-focus.html" aria-label="Keyboard Focus evidence in plotting interface" title="Keyboard Focus evidence in plotting interface">PI-13</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/keyboard-focus.html" aria-label="Keyboard Focus evidence in annotations" title="Keyboard Focus evidence in annotations">A-11</a>].</li>
    <li>Zoom and reflow are not supported [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/zoom-reflow.html" aria-label="Zoom Reflow evidence in plot tools" title="Zoom Reflow evidence in plot tools">PT-20</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/zoom-reflow.html" aria-label="Zoom Reflow evidence in plotting interface" title="Zoom Reflow evidence in plotting interface">PI-30</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/zoom-reflow.html" aria-label="Zoom Reflow evidence in annotations" title="Zoom Reflow evidence in annotations">A-26</a>].</li>
    <li>Scrolling experiences cannot be altered [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/scrolling.html" aria-label="Scrolling evidence in plotting interface" title="Scrolling evidence in plotting interface">PI-19</a>].</li>
</ul>

##### Example

<p><i>Example taken from plotting interface [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/zoom-reflow.html" aria-label="Zoom and reflow evidence in plotting interface" title="Zoom and reflow evidence in plotting interface">1</a>].</i> Below demonstrates how a high-zoom user will have a worse experience reading Bokeh's text than someone who uses Bokeh at 100% zoom. Because Bokeh renders with canvas, text becomes rasterized and does not scale well compared to HTML or SVG elements when zoomed.</p>

```{figure} ./plotting-interface/assets/plotting-interface_zoom-reflow_6.png
:width: 100%
:alt: Viewport is zoomed in to 400% showing the canvas-based text from the bar chart labels being highly aliased and fuzzy, compared to the text for the Scatter plot beneath (circled in red) which is high fidelity and readable (fails).

Viewport is zoomed in to 400% showing the canvas-based text from the bar chart labels being highly aliased and fuzzy, compared to the text for the Scatter plot beneath (circled in red) which is high fidelity and readable (fails).
```

#### <a id="finding-3B" href="#finding-3B" aria-label="Finding 3B"><span aria-hidden="true">#</span></a> B. System's presentation is not flexible

Many users, especially those with disabilities, customize their technology experiences. This is called "fitting" in some spaces, but generally is part of "personalization" and "customization." In order for an end user to be able to make these changes to an interface, it must be built on a relatively flexible system. Rigid systems will try to enforce their own rules for styling, animation and more. But flexible systems are built with an assumption that end users may override things.

There is a massive array of different things that end users might want to be able to do and building a system that could allow them to do whatever they wanted might be impossible. However, there are a few things that should _always_ work as-expected out of the box, which we check for: detecting and adapting to changes in system-set high contrast mode, if textures/patterns are on can they be turned off, whether animations can be disabled, zoom/reflow support, ability to adjust scrolling experiences, whether obscure chart types have alternatives for viewing the same data, and whether text can be manipulated using css.

Foundationally, many users leverage browser extensions that automatically try to update every webpage they visit to suit their preferred minimum font size, text spacing, color choices, and more. A library's inability to respond to simple CSS-based changes can produce pretty harsh barriers for some end users (and also can look clunky too). Responding to an end-user's personal CSS as-expected is easily the most important first thing we check. Then we test different devices and assistive tech (mobile devices, magnifiers). After that, we work through system settings (contrast, animations, textures, etc) and lastly we check certain visualization-specific things.

Ideally, all content on the web is flexible enough to handle these variations that facilitate an end-user's "fit."

##### Evidence of this finding

<ul>
    <li>Complex actions have alternatives [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/complex-actions.html" aria-label="Complex Actions evidence in plot tools" title="Complex Actions evidence in plot tools">PT-2</a>].</li>
    <li>Zoom and reflow are not supported [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/zoom-reflow.html" aria-label="Zoom Reflow evidence in plotting interface" title="Zoom Reflow evidence in plotting interface">PI-30</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/zoom-reflow.html" aria-label="Zoom Reflow evidence in annotations" title="Zoom Reflow evidence in annotations">A-26</a>].</li>
    <li>Scrolling experiences cannot be altered [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/scrolling.html" aria-label="Scrolling evidence in plotting interface" title="Scrolling evidence in plotting interface">PI-19</a>].</li>
    <li>User's style changes are not respected [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/style-change-respected.html" aria-label="Style Change Respected evidence in plot tools" title="Style Change Respected evidence in plot tools">PT-16</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/style-change-respected.html" aria-label="Style Change Respected evidence in plotting interface" title="Style Change Respected evidence in plotting interface">PI-24</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/style-change-respected.html" aria-label="Style Change Respected evidence in annotations" title="Style Change Respected evidence in annotations">A-19</a>].</li>
    <li>Contrast and texture cannot be adjusted [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/contrast-texture-adjustments.html" aria-label="Contrast Texture Adjustments evidence in plot tools" title="Contrast Texture Adjustments evidence in plot tools">PT-5</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/contrast-texture-adjustments.html" aria-label="Contrast Texture Adjustments evidence in plotting interface" title="Contrast Texture Adjustments evidence in plotting interface">PI-5</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/contrast-texture-adjustments.html" aria-label="Contrast Texture Adjustments evidence in annotations" title="Contrast Texture Adjustments evidence in annotations">A-4</a>].</li>
    <li>User's text adjustments are not respected [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/text-adjustments.html" aria-label="Text Adjustments evidence in plotting interface" title="Text Adjustments evidence in plotting interface">PI-26</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/text-adjustments.html" aria-label="Text Adjustments evidence in annotations" title="Text Adjustments evidence in annotations">A-23</a>].</li>
</ul>

##### Example

<p><i>Example taken from plotting interface [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/contrast-texture-adjustments.html" aria-label="Contrast and texture evidence in plotting interface" title="Contrast and texture evidence in plotting interface">1</a>].</i> Below demonstrates how an inflexible visualization is incapable of correctly responding to an operating system's *High Contrast* mode.</p>

```{figure} ./plotting-interface/assets/plotting-interface_style-change-respected.png
:width: 100%
:alt: A scatter plot is shown. A high contrast filter has been implemented, and the web browser background is black with white font. However, the chart space retains it's default color scheme - the contrast change was not applied (fails).

A scatter plot is shown. A high contrast filter has been implemented, and the web browser background is black with white font. However, the chart space retains it's default color scheme - the contrast change was not applied (fails).
```

## <a id="suggestions" href="#suggestions" aria-label="Suggestions"><span aria-hidden="true">#</span></a> Suggested directions for remediation

The following suggestions are primarily intended as high-level goals, spelled out as imperatives. The lower-level details for how to accomplish each of these should be sorted out in our actual roadmap and eventual issues on github.

Ideally, the following are written as _invitations_ for the Bokeh community to get involved. There's a lot to do!

### Focus on text experiences: explanations, descriptions, and labels

Charts need to be described. A designer or developer should, at the very least, have a way to easily provide descriptions for their visualizations. This should be done before anything else. Bokeh needs to give them a way to add descriptions for screen reader users. (Note: this is not the same as a caption.)

Common practice in other libraries (see Highcharts, Visa Chart Components, Vega Lite, Olli, etc) is to automatically describe parts of the chart that can be automatically parsed, like the axes, legends, data ranges, data types, etc. This should be provided to users in alt text (at minimum) or at best via an alternative document. This is typically _after_ the designer-provided descriptions.

The final part of descriptions is that many major visualization libraries also add navigable labels for rendered elements within the chart. This can be quite a lot of work to do well, especially if interactivity (and not just screen reader navigation) is part of the equation. I break this down a little bit more in the "support assitive technology interaction" section, below.

In addition, all of the major text elements in a chart (title, subtitle, captions, annotations, etc) need to be exposed to screen reader users somehow. Rendering text in a raster format (like `<canvas>`) puts pressure on the system: either you completely recreate the major text elements in HTML (but hide them visually in a way that still allows screen reader access) or you may need to move text rendering off of canvas. Coordinating either of these can be a bit of work.

More care should also be taken for describing what various things and explaining how to use and interpret the things they do (for example, the interactive annotations and all of the plot tools). New users need cues to know what is interactive, especially like the subtle examples of the tooltips and selectable legend in our [line chart](https://quansight-labs.github.io/bokeh-a11y-audit/). I would go so far as recommending adding end-user how-to guides. I highly suggest adding documentation that is focused on helping Bokeh's end-users get the most out of their interactive experience, especially those who are new. By now, Bokeh's community has likely established enough interaction patterns that could be written up.

### Use better building materials

The next most important thing, after locking in text-related accessibility, is to use the correct building materials.

As already hinted, `<canvas>` can have some limitations for accessibility. It's great for high-performance rendering, but that performance is directly related to a lack of markup + DOM overhead that comes with more accessible materials, like HTML (or even SVG).

As for virtually everything that is interactive, from annotations, tooltip-triggering elements, to the buttons in the plot tools, natively semantic HTML elements will be far better for accessibility than the elements that they currently are. As an example: a `<div>` isn't natively semantic at all, but a `<button>` is. Adding on-click event listeners to a div would make it listen to mouse events, but keyboard-driven assistive technologies can't reach those elements natively, like they do with a button. The general philosophy here in accessibility communities online is that if a native element can do what you're trying to do, you should use that element.

[Sarah Higley writes](https://sarahmhigley.com/writing/tooltips-in-wcag-21/) about how "a major pitfall of approaching web design as a visual medium is conflating visual patterns with functional or interaction patterns." Her point is that thinking in terms of a visual language can sometimes bias web developers and designers into trying to solve all interactive problems using visual means. HTML has a [massive array](https://developer.mozilla.org/en-US/docs/Glossary/Semantics#semantic_elements) of elements with functional semantics and they should be used whenever possible. Not only will assistive technologies have a better time, but so will automatic agents when parsing a website (like crawlers for search engines and foundational models).

Plus, it is easier for someone else to interpret code that uses semantic markup. This will certainly have a downstream effect on future community contributions and new projects.

### Build a flexible system
People personalize their technology. And people also use software with a variety of different devices in different contexts. A flexible, compromising system is necessary for that software to be usable for all people in all places.

There are some existing, relatively ubiquitous UI customizations that people commonly do that Bokeh needs to "watch" for. People commonly use "high contrast" modes, increase font size/weight/spacing, turn off motion/animations, turn on redundant encodings, and zoom/magnify. Media queries and other strategies in CSS (and even JavaScript) can be used to look out for these user-determinations. But also, an API should be implemented that allow someone to programmatically override the design of a visualization on their own (in cases when it might be hard to automatically determine what the user's needs).

In my latest project on what I call "[softerware](https://www.frank.computer/papers/2025-cga-softerware.pdf)," I actually explored what the future of accessibility customization could look like for data visualizations. But at large, the most accessible data visualization libraries (like Highcharts) only really implement a couple of automatically-adjusting characteristics. Bokeh's community has the opportunity to really lead (or co-lead) the development and implementation of what user personalizations every data visualization library should be flexibly designed to adapt to.


### Help developers succeed

One of the lessons that I learned while at Visa, helping to build [Visa Chart Components](https://github.com/visa/visa-chart-components), was that our *first* users were developers. And if we wanted them to actually implement the cool things we put in place, we needed to have a strategy focused on making their lives as easy as possible.

So in order for this entire accessibility project to be successful, developers need smart **defaults** for anything that we believe we should handle out of the box (such as supplying automatic descriptions for certain parts of a chart, making charts navigable and interactive with assistive tech, minimum font sizes, strong contrast defaults, etc).

In addition to **defaults**, we also should consider which **guardrails** to put in place, such as validation errors when alt text (or other important characteristics) aren't supplied. We could also consider limits on how many categories can be encoded before throwing warnings in the JavaScript console (that perhaps suggest other strategies like small multiples, aggregation, or other visualization types).

After **defaults** and **guardrails**, developers will eventually want special control and modularity with accessibility too. Simple, powerful **utilities** are huge in the right hands. Your power-users who really know what they are doing will thank you. Defaults and guardrails are for your developers who aren't as familiar with accessibility. But you also want to maximize the productivity of the developers who *do* know what they're doing. Give them more capabilities whenever possible. One good example of this that I recognized in past work was separating our [color contrast checking algorithms](https://github.com/visa/visa-chart-components/tree/main/packages/utils#colors) into modular functions. It not only helps power-users but even folks who might not be interested in the rest of the Bokeh ecosystem. Sometimes if the utilities are good enough, folks will come to Bokeh just for that.

Lastly, for developers to succeed, they also need to develop a sense of language for accessibility. If you want people to *think* in terms of accessibility, first you need to give them the right language. [Language is the pre-requisite to seeing and thinking about the world in a new way](https://en.wikipedia.org/wiki/Linguistic_relativity). And tools can help your practitioner-users develop a **design vocabulary** for how their decisions impact users with disabilities.

To buld a design vocabulary among our users, first we need strong examples and documentation. But also, the functions, utilities, and architecture of Bokeh should be designed in a way that helps developers understand the outcomes of their design decisions. There should be *vocabulary correspondance* between the concepts we want people to envision and how the API is actually used.

An example of a bad API is `aria-label` versus `alt` as properties on elements. As much as I love [ARIA](https://www.w3.org/WAI/standards-guidelines/aria/) (the Accessible, Rich, Internet Applications) standards, they end up introducing a whole second layer of language into web development. If someone hears the term "aria label" they might have no idea how that impacts someone with a disability. What does this *do*? And to make it worse, it is a parallel term to "alt text." Confusing! So if someone sees these two phrases (`aria-label` and `alt`), they might have no idea what they mean or when to use one over the other.

But as toolmakers, we can consolidate these concepts into a new design-focused term, like `accessibility-description` or `screen-reader-description` or equivalent. Bokeh can do translation work between what actually makes an interface accessible at a low level and the **design vocabulary** that is ideal for Bokeh's practitioner-users.

We have the opportunity to teach an entire community of Python data scientists, analysts, and developers how to make visualizations more accessible. To do this, we need to focus on making it as easy as possible for them to learn-through-use. Developers need smart **defaults**, thoughtful **guardrails**, powerful **utilities**, and a focus on a disability-centered **design vocabulary**.