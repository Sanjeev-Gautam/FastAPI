from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="The ID of the item you would like to view")):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str = Query(None, title="Name", description="Enter the name of the item ")):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID already exists.")

@app.get("/get-item-Attribute/{item_id}/{name}")
def get_item(item_id: int, name: str):
    return inventory[item_id]

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error":"Item ID already exist."}

    inventory[item_id] = item
    return inventory[item_id]


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item ID does not already exists."}

    if item.name != None:
        inventory[item_id].name =  item.name

    if item.price != None:
        inventory[item_id].price =  item.price

    if item.brand != None:
        inventory[item_id].brand =  item.brand

    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The ID of the item to delete ")):
    if item_id not in inventory:
        return {"Error": "ID does not exist."}

    del inventory[item_id]
    return {"Success": "Item deleted!"}

@app.get("/")
def home():
    return {"Data" : "Testing"}

@app.get("/about")
def about():
    return {"Data" : "About"}