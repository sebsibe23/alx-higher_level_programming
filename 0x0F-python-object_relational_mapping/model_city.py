#!/usr/bin/python3
"""
Contains the class definition of a City.

The City class represents a city entity
in the database.

Attributes:
    id (Column): The unique identifier of the city (Integer).
    name (Column): The name of the city
    (String, max length 128).
    state_id (Column): The foreign key referencing
    the associated state (Integer).

Table Name:
    cities

"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Class that defines each city.

    Args:
        Base (DeclarativeMeta): The base class
        for declarative class definitions.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        id (Column): The unique identifier of the city (Integer).
        name (Column): The name of the city (String, max length 128).
        state_id (Column): The foreign key referencing
        the associated state (Integer).

    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
