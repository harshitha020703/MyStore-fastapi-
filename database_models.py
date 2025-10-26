
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)          # ✅ added length
    description = Column(String(500))               # ✅ added length
    price = Column(Float)
    quantity = Column(Integer)
