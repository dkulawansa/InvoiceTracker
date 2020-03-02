from datetime import datetime
from invoice import db, app

from sqlalchemy import (
	Column, 
	DateTime, 
	ForeignKey, 
	Integer, 
	Numeric, 
	String, 
	func, 
	Text
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import column_property, relationship

Base = declarative_base()

		
class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    cust_name = Column(String(50), unique=False)
    date_created = Column(DateTime, default=func.now())
	
    def __init__(self, cust_name=None, date_created=None):
        self.cust_name = cust_name
        self.date_created = date_created


class InvoiceItem(Base):
    __tablename__ = 'invoice_items'

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey('invoices.id'), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    description = Column(String(200), nullable=True)
    invoice = relationship('Invoice')
	
    def __init__(self, invoice_id, amount, description=None):
	    self.invoice_id = invoice_id
	    self.description = description
	    self.amount = amount
	
