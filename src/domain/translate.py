from typing import Optional

from deepl import Translator, DeepLException


def translate_text(text: str, translator: Translator) -> Optional[str]:
    try:
        response = translator.translate_text(
            text,
            source_lang='FR',
            target_lang='EN-GB'
        )
        return response.text
    except DeepLException as error:
        print(error)
