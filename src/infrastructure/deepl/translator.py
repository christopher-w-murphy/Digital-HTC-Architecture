from deepl import Translator


def get_translator(auth_key: str) -> Translator:
    return Translator(auth_key)
