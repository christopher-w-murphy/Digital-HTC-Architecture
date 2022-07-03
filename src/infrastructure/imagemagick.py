from pathlib import Path

from wand.image import Image


def get_tiff_filepath(filepath: Path) -> Path:
    """
    Take a file path and replace its extention with .tiff
    """
    return filepath.with_suffix('.tiff')


def process_image(filepath: Path) -> None:
    """
    Convert PDF to TIFF and make it easier to OCR
    """
    with Image(filename=filepath, resolution=300) as img:
        img.format = 'tiff'
        img.depth = 8
        img.strip()
        img.background_color = 'white'
        img.alpha_channel = 'off'

        tiff_filename = get_tiff_filepath(filepath)
        img.save(filename=tiff_filename)


def delete_tiff_file(filepath: Path) -> None:
    """
    The created TIFF files are large, so delete them when we're done with them
    """
    tiff_filename = get_tiff_filepath(filepath)
    Path.unlink(tiff_filename, missing_ok=True)
