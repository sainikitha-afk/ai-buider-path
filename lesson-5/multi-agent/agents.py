from langchain_community.llms import Ollama
from tools import read_file, web_search

llm = Ollama(model="phi3:mini")

# ---- IT AGENT ----
def it_agent(query):
    docs = read_file("data/it_docs.txt")

    context = f"""
IT Documentation:
{docs}

Web Info:
{web_search(query)}
"""

    prompt = f"""
You are an IT support assistant.

Use the context below to answer:

{context}

Question: {query}
"""

    return llm.invoke(prompt)


# ---- FINANCE AGENT ----
def finance_agent(query):
    docs = read_file("data/finance_docs.txt")

    context = f"""
Finance Documentation:
{docs}

Web Info:
{web_search(query)}
"""

    prompt = f"""
You are a finance support assistant.

Use the context below to answer:

{context}

Question: {query}
"""

    return llm.invoke(prompt)


# ---- SUPERVISOR ----
def supervisor(query):
    q = query.lower()

    if any(word in q for word in ["vpn", "software", "laptop", "it"]):
        return "it"
    elif any(word in q for word in ["reimbursement", "payroll", "budget", "finance"]):
        return "finance"
    else:
        return "it"