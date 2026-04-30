# Architecture

The project has three layers:

- Local extractive summarizer for fast, deterministic demos.
- Optional Streamlit app for document upload and interactive summaries.
- Optional BART-large fine-tuning script for abstractive summarization.

```mermaid
flowchart LR
  A["TXT or PDF document"] --> B["Text extraction"]
  B --> C["Sentence splitting"]
  C --> D["Sentence scoring"]
  D --> E["Summary assembly"]
  E --> F["Summary JSON or Streamlit output"]
```

## Baseline

The baseline scores sentences using token frequency and position weighting, then selects high-value sentences until the word budget is reached.

## Fine-Tuned Model

The BART script tokenizes document-summary pairs and trains a sequence-to-sequence model. It is intended for GPU environments and larger labeled datasets.

