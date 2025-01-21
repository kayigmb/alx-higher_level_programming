#!/usr/bin/python3
"""
Commentign
"""


from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    """Commentign"""

    __tablename__ = 'cities'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=Fa
