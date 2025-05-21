
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schema.product import Product
from typing import Optional

from routers.products import products
# Allow CORS for all origins
origins = [
    "http://localhost:3000",
    "https://your-frontend-domain.com",
]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

