def text_file_with_extension(text_file: str) -> str:
    if not text_file.endswith('.txt'):
        return text_file + '.txt'
    return text_file


def read_from_file(input_file: str) -> str:
    file_name = text_file_with_extension(input_file)

    with open(file_name, 'rb') as f:
        text = f.read()
    return text


def write_to_file(output_file: str, text: str) -> None:
    file_name = text_file_with_extension(output_file)
    
    with open(file_name, 'wb') as f:
        f.write(text)
