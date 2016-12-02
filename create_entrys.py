print "test"

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import Base,Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession=sessionmaker(bind=engine)
session = DBSession()

#Lets Create!

myfirstRestaurant = Restaurant(name="Valentins CAFE")
session.add(myfirstRestaurant)
session.commit()

cheesepizza=MenuItem(name="PIZZA Extreme", description="Diese Pizza haut dich um", course="Entree", price="22 EUR", restaurant= myfirstRestaurant)
session.add(cheesepizza)
session.commit()
allItems= session.query(MenuItem).all()
print "hey"