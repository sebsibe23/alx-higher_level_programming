#!/usr/bin/python3

"""
This script connects to a MySQL database and updates
the name of a State object with the specified ID.
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

    # Retrieve the State object with the specified ID
    new_instance = session.query(State).filter_by(id=2).first()

    # Update the name of the State object
    new_instance.name = 'New Mexico'

    # Commit the changes to the database
    session.commit()
