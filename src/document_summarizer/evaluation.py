from __future__ import annotations

from document_summarizer.summarizer import summarize, tokenize


def rouge_l_score(prediction: str, reference: str) -> float:
    predicted_tokens = tokenize(prediction)
    reference_tokens = tokenize(reference)
    if not predicted_tokens or not reference_tokens:
        return 0.0
    lcs = longest_common_subsequence(predicted_tokens, reference_tokens)
    precision = lcs / len(predicted_tokens)
    recall = lcs / len(reference_tokens)
    if precision + recall == 0:
        return 0.0
    return (2 * precision * recall) / (precision + recall)


def evaluate_pairs(pairs: list[dict[str, str]], max_words: int = 300) -> dict[str, float]:
    if not pairs:
        return {"examples": 0.0, "rouge_l": 0.0}
    scores = []
    for pair in pairs:
        prediction = summarize(pair["document"], max_words=max_words).summary
        scores.append(rouge_l_score(prediction, pair["summary"]))
    return {
        "examples": float(len(pairs)),
        "rouge_l": sum(scores) / len(scores),
    }


def longest_common_subsequence(left: list[str], right: list[str]) -> int:
    previous = [0] * (len(right) + 1)
    for left_token in left:
        current = [0]
        for index, right_token in enumerate(right, start=1):
            if left_token == right_token:
                current.append(previous[index - 1] + 1)
            else:
                current.append(max(previous[index], current[-1]))
        previous = current
    return previous[-1]

