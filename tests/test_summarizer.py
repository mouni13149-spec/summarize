import unittest

from document_summarizer.evaluation import rouge_l_score
from document_summarizer.summarizer import summarize


class SummarizerTests(unittest.TestCase):
    def test_summarize_respects_word_budget(self):
        text = (
            "The team discussed document summarization and PDF processing. "
            "Engineering will build a Streamlit app for uploads. "
            "Product requested concise summaries for managers."
        )

        result = summarize(text, max_words=12)

        self.assertLessEqual(result.summary_words, 12)
        self.assertGreater(result.input_words, result.summary_words)

    def test_rouge_l_scores_exact_match(self):
        self.assertEqual(rouge_l_score("a concise summary", "a concise summary"), 1.0)


if __name__ == "__main__":
    unittest.main()

