#!/usr/bin/python3
""""
my filter
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    name = sys.argv[1]
    pwd = sys.argv[2]
    data_name = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(user=name, passwd=pwd, db=data_name)
    c = db.cursor()
    c.execute("""SELECT id, name FROM states WHERE name = %s""", (state))
    items = c.fetchall()
    for a in items:
        print(a)
