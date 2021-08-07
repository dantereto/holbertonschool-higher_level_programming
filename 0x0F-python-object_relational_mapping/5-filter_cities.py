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
    cursor.execute("SELECT c.name\
    FROM cities AS c\
    JOIN states AS s\
    ON c.state_id  = s.id\
    WHERE s.name = %s\
    ORDER BY c.id", (sys.argv[4],))
    cities = []
    for data in cursor.fetchall():
        cities.append(data[0])
    print(', '.join(cities))
    cursor.close()
    db.close()
