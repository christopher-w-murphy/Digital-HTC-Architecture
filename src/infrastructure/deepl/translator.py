from deepl import Translator

from src.infrastructure.deepl.configuration import get_deepl_auth_key


def get_translator(auth_key: str) -> Translator:
    return Translator(auth_key)
