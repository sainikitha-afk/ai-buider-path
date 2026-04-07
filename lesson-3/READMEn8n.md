## Assignment 2 — Smart Gmail Agent with n8n

An n8n workflow that classifies incoming support queries using an AI agent and automatically routes emails to the right users based on their role.

---

## What it does

When a query comes in, the agent reads it, figures out whether it's a customer-facing issue or something that needs admin/technical attention, fetches the user list from an API, filters by the matched role, and sends an email to every user that qualifies.

```
Query → AI Agent classifies role → HTTP fetch users → Filter by role → Send Gmail to matched users
```

---

## Workflow

| Node | Type | What it does |
|---|---|---|
| When chat message received | Trigger | Entry point — accepts the incoming query |
| AI Agent | AI | Classifies the query as `customer` or `admin` |
| HTTP Request (Tool) | Tool | Fetches mock users from the API |
| Code in JavaScript | Code | Filters users by the classified role |
| Send a message | Gmail | Sends email to every matched user |

---

## Classification Logic

| Role | Query Types |
|---|---|
| `customer` | Product Inquiry, General Support, Sales Question, Billing Inquiry, Feature Request |
| `admin` | Technical Escalation, System Issue, Security Concern, Data Issue, Integration Problem |

---

## Setup

1. Import `workflow.json` into your n8n instance
2. Connect your Gmail account in the **Send a message** node
3. Add your OpenAI / Ollama credentials in the **AI Agent** node
4. Hit **Test workflow** and type a query in the chat

---

## Example Queries to Test

**Customer route:**
```
I was charged twice for this month's subscription. Can someone from billing review my account?
```

**Admin route:**
```
URGENT: Our API integration is down and affecting production systems. Need immediate support.
```

---

## Demo

![Demo Video](demo.mp4)

---

## How it actually works (the non-copy-paste explanation)

**Why an AI Agent and not just an if/else?**
A hardcoded if/else would break the moment someone phrases a billing question differently. The AI agent understands intent — "I got charged twice" and "there's a duplicate transaction on my account" both map to the same category even though the words are completely different.

**What is the HTTP Request Tool doing?**
The agent has access to a "tool" — essentially a function it can call mid-reasoning. When it decides on a role, it calls the HTTP tool to fetch the user list from `https://api.escuelajs.co/api/v1/users`. This is what makes it agentic — it's not just classifying, it's taking action based on the classification.

**Why does the Code node re-fetch the users?**
The agent's text output is unpredictable — sometimes it summarizes the users, sometimes it lists them, sometimes it doesn't include them at all. Instead of trying to parse the agent's free-text response, the Code node fetches the users itself and filters cleanly by role. More reliable.

**What is FAISS / RAG doing here?**
Nothing — this assignment doesn't use RAG. The agent uses live API data, not a vector store. RAG is for when you need to retrieve from a static document corpus. Here the "knowledge" (user list) is dynamic and comes from an API call at runtime.

---

*Submitted as part of AI Builder Program — Lesson 1, Assignment 2*
