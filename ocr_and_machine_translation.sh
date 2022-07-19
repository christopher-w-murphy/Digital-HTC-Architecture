#!/bin/bash

# Active Python virtual environment
source venv/digital_htc_architecture/bin/activate
# Run the OCR and Translation program on a file
streamlit run 0_🦃_Digital_HTC_Architecture.py
# streamlit run src/frontend/streamlit.py
# Deactivate Python virtual environment
wait
deactivate
