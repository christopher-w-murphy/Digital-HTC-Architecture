from typing import Optional

from PIL import Image
from pytesseract import image_to_string

from src.domain.text_processing import remove_excess_line_breaks


def image_to_ocr_string(img: Image, lang_code: Optional[str] = None) -> str:
    if lang_code is None:
        lang_code = 'fra'

    text_pages = list()
    
    for page in range(img.n_frames):
        img.seek(page)
        text_page = image_to_string(img, lang=lang_code)
        text_pages.append(text_page)
    text = '\n'.join(text_pages)
    return remove_excess_line_breaks(text)
