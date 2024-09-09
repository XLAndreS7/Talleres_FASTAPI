from fastapi import APIRouter, Body 
from ..models.car  import Car

car_route = APIRouter()


@car_route.get("/")
async def get_car():
   try:
      return {"message": "Car Data"}
   except Exception as e:
      return {"error": str()}


@car_route.post("/")
def create_car(car: Car = Body (...)):
    try:
      return {"message": "Car Created"}
    except Exception as e:
       return {"error": str()}

    
@car_route.put("/{id}")
async def update_car(id: int, car: Car = Body(...)):
    try:
        return {"message": "Car Updated"}
    except Exception as e:
        return {"error": str(e)}
    
@car_route.delete("/{id}")
async def delete_car(id: int):
    try:
         return {"message": "Car Deleted"}
    except Exception as e:
        return {"error": str(e)}