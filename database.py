from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "mysql+pymysql://root:12345678@localhost:3306/apidatabase"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
