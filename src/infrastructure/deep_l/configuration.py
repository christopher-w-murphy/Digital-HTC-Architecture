from importlib.resources import read_text

import configs

def get_deepl_auth_key() -> str:
    return read_text(configs, 'auth.txt')
