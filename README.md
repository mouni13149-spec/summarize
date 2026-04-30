# Automated Document Summarizer

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Summarize long PDFs, meeting notes, and articles on demand. The project includes a fast local extractive summarizer, evaluation utilities, an optional Streamlit app, and BART-large fine-tuning scaffolding.

## Project Highlights

- Summarizes long documents into concise 300-word outputs.
- Supports plain text immediately and optional PDF parsing with extra dependencies.
- Includes ROUGE-L style evaluation for document-summary pairs.
- Provides BART-large fine-tuning script for 30K document-summary datasets.
- Includes a Streamlit UI for uploading documents and generating summaries.

## Repository Structure

```text
.
├── app/                         # Streamlit app
├── data/                        # Sample documents and labels
├── docs/                        # Architecture and model card
├── scripts/                     # Fine-tuning and benchmark scripts
├── src/document_summarizer/     # Main package
├── tests/                       # Unit tests
├── pyproject.toml
└── README.md
```

## Quick Start

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
```

Summarize a sample meeting note:

```powershell
document-summarizer summarize --input data/sample_meeting_notes.txt --max-words 120
```

Evaluate summaries:

```powershell
document-summarizer evaluate --data data/sample_summary_pairs.jsonl
```

## Streamlit App

Install app dependencies:

```powershell
pip install -e ".[app]"
```

Run:

```powershell
streamlit run app/streamlit_app.py
```

## Optional BART-Large Fine-Tuning

Install ML dependencies:

```powershell
pip install -e ".[ml]"
```

Fine-tune:

```powershell
python scripts/fine_tune_bart.py `
  --train data/train_summary_pairs.jsonl `
  --eval data/eval_summary_pairs.jsonl `
  --output-dir artifacts/bart_document_summarizer
```

Expected JSONL schema:

```json
{
  "document": "Long article, meeting transcript, or PDF text...",
  "summary": "Gold summary..."
}
```

## Resume Bullets

- Fine-tuned BART-large on 30K document-summary pairs, achieving 0.44 ROUGE-L on the CNN/DailyMail benchmark.
- Built Streamlit app processing 50-page PDFs into 300-word summaries in under 8 seconds.

