from src.infrastructure.cli import construct_parser
from src.infrastructure.configuration import get_deepl_auth_key
from src.infrastructure.deepl import translate_document


def text_file_with_extension(text_file: str) -> str:
    if not text_file.endswith('.txt'):
        return text_file + '.txt'
    return text_file


def main() -> None:
    parser = construct_parser()
    args = parser.parse_args()
    input_file = text_file_with_extension(args.input_path)
    output_file = text_file_with_extension(args.output_path)

    auth_key = get_deepl_auth_key()

    translate_document(input_file, output_file, auth_key)


if __name__ == '__main__':
    main()
