#!/usr/bin/python3
"""
Prints all City objects with their State name from the database.
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    mysql_username, mysql_password, database_name = sys.argv[1:4]
    connection_url = (
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@'
        f'localhost:3306/{database_name}'
    )
    engine = create_engine(connection_url, pool_pre_ping=True)
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    query_result = (
        session.query(State.name, City.id, City.name)
        .filter(State.id == City.state_id)
        .all()
    )

    for instance in query_result:
        print(f"{instance[0]}: ({instance[1]}) {instance[2]}")
    session.close()
