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

    # Create a new State object with the specified name
    new_state = State(name='Louisiana')

    # Add the new State object to the session
    session.add(new_state)

    # Retrieve the new State object from the session
    new_instance = session.query(State).filter_by(name='Louisiana').first()

    # Print the ID of the new State object
    print(new_instance.id)

    # Commit the changes to the database
    session.commit()
