# 📚 AI Multi Document RAG
Chat with multiple PDF documents simultaneously using the power of RAG (Retrieval-Augmented Generation)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![LangChain](https://img.shields.io/badge/LangChain-latest-green)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20DB-orange)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-blue?logo=google)

---

## 📌 About

AI Multi Document RAG is a production-style AI application that solves a real problem — **information overload**. Instead of manually reading through multiple PDFs, you upload them, ask your question, and get an accurate answer with exact source references in seconds.

Built to demonstrate end-to-end RAG pipeline engineering using modern LLM frameworks and vector search.

---

## 😤 Problem It Solves

> *"I have 5 research papers, 3 reports and 2 manuals. Finding a specific answer means reading everything manually — that takes hours."*

**Solution:** Upload all PDFs at once → Ask anything → Get accurate answers with page-level source citations — powered by semantic search and Groq LLaMA 3.3.

---

## ✨ Features

- 📄 **Multi PDF Upload** — upload and query multiple documents simultaneously
- 🧠 **Google Gemini Embeddings** — deep semantic understanding of document content
- ⚡ **Google Gemini (gemini-2.5-flash)** — fast, accurate answers grounded in your documents
- 🔍 **Source Citations** — every answer shows exactly which document and page it came from
- 🛡️ **Hallucination Prevention** — model strictly answers from uploaded content only
- 📄 **Retrieved Chunks View** — see the exact text used to generate the answer
- 🎨 **Clean Streamlit UI** — intuitive and easy to use

---

## 🗂️ Project Structure

```
ai-multi-document-rag/
│
├── ingest.py          # PDF loading, chunking, embedding, FAISS index creation
├── rag.py             # Vectorstore loading, retrieval, Groq answer generation
├── app.py             # Streamlit frontend — user interface
├── data/
│   └── documents/     # Place your PDF files here for CLI usage
├── faiss_index/       # Auto-generated FAISS vector store
├── requirements.txt   # All dependencies
└── .env               # API keys (not committed to Git)
```
---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| 🐍 Language | Python 3.10+ |
| 🔗 RAG Framework | LangChain |
| 🗄️ Vector Database | FAISS |
| 🧬 Embeddings | Google Gemini (gemini-embedding-001) |
| 🤖 LLM | Google Gemini — gemini-2.5-flash |
| 📄 PDF Loader | LangChain PyPDFLoader |
| 🎨 Frontend | Streamlit |

---

## ⚙️ How It Works

```
Upload PDF Files (multiple supported)
        │
        ▼
Extract Text (PyPDFLoader — page by page)
        │
        ▼
Split into Chunks (RecursiveCharacterTextSplitter)
chunk_size=1000 | chunk_overlap=200
        │
        ▼
Embed with Google Gemini → 3072 dimensional vectors
        │
        ▼
Store in FAISS Vector Database
        │
        ▼
User asks a question
        │
        ▼
Semantic Search → Top 3 Most Relevant Chunks
        │
        ▼
Google Gemini (gemini-2.5-flash) generates answer from context
        │
        ▼
Answer + Source Citations returned ✅
```
---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Abdul-Samad43/ai-multi-document-rag.git
cd ai-multi-document-rag
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory:
GOOGLE_API_KEY=your_google_api_key_here
- Get Google API key: https://aistudio.google.com

### 4. Run the App

```bash
streamlit run app.py
```

---

## 📋 Requirements
langchain
langchain-community
langchain-google-genai
langchain-core
langchain-text-splitters
faiss-cpu
pypdf
streamlit
python-dotenv
---

## 🌍 Real World Use Cases

| Use Case | Example |
|---|---|
| 📖 Research | Query multiple research papers at once |
| ⚖️ Legal | Extract clauses from contracts and agreements |
| 🏢 Business | Search through company reports and manuals |
| 🎓 Education | Study from multiple textbooks simultaneously |
| 🏥 Healthcare | Query medical documents and patient records |

---

> ⚠️ **Note:** Due to cloud server restrictions, this app works best when run locally. Clone the repo and run `streamlit run app.py` on your machine.

---

## 👨‍💻 Author

**Abdul Samad** — AI Engineering Student

[![GitHub](https://img.shields.io/badge/GitHub-Abdul--Samad43-black?logo=github)](https://github.com/Abdul-Samad43)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Abdul%20Samad-0A66C2?logo=linkedin)](https://www.linkedin.com/in/abdul-samad-95541a388)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with ❤️ using LangChain, FAISS and Google Gemini*
