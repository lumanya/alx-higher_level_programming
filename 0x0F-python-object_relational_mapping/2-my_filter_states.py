#!/usr/bin/python3
"""
 script that takes in an argument and displays all values in  the states table
 of hbtn_0e_0_usa where name matches the arguments
 script takes 4 arguments: <mysql username>, <mysql password>, <database name>,
 <state name searched>
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY \
        states.id ASC".format(argv[4])
    )
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
