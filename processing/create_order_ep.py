import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from database.db_con import database_connection
from database import models, schemas
from create_order_crud import create_order, create_order_product
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()


@app.post("/api/create-order", response_model=schemas.OrderCreate)
def handle_create_order(order: schemas.OrderBase, db: Session = Depends(database_connection)):
    avail_cust = db.query(models.Customers).filter(models.Customers.id == order.customer_id).first()
    if avail_cust is None:
        raise HTTPException(status_code=400, detail="Customer does not exist")
    return create_order(db=db, order=order)


@app.post("/api/create-order-product", response_model=dict)
def handle_create_order_product(order_prod: schemas.OrderProductsCreate, db: Session = Depends(database_connection)):
    order_prod.order_number = order_prod.order_number.upper()
    for prod_data in order_prod.products:
        product_id = prod_data.product_id
    avail_prod = db.query(models.Products).filter(models.Products.id == product_id).first()
    if avail_prod is None:
        raise HTTPException(status_code=400, detail="Product does not exist")
    create_order_product(db=db, order_prod=order_prod)
    return {"message":"success","detail": "Order product(s) created successfully"}



