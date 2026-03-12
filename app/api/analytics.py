from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.db import SessionLocal
from app.models.item import Item

router = APIRouter(prefix="/analytics")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ------------------------
# Popular items
# ------------------------

@router.get("/popular-items")
def popular_items(db: Session = Depends(get_db)):

    items = db.query(Item).order_by(Item.price.desc()).limit(10).all()

    return {"popular_items": items}


# ------------------------
# Top categories
# ------------------------

@router.get("/top-categories")
def top_categories(db: Session = Depends(get_db)):

    categories = (
        db.query(Item.category, func.count(Item.id))
        .group_by(Item.category)
        .all()
    )

    return {"categories": categories}


# ------------------------
# Price distribution
# ------------------------

@router.get("/price-distribution")
def price_distribution(db: Session = Depends(get_db)):

    prices = db.query(Item.price).all()

    return {"prices": [p[0] for p in prices]}