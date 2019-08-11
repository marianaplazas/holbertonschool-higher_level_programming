#!/usr/bin/python3
"""
filter cities
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    name = sys.argv[1]
    pwd = sys.argv[2]
    data_name = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(user=username, passwd=pwd, db=name)
    c = db.cursor()
    cur.execute(
        "SELECT cities.name FROM cities"
        " WHERE state_id IN (SELECT states.id from states WHERE"
        " name = '{}') ORDER BY cities.id ASC".format(state))
    items = c.fetchall()
    cities = []
    for a in items:
        cities.append(a[1])
    print(", ".join(cities))
    db.close()
