from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schema.product import ProductCreateSchema
from typing import Optional

from routers.products import products
from routers.inventorysales import sales
from routers.auth import router as auth_router

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

# Include routers
app.include_router(auth_router)
app.include_router(products.router)
app.include_router(sales.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

