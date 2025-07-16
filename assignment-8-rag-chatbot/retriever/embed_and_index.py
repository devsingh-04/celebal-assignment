# embed_and_index.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

# List of knowledge facts (you can later load this from a JSON or DB too)
chunks = [
    "Applicants with credit history = 0 had an approval rate of 0.08.",
    "Applicants with credit history = 1 had an approval rate of 0.79.",
    "Female applicants had a loan approval rate of 0.67.",
    "Male applicants had a loan approval rate of 0.69.",
    "Applicants with income above 6000 had a loan approval rate of 0.66.",
    "Graduate applicants had a loan approval rate of 0.71.",
    "Not Graduate applicants had a loan approval rate of 0.61.",
    "Self-employed status = No had a loan approval rate of 0.69.",
    "Self-employed status = Yes had a loan approval rate of 0.68.",
    "Applicants from Urban area had a loan approval rate of 0.68.",
    "Applicants from Semiurban area had a loan approval rate of 0.77.",
    "Applicants from Rural area had a loan approval rate of 0.63.",
]

# Load sentence transformer model
print("[+] Loading embedding model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

# Encode the chunks to vector embeddings
print("[+] Encoding knowledge chunks...")
embeddings = model.encode(chunks).astype('float32')

# Create and store FAISS index
print("[+] Creating FAISS index...")
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Save index and chunks to file
print("[+] Saving index and chunks...")
faiss.write_index(index, "faiss_index.index")
np.save("chunks.npy", np.array(chunks))

print("[✓] Embedding and indexing complete.")
