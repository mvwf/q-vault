# backend/app/api/routes/user.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.db.db_client import inject_db
from backend.models.user import User

router = APIRouter()

@router.get("/hello/{name}", tags=["greetings"])
def say_hello(name: str, db: Session = Depends(inject_db)) -> dict[str, str]:
    user = db.query(User).filter(User.name == name).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"Hello {user.name}, user exists! They have email {user.email}."}
