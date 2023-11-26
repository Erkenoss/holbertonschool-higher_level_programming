#!/usr/bin/python3
"""
 script that takes in the name of a state as an
 argument and lists all cities of that state, using
 the database hbtn_0e_4_usa
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
    state_to_search = sys.argv[4]
    query = """SELECT cities.name
            FROM cities JOIN states
            ON cities.states_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id
            """
    cursor.execute(query, (state_to_search,))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    database.close()
