#!/bin/bash
set -euo pipefail

# Check if Homebrew is installed
if ! command -v brew &> /dev/null
then
  echo "brew could not be found. Installing Homebrew."
  # Install Homebrew if not found
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi


# Check if Imagemagick is installed
if ! command -v convert &> /dev/null
then
  echo "Imagemagick could not be found. Installing Imagemagick."
  # Install Imagemagick if not found
  brew install imagemagick
fi


# Check if Tesseract is installed
if ! command -v tesseract &> /dev/null
then
  echo "tesseract could not be found. Installing Tesseract."
  # Install Tesseract if not found
  brew install tesseract
  # Enables extra languages support for Tesseract, if not already installed
  brew ls --versions tesseract-lang || brew install tesseract-lang
fi


# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
  echo "python3 could not be found. Installing Python 3.9."
  # Install Python 3 if not found
  brew install python@3.9
fi


# Upgrade pip for superstitious reasons.
python3 -m pip install --upgrade pip


# Check if virtualenv is installed
if ! command -v virtualenv &> /dev/null
then
  echo "virtualenv could not be found. Installing virtualenv."
  # Install virtualenv if not found
  python3 -m pip install virtualenv
fi


# Python environment
echo "Creating a Python virtual environment."
python3 -m virtualenv venv
echo "Installing Python packages."
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
deactivate
