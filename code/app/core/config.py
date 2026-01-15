from pydantic_settings import BaseSettings
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "ResearchBot AI"
    APP_VERSION: str = "v1"
    
    GROQ_API_KEY: str
    TAVILY_API_KEY:str
    
    class Config:
        env_file = ".env"

# Create one instance to use everywhere
settings = Settings()