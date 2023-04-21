#!/usr/bin/python3
"""
 model_state - is the module that contains class definition of State
 and instance of declarative_base
"""
from sqlalchemy import Column, Integer, String, Sequence, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """"
    State class
    attributes:
     __tablename__ (str): Link to the MySQL table states
    id (int): represents column of auto-generated, unique number intger
    name (str): column that represents column of string
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
