from fastapi import FastAPI
from backend.app.routes import user

app = FastAPI()
app.include_router(user.router)
