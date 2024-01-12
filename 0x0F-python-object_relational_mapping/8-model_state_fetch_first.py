#!/usr/bin/python3

"""
This script connects to a MySQL database and
retrieves the first State object from the 'hbtn_0e_6_usa' database.
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

    # Retrieve the first State object from the database
    instance = session.query(State).first()

    if instance is None:
        print("Nothing")
    else:
        print(instance.id, instance.name, sep=": ")
