#!/usr/bin/python3
"""
 lists all State objects from the database
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    states = session.query(State).filter(State.name == argv[4]).all()

    if states == []:
        print("Not found")
    else:
        for state_id in states:
            print("{}".format(state_id.id))

    session.close()
