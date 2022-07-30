import streamlit as st

from src.application.ocr_app import ocr_documents
from src.application.languages import tesseract_languages
from src.infrastructure.streamlit.downloads import zip_results_for_download, get_zip_filename


st.set_page_config(page_title="OCR and Translation", page_icon="😎")

st.header('OCR')

st.subheader('Select your files')

files = st.file_uploader("Upload PDF(s)", type='pdf', accept_multiple_files=True)

st.subheader('Select your language')

language_names = list(tesseract_languages.keys())
language_names.sort()
default_language = language_names.index('French')
source_lang = st.selectbox("Source Language", language_names, index=default_language)

st.subheader('Run the OCR')
run = st.button("Click to run")

if run and files is not None:
    with st.spinner("Wait for it..."):
        results = ocr_documents(files, source_lang)

    zip_buffer = zip_results_for_download(results)
    zip_filename = get_zip_filename('ocr')
    st.download_button('Download results', zip_buffer, file_name=zip_filename, mime='application/zip')
    st.success('Done!')
