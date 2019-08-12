#!/usr/bin/python3
"""
filter the data
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    name = sys.argv[1]
    pwd = sys.argv[2]
    data_name = sys.argv[3]
    db = MySQLdb.connect(user=name, passwd=pwd, db=data_name, host="localhost", port=3306)
    c = db.cursor()
    c.execute("""SELECT id, name FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC""")
    items = c.fetchall()
    for a in items:
        print(a)
    c.close()
    db.close()
