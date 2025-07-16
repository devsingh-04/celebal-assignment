# 🏦 LoanGPT – RAG-Based Loan Approval Chatbot

> 🎯 **Assignment 8 – Celebal Technologies Internship (July 2025)**  
> Built by **Dev Singh**, Final Year B.Tech CSE, Manipal University Jaipur

---

## 🚀 Project Overview

**LoanGPT** is a Retrieval-Augmented Generation (RAG) based chatbot that answers user queries regarding loan approvals using a custom dataset. It leverages:

- 📚 **ChromaDB** as a vector database for fast semantic retrieval
- 🧠 **Sentence Transformers** for high-quality embeddings
- 💬 **FLAN-T5** for intelligent, generative responses
- 📊 **Streamlit** for an interactive web UI

---

## 🧠 How It Works

1. **Embedding Phase (`chroma_embed.py`)**  
   - Reads training data  
   - Converts loan-related text into embeddings  
   - Stores them in a ChromaDB vector store

2. **Retrieval + Generation (`app.py`)**  
   - Accepts user query via Streamlit UI  
   - Retrieves top relevant document chunks from ChromaDB  
   - Combines context with query  
   - Feeds it into the FLAN-T5 model to generate a response

---

## 📂 Project Structure

assignment-8-rag-chatbot/
│
├── app.py # Streamlit app UI & logic
├── retriever/
│ └── chroma_embed.py # Vector DB embedder
├── generator/
│ └── generate.py # (Optional script)
├── data/
│ ├── Training Dataset.csv
│ ├── Test Dataset.csv
│ └── Sample_Submission.csv
├── requirements.txt
├── README.md
└── .gitignore



---

## ⚙️ Tech Stack

| Component       | Tech Used                              |
|----------------|-----------------------------------------|
| Language        | Python 3.10                             |
| Embeddings      | `sentence-transformers` (MiniLM-L6-v2)  |
| Vector Store    | ChromaDB                                |
| Gen Model       | FLAN-T5 (from HuggingFace Transformers) |
| Frontend        | Streamlit                               |

---




### 🧪 3. Features Implemented

✅ RAG-based document-aware chatbot  
✅ Query logging with `st.session_state`  
✅ Real-time query count metric  
✅ Toggle to view retrieved document chunks  
✅ Context preview using `st.expander`

---

### 📘 4. Dataset Used

Located in the `data/` folder:

- `Training Dataset.csv` – used for context generation  
- `Test Dataset.csv` – placeholder for future use  
- `Sample_Submission.csv` – format reference

---

### 🧠 5. How It Works

1. User inputs a loan-related question in the Streamlit UI  
2. Top 3 relevant text chunks are retrieved via ChromaDB (vector DB)  
3. The retrieved chunks are used as context for FLAN-T5  
4. A generative answer is produced using the prompt + context  
5. Query is logged and optionally, context is shown

---

### 💡 6. Future Improvements

- 🔐 Add Streamlit authentication (`streamlit-authenticator`)  
- 📊 Admin analytics dashboard (query heatmap, logs, etc.)  
- 🎙 Speech-to-text input support (via `SpeechRecognition` or Whisper)  
- 🧮 Model confidence score visualizations for transparency

---

### 🙌 7. Acknowledgments

- 🤗 HuggingFace Transformers & Datasets  
- 🧠 SentenceTransformers (for `all-MiniLM-L6-v2`)  
- 📦 ChromaDB – lightweight local vector store  
- 👨‍💼 Celebal Technologies – for internship opportunity & challenge  

---

### 👤 8. Author

**Dev Singh**  
🎓 Manipal University Jaipur – B.Tech CSE  
🔗 [LinkedIn](https://www.linkedin.com/) *(Replace with your actual profile)*

---

### 📁 9. Project Repo
assignment-8-rag-chatbot/
│
├── generator/ # Response generation logic
├── retriever/ # Embedding & ChromaDB indexing
├── interface/ # Streamlit chatbot interface
├── data/ # Training, test, and sample submission CSVs
└── README.md # 📘 You are here


GitHub Repo: [celebal-assignment](https://github.com/yourusername/celebal-assignment) *(Update URL if needed)*

---

### 🏁 10. Final Note

> "Built with 💼, 💡, and 💬 – because AI isn't just the future, it's the now."

This chatbot was developed as an **industry-facing GenAI solution** to demonstrate real-world applications of **RAG**, **NLP**, and **vector databases** in financial technology.

---

## 📦 Setup & Usage

### 🔧  Install Dependencies
```bash
pip install -r requirements.txt
cd retriever
python3 chroma_embed.py
cd ..
streamlit run app.py












