from pathlib import Path

from PIL import Image


class PillowContextManager(object):
    def __init__(self, filepath: Path):
        self.img = Image.open(filepath)

    def __enter__(self):
        return self.img

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.img.close()
