from pathlib import Path

from wand.image import Image

from src.infrastructure.io import get_tiff_filepath


class WandContextManager(object):
    def __init__(self, filepath: Path, resolution: int = 300):
        self.img = Image(filename=filepath, resolution=300)

    def __enter__(self):
        return self.img

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.img.close()


def save_image(filepath: Path, img: Image) -> None:
    tiff_filename = get_tiff_filepath(filepath)
    img.save(filename=tiff_filename)
