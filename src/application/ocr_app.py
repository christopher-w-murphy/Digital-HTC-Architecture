from io import BytesIO
from pathlib import Path

from src.infrastructure.imagemagick.io import WandContextManager, save_tiff_file, get_temp_path
from src.domain.image_processing import process_image
from src.infrastructure.tesseract.io import PillowContextManager, delete_tiff_file
from src.domain.ocr import image_to_ocr_string


def get_tiff_filepath(filename: str) -> Path:
    file_stem = filename.split('.')[0]
    temp_path = get_temp_path()
    return temp_path / f'{file_stem}.tiff'


def ocr_document(pdf_file: BytesIO) -> str:
    """
    OCR a PDF yielding a text file with the result
    """

    tiff_filepath = get_tiff_filepath(pdf_file.name)

    # Convert a PDF to TIFF and make it easier to OCR
    with WandContextManager(pdf_file, output_filepath=tiff_filepath) as pdf_img:
        processed_img = process_image(pdf_img)
        # save to disk to avoid using the Python shelve library
        save_tiff_file(processed_img, tiff_filepath)

    # Run the Tesseract OCR program to produce a plain text file in French
    with PillowContextManager(tiff_filepath) as tiff_img:
        source_text = image_to_ocr_string(tiff_img)
    # delete tiff file as they tend to be large
    delete_tiff_file(tiff_filepath)

    return source_text
