#!/usr/bin/python3
"""
Lists all cities with their corresponding state
names from the 'hbtn_0e_0_usa' database.

This script connects to a MySQL database and
retrieves the city ID, city name, and state name
by joining the 'cities' and 'states' tables.
The results are then printed one by one.
"""

import MySQLdb
import sys


def fetch_data(username, password, db_name):
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )
    cur = db.cursor()
    query = """SELECT cities.id, cities.name, states.name
               FROM cities
               INNER JOIN states ON states.id = cities.state_id"""
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    fetch_data(username, password, db_name)
