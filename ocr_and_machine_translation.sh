#!/bin/bash

# Prompt the user to enter a folder name
read -p "enter folder name: " folder;

# Create a variable containing the full file path of that folder
PROJECT_DIR=/Users/christopherwmurphy/Documents/projects/digital_history
FILES=$PROJECT_DIR/$folder/*

# Active Python virtual environment
source venv/digital_htc_architecture/bin/activate

# Iterate through all the files in the folder
for file in $FILES;
do
  # Run the OCR and Translation program on a file
  python3 -m src.application.translator_app $file
  sleep 1m
done

# Deactivate Python virtual environment
deactivate
