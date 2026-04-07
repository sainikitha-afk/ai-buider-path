from langchain_community.llms import Ollama
import time

from tools import rag_tool, mcp_tool, web_tool
from guardrails import check_guardrails

llm = Ollama(model="phi3:mini")

tools = {
    "rag": rag_tool,
    "mcp": mcp_tool,
    "web": web_tool
}

def choose_tool(query):
    q = query.lower()

    if "policy" in q or "mechanism" in q:
        return "rag"
    elif "internal" in q or "research" in q:
        return "mcp"
    elif "trend" in q or "industry" in q:
        return "web"
    else:
        return "rag"

while True:
    query = input("Ask: ")

    if query.lower() == "exit":
        break

    # ---- GUARDRAILS ----
    blocked = check_guardrails(query)
    if blocked:
        print(blocked)
        continue

    start_time = time.time()

    tool_name = choose_tool(query)
    tool_output = tools[tool_name](query)

    prompt = f"""
You are an intelligent research assistant.

Context:
{tool_output}

Question: {query}
"""

    print("\n--- OBSERVABILITY LOG ---")
    print("User Query:", query)
    print("Tool Used:", tool_name)
    print("Prompt:", prompt[:200])
    print("Token Usage: Approx (local model)")

    response = llm.invoke(prompt)

    end_time = time.time()

    print("Response:", response)
    print("Latency:", round(end_time - start_time, 2), "seconds")
    print("--- END LOG ---\n")