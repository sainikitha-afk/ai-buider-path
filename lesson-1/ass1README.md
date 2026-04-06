# Assignment 1 — AI Model Comparison

Comparing GPT-4o, Claude Sonnet, Gemini Flash, and DeepSeek R1:7b (local via Ollama) across three core use cases from the AI Builder program. Same prompts, different models, real observations.

---

## Test Prompts Used

**Code Generation:** Write a Python function that connects to a PostgreSQL database, fetches all users where status = 'active', and returns them as a list of dicts.

**SQL Generation:** Write a SQL query to find the top 5 departments by average salary, only include departments with more than 10 employees, sorted descending.

**Infra Automation:** Write a Terraform configuration to deploy an AWS EC2 instance with t3.micro, attach a security group allowing SSH on port 22, and output the public IP.

---

## Comparison Table

| Criteria | GPT-4o | Claude Sonnet | Gemini Flash | DeepSeek R1:7b (Local) |
|---|---|---|---|---|
| Code Generation | Excellent | Excellent | Good | Basic |
| SQL Generation | Good | Good | Good | Basic |
| Infra Automation | Good | Excellent | Good | Basic |
| Ease of Use | Excellent | Excellent | Excellent | Basic |
| Speed / Latency | Excellent | Excellent | Excellent | Good |
| Comments | Clean output, good structure but hardcoded the SQL string directly — minor injection risk | Best overall quality. Used parameterized queries for SQL injection safety, added variables in Terraform instead of hardcoding, and included a bonus `ssh_command` output. Most production-aware of the four | Solid, readable output across all three. SQL query was slightly simplified (no department name join) but functional. Terraform was clean and demo-grade | Ran locally via Ollama — no cloud dependency which is the whole point. Noticeably slower and responses were more verbose/less structured. Needed follow-up prompting to clean up output. Good for offline/privacy use cases, not ready for production use as-is |

---

## Key Observations

**On Code Quality:**
Claude was the only model that used parameterized queries in the Python function (`%s` with a tuple) instead of interpolating the string directly. That's the difference between something that's *technically correct* and something that's actually safe to deploy.

**On Terraform:**
GPT and Gemini both hardcoded the region, AMI, and CIDR range — fine for a demo, would be a headache in any real setup. Claude separated everything into variables and even threw in a ready-to-copy `ssh_command` output. Small thing, big difference in usability.

**On Local Models:**
DeepSeek R1:7b on Ollama is genuinely impressive for a free, offline model. The output quality gap is real though — it needed more hand-holding through prompts and the Terraform output especially needed cleanup. For privacy-sensitive or air-gapped environments it makes sense. For speed and reliability it can't match the hosted models yet.

**On SQL:**
All four models got the `HAVING` vs `WHERE` distinction right (common mistake people make — `WHERE` runs before aggregation, `HAVING` runs after). Gemini's query skipped joining the departments table for the department name which means you'd only get IDs in the output, not names. Functional but less useful in practice.

---

## Setup Notes

- GPT-4o tested via chat.openai.com
- Claude Sonnet tested via claude.ai
- Gemini Flash tested via gemini.google.com
- DeepSeek R1:7b run locally using Ollama (`ollama pull deepseek-r1:7b`)

---

*Submitted as part of AI Builder Program — Lesson 1, Assignment 1*