# Channel Strategy
Why this channel exists, who it serves, and what **winning** looks like.

## Mission
> Explore the universe through astrophysics, machine learning, and visual storytelling. Every episode aims to transform difficult concepts into insights that feel inevitable in hindsight.

## Content Scope
The channel focuses on understanding the universe while also exploring the mathematics, computation, artificial intelligence, and scientific methods used to study it. Long-form videos are built around two primary pillars:

1. **Astronomy & Astrophysics:** Intuition-first explorations of the universe, from planetary systems and stellar evolution to black holes, galaxies, and cosmology. Concepts are built from first principles using visual explanations, simulations, and scientific reasoning.
2. **Computational Astrophysics & AI:** The methods that enable modern astronomical discovery. Physics drives the questions, computation provides the tools. Topics include Bayesian inference, scientific computing, machine learning, and generative models, with an emphasis on understanding both the underlying mathematics and their real-world applications in astronomy. Example topics:
   - **Markov Chain Monte Carlo (MCMC)** for parameter estimation in cosmology, exoplanet characterization, and astrophysical model fitting.
   - **Diffusion and score-based generative models** for realistic galaxy image synthesis and astronomical data augmentation.
   - **Simulation-Based Inference (SBI)**, **Neural Posterior Estimation (NPE)**, **Normalizing Flows**, and other modern techniques used when traditional likelihood-based methods become impractical.
   - **Machine learning for astronomy**, including source classification, anomaly detection, time-series analysis, and large-scale survey science.

Both pillars share the same standard: rigorous, narrated, animated from scratch. The CS / AI pillar is never ***"here's a paper summary"*** — it is ***"here is the idea, here is the math intuition, here is what it produces on real data"***.

## Scientific Teaching Philosophy
WithRamtin teaches difficult concepts through :
* intuition
* visualization
* animation
* mathematical reasoning
* physical reasoning
* examples
* simulations
* real astronomical applications

The goal is not to remove mathematical rigor. The goal is to make the mathematics and physics **understandable and motivated**.

---

## Audience
We serve curious viewers who want understanding, not oversimplification. The channel is designed to make complex ideas intuitive while preserving scientific rigor. Segments, in priority order:

1. **Curious learners** who are fascinated by astronomy, astrophysics, space exploration, artificial intelligence, and scientific discovery. They want explanations that build intuition rather than assume advanced mathematics.
2. **High-school, undergraduate, and graduate students** in physics, astronomy, computer science, data science, and related fields who use the videos to develop intuition before diving into formal coursework and research.
3. **Researchers, educators, and science communicators** who appreciate clear visual explanations of astrophysical concepts, computational methods, and modern AI techniques.
4. **Aspiring scientists, Olympiad students, and self-learners** looking to explore topics beyond a standard classroom curriculum.

The vocabulary, pacing, and depth assume a motivated audience with a curiosity for science and a willingness to engage with challenging ideas.

## Voice Strategy
WithRamtin is not restricted to a single permanent voice. The channel develops a **consistent audio identity with multiple carefully selected voices**. Different voices may be associated with different scientific domains or recurring roles (e.g. Cosmology, Astrophysics, Spherical Astronomy, Machine Learning). The exact mapping between voices and domains is kept flexible and is chosen based on what best serves the content. Both male and female voices may be used. The governing principle is :

> **One recognizable WithRamtin audio identity, multiple voices when they improve storytelling or comprehension.**

> [!NOTE]
> Episodes may use several voices interacting with each other, such as :
> * a student asks questions, challenges assumptions, or makes mistakes while a professor guides the reasoning
> * an observer that appears with a new or unexpected observation, reporting what was detected without knowing why it happened.
> * two scientists debate a competing explanation, each presenting evidence for their interpretation until an experiment, calculation, or observation reveals which explanation holds up.

---

## Video Format
Operational specifications for production.

### Long-form
* **Length:** 3–15 minutes per video. Sweet spot 4–9 min.
* **Pacing:** `one beat = one visual`. A beat is one line of narration wrapped in a `with self.voiceover(...)` block.
* **Aspect:** 1920×1080, 30 FPS, see `manim.cfg`.
* **Branding:** Channel intro ≤ 5 s, outro ≤ 10 s. See `common/branding.py`.

### Shorts
* **Length:** ≤ 2 minutes. Tight script, no setup, no recap, no outro.
* **Aspect:** 1080×1920. Same palette and fonts as long-form.
* **Branding:** Channel watermark only, no intro/outro animation.

## Publishing Cadence
Two parallel tracks. Both ship on a fixed schedule so subscribers know what to expect.

* ### Long-form
  * **Pilot month (after the foundation is done) :** 1 video, shipped, measured. Don't optimize before measuring.
  * **Steady state target :** 1 video per 2 weeks. One weekend to write the script, one weekend to animate + render.

