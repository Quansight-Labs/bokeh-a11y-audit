# Audit Summary

```{note}
This page is being developed.
```

This summary document serves 2 purposes and is organized into 2 major subheadings, below.

The first section focuses on providing an overview of problems and themes present in the evidence gathered from our audit of Bokeh's [plotting interface](https://bokeh-a11y-audit.readthedocs.io/plotting-interface/index.html), [plot tools](https://bokeh-a11y-audit.readthedocs.io/plot-tools/index.html), and [annotations](https://bokeh-a11y-audit.readthedocs.io/annotations/index.html) artifacts.

The second section focuses on suggestions for remediation based on the connectedness of various issues, prioritization of critical failures, and (in some cases) the ease of the fix involved. The remediation process should be negotiated and discussed broadly, broken into an actionable plan, and then enacted. However, it is important as an auditor to present my suggested course of action as a starting point for the discussion.

## <a id="findings" href="#findings" aria-label="Findings"><span aria-hidden="true">#</span></a> Overview of findings: problems and themes

This section will break down the major themes related to problems or meta-issues as a result of our auditing evaluation. It is important to note that audits, when performed true to their intent, are about focusing on gathering evidence of failures, issues, gaps, or problems. Then that evidence serves as a basis for an analysis of systemic and interconnected issues across a system.

What separates an audit from the typical atomic or incremental approach used in open source software (aka "opening an issue") is that audits are a chance to systematically evaluate and analyze an entire ecosystem and synthesize all possible related problems at once. As an example, it is common to see an issue on an open source repo that asks for "alt text capabilities." While this might be great to add on, sometimes a library or tool needs several larger refactors or overhauls to really reach ideals/goals and uphold principles of good design. In order to do this (and even know what the larger issues are), having a procedure for taking a step back, finding the biggest gaps, and setting goalposts is vital. Consider the following subheadings as those big gaps.

### <a id="finding-1" href="#finding-1" aria-label="Finding 1"><span aria-hidden="true">#</span></a> 1. Finding: Lacks foundational accessibility

I don't think this will come as a surprise to the Bokeh team, but it is quite clear that Bokeh has substantial gaps for basic assistive technology support and text accessibility.

Providing alternative text will not be enough for Bokeh to become accessible, either. Textual design overall is lacking and due to the complexity of interaction that Bokeh is capable of, significantly more work will need to be done to lay the groundwork for foundational accessibility.

Many, many tests failed because of this. Some areas:

#### <a id="finding-1A" href="#finding-1A" aria-label="Finding 1A"><span aria-hidden="true">#</span></a> A. Little textual accessibility
Across our tests, this was the most consistent finding and also the type of failure that intersects with the most evidence.

Both screen reader accessibility and cognitive accessibility require good text design, which means this is fundamental to include in order to support assistive technologies. Text should be a deeply embedded part of any interface but especially one that relies heavily on visuals, data, and complex interactivity.

Note that *only* alt text (and aria-labels) are hidden visually. But overall, the accessibility of a textual experience that accompanies an analytical dashboard, visualization, or interface, is the cornerstone contributor to the overall accessibility of that artifact. Text accessibility is paramount.

Not only should screen readers be provided descriptions so that screen reader users can perceive *what* content is (at both a high level through alt but also a low level via tables and elements with aria labels), but descriptions should be provided for *how* to interact, *why* things are the way they are, and more. Making these additional textual descriptions and experiences visually available has a broad impact on who gets included, how much work an interface is asking its users to do, and ultimately how successful the usability of that interface is. Better text makes for a better experience for everyone.

Busy executives can look at an interface and make faster decisions. Scientists can share their work more clearly and succinctly with their peers. Novices can learn more quickly. And of course, people with disabilities can be included.

Text design must consider all possible text in an interface and includes: titles, subtitles, captions, alt text on a visualization, aria labels on navigation elements, aria labels on interactive elements, semantics and aria roles are provided, tables of data, descriptions and help menus, and more.

