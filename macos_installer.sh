#!/bin/bash

# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Image Processing
brew install imagemagick

# OCR
brew install tesseract
brew install tesseract-lang

# DeepL
python3 -m pip install -r requirements.txt
