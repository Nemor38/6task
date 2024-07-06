from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey, Enum, Numeric, String
from enum import Enum as BaseEnum

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    baskets = db.relationship('Basket', backref='user')

class BasketStatus(BaseEnum):
    Open = 'Open'
    Closed = 'Closed'
    Cancelled = 'Cancelled'

class Basket(db.Model):
    __tablename__ = 'baskets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    status = Column(Enum(BasketStatus), nullable=False, default=BasketStatus.Open)
