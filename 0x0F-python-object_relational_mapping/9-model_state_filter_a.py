#!/usr/bin/python3
"""
Lists all State objects containing the letter
'a' from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    mysql_username, mysql_password, database_name = argv[1:4]

    connection_url = (
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@'
        f'localhost:3306/{database_name}'
    )
    engine = create_engine(connection_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_query = session.query(State)
    state_query = state_query.filter(State.name.like('%a%'))
    state_query = state_query.order_by(State.id)
    states_with_a = state_query.all()
    if states_with_a:
        for state in states_with_a:
            print(f'{state.id}: {state.name}')
    else:
        print('Nothing')
    session.close()
