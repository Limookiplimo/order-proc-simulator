from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = 'postgresql://user:password@localhost:3306/simulator'

engine = create_engine(db_url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def database_connection():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()