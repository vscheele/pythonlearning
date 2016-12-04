
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import Base,Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession=sessionmaker(bind=engine)
session = DBSession()
