#!/usr/bin/python3
"""
filter the data
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    c = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3],)
    cur = c.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    state_rows = cur.fetchall()
    for state in state_rows:
        print(state)
    cur.close()
    c.close()
