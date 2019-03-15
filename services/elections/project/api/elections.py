# services/elections/project/api/elections.py


from flask import Blueprint, jsonify, request

from sqlalchemy import exc

from project.api.models import Election
from project import db

elections_blueprint = Blueprint('elections', __name__)


@elections_blueprint.route('/elections/ok', methods=['GET'])
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

@elections_blueprint.route('/elections', methods=['POST'])
def add_election():
    post_data = request.get_json()
    response_object = {
        'status': 'fail',
        'message': 'Invalid payload.'
    }
    if not post_data:
        return jsonify(response_object), 400
    general_election_date = post_data.get('general_election_date')
    primary_election_date = post_data.get('primary_election_date')
    state = post_data.get('state')
    try:
        election = Election.query.filter_by(general_election_date=general_election_date, state=state).first()
        if not election:
            db.session.add(Election(general_election_date=general_election_date, primary_election_date=primary_election_date, state=state))
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': f'{general_election_date} in {state} was added!'
            }
            return jsonify(response_object), 201
        else:
            response_object['message'] = 'Sorry. That election already exists.'
            return jsonify(response_object), 400
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(response_object), 400