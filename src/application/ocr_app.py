from io import BytesIO
from pathlib import Path
from typing import List, Dict, Optional

from src.infrastructure.imagemagick.io import WandContextManager, save_tiff_file, get_temp_directory
from src.domain.image_processing import process_image
from src.infrastructure.tesseract.io import PillowContextManager, delete_tiff_file
from src.domain.ocr import image_to_ocr_string
from src.application.languages import tesseract_languages


def get_tiff_filepath(filename: str) -> Path:
    file_stem = filename.split('.')[0]
    temp_dir = get_temp_directory()
    return temp_dir / f'{file_stem}.tiff'


def ocr_document(pdf_file: BytesIO, lang_code: Optional[str] = None) -> str:
    """
    OCR a PDF yielding a text file with the result
    """

    tiff_filepath = get_tiff_filepath(pdf_file.name)

    # Convert a PDF to TIFF and make it easier to OCR
    with WandContextManager(pdf_file, output_filepath=tiff_filepath) as pdf_img:
        processed_img = process_image(pdf_img)
        save_tiff_file(processed_img, tiff_filepath)

    # Run the Tesseract OCR program to produce a plain text file in French
    with PillowContextManager(tiff_filepath) as tiff_img:
        source_text = image_to_ocr_string(tiff_img, lang_code)
    delete_tiff_file(tiff_filepath)

    return source_text


def ocr_documents(pdf_files: List[BytesIO], lang_name: Optional[str] = None) -> Dict[str, str]:
    """
    Run OCR on multiple documents
    """
    results = dict()
    lang_code = tesseract_languages.get(lang_name)

    for pdf_file in pdf_files:
        if pdf_file is not None:
            source_text = ocr_document(pdf_file, lang_code)

            file_stem = pdf_file.name.split('.')[0]
            results[file_stem + '_OCR.txt'] = source_text

    return results
