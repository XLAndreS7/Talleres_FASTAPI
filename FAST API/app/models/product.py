from pydantic import BaseModel

class Product (BaseModel):
     id: int
     name: str 
     amount: str 
     price : str
     