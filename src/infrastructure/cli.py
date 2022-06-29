from argparse import ArgumentParser


def construct_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument('input_path', help='The name of the OCR file.', type=str)
    parser.add_argument('output_path', help='The name of the translated file.', type=str)
    return parser
