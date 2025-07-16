# app.py

import streamlit as st
import chromadb
from chromadb.utils import embedding_functions
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# ✅ Set Streamlit page config
st.set_page_config(page_title="LoanGPT", layout="wide", page_icon="💼")

# ✅ Title and description
st.title("🏦 Loan Approval RAG Chatbot")
st.markdown("Ask anything about loan approvals. Powered by RAG and Generative AI 💬🚀")

# ✅ Session state setup
if "query_count" not in st.session_state:
    st.session_state["query_count"] = 0
if "query_log" not in st.session_state:
    st.session_state["query_log"] = []

# ✅ Sidebar UI
st.sidebar.metric("📈 Queries Today", st.session_state["query_count"])
show_context = st.sidebar.checkbox("🔍 Show retrieved chunks", value=False)

# ✅ Clear session button
if st.sidebar.button("🗑️ Clear Session"):
    st.session_state["query_log"] = []
    st.session_state["query_count"] = 0
    st.sidebar.success("Session cleared!")

# ✅ Query history display
if st.session_state["query_log"]:
    st.sidebar.markdown("### 🕓 Query History")
    for i, q in enumerate(reversed(st.session_state["query_log"]), 1):
        st.sidebar.markdown(f"**{i}.** {q}")

# ✅ Load ChromaDB client
client = chromadb.PersistentClient(path="../chroma_db")

# ✅ Load embedding function
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# ✅ Refresh collection to avoid embedding conflict
existing_collections = [col.name for col in client.list_collections()]
if "loan_docs" in existing_collections:
    client.delete_collection(name="loan_docs")

collection = client.create_collection(name="loan_docs", embedding_function=embedding_function)

# ✅ Load FLAN-T5 model and tokenizer
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
    return tokenizer, model

tokenizer, model = load_model()

# 🔍 Retrieve top K documents from vector DB
def get_top_k_docs(query, k=3):
    results = collection.query(query_texts=[query], n_results=k)
    return results["documents"][0]

# 🤖 Generate answer using FLAN-T5
def generate_answer(query):
    docs = get_top_k_docs(query)
    context = " ".join(docs)
    prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(**inputs, max_new_tokens=100)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer, docs

# 🌐 Streamlit UI for user input and response
st.subheader("📊 Ask anything about loan approvals based on the available documents.")
user_query = st.text_input("💬 Your question")

if user_query:
    try:
        with st.spinner("Generating response..."):
            response, top_chunks = generate_answer(user_query)
            st.session_state["query_count"] += 1
            st.session_state["query_log"].append(user_query)

        st.success("✅ Response:")
        st.write(response)

        if show_context:
            with st.expander("🧠 Retrieved Context Chunks"):
                for i, chunk in enumerate(top_chunks, 1):
                    st.markdown(f"**Chunk {i}**: {chunk}")

    except Exception as e:
        st.error("❌ Something went wrong while generating the response.")
        st.exception(e)

# ✅ Footer
st.markdown("---")
st.markdown("Developed with ❤️ by Dev Singh | Celebal Assignment 8 | July 2025")
# ✅ License
st.markdown("This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.")
# ✅ Acknowledgements
st.markdown("Special thanks to the open-source community for their contributions and support.")     
# ✅ End of app.py
# ✅ Note: Ensure you have the required packages installed in your environment.
# ✅ Use `pip install -r requirements.txt` to install dependencies. 
