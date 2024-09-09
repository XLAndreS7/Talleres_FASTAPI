from pydantic import BaseModel

class Computer (BaseModel):
     id: int
     brand: str 
     processor: str 
     operatingSystem : str
     memory : str