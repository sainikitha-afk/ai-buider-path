import numpy as np
import faiss

def embed(text):
    return np.random.rand(384)

with open("data/rag_data.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = [c.strip() for c in text.split("\n") if c.strip()]
embeddings = [embed(c) for c in chunks]

index = faiss.IndexFlatL2(384)
index.add(np.array(embeddings).astype("float32"))

def rag_search(query):
    q = embed(query)
    D, I = index.search(np.array([q]).astype("float32"), k=2)
    results = [chunks[i] for i in I[0]]

    return f"""
[Research Knowledge Base]

{chr(10).join(results)}
"""