* ### Shorts
  Shorts follow an independent rhythm from the long-form curriculum. Six recurring formats:

  - **One Question About the Universe** (weekly) : A single conceptual question, answered with one animation and ~60 s of narration. Everyday astronomy that viewers can observe or reason about themselves.
    > * *When exactly does the Sun rise today at my latitude?*
    > * *How long is a day on Earth — and why is it 24 hours, not 23 h 56 min?*
    > * *What time is solar noon right now, and why is it rarely 12:00 on your wall clock?*
    > * *Why does the Moon sometimes rise 50 minutes later than yesterday?*

  - **Cosmic Profile** (weekly) : One specific celestial object explored in ~60 s — a star, galaxy, nebula, black hole, planet, moon, comet, asteroid, exoplanet, spacecraft, or probe. The audience leaves knowing one concrete and interesting thing about it.

  - **Think Like a Physicist** (weekly) : One problem, puzzle, thought experiment, or estimation challenge solved on-screen, beat by beat. May include Olympiad problems, astronomical estimation, counterintuitive scenarios, or historical reconstruction puzzles.

  - **Concept Burst** : One established concept explained clearly in 30–45 s, focusing on a single piece of intuition, equation, or physical idea.

  - **Science Brief** : A short reaction to a new discovery, paper, observation, or development in astronomy, astrophysics, or AI-for-astronomy. The goal is explanation and context, not simply reporting the news.

  - **Long-Form Teaser** : A 15–30 s clip, question, or trailer connected to an upcoming long-form episode, published 3–7 days before release.

  **Seed relationship.** A short that opens a deep question may later seed a long-form episode on the same topic : the short plants the question, the long-form develops it. A sustainable monthly rhythm :

  | Week |    Type    | Format |
  |------|------------|--------|
  |  1   | Short-form | One Question About the Universe |
  |  1   | Short-form | Cosmic Profile                  |
  |  1   | Short-form | Think Like a Physicist          |
  |  1   | Long-form  | Topic                           |
  |  2   | Short-form | Concept Burst                   |
  |  2   | Short-form | Science Brief                   |
  |  2   | Short-form | Long-form Teaser                |
  |  3   | Short-form | One Question About the Universe |
  |  3   | Short-form | Cosmic Profile                  |
  |  3   | Short-form | Think Like a Physicist          |
  |  3   | Long-form  | Topic                           |
  |  4   | Short-form | Concept Burst                   |
  |  4   | Short-form | Science Brief                   |
  |  4   | Short-form | Long-form Teaser                |

---

## The WithRamtin Model Curriculum

A major long-term direction of the project is the development of an open astronomy curriculum that simultaneously serves two audiences:

1. Human learners.
2. Machine learning systems.

The primary goal is **not** to create a chatbot. The primary goal is to build a structured astronomy curriculum that can be used to teach humans, evaluate models, and investigate curriculum-based learning in language models.

Language models are treated as experimental learners operating within the curriculum. As the project evolves, different models may be evaluated, adapted, fine-tuned, or replaced. The curriculum itself remains the core artifact. Conceptually, the project evolves through the following progression :

**Base Model → Astronomy Curriculum → Evaluation Benchmarks → Model Experiments**

Existing open models such as Gemma, Qwen, Llama, Mistral, or astronomy-specialized models may be used as experimental baselines. No single model family is assumed to be permanent. The "student → expert" framing occasionally used by the project is a pedagogical metaphor. It is **not** a claim that a model possesses human-like understanding.

## Curriculum-First Philosophy

The project treats the curriculum as more important than any individual model checkpoint. Models will change over time. Architectures, parameter counts, and training methods will evolve. A carefully designed astronomy curriculum and benchmark suite can remain useful across generations of models.The project therefore prioritizes the creation of :

* structured astronomy knowledge
* learning objectives
* prerequisite relationships
* exercises
* misconceptions
* evaluation benchmarks
* curriculum datasets

Model training is considered a downstream application of these resources.

## Episode → Dataset → Benchmark → Model Pipeline

Each major educational episode is intended to produce multiple outputs :

1. A high-quality educational experience for humans.
2. Structured curriculum material.
3. Training data candidates.
4. Evaluation data candidates.
5. Benchmark updates.

The conceptual pipeline is :

**Scientific Research → Episode Development → Educational Content → Structured Knowledge → Curriculum Assets → Training Dataset → Evaluation Dataset → Model Experiments → Benchmark Results**

The video script itself should **not** be copied directly into a training dataset. Instead, the underlying concepts are transformed into structured educational examples. Possible example categories include :

* definitions
* physical intuition
* mathematical relationships
* derivations
* worked examples
* astronomy applications
* misconception correction
* conceptual questions
* mathematical questions
* reasoning problems
* application problems
* comparisons
* edge cases
* observational scenarios
* historical context
* scientific interpretation tasks

A single episode may generate many structured examples covering different perspectives of the same concept.

## Multi-Level Educational Examples

Concepts should be represented at multiple levels of difficulty.

Examples may include :

* explanation for a child
* explanation for a high-school student
* explanation for an undergraduate
* explanation for an advanced astrophysics student

The objective is not merely factual recall but the ability to communicate scientific ideas across different educational levels.

## Socratic and Guided Reasoning

