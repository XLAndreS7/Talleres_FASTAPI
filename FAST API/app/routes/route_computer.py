from fastapi import APIRouter, Body 
from ..models.computer  import Computer

computer_route = APIRouter()

@computer_route.get("/")
async def get_computer():
   try:
      return {"message": "Computer Data"}
   except Exception as e:
      return {"error": str()}


@computer_route.post("/")
def create_computer(computer: Computer = Body (...)):
    try:
      return {"message": "Computer Created"}
    except Exception as e:
       return {"error": str()}

    
@computer_route.put("/{id}")
async def update_computer(id: int, computer: Computer = Body(...)):
    try:
        return {"message": "Computer Updated"}
    except Exception as e:
        return {"error": str(e)}
    
@computer_route.delete("/{id}")
async def delete_computer(id: int):
    try:
         return {"message": "Computer Deleted"}
    except Exception as e:
        return {"error": str(e)}