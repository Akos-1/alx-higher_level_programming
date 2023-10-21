#!/usr/bin/python3
"""
Script that lists all states with a name starting
with N from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )
    cur = db.cursor()
    query = (
        "SELECT MIN(id), name "
        "FROM states "
        "WHERE name LIKE 'N%' "
        "GROUP BY name "
        "ORDER BY MIN(id) ASC"
    )
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
