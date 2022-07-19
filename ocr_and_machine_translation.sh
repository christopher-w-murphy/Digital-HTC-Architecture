#!/bin/bash

# Active Python virtual environment
source venv/digital_htc_architecture/bin/activate
# Run the OCR and Translation program on a file
streamlit run streamlit_app.py
# Deactivate Python virtual environment
wait
deactivate
