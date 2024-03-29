#!/usr/bin/python3
"""module docs"""

from relationship_state import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, ForeignKey


class City(Base):
    """Class City"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
