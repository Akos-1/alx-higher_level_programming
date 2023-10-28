#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    mysql_username, mysql_password, database_name = sys.argv[1:4]

    connection_url = (
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@'
        f'localhost:3306/{database_name}'
    )
    engine = create_engine(connection_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    session.add(new_state)
    session.commit()
