import unittest
import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.headers = {"X-API-KEY": "OGNJUdjdejrjr6258hjdfj"}
    
    def test_query(self):
        response = self.app.post("/query", json={"query": "Show total sales"}, headers=self.headers)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()