from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from .database import Base
import uuid

class User(Base):
    __tablename__ = 'users'
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), unique=True, nullable=False)
    display_name = Column(String(100))
    email_hash = Column(String(64), nullable=False)
    created_at = Column(DateTime, server_default='now()')
    last_active_at = Column(DateTime)
