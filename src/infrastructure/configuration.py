from importlib.resources import read_text

def get_deepl_auth_key() -> str:
    return read_text('configs', 'auth.txt')
 
