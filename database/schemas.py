# PYDANTIC MODEL SCHEMAS
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from typing import List

class OrderBase(BaseModel):
    customer_id: int

    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    id: Optional[int]
    order_number: str
    customer_id: int
    total_amount: float
    total_weight: float
    order_status: int=0
    created_at: datetime
    updated_at: datetime


class OPCreate(BaseModel):
    product_id: int
    quantity: int

class OrderProductsCreate(BaseModel):
    order_number: str
    products: list[OPCreate]







