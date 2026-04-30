from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SummaryResult:
    summary: str
    input_words: int
    summary_words: int
    compression_ratio: float
    method: str

    def to_dict(self) -> dict[str, object]:
        return {
            "summary": self.summary,
            "input_words": self.input_words,
            "summary_words": self.summary_words,
            "compression_ratio": round(self.compression_ratio, 4),
            "method": self.method,
        }

