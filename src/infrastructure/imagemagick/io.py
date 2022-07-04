from io import BytesIO

from wand.image import Image


class WandContextManager(object):
    def __init__(self, file, resolution: int = 300):
        self.img = Image(file=file, resolution=resolution)

    def __enter__(self):
        return self.img

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.img.close()


def save_bytes_as_stream(img: Image, stream: BytesIO) -> None:
    img.save(stream)
