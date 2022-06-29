from src.infrastructure.cli import construct_parser
from src.infrastructure.configuration import get_deepl_auth_key
from src.domain.translate import translate_document


def main():
    parser = construct_parser()
    args = parser.parse_args()

    auth_key = get_deepl_auth_key()

    translate_document(args.input_path, args.output_path, auth_key)


if __name__ == '__main__':
    main()
