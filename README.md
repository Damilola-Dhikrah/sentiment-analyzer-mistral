\# Sentiment Analyzer (Mistral)



A simple AI app that uses the \*\*Mistral\*\* model via \*\*Ollama\*\* to classify text as \*\*Positive\*\*, \*\*Negative\*\*, or \*\*Neutral\*\*.



\- \*\*FastAPI\*\* backend (`/analyze`)

\- \*\*Streamlit\*\* frontend

\- \*\*Ollama-hosted Mistral\*\* (runs locally)



\## Setup (Windows PowerShell)

1\) Clone:

git clone https://github.com/Damilola-Dhikrah/sentiment-analyzer-mistral.git

cd sentiment-analyzer-mistral



2\) Virtual env:

python -m venv venv

.\\venv\\Scripts\\Activate



3\) Install deps:

pip install -r requirements.txt

\# If installing individually, also do:

\# pip install fastapi uvicorn streamlit requests python-multipart



4\) Install Ollama \& model:

Download Ollama: https://ollama.com

ollama pull mistral



\## Run

\# Splunk often uses port 8000, so we use 8001



Terminal A (backend):

uvicorn backend.main:app --reload --host 127.0.0.1 --port 8001



Terminal B (frontend):

streamlit run frontend/app.py



In the app, set Backend URL to:

http://localhost:8001/analyze/



Open http://localhost:8501



\## Project Structure

sentiment-analyzer-mistral/

├── backend/

│   └── main.py

├── frontend/

│   └── app.py

├── requirements.txt

└── README.md



\## How it works (one-liner)

Streamlit sends your text to FastAPI → FastAPI prompts the local Mistral model via Ollama → returns one word: Positive/Negative/Neutral.



\## Troubleshooting

\- \*\*Connection refused\*\*: make sure backend is running on 8001.

\- \*\*Form data requires python-multipart\*\*: pip install python-multipart

\- \*\*Model errors\*\*: make sure Ollama is running and you did `ollama pull mistral`.



