#!/usr/bin/python3
"""
Lists cities from a specific state in the 'hbtn_0e_0_usa' database.

This script connects to a MySQL database and retrieves the names of cities
that belong to a specific stats.
The state name is provided as a command-line argument.
The city names are then printed, separated by commas.
"""

import MySQLdb
import sys


def fetch_city_names(username, password, db_name, state_name):
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )
    cur = db.cursor()
    query = """SELECT cities.name FROM cities
               INNER JOIN states ON states.id = cities.state_id
               WHERE states.name = %s"""
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))
    cur.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    fetch_city_names(username, password, db_name, state_name)
