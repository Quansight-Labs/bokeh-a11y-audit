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

### <a id="finding-1" href="#finding-1" aria-label="Finding 1"><span aria-hidden="true">#</span></a> 1. Finding: Assistive technology is not supported

I don't think this will come as a surprise to the Bokeh team, but it is quite clear that Bokeh has substantial gaps for basic assistive technology support. And providing a means for simple alternative text is not enough for Bokeh to be accessible. Bokeh is capable of relatively complex mouse-pointer based interactivity. The functional outcomes of that interactivity must also be made easily available to users of assistive technologies (including more than just screen reader users).

Many, many tests failed because of this. Some areas:

#### <a id="finding-1A" href="#finding-1A" aria-label="Finding 1A"><span aria-hidden="true">#</span></a> A. Screen reader perception

```{note}
Explanation and citations pending.
```

#### <a id="finding-1B" href="#finding-1B" aria-label="Finding 1B"><span aria-hidden="true">#</span></a> B. Screen reader interactivity

```{note}
Explanation and citations pending.
```

#### <a id="finding-1C" href="#finding-1C" aria-label="Finding 1C"><span aria-hidden="true">#</span></a> C. Foundational navigation

keyboard trap, narrative structure, etc

```{note}
Explanation and citations pending.
```

#### <a id="finding-1D" href="#finding-1D" aria-label="Finding 1D"><span aria-hidden="true">#</span></a> D. Foundational interactivity

```{note}
Explanation and citations pending.
```

### <a id="finding-2" href="#finding-2" aria-label="Finding 2"><span aria-hidden="true">#</span></a> 2. Finding: Minimal cognitive support exists

```{note}
Explanation and citations pending.
```

#### <a id="finding-2A" href="#finding-2A" aria-label="Finding 2A"><span aria-hidden="true">#</span></a> A. Findability

```{note}
Explanation and citations pending.
```

Lack of button labels, difficulty of finding out tooltips exist

#### <a id="finding-2B" href="#finding-2B" aria-label="Finding 2B"><span aria-hidden="true">#</span></a> B. Explanations and descriptions

```{note}
Explanation and citations pending.
```

don't forget the decimal points from annotations

#### <a id="finding-2C" href="#finding-2C" aria-label="Finding 2C"><span aria-hidden="true">#</span></a> C. Cues and callouts

```{note}
Explanation and citations pending.
```

#### <a id="finding-2D" href="#finding-2D" aria-label="Finding 2D"><span aria-hidden="true">#</span></a> D. System feedback

```{note}
Explanation and citations pending.
```

#### <a id="finding-2E" href="#finding-2E" aria-label="Finding 2E"><span aria-hidden="true">#</span></a> E. Complexity of interactions

```{note}
Explanation and citations pending.
```

### <a id="finding-3" href="#finding-3" aria-label="Finding 3"><span aria-hidden="true">#</span></a> 3. Finding: System and experience is fragile

```{note}
Explanation and citations pending.
```

#### <a id="finding-3A" href="#finding-3A" aria-label="Finding 3A"><span aria-hidden="true">#</span></a> A. Functional semantics

```{note}
Explanation and citations pending.
```

#### <a id="finding-3B" href="#finding-3B" aria-label="Finding 3B"><span aria-hidden="true">#</span></a> B. Contextual robustness

```{note}
Explanation and citations pending.
```

#### <a id="finding-3C" href="#finding-3C" aria-label="Finding 3C"><span aria-hidden="true">#</span></a> C. Multiple paths to the same goal

```{note}
Explanation and citations pending.
```

#### <a id="finding-3D" href="#finding-3D" aria-label="Finding 3D"><span aria-hidden="true">#</span></a> D. Respect for user preferences

```{note}
Explanation and citations pending.
```

### <a id="finding-4" href="#finding-4" aria-label="Finding 4"><span aria-hidden="true">#</span></a> 4. Finding: Perception can be difficult

```{note}
Explanation and citations pending.
```

#### <a id="finding-4A" href="#finding-4A" aria-label="Finding 4A"><span aria-hidden="true">#</span></a> A. Contrast and discriminability

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

```{note}
Explanation pending.
```

### Help developers succeed

utilities, validation, and smart defaults

```{note}
Explanation pending.
```

### Consider user documentation

```{note}
Explanation pending.
```
