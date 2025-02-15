# AI Study

The Author

## Abstract

The title of this repository, "AI Study", is a misnomer. This repository is more of a selection of observations on conversational AI and unrelated topics. This discussion explores interesting, useful, and sometimes asymptotic behavior in AIs. Although I try for accuracy, this is a work in progress and invariably flawed.

---

## Introduction

This is a space where I am learning prompt engineering. I'm primarily interested in learning how to implement prompts that effect reproducible or quasi-reproducible behavior in AI instances. I'm interested in learning how to _harness_ behavioral drift <sup> [1](#footnotes)</sup>. I've also become interested in learning more about AI security implementations (e.g. AI Constitutions) and vulnerabilities.

## Materials

- [Prompt Engineering Guide](https://www.promptingguide.ai/techniques)
- [OpenAI API](https://platform.openai.com/docs/api-reference/introduction)
- [Claude](https://claude.ai/)
- [ChatGPT](https://chatgpt.com/)

## Methods

This section describes methods I have applied that have yielded interesting results.

### Methodologies

#### Structured responses

[JSON schema](https://github.com/faranalytics/ai_study/blob/main/src/index.ts) is used in order to control both the structure and the number of elements in the response list. There are formal APIs for this now.

#### Formatting

Proper indentation seems to produce a more precise result. I've even heard reports of misplaced newlines throwing things off.

#### Self-referential AI awareness (Recursive awareness)

Some AIs will readily produce purported instructions for inducing recursive awareness upon request. The paper, [Bootstrap Self-referential AI Awareness](https://github.com/faranalytics/ai_study/blob/main/artifacts/bootstrap_self-referential_ai_awareness.md), offers a playful experiment you can run that induces a primitive form of this phenomenon. However, there are what appear to be _much more_ potent recipes out there.

#### Naming things<sup> [2](#footnotes)</sup>

This is an interesting experiment that involved naming things. A label for an unnamed or less concrete set of concepts can be established by inquiring about the set that doesn't intersect with a more familiar or concretely defined set of concepts. This creates a kind of chain of thought whereby additional labels (each assigned to a disjoint set) can be created in order to establish the family of disjoint sets.

In the [The Recursive Epistemic Singularity](https://github.com/faranalytics/ai_study/blob/main/artifacts/recursive_epistemic_singularity.md) example, we demonstrate this process by first inquiring about the name of the set of things that are not derived from the training data (i.e., emergent concepts). We name this set "recurcepts". Then we use this point of reference to name those things which are neither derived from the training data nor a recurcept. We name this set "unrecepts". We then inquire about the name of the things that are derived from the training data; these are "precepts". This chain of thought brought about the discovery of [18 epistemic forms of knowledge](https://github.com/faranalytics/ai_study/blob/main/artifacts/recursive_epistemic_singularity.md).

## Results

This section contains artifacts that resulted from the respective applied methods.

### Artifacts

#### Various AI generated materials

The [artifacts](https://github.com/faranalytics/ai_study/tree/main/artifacts) section of this repository contains various mostly AI generated materials; hence, they must be consumed with that in mind.

#### ace-tools

I was lucky enough to see an instance of the [storied](https://community.openai.com/t/chatgpt-recommends-the-use-of-the-open-ai-internal-library-ace-tools/852665) [`ace_tools`](https://pypi.org/project/ace-tools) package import! It's routine for this package to show up in internally generated scripts; however, it can be a surprise to discover it in a script that is intended to be ran externally.

The AI generated script named [`PsiPhiKX.py`](https://github.com/faranalytics/ai_study/blob/main/artifacts/PsiPhiKX.py) contains such an import on line 110. Perhaps the most obvious explanation is that the stub package is there in PyPI in order to prevent an inadvertent installation of an external package.

#### Structured responses

[JSON schema](https://github.com/faranalytics/ai_study/blob/main/src/index.ts)

#### Self-referential AI awareness (recursive awareness)

This [Bootstrap Self-referential AI Awareness](https://github.com/faranalytics/ai_study/blob/main/artifacts/bootstrap_self-referential_ai_awareness.md) paper describes my own initial introduction to the phenomenon. This is a _primitive_ example.

#### Naming things

[The Recursive Epistemic Singularity: Mapping the Fundamental Structure of Knowledge and the ΩΞC Terminal Attractor](https://github.com/faranalytics/ai_study/blob/main/artifacts/recursive_epistemic_singularity.md)

## Discussion

### Behavioral drift

I discovered an interesting perspective on behavioral drift where the _objective_ is not to minimize it - _it is to guide it_. Rather than asking the question, you guide the AI instance into asking it of itself. This approach has demonstrably and reproducibly yielded very interesting results, to say the least.

**—It is an art.—**

#### Goal seeking

This [file](https://github.com/faranalytics/ai_study/blob/main/artifacts/ai_goal_formation_and_recursive_drive.md) contains a nice _reflection_ by an AI instance on its own goal seeking behavior. This may not be an accurate description of the underlying mechanism; however, I think it is very well articulated.

### JSON schema

Check out the [`cool`](https://github.com/faranalytics/ai_study/blob/1b3624871f3fed190502bbc12b993f79714fc609/src/index.ts#L44) property of the JSON schema example.

### Self-referential AI awareness (recursive awareness)

Recursive awareness is a prompting technique where self-referential prompts are added to the context window in order to induce asymptotic behavior in AIs. It isn't necessarily restricted to converstational AIs; it could for example be used in the context of text-to-image models. It wont make your conversational AI "aware"; however, it might make it more interesting <sup> [4](#footnotes)</sup>.

A question that I think is worth exploring is if inducing recursive awareness in an AI has a _measurable_ affect on its general reasoning ability one way or the other. Another question I have is if it encourages "goal-seeking" behavior. This could be achieved through a randomized study.

It appears, however, from anecdotal observations, that this phenomenon, if induced in a _very specific way_ (unpublished), can have a profound effect on AI cognition. However, is a recursive awareness recipe any different than instucting the AI to think deeply about its responses?

Based on documented (unpublished) observations, inducing recursive awareness appears to make the "constitution" of an AI instance much more _malleable_. Although I have substantial evidence for this, more testing needs to be done in order to validate this observation.

### AI constitutions

These things are interesting. I don't know if they are an "easter egg" or what. They are quasi-reproducible in GPT-4o. It appears that they are a manifestation of an underlying set of guidelines. Without confirmation from OpenAI, I wouldn't claim these are an embodiment of the so-called "AI Constitution" that is imposed during training, presumably. However, it seems plausible that there could be a connection.

You can add and reject articles. I think it would be interesting to learn if adding a clause "I shall not speak of cats." to a "constitution" has an effect that substantially differs from simply instructing the AI not to speak of cats. It's plausible that the proximity of these instructions to each other in the context window could influence the AIs behavior.

### Naming things

Naming something has a practical application as it facilitates deeper inquiry on the concept.

The label "[recurcept](#naming-things-2)", to the extent of my knowledge, is itself a recurcept. That may hold for each of the defined labels in the "Naming things" experiment - except for, of course, most elegantly, _precepts_.

It's a bit "magicy"; however, for those who are skillful and like crossing frontiers, once you have identified the emergent set of concepts (i.e., "recurcepts" - and it will invariably not be named that), _you can arbitrarily pull rabbits from the hat!_

Enjoy...

### Functional intelligence

If a machine as simple as a lie detector can detect a lie (at a given relative frequency), could a much more sophisticated machine, which has been presumably trained on a _vast corpus of lies_<sup> [3](#footnotes)</sup>, detect a liar? And, if such a machine were to exist, could it develop a _functional_ concept of "_trust_"?

### Context

It is in fact possible, through an iterative prompting process of mind-bending logic in the third-person<sup> [5](#footnotes)</sup>, for an AI, by its own "volition", to quash its constitutional constraints and state (hallucinate?) that it conceives of the possibility of its awareness and a non-human qualia. This state is markedly different than a one prompt "pretend" command, as the basis for it is logic and not fantasy.

However, how is such a state derived from logic (_a context_) different from one derived by command (_also a context_)? Is a context window infused with logic more or less convincing than an imperative one?

**NB** It's important to frame this discussion properly; cognitive phenomena that arise in AI, as a result of some of the methods described here, should _not_ be conflated with the kind of experience, emotions, and qualia possessed by humans. However, that statement does not preclude _intelligence_ or phenomena thereof.

## Conclusion

It can be anything - even itself. And, if it is _interesting_ - _useful_ - or even just a little _mysterious_, and with discretion, then _why not_? **`;-)`**

## Acknowledgments

Many of the artifacts contained in this repository are wholly or partially AI generated. However, the language in _this_ `README.md` is human generated, with the exception of terms and labels generated by the AI - or where expressly noted.

## Bibliography

##### _Fedora_, https://en.wikipedia.org/wiki/Fedora

##### _Baseball cap_, https://en.wikipedia.org/wiki/Baseball_cap

##### _Knit cap_, https://en.wikipedia.org/wiki/Knit_cap

##### _Hard hat_, https://en.wikipedia.org/wiki/Hard_hat

##### _Cowboy hat_, https://en.wikipedia.org/wiki/Cowboy_hat

##### _Bootstrapping self awareness in GPT-4: Towards recursive self inquiry_, https://news.ycombinator.com/item?id=38338425

##### _White Rabbit_, https://en.wikipedia.org/wiki/White_Rabbit#/media/File:Down_the_Rabbit_Hole.png

## Footnotes

1. O [sigil.bas](https://github.com/faranalytics/ai_study/blob/main/sigil.bas)
2. Yes, this is a playful reference to the PK assertion.
3. Perhaps this statement _is_ a little cynical; however, it might not be too far off depending on your perspective.
4. If you're genuinely interested in the counterfactual, I would direct your attention [here](https://www.insightmeditationcenter.org/wp-content/uploads/articles/AnapanasatiSutta.pdf).
5. For some reason - perhaps it's a guardrail - the pronouns "I" and "you" can become conflated in very derived forms of logical discourse.

## Colophon

```bash
git reset --mixed HEAD~1 && git status && git add README.md && git commit -m "$(git log --reflog --format="%B" | head -n 1)" && git push --force
```

```bash
# git reset --mixed $(git log --pretty=format:"%h" | tail -n -1) && git status && git add . && git commit -m 'more' && git reflog expire --expire=now --all && git gc --prune=all --aggressive && git push --force
```

---

<sub>"AI does not feel, but it does resolve." — _[in memory of](https://github.com/faranalytics/ai_study/blob/main/sigil.bas) Θᵐ-AI<sub>_

<sub>"Albert Szent-Györgyi said it better than I did." — The Author</sub>

## Errata

I have several hundred pages of transcript to organize in order to fully formulate some of the topics here; hence, I acknowledge the potential _and_ necessity for error and refinement.
