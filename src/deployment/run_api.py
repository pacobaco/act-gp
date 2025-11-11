from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_DIR = "../../model_output/"

app = FastAPI()
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForCausalLM.from_pretrained(MODEL_DIR)

class Prompt(BaseModel):
    text: str

@app.post("/generate")
def generate(prompt: Prompt):
    input_ids = tokenizer(prompt.text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=100)
    return {"output": tokenizer.decode(outputs[0], skip_special_tokens=True)}

# Run with: uvicorn src.deployment.run_api:app --reload
