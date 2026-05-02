from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "ResearchBot AI"
    APP_VERSION: str = "v1"
    
    # Optional so the app can start even without these set (will error only on chat requests)
    GROQ_API_KEY: Optional[str] = None
    TAVILY_API_KEY: Optional[str] = None
    
    class Config:
        env_file = ".env"

# Create one instance to use everywhere
settings = Settings()