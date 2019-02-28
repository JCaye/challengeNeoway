from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from model import Base

class ChallengeDB():
    engine = None

    Session = None

    def __init__(self, db_path):
        self.engine = create_engine("sqlite:///{}".format(db_path))
        Base.metadata.create_all(self.engine)

        self.Session = scoped_session(sessionmaker(bind=self.engine))

    def get_session(self):
        return self.Session()

    def close_session(self):
        self.Session.remove()
