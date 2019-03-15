# services/elections/project/tests/test_elections.py


import json
import unittest

from project.tests.base import BaseTestCase


class TestElectionService(BaseTestCase):
    """Tests for the Elections Service."""

    def test_elections(self):
        """Ensure the /ok route behaves correctly."""
        response = self.client.get('/elections/ok')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(0, data['universal_absentee'])
        self.assertIn('success', data['status'])

    def test_add_election(self):
	    """Ensure a new election can be added to the database."""
	    with self.client:
	        response = self.client.post(
	            '/elections',
	            data=json.dumps({
	                'general_election_date': 'November 3, 2020',
	                'primary_election_date': 'March 3, 2020',
	                'state': 'ok'
	            }),
	            content_type='application/json',
	        )
	        data = json.loads(response.data.decode())
	        self.assertEqual(response.status_code, 201)
	        self.assertIn('November 3, 2020 in ok was added!', data['message'])
	        self.assertIn('success', data['status'])

    def test_add_election_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty."""
        with self.client:
            response = self.client.post(
                '/elections',
                data=json.dumps({}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_election_invalid_json_keys(self):
        """
        Ensure error is thrown if the JSON object does not have a state key.
        """
        with self.client:
            response = self.client.post(
                '/elections',
                data=json.dumps({'general_election_date': 'November 3, 2020'}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_election_duplicate_email(self):
        """Ensure error is thrown if the election already exists."""
        with self.client:
            self.client.post(
                '/elections',
                data=json.dumps({
                    'general_election_date': 'November 3, 2020',
                    'state': 'ok'
                }),
                content_type='application/json',
            )
            response = self.client.post(
                '/elections',
                data=json.dumps({
                    'general_election_date': 'November 3, 2020',
                    'state': 'ok'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                'Sorry. That election already exists.', data['message'])
            self.assertIn('fail', data['status'])


if __name__ == '__main__':
    unittest.main()