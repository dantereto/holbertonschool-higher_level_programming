#!/usr/bin/python3
"""start the function"""

from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    sesion = session.query(City).order_by(City.id).all()
    for city in sesion:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
