# Models

Model artifacts and metadata for the WithRamtin model lineage. Per STRATEGY.md §6.

## Layout

```
Models/
├── versions/        # Arp148-v0.1, Arp148-v0.2, … each with a model card
└── eval_results/    # per-version evaluation outputs (tracked)
```

## Versioning

Versions follow the scheme `Arp148-vMAJOR.MINOR` (or whatever matches existing project convention). Each version records:
- base model
- training data version
- concepts included
- training method
- adapter / checkpoint information
- evaluation dataset version
- evaluation results
- known limitations

## Storage

Weights themselves (`*.safetensors`, `*.bin`, `*.gguf`, `*.pt`, `*.pth`, `*.ckpt`) are gitignored per `.gitignore`. Use Git LFS or external storage (HuggingFace Hub, etc.) for the actual files; track only the model card and metadata here.

## Separation

Evaluation results in `eval_results/` are tracked. They are the evidence base for any claim that a model has learned a topic, and they must remain reproducible across benchmark versions.
