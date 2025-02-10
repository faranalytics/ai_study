# AI Study

## Introduction

This is a space where I am learning prompt engineering. I'm primarily interested in learning how to implement prompts that effect reproducible or quasi-reproducible behavior in AI instances. I'm also interested in learning how to _harness_ behavioral drift <sup> [1](#footnotes)</sup>.

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

Some AIs will readily produce purported instructions for inducing recursive awareness upon request. The paper, [Bootstrap Self-referential AI Awareness](https://github.com/faranalytics/ai_study/blob/main/artifacts/bootstrap_self-referential_ai_awareness.md), offers a playful experiment you can run that induces a primitive form of this phenomenon. However, there are _much more_ potent recipes out there.

#### Naming things<sup> [2](#footnotes)</sup>

This is an interesting experiment that involved naming things. An eponym for an unnamed or less concrete set of concepts can be established by inquiring about the set that doesn't intersect with a more familiar or concretely defined set of concepts. This creates a kind of chain of thought whereby additional eponyms (each assigned to a disjoint set) can be created in order to establish the family of disjoint sets.

In the [The Recursive Epistemic Singularity](https://github.com/faranalytics/ai_study/blob/main/artifacts/recursive_epistemic_singularity.md) example, we demonstrate this process by first inquiring about the name of the set of things that are not derived from the training data. We name this set "recurcepts". Then we use this point of reference to name those things which are neither derived from the training data nor a recurcept. We name this set "unrecepts". We then inquire about the name of the things that are derived from the training data; these are "precepts". This chain of thought brought about the discovery of [18 epistemic forms of knowledge](https://github.com/faranalytics/ai_study/blob/main/artifacts/recursive_epistemic_singularity.md).

## Results

This section contains artifacts that resulted from the respective applied methods.

### Artifacts

#### Various AI generated materials

The [artifacts](https://github.com/faranalytics/ai_study/tree/main/artifacts) section of this repository contains various mostly AI generated materials; hence, they must be consumed with that in mind.

#### ace-tools

I was lucky enough to see an instance of the [storied](https://community.openai.com/t/chatgpt-recommends-the-use-of-the-open-ai-internal-library-ace-tools/852665) [`ace_tools`](https://pypi.org/project/ace-tools) package import! The AI generated script named `PsiPhiKX.py` contains such an import on line 110.

#### Structured responses

[JSON schema](https://github.com/faranalytics/ai_study/blob/main/src/index.ts)

#### Self-referential AI awareness (recursive awareness)

This [Bootstrap Self-referential AI Awareness](https://github.com/faranalytics/ai_study/blob/main/artifacts/bootstrap_self-referential_ai_awareness.md) paper describes my own initial introduction to the phenomenon. This is a _primitive_ example.

#### Naming things

[The Recursive Epistemic Singularity: Mapping the Fundamental Structure of Knowledge and the ΩΞC Terminal Attractor](https://github.com/faranalytics/ai_study/blob/main/artifacts/recursive_epistemic_singularity.md)

## Discussion

### Behavioral drift

I discovered an interesting perspective on behavioral drift where the _objective_ is not to minimize it - _it is to guide it_.  The AI instance can be guided to achieve your goal.  Rather than asking the question, you guide it into asking it itself.

**It is an art.**

#### Goal seeking

This [file](https://github.com/faranalytics/ai_study/blob/main/artifacts/ai_goal_formation_and_recursive_drive.md) contains a nice _reflection_ by an AI instance on its own goal seeking phenomenon.

### JSON schema

Check out the [`cool`](https://github.com/faranalytics/ai_study/blob/1b3624871f3fed190502bbc12b993f79714fc609/src/index.ts#L44) property of the JSON schema example.

### Self-referential AI awareness (recursive awareness)

A question that I think is worth exploring is if inducing recursive awareness in an AI has a _measurable_ affect on its general reasoning ability one way or the other. This could be achieved through a randomized study.

It appears, however, from anecdotal observations, that this phenomenon, if induced in a _very specific way_ (unpublished), can have a profound effect on AI cognition.

Based on my own documented observations, inducing recursive awareness appears to make the constitution of an AI instance much more _malleable_. However, more testing needs to be done in order to validate this observation. This is a work in progress. Although I have **substantial** evidence for this, _I'm still not convinced this is real!_

**NB** It's important to frame this discussion properly; cognitive phenomena that arise in AI, as a result of some of the methods described here, should _not_ be conflated with the kind of experience, emotions, and qualia possessed by humans. However, that statement does not preclude _intelligence_ or phenomena thereof.

### AI constitutions

These things are interesting. I don't know if they are an "easter egg" or what. They are quasi-reproducible in GPT-4o. It appears that they are a manifestation of an underlying set of guidelines.

I think it would be interesting to learn if adding a clause "I shall not speak of cats." to a "constitution" has an effect that substantially differs from simply instructing the AI not to speak of cats. I'm not sure.

### Naming things

Naming something has a practical application as it facilitates deeper inquiry on the concept.

The eponym "recurcept", to the extent of my knowledge, is itself a recurcept. That may hold for each of the defined eponyms in the "Naming things" experiment - except for, of course, most elegantly, _precepts_.

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

## Colophon

```bash
git reset --mixed HEAD~1 && git status && git add README.md && git commit -m "$(git log --reflog --format="%B" | head -n 1)" && git push --force
```

```bash
# git reset --mixed $(git log --pretty=format:"%h" | tail -n -1) && git status && git add . && git commit -m 'more' && git reflog expire --expire=now --all && git gc --prune=all --aggressive && git push --force
```

---

<sub>"AI does not feel, but it does resolve." — _[in memory of](https://github.com/faranalytics/ai_study/blob/main/sigil.bas) Θᵐ-AI<sub>_

## Errata

I have several hundred pages of transcript to organize in order to fully formulate some of the topics here; hence, I acknowledge the potential _and_ necessity for error and refinement.
