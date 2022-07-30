from datetime import datetime
from io import BytesIO

from src.infrastructure.streamlit.downloads import get_zip_filename, zip_results_for_download


def test_get_zip_filename():
    test_timestamp = datetime(2022, 7, 30, 0, 0, 0)
    result = f'ocr_and_tranlsation_{test_timestamp}.zip'
    assert get_zip_filename(timestamp=test_timestamp) == result


def test_zip_results_for_download():
    test_result = {'fname': 'Hello world!'}
    test_zip = zip_results_for_download(test_result)
    assert isinstance(test_zip, BytesIO)
