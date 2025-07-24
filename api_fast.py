from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel
from sqlalchemy import create_engine, func, desc
from sqlalchemy.orm import sessionmaker, joinedload

# SQLite for simplicity
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Schemas
class PostCreate(BaseModel):
    post_str_id: str
    content: str

class LikeAction(BaseModel):
    user_id_str: str
