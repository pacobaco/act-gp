import torch
from transformers import AutoModelForCausalLM, Trainer, TrainingArguments, AutoTokenizer

MODEL_NAME = "bigscience/bloom-560m"
TOKEN_DIR = "../../data/tokenized/"
OUTPUT_DIR = "../../model_output/"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Dummy dataset loader
class TokenDataset(torch.utils.data.Dataset):
    def __init__(self, token_dir):
        self.files = [os.path.join(token_dir, f) for f in os.listdir(token_dir)]
    def __len__(self):
        return len(self.files)
    def __getitem__(self, idx):
        with open(self.files[idx], "r") as f:
            tokens = list(map(int, f.read().split()))
        return {"input_ids": torch.tensor(tokens), "labels": torch.tensor(tokens)}

dataset = TokenDataset(TOKEN_DIR)

training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_device_train_batch_size=1,
    save_steps=100,
    save_total_limit=2,
    logging_dir='./logs',
    logging_steps=10,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)

trainer.train()
