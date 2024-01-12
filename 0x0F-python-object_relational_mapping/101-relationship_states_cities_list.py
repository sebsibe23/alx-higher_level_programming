#!/usr/bin/python3
"""
Prints the State object with the specified name from the database.

Usage: python script_name.py username password database_name

This script connects to a MySQL database using the
provided credentials and queries the State
objects from the database. It then prints the ID and
name of each State object, along with the
associated City objects.

Arguments:
- username: The username for the MySQL database.
- password: The password for the MySQL database.
- database_name: The name of the MySQL database.

Dependencies:
- SQLAlchemy: The Python SQL toolkit and
Object-Relational Mapping (ORM) library.

Note: Before running the script, ensure that
the necessary SQLAlchemy models (State and City) and
their relationships are defined in the
'relationship_state.py' and 'relationship_city.py' files
respectively. Also, make sure that the MySQL database
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
        print(instance.id, instance.name, sep=": ")
        for city_ins in instance.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")
