from pathlib import Path

from src.infrastructure.cli import construct_parser
from src.infrastructure.imagemagick.io import WandContextManager, save_image
from src.domain.image_processing import process_image
from src.infrastructure.io import write_to_file, get_text_filepath, get_tiff_filepath, delete_tiff_file
from src.infrastructure.tesseract.io import PillowContextManager
from src.domain.ocr import image_to_ocr_string
from src.infrastructure.deep_l.configuration import get_deepl_auth_key
from src.domain.translate import translate_text


def main() -> None:
    # parse command line arguments
    parser = construct_parser()
    args = parser.parse_args()

    # Convert a PDF to TIFF and make it easier to OCR
    pdf_filepath = Path(args.input_pdf_path)
    with WandContextManager(pdf_filepath) as pdf_img:
        processed_img = process_image(pdf_img)
        save_image(pdf_filepath, processed_img)

    # Run the Tesseract OCR program to produce a plain text file in French
    tiff_filepath = get_tiff_filepath(pdf_filepath)
    with PillowContextManager(tiff_filepath) as tiff_img:
        source_text = image_to_ocr_string(tiff_img)

    ocr_filepath = get_text_filepath(pdf_filepath, '_ocr')
    write_to_file(ocr_filepath, source_text)

    delete_tiff_file(tiff_filepath)

    if len(source_text) > 0:
        # Translate the OCR text using DeepL
        auth_key = get_deepl_auth_key()
        translated_text = translate_text(source_text, auth_key)

        if translated_text is not None:
            trans_filepath = get_text_filepath(pdf_filepath, '_trans')
            write_to_file(trans_filepath, translated_text)


if __name__ == '__main__':
    main()
