from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling
import os

print("🚀 Fine-tuning Vietnamese GPT-2 on data.txt...")

# Load Vietnamese tokenizer & model
tokenizer = AutoTokenizer.from_pretrained("NlpHUST/gpt2-vietnamese")
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained("NlpHUST/gpt2-vietnamese")

# Create dataset
dataset = TextDataset(
    tokenizer=tokenizer,
    file_path="data.txt",
    block_size=128
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,
)

# Training args
training_args = TrainingArguments(
    output_dir="./dragonfly_model",
    overwrite_output_dir=True,
    num_train_epochs=10,
    per_device_train_batch_size=1,
    save_steps=50,
    logging_steps=10,
    learning_rate=5e-5,
)

# Train
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)

trainer.train()

# Save
model.save_pretrained("./dragonfly_model")
tokenizer.save_pretrained("./dragonfly_model")
print("✅ Model saved to ./dragonfly_model")