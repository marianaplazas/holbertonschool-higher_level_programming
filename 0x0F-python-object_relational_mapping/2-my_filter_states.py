#!/usr/bin/python3
"""
user filter
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ code to be executed when imported """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3],)
    c = db.cursor()
    c.execute(
        "SELECT * FROM states WHERE name LIKE BINARY"
        " '{}' ORDER BY id ASC".format(argv[4]))
    state_rows = cur.fetchall()
    for state in state_rows:
        print(state)
    c.close()
    db.close()
