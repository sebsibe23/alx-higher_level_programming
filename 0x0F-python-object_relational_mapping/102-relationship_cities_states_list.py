#!/usr/bin/python3
"""
Prints the State object with the
specified name from the database.

Usage: python script_name.py username
password database_name

This script connects to a MySQL database
using the provided credentials and queries the State
objects from the database. It then prints
the ID, name, and associated cities of each State object.

Arguments:
- username: The username for the MySQL database.
- password: The password for the MySQL database.
- database_name: The name of the MySQL database.

Dependencies:
- SQLAlchemy: Python SQL toolkit and
Object-Relational Mapping (ORM) library.

Note: Before running the script, make
sure the necessary SQLAlchemy models (State and City) and
their relationships are defined in the
'relationship_state.py' and 'relationship_city.py' files
respectively. Also, ensure that the MySQL database
is running and accessible.

"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        for city_ins in instance.cities:
            print(city_ins.id, city_ins.name, sep=": ", end="")
            print(" -> " + instance.name)
