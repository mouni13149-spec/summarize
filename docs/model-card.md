# Model Card

## Intended Use

Summarize long meeting notes, articles, and PDF text for demos, productivity prototypes, and portfolio projects.

## Not Intended For

- Legal, medical, or financial decisions without human review.
- Summarizing confidential documents without privacy controls.
- Replacing full-document review when exact wording matters.

## Data

The repository includes synthetic examples. The full project concept assumes 30K document-summary pairs for fine-tuning.

## Metrics

Primary metric:

- ROUGE-L

Secondary metrics:

- Latency
- Compression ratio
- Summary word count

## Risks

Summaries may omit important details or overemphasize repeated terms. Generative models may introduce unsupported details.

## Mitigations

- Keep source document available.
- Report compression ratio and method.
- Use extractive summaries for low-risk demos.
- Add human review for high-stakes documents.

