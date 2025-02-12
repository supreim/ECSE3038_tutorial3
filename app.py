from datetime import datetime
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

fruits = []

class Fruit(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    variety: str
    quantity: int
    supplier: str
    harvest_date: datetime
    creation_date: datetime | None = datetime.now()
    availability: bool | None = True
    price: float
   
class Fruit_Update(BaseModel):
    availability: bool | None
    price: float | None
    quantity: int | None

app = FastAPI()


@app.get("/api/fruits",status_code=200)
async def get_fruits():
    return fruits

@app.get("/api/fruits/{id}",status_code=200)
async def get_fruit():
    for fruit in fruits:
        if fruit.id == id:
            return fruit
        else  :  
            raise HTTPException(status_code=404, detail="Fruit not found")

@app.post("/api/fruits",status_code=201)
async def add_fruit(fruit:Fruit):
    fruits.append(fruit)

@app.patch("/api/fruits/{id}",status_code=201)
async def update_fruit(f:Fruit_Update, id:UUID):
    for i, fruit in fruits:
        if fruit.id == id:
            fruits[i].availability = f.availability if f.availability else fruits[i].availability
            fruits[i].price = f.price if f.price else fruits[i].price
            fruits[i].quantity = f.quantity if f.quantity else fruits[i].quantity
            return    
    raise HTTPException(status_code=404, detail="Fruit not found")

@app.delete("/api/fruits/{id}",status_code=201)
async def delete_fruit(id:UUID):
    for i, fruit in fruits:
        if fruit.id == id:
            fruits[i].availability = False
            return
    raise HTTPException(status_code=404, detail="Fruit not found")