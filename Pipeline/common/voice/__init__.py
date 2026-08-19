from pathlib import Path


CACHE_DIR = Path(".tts_cache")


def synth(text: str, *, voice: str, out_path: Path) -> Path:
    raise NotImplementedError
