from pydantic import BaseModel

class Car (BaseModel):
     id: int
     color: str 
     typeCar: str 
     