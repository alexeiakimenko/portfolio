from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base


class Buyer(Base):
    __tablename__ = 'Buyers'

    id = Column(Integer, primary_key=True)
    buyers = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    quantity = Column(Integer, nullable=False)
    products = relationship('Product')

    def __init__(self, buyers, name, quantity):
        self.buyers = buyers
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f'Покупатель: {self.buyers}, купил: {self.name}, в количестве: {self.quantity}'
