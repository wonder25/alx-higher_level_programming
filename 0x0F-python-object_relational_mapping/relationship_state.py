#!/usr/bin/python3
"""module docs"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, MetaData
from sqlalchemy.orm import relationship


Base = declarative_base()

class State(Base):
    """Class State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')
