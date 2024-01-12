#!/usr/bin/python3

"""
Contains the State class and Base,
an instance of declarative_base().
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Class that represents a state entity in the database.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        id (Column): The unique identifier of the state (Integer).
        name (Column): The name of the state (String, max length 128).
        cities (relationship): The relationship to
        the associated City objects.

    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
