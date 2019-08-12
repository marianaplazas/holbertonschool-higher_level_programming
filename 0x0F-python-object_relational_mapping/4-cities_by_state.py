#!/usr/bin/python3
"""
lists all cities from the database 
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()

    c.execute("SELECT cities.id, cities.name, states.name FROM\
    cities INNER JOIN states ON cities.state_id = states.id ORDER BY\
    cities.id ASC")
    for row in c.fetchall():
        print(row)
    c.close()
    db.close()
