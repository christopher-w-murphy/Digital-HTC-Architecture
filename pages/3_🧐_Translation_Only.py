import streamlit as st

from src.application.translation_app import translate_documents
from src.application.languages import deepl_source_languages, deepl_target_languages
from src.infrastructure.streamlit.downloads import zip_results_for_download, get_zip_filename


st.set_page_config(page_title="Translation", page_icon="🧐")

st.header('Translation')

st.subheader('Select your files')

files = st.file_uploader("Upload text file(s)", type='txt', accept_multiple_files=True)

st.subheader('Select your languages')

source_lang_names = list(deepl_source_languages.keys())
source_lang_names.sort()
default_source_name = source_lang_names.index('French')
source_lang = st.selectbox("Source Language", source_lang_names, index=default_source_name)

target_lang_names = list(deepl_target_languages.keys())
target_lang_names.sort()
default_target_name = target_lang_names.index('English (British)')
target_lang = st.selectbox("Target Language", target_lang_names, index=default_target_name)

st.subheader('Enter your DeepL authentication key')

auth_key = st.text_input("DeepL Authentication Key", type="password", help='Sign up for free at: https://www.deepl.com/pro-api')

st.subheader('Run the Translator')
run = st.button("Click to run")

if run and files is not None:
    with st.spinner("Wait for it..."):
        results = translate_documents(files, auth_key, source_lang, target_lang)

    if results is not None:
        zip_buffer = zip_results_for_download(results)
        zip_filename = get_zip_filename('tranlation')
        st.download_button('Download results', zip_buffer, file_name=zip_filename, mime='application/zip')
        st.success('Done!')
    else:
        st.error('No results returned.')
