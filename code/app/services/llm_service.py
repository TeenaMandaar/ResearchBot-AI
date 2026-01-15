from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langgraph.prebuilt import create_react_agent
from app.core.config import settings
from app.services.tools import tavily_tool

class LLMService:
    def __init__(self):
        # Initialize the Brain (Llama 3)
        self.llm = ChatGroq(
            temperature=0,
            model_name="llama-3.1-8b-instant",
            api_key=settings.GROQ_API_KEY
        )
        
        # Initialize the Tools (Search)
        self.tools = [tavily_tool]
        
        # Create the Agent that combines Brain + Tools
        self.agent_executor = create_react_agent(self.llm, self.tools)

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
        
        # Send everything to the Agent
        result = self.agent_executor.invoke({"messages": langchain_messages})
        
        # Get the list of all messages returned by the agent
        all_messages = result["messages"]
        
        # The last message in the list is the final answer
        final_answer = all_messages[-1].content
        
        return final_answer

# Create one instance to use in the app
llm_service = LLMService()