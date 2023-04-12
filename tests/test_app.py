from unittest import TestCase
from app import app


class TestApp(TestCase):
    """General tests for the flask app"""

    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_input_feature(self):
        response = self.client.get("/input-feature/")
        self.assertEqual(response.status_code, 200)

    def test_select_feature(self):
        response = self.client.get("/select-feature/")
        self.assertEqual(response.status_code, 200)

    def test_update_feature(self):
        response = self.client.get("/update-feature/")
        self.assertEqual(response.status_code, 200)

    def test_get_ddos_prediction(self):
        response = self.client.get("/get-ddos-prediction/")
        self.assertEqual(response.status_code, 200)

    def test_bulk_prediction(self):
        response = self.client.get("/bulk-predicton/")
        self.assertEqual(response.status_code, 200)

    def test_get_metrics(self):
        response = self.client.get("/metrics/")
        self.assertEqual(response.status_code, 200)

