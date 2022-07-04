from typing import Tuple, Optional, Dict, List
from io import BytesIO

from src.application.ocr_app import ocr_document
from src.application.translation_app import translate_document


def ocr_and_translate_document(pdf_file: BytesIO, auth_key: str) -> Tuple[str, Optional[str]]:
    """
    OCR and Translate a PDF Document
    """

    source_text = ocr_document(pdf_file)

    if len(source_text) > 0:
        translated_text = translate_document(source_text, auth_key)
        if translated_text is not None:
            return source_text, translated_text

    return source_text, None


def ocr_and_translate_documents(pdf_files: List[BytesIO], auth_key: str) -> Dict[str, str]:
    """
    Run OCR and Translation on multiple documents
    """
    results = dict()

    for pdf_file in pdf_files:
        if pdf_file is not None:
            source_text, translated_text = ocr_and_translate_document(pdf_file, auth_key)

            file_stem = pdf_file.name.split('.')[0]
            results[file_stem + '_OCR.txt'] = source_text
            if translated_text is not None:
                results[file_stem + '_translated.txt'] = translated_text

    return results
