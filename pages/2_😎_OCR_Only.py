from pathlib import Path
import sys

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parent.parent))


st.set_page_config(page_title="OCR and Translation", page_icon="😎")

st.header('OCR')

st.subheader('Select your files')

files = st.file_uploader("Upload PDF(s)", type='pdf', accept_multiple_files=True)

st.subheader('Select your language')

source_lang = st.selectbox("Source Language", ["French"])

st.subheader('Run the OCR')
run = st.button("Click to run")
