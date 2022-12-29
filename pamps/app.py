from fastapi import FastAPI
from .routes import main_router


app = FastAPI(
    title="PAMPS",
    version="0.1.0",
    description="PAMPS is a Python API simple blog system",
)
app.include_router(main_router)
