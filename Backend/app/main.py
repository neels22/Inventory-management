

# the entry point 

from fastapi import Fastapi
from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routers import inventory, sales
from constants.products import products
from constants.sales import sales as sales_data

app = FastAPI(title="Inventory Management API")


app.include_router(inventory.router)
