"""Steps for a Kaggle notebook (GPU T4). Copy cell by cell; do not run this on your laptop.
APIs change: check the current Unsloth docs before you start (https://docs.unsloth.ai)."""

# Cell 1: install
# !pip install unsloth

# Cell 2: load a small base model in 4 bit
# TODO: from unsloth import FastLanguageModel
#       model, tokenizer = FastLanguageModel.from_pretrained("unsloth/Qwen2.5-0.5B-Instruct",
#                                                            max_seq_length=512, load_in_4bit=True)

# Cell 3: add LoRA adapters
# TODO: model = FastLanguageModel.get_peft_model(model, r=16, lora_alpha=16, lora_dropout=0,
#                 target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"])
#       Question for your log: how many parameters are trainable vs total? (model.print_trainable_parameters())

# Cell 4: data
# TODO: load train.jsonl from /kaggle/input/<your-dataset>/, apply tokenizer.apply_chat_template
#       Train only on the assistant answer if the docs show how (why does that matter?)

# Cell 5: train
# TODO: TRL SFTTrainer, 1 to 3 epochs, learning rate around 2e-4, batch size 8, seed 42
#       Watch the loss. Write down GPU minutes used.

# Cell 6: evaluate
# TODO: for each test row, generate with max_new_tokens=5, temperature 0,
#       map with label_from_output (copy it from prepare_data.py), compute accuracy and macro F1
#       with evaluate.py. Save predictions.csv and download it.

# Cell 7: save the adapter only (a few MB), then STOP the session.
# model.save_pretrained("ticket_lora")
