from pathlib import Path
import sys

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.application.ocr_and_translation_app import ocr_and_translate_documents
from src.infrastructure.streamlit.downloads import zip_results_for_download, get_zip_filename


st.set_page_config(page_title="Translation", page_icon="🧐")

st.header('Translation')

st.subheader('Select your files')

files = st.file_uploader("Upload text file(s)", type='txt', accept_multiple_files=True)

st.subheader('Select your languages')

source_lang = st.selectbox("Source Language", ["French"])
target_lang = st.selectbox("Target Language", ["English"])

st.subheader('Enter your DeepL authentication key')

auth_key = st.text_input("DeepL Authentication Key", type="password", help='Sign up for free at: https://www.deepl.com/pro-api')

st.subheader('Run the Translator')
run = st.button("Click to run")
