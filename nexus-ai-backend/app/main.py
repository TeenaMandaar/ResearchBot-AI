from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from sqlmodel import Session, select
from contextlib import asynccontextmanager

# Import our own modules
from app.core.database import create_db_and_tables, get_session
from app.models import ChatSession, ChatMessage
from app.services.llm_service import llm_service

# This runs once when the server starts to create the database file
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

# Define what data we expect from the user
class ChatRequest(BaseModel):
    query: str
    session_id: Optional[int] = None

@app.get("/")
def health_check():
    return {"status": "running"}

@app.post("/chat")
def chat_endpoint(request: ChatRequest, db: Session = Depends(get_session)):
    
    # Step 1: Handle the Session ID
    # If the user didn't send an ID, we need to create a new chat session.
    session_id = request.session_id
    
    if session_id is None:
        # Create a new session in the database
        new_session = ChatSession(name=request.query[:30]) # Use first 30 chars of query as name
        db.add(new_session)
        db.commit()
        db.refresh(new_session)
        session_id = new_session.id
    else:
        # Check if the session actually exists
        existing_session = db.get(ChatSession, session_id)
        if existing_session is None:
            raise HTTPException(status_code=404, detail="Invalid Session ID")

    # Step 2: Save the User's message to the database
    user_message = ChatMessage(
        session_id=session_id,
        role="user",
        content=request.query
    )
    db.add(user_message)
    db.commit()

    # Step 3: Get previous messages for context
    # We need the history so the AI knows what we are talking about
    statement = select(ChatMessage).where(ChatMessage.session_id == session_id)
    history = db.exec(statement).all()
    
    # Step 4: Get answer from AI Service
    ai_text = llm_service.generate_response(history)

    # Step 5: Save the AI's message to the database
    ai_message = ChatMessage(
        session_id=session_id,
        role="assistant",
        content=ai_text
    )
    db.add(ai_message)
    db.commit()

    # Step 6: Return the answer to the frontend
    return {
        "response": ai_text, 
        "session_id": session_id
    }