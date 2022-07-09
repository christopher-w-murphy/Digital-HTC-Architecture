from pathlib import Path

from PIL import Image


class PillowContextManager(object):
    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.img = Image.open(self.filepath)

    def __enter__(self) -> Image:
        return self.img

    def __exit__(self, ctx_type, ctx_value, ctx_traceback) -> None:
        self.img.close()


def delete_tiff_file(filepath: Path) -> None:
    filepath.unlink(missing_ok=True)
