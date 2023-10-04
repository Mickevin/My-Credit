import unittest
from fastapi.testclient import TestClient
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.data = {
            "age": 58,
            "job": 0,
            "marital": 1,
            "education": 2,
            "default": 0,
            "balance": 2143,
            "housing": 1,
            "loan": 0,
            "contact": 2,
            "day": 5,
            "month": 8,
            "duration": 261,
            "campaign": 1,
            "pdays": -1,
            "previous": 0,
            "poutcome": 3
        }
    
    
    def test_response(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "Hello World")


    def test_data_type(self):
        response = self.client.get("/square?number=5")
        # test du type de variable
        self.assertEquals(type(response.json()['Value']), int)
        self.assertEquals(type(response.json()['Text']), str)

    def test_predict(self):
        response = self.client.post("/predict", json=self.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "0")

        self.data['age'] = 'Bonjour'
        response = self.client.post("/predict", json=self.data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json()['detail'][0]['msg'], "value is not a valid integer")



if __name__ == '__main__':
    unittest.main()