This finding is primarily about the fact that a significant amount of text that should be present in the interface (and under the hood) simply isn't.

Evidence of this finding:
<ul>
    <li>Elements are visual only [<a href="https://bokeh-a11y-audit.readthedocs.io/plot-tools/visual-only.html" aria-label="Visual only evidence in plot tools" title="Visual only evidence in plot tools">1</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/plotting-interface/visual-only.html" aria-label="Visual only evidence in plotting interface" title="Visual only evidence in plotting interface">2</a>, <a href="https://bokeh-a11y-audit.readthedocs.io/annotations/visual-only.html" aria-label="Visual only evidence in annotations" title="Visual only evidence in annotations">3</a>].</li>
    <li>Only one modality/input is provided [].</li>
    <li>Cannot be navigated according to narrative/structure [].</li>
    <li>Semantically invalid [].</li>
    <li>No title, summary, or caption provided [].</li>
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



##### Examples

```{note}
Explanation and citations pending.
```

### <a id="finding-2" href="#finding-2" aria-label="Finding 2"><span aria-hidden="true">#</span></a> 2. Finding: Minimal cognitive support exists

```{note}
Explanation and citations pending.
```

#### <a id="finding-2A" href="#finding-2A" aria-label="Finding 2A"><span aria-hidden="true">#</span></a> A. Findability has problems

```{note}
Explanation and citations pending.
```

Lack of button labels, difficulty of finding out tooltips exist

#### <a id="finding-2B" href="#finding-2B" aria-label="Finding 2B"><span aria-hidden="true">#</span></a> B. Understanding is not easy
Explanations and descriptions, human readible, reading level, Complexity of interactions

```{note}
Explanation and citations pending.
```

don't forget the decimal points from annotations

#### <a id="finding-2C" href="#finding-2C" aria-label="Finding 2C"><span aria-hidden="true">#</span></a> C. Cues, callouts, and feedback are missing

```{note}
Explanation and citations pending.
```

#### <a id="finding-2D" href="#finding-2D" aria-label="Finding 2D"><span aria-hidden="true">#</span></a> D. System feedback is lacking

```{note}
Explanation and citations pending.
```

### <a id="finding-3" href="#finding-3" aria-label="Finding 3"><span aria-hidden="true">#</span></a> 3. Finding: System and experience is fragile

```{note}
Explanation and citations pending.
```

#### <a id="finding-3A" href="#finding-3A" aria-label="Finding 3A"><span aria-hidden="true">#</span></a> A. Functional semantics are very poor

```{note}
Explanation and citations pending.
```

#### <a id="finding-3B" href="#finding-3B" aria-label="Finding 3B"><span aria-hidden="true">#</span></a> B. Is not contextually robust

```{note}
Explanation and citations pending.
```

#### <a id="finding-3C" href="#finding-3C" aria-label="Finding 3C"><span aria-hidden="true">#</span></a> C. Lacking multiple paths to the same goal

```{note}
Explanation and citations pending.
```

#### <a id="finding-3D" href="#finding-3D" aria-label="Finding 3D"><span aria-hidden="true">#</span></a> D. Litle to no respect for user preferences

```{note}
Explanation and citations pending.
```

### <a id="finding-4" href="#finding-4" aria-label="Finding 4"><span aria-hidden="true">#</span></a> 4. Finding: Perception can be difficult

```{note}
Explanation and citations pending.
```

#### <a id="finding-4A" href="#finding-4A" aria-label="Finding 4A"><span aria-hidden="true">#</span></a> A. Low contrast and discriminability

```{note}
Explanation and citations pending.
```

#### <a id="finding-4B" href="#finding-4B" aria-label="Finding 4B"><span aria-hidden="true">#</span></a> B. Small things, hidden things

```{note}
Explanation and citations pending.
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

### Consider *end*-user documentation

```{note}
Explanation pending.
```
