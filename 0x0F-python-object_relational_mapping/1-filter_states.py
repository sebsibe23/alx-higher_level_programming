#!/usr/bin/python3
"""Lists states starting with 'N' from the 'hbtn_0e_0_usa' database.

This script connects to a MySQL database and
retrieves all the states from the 'states' table
that start with the letter 'N'. The states are then printed one by one.
"""

import MySQLdb
import sys


def fetch_states_starting_with_N(host, user, passwd, db, port):
    """Fetches states from the database starting with 'N'."""
    db = MySQLdb.connect(
        host=host,
        user=user,
        passwd=passwd,
        db=db,
        port=port
    )
    cur = db.cursor()
    cur.execute(
        """
        SELECT * FROM states WHERE name LIKE
        BINARY 'N%' ORDER BY states.id
        """
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

    fetch_states_starting_with_N(host, user, passwd, db, port)
