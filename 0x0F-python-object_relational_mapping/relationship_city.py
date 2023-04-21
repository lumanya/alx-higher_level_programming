#!/usr/bin/python3
"""
 Script contain Class Mapping with tables
"""


from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import State, Base

class City(Base):
    """
    class definition of City with inherits from Base Class
    Args:
    id (int): unque identifier which is primary key
    name (str): name of the city
    state_id (int) foreignkey
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
