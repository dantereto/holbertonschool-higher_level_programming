#!/usr/bin/python3

from model_city import City
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                       pool_pre_ping=True)

if __name__ == '__main__':

    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(State, City)\
                              .filter(State.id == City.state_id)\
                              .order_by(City.id):
        print("{}: ({}) {}".format( city.name, city.id, state.name))
    session.close()
