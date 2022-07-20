from sqlalchemy import Column, DateTime, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from models.product import Products

# инициализация декларативного стиля
Base = declarative_base()


class Order(Base):

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    quantiti = Column(Integer)
    data = Column(DateTime)
    product_id = Column(Integer, ForeignKey('products.id'))
    user_id = Column(Integer)

    # каскадное удаление
    # удаляются все продукты из 'orders' при удалении данного продукта из таблицы 'products'
    products = relationship(
        Products,
        backref=backref('orders',
                        uselist=True,
                        cascade='delete, all'))

    def __str__(self):
        return f"{self.quantiti} {self.data}"
    