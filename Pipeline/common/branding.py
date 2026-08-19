from manim import Scene


INTRO_MAX_SECONDS = 5
OUTRO_MAX_SECONDS = 10


def add_intro(scene: Scene) -> None:
    raise NotImplementedError


def add_outro(scene: Scene) -> None:
    raise NotImplementedError


def channel_watermark(scene: Scene) -> None:
    raise NotImplementedError