The curriculum may include guided reasoning examples in addition to direct question-answer pairs. Example structure :

**Question → Hint 1 → Hint 2 → Hint 3 → Solution**

These examples encourage step-by-step reasoning and support educational use cases where learners discover answers progressively rather than receiving them immediately.

## Concept Dependency Graph

The curriculum is treated as a connected knowledge graph rather than a collection of isolated lessons. Topics should define :

* prerequisites
* dependent concepts
* related concepts
* common misconceptions

Example :

**Celestial Sphere → Coordinate Systems → Parallax → Distance Ladder → Cepheids → Type Ia Supernovae → Hubble Expansion**

This dependency structure helps both curriculum design and model evaluation.

## Evaluation Must Be Separate

The project maintains a **held-out evaluation dataset** that is never used for training. Evaluation is performed using benchmark tasks rather than subjective chatbot impressions. Possible evaluation categories include :

* conceptual understanding
* mathematical reasoning
* physical interpretation
* problem solving
* misconception detection
* astronomy applications
* scientific explanation
* transfer learning
* prerequisite understanding
* novel or unseen scenarios

Claims that a model has "learned" a topic are treated as measurable benchmark outcomes rather than subjective observations. Before-and-after evaluations should be preserved at important curriculum milestones.

## WithRamtin AstroBench

A long-term objective is the development of an astronomy benchmark suite tentatively referred to as :

**WithRamtin AstroBench**

The benchmark is intended to provide objective measurement across astronomy and astrophysics topics. Potential benchmark categories include :

* astronomy fundamentals
* celestial mechanics
* observational astronomy
* stellar astrophysics
* galactic astronomy
* cosmology
* spectroscopy
* astronomical imaging
* scientific reasoning
* mathematical astronomy
* misconception detection

The benchmark remains strictly separated from training data.

## Continual Learning Research

A major research question of the project is :

**Can astronomy knowledge be acquired through a curriculum without catastrophic forgetting?**

Sequential fine-tuning is not assumed to be the correct solution. Possible strategies include :

* sequential fine-tuning
* LoRA
* QLoRA
* replay-based training
* curriculum consolidation
* modular adapters
* retrieval-augmented systems
* hybrid approaches
* periodic retraining from accumulated curriculum data

A central concern is **catastrophic forgetting**: whether learning new concepts causes measurable degradation on previously learned concepts. Performance should be tracked throughout the curriculum rather than only at the final stage.

## Model Architecture Direction

The project remains architecture-agnostic. Potential experimental starting points include :

* Gemma
* Qwen
* Llama
* Mistral
* astronomy-specialized models
* future open models

For local experimentation, smaller models such as **Gemma 3 4B** may provide a practical starting point. Larger models may be evaluated as resources permit. The project distinguishes clearly between :

* base models
* continued-pretraining checkpoints
* instruction-tuned models
* training checkpoints
* deployment models
* LoRA adapters
* QLoRA adapters
* retrieval-augmented systems

Ollama may be used for local inference and testing, but it is not considered the training framework. Architecture decisions are treated as empirical questions and may change as evidence accumulates.

## Long-Term Vision

The long-term objective is not merely the creation of a specialized astronomy model. The larger goal is to develop :

* an open astronomy curriculum
* a structured astronomy knowledge base
* a reusable astronomy benchmark suite
* reproducible model evaluation procedures
* curriculum-based continual learning experiments

The resulting models are valuable outputs of the project, but the curriculum, benchmark, and scientific methodology are considered the primary long-term assets.

## Model Versioning
The model evolves through explicit versions such as :

* `Arp148-v0.1`
* `Arp148-v0.2`
* `Arp148-v1.0`

Each important version records :

* base model
* training data
* concepts included
* training method
* adapter / checkpoint information
* evaluation dataset version
* evaluation results
* known limitations

The exact naming scheme may be adjusted to match existing project conventions.

## Research Potential
The model curriculum is not a supporting feature for the YouTube channel. It is intended to mature into a legitimate ML/AI research direction in its own right. Potential research questions include :

* Can a structured scientific curriculum improve domain adaptation?
* Does the ordering of concepts affect model learning?
* How much does high-quality pedagogical data matter compared with raw domain data?
* How severe is catastrophic forgetting during sequential astronomy training?
* Can replay or modular adapters preserve previous knowledge?
* How does curriculum-based adaptation compare with retrieval-augmented approaches?
* How does the approach behave across different model sizes?
* Can model performance be tracked quantitatively as the curriculum grows?

Enough experimental data, versions, benchmarks, and methodology are preserved that the work could eventually support a scientific paper.

## Long-Term Vision
The long-term vision is for WithRamtin to become more than an astronomy education channel. It combines :

* Scientific storytelling
* Astrophysics
* AI / Machine Learning
* Scientific computing
* Open model development
* Curriculum-based learning research

The human audience learns about the universe through the videos while the WithRamtin model progressively learns the same scientific concepts through a structured, measurable curriculum. This is not a gimmick. It is treated as a serious long-term technical and research direction.