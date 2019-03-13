# services/users/project/__init__.py


from flask import Flask, jsonify


# instantiate the app
app = Flask(__name__)

# set config
app.config.from_object('project.config.DevelopmentConfig')

@app.route('/elections/ok', methods=['GET'])
def election_data():
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