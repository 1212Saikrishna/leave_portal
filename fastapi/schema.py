from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    age: int
    designation:str
    description: str



