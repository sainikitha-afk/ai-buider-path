#  RAG Chatbot — Tiger Conservation Assistant

##  Overview
This project implements a **Retrieval-Augmented Generation (RAG) chatbot** that answers questions about tiger conservation in India using a custom knowledge base.

The chatbot retrieves relevant information from stored data and generates accurate, context-aware responses using a local language model.

---

## Features
-  Retrieval-Augmented Generation (RAG)
-  Context-aware answers from custom dataset
-  Fast responses using cached embeddings
-  Conversation memory (chat history)
-  Fully local setup (no API required)

---

## Tech Stack
- Python
- FAISS (Vector Database)
- Ollama (Local LLM runtime)
- **phi3:mini** (Chat Model)
- nomic-embed-text (Embedding Model)
- NumPy

---

## Project Structure
- rag-chatbot/
    ├── main.py
    ├── embeddings.pkl
    ├── data/
    │ └── tigers.txt
    ├── requirements.txt
    └── demo.mp4 

---

## Dataset
The dataset contains real-world information about:
- Project Tiger initiative
- Tiger population statistics
- Structure of tiger reserves
- Conservation challenges

The content was collected and cleaned from publicly available sources.

---

## How It Works
1. Load dataset (tigers.txt)
2. Split text into chunks
3. Convert chunks into embeddings using `nomic-embed-text`
4. Store embeddings in FAISS vector database
5. Retrieve relevant chunks based on user query
6. Send context + query to `phi3:mini`
7. Generate accurate response

---

## ▶️ How to Run

### 1. Install dependencies
- pip install faiss-cpu numpy requests
### 2. Install Ollama
- Download from: https://ollama.com
### 3. Pull required models
- ollama pull phi3:mini
  ollama pull nomic-embed-text
### 4. Run the chatbot
- python main.py

--- 

## Example Questions
- What is Project Tiger?
- How many tigers are there in India?
- What are the threats to tiger conservation?
- Which state has the most tiger reserves?

---

## Demo Video
📹 [Watch Demo](./demo.mp4)

---

## Key Learnings
- Understanding of RAG pipeline
- Working with vector databases (FAISS)
- Using local LLMs with Ollama
- Handling embeddings and retrieval
- Building context-aware AI systems

---

##  Conclusion
This project demonstrates how a **RAG-based chatbot** can be built from scratch using local models, enabling efficient and cost-free AI applications.

---