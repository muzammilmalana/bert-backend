# BERT PDF & Image PII Redaction API

This project provides a FastAPI-based web API for extracting text and images from PDFs, performing Named Entity Recognition (NER) using a BERT model, and analyzing/redacting PII in images.

## Installation

### 1. Clone the repository

```bash
git clone <https://github.com/muzammilmalana/bert-backend>
cd bert-backend
```

### 2. Install Python dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Install Tesseract OCR

Some features require [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) to be installed on your system.

- **Windows:** Download the installer from [here](https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe) and add the installation path to your system's PATH variable (IMPORTANT).

## Running the API

Start the FastAPI server:

```bash
fastapi dev app.py       
```

- The API will be available at: `http://127.0.0.1:8000`
- Interactive API docs: `http://127.0.0.1:8000/docs`

## Notes

- Make sure Tesseract is installed and accessible in your PATH for OCR features.
- The NER model is loaded from HuggingFace: `CyberPeace-Institute/SecureBERT-NER`.
