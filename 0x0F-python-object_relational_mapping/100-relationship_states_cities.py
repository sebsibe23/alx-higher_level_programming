#!/usr/bin/python3

"""
This script creates the State "California" with
the City "San Francisco" in a MySQL database.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # Establish a connection to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create the tables in the database based on the defined models
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the State "California"
    california = State(name='California')

    """
    Create the City "San Francisco" and associate
    it with the State "California"
    """
    san_francisco = City(name='San Francisco')
    california.cities.append(san_francisco)

    """
    Add the State and City objects to the session
    and commit the changes to the database
    """
    session.add(california)
    session.add(san_francisco)
    session.commit()
