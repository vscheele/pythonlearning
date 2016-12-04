_author_ = "Valentin Scheele"
_project_ = "vscsqltests"
####################################################
#
# Creates the puppy database from Udacity
# Full Stack Foundations Exercise 1
#
# December 2016
#
#
###################################################


import sys #provides runtime env access


from sqlalchemy import ForeignKey,Column, Integer,String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base= declarative_base()

class Shelter(Base):
    __tablename__='shelter'
    name    = Column(String(80),nullable= False)
    adress  = Column(String(200),nullable= True)
    city    = Column(String(80),nullable= True)
    state   = Column(String(20),nullable= True)
    zipCode = Column(String(8), nullable= True)
    website = Column(String(800), nullable= True)
    id = Column(Integer,primary_key=True)

class Puppy(Base):
    __tablename__='puppy'
    name = Column(String(80), nullable=False)
    dateOfBirth = Column(Date, nullable=True)
    gender = Column(String(80), nullable=False)
    weight = Column(Float, nullable=False)
    id = Column(Integer, primary_key=True)
    shelter_id=Column(Integer,ForeignKey('shelter.id'))
    shelter=relationship(Shelter)

### at end of file  ########################################################
engine=create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)
