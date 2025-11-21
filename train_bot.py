from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import load_dataset
import torch, os

print("🚀 Bắt đầu huấn luyện GPT-2!")

# 1️⃣ Load model và tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token
model = GPT2LMHeadModel.from_pretrained("gpt2")

# 2️⃣ Load dữ liệu từ data.txt
if not os.path.exists("data.txt"):
    raise FileNotFoundError("❌ Không tìm thấy file data.txt!")

dataset = load_dataset("text", data_files={"train": "data.txt"})
print(f"📘 Đã load {len(dataset['train'])} dòng dữ liệu")

def tokenize(batch):
    return tokenizer(batch["text"], truncation=True, padding="max_length", max_length=64)
dataset = dataset.map(tokenize, batched=True)

# 3️⃣ Collator
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# 4️⃣ Tham số train
training_args = TrainingArguments(
    output_dir="./model",
    overwrite_output_dir=True,
    num_train_epochs=5,
    per_device_train_batch_size=1,
    save_steps=50,
    logging_steps=5,
    report_to="none",
    learning_rate=5e-5
)

# 5️⃣ Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset["train"]
)

# 6️⃣ Train
trainer.train()

# 7️⃣ Lưu model
model.save_pretrained("./my_gpt2")
tokenizer.save_pretrained("./my_gpt2")
print("✅ Huấn luyện xong, model lưu tại ./my_gpt2")
