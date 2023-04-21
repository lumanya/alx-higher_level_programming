#!/usr/bin/python3
"""
 script that fetch thats prints all cities from the databse
 - the script takes 3 arguments: <mysql username> <mysql password> <mysql db>
"""

from sys import argv
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    connect to the database and prints all cities
    <state name>: (<city id>) <city name>
    """
    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(City, State).join(State).all():
        print(f"{state.name}: ({city.id}) {city.name}")
