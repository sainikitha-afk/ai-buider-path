import numpy as np
import faiss
import requests
import pickle
import os

# ---- CONFIG ----
OLLAMA_BASE = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL = "phi3:mini"
CACHE_FILE = "embeddings.pkl"

# ---- EMBEDDING FUNCTION ----
def get_embedding(text):
    response = requests.post(
        f"{OLLAMA_BASE}/api/embeddings",
        json={"model": EMBED_MODEL, "prompt": text}
    )
    data = response.json()

    if "embedding" not in data:
        raise Exception(f"Embedding error: {data}")

    return data["embedding"]

# ---- LOAD DATA ----
with open("data/tigers.txt", "r", encoding="utf-8") as f:
    text = f.read()

# ---- CLEAN + CHUNK ----
chunks = [chunk.strip() for chunk in text.split("\n") if chunk.strip()]

# ---- LOAD OR CREATE EMBEDDINGS ----
if os.path.exists(CACHE_FILE):
    print("⚡ Loading cached embeddings...")
    with open(CACHE_FILE, "rb") as f:
        embeddings = pickle.load(f)
else:
    print(f"⏳ Generating embeddings for {len(chunks)} chunks using {EMBED_MODEL}...")
    embeddings = [get_embedding(chunk) for chunk in chunks]

    with open(CACHE_FILE, "wb") as f:
        pickle.dump(embeddings, f)

    print("✅ Embeddings cached!")

# ---- VECTOR STORE ----
dimension = len(embeddings[0])
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings).astype("float32"))

print(f"📦 Indexed {len(chunks)} chunks.")
print(f"🤖 Chat model: {CHAT_MODEL}")
print("-" * 50)
print("💬 RAG Chatbot ready! Type 'exit' to quit.\n")

# ---- RETRIEVE ----
def retrieve(query, k=2):
    query_embedding = get_embedding(query)
    D, I = index.search(np.array([query_embedding]).astype("float32"), k=k)
    return [chunks[i] for i in I[0]]

# ---- ASK MODEL ----
def ask_ollama(messages):
    try:
        response = requests.post(
            f"{OLLAMA_BASE}/api/chat",
            json={
                "model": CHAT_MODEL,
                "messages": messages,
                "stream": False
            }
        )

        data = response.json()

        if "error" in data:
            return f"[Model Error: {data['error']}]"

        if "message" in data:
            return data["message"]["content"]
        elif "response" in data:
            return data["response"]
        else:
            return f"[Unexpected response: {data}]"

    except Exception as e:
        return f"[Request failed: {str(e)}]"

# ---- CHAT LOOP ----
conversation_history = []

while True:
    query = input("You: ").strip()

    if query.lower() == "exit":
        print("👋 Bye!")
        break

    if not query:
        continue

    retrieved_chunks = retrieve(query)
    context = "\n".join(retrieved_chunks)

    messages = [
        {
            "role": "system",
            "content": (
                "You are a wildlife expert. "
                "Answer ONLY using the provided context. "
                "If the answer is not present, say you don't know."
            )
        }
    ]

    messages.extend(conversation_history)

    messages.append({
        "role": "user",
        "content": f"Context:\n{context}\n\nQuestion: {query}"
    })

    print("\nBot: ", end="", flush=True)
    answer = ask_ollama(messages)
    print(answer)
    print()

    # store history
    conversation_history.append({"role": "user", "content": query})
    conversation_history.append({"role": "assistant", "content": answer})

    # limit memory
    if len(conversation_history) > 10:
        conversation_history = conversation_history[-10:]