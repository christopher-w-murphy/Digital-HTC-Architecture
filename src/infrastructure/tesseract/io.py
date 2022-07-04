from io import BytesIO

from PIL import Image


class PillowContextManager(object):
    def __init__(self, bytes_stream: BytesIO):
        self.img = Image.open(bytes_stream)

    def __enter__(self):
        return self.img

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.img.close()
