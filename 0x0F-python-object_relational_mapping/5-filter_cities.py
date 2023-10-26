#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: {} username password database state".format(argv[0]))
    else:
        mysql_username = argv[1]
        mysql_password = argv[2]
        database_name = argv[3]
        state_name = argv[4]

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )
        cursor = db.cursor()
        query = "SELECT cities.id, states.name, cities.name FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %s ORDER BY cities.id ASC"
        cursor.execute(query, (state_name,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        db.close()
