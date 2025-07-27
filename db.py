from sqlite3 import DatabaseError
from sqlmodel import create_engine, Session, SQLModel

DATABASE_URL = "sqlite:/// ./messenger.db"

engine = create_engine(DATABASE_URL, echo=False)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)
