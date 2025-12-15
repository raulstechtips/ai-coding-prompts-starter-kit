from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI()

users_db = {}
items_db = []
orders_db = []

class UserCreate(BaseModel):
    name: str
    email: str
    age: int

class Item(BaseModel):
    name: str
    price: float
    category: str

class Order(BaseModel):
    user_id: int
    items: List[str]
    total: float

@app.get("/")
def root():
    return {"message": "API is running", "timestamp": datetime.now().isoformat()}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@app.post("/users")
def create_user(user: UserCreate):
    user_id = len(users_db) + 1
    user_data = {
        "id": user_id,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "created_at": datetime.now().isoformat()
    }
    users_db[user_id] = user_data
    return user_data

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id].update({
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "updated_at": datetime.now().isoformat()
    })
    return users_db[user_id]

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user = users_db.pop(user_id)
    return {"message": "User deleted", "user": deleted_user}

@app.get("/items")
def list_items(category: Optional[str] = Query(None), min_price: Optional[float] = Query(None)):
    filtered_items = items_db
    if category:
        filtered_items = [item for item in filtered_items if item["category"] == category]
    if min_price:
        filtered_items = [item for item in filtered_items if item["price"] >= min_price]
    return {"count": len(filtered_items), "items": filtered_items}

@app.post("/items")
def add_item(item: Item):
    item_data = {
        "id": len(items_db) + 1,
        "name": item.name,
        "price": item.price,
        "category": item.category
    }
    items_db.append(item_data)
    return item_data

@app.post("/orders")
def create_order(order: Order):
    if order.user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    order_data = {
        "id": len(orders_db) + 1,
        "user_id": order.user_id,
        "items": order.items,
        "total": order.total,
        "status": "pending",
        "created_at": datetime.now().isoformat()
    }
    orders_db.append(order_data)
    return order_data

@app.get("/stats")
def get_stats():
    return {
        "total_users": len(users_db),
        "total_items": len(items_db),
        "total_orders": len(orders_db),
        "revenue": sum(order["total"] for order in orders_db)
    }
