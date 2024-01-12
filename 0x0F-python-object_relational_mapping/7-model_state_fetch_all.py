#!/usr/bin/python3

"""
This script establishes a connection to a MySQL database and
queries the 'states' table to retrieve the id, name,
and capital of each state, ordered by id.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Establish a connection to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create the tables in the database based on the defined models
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Query the 'states' table and print the id, name,
    and capital of each state
    """
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, instance.capital, sep=": ")
