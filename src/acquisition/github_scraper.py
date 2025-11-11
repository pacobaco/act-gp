import os
import requests
from langdetect import detect

GITHUB_API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN")

def fetch_repo_readme(owner, repo):
    url = f"{GITHUB_API}/repos/{owner}/{repo}/readme"
    headers = {"Authorization": f"token {TOKEN}"} if TOKEN else {}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = response.json().get('content')
        if content:
            import base64
            return base64.b64decode(content).decode('utf-8')
    return None

def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

if __name__ == "__main__":
    owner = "pacobaco"
    repo = "example-repo"
    readme = fetch_repo_readme(owner, repo)
    if readme:
        lang = detect_language(readme)
        print(f"Detected language: {lang}")
        with open(f"../../data/raw/{repo}_README.txt", "w", encoding="utf-8") as f:
            f.write(readme)
