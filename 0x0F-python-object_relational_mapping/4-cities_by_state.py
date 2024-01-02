#!/usr/bin/python3
"""Lists all cities in database"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    MY_HOST = 'localhost'
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]

    """ Connect to DB """
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)

    """creates cursor object"""
    cur = db.cursor()

    qry = "SELECT cities.id, \
            cities.name, states.name FROM cities JOIN states ON\
            states.id = cities.state_id ORDER BY cities.id ASC;"

    cur.execute(qry)

    """ Print all rows returned by query"""
    rows = cur.fetchall()

    for state in rows:
        print(state)
