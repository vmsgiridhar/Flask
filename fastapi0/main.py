# loading pre-requisites

from typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel
from starlette.responses import StreamingResponse

# creating the app based on FastAPI
app = FastAPI()

# creating a Item 
class Item(BaseModel):
    name: str
    price: float 
    is_offer: Optional[bool] = None 

# default root
@app.get("/")
def read_root():
    return {"Hello":"World"}

# another example item route
# we are using async await here for example
# https://fastapi.tiangolo.com/async/#in-a-hurry
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item:Item):
    return {"item_id": item_id, "item_name": item.name, "item_price": item.price}