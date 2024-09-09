from fastapi import APIRouter, Body 
from ..models.user  import User

user_route = APIRouter()

@user_route.get("/")
async def get_user():
   try:
      return {"message": "User Data"}
   except Exception as e:
      return {"error": str()}


@user_route.post("/")
async def create_users(user: User = Body (...)):
    try:
      return {"message": "User Created"}
    except Exception as e:
       return {"error": str()}
    
@user_route.put("/{id}")
async def update_user(id: int, user: User = Body(...)):
    try:
        return {"message": "User Updated"}
    except Exception as e:
        return {"error": str(e)}
    
@user_route.delete("/{id}")
async def delete_user(id: int):
    try:
         return {"message": "User Deleted"}
    except Exception as e:
        return {"error": str(e)}

