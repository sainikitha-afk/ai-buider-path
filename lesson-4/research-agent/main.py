from langchain_community.llms import Ollama

from rag_tool import rag_search
from web_tool import web_search
from mcp_tool import mcp_search

# ---- LLM ----
llm = Ollama(model="phi3:mini")

# ---- TOOL MAP ----
tools = {
    "rag": rag_search,
    "web": web_search,
    "mcp": mcp_search
}

# ---- AGENT DECISION ----
def choose_tool(query):
    q = query.lower()

    if "policy" in q or "compliance" in q:
        return "rag"
    elif "trend" in q or "industry" in q:
        return "web"
    elif "internal" in q or "research" in q:
        return "mcp"
    else:
        return "rag"

# ---- MAIN LOOP ----
while True:
    query = input("Ask: ")

    if query.lower() == "exit":
        break

    tool_name = choose_tool(query)
    print(f"\n[Agent] Using tool: {tool_name.upper()}")

    tool_result = tools[tool_name](query)

    prompt = f"""
You are an intelligent research assistant.

Use the following context to answer:

{tool_result}

Question: {query}
"""

    response = llm.invoke(prompt)

    print("\nAnswer:", response)