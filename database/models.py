from sqlalchemy import Column, String, BigInteger, TIMESTAMP, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Customers(Base):
    _tablename__ = 'customers'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    customer_code = Column(String(255), nullable=False)
    phone = Column(BigInteger, nullable=True, unique=True)
    credit_limit = Column(Float, nullable=False)
    credit_due = Column(Float, nullable=False)
    credit_balance = Column(Float, nullable=False)
    location = Column(String(255), nullable=False)
    route = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

    orders = relationship('Orders', back_populates='customers')

class Products(Base):
    _tablename__ = 'products'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    product_code = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    stock_count = Column(BigInteger, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

    orders = relationship('Orders', back_populates='products')

class Orders(Base):
    _tablename__ = 'orders'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    customer_code = Column(String(255), ForeignKey('customers.id'), nullable=False)
    product_code = Column(String(255), ForeignKey('products.id'), nullable=False)
    total_amount = Column(Float, nullable=False)
    total_weight = Column(Float, nullable=False)
    quantity = Column(BigInteger, nullable=False)
    order_status = Column(BigInteger, default=0, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

    products = relationship('Products', back_populates='orders')
    customers = relationship('Customers', back_populates='orders')
    invoices = relationship('Invoices', back_populates='orders')

class PendingOrders(Base):
    _tablename__ = 'pending_orders'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    customer_code = Column(String(255), ForeignKey('customers.id'), nullable=False)
    product_code = Column(String(255), ForeignKey('products.id'), nullable=False)
    total_amount = Column(Float, nullable=False)
    total_weight = Column(Float, nullable=False)
    quantity = Column(BigInteger, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

    products = relationship('Products', back_populates='orders')
    customers = relationship('Customers', back_populates='orders')

class Invoices(Base):
    _tablename__ = 'invoices'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    invoice_no = Column(String(255), nullable=False)
    order_id = Column(BigInteger, ForeignKey('orders.id'), nullable=False)
    invoice_amount = Column(Float, nullable=False)
    invoice_weight = Column(Float, nullable=False)
    invoice_discount = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

    orders = relationship('Orders', back_populates='invoices')

