from fastapi import FastAPI
from sqlmodel import SQLModel, Field
from typing import Optional
import datetime

app = FastAPI()

@app.get("/")
def home():
    return{"message" : "Start Messenger"}

class User(SQLModel, tabel=True):
    id:Optional[int] = Field(default=None, primary_kay=True)
    email: str = Field(index=True, unique=True)
    password_hash : str
    created_at : datetime.datetime = Field(
        default_factory = datetime.datetime.utcnow
    )
