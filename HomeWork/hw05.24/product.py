from sqlalchemy import  ForeignKey,Column, Integer, String
from db import Base


class Product(Base):
    __tablename__ = 'Products'

    id = Column(Integer, primary_key=True)
    code = Column(Integer, nullable=False)
    name = Column(String(250),ForeignKey('Buyers.name') )
    price = Column(String(250), nullable=False)


    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

    def __repr__(self):
        return f'Код: {self.code}, Название: {self.name}, Цена: {self.price}'
