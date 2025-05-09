
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schema.product import Product
from typing import Optional

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

productarr = [
    {"id":1,"name": "Product 1", "price": 10.0, "description": "Description 1"},
    {"id":2,"name": "Product 2", "price": 20.0, "description": "Description 2"},
    {"id":3,"name": "Product 3", "price": 30.0, "description": "Description 3"},
    {"id":4,"name": "Product 4", "price": 40.0, "description": "Description 4"},
    {"id":5,"name": "Product 5", "price": 50.0, "description": "Description 5"},
]   


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/product")
async def create_product(product: Product):
    # Here you would typically save the product to a database
    return {"message": "Product created", "product": product}


@app.get("/products/")
async def get_all_products():
    return {"message": "All products retrieved", "products": productarr}

@app.get("/product/{product_id}")
async def get_product(product_id: int):
    for product in productarr:
        if product["id"] == product_id:
            return {"message": "Product retrieved", "product": product}
    return {"message": "Product not found"}