#!/usr/bin/python3
"""List all states with specified state name, SAFE"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    MY_HOST = 'localhost'
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    state_name = sys.argv[4]

    """Connect to DB"""
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)

    """creates cursor object"""
    cur = db.cursor()

    qry = "SELECT * \
            FROM states WHERE states.name = %s ORDER BY \
            states.id ASC;"

    cur.execute(qry, (state_name,))

    """Prints all rows returned by query"""
    rows = cur.fetchall()

    for state in rows:
        print(state)
