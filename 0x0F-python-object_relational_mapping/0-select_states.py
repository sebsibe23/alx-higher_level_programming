#!/usr/bin/python3
"""Lists all states from the 'hbtn_0e_0_usa' database.

This script connects to a MySQL database and
retrieves all the states from the 'states' table.
The states are then printed one by one.
"""

import MySQLdb
import sys


def fetch_states(host, user, passwd, db, port):
    """Fetches states from the database."""
    db = MySQLdb.connect(
        host=host,
        user=user,
        passwd=passwd,
        db=db,
        port=port
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
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

    fetch_states(host, user, passwd, db, port)
