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
    <li>Cannot be navigated according to narrative/structure [].</li>
    <li>Semantically invalid [].</li>
    <li>No title, summary, or caption provided [].</li>
    <li>No table [].</li>
    <li>Visually apparent features are not described [].</li>
</ul>

This issue is closely related to both [functional semantics](#finding-3A) and [explanations and descriptions](finding-2B), below. (These sections focus on how text can be present but still done incorrectly.)

##### Example

<p><i>Example taken from plotting interface [<a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">2</a>].</i> Below demonstrates that the lack of textual information excludes screen reader users from participation.</p>
<video controls="True" preload="auto" width="100%"><source src="https://bokeh-a11y-audit.readthedocs.io/_images/plotting-interface_visual-only.mp4" type="video/mp4"></video>
<p>A web browser is shown with multiple charts. A screen reader navigates through the page and through multiple charts, but very limited information is given as they do so (fails).</p>
<!-- <figure>
    <img></img>
    <figcaption>
</figure> -->

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
<video controls="True" preload="auto" width="100%"><source src="https://bokeh-a11y-audit.readthedocs.io/_images/plot-tools_visual-only.mp4" type="video/mp4"></video>

<p>A color scatter plot is shown. A screen reader focus indicator moves across the plot tool icons, but when a tool is selected it opens a previously visited link instead of toggling the tool that corresponds to the visual focus indication (fails).</p>

### <a id="finding-2" href="#finding-2" aria-label="Finding 2"><span aria-hidden="true">#</span></a> 2. Finding: Minimal cognitive support exists
Cognitive support can be a difficult thing to ask a visualization library to provide because it isn't always the responsibility of a tool but the implementer of the tool to provide end users with cognitive support. In general, the application and use of the library (the contexts where Bokeh is used) should explain, describe, make outcomes easy, and provide robust alternative ways to reach those outcomes.

However, there are some areas that a visualization library _should_ be responsible for. And of course, there are many things that a visualization library can assist developer-users and designer-users with. Below we are focusing on issues that either fall under the purview of Bokeh or are things that Bokeh can do to assist their users with.

#### <a id="finding-2A" href="#finding-2A" aria-label="Finding 2A"><span aria-hidden="true">#</span></a> A. Findability has problems

Users need to be able to find things. And unfortunately, there are some elements that become essentially invisible or hidden. This can add difficulty or even make certain things impossible.

For screen reader users, semantic labels need to exist for interactive elements so that they know what a particular button or input does and its current state. And without proper labels on elements, they are virtually invisible to screen reader users.

For low vision users, contrast must be sufficiently strong on interactive elements and especially elements that display a change of state (from off to on) where the "off" state should still be interactable.

For sighted mouse users with motor and dexterity impairents, tooltips can be helpful on chart elements but the target size of elements (such as in the line chart) are far too small. Discovering that tooltips exist on an element using pixel-perfect strategies actually creates accessibility barriers for all kinds of folks (but especially those with dexterity disabilities such as tremors or upper-body motor impairments).

##### Evidence of this finding
<ul>
    <li>Visual only [].</li>
    <li>Semantically invalid [].</li>
    <li>Color contrast [].</li>
    <li>Contrast of interactive elements [].</li>
    <li>Target pointer size [].</li>
</ul>

##### Example
<p><i>Example taken from plot tools [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">1</a>].</i> Below demonstrates a screen reader user's frustrating and confusing interaction experience.</p>
<video controls="True" preload="auto" width="100%"><source src="https://bokeh-a11y-audit.readthedocs.io/_images/plot-tools_visual-only.mp4" type="video/mp4"></video>

<p>.</p>

#### <a id="finding-2B" href="#finding-2B" aria-label="Finding 2B"><span aria-hidden="true">#</span></a> B. Understanding is not easy

Explanations and descriptions, human readible, reading level, Complexity of interactions

```{note}
Explanation and citations pending.
```

don't forget the decimal points from annotations

##### Evidence of this finding
<ul>
    <li>a [].</li>
</ul>

##### Example
<p><i>Example taken from plot tools [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">1</a>].</i> Below demonstrates a screen reader user's frustrating and confusing interaction experience.</p>
<video controls="True" preload="auto" width="100%"><source src="https://bokeh-a11y-audit.readthedocs.io/_images/plot-tools_visual-only.mp4" type="video/mp4"></video>

<p>.</p>

#### <a id="finding-2C" href="#finding-2C" aria-label="Finding 2C"><span aria-hidden="true">#</span></a> C. Cues, callouts, and feedback are missing

```{note}
Explanation and citations pending.
```

##### Evidence of this finding
<ul>
    <li>a [].</li>
</ul>

##### Example
<p><i>Example taken from plot tools [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">1</a>].</i> Below demonstrates a screen reader user's frustrating and confusing interaction experience.</p>
<video controls="True" preload="auto" width="100%"><source src="https://bokeh-a11y-audit.readthedocs.io/_images/plot-tools_visual-only.mp4" type="video/mp4"></video>

<p>.</p>

### <a id="finding-3" href="#finding-3" aria-label="Finding 3"><span aria-hidden="true">#</span></a> 3. Finding: System and experience is fragile

```{note}
Explanation and citations pending.
```

#### <a id="finding-3A" href="#finding-3A" aria-label="Finding 3A"><span aria-hidden="true">#</span></a> A. Functional semantics are very poor

```{note}
Explanation and citations pending.
```
##### Evidence of this finding
<ul>
    <li>a [].</li>
</ul>

##### Example
<p><i>Example taken from plot tools [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">1</a>].</i> Below demonstrates a screen reader user's frustrating and confusing interaction experience.</p>
<video controls="True" preload="auto" width="100%"><source src="https://bokeh-a11y-audit.readthedocs.io/_images/plot-tools_visual-only.mp4" type="video/mp4"></video>

<p>.</p>

#### <a id="finding-3B" href="#finding-3B" aria-label="Finding 3B"><span aria-hidden="true">#</span></a> B. Is not contextually robust

```{note}
Explanation and citations pending.
```
##### Evidence of this finding
<ul>
    <li>a [].</li>
</ul>

##### Example
<p><i>Example taken from plot tools [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">1</a>].</i> Below demonstrates a screen reader user's frustrating and confusing interaction experience.</p>
<video controls="True" preload="auto" width="100%"><source src="https://bokeh-a11y-audit.readthedocs.io/_images/plot-tools_visual-only.mp4" type="video/mp4"></video>

<p>.</p>

#### <a id="finding-3C" href="#finding-3C" aria-label="Finding 3C"><span aria-hidden="true">#</span></a> C. Lacks multiple paths to the same goal

```{note}
Explanation and citations pending.
```
##### Evidence of this finding
<ul>
    <li>a [].</li>
</ul>

##### Example
<p><i>Example taken from plot tools [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">1</a>].</i> Below demonstrates a screen reader user's frustrating and confusing interaction experience.</p>
<video controls="True" preload="auto" width="100%"><source src="https://bokeh-a11y-audit.readthedocs.io/_images/plot-tools_visual-only.mp4" type="video/mp4"></video>

<p>.</p>

#### <a id="finding-3D" href="#finding-3D" aria-label="Finding 3D"><span aria-hidden="true">#</span></a> D. Has little to no respect for user preferences

```{note}
Explanation and citations pending.
```
##### Evidence of this finding
<ul>
    <li>a [].</li>
</ul>

##### Example
<p><i>Example taken from plot tools [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">1</a>].</i> Below demonstrates a screen reader user's frustrating and confusing interaction experience.</p>
<video controls="True" preload="auto" width="100%"><source src="https://bokeh-a11y-audit.readthedocs.io/_images/plot-tools_visual-only.mp4" type="video/mp4"></video>

<p>.</p>

### <a id="finding-4" href="#finding-4" aria-label="Finding 4"><span aria-hidden="true">#</span></a> 4. Finding: Perception can be difficult

```{note}
Explanation and citations pending.
```
##### Evidence of this finding
<ul>
    <li>a [].</li>
</ul>

##### Example
<p><i>Example taken from plot tools [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">1</a>].</i> Below demonstrates a screen reader user's frustrating and confusing interaction experience.</p>
<video controls="True" preload="auto" width="100%"><source src="https://bokeh-a11y-audit.readthedocs.io/_images/plot-tools_visual-only.mp4" type="video/mp4"></video>

<p>.</p>

#### <a id="finding-4A" href="#finding-4A" aria-label="Finding 4A"><span aria-hidden="true">#</span></a> A. Low contrast and discriminability

```{note}
Explanation and citations pending.
```
##### Evidence of this finding
<ul>
    <li>a [].</li>
</ul>

##### Example
<p><i>Example taken from plot tools [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">1</a>].</i> Below demonstrates a screen reader user's frustrating and confusing interaction experience.</p>
<video controls="True" preload="auto" width="100%"><source src="https://bokeh-a11y-audit.readthedocs.io/_images/plot-tools_visual-only.mp4" type="video/mp4"></video>

<p>.</p>

#### <a id="finding-4B" href="#finding-4B" aria-label="Finding 4B"><span aria-hidden="true">#</span></a> B. Small things, hidden things, silent things

```{note}
Explanation and citations pending.
```
##### Evidence of this finding
<ul>
    <li>a [].</li>
</ul>

##### Example
<p><i>Example taken from plot tools [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">1</a>].</i> Below demonstrates a screen reader user's frustrating and confusing interaction experience.</p>
<video controls="True" preload="auto" width="100%"><source src="https://bokeh-a11y-audit.readthedocs.io/_images/plot-tools_visual-only.mp4" type="video/mp4"></video>

<p>.</p>

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

### Support more than just mouse interaction

```{note}
Explanation pending.
```

### Build a flexible system

softerware?? >:)

```{note}
Explanation pending.
```

### Help developers succeed

utilities, validation, smart defaults, and guardrails

```{note}
Explanation pending.
```

### Consider _end_-user documentation

```{note}
Explanation pending.
```
