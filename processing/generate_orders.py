from database.db_con import database_connection
from database.schemas import OrderCreate


from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import datetime

app = FastAPI()

def create_order(db: Session, order: OrderCreate):
    # Fetch customer data
    customer_data = None

    #Fetch product data
    pass