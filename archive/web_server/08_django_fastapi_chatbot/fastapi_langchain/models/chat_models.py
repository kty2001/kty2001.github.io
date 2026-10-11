from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ChatRequest(BaseModel):
    message: str = Field(..., description='User message', min_length=1, max_length=2000)
    session_id: Optional[str] = Field(default='default', description='Session id')

class ChatResponse(BaseModel):
    response: str = Field(..., description='Chatbot response message')
    session_id: str = Field(..., description='Session id')
    timestamp: datetime = Field(default_factory=datetime.now, description='Response cearted time')

class ErrorResponse(BaseModel):
    error: str = Field(..., description='Error message')
    detail: Optional[str] = Field(None, description='Detailed error info')

class HealthResponse(BaseModel):
    status: str = Field(..., description='Service health')
    timestamp: datetime = Field(default_factory=datetime.now, description='Response cearted time')

class HistoryItem(BaseModel):
    type: str = Field(..., description="Message type: 'human'|'user' or 'ai|'assistant'")
    content: str = Field(..., description='Message content')

class SetHistoryRequest(BaseModel):
    session_id: Optional[str] = Field(default='default', description="Session id")
    history: list[HistoryItem] = Field(default_factory=list, description='Session conversation list')
