# Datasets

Training data candidates derived from episodes and curriculum material. Per STRATEGY.md §3 and §4, evaluation data is strictly separated from training data.

## Layout

```
Datasets/
├── raw/         # source material, possibly large — gitignored
├── curated/     # cleaned, structured training candidates — gitignored
└── eval/        # held-out evaluation data — TRACKED, versioned
```

## Rules

- `raw/` and `curated/` are gitignored because they may be large and are rebuildable from sources.
- `eval/` is intentionally tracked. It is the held-out benchmark source-of-truth and must remain stable across model versions. Changes go through the `Benchmarks/versions/` snapshot flow.
- Video scripts are **not** copied directly into training data. Instead, the underlying concepts are transformed into structured examples (definitions, derivations, worked examples, misconception corrections, etc.) per STRATEGY.md §3.
