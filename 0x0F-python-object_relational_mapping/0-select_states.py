#!/usr/bin/python3
"""
selct the cities
"""

import MySQLdb
import sys

if __name__ == "__main__":
    name = sys.argv[1]
    pwd = sys.argv[2]
    data_name = sys.argv[3]
    db = MySQLdb.connect(user=name, passwd=pwd, db=data_name)
    c = db.cursor()
    c.execute("""SELECT id, name FROM states""")
    items = c.fetchall()
    for a in items:
        print(a)
