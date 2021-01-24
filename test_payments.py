import unittest
import os
import sys
import json
import flask
from app import create_app, db

class TestCardCase(unittest.TestCase):
    """ card test case """

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.card = {
            'creditcardnumber': 363663636363,
            'cardholder': 'Test',
            'expirationdate': '2023/02/26',
            'securitycode': 333,
            'amount': 300
        }

        with self.app.app_context():
            db.create_all()

    def test_card_create(self):
        res = self.client().post('/processCard/', data=self.card)
        self.assertEqual(res.status_code, 200)
        self.assertIn('Test', str(res.data))

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == '__main__':
    unittest.main()