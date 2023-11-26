#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
    )

    cursor = database.cursor()
    query = "SELECT * FROM cities ORDER BY cities.id"
    cursor.execute(query)

    for row in cursor.fetchall:
        print(row)

    cursor.close
    database.close
