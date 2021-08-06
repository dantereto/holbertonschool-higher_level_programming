#!/usr/bin/python3

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
    cursor.execute("SELECT c.id, c.name, s.name FROM cities AS c JOIN states AS s ON c.state_id  = s.id ORDER BY c.id")
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close()
