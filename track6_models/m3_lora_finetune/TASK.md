# M3: LoRA fine tune vs prompting

**Time:** 2 to 3 evenings · **Skill:** knowing WHEN fine tuning helps, and doing it cheaply.
Do this after the fine tuning learning pathway you started (read about LoRA first).

## The question you answer
"For a 6 class support ticket classifier, is a small fine tuned model better than prompting a
bigger one? At what cost?" You compare:
1. **Prompting** `qwen2.5:3b` (zero shot, then few shot with 6 examples) on your laptop.
2. **LoRA fine tune** of a small model (for example `Qwen2.5-0.5B-Instruct` or `-1.5B`) on Kaggle's
   free GPU with Unsloth, then evaluate it there on the same test set.

## Data (synthetic, made for this lab)
`data/train.csv` (240 rows) and `data/test.csv` (60 rows), columns `text, label`. Labels:
delivery, payment, refund, account, product_issue, other. Some rows are Banglish.
**Honest warning:** train and test come from the same templates, so scores will look too good.
Write 20 tickets of your own in `data/hard_test.csv` (different wording, typos, mixed Bangla)
and report that score too. That is the number that matters.

## What you write
- `prepare_data.py` (tested): `to_chat_example(text, label)` → the chat format used for training;
  `write_jsonl(rows, path)`; `label_from_output(text)` which maps a model reply to a valid label
  (or `"other"` if it can't).
- `evaluate.py` (tested): `accuracy`, `macro_f1`, `per_class_f1`. Use them for ALL three runs.
- `kaggle_train.py`: the steps to run in a Kaggle notebook (TODOs). Read the CURRENT Unsloth docs.

## Kaggle steps (free, no card)
1. Verify your phone on Kaggle, create a notebook, Accelerator → GPU T4, Internet on.
2. Upload `train.jsonl` / `test.jsonl` as a private Kaggle dataset.
3. Train for 1 to 3 epochs with LoRA (r=16 is a fine start). Save the adapter, not the full model.
4. Evaluate on test and hard_test in the notebook; download the predictions CSV.
5. **Stop the session** when done (Kaggle stops idle sessions too, but make it a habit).

## Done when
- [ ] `uv run pytest track6_models/m3_lora_finetune` passes.
- [ ] A table: approach, accuracy, macro F1 (test and hard_test), latency, what it cost ($0, GPU minutes).
- [ ] One paragraph: would you fine tune for this in a real product? Why or why not?
