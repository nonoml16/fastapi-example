from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

lista = []


class Item(BaseModel):
    name: str
    description: str | None = None


@app.get("/items")
async def get_all(item: Item):
    return lista


@app.get("/items/{pos}")
async def get_posicion(pos: int):
    return lista.pop(pos)


@app.post("/items/")
async def create_item(item: Item) -> Item:
    lista.append(item)
    return item


@app.put("/items/{pos}")
async def edit_item(pos: int, item: Item) -> Item:
    lista.remove(pos)
    lista.insert(pos, item)
    return lista.pop(pos)


@app.delete("/items/{pos}")
async def edit_item(pos: int):
    lista.remove(pos)
    return "{message: borrado}"