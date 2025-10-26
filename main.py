from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import database_models
from database import SessionLocal, engine
from models import Product

database_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS for React dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# list of products with 4 products like phones, laptops, pens, tables
products = [
    Product(id=1, name="Smartwatch", description="Tracks heart rate, steps, and sleep with smartphone sync", price=159.99, quantity=40),
    Product(id=2, name="Bluetooth Speaker", description="Portable speaker with rich bass and waterproof design", price=89.99, quantity=35),
    Product(id=3, name="Coffee Maker", description="Automatic espresso machine with milk frother", price=249.99, quantity=20),
    Product(id=4, name="Air Purifier", description="HEPA filter air purifier for large rooms", price=179.99, quantity=25),
    Product(id=5, name="Yoga Mat", description="Eco-friendly non-slip yoga mat for fitness workouts", price=29.99, quantity=60),
    Product(id=6, name="Wireless Charger", description="Fast Qi charging pad for phones and earbuds", price=39.99, quantity=50),
    Product(id=7, name="Desk Lamp", description="LED desk lamp with adjustable brightness and USB port", price=54.99, quantity=30),
    Product(id=8, name="Electric Kettle", description="Stainless steel kettle with 1.7L capacity and auto shut-off", price=49.99, quantity=40),
    Product(id=9, name="Smart Thermostat", description="Wi-Fi enabled thermostat with voice control and scheduling", price=129.99, quantity=15),
    Product(id=10, name="Fitness Tracker", description="Monitors steps, sleep, and calories burned throughout the day", price=69.99, quantity=55),
        
]


def init_db():
    db = SessionLocal()

    existing_count = db.query(database_models.Product).count()

    if existing_count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()
        print("Database initialized with sample products.")
        
    db.close()

init_db()    

@app.get("/products/")
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(database_models.Product).all()
    return products


@app.get("/products/{product_id}")
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    if product:
        return product
    return {"error": "Product not found"}

@app.post("/products/")
def create_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return {"message": "Product created successfully", "product": product}

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity
    db.commit()
    db.refresh(db_product)
    return {"message": "Product updated successfully", "product": db_product}


@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}
