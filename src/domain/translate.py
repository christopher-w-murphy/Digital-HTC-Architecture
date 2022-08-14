from typing import Optional

from deepl import Translator, DeepLException


def translate_text(text: str, translator: Translator, source_code: Optional[str] = None, target_code: Optional[str] = None) -> Optional[str]:
    """
    Use DeepL to translate text
    """
    if source_code is None:
        source_code = 'FR'
    if target_code is None:
        target_code = 'EN-GB'
    try:
        response = translator.translate_text(
            text,
            source_lang=source_code,
            target_lang=target_code
        )
        return response.text
    except DeepLException as error:
        print(error)
