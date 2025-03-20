from fastapi import FastAPI
from .database import engine, Base
from .routes import user_routes

app = FastAPI(title="User CRUD API", version="1.0")

Base.metadata.create_all(bind=engine)

app.include_router(user_routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI User CRUD"}
