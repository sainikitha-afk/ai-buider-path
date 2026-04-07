with open("data/internal_docs.txt", "r", encoding="utf-8") as f:
    company_data = f.read()

def mcp_search(query):
    return f"""
[Internal Research Insights]

{company_data}
"""