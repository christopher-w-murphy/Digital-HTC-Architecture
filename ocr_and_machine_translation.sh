#!/bin/bash

# Prompt the user to enter a folder name
read -p "enter folder name: " folder;

# Create a variable containing the full file path of that folder
PROJECT_DIR=/Users/christopherwmurphy/Documents/projects/digital_history
FILES=$PROJECT_DIR/$folder/*

# Iterate through all the files in the folder
for file in $FILES;
do
  # Filenames
  tiff=${file%.*}.tiff
  ocr=${file%.*}_ocr
  tlate=${file%.*}_trans
  # Convert a PDF and make it easier to OCR
  convert -density 300 $file -depth 8 -strip -background white -alpha off $tiff
  # Run the Tesseract OCR program to produce a plain text file in French
  tesseract $tiff $ocr -l fra
  # Translate the OCR text using DeepL
  translator=$PROJECT_DIR/src/application/translator_app.py
  python3 $translator $ocr $tlate
  # allow the previous file to finish being translated and written
  # as well as space out your requests to the DeepL API
  sleep 1m
done
