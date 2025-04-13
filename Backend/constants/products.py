
from schema.product import ProductBase
products = [
    ProductBase(
        id=1,
        code="P001",
        name="Product 1",
        nickname="Prod1",
        quantity=10,
        threshold=5,
        description="Description of Product 1",
        price=100.0,
        category="Category A",
        brand="Brand X",
        location="Location A"
    ),
    ProductBase(
        id=2,
        code="P002",
        name="Product 2",
        nickname="Prod2",
        quantity=20,
        threshold=10,
        description="Description of Product 2",
        price=200.0,
        category="Category B",
        brand="Brand Y",
        location="Location B"
    ),
    ProductBase(
        id=3,
        code="P003",
        name="Product 3",
        nickname="Prod3",
        quantity=30,
        threshold=15,
        description="Description of Product 3",
        price=300.0,
        category="Category C",
        brand="Brand Z",
        location="Location C"
    ),
    ProductBase(
        id=4,
        code="P004",
        name="Product 4",
        nickname="Prod4",
        quantity=40,
        threshold=20,
        description="Description of Product 4",
        price=400.0,
        category="Category D",
        brand="Brand W",
        location="Location D"
    ),
    ProductBase(
        id=5,
        code="P005",
        name="Product 5",
        nickname="Prod5",
        quantity=50,
        threshold=25,
        description="Description of Product 5",
        price=500.0,
        category="Category E",
        brand="Brand V",
        location="Location E"
    ),
    # Add more ProductBase instances if needed
]


# Example of how to use the products list
# for product in products:
#     print(f"Product ID: {product.id}, Name: {product.name}, Price: {product.price}")
# This code defines a list of products using the ProductBase schema.
# Each product has attributes like id, code, name, nickname, quantity, threshold,
# description, price, category, brand, and location.