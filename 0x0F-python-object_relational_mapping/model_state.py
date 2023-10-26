#!/usr/bin/python3
"""
Starts the link between a class and a table in the database.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    # Create the tables based on the defined classes
    Base.metadata.create_all(engine)
