from src.infrastructure.cli import construct_parser
from src.infrastructure.configuration import get_deepl_auth_key
from src.infrastructure.deep_l import translate_text
from src.infrastructure.io import read_from_file, write_to_file
from src.domain.text_processing import remove_line_breaks


def main() -> None:
    parser = construct_parser()
    args = parser.parse_args()

    auth_key = get_deepl_auth_key()

    source_text = read_from_file(args.input_path)
    source_text = remove_line_breaks(source_text)
    
    translated_text = translate_text(source_text, auth_key)
    write_to_file(args.output_path, translated_text)


if __name__ == '__main__':
    main()
