from argparse import ArgumentParser


def construct_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument('input_path')
    parser.add_argument('output_path')
    return parser
