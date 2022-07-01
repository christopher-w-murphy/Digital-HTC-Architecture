# Digital-HTC-Architecture
 This is a simple program for OCR and Machine Translation of PDF documents.

## Instructions
How to install and run the OCR and Machine Translation program. These instructions are for macOS. The Prerequisite and Setup steps only need to be run once.

### Prerequisites
Strictly speaking, you need macOS Catalina (10.15) or higher with a 64-bit processor. However, I've tested that this works on macOS Mojave (10.14).

Homebrew is used to install packages. If running `which brew` in a terminal does not return `/usr/local/bin/brew` (or something similar), you'll need to install Homebrew:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

git is needed to clone this repo. If running `which git` does not return something similar to `/usr/bin/git`, install git via Homebrew:
```
brew install git
```

Note that Python 3 is also required. However, this is installed as a dependency in the installer script step below if it's not already on your machine. I'm using Python 3.9. At least Python 3.6 is needed to run this code, but I haven't tested different Python versions.

### Setup
Clone this repo. One optional is to open a terminal and run:
```
git clone https://github.com/christopher-w-murphy/Digital-HTC-Architecture.git
```
Move into the repo directory:
```
cd Digital-HTC-Architecture/
```
Run the installer script:
```
bash macos_installer.sh
```

DeepL is used for translation, and an authentication key is needed to access their API. You can get a key for free, but [registration](https://www.deepl.com/pro-api?cta=header-pro-api) is required. Treat this key as you would a password. For setup purposes, in the configs folder create a plain text file called `auth.txt` and paste your key in the file (and nothing else). Git will ignore this file, so it will not be version controlled, i.e. not shared publicly.

Lastly, in the script `ocr_and_machine_translation.sh` change the PROJECT_DIR to the path that will contain folders of files you'd like to OCR and translate.

### Running the OCR and Translation Program
While still in the `Digital-HTC-Architecture` directory, start the program by running the following command in a terminal:
```
bash ocr_and_machine_translation.sh
```
You will receive a prompt asking for a folder name. This is a subfolder within the PROJECT_DIR containing all the PDF files you want to OCR and translate. File names should not have special characters. I tend to avoid spaces in file names as well.

When the program is finished running you will have two output text files for each input PDF. One file is the text read from PDF in the source language and is labeled "ocr."  The other is the text translated into the target language, which is label "trans."


## Language Codes
Codes for specifying the language(s) of documents. Currently the program reads in French and translates to (British) English. A straightforward generalization would be to make the languages configurable.
- [Tesseract](https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc#LANGUAGES)
- [DeepL](https://www.deepl.com/docs-api/translating-text/?utm_source=github&utm_medium=github-python-readme)

## Acknowledgements

This process was inspired by [Programming Historian](https://programminghistorian.org/en/lessons/OCR-and-Machine-Translation). (Note they have installation instructions for Windows.) I'm using DeepL for translation as it was recommended to me for translation performance purposes.
