from typing import Union

def remove_line_breaks(text: Union[str, bytes]) -> Union[str, bytes]:
    if isinstance(text, bytes):
        return text.replace(b'-\n', b'')
    return text.replace('-\n', '')
