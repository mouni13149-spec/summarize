from __future__ import annotations

import tempfile
from pathlib import Path

import streamlit as st

from document_summarizer.io import read_document
from document_summarizer.summarizer import summarize


st.set_page_config(page_title="Document Summarizer", layout="wide")
st.title("Automated Document Summarizer")

uploaded_file = st.file_uploader("Upload a TXT or PDF document", type=["txt", "pdf"])
max_words = st.slider("Summary length", min_value=50, max_value=500, value=300, step=25)

if uploaded_file:
    suffix = Path(uploaded_file.name).suffix
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = Path(tmp.name)

    text = read_document(tmp_path)
    result = summarize(text, max_words=max_words)
    st.metric("Input words", result.input_words)
    st.metric("Summary words", result.summary_words)
    st.text_area("Summary", result.summary, height=300)

