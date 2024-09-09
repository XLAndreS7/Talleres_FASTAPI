from fastapi import APIRouter, Body 
from ..models.product  import Product

product_route = APIRouter()


@product_route.get("/")
async def get_product():
   try:
      return {"message": "Product Data"}
   except Exception as e:
      return {"error": str()}


@product_route.post("/")
def create_product(product: Product = Body (...)):
    try:
      return {"message": "Product Created"}
    except Exception as e:
       return {"error": str()}

    
@product_route.put("/{id}")
async def update_product(id: int, product: Product = Body(...)):
    try:
        return {"message": "Product Updated"}
    except Exception as e:
        return {"error": str(e)}
    
@product_route.delete("/{id}")
async def delete_product(id: int):
    try:
         return {"message": "Product Deleted"}
    except Exception as e:
        return {"error": str(e)}