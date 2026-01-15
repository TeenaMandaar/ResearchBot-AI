from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

# Table to store different conversations (Folders)
class ChatSession(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    name: str = Field(default="New Chat")

# Table to store individual messages inside a conversation (Files)
class ChatMessage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # This links the message to a specific session
    session_id: int = Field(foreign_key="chatsession.id")
    
    role: str   # "user" or "assistant"
    content: str 
    created_at: datetime = Field(default_factory=datetime.utcnow)