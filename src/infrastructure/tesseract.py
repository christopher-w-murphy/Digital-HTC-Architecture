from pathlib import Path

from PIL import Image
from pytesseract import image_to_string


def ocr(filepath: Path) -> str:
    text_pages = list()
    with Image.open(filepath) as img:
        for page in range(img.n_frames):
            img.seek(page)
            text_page = image_to_string(img, lang='fra')
            text_pages.append(text_page)
    return '\n'.join(text_pages)
