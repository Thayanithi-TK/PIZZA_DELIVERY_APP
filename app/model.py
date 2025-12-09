from sqlalchemy import Column ,Integer ,String , Float , ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class user(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email=Column(String)
    password =Column(String)
    
    orders=relationship('Order',back_populates='user')


class Pizza(Base):
    __tablename__ ='pizzas'
    
    id = Column(Integer,primary_key=True,index=True)
    name=Column(String)
    prime=Column(Float)
    description=Column(String)


class Order(Base):
    __tablename__='Orders'

    id =Column(Integer,primary_key=True,index=True)

    user_id=Column(Integer,ForeignKey('users.id'))
    pizz_id=Column(Integer,ForeignKey('pizzas.id'))
    status = Column(String,default="pending")
    
    user=relationship('User',back_populates='orders')
    pizza=relationship('pizz')