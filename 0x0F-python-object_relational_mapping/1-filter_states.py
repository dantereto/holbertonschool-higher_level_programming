#!/usr/bin/python3
"""start the function"""


import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name like BINARY'N%'\
    ORDER BY id ASC")
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close()
