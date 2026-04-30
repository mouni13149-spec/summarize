from __future__ import annotations

import argparse
import time

from document_summarizer.io import read_document
from document_summarizer.summarizer import summarize


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark document summarization latency.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--max-words", type=int, default=300)
    parser.add_argument("--repeat", type=int, default=10)
    args = parser.parse_args()

    text = read_document(args.input)
    started = time.perf_counter()
    for _ in range(args.repeat):
        summarize(text, max_words=args.max_words)
    elapsed = time.perf_counter() - started
    print(f"runs={args.repeat} elapsed_seconds={elapsed:.3f} avg_seconds={elapsed / args.repeat:.3f}")


if __name__ == "__main__":
    main()

