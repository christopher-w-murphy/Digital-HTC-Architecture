from datetime import datetime
from typing import Dict
from io import BytesIO
from zipfile import ZipFile, ZIP_DEFLATED


def get_zip_filename() -> str:
    now = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    return f'ocr_and_tranlsation_{now}.zip'


def zip_results_for_download(results: Dict[str, str]) -> str:
    zip_buffer = BytesIO()
    with ZipFile(zip_buffer, "a", ZIP_DEFLATED, False) as zip_file:
        for file_name, text in results.items():
            data = BytesIO(text.encode('utf-8')).getvalue()
            zip_file.writestr(file_name, data)
    return zip_buffer
