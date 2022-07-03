from pathlib import Path

from src.infrastructure.cli import construct_parser
from src.infrastructure.imagemagick import process_image, get_tiff_filepath, delete_tiff_file
from src.infrastructure.tesseract import ocr
from src.domain.text_processing import remove_line_breaks
from src.infrastructure.io import write_to_file, get_text_filepath
from src.infrastructure.configuration import get_deepl_auth_key
from src.infrastructure.deep_l import translate_text


def main() -> None:
    # parse command line arguments
    parser = construct_parser()
    args = parser.parse_args()

    # Convert a PDF to TIFF and make it easier to OCR
    pdf_filepath = Path(args.input_pdf_path)
    process_image(pdf_filepath)

    # Run the Tesseract OCR program to produce a plain text file in French
    tiff_filepath = get_tiff_filepath(pdf_filepath)
    source_text = ocr(tiff_filepath)
    source_text = remove_line_breaks(source_text)

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
