from wand.image import Image


def process_image(img: Image) -> Image:
    """
    Convert PDF to TIFF and make it easier to OCR
    """
    img.format = 'tiff'
    img.depth = 8
    img.strip()
    img.background_color = 'white'
    img.alpha_channel = 'off'
    return img
