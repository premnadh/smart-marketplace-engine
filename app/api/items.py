from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.models.item import Item
from app.schemas.item_schema import ItemCreate, ItemResponse
from app.ai.recommender import recommend_items

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE ITEM
@router.post("/items/create", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):

    db_item = Item(**item.dict())

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


# SEARCH ITEMS (MUST COME BEFORE item_id)
@router.get("/items/search")
def search_items(q: str, category: str | None = None, db: Session = Depends(get_db)):

    query = db.query(Item)

    if q:
        query = query.filter(Item.title.ilike(f"%{q}%"))

    if category:
        query = query.filter(Item.category == category)

    return {"results": query.all()}


# GET ALL ITEMS
@router.get("/items", response_model=list[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    return db.query(Item).all()


# GET SINGLE ITEM
@router.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):

    item = db.query(Item).filter(Item.id == item_id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item


# DELETE ITEM
@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):

    item = db.query(Item).filter(Item.id == item_id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()

    return {"message": "Item deleted"}
@router.get("/recommendations/{item_id}", response_model=list[ItemResponse])
def get_recommendations(item_id: int, db: Session = Depends(get_db)):

    items = db.query(Item).all()

    recommendations = recommend_items(items, item_id)

    return recommendations