from transformers import AutoTokenizer, AutoModel
import torch

# Load Vietnamese model for embeddings
tokenizer = AutoTokenizer.from_pretrained("NlpHUST/gpt2-vietnamese")
tokenizer.pad_token = tokenizer.eos_token
model = AutoModel.from_pretrained("NlpHUST/gpt2-vietnamese")

# Load knowledge base from data.txt
knowledge_base = {}
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("User:"):
            user_line = line.replace("User:", "").strip()
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line.startswith("Bot:"):
                    bot_line = next_line.replace("Bot:", "").strip()
                    if user_line and bot_line:
                        knowledge_base[user_line] = bot_line
            i += 2
        else:
            i += 1

print(f"✅ Loaded {len(knowledge_base)} Q&A pairs")
 

def get_embedding(text):
    """Get text embedding"""
    if not text or not text.strip():
        return torch.zeros(768).unsqueeze(0)
    
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)

def find_best_match(user_input, threshold=0.70):
    """Find best matching answer"""
    if not knowledge_base:
        return None
    
    user_embedding = get_embedding(user_input)
    best_match = None
    best_score = threshold
    best_question = None
    
    for question, answer in knowledge_base.items():
        q_embedding = get_embedding(question)
        similarity = torch.nn.functional.cosine_similarity(user_embedding, q_embedding).item()
        
        if similarity > best_score:
            best_score = similarity
            best_match = answer
            best_question = question
    
    return best_match

while True:
    user_input = input("Bạn: ")
    if user_input.lower() in ["exit", "quit", "thoát"]:
        break

    answer = find_best_match(user_input)
    print("Bot:", answer if answer else "Tôi không biết 🤔\n")
