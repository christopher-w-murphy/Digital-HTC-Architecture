from typing import Optional, List, Dict
from io import BytesIO, StringIO

from src.infrastructure.deepl.translator import get_translator
from src.domain.translate import translate_text
from src.application.languages import deepl_source_languages, deepl_target_languages


def translate_document(
    source_text: str,
    auth_key: str,
    source_code: Optional[str] = None,
    target_code: Optional[str] = None
) -> Optional[str]:
    """
    Translate the OCR text using DeepL
    """
    translator = get_translator(auth_key)
    return translate_text(source_text, translator, source_code, target_code)


def stream_to_str(txt_file: BytesIO) -> str:
    stringio = StringIO(txt_file.getvalue().decode("utf-8"))
    return stringio.read()


def translate_documents(
    txt_files: List[BytesIO],
    auth_key: str,
    source_name: Optional[str] = None,
    target_name: Optional[str] = None
) -> Optional[Dict[str, str]]:
    """
    Translate multiple documents
    """
    results = dict()
    source_lang_code = deepl_source_languages.get(source_name)
    target_lang_code = deepl_target_languages.get(target_name)

    for txt_file in txt_files:
        if txt_file is not None:
            source_text = stream_to_str(txt_file)

            translated_text = translate_document(source_text, auth_key, source_lang_code, target_lang_code)

            if translated_text is not None:
                file_stem = txt_file.name.split('.')[0]
                results[file_stem + '_translated.txt'] = translated_text

    if len(results) > 0:
        return results
