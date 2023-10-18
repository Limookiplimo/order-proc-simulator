import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from sqlalchemy import update
from database import schemas
from sqlalchemy.exc import IntegrityError
from database import models
from sqlalchemy.orm import Session, joinedload


def create_order(db: Session, order: schemas.OrderBase):
    try:      
        # Fetch customer data
        order_count = db.query(models.Orders).count()
        series_no = order_count + 1
        order_number = f"ORD{series_no:003d}"

        #defaults
        total_amount = 0.0
        total_weight = 0.0

        db_order = models.Orders(**order.model_dump(),order_number=order_number,
                                 total_amount=total_amount, total_weight=total_weight)
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order
    except IntegrityError as integrity_error:
        db.rollback()
        raise integrity_error
    except Exception as e:
        db.rollback()
        raise e

def create_order_product(db: Session, order_prod: schemas.OrderProductsCreate):
    try:
        order_num = order_prod.order_number
        order = db.query(models.Orders).filter(models.Orders.order_number == order_num).first()

        if order is None:
            raise ValueError("Order not found")
        
        for prod in order_prod.products:
            product_id = prod.product_id
            quantity = prod.quantity

            prods = db.query(models.Products).filter(models.Products.id==product_id).first()
            if prods is None:
                raise ValueError("Product not found")
            price = prods.price
            weight = prods.weight
            
            prod_count = db.query(models.OrderProducts).filter(models.OrderProducts.order_number==order_num).count()
            line_number = prod_count + 1
            t_amount = quantity * price
            t_weight = quantity * weight

            db_order_product = models.OrderProducts(
                        order_number=order_num,
                        line_number=line_number,
                        product_id=product_id,
                        total_amount=t_amount,
                        total_weight=t_weight,
                        quantity=quantity
                        )
            db.add(db_order_product)
            db.commit()
            db.refresh(db_order_product)

                # Update orders table
            order.total_amount += t_amount
            order.total_weight += t_weight

        db.commit()
        return db_order_product
    except IntegrityError as integrity_error:
        db.rollback()
        raise integrity_error
    except Exception as e:
        db.rollback()
        raise e