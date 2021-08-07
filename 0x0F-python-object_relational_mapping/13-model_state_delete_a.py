#!/usr/bin/python3
"""start the function"""

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
    for state in session.query(State).filter(State.name.like("%a%")):
        session.delete(state)
    session.commit()
    session.close()
