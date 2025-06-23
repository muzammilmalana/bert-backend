import os
import fitz  # PyMuPDF

def extract_text_and_images(pdf_path, output_dir="pdf_output"):
    os.makedirs(output_dir, exist_ok=True)
    images_dir = os.path.join(output_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    all_lines = []
    extracted_text = []
    for page_number in range(len(doc)):
        page = doc[page_number]
        text = page.get_text("text")
        lines = text.splitlines()
        cleaned_lines = [line.strip() for line in lines if line.strip()]
        sentence = " ".join(cleaned_lines)
        extracted_text.append(sentence)
        all_lines.extend(cleaned_lines)
        # Extract images
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = os.path.join(images_dir, f"page{page_number + 1}_img{img_index + 1}.{image_ext}")
            with open(image_filename, "wb") as img_file:
                img_file.write(image_bytes)
    return extracted_text, all_lines 