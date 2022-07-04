from io import BytesIO

from src.infrastructure.imagemagick.io import WandContextManager, save_bytes_as_stream
from src.domain.image_processing import process_image
from src.infrastructure.tesseract.io import PillowContextManager
from src.domain.ocr import image_to_ocr_string


def ocr_document(pdf_file: BytesIO) -> str:
    """
    OCR a PDF yielding a text file with the result
    """

    # Pass an image from Wand to Pillow as a bytes stream
    with BytesIO() as tiff_transfer:

        # Convert a PDF to TIFF and make it easier to OCR
        with WandContextManager(pdf_file) as pdf_img:
            processed_img = process_image(pdf_img)
            save_bytes_as_stream(processed_img, tiff_transfer)

        # Run the Tesseract OCR program to produce a plain text file in French
        with PillowContextManager(tiff_transfer) as tiff_img:
            source_text = image_to_ocr_string(tiff_img)

    return source_text
