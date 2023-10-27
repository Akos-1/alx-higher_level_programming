#!/usr/bin/python3
"""
Updates the name of the State object with id=2 to 'New Mexico'.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    mysql_username, mysql_password, database_name = sys.argv[1:4]
    connection_url = (
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@'
        f'localhost:3306/{database_name}'
    )
    engine = create_engine(connection_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()
    else:
        print("Not found")
    session.close()
