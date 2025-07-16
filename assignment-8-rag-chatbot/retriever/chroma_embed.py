# retriever/chroma_embed.py

from sentence_transformers import SentenceTransformer
import pandas as pd
import chromadb
from chromadb.utils import embedding_functions

# Load and preprocess your training dataset
df = pd.read_csv("../data/training_dataset.csv")
docs = []

for _, row in df.iterrows():
    doc = f"Gender: {row['Gender']}, Married: {row['Married']}, ApplicantIncome: {row['ApplicantIncome']}, Credit_History: {row['Credit_History']}, Loan_Status: {row['Loan_Status']}"
    docs.append(doc)

# Init Chroma DB
client = chromadb.PersistentClient(path="../chroma_db")
collection = client.get_or_create_collection(name="loan_docs")


embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# Add documents
collection.add(documents=docs, ids=[str(i) for i in range(len(docs))])

