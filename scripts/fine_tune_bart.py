from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Fine-tune BART-large for document summarization.")
    parser.add_argument("--train", required=True)
    parser.add_argument("--eval", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--base-model", default="facebook/bart-large-cnn")
    parser.add_argument("--epochs", type=float, default=2.0)
    parser.add_argument("--max-input-length", type=int, default=1024)
    parser.add_argument("--max-summary-length", type=int, default=300)
    args = parser.parse_args()

    try:
        from datasets import load_dataset
        from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, DataCollatorForSeq2Seq, Seq2SeqTrainer, Seq2SeqTrainingArguments
    except ImportError as exc:
        raise SystemExit("Install ML dependencies with: pip install -e \".[ml]\"") from exc

    tokenizer = AutoTokenizer.from_pretrained(args.base_model)
    model = AutoModelForSeq2SeqLM.from_pretrained(args.base_model)
    dataset = load_dataset("json", data_files={"train": args.train, "eval": args.eval})

    def preprocess(batch: dict) -> dict:
        inputs = tokenizer(batch["document"], max_length=args.max_input_length, truncation=True)
        labels = tokenizer(text_target=batch["summary"], max_length=args.max_summary_length, truncation=True)
        inputs["labels"] = labels["input_ids"]
        return inputs

    tokenized = dataset.map(preprocess, batched=True, remove_columns=dataset["train"].column_names)
    training_args = Seq2SeqTrainingArguments(
        output_dir=args.output_dir,
        num_train_epochs=args.epochs,
        learning_rate=3e-5,
        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,
        gradient_accumulation_steps=8,
        eval_strategy="epoch",
        save_strategy="epoch",
        predict_with_generate=True,
        report_to="none",
    )
    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=tokenized["train"],
        eval_dataset=tokenized["eval"],
        tokenizer=tokenizer,
        data_collator=DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model),
    )
    trainer.train()
    trainer.save_model(args.output_dir)


if __name__ == "__main__":
    main()

