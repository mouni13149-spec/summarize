from __future__ import annotations

import argparse
import json

from document_summarizer.evaluation import evaluate_pairs
from document_summarizer.io import load_summary_pairs, read_document, write_text
from document_summarizer.summarizer import summarize


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize long documents and evaluate summary quality.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    summarize_parser = subparsers.add_parser("summarize", help="Summarize one document.")
    summarize_parser.add_argument("--input", required=True)
    summarize_parser.add_argument("--max-words", type=int, default=300)
    summarize_parser.add_argument("--output")

    eval_parser = subparsers.add_parser("evaluate", help="Evaluate ROUGE-L on document-summary pairs.")
    eval_parser.add_argument("--data", required=True)
    eval_parser.add_argument("--max-words", type=int, default=300)

    args = parser.parse_args()
    if args.command == "summarize":
        run_summarize(args)
    elif args.command == "evaluate":
        run_evaluate(args)


def run_summarize(args: argparse.Namespace) -> None:
    result = summarize(read_document(args.input), max_words=args.max_words)
    payload = result.to_dict()
    print(json.dumps(payload, indent=2))
    if args.output:
        write_text(args.output, result.summary)


def run_evaluate(args: argparse.Namespace) -> None:
    metrics = evaluate_pairs(load_summary_pairs(args.data), max_words=args.max_words)
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()

