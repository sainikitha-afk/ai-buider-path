import numpy as np
import faiss

# ---- FAKE EMBEDDING ----
def embed(text):
    return np.random.rand(384)

# ---- LOAD RAG DATA ----
with open("data/rag_data.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = [c.strip() for c in text.split("\n") if c.strip()]
embeddings = [embed(c) for c in chunks]

index = faiss.IndexFlatL2(384)
index.add(np.array(embeddings).astype("float32"))

def rag_tool(query):
    q = embed(query)
    D, I = index.search(np.array([q]).astype("float32"), k=2)
    return "\n".join([chunks[i] for i in I[0]])

# ---- INTERNAL DOCS ----
with open("data/internal_docs.txt", "r", encoding="utf-8") as f:
    internal_data = f.read()

def mcp_tool(query):
    return internal_data

# ---- WEB TOOL ----
def web_tool(query):
    return f"""
AI in materials science is growing rapidly.
Physics-informed models are widely used.
Related to: {query}
"""