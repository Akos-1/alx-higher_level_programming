#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb


import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (state_name, ))
    state = cur.fetchall()
    for s in state:
        print(s)
    cur.close()
    db.close()
