from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

lista = []


class Item(BaseModel):
    name: str
    description: str = None


@app.get("/items", response_model=list[Item])
async def get_all():
    return lista


@app.get("/items/{pos}", response_model=Item)
async def get_posicion(pos: int):
    if pos < 0 or pos >= len(lista):
        raise HTTPException(status_code=404, detail="Item not found")
    return lista[pos]


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    lista.append(item)
    return item


@app.put("/items/{pos}", response_model=Item)
async def edit_item(pos: int, item: Item):
    if pos < 0 or pos >= len(lista):
        raise HTTPException(status_code=404, detail="Item not found")
    lista[pos] = item
    return item


@app.delete("/items/{pos}")
async def delete_item(pos: int):
    if pos < 0 or pos >= len(lista):
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = lista.pop(pos)
    return {"message": "Item deleted", "item": deleted_item}
