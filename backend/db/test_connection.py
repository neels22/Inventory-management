from dbconnection import engine, Base, SessionLocal
from sqlalchemy import text
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def test_connection():
    try:
        # Verify environment variable is set
        if not os.getenv("DATABASE_URL"):
            raise ValueError("DATABASE_URL environment variable is not set")
            
        # Test 1: Basic connection test
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("✅ Database connection successful!")
            
        # Test 2: Create a test table and perform operations
        with SessionLocal() as session:
            # Create a test table
            session.execute(text("""
                CREATE TABLE IF NOT EXISTS test_table (
                    id SERIAL PRIMARY KEY,
                    test_column VARCHAR(50)
                )
            """))
            session.commit()
            print("✅ Test table created successfully!")
            
            # Insert test data
            session.execute(text("""
                INSERT INTO test_table (test_column) 
                VALUES ('test_data')
            """))
            session.commit()
            print("✅ Test data inserted successfully!")
            
            # Query test data
            result = session.execute(text("SELECT * FROM test_table"))
            rows = result.fetchall()
            print("✅ Test data retrieved successfully!")
            print("Retrieved data:", rows)
            
            # Clean up
            session.execute(text("DROP TABLE test_table"))
            session.commit()
            print("✅ Test table cleaned up successfully!")
            
    except Exception as e:
        print("❌ Error occurred:", str(e))
        raise e

if __name__ == "__main__":
    print("Testing database connection...")
    test_connection()
    print("All tests completed!") 