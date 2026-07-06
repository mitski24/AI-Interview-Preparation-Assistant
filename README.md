# PrepAI

AI-Powered RAG-Based Interview Preparation Assistant.

PrepAI is a full-stack Retrieval-Augmented Generation (RAG) chatbot designed for interview preparation using uploaded study materials.

---

# Features

- Upload PDF, DOCX, TXT, CSV files
- Semantic search using FAISS
- AI-powered contextual responses
- Mock interview mode
- AI answer evaluation
- Modern ChatGPT-style UI
- RAG architecture implementation

---

# Tech Stack

## Frontend
- React
- Vite
- TailwindCSS

## Backend
- Flask
- Flask-CORS

## AI / RAG
- Groq API
- Llama 3.1 8B Instant
- sentence-transformers
- FAISS

---

# Project Structure

```plaintext
PrepAI/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── rag/
│   ├── uploads/
│   └── vectorstore/
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
├── README.md
└── .gitignore
```

---

# Setup Instructions

# Backend Setup

## 1. Open backend folder

```bash
cd backend
```

---

## 2. Create virtual environment

```bash
python3 -m venv venv
```

---

## 3. Activate environment

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\\Scripts\\activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Create .env file

Create:

```plaintext
backend/.env
```

Add:

```env
GROQ_API_KEY=your_groq_api_key
```

Get free API key from:

https://console.groq.com

---

## 6. Run backend

```bash
python app.py
```

Runs on:

```plaintext
http://127.0.0.1:5000
```

---

# Frontend Setup

## 1. Open frontend

```bash
cd frontend
```

---

## 2. Install packages

```bash
npm install
```

---

## 3. Run frontend

```bash
npm run dev
```

Runs on:

```plaintext
http://localhost:5173
```

---

# How to Use

1. Upload interview preparation documents
2. Ask questions in chat
3. View retrieved document chunks
4. Use mock interview mode
5. Get AI evaluations and feedback

---

# Supported File Types

- PDF
- DOCX
- TXT
- CSV

---

# RAG Workflow

1. File Upload
2. Text Extraction
3. Chunking
4. Embedding Generation
5. FAISS Storage
6. Semantic Retrieval
7. AI Response Generation

---

# Future Improvements

- Authentication
- Persistent database
- Streaming responses
- Voice interview mode
- Deployment

---

# Author

Payal A Bhavesh
# AI-Interview-Preparation-Assistant
AI-powered RAG-based interview preparation assistant using uploaded study materials.
