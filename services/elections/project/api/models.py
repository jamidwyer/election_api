# services/elections/project/api/models.py


from sqlalchemy.sql import func

from project import db


class Election(db.Model):  # new
    __tablename__ = 'elections'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    general_election_date = db.Column(db.String(128), nullable=True)
    primary_election_date = db.Column(db.String(128), nullable=True)
    state = db.Column(db.String(64), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, general_election_date, primary_election_date, state):
        self.general_election_date = general_election_date
        self.primary_election_date = primary_election_date
        self.state = state