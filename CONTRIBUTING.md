# Contributing

## Setup

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

## Tests

```powershell
pytest
```

## Guidelines

- Keep sample documents synthetic.
- Do not commit private meeting notes, contracts, or PDFs.
- Add tests when changing sentence scoring, chunking, ROUGE evaluation, or PDF parsing.

