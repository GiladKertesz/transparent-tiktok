from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    display_name: Optional[str]
    email_hash: str

class User(BaseModel):
    user_id: UUID
    username: str
    display_name: Optional[str]
    email_hash: str
    created_at: datetime
    last_active_at: Optional[datetime]

    class Config:
        orm_mode = True
