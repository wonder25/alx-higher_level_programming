#!/usr/bin/python3
"""List all State objects with letter a"""

if __name__ == '__main__':

    import sqlalchemy
    from sqlalchemy import create_engine,\
        Column, Integer, UniqueConstraint, String
    from sqlalchemy.ext.declarative import declarative_base
    from model_state import Base, State
    import sys
    from sqlalchemy.orm import sessionmaker

    USR = sys.argv[1]
    PWD = sys.argv[2]
    DB = sys.argv[3]
    HST = 'localhost'
    PRT = '3306'

    connection_url = f"mysql://{USR}:{PWD}@{HST}:{PRT}/{DB}"

    """connect to DB"""
    engine = create_engine(connection_url)

    """Session class for session objects"""
    Session = sessionmaker(bind=engine)

    """Session with database started"""
    session = Session()

    """sample query"""
    states = session.query(State).\
        filter(State.name.like('%a%')).order_by(State.id.asc())

    """Iterate through results of query"""
    for state in states:
        print(f"{state.id}: {state.name}")
