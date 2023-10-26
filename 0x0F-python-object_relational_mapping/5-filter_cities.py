#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username, mysql_password, database_name, state_name = sys.argv[1:5]

    db = MySQLdb.connect(host="localhost", user=mysql_username,
                         passwd=mysql_password, db=database_name, port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities INNER JOIN states ON
                states.id=cities.state_id WHERE states.name=%s""",
                (state_name,))
    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    print(*cities, sep=", ")
    cur.close()
    db.close()
