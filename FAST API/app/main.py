
from fastapi import FastAPI
from starlette. responses import RedirectResponse

# App routes
from .routes.route_user import user_route
from .routes.route_car import car_route
from .routes.route_computer import computer_route
from .routes.route_product import product_route
from .routes.route_room import room_route

from contextlib import asynccontextmanager 
from database import database as connection

@asynccontextmanager
async def lifespan(app: FastAPI) :
     # Conectar a la base de datos si la conexión está cerrada
  if connection.is_closed():
      connection.connect()
  try:
      yield
# Aquí es donde se ejecutará la aplicación
  finally:
# Cerrar la conexión cuando la aplicación se detenga if not connection, is_closed():
    if not connection.is_closed():
     connection,close()

# App instance
app = FastAPI()

@app .get ("/")
async def root():
  return RedirectResponse(url="/docs")

app.include_router(user_route, prefix="/users", tags=["users"])
app.include_router(user_route, prefix="/car", tags=["car"])
app.include_router(user_route, prefix="/computer", tags=["computer"])
app.include_router(user_route, prefix="/product", tags=["product"])
app.include_router(user_route, prefix="/room", tags=["room"])
# ruta para llamar def create_users(user: User = Body (...)):