from fastapi import FastAPI, UploadFile, File, Body
from fastapi.responses import JSONResponse
import os
from bert.utils_pdf import extract_text_and_images
from bert.utils_ner import make_predictions
from bert.utils_image import analyze_image_pii, redact_image
from typing import List

app = FastAPI()


@app.post("/extract")
async def extract_pdf(file: UploadFile = File(...)):
    # Save uploaded file
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, file.filename)
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    # Extract text and images
    extracted_text, all_lines = extract_text_and_images(file_path)
    return JSONResponse({
        "extracted_text": extracted_text,
        "num_lines": len(all_lines),
        "num_text_blocks": len(extracted_text)
    })

@app.post("/predict")
async def predict_ner(texts: List[str] = Body(..., embed=True)):
    tokens, pred_labels = make_predictions(texts)
    return JSONResponse({
        "tokens": tokens,
        "pred_labels": pred_labels
    })

@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    upload_dir = "uploads/images"
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, file.filename)
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    results = analyze_image_pii(file_path)
    return JSONResponse({"pii_entities": results})

@app.post("/redact-image")
async def redact_uploaded_image(file: UploadFile = File(...)):
    upload_dir = "uploads/images"
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, file.filename)
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    redacted_path = redact_image(file_path)
    return JSONResponse({"redacted_image_path": redacted_path})

# ... more endpoints to be added for NER and image PII analysis

