from presidio_image_redactor import ImageAnalyzerEngine, ImagePiiVerifyEngine
from PIL import Image
from typing import List, Dict

def analyze_image_pii(image_path: str) -> List[Dict]:
    image_analyzer_engine = ImageAnalyzerEngine()
    image = Image.open(image_path)
    results = image_analyzer_engine.analyze(image=image)
    return results

def redact_image(image_path: str, color=(255, 192, 203)) -> str:
    from presidio_image_redactor import ImageRedactorEngine
    image = Image.open(image_path)
    engine = ImageRedactorEngine()
    redacted_image = engine.redact(image, color)
    redacted_path = image_path.replace('.', '_redacted.')
    redacted_image.save(redacted_path)
    return redacted_path 