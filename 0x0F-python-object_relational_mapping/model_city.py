#!/usr/bin/python3
#   Defines a City model.
#   Inherits from SQLAlchemy Base and Links to the MySQL table cities

from aqlalchemy import Column, ForeignKey, Integer, String
from aqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    """Represents a city for a MySQL database.

    Attributes:
        id (str): The city's id.
        name (aqlalchemy.integer): The city's name.
        state_id (sqlalchemy.String): The city's state id.
    """
    _tablename_ = "cities"
    id = Column(Integer, pramary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
