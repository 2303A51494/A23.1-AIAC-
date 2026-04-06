import unittest
from app import app

class TestBillingSystem(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_billing(self):
        response = self.app.get('/api/billing')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_get_recommendations(self):
        response = self.app.get('/api/recommendations')
        self.assertEqual(response.status_code, 200)

    def test_get_fraud_detection(self):
        response = self.app.get('/api/fraud-detection')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()