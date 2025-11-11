import os
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_DIR = "../../model_output/"
TOKEN_DIR = "../../data/tokenized/"

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForCausalLM.from_pretrained(MODEL_DIR)

def evaluate_file(filepath):
    with open(filepath, "r") as f:
        tokens = list(map(int, f.read().split()))
    input_ids = torch.tensor([tokens])
    outputs = model.generate(input_ids, max_length=50)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    for filename in os.listdir(TOKEN_DIR):
        path = os.path.join(TOKEN_DIR, filename)
        output = evaluate_file(path)
        print(f"File: {filename}\nGenerated Output:\n{output}\n")
