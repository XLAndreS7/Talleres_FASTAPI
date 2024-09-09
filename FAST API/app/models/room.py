from pydantic import BaseModel

class Room (BaseModel):
     id: int
     availability: str 
     floor: str 
     roomPrice: str
     