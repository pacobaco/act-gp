# ACT-GP (AI Code & Text Generation Platform)

ACT-GP is a multilingual AI platform that generates code and text outputs from keyword prompts. The platform leverages **GitHub repositories**, **Blogspot posts**, and other public sources to create a structured, tokenized, and fine-tuned dataset for AI model training.

## Features
- Keyword-driven code and text generation
- Multilingual corpus support
- Structured data pipeline (acquisition → cleaning → tokenization → training)
- Transparent governance and licensing compliance
- Deployment via API and IDE plugin

## Repository Structure

data/             # Raw and processed data
notebooks/        # Analysis and prototyping
src/              # Source code (acquisition, preprocessing, model, evaluation, deployment)
configs/          # Config files
tests/            # Unit tests

## Installation
```bash
git clone https://github.com/<username>/act-gp.git
cd act-gp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
	1.	Data acquisition: python src/acquisition/github_scraper.py
	2.	Preprocessing: python src/preprocessing/clean_data.py
	3.	Tokenization: python src/tokenization/tokenize.py
	4.	Model training: python src/model/train_model.py
	5.	Evaluation: python src/evaluation/evaluate.py
	6.	Deployment: python src/deployment/run_api.py

## License

MIT License

---

