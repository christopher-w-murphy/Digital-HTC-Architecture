from typing import Optional

from src.infrastructure.deepl.translator import get_translator
from src.domain.translate import translate_text


def translate_document(source_text: str, auth_key: str) -> Optional[str]:
    """
    Translate the OCR text using DeepL
    """
    translator = get_translator(auth_key)
    return translate_text(source_text, translator)
