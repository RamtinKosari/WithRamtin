# Pipeline

Production code for the channel. Manim scenes, TTS service, branding, and per-format templates.

## Layout

```
Pipeline/
├── pyproject.toml            # deps (manim, dev tooling)
├── manim.cfg                 # long-form defaults (1920×1080, 30fps)
├── manim.short.cfg           # short-form override (1080×1920, -ql)
├── common/                   # shared branding, palette, fonts, voice
│   ├── branding.py           # channel intro ≤ 5 s, outro ≤ 10 s
│   ├── palette.py            # shared color constants
│   ├── fonts.py              # shared font references
│   └── voice/                # TTS service (Kokoro). .tts_cache/ at repo root.
├── long_form/                # shared long-form scene blocks
└── shorts/                   # per-format templates (mirror Contents/Shorts/)
```

## Rendering

**Long-form** (1920×1080, 30 FPS):
```bash
manim -qm scene_*.py
```

**Shorts** (1080×1920, low quality for fast turnaround):
```bash
manim --config manim.short.cfg -ql scene_*.py
```

The voice service caches generated clips in `.tts_cache/` at the repo root (gitignored).

## Conventions

- One beat of narration = one `with self.voiceover(...)` block, one visual.
- Long-form scripts and scenes live under `Contents/Long-form/episodes/<date-slug>/`.
- Short-form scripts and scenes live under the matching `Contents/Shorts/<format>/<date-slug>/`.
- Reusable scene blocks (intro, outro, transitions, common diagrams) live here under `common/` and `long_form/`.
