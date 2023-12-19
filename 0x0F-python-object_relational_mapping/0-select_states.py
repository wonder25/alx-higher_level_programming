#!/usr/bin/python3
"""List all states in db"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    MY_HOST = 'localhost'
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]

    """Connection to database"""
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
    """Create cursor object"""
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")

    """Get all rows returned by query"""
    rows = cur.fetchall()

    for state in rows:
        print(state)
