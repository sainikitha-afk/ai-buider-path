# 🤖 Multi-Agent Support System — LangGraph Implementation

## 📌 Overview

This project implements a **multi-agent support system** using LangGraph, where multiple specialized agents collaborate to handle user queries.

The system includes:

* A **Supervisor Agent** for query classification
* An **IT Agent** for technical support queries
* A **Finance Agent** for financial queries

The agents work together in a structured graph workflow to provide accurate and context-aware responses.

---

## 🚀 Features

* 🧠 Multi-agent architecture (Supervisor + Specialists)
* 🔀 Dynamic routing using LangGraph
* 💻 IT support handling (VPN, software, devices)
* 💰 Finance support handling (reimbursement, payroll, budget)
* 🌐 Web context integration
* 📄 Internal document retrieval

---

## 🛠️ Tech Stack

* Python
* LangGraph
* LangChain (Ollama integration)
* Ollama (Local LLM runtime)
* phi3:mini (LLM)

---

## 🧠 Architecture

User Query
↓
Supervisor Agent (Classification)
↓
├── IT Agent → (ReadFile + WebSearch)
└── Finance Agent → (ReadFile + WebSearch)
↓
Final Response

---

## 📂 Project Structure

```id="s7l2jv"
lesson-5/
└── multi-agent/
    ├── main.py
    ├── agents.py
    ├── tools.py
    └── data/
        ├── it_docs.txt
        └── finance_docs.txt
```

---

## ⚙️ Agents Description

### 🧠 Supervisor Agent

* Classifies queries into:

  * IT
  * Finance
* Routes query to appropriate agent

---

### 💻 IT Agent

Handles:

* VPN setup
* Software approvals
* Laptop requests

Tools:

* ReadFile (internal IT docs)
* WebSearch (external info)

---

### 💰 Finance Agent

Handles:

* Reimbursements
* Payroll queries
* Budget reports

Tools:

* ReadFile (finance docs)
* WebSearch (external info)

---

## ▶️ How to Run

### 1. Install dependencies

````
pip install langgraph langchain-community
``` id="l7t7db"

### 2. Start Ollama
````

ollama serve

```id="4u2x9d"

### 3. Pull model
```

ollama pull phi3:mini

```id="l8x3pr"

### 4. Run the system
```

python main.py

```id="0vkmrq"

---

## 💬 Example Queries
- How to set up VPN?  
- What software is approved?  
- How to file reimbursement?  
- When is payroll processed?  

---

## 🎥 Demo Video
📹 [Watch Demo](./demo.mp4)

---

## 🧠 Key Concepts Demonstrated
- Multi-agent systems
- Supervisor-worker pattern
- LangGraph workflows
- Tool-based reasoning
- Context-aware responses

---

## ✅ Conclusion
This project demonstrates how multiple AI agents can collaborate using LangGraph to handle different types of queries efficiently.

It highlights the transition from single-agent systems to **multi-agent workflows with structured coordination and decision-making**.

---
```
