from fastapi import FastAPI
from .database import Base, engine
from .routers import users

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title='Transparent TikTok API')
app.include_router(users.router)
