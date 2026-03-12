from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database.db import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Float)
    category = Column(String)
    description = Column(String)
    seller_id = Column(Integer, ForeignKey("users.id"))