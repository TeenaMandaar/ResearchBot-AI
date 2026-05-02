from langchain_community.tools.tavily_search import TavilySearchResults
from app.core.config import settings

def get_tavily_tool():
    # Create the search tool on demand (not at import time)
    # This prevents startup crashes if the API key isn't set yet
    return TavilySearchResults(
        tavily_api_key=settings.TAVILY_API_KEY,
        max_results=3
    )