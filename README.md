# LangGRAPH

# 🤖 Simple AI Agent with LangGraph

This is a basic AI Agent built using [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://www.langchain.com/), and OpenAI's GPT models. It showcases how to build a stateful multi-step agent workflow that integrates a simple tool and handles memory.

## 📌 Features

- 🧠 LLM Integration (OpenAI GPT-4)
- 🔁 LangGraph multi-step agent workflow
- 🛠️ Tool use (AI Agent can be made to use alot of thing inculding, webservices, crawling into websites etc.)
- 💾 Basic memory structure
- ⚡ Async and modular structure (extensible for more tools and workflows)

---

## 🏗️ Architecture

```mermaid
graph LR
A[User Input] --> B[LLM Response Node]
B --> C{Tool Trigger?}
C -->|Yes| D[Math Tool]
C -->|No| E[Final Output]
D --> E
