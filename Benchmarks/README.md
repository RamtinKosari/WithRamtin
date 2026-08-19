# WithRamtin AstroBench

The benchmark suite for the WithRamtin model. Per STRATEGY.md §4, evaluation is strictly separate from training. The held-out evaluation dataset is never used for training.

## Layout

```
Benchmarks/
├── tasks/        # benchmark tasks per category
├── versions/     # frozen benchmark snapshots (v0.1, v0.2, …)
└── scoring/      # scoring scripts + metric definitions
```

## Categories

Possible benchmark categories (per STRATEGY.md §4):
- astronomy fundamentals
- celestial mechanics
- observational astronomy
- stellar astrophysics
- galactic astronomy
- cosmology
- spectroscopy
- astronomical imaging
- scientific reasoning
- mathematical astronomy
- misconception detection

## Versioning

Each important curriculum milestone freezes a benchmark version with its evaluation results preserved. Before-and-after evaluations live in `versions/<version>/results.json` (or equivalent) and are tracked in git.

## Separation rule

Anything under `Benchmarks/` and `Datasets/eval/` must remain physically and procedurally separate from training data (`Datasets/raw/`, `Datasets/curated/`, training pipelines). A change to the benchmark requires a new version snapshot — never an in-place edit that invalidates prior model evaluations.
