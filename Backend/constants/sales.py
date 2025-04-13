

from schema.sale import SoldProduct, SaleBase
from datetime import datetime


sales = [
    SaleBase(
        id=1,
        date=datetime.now(),
        total_price=300.0,
        products=[
            SoldProduct(product_id=1, quantity=2),
            SoldProduct(product_id=5, quantity=1)
        ]
    ),
    SaleBase(
        id=2,
        date=datetime.now(),
        total_price=1100.0,
        products=[
            SoldProduct(product_id=10, quantity=1),
            SoldProduct(product_id=6, quantity=1)
        ]
    ),
    SaleBase(
        id=3,
        date=datetime.now(),
        total_price=1500.0,
        products=[
            SoldProduct(product_id=2, quantity=1),
            SoldProduct(product_id=3, quantity=1)
        ]
    ),
    SaleBase(
        id=4,
        date=datetime.now(),
        total_price=2000.0,
        products=[
            SoldProduct(product_id=4, quantity=1),
            SoldProduct(product_id=5, quantity=1)
        ]
    ),
    SaleBase(
        id=5,
        date=datetime.now(),
        total_price=2500.0,
        products=[
            SoldProduct(product_id=1, quantity=2),
            SoldProduct(product_id=3, quantity=1)
        ]
    )
]
