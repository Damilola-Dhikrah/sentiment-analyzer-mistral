# backend/main.py
from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Allow Streamlit on 8501 to call FastAPI on 8000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501", "http://127.0.0.1:8501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze/")
def analyze_sentiment(text: str = Form(...)):
    if not text.strip():
        raise HTTPException(status_code=400, detail="Text is empty.")

    # Keep the output stable and one-word
    prompt = (
        "You are a sentiment classifier. "
        "Given the text below, reply with exactly one of these words: Positive, Negative, or Neutral.\n\n"
        f"Text:\n{text}\n\n"
        "Answer with exactly one word from the set: Positive, Negative, Neutral."
    )

    try:
        r = requests.post(
            OLLAMA_URL,
            json={"model": MODEL_NAME, "prompt": prompt, "stream": False},
            timeout=120
        )
        r.raise_for_status()
        data = r.json()
        raw = data.get("response", "").strip()
        # normalize occasional punctuation
        sentiment = raw.split()[0].strip(",. ").capitalize()
        if sentiment not in {"Positive", "Negative", "Neutral"}:
            sentiment = "Neutral"
        return {"sentiment": sentiment}
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Ollama connection error: {e}")
