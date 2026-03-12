import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import random

from faker import Faker

from app.database.db import SessionLocal
from app.models.user import User
from app.models.item import Item
from app.utils.auth import hash_password

fake = Faker()

db = SessionLocal()

categories = [
    "electronics",
    "fashion",
    "books",
    "home",
    "sports",
    "toys"
]

# ----------------------
# Create Users
# ----------------------

users = []

for _ in range(100):
    user = User(
        username=fake.user_name(),
        email=fake.email(),
        password=hash_password("password123")
    )

    db.add(user)
    users.append(user)

db.commit()

print("Users created")

# ----------------------
# Create Items
# ----------------------

for _ in range(2000):

    seller = random.choice(users)

    item = Item(
        title=fake.word().capitalize() + " " + fake.word(),
        price=random.randint(10, 1000),
        category=random.choice(categories),
        description=fake.sentence(),
        seller_id=seller.id
    )

    db.add(item)

db.commit()

print("Items created")

db.close()