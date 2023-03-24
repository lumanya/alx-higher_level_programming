#!/usr/bin/python3
"""
List all states with a name starting with N
parameters given to script: username, password, database
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":

    # connect to databse
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset="utf8")

    # create cursor to exec queries using SQl
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id
                ASC")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
