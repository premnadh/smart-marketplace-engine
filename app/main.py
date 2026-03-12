from fastapi import FastAPI

from app.api import users, items, analytics
from app.database.db import engine, Base
from app.models.user import User
from app.models.item import Item


# Create database tables
Base.metadata.create_all(bind=engine)


# FastAPI application
app = FastAPI(title="Smart Marketplace Engine")


# Register API routers
app.include_router(users.router)
app.include_router(items.router)
app.include_router(analytics.router)


# Root endpoint
@app.get("/")
def home():
    return {"message": "Marketplace backend running"}