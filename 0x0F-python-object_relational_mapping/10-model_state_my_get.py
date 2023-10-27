#!/usr/bin/python3
"""
Prints the State object with the specified
name from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    mysql_username, mysql_password, database_name, state_name = argv[1:5]

    connection_url = (
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@'
        f'localhost:3306/{database_name}'
    )
    engine = create_engine(connection_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_query = session.query(State)
    state_query = state_query.filter(State.name == state_name)
    searched_state = state_query.first()
    if searched_state:
        print(searched_state.id)
    else:
        print('Not found')
    session.close()
