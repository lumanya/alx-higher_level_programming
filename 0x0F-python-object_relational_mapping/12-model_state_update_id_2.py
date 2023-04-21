#!/usr/bin/python3
"""
 script that update state on the database
 the database hbtn_0e_6_usa
 - script take 3 arguments: <mysql username> <mysql passwd> <mysql database>
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    connect to the database and get a state
    """
    db_url = "mysql+mysqldb://{}:{}@localhost/{}".\
        format(argv[1], argv[2], argv[3])
    engine = create_engine(db_url)

    # create configured session Class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"

    session.commit()
    session.close()
