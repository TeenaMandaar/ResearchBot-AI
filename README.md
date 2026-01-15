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

```git clone [https://github.com/TeenaMandaar/ResearchBot.git](https://github.com/TeenaMandaar/TeenaMandaar.git)
cd nexus-ai-backend  ```


### 2. Set Up Environment Variables
Create a .env file in the root directory and add your API keys:

```GROQ_API_KEY="your_groq_key"
TAVILY_API_KEY="your_tavily_key" ```

### 3. Run Locally
Start the Backend Server:

```uvicorn app.main:app --reload
Start the Frontend UI: ```

```streamlit run frontend/ui.py ```

### 4. Run with Docker (Optional)
```docker build -t ResearchBot .
docker run -p 8000:8000 nexus-ai ```