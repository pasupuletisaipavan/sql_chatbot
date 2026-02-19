from fastapi import FastAPI
from src.api.v1.endpoints import foundation

app = FastAPI()

# Register the router
app.include_router(foundation.router)