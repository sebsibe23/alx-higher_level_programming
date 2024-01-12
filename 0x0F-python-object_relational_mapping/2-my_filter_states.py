#!/usr/bin/python3
"""Lists specific states from the 'hbtn_0e_0_usa' database.

This script connects to a MySQL database and
retrieves states from the 'states' table
that match the provided name. The states are then printed one by one.
"""

import MySQLdb
import sys


def fetch_specific_states(host, user, passwd, db, port, state_name):
    """Fetches specific states from the database."""
    db = MySQLdb.connect(
        host=host,
        user=user,
        passwd=passwd,
        db=db,
        port=port
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}'"
        .format(state_name)
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    host = "localhost"
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    port = 3306
    state_name = sys.argv[4]

    fetch_specific_states(host, user, passwd, db, port, state_name)
