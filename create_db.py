_author_ = "Valentin Scheele"
_project_ = "vscsqltests"
####################################################
#
# Creates a Training DB for starting with PyCharm, GIT and SQLITE and SQLCHARM.
# for learning how this stuff works.
#
# December 2016
###################################################


import sys #provides runtime env access



from sqlalchemy import ForeignKey,Column, Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base= declarative_base()

class Restaurant(Base):
    __tablename__='restaurant'
    name = Column(String(80),nullable= False)
    id = Column(Integer,primary_key=True)

class MenuItem(Base):
    __tablename__='menu_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    course =Column(String(250))
    description=Column(String(250))
    price=Column(String(8))
    restaurant_id=Column(Integer,ForeignKey('restaurant.id'))
    restaurant=relationship(Restaurant)


### at end of file  ########################################################
engine=create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
