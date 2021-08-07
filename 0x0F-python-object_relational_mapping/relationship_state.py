#!/usr/bin/python3
"""start the function"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """start"""
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
