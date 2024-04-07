from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles







app = FastAPI()

app.mount("/", StaticFiles(directory="../pages", html = True), name="static")








from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["items"]

# Pydantic model for item
class Item(BaseModel):
    name: str
    description: str

# CRUD operations
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    result = collection.insert_one(item_dict)
    item_dict["_id"] = str(result.inserted_id)
    return item_dict

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    item = collection.find_one({"_id": item_id})
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}")
async def update_item(item_id: str, item: Item):
    item_dict = item.dict()
    result = collection.replace_one({"_id": item_id}, item_dict)
    if result.modified_count == 1:
        return {"message": "Item updated successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    result = collection.delete_one({"_id": item_id})
    if result.deleted_count == 1:
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")







if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port = 8000)