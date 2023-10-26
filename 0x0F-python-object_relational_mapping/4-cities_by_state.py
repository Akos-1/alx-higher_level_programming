#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
    else:
        mysql_username, mysql_password, database_name = argv[1], argv[2], argv[3]

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM cities ORDER BY cities.id ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        db.close()
