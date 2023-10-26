#!/usr/bin/python3
"""
Defines the State class that links to the MySQL table states.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class representing the 'states' table."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    import sys

    connection_url = (
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@'
        f'localhost:3306/{database_name}'
    )
    engine = create_engine(connection_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
