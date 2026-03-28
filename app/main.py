from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth_routes, todo_routes

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# routes
app.include_router(auth_routes.router)
app.include_router(todo_routes.router)