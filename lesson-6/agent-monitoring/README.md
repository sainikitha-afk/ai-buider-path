# 📊 Agent Monitoring, Guardrails & Evaluation

## 📌 Overview
This project enhances a LangChain-based research agent with:

- Observability (LangFuse-style logging)
- Guardrails (NeMo-style safety)
- Evaluation (Agent performance metrics)

---

## 🚀 Features
- Tool-based agent (RAG, MCP, Web)
- Query logging and tracing
- Safety checks for sensitive queries
- Performance evaluation

---

## ⚙️ How to Run

- ```bash
pip install faiss-cpu numpy langchain-community
ollama serve
ollama pull phi3:mini
python main.py

## Output 
![Demo Video](./demo.mp4)