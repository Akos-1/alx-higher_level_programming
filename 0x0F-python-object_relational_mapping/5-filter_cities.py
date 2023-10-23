#!/usr/bin/python3
"""
Script that lists all cities of a given state from hbtn_0e_4_usa database
using MySQLdb to prevent SQL injection.
"""


import MySQLdb
import sys


def fetch_cities(username, password, database, state_name):
    cur = None
    db = None
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cur = db.cursor()
        query = """
                SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name LIKE BINARY %s
                ORDER BY cities.id ASC
                """
        cur.execute(query, (state_name,))

        return cur.fetchall()

    except MySQLdb.Error as e:
        print("Error: {}".format(e))
        return []

    finally:
        if cur:
            cur.close()
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    result_cities = fetch_cities(mysql_username, mysql_password,
                                 database_name, state_name)
    for city in result_cities:
        print(city)
