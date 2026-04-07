from agent import agent

while True:
    query = input("Ask: ")

    if query.lower() == "exit":
        break

    result = agent(query)

    print("\nResponse:\n", result[:500], "\n")