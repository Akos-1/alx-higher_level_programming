#!/usr/bin/python3
""" Prints the State object with the name passed
as an argument from the database
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    mysql_username, mysql_password, database_name = sys.argv[1:4]

    connection_url = (
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@'
        f'localhost:3306/{database_name}'
    )
    engine = create_engine(connection_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state_instance in session.query(State).order_by(State.id):
        print(state_instance.id, state_instance.name, sep=": ")
        for city_instance in state_instance.cities:
            print("    ", end="")
            print(city_instance.id, city_instance.name, sep=": ")
