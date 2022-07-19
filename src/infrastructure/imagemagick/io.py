from pathlib import Path
from io import BytesIO
from typing import Optional

from wand.image import Image


class WandContextManager(object):
    def __init__(self, file: BytesIO, resolution: int = 300, output_filepath: Optional[Path] = None):
        self.img = Image(file=file, resolution=resolution)
        self.filepath = output_filepath

    def __enter__(self) -> Image:
        return self.img

    def __exit__(self, ctx_type, ctx_value, ctx_traceback) -> None:
        self.img.close()


def get_temp_path() -> Path:
    temp_path = Path.cwd() / 'temp'
    temp_path.mkdir(exist_ok=True)
    return temp_path


def save_tiff_file(img: Image, filepath: Path) -> None:
    img.save(filename=filepath)
