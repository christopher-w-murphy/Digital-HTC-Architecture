from typing import Union


def remove_excess_line_breaks(text: Union[str, bytes]) -> Union[str, bytes]:
    """
    Tesseract adds extra line breaks that affect translation
    """
    if isinstance(text, bytes):
        return _remove_line_breaks_bytes(text)
    return _remove_line_breaks_str(text)


def _remove_line_breaks_str(text: str) -> str:
    """
    Process line breaks in strings
    """
    # unwrap words that went onto the next line
    text = text.replace('-\n', '')
    # split into paragraphs, note two new lines from Tesseract
    text_list = text.split('\n\n')
    # replace new lines within a paragraph with spaces
    text_list = [line.replace('\n', ' ') for line in text_list if len(line) > 0]
    # join the paragraphs back together with one new line and indent new paragraphs
    return '\n\t'.join(text_list)


def _remove_line_breaks_bytes(text: bytes) -> bytes:
    """
    Process line breaks in bytes (encoded strings)
    """
    text = text.replace(b'-\n', b'')
    text_list = text.split(b'\n\n')
    text_list = [line.replace(b'\n', b' ') for line in text_list if len(line) > 0]
    return b'\n\t'.join(text_list)
