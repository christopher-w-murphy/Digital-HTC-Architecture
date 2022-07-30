import streamlit as st

from src.application.ocr_and_translation_app import ocr_and_translate_documents
from src.application.languages import deepl_target_languages
from src.infrastructure.streamlit.downloads import zip_results_for_download, get_zip_filename


st.set_page_config(page_title="OCR and Translation", page_icon="🤠")

st.header('OCR and Translation')

st.subheader('Select your files')

files = st.file_uploader("Upload PDF(s)", type='pdf', accept_multiple_files=True)

st.subheader('Select your languages')

source_lang = st.selectbox("Source Language", ["French"])

target_lang_names = list(deepl_target_languages.keys())
target_lang_names.sort()
default_target_name = target_lang_names.index('English (British)')
target_lang = st.selectbox("Target Language", target_lang_names, index=default_target_name)

st.subheader('Enter your DeepL authentication key')

auth_key = st.text_input("DeepL Authentication Key", type="password", help='Sign up for free at: https://www.deepl.com/pro-api')

st.subheader('Run the OCR and Translator')
run = st.button("Click to run")

if run and files is not None:
    with st.spinner("Wait for it..."):
        results = ocr_and_translate_documents(files, auth_key)

    zip_buffer = zip_results_for_download(results)
    zip_filename = get_zip_filename()
    st.download_button('Download results', zip_buffer, file_name=zip_filename, mime='application/zip')
    st.success('Done!')
