from fastapi import FastAPI, HTTPException, Depends

from db import *
from models import *
from models.item import Item

app = FastAPI()

lista = []


@app.on_event('startup')
def create_db():
    Base.metadata.create_all(bind=engine)


@app.get("/items", response_model=list[Item])
async def get_all():
    return lista


@app.get("/items/{pos}", response_model=Item)
async def get_posicion(pos: int):
    if pos < 0 or pos >= len(lista):
        raise HTTPException(status_code=404, detail="Item not found")
    return lista[pos]


@app.post("/items/", response_model=Item)
async def create_item(item: Item, session: Session = Depends(get_session())):
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
