#!/usr/bin/python3
"""start the function"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys
if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    first = session.query(State).first()
    if first is None:
        print("Nothing")
    else:
        print("{}: {}".format(first.id, first.name))
    session.close()
