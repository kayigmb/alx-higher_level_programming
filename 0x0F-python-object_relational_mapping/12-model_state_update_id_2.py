#!/usr/bin/python3
"""
commenting
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session1 = Session()
    Base.metadata.create_all(engine)
    data = session1.query(State).filter(State.id == 2).first()
    data.name = "New Mexico"
    session1.commit()
    session1.close()
