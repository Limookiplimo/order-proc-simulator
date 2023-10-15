# PYDANTIC MODEL SCHEMAS
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from typing import List

class OrderCreate(BaseModel):
    customer_id: int
    product_id: int
    quantity: int




