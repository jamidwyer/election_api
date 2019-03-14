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
        self.assertIn(0, data['univeral_absentee'])
        self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()