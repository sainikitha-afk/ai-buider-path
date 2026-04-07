from langgraph.graph import StateGraph
from typing import TypedDict

from agents import supervisor, it_agent, finance_agent

# ---- STATE ----
class State(TypedDict):
    query: str
    route: str
    answer: str

# ---- NODES ----
def supervisor_node(state: State):
    route = supervisor(state["query"])
    return {"route": route}

def it_node(state: State):
    answer = it_agent(state["query"])
    return {"answer": answer}

def finance_node(state: State):
    answer = finance_agent(state["query"])
    return {"answer": answer}

# ---- GRAPH ----
builder = StateGraph(State)

builder.add_node("supervisor", supervisor_node)
builder.add_node("it", it_node)
builder.add_node("finance", finance_node)

builder.set_entry_point("supervisor")

# routing logic
builder.add_conditional_edges(
    "supervisor",
    lambda state: state["route"],
    {
        "it": "it",
        "finance": "finance"
    }
)

builder.set_finish_point("it")
builder.set_finish_point("finance")

graph = builder.compile()

# ---- RUN LOOP ----
while True:
    query = input("Ask: ")

    if query.lower() == "exit":
        break

    result = graph.invoke({"query": query})

    print("\nAnswer:", result["answer"])