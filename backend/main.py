
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

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



class Product(BaseModel):
    name: str
    price: float
    description: str = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/product")
async def create_product(product: Product):
    # Here you would typically save the product to a database
    return {"message": "Product created", "product": product}
