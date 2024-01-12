#!/usr/bin/python3

"""
This script connects to a MySQL database and
retrieves the State object with the name passed as an argument.
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

    # Retrieve the State object with the specified name
    instance = session.query(State).filter(State.name == (sys.argv[4],))

    try:
        # Print the ID of the State object
        print(instance[0].id)
    except IndexError:
        print("Not found")
