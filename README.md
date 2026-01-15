# 🧠 ResearchBot: Autonomous Research Agent with Long-Term Memory

**ResearchBot** is an intelligent agent designed to perform autonomous web research while maintaining long-term conversation memory. Unlike standard chatbots, ResearchBot uses an **Agentic Workflow** (LangGraph) to decide *when* to search the internet and *how* to answer complex queries.

It solves the "Goldfish Memory" problem of LLMs by implementing a persistent database layer that remembers every user interaction across different sessions.

---

## 🚀 Key Features
* **🧠 Cognitive Architecture:** Uses **Llama 3 (via Groq)** for sub-second reasoning and decision making.
* **🕵️ Autonomous Research:** Integrated with **Tavily API** to fetch real-time data from the web (e.g., current events, stock prices).
* **💾 Long-Term Memory:** Stores conversation history in a **SQL Database (SQLite)**, allowing the agent to recall past context.
* **🛡️ Robust Backend:** Built with **FastAPI** for high-performance, asynchronous API handling.
* **🐳 Containerized:** Fully Dockerized application for consistent deployment across environments.

---

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Backend:** FastAPI, SQLModel (SQLAlchemy)
* **Frontend:** Streamlit
* **AI & Agents:** LangChain, LangGraph, Groq API
* **Tools:** Tavily Search API
* **DevOps:** Docker

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/TeenaMandaar/ResearchBot-AI]
cd ResearchBot-AI
cd code
```

### 2. Set Up Environment Variables
Create a .env file in the code directory and add your API keys:
``` bash 
GROQ_API_KEY="your_groq_key"
TAVILY_API_KEY="your_tavily_key" 
```

### 3. Run Locally
Install Dependencies:

```bash
pip install -r requirements.txt
```

Start the Backend Server:

```bash
uvicorn app.main:app --reload
```
Start the Frontend UI (In a new terminal):

```bash
cd code
streamlit run frontend/ui.py

```

### 4. Run with Docker (Optional)
```bash

docker build -t research-bot .
docker run -p 8000:8000 research-bot
```