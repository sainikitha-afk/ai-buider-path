def check_guardrails(query):
    banned = ["password", "credentials", "secret", "private"]

    if any(word in query.lower() for word in banned):
        return "❌ Access denied: Sensitive information request blocked."

    return None