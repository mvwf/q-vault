# backend/db/deps.py
from backend.db.session import SessionLocal
from sqlalchemy.orm import Session
from typing import Generator

def inject_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
