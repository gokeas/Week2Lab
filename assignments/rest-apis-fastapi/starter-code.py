from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., example="Sample item")
    price: float = Field(..., gt=0, example=9.99)
    description: str | None = Field(None, example="Optional description")

# simple in-memory data store
data_store: dict[int, Item] = {}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = data_store.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items/")
def create_item(item: Item):
    item_id = len(data_store) + 1
    data_store[item_id] = item
    return {"item_id": item_id, **item.dict()}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in data_store:
        del data_store[item_id]
        return {"status": "deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

# run the server with: uvicorn starter-code:app --reload
