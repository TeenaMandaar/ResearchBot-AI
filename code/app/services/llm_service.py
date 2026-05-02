from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langgraph.prebuilt import create_react_agent
from app.core.config import settings
from app.services.tools import get_tavily_tool

class LLMService:
    def __init__(self):
        # Don't initialize anything at startup — do it lazily on first use
        # This allows FastAPI to start and pass healthchecks even if keys are misconfigured
        self._agent_executor = None

    def _get_agent(self):
        # Initialize the agent only once, on first use
        if self._agent_executor is None:
            llm = ChatGroq(
                temperature=0,
                model_name="llama-3.1-8b-instant",
                api_key=settings.GROQ_API_KEY
            )
            tools = [get_tavily_tool()]
            self._agent_executor = create_react_agent(llm, tools)
        return self._agent_executor

    def generate_response(self, history: list):
        # We need to convert our Database messages into a format LangChain understands
        langchain_messages = []
        
        # Add the system instruction first
        system_instruction = SystemMessage(content="You are a helpful AI research assistant and a friendly companion. Be kind, supportive, and use the search tool to find current information when needed.")
        langchain_messages.append(system_instruction)
        
        # Loop through history and add user/ai messages
        for msg in history:
            if msg.role == "user":
                langchain_messages.append(HumanMessage(content=msg.content))
            elif msg.role == "assistant":
                langchain_messages.append(AIMessage(content=msg.content))
        
        # Get the agent (initializes on first call)
        agent_executor = self._get_agent()
        
        # Send everything to the Agent
        result = agent_executor.invoke({"messages": langchain_messages})
        
        # The last message in the list is the final answer
        final_answer = result["messages"][-1].content
        
        return final_answer

# Create one instance to use in the app (lightweight — no API calls at import time)
llm_service = LLMService()