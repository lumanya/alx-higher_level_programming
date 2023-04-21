#!/usr/bin/python3
"""
 Script that fetch first state in the database
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    connecting tp database and accessing data
    """
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
        format(argv[1], argv[2], argv[3])

    # create an engine
    engine = create_engine(db_url)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    state = session.query(State).first()
    if state:
        print(f'{state.id}: {state.name}')
    else:
        print("Nothing")
