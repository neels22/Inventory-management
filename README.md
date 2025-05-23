# Inventory Management System Backend

A FastAPI-based backend for an inventory management system with PostgreSQL database.

## Features

- Product management (CRUD operations)
- Sales management with automatic inventory updates
- Inventory tracking and low stock alerts
- Sales analytics and reporting
- RESTful API with OpenAPI documentation

## Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd inventory-management
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a PostgreSQL database:
```sql
CREATE DATABASE inventory_db;
```

5. Create a `.env` file in the root directory with the following content:
```
DATABASE_URL=postgresql+psycopg2://user:password@localhost/inventory_db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Replace `user` and `password` with your PostgreSQL credentials.

## Running the Application

1. Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

2. Access the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Products
- GET /api/v1/products/ - List all products
- POST /api/v1/products/ - Create a new product
- GET /api/v1/products/{product_id} - Get product details
- PUT /api/v1/products/{product_id} - Update a product
- DELETE /api/v1/products/{product_id} - Delete a product
- GET /api/v1/products/low-stock/ - Get low stock products

### Sales
- GET /api/v1/sales/ - List all sales
- POST /api/v1/sales/ - Create a new sale
- GET /api/v1/sales/{sale_id} - Get sale details
- PUT /api/v1/sales/{sale_id} - Update a sale
- DELETE /api/v1/sales/{sale_id} - Delete a sale

### Inventory
- GET /api/v1/inventory/summary - Get inventory summary

## Development

The project follows a modular structure:
```
inventory_backend/
├── app/
│   ├── api/          # API endpoints
│   ├── core/         # Core functionality
│   ├── crud/         # Database operations
│   ├── models/       # Database models
│   └── schemas/      # Pydantic models
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.



api list
- products
    - get all the products 
    - get only a product by its id 
    - get only a product by its name     
    - get only a product by its nickname     
    - get only a product by its code     
    - get only a product by its category   
        - check if only one api is required for above 
    - post a new product 
    - delete a product

    - update product details


- sale
    - put/add product to sale
    - delete product from the sale
    - create/post new sale
    - get the sale by its date or name
    
