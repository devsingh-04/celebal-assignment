# generator/generate.py

import chromadb
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

print("[+] Loading ChromaDB and tiny-T5 model...")

# Load Chroma collection
client = chromadb.PersistentClient()
collection = client.get_collection(name="loan_docs")

# Load generator
model_name = "sshleifer/tiny-t5"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_answer(query):
    results = collection.query(query_texts=[query], n_results=3)
    context = " ".join(results["documents"][0])

    prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_new_tokens=100)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    question = "What factors influence loan approval?"
    response = generate_answer(question)
    print("\n🤖 Bot:", response)
