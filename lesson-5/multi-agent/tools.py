def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def web_search(query):
    return f"""
[Web Info]
General best practices related to: {query}
"""