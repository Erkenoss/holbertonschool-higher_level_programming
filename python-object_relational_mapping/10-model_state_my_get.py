#!/usr/bin/python3
"""
 script that prints the State object with the name
 passed as argument from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    username, password, database = argv[1], argv[2], argv[3]
    state_to_search = argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = (
        session.query(State)
        .filter(State.name == state_to_search)
        .first()
    )

    if states:
        print(states.id)
    else:
        print("Not found")

    session.close()
