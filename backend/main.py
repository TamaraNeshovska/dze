from fastapi import FastAPI
from src.routers.healthcheck import router as health_router

app = FastAPI()

# include endpoints
app.include_router(health_router)