import os
import re
import unicodedata

RAW_DIR = "../../data/raw/"
CLEAN_DIR = "../../data/cleaned/"

def clean_text(text):
    # Normalize Unicode
    text = unicodedata.normalize("NFC", text)
    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)
    return text.strip()

if __name__ == "__main__":
    for filename in os.listdir(RAW_DIR):
        path = os.path.join(RAW_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            raw_text = f.read()
        cleaned_text = clean_text(raw_text)
        clean_path = os.path.join(CLEAN_DIR, filename)
        os.makedirs(CLEAN_DIR, exist_ok=True)
        with open(clean_path, "w", encoding="utf-8") as f:
            f.write(cleaned_text)
