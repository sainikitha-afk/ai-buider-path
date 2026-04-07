# 🔍 Internal Research Agent — LangChain (Materials AI Project)

## 📌 Overview

This project implements an **Internal Research Agent** using LangChain that can answer complex research queries by dynamically selecting from multiple tools.

The agent is designed around a **materials science use case**, specifically focused on predicting mechanical properties of A356 aluminum alloys using physics-informed approaches.

---

## 🚀 Features

* 🤖 LangChain-based AI Agent (ReAct framework)
* 📄 RAG Tool for technical research knowledge
* 🔧 MCP Tool (simulated) for internal project insights
* 🌐 Web Tool for external industry trends
* 🧠 Dynamic tool selection based on query
* 💻 Fully local setup using Ollama (no API cost)

---

## 🛠️ Tech Stack

* Python
* LangChain
* FAISS (Vector Database)
* NumPy
* Ollama (Local LLM runtime)
* phi3:mini (LLM)

---

## 🧠 Architecture

User Query
↓
LangChain Agent (ReAct)
↓
Tool Selection
├── RAG Tool (Research Knowledge Base)
├── MCP Tool (Internal Project Docs)
└── Web Tool (Industry Trends)
↓
Final Response

---

## 📂 Project Structure

```
lesson-4/
└── research-agent/
    ├── main.py
    ├── rag_tool.py
    ├── mcp_tool.py
    ├── web_tool.py
    ├── data/
    │   ├── rag_data.txt
    │   └── internal_docs.txt
    ├── embeddings.pkl
    ├── requirements.txt
    └── demo.mp4
```

---

## ⚙️ Tools Explanation

### 📄 RAG Tool — Materials Research

* Retrieves information from technical dataset
* Covers:

  * Orowan strengthening mechanism
  * Microstructure-property relationships
  * Physics-informed ML concepts

---

### 🔧 MCP Tool — Internal Research Docs

* Simulates internal company knowledge
* Includes:

  * Q1 research insights
  * project findings
  * experimental observations

---

### 🌐 Web Tool — Industry Insights

* Provides external context such as:

  * AI trends in materials science
  * adoption of PINNs
  * industry benchmarks

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install langchain langchain-community faiss-cpu numpy requests
```

### 2. Start Ollama

```
ollama serve
```

### 3. Pull required model

```
ollama pull phi3:mini
```

### 4. Run the agent

```
python main.py
```

---

## 💬 Example Queries

* Explain the Orowan strengthening mechanism
* Why do traditional ML models fail in this dataset?
* Summarize internal research findings
* Compare physics-informed models with ML
* What are industry trends in materials AI?

---

## 🎥 Demo Video

📹 [Watch Demo](./demo.mp4)

---

## 🧠 Key Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* Agent-based decision making
* ReAct framework (Reason + Act)
* Tool calling in LLM systems
* Multi-source information integration

---

## ✅ Conclusion

This project demonstrates how an **AI agent can intelligently combine multiple tools** to deliver accurate, contextual, and research-oriented responses.

It showcases the transition from simple LLM applications to **full AI systems with reasoning, retrieval, and tool usage**.

---
