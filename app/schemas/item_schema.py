from pydantic import BaseModel

class ItemCreate(BaseModel):
    title: str
    price: float
    category: str
    description: str
    seller_id: int


class ItemResponse(BaseModel):
    id: int
    title: str
    price: float
    category: str
    description: str
    seller_id: int

    class Config:
        from_attributes = True