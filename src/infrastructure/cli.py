from argparse import ArgumentParser


def construct_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument('input_pdf_path', help='The path to the PDF to OCR and translate.', type=str)
    return parser
