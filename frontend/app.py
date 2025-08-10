# frontend/app.py
import streamlit as st
import requests

st.set_page_config(page_title="Sentiment Analyzer (Mistral)", page_icon="💬")
st.title("💬 Sentiment Analyzer (Mistral)")

st.write("Type text below and click **Analyze**. Model runs locally via Ollama (Mistral).")

text_input = st.text_area("Enter your sentence here:", height=180, placeholder="Type something people might say...")
api_url = st.text_input("Backend URL", value="http://localhost:8000/analyze/")

if st.button("Analyze"):
    if not text_input.strip():
        st.error("Please enter some text.")
    else:
        with st.spinner("Thinking..."):
            try:
                res = requests.post(api_url, data={"text": text_input}, timeout=60)
                if res.status_code == 200:
                    sentiment = res.json().get("sentiment", "Error")
                    st.subheader("Predicted Sentiment:")
                    st.success(sentiment)
                else:
                    st.error(f"Error {res.status_code}: {res.text}")
            except requests.RequestException as e:
                st.error(f"Could not reach backend: {e}")
