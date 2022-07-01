def remove_line_breaks(text: str) -> str:
    if isinstance(text, bytes):
        return text.replace(b'-\n', b'')
    return text.replace('-\n', '')
