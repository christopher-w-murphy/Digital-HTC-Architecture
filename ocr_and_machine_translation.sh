#!/bin/bash
set -euo pipefail

# Active Python virtual environment
source venv/bin/activate
# Run the OCR and Translation program on a file
streamlit run 0_🦃_Digital_HTC_Architecture.py
# Deactivate Python virtual environment
wait
deactivate
