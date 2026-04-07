# 🕷️ Web Crawler Agent (AWS Bedrock Simulation)

## 📌 Overview
This project simulates a Web Crawler Agent inspired by AWS Bedrock Agents.

The agent:
- Accepts user queries
- Extracts URLs
- Uses a tool (`web_scrape`) to fetch webpage content
- Returns cleaned text snippets

---

## 🧠 Architecture

User Query  
↓  
Agent  
↓  
Tool: web_scrape  
↓  
Fetch + Clean HTML  
↓  
Return Text  

---

## ⚙️ How to Run

- ```bash
pip install -r requirements.txt
python main.py


---

# 🧪 TEST IT

Run:

- ```bash
python main.py

## Output 
![Demo Video](./demo.mp4)