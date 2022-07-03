from deepl import Translator

from src.infrastructure.deep_l.configuration import get_deepl_auth_key


def get_translator() -> Translator:
    auth_key = get_deepl_auth_key()
    return Translator(auth_key)
