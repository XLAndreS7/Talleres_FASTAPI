from fastapi import APIRouter, Body 
from ..models.room  import Room

room_route = APIRouter()

@room_route.get("/")
async def get_room():
   try:
      return {"message": "Room Data"}
   except Exception as e:
      return {"error": str()}


@room_route.post("/")
def create_rooms(room: Room = Body (...)):
    try:
      return {"message": "Room Created"}
    except Exception as e:
       return {"error": str()}

    
@room_route.put("/{id}")
async def update_room(id: int, room: Room = Body(...)):
    try:
        return {"message": "Room Updated"}
    except Exception as e:
        return {"error": str(e)}
    
@room_route.delete("/{id}")
async def delete_room(id: int):
    try:
         return {"message": "Room Deleted"}
    except Exception as e:
        return {"error": str(e)}