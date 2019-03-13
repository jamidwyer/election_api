# services/elections/project/__init__.py


from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# instantiate the app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)

# model
class Election(db.Model):  # new
    __tablename__ = 'elections'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    general_election_date = db.Column(db.String(128), nullable=True)
    primary_election_date = db.Column(db.String(128), nullable=True)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, general_election_date):
        self.general_election_date = general_election_date

#routes
@app.route('/elections/ok', methods=['GET'])
def state_data():
    return jsonify({
        'status': 'success',
        'absentee_ballot_url': '',
        'polling_place_url': '',
        'voter_registration_url': '',
        'universal_absentee': 0,
        'elections': [
        	{
        		'general_election_date': 'November 3, 2020',
        		'primary_election_date': '',
        		'search_terms': [
        			'oklahoma 2020 election'
        		]
        	}
        ]
    })