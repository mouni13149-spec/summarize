from __future__ import annotations

import math
import re
from collections import Counter

from document_summarizer.models import SummaryResult

SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")
TOKEN_RE = re.compile(r"[a-zA-Z][a-zA-Z0-9'-]*")
STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "in",
    "is", "it", "of", "on", "or", "that", "the", "this", "to", "was", "were", "with",
}


def summarize(text: str, max_words: int = 300) -> SummaryResult:
    sentences = split_sentences(text)
    if not sentences:
        return SummaryResult("", 0, 0, 0.0, "extractive_frequency")

    input_words = count_words(text)
    selected = select_sentences(sentences, max_words)
    summary = " ".join(selected)
    summary_words = count_words(summary)
    compression_ratio = summary_words / input_words if input_words else 0.0
    return SummaryResult(summary, input_words, summary_words, compression_ratio, "extractive_frequency")


def split_sentences(text: str) -> list[str]:
    cleaned = " ".join(text.split())
    return [sentence.strip() for sentence in SENTENCE_RE.split(cleaned) if sentence.strip()]


def select_sentences(sentences: list[str], max_words: int) -> list[str]:
    frequencies = token_frequencies(" ".join(sentences))
    scored = []
    for index, sentence in enumerate(sentences):
        tokens = tokenize(sentence)
        if not tokens:
            continue
        score = sum(frequencies[token] for token in tokens) / math.sqrt(len(tokens))
        if index == 0:
            score *= 1.15
        scored.append((score, index, sentence))

    chosen = []
    word_count = 0
    for _, index, sentence in sorted(scored, reverse=True):
        sentence_words = count_words(sentence)
        if word_count + sentence_words <= max_words or not chosen:
            chosen.append((index, sentence))
            word_count += sentence_words
        if word_count >= max_words:
            break
    return [sentence for _, sentence in sorted(chosen)]


def token_frequencies(text: str) -> Counter[str]:
    tokens = [token for token in tokenize(text) if token not in STOPWORDS]
    return Counter(tokens)


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in TOKEN_RE.findall(text)]


def count_words(text: str) -> int:
    return len(tokenize(text))

