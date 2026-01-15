from langchain_community.tools.tavily_search import TavilySearchResults
from app.core.config import settings

# Initialize the Search Tool
# We set max_results=3 so we don't get too much data to read
tavily_tool = TavilySearchResults(
    tavily_api_key=settings.TAVILY_API_KEY,
    max_results=3
)