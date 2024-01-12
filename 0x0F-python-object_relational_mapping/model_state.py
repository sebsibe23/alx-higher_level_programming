#!/usr/bin/python3

"""
This script contains the definition of the State class and
The Base instance, which is an instance of declarative_base().
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Represents a state with id, name, and capital attributes.
    """

    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    capital = Column(String(128), nullable=True)  # New variable

    def __init__(self, id, name, capital=None):
        self.id = id
        self.name = name
        self.capital = capital
