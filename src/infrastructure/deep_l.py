from deepl import Translator, DeepLException


def translate_text(text: str, auth_key: str) -> None:
    translator = Translator(auth_key)
    try:
        translator.translate_text(
            text,
            source_lang='FR',
            target_lang='EN-GB',
            split_sentences='off'
        )
    except DeepLException as error:
        print(error)
