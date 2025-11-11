import os
from transformers import AutoTokenizer

CLEAN_DIR = "../../data/cleaned/"
TOKEN_DIR = "../../data/tokenized/"
MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

def tokenize_file(filepath, tokenizer):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    tokens = tokenizer.encode(text)
    return tokens

if __name__ == "__main__":
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    os.makedirs(TOKEN_DIR, exist_ok=True)
    for filename in os.listdir(CLEAN_DIR):
        path = os.path.join(CLEAN_DIR, filename)
        tokens = tokenize_file(path, tokenizer)
        token_path = os.path.join(TOKEN_DIR, filename + ".tok")
        with open(token_path, "w", encoding="utf-8") as f:
            f.write(" ".join(map(str, tokens)))
