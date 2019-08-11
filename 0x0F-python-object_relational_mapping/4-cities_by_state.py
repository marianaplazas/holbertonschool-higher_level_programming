#!/usr/bin/python3
"""
lists all cities from the database 
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    name = sys.argv[1]
    pwd = sys.argv[2]
    data_name = sys.argv[3]
    db = MySQLdb.connect(user=name, passwd=pwd, db=data_name)
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities \
    INNER JOIN states WHERE \
    cities.state_id = states.id GROUP by cities.id ")
    items = c.fetchall()
    for a in items:
        print(a)
