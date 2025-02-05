from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String
from sqlalchemy.orm import sessionmaker

# Initialize FastAPI app
app = FastAPI()

# Initialize transformer-based chatbot (using GPT-2 for simplicity)
chatbot = pipeline("text-generation", model="gpt2")

# SQLite Database setup
DATABASE_URL = "sqlite:///./test.db"  # SQLite file in the current directory
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables if they don't exist
metadata = MetaData()
products = Table('products', metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String, index=True),
    Column('brand', String, index=True),
    Column('price', Integer),
)
metadata.create_all(bind=engine)

# Define Pydantic models
class ChatRequest(BaseModel):
    message: str

class Product(BaseModel):
    name: str
    brand: str
    price: int

# Chatbot endpoint
@app.post("/chat")
async def chat(request: ChatRequest):
    input_message = request.message
    response = chatbot(input_message, max_length=50, num_return_sequences=1)[0]['generated_text']
    return {"response": response}

# Endpoint to add a product to the database
@app.post("/products/")
async def create_product(product: Product):
    db = SessionLocal()
    try:
        new_product = products.insert().values(
            name=product.name, brand=product.brand, price=product.price
        )
        db.execute(new_product)
        db.commit()
        return {"message": "Product added successfully"}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()

# Endpoint to fetch all products
@app.get("/products/")
async def get_products():
    db = SessionLocal()
    try:
        query = products.select()
        result = db.execute(query).fetchall()
        return {"products": result}
    finally:
        db.close()
