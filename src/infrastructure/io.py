from pathlib import Path


def write_to_file(output_path: Path, text: str) -> None:
    with Path(output_path) as p:
        p.write_text(text, encoding='utf-8')


def get_text_filepath(filepath: Path, stem_extension: str) -> Path:
    new_stem = filepath.stem + stem_extension
    return filepath.with_stem(new_stem).with_suffix('.txt')
