# Curriculum

The open astronomy curriculum that anchors the channel and the WithRamtin AstroBench. Per STRATEGY.md §3, the curriculum is the core artifact: it serves both human learners and ML evaluation, and stays useful across generations of models.

## Layout

```
Curriculum/
├── dependency_graph.json     # concept → prerequisites → dependents
├── concepts/                 # one file per concept
├── examples/                 # by category (definitions, derivations, problems, …)
├── misconceptions/           # catalog of common misconceptions + corrections
└── levels/                   # multi-level explanations (child / high-school / undergrad / advanced)
```

## Concept dependency graph

`dependency_graph.json` is the spine of the curriculum. Each concept declares:
- prerequisites
- dependents
- related concepts
- common misconceptions

Example chain from STRATEGY.md:
`Celestial Sphere → Coordinate Systems → Parallax → Distance Ladder → Cepheids → Type Ia Supernovae → Hubble Expansion`

## Multi-level explanations

Per STRATEGY.md, concepts are represented at multiple difficulty levels. The `levels/` folder carries the per-level explanations so that the same concept can be assessed at different depths.

## Source of structured examples

Episodes generate structured training examples from the curriculum, not from raw script text. Example categories live under `examples/` and include definitions, derivations, worked examples, astronomy applications, misconception correction, and reasoning problems.

See STRATEGY.md §3 for the full set of example categories and the Episode → Dataset → Benchmark → Model pipeline.
