from pathlib import Path


def write_to_file(output_path: Path, text: str) -> None:
    with Path(output_path) as p:
        p.write_text(text, encoding='utf-8')


def get_text_filepath(filepath: Path, stem_extension: str) -> Path:
    new_stem = filepath.stem + stem_extension
    return filepath.with_stem(new_stem).with_suffix('.txt')


def get_tiff_filepath(filepath: Path) -> Path:
    """
    Take a file path and replace its extention with .tiff
    """
    return filepath.with_suffix('.tiff')


def delete_tiff_file(filepath: Path) -> None:
    """
    The created TIFF files are large, so delete them when we're done with them
    """
    tiff_filename = get_tiff_filepath(filepath)
    Path.unlink(tiff_filename, missing_ok=True)
