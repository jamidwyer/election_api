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
	        self.assertIn('November 3, 2020 was added!', data['message'])
	        self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()